/*
Solution for the Recluse problem posed in Chapter 6 of Eloquent JavaScript

Needs to make use of the text in recluse.txt file

Approach:
- Split the file into paragraphs by cutting it at every empty line.
- Remove the '%' characters from header paragraphs and mark them as headers.
- Process the text of the paragraphs themselves, splitting them into normal 
parts, emphasised parts, and footnotes.
- Move all the footnotes to the bottom of the document, leaving numbers1 in 
their place.
- Wrap each piece into the correct HTML tags.
- Combine everything into a single HTML document.
*/

recluseFile = "";

function main() {
    // var paragraphs = recluseFile.split("\n\n");
    // console.log("Found", paragraphs.length, " Paragraphs");
    var paragraphs = map(processParagraph, recluseFile.split("\n\n");
}

function processParagraph(paragraph) {
    var header = 0;
    while (paragraph.charAt(0) == '%') {
        paragraph = paragraph.slice(1);
        header++;
    }
    return {
        type: (header == 0 ? "p" : "h"+header),
        content: splitParagraph(paragraph)};
}
    
function splitParagraph(paragraph) {
    var ends_at, segment, fncnt = 0, split = [];
    
    while (paragraph.length != 0) {
        if (paragraph.charAt(0) == '*') {
            ends_at = paragraph.indexOf('*');
            segment = paragraph.slice(1, ends_at);
            paragraph = paragraph.slice(1);
            split.push({type: 'em', content: segment});
        } else if (paragraph.charAt(0) == '{') {
            fncnt += 1;
            ends_at = paragraph.indexOf('}');
            segment = paragraph.slice(1, ends_at);
            paragraph = paragraph.slice(1);
            split.push({type: 'footnote', content: segment, idx: fncnt});
        } else if (paragraph.indexOf('*') != -1) {
            ends_at = paragraph.indexOf('*');
            segment = paragraph.slice(0, ends_at);
            split.push({type: 'normal', content: segment});
        } else if (paragraph.indexOf('{') != -1) {
            ends_at = paragraph.indexOf('{');
            segment = paragraph.slice(0, ends_at);
            split.push({type: 'normal', content: segment});
        } else {
            split.push({type: 'normal', content: paragraph});
            paragraph = '';
        }
    }
    
    return split;
}
