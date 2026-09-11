# 📘 Code Explainer for Students

A small tool that turns any code snippet into a line-by-line, plain-language
explanation — pitched at either a beginner or intermediate level.

I built this because I kept doing the same thing by hand before every lecture:
take a code example, walk through it line by line, and adjust the depth of
explanation depending on who's in the room. This automates the first draft of
that, so I can spend prep time on the parts that actually need a human — the
analogies, the common mistakes, the "why does this matter" framing.

<!-- Add a screenshot or short GIF of the app here before publishing.
     A quick way: run the app, record your screen pasting a snippet in,
     save as demo.gif, and reference it like this:
     ![Demo](assets/demo.gif) -->

---

## What it does

- Paste any code snippet
- Choose **Beginner** (jargon-free, terms defined on first use) or
  **Intermediate** (assumes the student already codes, just not this pattern)
- Get back a one-line overview plus an explanation for every line, side by
  side with the code itself

## Why it's built this way

- **One model call, structured output.** The prompt asks for JSON directly
  rather than free-form text, so the explanation renders as a clean table
  instead of a wall of prose.
- **Two levels, not a slider.** A continuous "difficulty" slider sounds nice
  but doesn't actually change what the model does. Two concrete instructions
  — "define jargon" vs. "assume they can code" — produce genuinely different
  output.
- **Streamlit, not a custom frontend.** The goal was a tool I'd actually use
  before Tuesday's lecture, not a UI project. Streamlit gets out of the way.

## Getting started

### 1. Clone and install

```bash
git clone https://github.com/LailaMoataz/code-explainer.git
cd code-explainer
pip install -r requirements.txt
```

### 2. Add your API key

Get a free Gemini API key at [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey),
then:

```bash
cp .env.example .env
# open .env and paste your key in
```

### 3. Run it

```bash
streamlit run app.py
```

It opens at `http://localhost:8501`.

## Project structure

```
code-explainer/
├── app.py              # the whole app — UI + prompt + API call
├── requirements.txt
├── .env.example
├── .gitignore
├── LICENSE
└── CONTRIBUTING.md
```

## Roadmap

- [ ] Export an explanation as a shareable handout (Markdown/PDF)
- [ ] Support a third level for total first-timers
- [ ] Let students highlight a single line instead of reading the whole list
- [ ] Deploy a public demo (Streamlit Community Cloud or Hugging Face Spaces)

Contributions welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

## About

I teach AI and deep learning (Assistant Lecturer, PhD candidate researching
explainable deep learning for medical imaging) and build small practical
tools like this one alongside my course material.

- 🎥 YouTube: **[add your channel link]**
- 🎓 Course (build a chatbot with OpenAI/Gemini APIs): **[add your Udemy link]**
- 💼 LinkedIn: **[add your LinkedIn link]**

## License

MIT — see [LICENSE](LICENSE).
