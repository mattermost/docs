#!/usr/bin/env python3
"""
Final version of enhanced PDF generation script for Mattermost documentation.

Features:
- Merges sections of the Sphinx-generated HTML docs into PDFs
- Cleans external assets (badges, web-only links, sidebar nav)
- Optimizes layout for more compact page use
- Converts inline images correctly
- Adds TOC with estimated page numbers
- Designed for use in air-gapped or offline environments

To use:
1. Clone https://github.com/mattermost/docs
2. From within the repo root:
   $ pip install -r requirements.txt
   $ make html
3. Run this script from the same directory:
   $ python generate_pdfs_final.py
"""


import weasyprint
from pathlib import Path
import sys
from bs4 import BeautifulSoup, Tag
import logging
import re

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# Define the document structure for each targeted PDF
PDF_GUIDES = {'operations': {'title': 'Mattermost Deployment & Operations Guide', 'filename': 'mattermost-deployment-operations-guide.pdf', 'sections': ['deployment-guide/', 'security-guide/', 'administration-guide/'], 'description': 'Includes deployment, security, and administration guidance'}, 'application': {'title': 'Mattermost Usage Guide', 'filename': 'mattermost-usage-guide.pdf', 'sections': ['use-case-guide/', 'end-user-guide/', 'integrations-guide/'], 'description': 'Includes use cases, end-user usage, and integrations'}}

if __name__ == "__main__":
    for name, config in PDF_GUIDES.items():
        print(f"Would generate PDF for: {config['title']} with sections: {config['sections']}")

def is_redirect_page(html_file: Path) -> bool:
    """Check if an HTML file is just a redirect page."""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for redirect indicators
        if 'meta http-equiv="refresh"' in content.lower():
            return True
        if '<title>redirect</title>' in content.lower():
            return True
        # Check if file is very small (likely just a redirect)
        if len(content.strip()) < 500 and 'url=' in content:
            return True
            
        return False
    except Exception:
        return False

def collect_html_files(build_dir: Path, sections: list) -> list:
    """Collect HTML files for specified sections, excluding redirects."""
    html_files = []
    
    for section in sections:
        section_path = build_dir / "html" / section
        if section_path.exists() and section_path.is_dir():
            # Find all HTML files in this section
            for html_file in section_path.rglob("*.html"):
                # Skip index files as they're usually navigation
                if html_file.name == "index.html":
                    continue
                    
                # Skip redirect pages
                if is_redirect_page(html_file):
                    logger.debug(f"Skipping redirect: {html_file.relative_to(build_dir)}")
                    continue
                    
                html_files.append(html_file)
                logger.debug(f"Added: {html_file.relative_to(build_dir)}")
        else:
            logger.warning(f"Section not found: {section}")
    
    return sorted(html_files)

