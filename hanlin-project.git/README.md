# EducationStudio

AI-powered educational marketing & branding studio.  
Built on OpenClaw, ComfyUI, and Ollama (qwen3.5:9b).

## Structure

| Directory | Purpose |
|-----------|---------|
| `skills/` | Sub-agent definitions for each creative role |
| `knowledge/` | Client & domain knowledge base |
| `templates/` | Reusable document/presentation templates |
| `workflows/` | ComfyUI workflow JSONs for image generation |
| `assets/` | Shared fonts, icons, logos, photos |
| `outputs/` | Generated deliverables organized by format |

## Skills

- **CreativeDirector** — Oversees project creative direction
- **BrochureDesigner** — Creates brochure layouts (ComfyUI + Canva)
- **CopyWriter** — Writes marketing copy & brand messaging
- **PPTDesigner** — Generates presentation decks
- **EducationConsultant** — Domain expertise for education projects
- **BusinessPlanner** — Business plans & feasibility analysis
- **ComfyUIDesigner** — ComfyUI workflow specialist
- **BrandManager** — Brand guideline compliance

## Tech Stack

- **LLM**: Ollama — qwen3.5:9b (RTX 3080, CUDA 12)
- **Image Gen**: ComfyUI (192.168.199.112:8188)
- **Platform**: OpenClaw gateway (fnOS, port 18789)
