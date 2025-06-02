import os
from pathlib import Path

# Step 1: Define source and target directories
source_dir = Path("~/Projects/logseq/knowledge-graph/pages/").expanduser()
target_dir = Path("~/Projects/blogs/blog-personal/content/posts/").expanduser()

# Make sure the target directory exists
target_dir.mkdir(parents=True, exist_ok=True)

# Step 2: List all markdown files in source_dir
markdown_files = list(source_dir.glob("*.md"))

# Step 3: Print file names (for now)
for md_file in markdown_files:
    print(f"Found draft: {md_file.name}")