def clean_html_content(soup: BeautifulSoup, build_dir: Path) -> BeautifulSoup:
    """Remove web-specific elements that don't belong in PDF."""
    
    # Fix image paths first - convert relative paths to absolute file:// URLs
    for img in soup.find_all('img'):
        src = img.get('src', '')
        if src and not src.startswith(('http://', 'https://', 'data:', 'file://')):
            # Convert all relative paths to absolute file:// URLs
            found = False
            
            # Try different path combinations based on common patterns
            path_attempts = []
            
            if src.startswith('../'):
                # Path like '../_images/file.png' -> this is relative to the current HTML file directory
                # If the HTML file is in build/html/collaborate/, then ../_images/ points to build/html/_images/
                clean_src = src[3:]  # Remove '../'
                path_attempts = [
                    build_dir / "html" / clean_src,  # This should be the correct path
                    build_dir / "html" / "_images" / Path(clean_src).name,
                    build_dir / "html" / "images" / Path(clean_src).name,
                    Path("source") / clean_src,
                    Path("source") / "images" / Path(clean_src).name
                ]
            elif src.startswith('./'):
                # Path like './images/file.png' -> remove './' and try locations  
                clean_src = src[2:]
                path_attempts = [
                    build_dir / "html" / clean_src,
                    build_dir / "html" / "_images" / Path(clean_src).name,
                    build_dir / "html" / "images" / Path(clean_src).name
                ]
            elif src.startswith('_images/'):
                # Path like '_images/file.png' -> direct mapping
                path_attempts = [
                    build_dir / "html" / src,
                    build_dir / "html" / "_images" / Path(src).name
                ]
            elif src.startswith('images/'):
                # Path like 'images/file.png' -> try both images and _images
                path_attempts = [
                    build_dir / "html" / src,
                    build_dir / "html" / "_images" / Path(src).name,
                    build_dir / "html" / "images" / Path(src).name
                ]
            elif src.startswith('/'):
                # Skip absolute paths that start with /
                continue
            else:
                # Other relative paths - try common locations
                filename = Path(src).name
                path_attempts = [
                    build_dir / "html" / src,
                    build_dir / "html" / "_images" / filename,
                    build_dir / "html" / "images" / filename,
                    build_dir / "html" / "_static" / "images" / filename,
                    Path("source") / "images" / filename,
                    Path("source") / "_static" / "images" / filename
                ]
            
            # Try each path until we find the image
            for attempt_path in path_attempts:
                abs_path = attempt_path.resolve()
                if abs_path.exists():
                    img['src'] = f"file://{abs_path}"
                    found = True
                    break
            
            if not found:
                logger.debug(f"Image not found: {src} (tried {len(path_attempts)} locations)")
                # Keep original src, WeasyPrint will handle the error gracefully
    
    # Remove elements that are web-specific
    selectors_to_remove = [
        # Navigation elements
        '.navbar', '.navigation', '.breadcrumb', '.toctree-wrapper',
        
        # Footers and web-specific content
        '.footer', '.site-footer', '.page-footer',
        'footer',  # Generic footer tag
        '.docs-feedback-block',  # Mattermost-specific feedback widget
        '.bottom-of-page',  # Bottom page information
        '.copyright',  # Copyright notices
        '.c-thermometer-modal__container',  # Feedback modal
        '.c-thermometer-modal__content',  # Feedback content
        '.feedback', '.feedback-form', 
        '.edit-on-github', '.edit-this-page',
        '.page-info',  # Page metadata
        '.doc-info',   # Document information
        
        # Interactive elements
        '.search', '.search-box', '#search',
        '.sidebar', '.toc-sidebar', '.right-sidebar',
        
        # Theme/UI elements
        '.theme-toggle', '.dark-mode-toggle',
        '.mobile-nav', '.hamburger',
        
        # Advertising/tracking
        '.ads', '.advertisement', '.google-ads',
        
        # Specific to Sphinx/Furo theme
        '.sidebar-drawer', '.sidebar-container',
        '.theme-toggle-container',
        '.content-icon-container',
        '.mobile-header',
        '.related-pages',
        
        # Forms and interactive widgets
        'form', '.form-group', 'input', 'button[type="submit"]',
        '.survey-form', '.rating-form',
        
        # Comments and social media
        '.comments', '.social-share', '.share-buttons',
        
        # Icons and badges
        '.icon', '.badge', '.emoji', '.fa', '.fas', '.far',
        '.material-icons', '.glyphicon',
        '.plan-badge', '.feature-badge',
        '.mm-badge-flag',  # Mattermost plan/deployment badge icons
    ]
    
    for selector in selectors_to_remove:
        for element in soup.select(selector):
            element.decompose()
    
    # Handle Mattermost plan badges specially - convert to italic text
    for badge in soup.select('.mm-plans-badge'):
        # Extract the text content and clean it up
        text_content = badge.get_text(strip=True)
        
        # Create italic paragraph for plan availability
        if 'available' in text_content.lower():
            # Clean up the text - remove "all plans" link reference
            clean_text = re.sub(r'Available on all plans', 'Available on all plans', text_content, flags=re.IGNORECASE)
            italic_p = soup.new_tag('p')
            italic_em = soup.new_tag('em')
            italic_em.string = clean_text
            italic_p.append(italic_em)
            badge.replace_with(italic_p)
        else:
            # For deployment badges, just keep the text
            p_tag = soup.new_tag('p')
            p_tag.string = text_content
            badge.replace_with(p_tag)
    
    # Handle standalone deployment badge paragraphs (those with deployment-img)
    for p in soup.find_all('p'):
        img = p.find('img', alt='deployment-img')
        if img:
            # Remove the image and clean up the text
            img.decompose()
            text_content = p.get_text(strip=True)
            if text_content:
                p.clear()
                p.string = text_content
    
    # Remove script and style tags
    for script in soup.find_all("script"):
        script.decompose()
    for style in soup.find_all("style"):
        style.decompose()
    
    # Clean up links - handle different types appropriately
    for link in soup.find_all("a", href=True):
        href = link.get("href", "")
        link_text = link.get_text().strip()
        
        if href.startswith("#"):
            # Remove internal anchor links entirely (they don't work in combined PDF)
            if link_text.lower() in ['back to top', 'top', '↑', '⬆']:
                link.decompose()  # Remove "back to top" links
            else:
                link.replace_with(link_text)  # Just keep the text
        elif href.startswith("http"):
            # For external links, be more selective about showing URLs
            if link_text and href != link_text:
                # Don't show URL if the link text is descriptive enough
                if any(word in link_text.lower() for word in ['cloud', 'self-hosted', 'download', 'sign-up', 'website', 'documentation']):
                    link.replace_with(link_text)  # Just keep descriptive text
                else:
                    link.string = f"{link_text} ({href})"  # Show URL for unclear links
            else:
                link.replace_with(href)  # Fallback to URL
        else:
            # Local links - just keep the text
            if link_text:
                link.replace_with(link_text)
    
    # Additional content-based footer removal
    # Remove any remaining elements containing typical footer text
    for element in soup.find_all(string=re.compile(r'(Made with|Built with|Copyright|©|Sphinx|Furo|pradyunsg)', re.IGNORECASE)):
        parent = element.parent
        if parent and parent.name in ['div', 'p', 'span', 'footer']:
            parent.decompose()
    
    # Clean up Sphinx directive artifacts
    text_content = str(soup)
    
    # Remove common Sphinx directive artifacts
    sphinx_artifacts = [
        'plans-img', 'deployment-img', 'plans-img-yellow', 'deployment-img-yellow',
        '|plans-img|', '|deployment-img|', '|plans-img-yellow|', '|deployment-img-yellow|'
    ]
    
    for artifact in sphinx_artifacts:
        text_content = text_content.replace(artifact, '')
    
    # Remove paragraph symbols and other unwanted characters
    text_content = re.sub(r'¶', '', text_content)  # Remove paragraph symbols
    text_content = re.sub(r'&para;', '', text_content)  # Remove HTML paragraph entities
    text_content = re.sub(r'&#182;', '', text_content)  # Remove numeric paragraph entities
    
    # Remove common icon placeholders and artifacts
    text_content = re.sub(r'[\u2328\ufe0f]', '', text_content)  # Remove keyboard emoji
    text_content = re.sub(r'[\U0001f4bb]', '', text_content)  # Remove computer emoji  
    text_content = re.sub(r'[\u26a1]', '', text_content)  # Remove lightning emoji
    text_content = re.sub(r'[\u2699\ufe0f]', '', text_content)  # Remove gear emoji
    text_content = re.sub(r'[\U0001f5a5\ufe0f]', '', text_content)  # Remove desktop emoji
    
    # Remove other common unicode artifacts
    text_content = re.sub(r'[\u200b-\u200d\ufeff]', '', text_content)  # Remove zero-width characters
    
    # Clean up extra whitespace and newlines
    text_content = re.sub(r'\\n', ' ', text_content)  # Replace literal \n with space
    text_content = re.sub(r'\s+', ' ', text_content)  # Collapse multiple spaces
    text_content = re.sub(r'<p>\s*</p>', '', text_content)  # Remove empty paragraphs
    
    return BeautifulSoup(text_content, 'html.parser')

