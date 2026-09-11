"""
Code Explainer for Students
----------------------------
A small tool that turns any code snippet into a line-by-line, plain-language
explanation — pitched at either a beginner or intermediate level.

Built for prepping lecture walkthroughs faster: paste a snippet, pick a level,
get an annotated breakdown you can read straight into a class or hand to a student.

Author: Laila Moataz
"""

import json
import os

import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

st.set_page_config(
    page_title="Code Explainer for Students",
    page_icon="📘",
    layout="wide",
)

API_KEY = os.getenv("GEMINI_API_KEY")

SAMPLE_CODE = """def get_user(id):
    return db.execute(f"SELECT * FROM users WHERE id={id}")

def calculate_average(scores):
    total = sum(scores)
    return total / len(scores)"""

LEVEL_INSTRUCTIONS = {
    "Beginner": (
        "Explain as if teaching someone who has just learned basic syntax "
        "(variables, loops, functions). Avoid jargon; when you must use a "
        "technical term, define it in plain words the first time."
    ),
    "Intermediate": (
        "Explain as if teaching someone who already codes but is new to this "
        "specific pattern, library, or concept. You can use standard technical "
        "vocabulary without redefining basics."
    ),
}


# ---------------------------------------------------------------------------
# Core logic
# ---------------------------------------------------------------------------

def build_prompt(code: str, level: str) -> str:
    return f"""You are a patient, precise programming instructor. A student pasted
this code and wants a line-by-line explanation.

{LEVEL_INSTRUCTIONS[level]}

Code:
```
{code}
```

Respond with ONLY a JSON object, no markdown fences, no preamble, in exactly this shape:
{{
  "overview": "one or two sentence plain-language summary of what this code does overall",
  "lines": [
    {{"line_number": 1, "code": "the exact line of code", "explanation": "plain language explanation of what this line does and why"}}
  ]
}}

Include every non-blank line of code as its own entry, in order. If a line is
trivial (like a closing bracket), keep the explanation short rather than
omitting the line."""


def explain_code(code: str, level: str) -> dict:
    """Call Gemini and parse the structured explanation. Raises on failure."""
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(build_prompt(code, level))
    raw = response.text.strip()
    clean = raw.replace("```json", "").replace("```", "").strip()
    return json.loads(clean)


# ---------------------------------------------------------------------------
# UI
# ---------------------------------------------------------------------------

def render_header():
    st.markdown("## 📘 Code Explainer for Students")
    st.caption(
        "Paste a snippet. Get a line-by-line explanation, pitched to the level "
        "your student is at."
    )


def render_missing_key_notice():
    st.warning(
        "No Gemini API key found. Add `GEMINI_API_KEY` to a `.env` file "
        "(see `.env.example`) or set it as an environment variable, then "
        "restart the app.",
        icon="🔑",
    )


def render_results(result: dict):
    if result.get("overview"):
        st.markdown(f"> {result['overview']}")

    st.divider()

    for item in result.get("lines", []):
        col_code, col_explanation = st.columns([1, 1.1])
        with col_code:
            st.code(
                f"{item['line_number']:>2}  {item['code']}",
                language="python",
            )
        with col_explanation:
            st.markdown(item["explanation"])


def main():
    render_header()

    if not API_KEY:
        render_missing_key_notice()
    else:
        genai.configure(api_key=API_KEY)

    level = st.radio(
        "Explain for:",
        options=["Beginner", "Intermediate"],
        horizontal=True,
    )

    code = st.text_area(
        "Your code",
        value=SAMPLE_CODE,
        height=220,
        label_visibility="collapsed",
        placeholder="Paste your code here...",
    )

    explain_clicked = st.button(
        "Explain this code",
        type="primary",
        disabled=not API_KEY or not code.strip(),
    )

    if explain_clicked:
        with st.spinner("Explaining..."):
            try:
                result = explain_code(code, level)
                render_results(result)
            except json.JSONDecodeError:
                st.error(
                    "Couldn't parse the explanation. Try again, or shorten "
                    "the snippet."
                )
            except Exception as exc:  # noqa: BLE001 - surface any API error to the user
                st.error(f"Something went wrong: {exc}")


if __name__ == "__main__":
    main()
