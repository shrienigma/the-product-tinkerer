"""
Streamlit UI for the blog/article summarizer.

This provides a PM-friendly interface around the core functions in `summarize_article.py`:
- paste a URL
- provide an OpenAI API key
- tweak summary settings
"""

import streamlit as st

from summarize_article import extract_main_text, summarize_with_openai


st.set_page_config(page_title="Web Article Summarizer", page_icon="📰", layout="centered")

st.title("📰 Web Article Summarizer")
st.write(
    "Paste a URL to any public article, enter your OpenAI API key, and get a concise summary."
)


with st.sidebar:
    st.header("Settings")
    # API key is provided per-session in the UI instead of relying on environment variables.
    api_key = st.text_input("OpenAI API key", type="password")
    max_words = st.slider(
        "Max summary length (words)",
        min_value=50,
        max_value=500,
        value=200,
        step=25,
    )
    language = st.selectbox(
        "Summary language",
        ["English", "Hindi", "Spanish", "French", "German"],
    )
    model = st.text_input("OpenAI model", value="gpt-4o-mini")


url = st.text_input("Article URL", placeholder="https://example.com/some-article")

if st.button("Summarize", type="primary"):
    if not api_key.strip():
        st.warning("Please enter your OpenAI API key in the sidebar.")
    elif not url.strip():
        st.warning("Please paste a valid article URL.")
    else:
        try:
            with st.spinner("Fetching and extracting article text..."):
                article_text = extract_main_text(url)

            with st.spinner("Generating summary with OpenAI..."):
                summary = summarize_with_openai(
                    article_text,
                    max_words=max_words,
                    language=language,
                    model=model,
                    api_key=api_key,
                )

            st.subheader("Summary")
            st.write(summary)

            with st.expander("Show extracted article text"):
                st.text_area("Article text", article_text, height=300)

        except Exception as exc:  # Broad catch is acceptable at UI boundary.
            st.error(f"Error: {exc}")


