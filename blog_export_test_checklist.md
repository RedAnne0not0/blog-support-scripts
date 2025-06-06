# Test Checklist for export_logseq_to_blog.py
Completed June 2025

# Blog Export Script Test Checklist

This checklist covers minimum test cases for the blog export script functionality.
Each test case has a matching dummy `.md` file. The expected result is listed below.

## ✅ Test Cases

### 1. Valid export
- [✅] **Export Test 1**: Valid front matter, should be copied.

### 2. Blog not blog-personal
- [✅] **Export Test 2**: Front matter specifies a different blog. Should be skipped silently.

### 3. Missing `slug`
- [✅] **Export Test 3**: Should report missing slug and skip.

### 4. YAML parsing error
- [✅] **Export Test 4**: Invalid YAML syntax, should raise a parsing error.

### 5. No front matter - No --verbose flag
- [✅] **Export Test 5**: Should be skipped silently.

### 6. Duplicate slug (existing file) - No `--overwrite` flag
- [✅] **Export Test 6**: A file with slug already exists. Should not overwrite.

### 7.`--verbose` flag set
- [✅] Eport Test 2: Front matter specifies a different blog. Should be skipped verbosely.
- [✅] Export Test 5: Should be skipped verbosely

### 8. Duplicate slug (existing file) - with `--overwrite` flag set
- [✅] Export Test 6: A file with slug already exists. Should overwrite.

## 🛠 Testing Notes
- Before running any tests, ensure no files are at target directory
- Create dummy target file `export-test-duplicate.md` for Test 6 and place in target directory
- Run script without flags → only Test 1 should copy
- Run with `--verbose` to see skips and reasons
- Run with `--overwrite` → Test 6 should copy over existing file
