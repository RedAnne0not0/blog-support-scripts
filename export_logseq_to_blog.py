#!/usr/bin/env python3

"""
Script: export_logseq_to_blog.py
Description: Parses Logseq markdown pages for valid front matter,
             and copies those tagged for 'blog-personal' to the Hugo
             blog content directory using the front matter 'slug' as the filename.

Status: Stage 1 — Basic copy functionality with overwrite protection.
"""

# list_logseq_drafts.py — Draft Detection for Hugo Blog

# This script scans Markdown files in a Logseq graph and identifies which ones are drafts for a given blog
# It does so by parsing the YAML front matter block for a custom 'blog' field (e.g. blog-personal)
# Only files that match the configured blog name are printed with their metadata

from pathlib import Path  # pathlib is used for cleaner and more flexible file path handling
import shutil  # used for high-level file operations, such as copying
import argparse  #required for CLI arguments

import yaml  # PyYAML is used to parse YAML front matter (install with: pip install pyyaml)

# -------------------------
# Configuration
# -------------------------
# # Toggle verbose logging (non-critical skips, warnings)
# VERBOSE = False ## Deprecated now uses CLI argument

# Define the source directory: where your Logseq pages are located
SOURCE_DIR = Path("~/Projects/logseq/knowledge-graph/pages/").expanduser()
# Define the destination folder in your Hugo blog (used for export - future capability)
TARGET_DIR = Path("~/Projects/blogs/blog-personal/content/posts/").expanduser()
# Define the blog this script is targeting
TARGET_BLOG = "blog-personal"

# -------------------------
# Command-line Argument Parsing
# -------------------------
parser = argparse.ArgumentParser(description="Export blog drafts from Logseq to local blog instance.")  # sets up a parser and provides a description that will display when the script is called with `--help`
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")  # defines a --verbose flag that will optionally output detailed results of file processing, including the processing of files that should not be copied.
parser.add_argument("--overwrite", action="store_true", help="Allow overwriting existing files") # defines an --overwrite flag to optionally overwrite existing files of the same name (e.g. re-importing the same page.)
args = parser.parse_args()
# TODO: Add --target-blog argument to allow dynamic selection of blog (e.g., blog-personal, blog-multiplicite)
# This will replace the hardcoded TARGET_BLOG value.

# Use command-line argument to control verbosity
VERBOSE = args.verbose  # Assigns VERBOSE the value `args.verbose`
ALLOW_OVERWRITE = args.overwrite

# Ensure the target directory exists; if not, create it
# 'parents=True' allows creation of nested directories
# 'exist_ok=True' prevents error if the directory already exists
TARGET_DIR.mkdir(parents=True, exist_ok=True)

# -------------------------
# Front Matter Extraction
# -------------------------
# This function extracts and parses the front matter from a Markdown file
# It returns the front matter as a dictionary (if successful) and the line index where the body begins
# If parsing fails or no valid front matter is found, it returns (None, None)
def extract_front_matter(lines):
    in_front_matter = False
    front_matter_lines = []

    for i, line in enumerate(lines):
        stripped = line.strip()

        if not in_front_matter:
            if stripped == "---":
                in_front_matter = True  # Start recording front matter
                continue
            elif stripped.startswith("- ") or stripped.startswith("# "):
                # Avoid interpreting list items or headings as front matter
                break
            else:
                continue  # Ignore other lines before front matter starts

        elif stripped == "---":
            # End of front matter block
 
            # # NOTE on edge case handling (see test case 6):
            # This script intentionally does not support YAML front matter that is embedded
            # within Markdown-style bullet lists (e.g., lines like `- ---`, `- title: Foo`, etc).
            #
            # Although our parser strips leading bullet characters (`-`, `*`, etc) when scanning
            # for delimiters, lines like `- title: Foo` are still treated by PyYAML as part of
            # a list, not a mapping. This causes YAML parsing to fail, since front matter is
            # expected to be a dictionary (mapping) with key-value pairs.
            #
            # For robustness and clarity, we do not attempt to parse or normalize YAML that
            # appears to be inside a list structure. If this becomes a real-world issue,
            # one could extend the parser to:
            #   - Detect list-style front matter and try to reformat it into a mapping
            #   - Or issue a warning that such formatting is unsupported
 
            try:
                front_matter_raw = "\n".join(front_matter_lines)
                front_matter = yaml.safe_load(front_matter_raw)
                return front_matter, i  # Return parsed YAML and index of closing '---'
            except yaml.YAMLError as e:
                print(f"⚠️ {md_file.name}: YAML parsing error: {e}")  # YAML header is invalid
                return None, None

        else:
            front_matter_lines.append(line)  # Accumulate lines within front matter

    # If the loop completes without closing front matter, then no valid front matter is found
    return None, None

# -------------------------
# Main Export Logic
# -------------------------

# Get all markdown files in the Logseq pages directory
markdown_files = list(SOURCE_DIR.glob("*.md"))

# Print header to clarify output purpose
print(f"📦 Exporting blog drafts to: {TARGET_DIR}")

# ========== Main Processing Loop ==========
# Loop through each .md file and inspect front matter
for md_file in markdown_files:
#    if VERBOSE:
#        print(f"\nProcessing: {md_file.name}")

    # Read the file line by line
    with md_file.open("r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    # Attempt to extract front matter
    front_matter, end_index = extract_front_matter(lines)

    # Check that parsing worked and returned a dictionary
    if not isinstance(front_matter, dict):
        if VERBOSE:
            print(f"⚠️ {md_file.name}: Invalid or missing front matter.")
        continue

    # Skip files not meant for this specific blog
    if front_matter.get("blog") != TARGET_BLOG:
        if VERBOSE:
            print(f"⏩ {md_file.name}: Skipped (not tagged for {TARGET_BLOG})")
        continue

    # Skip files with valid fron matter but no slug
    slug = front_matter.get("slug")
    if not slug:
        print(f"⚠️ {md_file.name}: Missing 'slug' — skipping.")
        continue

    # Skip if target exists, do not overwrite by default
    target_path = TARGET_DIR / f"{slug}.md"
    if target_path.exists() and not ALLOW_OVERWRITE:
        print(f"⚠️ {md_file.name}: {target_path.name} already exists. Use --overwrite to replace it.")
        continue

    # Write content to new location
    if VERBOSE:
        print(f"✅ Exporting {md_file.name} → {target_path.name}")
    shutil.copy(md_file, target_path)

print("✅ Export complete.")

# --- former content for writing output presevered for future optional feature ---
    # Output metadata if file matches blog
    #print(f"✅  {md_file.name}: matches {TARGET_BLOG}")
    # Define keys and default fallback values
    #keys_and_defaults = {
        #"title": "<no title>",
        #"date": "<no date>",
        #"slug": "<no slug>"
    #}

    # Loop through each key and print the value (or fallback if missing)
    #for key, default in keys_and_defaults.items():
        #value = front_matter.get(key, default)
        #print(f"  {key.capitalize()}: {value}")
