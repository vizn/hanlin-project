#!/bin/bash

OUTPUT="ppcha_promotion.mp4"
DURATION=30  # seconds

echo "🎬 Creating PPCHA Promotion Video..."

# Step 1: Create base blue background video (18s)
ffmpeg -y -f lavfi \
  -i "color=c=blue:s=1920x1080:r=30" \
  -t 18 \
  -c:v libx264 -crf 23 -pix_fmt yuv420p \
  "${OUTPUT}" 2>/dev/null

# Step 2: Add title overlay
ffmpeg -y -i "${OUTPUT}" \
  -filter_complex "drawtext='fontcolor=white:fontsize=72:text=\'Philippine Pasay Chung Hua Academy\':x=(w-text_w)/2:y=(h-text_h)/2:fontfile=/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf'" \
  "${OUTPUT}"

# Step 3: Add tagline
ffmpeg -y -i "${OUTPUT}" \
  -filter_complex "drawtext='fontcolor=lightblue:fontsize=56:text=\'Help Your Child Become A Well-Rounded Individual\':x=(w-text_w)/2:y=h/1.8:fontfile=/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf'" \
  "${OUTPUT}"

# Step 4: Add school highlights (Chinese)
ffmpeg -y -i "${OUTPUT}" \
  -filter_complex "drawtext='fontcolor=yellow:fontsize=52:text=\'✓ 近百年华文学校\':x=(w-text_w)/2:y=h/1.6:fontfile=/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc:'drawtext='fontcolor=yellow:fontsize=52:text=\'✓ 菲律宾教育部认证\':x=(w-text_w)/2:y=h/1.48:fontfile=/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc:'drawtext='fontcolor=yellow:fontsize=52:text=\'✓ 中英菲三语教学\':x=(w-text_w)/2:y=h/1.36:fontfile=/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc'" \
  "${OUTPUT}"

echo "✅ Video created! Size:" && ls -lh ${OUTPUT}
