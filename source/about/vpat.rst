:orphan:

Voluntary Product Accessibility Template (VPAT) 
===============================================

The following Voluntary Product Accessiblity Template for 508 Compliance is completed per `online guidelines from the United States Department of State <https://www.state.gov/m/irm/impact/126343.htm>`__.

- **Product Name**: Mattermost Enterprise Edition (including E10, E20 and all variants) 
- **Product Version Number**: Assessment applies to release 3.7 and later 
- **Vendor Company Name**: Mattermost, Inc. 
- **Vendor Contact Name**: Steve Green
- **Vendor Contact Telephone**: Please `contact Mattermost, Inc. <https://mattermost.com/contact-us/>`__ for telephone access. 

.. contents::
    :backlinks: top

Summary 
-------

A summary of Mattermost's support of 508 compliance standards is as follows:

Section 1194.21 Software Applications and Operating Systems                     

- **Level of Support and Supporting Features**: SUPPORTS for 10 criteria, NOT APPLICABLE for 1 criteria, SUPPORTS THROUGH EQUIVALENT FACILITATION for 1 criteria.  

- **Remarks and Explanations**: NOT APPLICABLE criteria references requirements for animations, which are not used in the product. SUPPORTS THROUGH EQUIVALENT FACILITATION references the use of a user's contrast and color settings at as an equivalent Mattermost can reproduce contrast and color settings in its web interface, though--like any web application--it does not draw them from a user's PC settings. 

Section 1194.22 Web-based Intranet and Internet information and Applications 

- **Level of Support and Supporting Features**: SUPPORTS for 5 criteria, NOT APPLICABLE for 9 criteria, SUPPORTS WITH EXCEPTION for 1 criteria, DOES NOT SUPPORT for 1 criteria. 

- **Remarks and Explanations**: SUPPORTS WITH EXCEPTION refers to having 80-90% coverage of text equivalents for every non-text element, with plans to increase coverage in 2018 release. DOES NOT SUPPORT refers to readability without associated style sheet with plan to address this issue in 2018 release. 

Section 1194.23 Telecommunications Products 

- **Level of Support and Supporting Features**: NOT APPLICABLE for 14 criteria.

- **Remarks and Explanations**: Mattermost is not a telecommunications product. 

Section 1194.24 Video and Multi-media Products 

- **Level of Support and Supporting Features**: NOT APPLICABLE for 5 criteria.

- **Remarks and Explanations**: Mattermost is not a video or multi-media product. 

Section 1194.25 Self-Contained, Closed Products 

- **Level of Support and Supporting Features**: NOT APPLICABLE for 14 criteria.

- **Remarks and Explanations**: Mattermost is not a closed prduct. 

Section 1194.26 Desktop and Portable Computers 

- **Level of Support and Supporting Features**: NOT APPLICABLE for 4 criteria.

- **Remarks and Explanations**: Mattermost is not a desktop or portable computer. 

Section 1194.31 Functional Performance Criteria 

- **Level of Support and Supporting Features**: SUPPORTS for 4 criteria, NOT APPLICABLE for 2 criteria.

- **Remarks and Explanations**: NOT APPLICABLE due to no audio-entry for Mattermost.

Section 1194.41 Information, Documentation and Support 

- **Level of Support and Supporting Features**: SUPPORTS for 3 criteria.

- **Remarks and Explanations**: No additional comments. 

Section 1194.21 Software Applications and Operating Systems - Detail 
--------------------------------------------------------------------

(a) When software is designed to run on a system that has a keyboard, product functions shall be executable from a keyboard where the function itself or the result of performing a function can be discerned textually.

- **Level of Support and Supporting Features**: SUPPORTS 

- **Remarks and Explanations**: Web-based application has extensive keyboard shortcut controls along with support for tabbed interface allowing operating using keyboard only. `Definitions of keyboard shortcuts are available in product documentation <https://docs.mattermost.com/help/messaging/keyboard-shortcuts.html>`__. Keyboard functionality is under continually review for opportunities for improvement. 