def clean_title_text(title: str) -> str:
    """Clean title text by removing unwanted characters and symbols."""
    # Remove paragraph symbols and other unwanted characters
    title = re.sub(r'¶', '', title)  # Remove paragraph symbols
    title = re.sub(r'&para;', '', title)  # Remove HTML paragraph entities
    title = re.sub(r'&#182;', '', title)  # Remove numeric paragraph entities
    
    # Clean up extra whitespace
    title = re.sub(r'\s+', ' ', title)  # Collapse multiple spaces
    title = title.strip()
    
    return title

def extract_page_title(soup: BeautifulSoup) -> str:
    """Extract the main page title."""
    # Try different selectors for the main title
    title_selectors = [
        'h1', '.document h1', 'main h1', 
        '.content h1', 'article h1',
        '.section h1', '#content h1'
    ]
    
    for selector in title_selectors:
        title_elem = soup.select_one(selector)
        if title_elem:
            title = title_elem.get_text().strip()
            return clean_title_text(title)
    
    # Fallback to HTML title
    title_elem = soup.find('title')
    if title_elem:
        title = title_elem.get_text().strip()
        # Clean up Sphinx-style titles
        if ' — ' in title:
            title = title.split(' — ')[0]
        return clean_title_text(title)
    
    return "Untitled"

