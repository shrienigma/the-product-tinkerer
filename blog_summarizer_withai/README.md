## Web Article Summarizer (OpenAI)

This project is a **command-line + web UI tool** that summarizes any web article using the **OpenAI API**.

You provide a URL, the app extracts the main article text from the page, then asks OpenAI to produce a concise summary.

---

### 1. Setup

- **Prerequisites**
  - Python 3.10+ installed
  - An OpenAI API key

- **Install dependencies**

  From the project root (`blog_summarizer_withai`):

  ```bash
  pip install -r requirements.txt
  ```

- **Set your OpenAI API key**

  On macOS / Linux (zsh or bash):

  ```bash
  export OPENAI_API_KEY="your_api_key_here"
  ```

  You can add that line to your shell profile (e.g. `~/.zshrc`) to make it persistent.

---

### 2. Usage (CLI)

Basic usage (default ~200-word summary):

```bash
python summarize_article.py "https://example.com/some-article"
```

Specify a custom maximum word count for the summary:

```bash
python summarize_article.py "https://example.com/some-article" 350
```

The script will:

- **Fetch and parse** the article from the given URL
- **Extract** the main readable content
- **Send** it to OpenAI with instructions to summarize
- **Print** the resulting summary to your terminal

---

### 3. Usage (Streamlit web app)

- **Start the app**

  ```bash
  streamlit run streamlit_app.py
  ```

- A browser window will open where you can:
  - Paste an article URL
  - Adjust max summary length and language
  - Click **Summarize** to see the result

---

### 4. How it works

- **`requests`** downloads the page.
- **`readability-lxml`** isolates the main article body.
- **`beautifulsoup4`** cleans and extracts text from the HTML.
- **`openai`** (official Python SDK) calls OpenAI Chat Completions (default: `gpt-4o-mini`) to generate the summary.

You can customize the model, style, or output language by editing `summarize_article.py`.

---

### 5. Next steps / ideas

- **Save summaries** to a local file (Markdown or PDF).
- **Batch mode**: summarize multiple URLs from a text file.
- **Add authentication / usage tracking** if you deploy this for others.


