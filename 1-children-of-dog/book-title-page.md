# {{book-title}}

{{#if validAuthors.length}}
{{#each validAuthors}}
by {{givenNames}} {{surname}}
{{/each}}
{{else}}
No author certificates found.

1. Put author certificate files in the root of your book project.
2. Edit the `book.json` file to set the book title.
3. For more elaborate formatting of the title page consult the manual.
{{/if}}