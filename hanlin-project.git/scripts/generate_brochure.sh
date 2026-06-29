#!/bin/bash
# EducationStudio Brochure Generator
# Usage: ./generate_brochure.sh <project_name> <project_dir> [output_name]
#
# Example: ./generate_brochure.sh 中华书院 knowledge/中华书院 中华书院_华侨生保录宣传册

set -e
EDU_DIR="/root/.openclaw/workspace/EducationStudio"
PROJECT_NAME="$1"
KNOWLEDGE_DIR="$2"
OUTPUT_NAME="${3:-${PROJECT_NAME}_brochure}"

if [ -z "$PROJECT_NAME" ]; then
  echo "Usage: $0 <project_name> <knowledge_dir> [output_name]"
  echo "Example: $0 中华书院 knowledge/中华书院 中华书院_华侨生保录宣传册"
  exit 1
fi

echo "=== EducationStudio Brochure Generator ==="
echo "Project: $PROJECT_NAME"
echo "Knowledge: $EDU_DIR/$KNOWLEDGE_DIR"
echo "Output: $OUTPUT_NAME"

# Step 1: List available knowledge files
echo ""
echo "--- Knowledge Base ---"
ls -la "$EDU_DIR/$KNOWLEDGE_DIR/" 2>/dev/null || echo "WARNING: Knowledge dir not found"

# Step 2: Create output directory
mkdir -p "$EDU_DIR/outputs/Markdown"
mkdir -p "$EDU_DIR/outputs/PDF"

# Step 3: Generate brochure copy
OUTPUT_FILE="$EDU_DIR/outputs/Markdown/${OUTPUT_NAME}.md"
echo ""
echo "--- Output will be saved to ---"
echo "$OUTPUT_FILE"
echo ""
echo "=== To generate content, use: ==="
echo "1. Read knowledge files from: $EDU_DIR/$KNOWLEDGE_DIR/"
echo "2. Write brochure content to: $OUTPUT_FILE"
echo "3. Review brand guidelines from: $EDU_DIR/knowledge/品牌规范/"
echo ""
echo "Done."
