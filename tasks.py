from crewai import Task


def create_tasks(blog_researcher, blog_writer, blog_editor):
    
    ## Research Task 

    research_task = Task(
        description = (
            "Identify and analyze relevant YouTube videos about the topic: {topic}. "
            "Extract key points, speaker insights, and examples from the video(s)."
        ),
        expected_output="A comprehensive, 3-paragraph research summary covering the main points, context, and technical insights related to {topic}.",
        agent = blog_researcher
    )

    ## Writing task 

    write_task = Task(
        description=(
            "Based on the research, write a compelling and informative blog article on the topic: {topic}. "
            "Focus on clarity, engagement, and technical accuracy."
        ),
        expected_output= "A blog post draft suitable for publication, clearly explaining the topic {topic} based on the YouTube video insights.",
        agent = blog_writer,
        async_execution=False
    )

    ## Editing task

    edit_task = Task(
    description = "Take the draft blog and rewrite it for polish, clarity, markdown structure, and visual readability.",
    expected_output = "A clean, formatted markdown blog with proper headings, lists, and structure.",
    agent = blog_editor
)

    return research_task, write_task, edit_task