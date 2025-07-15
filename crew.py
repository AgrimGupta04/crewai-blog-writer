from crewai import Crew, Process
from agents import create_agents
from tasks import create_tasks
from tools import get_yt_tool

import markdown2
import pdfkit
import os


def convert_blog_file(md_path, output_format):
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    filename = "new-blog-post." + output_format

    if output_format == "md":
        return md_path

    elif output_format == "txt":
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        return filename

    elif output_format == "html":
        html = markdown2.markdown(content)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)
        return filename

    elif output_format == "pdf":
        html = markdown2.markdown(content)
        with open("temp.html", "w", encoding="utf-8") as f:
            f.write(html)
        try:
            pdfkit.from_file("temp.html", filename)
            return filename
        except OSError:
            error_file = "pdf_error.txt"
            with open(error_file, "w", encoding="utf-8") as errfile:
                errfile.write("PDF conversion failed. Please make sure 'wkhtmltopdf' is installed.\n")
                errfile.write("Download from: https://wkhtmltopdf.org/downloads.html")
            return error_file

    else:
        raise ValueError("Unsupported format")


def run_crew(topic: str, video_url: str, user_api_key: str, output_format: str):
    try:
        video_url = video_url.strip()
        print(f"[DEBUG] YouTube URL used: {video_url}")

        yt_tool = get_yt_tool(video_url=video_url, user_api_key=user_api_key)

        researcher, writer, editor = create_agents(yt_tool, user_api_key)
        task1, task2, task3 = create_tasks(researcher, writer, editor)

        ## Launching Crew
        crew = Crew(
            agents=[researcher, writer, editor],
            tasks=[task1, task2, task3],
            process=Process.sequential,
            memory=True,
            cache=True,
            share_crew=True
        )

        result = crew.kickoff(inputs={"topic": topic})

        ## Save the result content to a markdown file
        blog_content = str(result) 
        md_path = "new-blog-post.md"
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(blog_content)

        ## Convert the markdown to the selected format
        return convert_blog_file(md_path, output_format)

    except Exception as e:
        print(f"[ERROR] Crew execution failed: {e}")
        raise
