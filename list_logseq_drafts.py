import os
from pathlib import Path
import yaml  # requires PyYAML, a common YAML parser

# Step 1: Define source and target directories
source_dir = Path("~/Projects/logseq/knowledge-graph/pages/").expanduser()
target_dir = Path("~/Projects/blogs/blog-personal/content/posts/").expanduser()

# Step 2: Ensure target directory exists
target_dir.mkdir(parents=True, exist_ok=True)

# Step 3: List markdown files in source directory
markdown_files = list(source_dir.glob("*.md"))

# Step 4: Process each file
for md_file in markdown_files:
    with md_file.open("r", encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines()

    if "---" in lines:
        start = lines.index("---")
        try:
            end = lines.index("---", start + 1)
            front_matter_raw = "\n".join(lines[start + 1:end])
            body = "\n".join(lines[end + 1:])
            front_matter = yaml.safe_load(front_matter_raw)

            # Filter for blog-personal
            if front_matter.get("blog") != "blog-personal":
                continue  # Silent skip

            # ✅ Show only relevant matches
            print(f"✅ {md_file.name}: matches blog-personal")
            print(f"  Title: {front_matter.get('title')}")
            print(f"  Date: {front_matter.get('date')}")
            print(f"  Slug: {front_matter.get('slug')}")
        except ValueError:
            print(f"⚠️ {md_file.name}: Could not find second '---'")
        except yaml.YAMLError as e:
            print(f"⚠️ {md_file.name}: YAML parsing error: {e}")
    else:
        continue  # Silent skip
