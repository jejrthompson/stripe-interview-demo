#!/bin/bash

# Generate PNG diagrams from all .mmd files in ./diagrams

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
CONFIG_FILE="$PROJECT_ROOT/mermaid.config.json"

find "$PROJECT_ROOT/diagrams" -name "*.mmd" | while read -r mmd_file; do
    png_file="${mmd_file%.mmd}.png"
    echo "Generating: $png_file"
    mmdc -i "$mmd_file" -o "$png_file" -c "$CONFIG_FILE"
done

echo "Done!"
