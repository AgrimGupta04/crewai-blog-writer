import gradio as gr
from crew import run_crew

def interface(topic, channel, user_api_key, format_choice):
    file_path = run_crew(topic, channel, user_api_key, format_choice)

    ## Handle PDF preview or fallback txt file
    if (
        format_choice == "pdf"
        or (file_path.endswith(".txt") and "pdf_error" in file_path)
    ):
        preview = (
            "PDF preview not available.\n\n"
            "If you're seeing this message, it means `wkhtmltopdf` is not installed "
            "on the server or system running the app.\n\n"
            "The blog file has still been generated. You can download it below."
        )
    else:
        with open(file_path, "r", encoding="utf-8") as f:
            preview = f.read()

    return file_path, preview


gr.Interface(
    fn=interface,
    inputs=[
        gr.Textbox(label="Blog Topic", placeholder='e.g. What is Neural Network?'),
        gr.Textbox(label="YouTube Video URL", placeholder='e.g. https://www.youtube.com/watch?v=dQw4w9WgXcQ'),
        gr.Textbox(label="Your OpenAI API Key", type="password"),
        gr.Dropdown(
            label="Choose Output Format",
            choices=["md", "txt", "html", "pdf"],
            value="md"
        )
    ],
    outputs=[
        gr.File(label="Download Blog"),
        gr.Textbox(label="Blog Preview", lines=30, interactive=False)
    ],
    title="AI Blog Generator from YouTube",
    description="Generate multi-format blogs using CrewAI agents. See and download your blog post in Markdown, PDF, HTML, or plain text."
).launch()
