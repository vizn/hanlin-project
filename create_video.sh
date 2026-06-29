#!/bin/bash

# PPCHA School Promotional Video Generator
# Creates a simple promotional video using FFmpeg

OUTPUT_FILE="output.mp4"
DURATION=18  # seconds

echo "Creating PPCHA School Promotional Video..."

# Create the background gradient animation
ffmpeg -f lavfi -i color=c=srgba:fc=blue:s=1920x1080:r=30 -filter_complex "format=grey" \
    -y "${OUTPUT_FILE}" 2>/dev/null

echo "Basic video created. Adding text overlays..."

# Add title overlay
ffmpeg -i "${OUTPUT_FILE}" \
    -vf "drawtext='fontcolor=white:fontsize=72:text='Philippine Pasay Chung Hua Academy':x=(width-text_w)/2:y=(height-text_h)/2'" \
    -y "${OUTPUT_FILE}"

# Add tagline overlay  
ffmpeg -i "${OUTPUT_FILE}" \
    -vf "drawtext='fontcolor=lightblue:fontsize=56:text='Help Your Child Become A Well-Rounded Individual':x=(width-text_w)/2:y=(height/1.8):fontfamily=Arial'" \
    -y "${OUTPUT_FILE}"

echo "Video created successfully!"
ls -lh ${OUTPUT_FILE}
