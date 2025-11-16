# Children of Dog

The story Antipodean has been renamed and also heavily reorganised to suit the book compiler I'm also writing.

## Structure

### Core Files
- `book.json` - Simple project configuration (title, author, etc.)
- `book.css` - CSS styling with Paged Media for print layout
- `title-page.md` - Dedicated title page content
- `book.handlebars` - Main template for assembling the book

### Content Directories
- `front-matter/` - Foreword, contents, etc. (Roman numeral pages)
- `body/` - Main chapters (Arabic numeral pages starting from 1)  
  - For simple books: direct markdown files
  - For arc-based books: arc subdirectories containing chapters
- `back-matter/` - Acknowledgments, appendices, etc. (Continued Arabic pages)

## Arc Structure Support

The compiler detects arc structure automatically:

### Simple Structure
```
body/
├── 1-Chapter-One.md
├── 2-Chapter-Two.md
└── 3-Chapter-Three.md
```
Results in: `body: [html1, html2, html3]`

### Arc Structure  
```
body/
├── arc-1-genesis/
│   ├── 1-Boot-Sequence.md
│   └── 2-Getting-Started.md
└── arc-2-domain/
    ├── 1-Deep-and-Meaningful.md
    └── 2-All-in-the-Name.md
```
Results in:
```javascript
body: [
  {
    arcName: 'genesis',
    arcTitle: 'Genesis', 
    chapters: [html1, html2]
  },
  {
    arcName: 'domain',
    arcTitle: 'Domain',
    chapters: [html3, html4]
  }
]
```

### Citation Templates
- `cite-inline.handlebars` - For inline citations like (Author, 2023)
- `cite-footnote.handlebars` - For footnote citations with superscript numbers
- `cite-chapter-endnote.handlebars` - For endnotes at chapter end
- `cite-bibliography.handlebars` - For full bibliography entries

## Key Simplifications

### Required H1 Headers
All markdown files MUST contain exactly one H1 header. Files with no H1 or multiple H1s will cause compilation errors. This eliminates complex title injection logic.

### Global Heading IDs
During compilation, every heading gets a unique ID of the form `id-x` where x is a global counter. This provides predictable anchors for cross-references and TOC generation.

### CSS String-Set
Book and chapter titles are captured using CSS `string-set` properties and displayed in running headers/footers automatically. No template variable substitution needed.

### Handlebars Assembly
The compilation process:
1. Converts each markdown file to HTML
2. Groups HTML by section (front, body, back)
3. Passes arrays to Handlebars template
4. Generates complete book HTML

## Content Sample

This test includes:
- **Genesis Arc**: Boot Sequence, Getting Started
- **Domain Arc**: Deep and Meaningful, All in the Name  
- **Independence Arc**: No Help
- **Apotheosis Arc**: Gentle Warning

Selected from the full Antipodean narrative to demonstrate the new format without creating an unwieldy test document.

## Compilation

With the new simplified compiler:
```bash
book-compiler compile --source ./
```

This would:
1. Validate all markdown files have exactly one H1
2. Convert markdown to HTML with global heading IDs
3. Build headings registry for TOC/navigation
4. Render final book using Handlebars template
5. Generate print-ready HTML with PagedJS