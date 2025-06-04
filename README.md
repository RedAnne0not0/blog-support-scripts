# Blog Support Scripts

This repository contains Python scripts to support a Markdown-based blog workflow using [Logseq](https://logseq.com/) for drafting and [Hugo](https://gohugo.io/) for publishing.

Currently, the main script is:

## `list_logseq_drafts.py`

This script scans your Logseq graph for Markdown files with blog-style front matter and filters for a specific blog destination (e.g., `blog-personal`). It validates front matter, handles common formatting edge cases (like improperly indented or bulleted YAML blocks), and prints metadata for posts intended for export.

---

## 🔧 Features

- ✅ Scans `~/Projects/logseq/knowledge-graph/pages/` for `.md` files
- ✅ Extracts YAML front matter from each file
- ✅ Ignores improperly formatted or missing front matter
- ✅ Filters posts by the `blog:` key (default: `blog-personal`)
- ✅ Gracefully handles:
  - `- ---` errors (e.g. from Logseq list formatting)
  - Missing `slug`, `title`, or `date`
  - Invalid YAML blocks
- ✅ Supports a `--verbose` CLI flag for more detailed output during testing
- ✅ Provides clear, color-coded output for matched drafts and errors

---

## 🚀 Usage

Make sure you have [Python 3.6+](https://www.python.org/downloads/) and install the required dependency:

```bash
python3 -m pip install pyyaml
```

Then run the script from the command line:

```bash
python3 list_logseq_drafts.py
```

Use the optional `--verbose` flag for additional logging:

```bash
python3 list_logseq_drafts.py --verbose
```

By default, the script looks in:

- **Source directory**: `~/Projects/logseq/knowledge-graph/pages/`
- **Target blog**: `blog-personal`

---

## 📦 Dependencies

- [PyYAML](https://pyyaml.org/) — used to safely parse front matter from Markdown files.

Install with:

```bash
python3 -m pip install pyyaml
```

---

## 🗺️ Planned Features

- [ ] `--target-blog` CLI argument to dynamically specify blog destination
- [ ] `--copy` or `--move` flag to automatically place matching drafts in the appropriate Hugo content folder
- [ ] Export options for full or partial post content
- [ ] Dry-run and safe modes
- [ ] Error log output to file for larger batch processing
- [ ] Optional detection of Hugo formatting issues in body (e.g. Logseq block refs or unsupported markdown)

---

## 📝 Conventions

- Each blog draft must include YAML front matter bounded by `---` markers.
- Files must include the key: `blog: blog-personal` (or appropriate blog name).
- Missing or malformed front matter is skipped unless `--verbose` is used.

---

## 🗃️ Project Structure

```
blog-support-scripts/
├── list_logseq_drafts.py  # Main script
└── README.md              # You're here
```

---

## 👤 Maintainer

This project is maintained by Red Anne.

Please open issues or submit improvements if you'd like to contribute.
