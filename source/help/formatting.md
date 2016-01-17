# Formatting Text  
___

Markdown makes it easy to format messages. Type a message as you normally would, and use these rules to render it with special formatting. 

## Text Style 

You can use either `_` or `*` around a word to make it italic. Use two to make it bold.

* `_italics_` renders as _italics_
* `**bold**` renders as **bold**
* `**_bold-italic_**` renders as **_bold-italics_**
* `~~strikethrough~~` renders as ~~strikethrough~~

## Code Block 

Create a code block by indenting each line by four spaces, or by placing ``` on the line above and below your code. 

Example:

    ```
    code block
    ```

Renders as: 
```
code block
```

### Syntax Highlighting

To add syntax highlighting, type the language to be highlighted after the ``` at the beginning of the code block. 

Supported languages are:
`diff, apache, makefile, http, json, markdown, javascript, css, nginx, objectivec, python, xml, perl, bash, php, coffeescript, cs (C#), cpp (C++), sql, go, ruby, java, ini, latex`

Example:

    ``` go
    package main
    import "fmt"
    func main() {
	    fmt.Println("Hello, 世界")
    }
    ```

Renders as: 
``` go
package main
import "fmt"
func main() {
	fmt.Println("Hello, 世界")
}
```

## In-line Code

Create in-line monospaced font by surrounding it with backticks. 
```
`monospace`
```
Renders as: `monospace`.

## Links  

Create labeled links by putting the desired text in square brackets and the associated link in normal brackets. 

`[Check out Mattermost!](www.mattermost.com)`

Renders as: [Check out Mattermost!](www.mattermost.com)

## In-line Images  

Create in-line images using an `!` followed by the alt text in square brackets and the link in normal brackets. Add hover text by placing it in quotes after the link.
```
![alt text](link "hover text")

and

[![Build Status](https://travis-ci.org/mattermost/platform.svg?branch=master)](https://travis-ci.org/mattermost/platform) [![Github](https://assets-cdn.github.com/favicon.ico)](https://github.com/mattermost/platform)
```
Renders as: 

![alt text](link "hover text")

and

[![Build Status](https://travis-ci.org/mattermost/platform.svg?branch=master)](https://travis-ci.org/mattermost/platform) [![Github](https://assets-cdn.github.com/favicon.ico)](https://github.com/mattermost/platform)

## Emojis  

Emoji provided free by [Emoji One](http://emojione.com/). Check out a full list of emojis [here](http://http://emoji.codes/).

```
:smile: :+1: :sheep:
```
Renders as:
:smile: :+1: :sheep:

## Lines  

Create a line by using three `*`, `_`, or `-`.

`***` renders as: 
***

## Block quotes  

Create block quotes using `>`.

`> block quotes` renders as:
> block quotes

## Lists  

Create a list by using `*` or `-` as bullets. Indent a bullet point by adding two spaces in front of it.
```
* list item one
* list item two
  * item two sub-point
```
Renders as: 
* list item one
* list item two
  * item two sub-point

Make it an ordered list by using numbers instead:
```
1. Item one
2. Item two
```
Renders as: 
1. Item one
2. Item two

Make a task list by including square brackets:
```
- [ ] Item one
- [ ] Item two
- [x] Completed item
```
Renders as:  

![check list](https://pre-release.mattermost.com/api/v1/files/get/pspxu7bu17yttmtnzsjnqu78fe/o1nq6cmn5pfo8k8tchb4gtx4kc/nrrtpzob338smc9zk7zjdy655c/Image%20Pasted%20at%202016-0-15%2012-57.png?d=%7B%22filename%22%3A%22nrrtpzob338smc9zk7zjdy655c%2FImage%2520Pasted%2520at%25202016-0-15%252012-57.png%22%2C%22time%22%3A%221452887842154%22%7D&h=%242a%2410%24hVg%2FvdcZJwD6dEvZc4YF8.X.ea84XqLLQvHHVGLfd8W9sjcG5hZCO&t=rcgiyftm7jyrxnma1osd8zswby)

## Tables  

Create a table by placing a dashed line under the header row and separating the columns with a pipe `|`. (The columns don’t need to line up exactly for it to work). Choose how to align table columns by including colons `:` within the header row.
```
| Left-Aligned  | Center Aligned  | Right Aligned |
| :------------ |:---------------:| -----:|
| Left column 1 | this text       |  $100 |
| Left column 2 | is              |   $10 |
| Left column 3 | centered        |    $1 |
```

Renders as:

![table](https://pre-release.mattermost.com/api/v1/files/get/pspxu7bu17yttmtnzsjnqu78fe/o1nq6cmn5pfo8k8tchb4gtx4kc/xbx81knszjgz5f4bdwf4c89ykw/Image%20Pasted%20at%202016-0-15%2013-00.png?d=%7B%22filename%22%3A%22xbx81knszjgz5f4bdwf4c89ykw%2FImage%2520Pasted%2520at%25202016-0-15%252013-00.png%22%2C%22time%22%3A%221452887948032%22%7D&h=%242a%2410%24%2F528CxcUFR9bvnud2PLX9ebDn%2FJoVviuZfKtRiHcjdMaDH.tot92S&t=rcgiyftm7jyrxnma1osd8zswby)

## Headings:  

Make a heading by typing # and a space before your title. For smaller headings, use more #’s. 
```
## Large Heading
### Smaller Heading
#### Even Smaller Heading
```
Renders as: 
## Large Heading
### Smaller Heading
#### Even Smaller Heading

Alternatively, you can underline the text using `===` or `---` to create headings.
```
Heading
-------
```
Renders as:  

Large Heading
-------
