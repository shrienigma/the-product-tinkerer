import os
import sys
from typing import Optional

import requests
from bs4 import BeautifulSoup
from readability import Document
from openai import OpenAI


def extract_main_text(url: str) -> str:
    """
    Fetch the URL and extract the main article text using readability + BeautifulSoup.
    """
    resp = requests.get(url, timeout=20)
    resp.raise_for_status()

    doc = Document(resp.text)
    html = doc.summary()
    soup = BeautifulSoup(html, "html.parser")

    # Join all paragraphs into one text block
    paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]
    text = "\n\n".join(p for p in paragraphs if p)

    if not text:
        raise ValueError("Could not extract readable text from this page.")

    return text


def summarize_with_openai(
    text: str,
    *,
    model: str = "gpt-4o-mini",
    max_words: int = 200,
    language: str = "English",
    api_key: Optional[str] = None,
) -> str:
    """
    Call OpenAI to summarize the given text.
    """
    # Prefer an explicit key if provided (e.g. from UI), otherwise fall back to env var.
    if api_key is None:
        api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OpenAI API key is not set. Provide it explicitly or via OPENAI_API_KEY.")

    client = OpenAI(api_key=api_key)

    prompt = (
        f"Summarize the following article in clear, concise bullet points in {language}. "
        f"Keep the summary under approximately {max_words} words.\n\n"
        f"--- ARTICLE START ---\n{text}\n--- ARTICLE END ---"
    )

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that creates concise, accurate article summaries.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.4,
    )

    return completion.choices[0].message.content.strip()


def main(argv: Optional[list[str]] = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    if not argv:
        print("Usage: python summarize_article.py <article_url> [max_words]", file=sys.stderr)
        return 1

    url = argv[0]
    max_words = 200
    if len(argv) >= 2:
        try:
            max_words = int(argv[1])
        except ValueError:
            print("max_words must be an integer.", file=sys.stderr)
            return 1

    try:
        print("Fetching and extracting article text...", file=sys.stderr)
        article_text = extract_main_text(url)

        print("Generating summary with OpenAI...", file=sys.stderr)
        summary = summarize_with_openai(article_text, max_words=max_words)

        print("\n=== Summary ===\n")
        print(summary)
        return 0
    except Exception as e:  # noqa: BLE001
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())


