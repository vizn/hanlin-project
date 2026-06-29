#!/bin/bash
# EducationStudio Project Description Generator
# Usage: ./generate_project_description.sh <project_name> <knowledge_dir>
#
# Example: ./generate_project_description.sh 中华书院 knowledge/中华书院

set -e
EDU_DIR="/root/.openclaw/workspace/EducationStudio"
PROJECT_NAME="$1"
KNOWLEDGE_DIR="$2"
OUTPUT_NAME="${PROJECT_NAME}_项目说明书"

if [ -z "$PROJECT_NAME" ]; then
  echo "Usage: $0 <project_name> <knowledge_dir>"
  echo "Example: $0 中华书院 knowledge/中华书院"
  exit 1
fi

echo "=== EducationStudio Project Description Generator ==="
echo "Project: $PROJECT_NAME"

# List knowledge files
echo ""
echo "--- Knowledge Base ---"
ls -la "$EDU_DIR/$KNOWLEDGE_DIR/" 2>/dev/null

# Create output
mkdir -p "$EDU_DIR/outputs/Markdown"
OUTPUT_FILE="$EDU_DIR/outputs/Markdown/${OUTPUT_NAME}.md"
echo ""
echo "--- Output ---"
echo "$OUTPUT_FILE"
echo ""
echo "To write the project description:"
echo "1. Read: $EDU_DIR/$KNOWLEDGE_DIR/"
echo "2. Write to: $OUTPUT_FILE"
echo ""
