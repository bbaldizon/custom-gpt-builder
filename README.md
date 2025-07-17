# Custom GPT Builder – MESD AI Instruction Generator

This Streamlit app helps educators and school staff design their own custom GPTs by walking through a structured, non-technical conversation. It generates draft instruction text that users can paste into ChatGPT’s “Custom GPT” builder.

## 👥 Who It’s For
MESD staff interested in building task-based, coaching, or creative GPTs tailored to their work.

## 🤖 What It Does
- Asks users about the type of GPT they want (e.g., task-specific, thought-partner, onboarding)
- Helps define:
  - What the GPT should do
  - Inputs and expected outputs
  - Tone and behavior
  - Patterns or examples to learn from
- Outputs a draft instruction they can copy/paste into ChatGPT

## 🛠️ Tech Stack
- [Streamlit](https://streamlit.io/) for the front-end interface
- [OpenAI GPT-4 API](https://platform.openai.com/docs/models/gpt-4) for GPT logic

## 🔒 Data & Privacy
- Name and email are used only for light identity tracking
- No data is stored or logged unless connected to a database or Google Sheet (optional)

## 🚀 How to Run Locally
1. Clone the repo
2. Set your OpenAI API key:
   ```bash
   export OPENAI_API_KEY=your-key-here
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```

## 📫 Contact
Questions? Contact [Ben Baldizon](mailto:bbaldizon@mesd.k12.or.us), Program Manager for AI Innovation & Capacity Building.

---
*Part of MESD’s AI capacity-building toolkit.*
