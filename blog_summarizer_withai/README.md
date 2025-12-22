# Blog Summarizer with AI

## 🎯 What This Project Does

This project helps Product Managers quickly digest long-form content by building a web app that summarizes any article from a URL using OpenAI's API. Instead of reading entire articles, PMs can paste a link and get a concise summary in seconds. It solves the problem of information overload—a common challenge when researching competitors, industry trends, or technical documentation.

## 🧠 AI Concepts You'll Learn

- **LLM API Integration**: Learn how to call OpenAI's Chat Completions API to process text and generate summaries, understanding how to structure prompts and handle responses.
- **Prompt Engineering**: Discover how small changes to your instructions (like "summarize in bullet points" vs "write a paragraph") dramatically change the output quality and format.
- **Text Extraction & Preprocessing**: Understand how to clean messy web content using libraries like `readability-lxml` and `BeautifulSoup` to extract just the article text, filtering out navigation, ads, and other noise.

## 🛠️ What You Built

- **Web Scraping Pipeline**: A function that fetches any URL, uses readability algorithms to identify the main article content, and extracts clean text from HTML.
- **OpenAI Integration**: A flexible summarization function that accepts custom parameters (word count, language, model choice) and handles API authentication.
- **Streamlit Web UI**: A user-friendly interface where you paste URLs, enter your API key, adjust settings (summary length, language), and view results—no command line needed.
- **CLI Tool**: A command-line version for quick summaries from the terminal, useful for automation or batch processing.
- **Error Handling**: Graceful handling of invalid URLs, missing API keys, and extraction failures with clear error messages.

## 📚 Key Learnings

### Technical Insights

- **Type Hints Matter**: Python 3.9 doesn't support the `str | None` syntax (that's Python 3.10+). Using `Optional[str]` from the `typing` module ensures compatibility across Python versions—a critical lesson when building tools others will use.
- **API Key Management**: Starting with environment variables is fine for CLI tools, but moving to UI input dramatically improves UX. Users don't need to configure their shell environment—they just paste and go.
- **Web Content Extraction**: Raw HTML is messy. Using `readability-lxml` (which mimics how browsers identify main content) combined with `BeautifulSoup` for parsing gives much better results than naive regex or simple HTML parsing.

### PM Takeaways

- **User Experience Over Technical Elegance**: The initial version required setting environment variables, which is a barrier for non-technical users. Moving the API key to the UI made the tool accessible to anyone—a reminder that the "best" technical solution isn't always the most usable.
- **Cost Awareness**: OpenAI API calls cost money per token. Using `gpt-4o-mini` instead of `gpt-4` for summarization tasks provides 90% of the quality at a fraction of the cost—important when scoping AI features that will scale.
- **Prompt Engineering is Product Work**: The quality of your summary depends heavily on how you phrase the prompt. Testing different instructions (bullet points vs paragraphs, word limits, tone) is similar to A/B testing—small changes can have big impacts on user satisfaction.

## ⚠️ Gotchas & Lessons Learned

1. **Python Version Compatibility**: Used `str | None` type hints initially, which broke on Python 3.9. **Why**: The union type syntax (`|`) was introduced in Python 3.10. **Fix**: Switched to `Optional[str]` from the `typing` module, which works across Python 3.7+.

2. **Virtual Environment Not in .gitignore**: Accidentally committed the entire `.venv` folder (hundreds of files) to git. **Why**: No `.gitignore` file existed, and `git add -A` staged everything. **Fix**: Added `.gitignore` with common Python patterns (`.venv/`, `__pycache__/`, `*.pyc`). **Lesson**: Always set up `.gitignore` before your first commit.

3. **Streamlit Command Not Found**: After installing dependencies, `streamlit` command wasn't recognized. **Why**: Packages were installed in a virtual environment, but the shell wasn't activated. **Fix**: Activated the venv with `source .venv/bin/activate` before running commands. **Lesson**: Virtual environments isolate dependencies, but you need to activate them—this is actually a feature, not a bug.

## 🚀 How to Run

### Prerequisites
- Python 3.9+ installed (check with `python3 --version`)
- An OpenAI API key ([get one here](https://platform.openai.com/api-keys))

### Setup

1. **Navigate to the project directory**:
   ```bash
   cd blog_summarizer_withai
   ```

2. **Create and activate a virtual environment** (recommended):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Web App (Recommended)

```bash
streamlit run streamlit_app.py
```

A browser window will open automatically. Then:
- Enter your OpenAI API key in the sidebar
- Paste an article URL
- Adjust settings (summary length, language, model)
- Click "Summarize"

### Running the CLI Tool

```bash
# Basic usage (200-word summary)
python summarize_article.py "https://example.com/article"

# Custom word count
python summarize_article.py "https://example.com/article" 350
```

**Note**: For CLI, you'll need to set the `OPENAI_API_KEY` environment variable:
```bash
export OPENAI_API_KEY="your-api-key-here"
```

## 💡 Ideas for Extension

- **Save Summaries**: Add a "Download as Markdown" button to save summaries for later reference or sharing with your team.
- **Batch Processing**: Upload a CSV of URLs and generate summaries for all of them at once—useful for competitive research.
- **Summary History**: Store past summaries in a local database (SQLite) so you can search and revisit them.
- **Custom Prompts**: Let users write their own prompt templates (e.g., "summarize for a technical audience" or "extract key metrics and numbers").
- **Multi-language Detection**: Automatically detect the article's language and summarize in that language (or translate to your preferred language).
- **Cost Tracking**: Show token usage and estimated cost per summary to help users understand API consumption.

## 🔗 Useful Resources

- [OpenAI API Documentation](https://platform.openai.com/docs/api-reference) - Official reference for Chat Completions API, models, and parameters
- [Streamlit Documentation](https://docs.streamlit.io/) - Learn how to build interactive web apps with Python
- [BeautifulSoup Tutorial](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Guide to parsing HTML and extracting content
- [readability-lxml GitHub](https://github.com/buriy/python-readability) - Library that extracts readable content from web pages
- [OpenAI Pricing](https://openai.com/pricing) - Understand token costs and model pricing before scaling

---

**Project Details:**
- **Tech Stack**: OpenAI API, Python 3.9+, Streamlit, BeautifulSoup4, readability-lxml, requests
- **Time Invested**: ~2-3 hours (including setup, debugging, and UI improvements)
- **Difficulty Level**: Beginner-friendly (good first AI project)
