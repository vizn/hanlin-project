# ComfyUI Workflows

| Directory | Description | Resolution |
|-----------|-------------|------------|
| `Brochure/` | Brochure cover/inside page images | 512x768 (portrait) |
| `Poster/` | Promotional poster generation | 512x768 (portrait) |
| `Campus/` | Campus/scenery visualization | 768x512 (landscape) |
| `Logo/` | Logo and brand element designs | 512x512 (square) |
| `PPT/` | Presentation background images | 1024x768 (landscape) |

All workflows use `v1-5-pruned-emaonly.safetensors` checkpoint.
Place `{prompt}` in CLIPTextEncode nodes for dynamic prompts.