(b) Applications shall not disrupt or disable activated features of other products that are identified as accessibility features, where those features are developed and documented according to industry standards. Applications also shall not disrupt or disable activated features of any operating system that are identified as accessibility features where the application programming interface for those accessibility features has been documented by the manufacturer of the operating system and is available to the product developer.

- **Level of Support and Supporting Features**: SUPPORTS 

- **Remarks and Explanations**: Nothing to add. 

(c) A well-defined on-screen indication of the current focus shall be provided that moves among interactive interface elements as the input focus changes. The focus shall be programmatically exposed so that Assistive Technology can track focus and focus changes.

- **Level of Support and Supporting Features**: SUPPORTS 

- **Remarks and Explanations**: Nothing to add. 

(d) Sufficient information about a user interface element including the identity, operation and state of the element shall be available to Assistive Technology. When an image represents a program element, the information conveyed by the image must also be available in text.

- **Level of Support and Supporting Features**: SUPPORTS 

- **Remarks and Explanations**: Nothing to add. 

(e) When bitmap images are used to identify controls, status indicators, or other programmatic elements, the meaning assigned to those images shall be consistent throughout an application's performance.

- **Level of Support and Supporting Features**: SUPPORTS 

- **Remarks and Explanations**: Nothing to add. 

(f) Textual information shall be provided through operating system functions for displaying text. The minimum information that shall be made available is text content, text input caret location, and text attributes.

- **Level of Support and Supporting Features**: SUPPORTS 

- **Remarks and Explanations**: Nothing to add. 

(g) Applications shall not override user selected contrast and color selections and other individual display attributes.

- **Level of Support and Supporting Features**: SUPPORTS THROUGH EQUIVALENT FACILITATION

- **Remarks and Explanations**: Mattermost web application can be used in high contrast mode with support for use selected colors and contrast options. 

(h) When animation is displayed, the information shall be displayable in at least one non-animated presentation mode at the option of the user.

- **Level of Support and Supporting Features**: NOT APPLICABLE  

- **Remarks and Explanations**: No core functionality in the product relies on animations. While some loading indicators are animated, failure to load is documented in text with error messages. 

(i) Color coding shall not be used as the only means of conveying information, indicating an action, prompting a response, or distinguishing a visual element.

- **Level of Support and Supporting Features**: SUPPORTS

- **Remarks and Explanations**: No indicators rely on color alone. 

(j) When a product permits a user to adjust color and contrast settings, a variety of color selections capable of producing a range of contrast levels shall be provided.

- **Level of Support and Supporting Features**: SUPPORTS

- **Remarks and Explanations**: See `full documentation <https://docs.mattermost.com/help/settings/theme-colors.html>`__.

(k) Software shall not use flashing or blinking text, objects, or other elements having a flash or blink frequency greater than 2 Hz and lower than 55 Hz.

- **Level of Support and Supporting Features**: SUPPORTS 

- **Remarks and Explanations**: Nothing to add. 

(l) When electronic forms are used, the form shall allow people using Assistive Technology to access the information, field elements, and functionality required for completion and submission of the form, including all directions and cues.

- **Level of Support and Supporting Features**: SUPPORTS 

- **Remarks and Explanations**: Nothing to add. 

Section 1194.22 Web-based Intranet and Internet information and Applications - Detail 
-------------------------------------------------------------------------------------

(a) A text equivalent for every non-text element shall be provided (e.g., via "alt", "longdesc", or in element content).

- **Level of Support and Supporting Features**: SUPPORTS WITH EXCEPTION  

- **Remarks and Explanations**: 80-90% supported, full supported expected in 2018 release. 

(b) Equivalent alternatives for any multimedia presentation shall be synchronized with the presentation.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product. 

(c) Web pages shall be designed so that all information conveyed with color is also available without color, for example from context or markup.

- **Level of Support and Supporting Features**: SUPPORTS 

- **Remarks and Explanations**: Nothing to add. 

(d) Documents shall be organized so they are readable without requiring an associated style sheet.

