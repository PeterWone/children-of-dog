# Acknowledgments

You can put anything you like in the back-matter. 

As for other sections, filenames determine order of appearance.

Do not delete, rename or move any of the following project files.

- title-page.md
- front-matter/front-matter.css
- body/body.css
- back-matter/back-matter.css
- any of the handlebars files

You may have noticed the page-breaking is different in the back-matter, without the page-break: right behaviour. This is controlled by the back-matter stylesheet and you can customise it.

If you added the following, you would get a page-break:always after each contributing document. 

```css
section.front-matter-content {
    break-before: always;
}

```

## Why break-before

Why `break-before` rather than `break-after`? 

Because `break-before` is smart enough to not to put a page break right at the start. If you use `break-after`, you'll get a break after the last page.

## Content files

Content files are the Markdown files you supply. 

In the body section you could call them chapters. In the front and back matter sections this wouldn't be quite true.

In the section CSS this material is referred to as content, so the `front-matter-content` CSS class in the example above applies to each contributing document as a unit, and applies only to front-matter content files.

