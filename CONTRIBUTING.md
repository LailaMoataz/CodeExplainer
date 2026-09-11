# Contributing

This started as a small tool to speed up prepping code walkthroughs for my
own students, so it's intentionally simple. Contributions are welcome if
they keep it that way.

## Ideas that would be genuinely useful

- Support for more languages beyond Python-style snippets
- A third difficulty level ("explain like I'm teaching this concept for the
  first time ever")
- Swappable model backend (OpenAI, Claude, local models)
- Export explanations as a shareable handout (PDF/Markdown)

## Making a change

1. Fork the repo and create a branch: `git checkout -b feature/your-idea`
2. Keep changes focused — one feature or fix per pull request
3. Test locally with `streamlit run app.py` before opening a PR
4. Describe *why* the change helps, not just what it does

## Reporting a bug

Open an issue with the snippet you tried, the difficulty level you picked,
and what went wrong. If the app errored, include the message shown.
