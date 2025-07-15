## crewai-blog-writer

##  AI Blog Generator from YouTube using CrewAI

Generate insightful, well-structured blog posts from YouTube videos using autonomous AI agents powered by [CrewAI](https://github.com/joaomdmoura/crewai), [LangChain](https://github.com/langchain-ai/langchain), and OpenAI models. This tool extracts meaningful insights from AI/ML-related videos and composes professional blogs in various formats.

-----------------------------------------------------------------------

##  Features

✅ Multi-agent architecture (Researcher, Writer, Editor)  
✅ Semantic search from YouTube videos  
✅ Outputs blogs in `.md`, `.html`, `.txt`, or `.pdf`  
✅ Interactive UI via [Gradio](https://gradio.app)  
✅ Supports OpenAI (gpt-3.5-turbo or gpt-4)

-------------------------------------------------------------------------

##  Example Use Case

> Input:  
> Topic: **"How GPT models work"**  
> YouTube Video: `https://www.youtube.com/watch?v=kCc8FmEb1nY`  
> Format: `Markdown`  

> Output:  
> A clean, readable blog post explaining the core concepts of GPT architecture and training.

-------------------------------------------------------------------

##  Tech Stack

- **Python 3.10+**
- [CrewAI](https://github.com/joaomdmoura/crewai)
- [LangChain](https://github.com/langchain-ai/langchain)
- [OpenAI API](https://platform.openai.com/)
- [Gradio](https://gradio.app)
- [EmbedChain](https://github.com/embedchain/embedchain)
- `pdfkit` + `wkhtmltopdf` for PDF export

-------------------------------------------------------------------

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/yt-ai-blogger.git
cd yt-ai-blogger




-----------------------------------------------------------------

### 2. Create Virtual Environment

python -m venv myenv
source myenv/bin/activate  ## or `myenv\Scripts\activate` on Windows

## Install the requirements.txt file

pip install -r requirements.txt

## Run the app
python app.py



How It Works
You provide: a topic, a valid YouTube video link, and your OpenAI API key.

Agent 1 (Researcher): Analyzes video content for key technical insights.

Agent 2 (Writer): Drafts a human-readable blog based on the research.

Agent 3 (Editor): Polishes and formats the blog using Markdown.

You get: A downloadable blog in your selected format.



Built by Agrim Gupta
Inspired by CrewAI and LangChain