- **Level of Support and Supporting Features**: DOES NOT SUPPORT 

- **Remarks and Explanations**: This functionality is planned for 2018 release. 

(e) Redundant text links shall be provided for each active region of a server-side image map.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product. 

(f) Client-side image maps shall be provided instead of server-side image maps except where the regions cannot be defined with an available geometric shape.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product. 

(g) Row and column headers shall be identified for data tables.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product. 

(h) Markup shall be used to associate data cells and header cells for data tables that have two or more logical levels of row or column headers.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product. 

(i) Frames shall be titled with text that facilitates frame identification and navigation

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product. 

(j) Pages shall be designed to avoid causing the screen to flicker with a frequency greater than 2 Hz and lower than 55 Hz.

- **Level of Support and Supporting Features**: SUPPORTS 

- **Remarks and Explanations**: Nothing to add. 

(k) A text-only page, with equivalent information or functionality, shall be provided to make a web site comply with the provisions of this part, when compliance cannot be accomplished in any other way. The content of the text-only page shall be updated whenever the primary page changes.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Compliance criteria is supported, therefore text-only page is not provided. 

(l) When pages utilize scripting languages to display content, or to create interface elements, the information provided by the script shall be identified with functional text that can be read by Assistive Technology.

- **Level of Support and Supporting Features**: SUPPORTS 

- **Remarks and Explanations**: Nothing to add. 

(m) When a web page requires that an applet, plug-in or other application be present on the client system to interpret page content, the page must provide a link to a plug-in or applet that complies with 1194.21(a) through (l).

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product. 

(n) When electronic forms are designed to be completed on-line, the form shall allow people using Assistive Technology to access the information, field elements, and functionality required for completion and submission of the form, including all directions and cues.

- **Level of Support and Supporting Features**: SUPPORTS 

- **Remarks and Explanations**: Nothing to add. 

(o) A method shall be provided that permits users to skip repetitive navigation links.

- **Level of Support and Supporting Features**: SUPPORTS

- **Remarks and Explanations**: Keyboard shortcuts can skip repetitive navigation links.

(p) When a timed response is required, the user shall be alerted and given sufficient time to indicate more time is required.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product. There are no timed responses used in the system. 

Section 1194.23 Telecommunications Products - Detail
----------------------------------------------------

(a) Telecommunications products or systems which provide a function allowing voice communication and which do not themselves provide a TTY functionality shall provide a standard non-acoustic connection point for TTYs. Microphones shall be capable of being turned on and off to allow the user to intermix speech with TTY use.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

(b) Telecommunications products which include voice communication functionality shall support all commonly used cross-manufacturer non-proprietary standard TTY signal protocols.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

(c) Voice mail, auto-attendant, and interactive voice response telecommunications systems shall be usable by TTY users with their TTYs.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

(d) Voice mail, messaging, auto-attendant, and interactive voice response telecommunications systems that require a response from a user within a time interval, shall give an alert when the time interval is about to run out, and shall provide sufficient time for the user to indicate more time is required.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

(e) Where provided, caller identification and similar telecommunications functions shall also be available for users of TTYs, and for users who cannot see displays.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

(f) For transmitted voice signals, telecommunications products shall provide a gain adjustable up to a minimum of 20 dB. For incremental volume control, at least one intermediate step of 12 dB of gain shall be provided.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

(g) If the telecommunications product allows a user to adjust the receive volume, a function shall be provided to automatically reset the volume to the default level after every use.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

(h) Where a telecommunications product delivers output by an audio transducer which is normally held up to the ear, a means for effective magnetic wireless coupling to hearing technologies shall be provided.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

(i) Interference to hearing technologies (including hearing aids, cochlear implants, and assistive listening devices) shall be reduced to the lowest possible level that allows a user of hearing technologies to utilize the telecommunications product.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

(j) Products that transmit or conduct information or communication, shall pass through cross-manufacturer, non-proprietary, industry-standard codes, translation protocols, formats or other information necessary to provide the information or communication in a usable format. Technologies which use encoding, signal compression, format transformation, or similar techniques shall not remove information needed for access or shall restore it upon delivery.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

