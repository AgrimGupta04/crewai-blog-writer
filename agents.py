from crewai import Agent
from langchain_openai import ChatOpenAI  # OpenAI wrapper
import os

def create_agents(yt_tool, openai_api_key: str):
    # Set the API key dynamically
    os.environ["OPENAI_API_KEY"] = openai_api_key

    # Use ChatOpenAI as the LLM
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7,
        api_key=openai_api_key  # explicitly pass the key too (redundant but safe)
    )

    # Agent 1: Blog Researcher
    blog_researcher = Agent(
        role='Blog Researcher from youtube videos.',
        goal='Get the relevant video content for the topic {topic} from YouTube channel.',
        verbose=True,
        memory=True,
        backstory=(
            'Expert in understanding videos in AI, Data Science, Machine Learning and GenAI and providing suggestions.'
        ),
        tools=[yt_tool],
        allow_delegation=True,
        llm=llm
    )

    # Agent 2: Blog Writer
    blog_writer = Agent(
        role='Blog Writer',
        goal='Narrate compelling tech stories about the video {topic}',
        verbose=True,
        memory=True,
        backstory=(
            "With a flair for simplifying complex topics, you craft "
            "engaging narratives that captivate and educate, bringing new "
            "discoveries to light in an accessible manner."
        ),
        tools=[yt_tool],
        allow_delegation=True,
        llm=llm
    )

    # Agent 3: Blog Editor
    blog_editor = Agent(
        role='Blog Editor',
        goal='Polish the draft blog and format it with markdown for readability.',
        verbose=True,
        memory=True,
        backstory="You're a senior editor skilled in technical blog writing and formatting.",
        tools=[yt_tool],
        allow_delegation=False,
        llm=llm
    )

    return blog_researcher, blog_writer, blog_editor
