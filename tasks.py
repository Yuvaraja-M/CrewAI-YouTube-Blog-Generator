from crewai import Task
from tools import ytool
from agents import blog_researcher, blog_writer

research_task = Task(
    description=(
        "Idenltify the video {topic}"
        "Get detailed information about the vide from the channel"
    ),
    expected_output='A comprehensive 3 paragraph long report based on the {topic} of video',
    tools = [ytool],
    agent=blog_researcher,
)

write_task = Task(
    description=(
        "get the info from the yt channel on the topic {topic}"
    ),
    expected_output='summarize the info from the youtube channel video on the topic {topic} and create the content for the blog',
    tools = [ytool],
    agent=blog_researcher,
    async_execution = False,
    output_file = 'new-blog-post.md'
)