(k)(1) Products which have mechanically operated controls or keys shall comply with the following: Controls and Keys shall be tactilely discernible without activating the controls or keys.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

(k)(2) Products which have mechanically operated controls or keys shall comply with the following: Controls and Keys shall be operable with one hand and shall not require tight grasping, pinching, twisting of the wrist. The force required to activate controls and keys shall be 5 lbs. (22.2N) maximum.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

(k)(3) Products which have mechanically operated controls or keys shall comply with the following: If key repeat is supported, the delay before repeat shall be adjustable to at least 2 seconds. Key repeat rate shall be adjustable to 2 seconds per character.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

(k)(4) Products which have mechanically operated controls or keys shall comply with the following: The status of all locking or toggle controls or keys shall be visually discernible, and discernible either through touch or sound.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

Section 1194.24 Video and Multi-media Products - Detail  
-------------------------------------------------------

a) All analog television displays 13 inches and larger, and computer equipment that includes analog television receiver or display circuitry, shall be equipped with caption decoder circuitry which appropriately receives, decodes, and displays closed captions from broadcast, cable, videotape, and DVD signals. As soon as practicable, but not later than July 1, 2002, widescreen digital television (DTV) displays measuring at least 7.8 inches vertically, DTV sets with conventional displays measuring at least 13 inches vertically, and stand-alone DTV tuners, whether or not they are marketed with display screens, and computer equipment that includes DTV receiver or display circuitry, shall be equipped with caption decoder circuitry which appropriately receives, decodes, and displays closed captions from broadcast, cable, videotape, and DVD signals.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

(b) Television tuners, including tuner cards for use in computers, shall be equipped with secondary audio program playback circuitry.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

(c) All training and informational video and multimedia productions which support the agency's mission, regardless of format, that contain speech or other audio information necessary for the comprehension of the content, shall be open or closed captioned.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

(d) All training and informational video and multimedia productions which support the agency's mission, regardless of format, that contain visual information necessary for the comprehension of the content, shall be audio described.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

(e) Display or presentation of alternate text presentation or audio descriptions shall be user-selectable unless permanent.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

Section 1194.25 Self-Contained, Closed Products - Detail 
--------------------------------------------------------

(a) Self contained products shall be usable by people with disabilities without requiring an end-user to attach Assistive Technology to the product. Personal headsets for private listening are not Assistive Technology.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

(b) When a timed response is required, the user shall be alerted and given sufficient time to indicate more time is required.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

(c) Where a product utilizes touchscreens or contact-sensitive controls, an input method shall be provided that complies with 1194.23 

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

(d) When biometric forms of user identification or control are used, an alternative form of identification or activation, which does not require the user to possess particular biological characteristics, shall also be provided.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

(e) When products provide auditory output, the audio signal shall be provided at a standard signal level through an industry standard connector that will allow for private listening. The product must provide the ability to interrupt, pause, and restart the audio at anytime.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

(f) When products deliver voice output in a public area, incremental volume control shall be provided with output amplification up to a level of at least 65 dB. Where the ambient noise level of the environment is above 45 dB, a volume gain of at least 20 dB above the ambient level shall be user selectable. A function shall be provided to automatically reset the volume to the default level after every use.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

(g) Color coding shall not be used as the only means of conveying information, indicating an action, prompting a response, or distinguishing a visual element.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

(h) When a product permits a user to adjust color and contrast settings, a range of color selections capable of producing a variety of contrast levels shall be provided.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

(i) Products shall be designed to avoid causing the screen to flicker with a frequency greater than 2 Hz and lower than 55 Hz.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

(j) (1) Products which are freestanding, non-portable, and intended to be used in one location and which have operable controls shall comply with the following: The position of any operable control shall be determined with respect to a vertical plane, which is 48 inches in length, centered on the operable control, and at the maximum protrusion of the product within the 48 inch length on products which are freestanding, non-portable, and intended to be used in one location and which have operable controls.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

