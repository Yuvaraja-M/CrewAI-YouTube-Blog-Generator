from crewai import Agent
from tools import ytool
import os
from dotenv import load_dotenv
load_dotenv()
# Load environment variables from .env (do NOT hardcode secrets in source)
# The project's .env already contains the necessary Azure/OpenAI values.
# If you need to override for local testing, set environment variables instead
# of editing this file.

# Ensure critical vars are present (optional warning) - don't overwrite if set
if not os.getenv("AZURE_OPENAI_API_KEY"):
    # If you want to surface a runtime warning uncomment the print below
    # print('Warning: AZURE_OPENAI_API_KEY not set. Some tools may fail.')
    pass

# Placeholder for an LLM instance. Replace this with a proper LLM client
# initialization (for example, creating an Azure/OpenAI LLM wrapper) before
# running production workloads. This prevents a NameError at import-time.
llm = None
blog_researcher = Agent(
    role="Blog Researcher from the Youtube Videos",
    goal = "get the releavent video content for the topic {topic} from Yt channel",
    verbose = True,
    memory = True,
    backstory=(
        "Expert in understanding videos in AI Data Science,Machine learning and GEN AI and providing suggestion"
    ),
    tools = [ytool],
    llm = llm,
    allow_delegation = True
)

#creating a senior blog writer agent with yt tools

blog_writer = Agent(
    role = "Blog Writer",
    goal = "Narrate compelling tech stories about the video{topic}",
    verbose = True,
    memory = True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner"
    ),
    tools = [ytool],
    llm = llm,
    allow_delegation=False
)