def analyze_document_structure(html_files: list, build_dir: Path) -> list:
    """Analyze document structure to create hierarchical TOC with page estimates."""
    toc_items = []
    page_counter = 3  # Start after cover page and TOC
    
    current_section = None
    section_items = []
    
    for i, html_file in enumerate(html_files):
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
                soup = BeautifulSoup(content, 'html.parser')
            
            title = extract_page_title(soup)
            rel_path = html_file.relative_to(build_dir / "html")
            section = rel_path.parts[0] if rel_path.parts else 'General'
            
            # Estimate pages based on content length (rough approximation)
            text_length = len(soup.get_text())
            estimated_pages = max(1, text_length // 3000)  # ~3000 chars per page
            
            anchor_id = f"section_{i}"
            
            item = {
                'title': title,
                'path': str(rel_path),
                'section': section,
                'anchor': anchor_id,
                'page': page_counter,
                'estimated_pages': estimated_pages,
                'level': 1  # Default level
            }
            
            # Determine hierarchy level based on file path depth and title
            path_depth = len(rel_path.parts) - 1  # Subtract 1 for filename
            if title.lower().startswith(('overview', 'introduction', 'getting started')):
                item['level'] = 1
            elif path_depth > 1 or any(word in title.lower() for word in ['configuration', 'settings', 'advanced']):
                item['level'] = 2
            else:
                item['level'] = 1
            
            toc_items.append(item)
            page_counter += estimated_pages
            
        except Exception as e:
            logger.warning(f"Could not analyze {html_file}: {e}")
    
    return toc_items

def create_table_of_contents(html_files: list, build_dir: Path) -> tuple:
    """Generate a hierarchical table of contents with page numbers."""
    toc_items = analyze_document_structure(html_files, build_dir)
    
    # Generate enhanced TOC HTML
    toc_html = """
    <div class="table-of-contents">
        <h1>Table of Contents</h1>
        <div class="toc-structure">
    """
    
    current_section = None
    for item in toc_items:
        section = item['section']
        
        # Start new section if needed
        if section != current_section:
            if current_section is not None:
                toc_html += "        </div>\n"  # Close previous section
            
            section_name = section.replace('-', ' ').replace('_', ' ').title()
            toc_html += f"""
        <div class="toc-section">
            <h2 class="toc-section-title">{section_name}</h2>
            <div class="toc-section-content">
"""
            current_section = section
        
        # Add TOC entry with proper indentation and page number
        indent_class = f"toc-level-{item['level']}"
        toc_html += f"""
            <div class="toc-entry {indent_class}">
                <a href="#{item['anchor']}" class="toc-link">
                    <span class="toc-title">{item['title']}</span>
                    <span class="toc-dots"></span>
                    <span class="toc-page">{item['page']}</span>
                </a>
            </div>
"""
    
    if current_section is not None:
        toc_html += "        </div>\n"  # Close last section
    
    toc_html += """
        </div>
    </div>
    """
    
    return toc_html, toc_items

def create_enhanced_combined_html(html_files: list, title: str, output_dir: Path, build_dir: Path) -> Path:
    """Create an enhanced combined HTML file with TOC and clean formatting."""
    combined_file = output_dir / f"enhanced_{title.lower().replace(' ', '_')}.html"
    
    # Enhanced CSS for professional PDF output
    enhanced_css = """
        @page {
            size: A4;
            margin: 1in;
            @top-center {
                content: string(doctitle);
                font-size: 10pt;
                color: #666;
            }
            @bottom-center {
                content: "Page " counter(page) " of " counter(pages);
                font-size: 9pt;
                color: #666;
            }
        }
        
        @page :first {
            @top-center { content: none; }
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            font-size: 11pt;
        }
        
        .document-title {
            string-set: doctitle content();
            font-size: 28pt;
            color: #1e40af;
            text-align: center;
            margin-bottom: 2rem;
            page-break-after: always;
        }
        
        .table-of-contents {
            page-break-after: always;
        }
        
        .table-of-contents h1 {
            font-size: 22pt;
            color: #1e40af;
            border-bottom: 2px solid #1e40af;
            padding-bottom: 0.5rem;
            margin-bottom: 1.5rem;
        }
        
        .toc-structure {
            margin-top: 1rem;
        }
        
        .toc-section {
            margin-bottom: 2rem;
        }
        
        .toc-section-title {
            font-size: 14pt;
            color: #1e40af;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 0.75rem;
            border-bottom: 1px solid #e5e7eb;
            padding-bottom: 0.25rem;
        }
        
        .toc-section-content {
            margin-left: 0.5rem;
        }
        
        .toc-entry {
            margin-bottom: 0.4rem;
            page-break-inside: avoid;
        }
        
        .toc-link {
            display: flex;
            align-items: baseline;
            text-decoration: none;
            color: #374151;
            padding: 0.3rem 0;
            border-bottom: 1px dotted #e5e7eb;
        }
        
        .toc-link:hover {
            color: #1e40af;
            background-color: #f8fafc;
        }
        
        .toc-title {
            flex-shrink: 0;
            font-weight: 400;
        }
        
        .toc-dots {
            flex-grow: 1;
            border-bottom: 1px dotted #9ca3af;
            margin: 0 0.5rem;
            height: 1px;
            margin-bottom: 0.25rem;
        }
        
        .toc-page {
            flex-shrink: 0;
            font-weight: 600;
            color: #6b7280;
            min-width: 2rem;
            text-align: right;
        }
        
        .toc-level-1 {
            margin-left: 0;
        }
        
        .toc-level-2 {
            margin-left: 1rem;
        }
        
        .toc-level-2 .toc-title {
            font-size: 10pt;
            color: #6b7280;
        }
        
        h1, h2, h3, h4, h5, h6 {
            color: #1f2937;
            page-break-after: avoid;
            margin-top: 1.5rem;
            margin-bottom: 0.75rem;
        }
        
        h1 {
            font-size: 20pt;
            border-bottom: 2px solid #1e40af;
            padding-bottom: 0.5rem;
            page-break-before: always;
        }
        
        h1:first-of-type {
            page-break-before: avoid;
        }
        
        h2 {
            font-size: 16pt;
            color: #374151;
            margin-top: 2rem;
        }
        
        h3 {
            font-size: 14pt;
            color: #4b5563;
        }
        
        h4, h5, h6 {
            font-size: 12pt;
            color: #6b7280;
        }
        
        p {
            margin-bottom: 0.75rem;
            text-align: justify;
            orphans: 2;
            widows: 2;
        }
        
        ul, ol {
            margin-bottom: 0.75rem;
            padding-left: 1.5rem;
        }
        
        li {
            margin-bottom: 0.25rem;
        }
        
        pre, code {
            font-family: 'SF Mono', 'Monaco', 'Cascadia Code', monospace;
            font-size: 9pt;
        }
        
        pre {
            background-color: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 6px;
            padding: 1rem;
            overflow-x: auto;
            page-break-inside: avoid;
            white-space: pre-wrap;
            word-wrap: break-word;
        }
        
        code {
            background-color: #f1f5f9;
            padding: 0.125rem 0.25rem;
            border-radius: 3px;
            color: #dc2626;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 1rem 0;
            page-break-inside: avoid;
            font-size: 10pt;
        }
        
        th, td {
            border: 1px solid #d1d5db;
            padding: 0.5rem;
            text-align: left;
            vertical-align: top;
        }
        
        th {
            background-color: #f9fafb;
            font-weight: 600;
            color: #374151;
        }
        
        img {
            max-width: 100%;
            height: auto;
            page-break-inside: avoid;
            display: block;
            margin: 1rem auto;
        }
        
        blockquote {
            border-left: 4px solid #3b82f6;
            padding-left: 1rem;
            margin: 1rem 0;
            font-style: italic;
            color: #4b5563;
        }
        
        .section-break {
            page-break-before: always;
        }
        
        .note, .warning, .tip {
            padding: 1rem;
            margin: 1rem 0;
            border-radius: 6px;
            page-break-inside: avoid;
        }
        
        .note {
            background-color: #eff6ff;
            border-left: 4px solid #3b82f6;
        }
        
        .warning {
            background-color: #fef2f2;
            border-left: 4px solid #ef4444;
        }
        
        .tip {
            background-color: #f0fdf4;
            border-left: 4px solid #10b981;
        }
    """
    
    # Create combined HTML structure
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>{enhanced_css}</style>
</head>
<body>
    <h1 class="document-title">{title}</h1>
    <p style="text-align: center; font-style: italic; margin-bottom: 2rem;">
        Generated from Mattermost Documentation
    </p>
"""
    
    # Add Table of Contents
    toc_html, toc_items = create_table_of_contents(html_files, build_dir)
    html_content += toc_html
    
    # Process each HTML file
    for i, html_file in enumerate(html_files):
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')
            
            # Clean the content
            soup = clean_html_content(soup, build_dir)
            
            # Extract the main content
            main_content = None
            for selector in ['main', '.main', '#main', 'article', '.document', '.content']:
                main_content = soup.select_one(selector)
                if main_content:
                    break
            
            if not main_content:
                main_content = soup.find('body')
            
            if main_content:
                # Add section break for all but the first file
                if i > 0:
                    html_content += '<div class="section-break"></div>\n'
                
                # Add anchor for TOC linking
                anchor_id = toc_items[i]['anchor']
                page_title = clean_title_text(toc_items[i]['title'])  # Clean the title
                html_content += f'<div id="{anchor_id}"><h1>{page_title}</h1></div>\n'
                
                # Add the cleaned content (without the original h1 to avoid duplication)
                content_str = str(main_content)
                # Remove the first h1 if it exists to avoid duplication
                soup_content = BeautifulSoup(content_str, 'html.parser')
                first_h1 = soup_content.find('h1')
                if first_h1:
                    first_h1.decompose()
                
                html_content += str(soup_content)
                logger.debug(f"Processed: {html_file.name}")
            else:
                logger.warning(f"No content found in: {html_file}")
                
        except Exception as e:
            logger.error(f"Error processing {html_file}: {e}")
    
    html_content += """
</body>
</html>"""
    
    # Write the combined HTML file
    with open(combined_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    logger.info(f"Created enhanced combined HTML: {combined_file}")
    return combined_file

def generate_enhanced_pdf(guide_name: str, guide_config: dict, build_dir: Path, output_dir: Path) -> bool:
    """Generate an enhanced PDF with improved formatting."""
    logger.info(f"\\n=== Generating Enhanced {guide_config['title']} ===")
    
    # Collect HTML files for this guide
    html_files = collect_html_files(build_dir, guide_config['sections'])
    
    if not html_files:
        logger.error(f"No HTML files found for {guide_name}")
        return False
    
    logger.info(f"Found {len(html_files)} HTML files")
    
    # Create enhanced combined HTML file
    try:
        combined_html = create_enhanced_combined_html(
            html_files, 
            guide_config['title'], 
            output_dir,
            build_dir
        )
        
        # Generate PDF with better options
        pdf_path = output_dir / guide_config['filename']
        logger.info(f"Converting to enhanced PDF: {pdf_path}")
        
        html_doc = weasyprint.HTML(filename=str(combined_html))
        html_doc.write_pdf(
            str(pdf_path),
            presentational_hints=True,
            optimize_images=True
        )
        
        # Get file size
        size_kb = pdf_path.stat().st_size / 1024
        logger.info(f"✅ Success! Created enhanced {pdf_path} ({size_kb:.1f} KB)")
        
        # Clean up temporary HTML file
        combined_html.unlink()
        
        return True
        
    except Exception as e:
        logger.error(f"❌ Error generating enhanced PDF for {guide_name}: {e}")
        return False

def main():
    """Main function to generate enhanced PDF guides."""
    # Check if HTML build exists
    build_dir = Path("build").resolve()  # Make it absolute immediately
    if not (build_dir / "html").exists():
        logger.error("HTML build not found. Run 'gmake html' first.")
        sys.exit(1)
    
    # Create output directory
    output_dir = Path("pdfs").resolve()
    output_dir.mkdir(exist_ok=True)
    
    logger.info("🚀 Starting Enhanced PDF generation for Mattermost Documentation")
    logger.info(f"Build directory: {build_dir.absolute()}")
    logger.info(f"Output directory: {output_dir.absolute()}")
    
    # Generate each guide
    results = {}
    for guide_name, guide_config in PDF_GUIDES.items():
        results[guide_name] = generate_enhanced_pdf(guide_name, guide_config, build_dir, output_dir)
    
    # Summary
    logger.info("\\n" + "="*60)
    logger.info("📊 Enhanced PDF Generation Summary")
    logger.info("="*60)
    
    successful = 0
    for guide_name, success in results.items():
        guide_config = PDF_GUIDES[guide_name]
        status = "✅ SUCCESS" if success else "❌ FAILED"
        logger.info(f"{status}: {guide_config['title']}")
        if success:
            successful += 1
    
    logger.info(f"\\n📈 Generated {successful}/{len(PDF_GUIDES)} enhanced PDF guides successfully")
    
    if successful > 0:
        logger.info(f"\\n📁 Enhanced PDF files available in: {output_dir.absolute()}")
        for guide_name, success in results.items():
            if success:
                guide_config = PDF_GUIDES[guide_name]
                pdf_path = output_dir / guide_config['filename']
                size_kb = pdf_path.stat().st_size / 1024
                logger.info(f"  • {guide_config['filename']} ({size_kb:.1f} KB)")

if __name__ == "__main__":
    main()