(j)(2) Products which are freestanding, non-portable, and intended to be used in one location and which have operable controls shall comply with the following: Where any operable control is 10 inches or less behind the reference plane, the height shall be 54 inches maximum and 15 inches minimum above the floor.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

(j)(3) Products which are freestanding, non-portable, and intended to be used in one location and which have operable controls shall comply with the following: Where any operable control is more than 10 inches and not more than 24 inches behind the reference plane, the height shall be 46 inches maximum and 15 inches minimum above the floor.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

(j)(4) Products which are freestanding, non-portable, and intended to be used in one location and which have operable controls shall comply with the following: Operable controls shall not be more than 24 inches behind the reference plane.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

Section 1194.26 Desktop and Portable Computers - Detail 
-------------------------------------------------------

(a) All mechanically operated controls and keys shall comply with 1194.23 (k) (1) through (4).

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

(b) If a product utilizes touchscreens or touch-operated controls, an input method shall be provided that complies with 1194.23 (k) (1) through (4).

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

(c) When biometric forms of user identification or control are used, an alternative form of identification or activation, which does not require the user to possess particular biological characteristics, shall also be provided.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

(d) Where provided, at least one of each type of expansion slots, ports and connectors shall comply with publicly available industry standards

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: Functionality described in this requirement is not included in the product.

Section 1194.31 Functional Performance Criteria – Detail
--------------------------------------------------------

(a) At least one mode of operation and information retrieval that does not require user vision shall be provided, or support for Assistive Technology used by people who are blind or visually impaired shall be provided.

- **Level of Support and Supporting Features**: SUPPORTS

- **Remarks and Explanations**: Made available via browser.

(b) At least one mode of operation and information retrieval that does not require visual acuity greater than 20/70 shall be provided in audio and enlarged print output working together or independently, or support for Assistive Technology used by people who are visually impaired shall be provided.

- **Level of Support and Supporting Features**: SUPPORTS 

- **Remarks and Explanations**: Increasing Zoom level in Mattermost web app can be used to fulfill this requirement. 

(c) At least one mode of operation and information retrieval that does not require user hearing shall be provided, or support for Assistive Technology used by people who are deaf or hard of hearing shall be provided

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: There is no functionality relying on audio only. 

(d) Where audio information is important for the use of a product, at least one mode of operation and information retrieval shall be provided in an enhanced auditory fashion, or support for assistive hearing devices shall be provided.

- **Level of Support and Supporting Features**: NOT APPLICABLE 

- **Remarks and Explanations**: There is no functionality relying on audio only. 

(e) At least one mode of operation and information retrieval that does not require user speech shall be provided, or support for Assistive Technology used by people with disabilities shall be provided.

- **Level of Support and Supporting Features**: SUPPORTS 

- **Remarks and Explanations**: No speech-only interfaces in Mattermost. 

(f) At least one mode of operation and information retrieval that does not require fine motor control or simultaneous actions and that is operable with limited reach and strength shall be provided.

- **Level of Support and Supporting Features**: SUPPORTS 

- **Remarks and Explanations**: System can be operated with computer keyboard only, which can meet stated requirements when in accessibility mode. 

Section 1194.41 Information, Documentation and Support – Detail
---------------------------------------------------------------

(a) Product support documentation provided to end-users shall be made available in alternate formats upon request, at no additional charge

- **Level of Support and Supporting Features**: SUPPORTS 

- **Remarks and Explanations**: Full documentation publicly available at https://docs.mattermost.com 

(b) End-users shall have access to a description of the accessibility and compatibility features of products in alternate formats or alternate methods upon request, at no additional charge.

- **Level of Support and Supporting Features**: SUPPORTS 

- **Remarks and Explanations**: This documentation include links to all relevant accessibility and compatibility options, including theme colors and keyboard shortcuts. 

(c) Support services for products shall accommodate the communication needs of end-users with disabilities.

- **Level of Support and Supporting Features**: SUPPORTS

- **Remarks and Explanations**: Mattermost Enterprise Edition support available via email. 
