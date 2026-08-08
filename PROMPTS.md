# AI-Usage Log & Prompt History

This document logs the core prompts and iterative conversational steps used with the AI collaborator to build the Cinematic AI Technical Exit Interview platform.

## Phase 1: Core Functionality & Backend Architecture
- **Prompt:** "Help me structure a FastAPI backend that handles interview session states, tracks question counts up to a target of 8, and integrates with LLM endpoints."
- **Result:** Created `main.py` managing state, session IDs, and conversational flow.

## Phase 2: Frontend Integration & Basic UI
- **Prompt:** "Build a Streamlit frontend (`app.py`) that connects to the FastAPI backend, renders message history, and shows live progress in a sidebar."
- **Result:** Established the initial Streamlit chat interface and session state management.

## Phase 3: Cinematic Cyberpunk Overhaul & Styling
- **Prompt:** "It looks very simple and boring. I want it more cinematic, attractive, eye-catching, full of life, with a high-end dark theme, sci-fi HUD elements, custom fonts, and high-contrast text visibility."
- **Result:** Injected custom CSS, keyframe animations, Google Fonts (`Orbitron`, `Share Tech Mono`), matte-black HUD cards, and glowing reactor indicators.
