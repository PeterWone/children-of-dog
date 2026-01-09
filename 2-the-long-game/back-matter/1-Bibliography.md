# Bibliography Examples

This page demonstrates both bibliography modes available in the Book Compiler.

## Cited References Only

This section shows only the works that were actually cited in the text:

```bibliography
mode: references
```

## Further Reading

This section shows all available references, whether cited or not:

```bibliography
mode: further-reading
```

---

### About Bibliography Modes

*The bibliography is automatically generated based on the mode setting:*

- **`mode: references`** - Shows only works that were actually cited in the text (Orwell's 1984 in this example)
- **`mode: further-reading`** - Shows all references from `references.json` (both Orwell's 1984 and Huxley's Brave New World)

*Citations are created using the `❲cіte|id|excerpt❳` syntax in your markdown files, and bibliography entries are formatted according to the citation scheme specified in your `book.json` configuration.*

*To add references, edit the `references.json` file in your project root. The Book Compiler supports multiple citation styles including Harvard, APA, MLA, Chicago, Oxford (OSCOLA), and AGLC.*
