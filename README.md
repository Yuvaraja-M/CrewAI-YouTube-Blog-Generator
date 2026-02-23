# 🤖 AI Content Creator: YouTube to Blog Automation with CrewAI

An intelligent multi-agent system that automatically researches YouTube videos and generates comprehensive blog posts using CrewAI framework. This project demonstrates the power of autonomous AI agents working together to create high-quality content from video sources.

## 🌟 Features

- **Autonomous Research Agent**: Automatically searches and analyzes YouTube videos on specified topics
- **Expert Content Writer**: Transforms video content into engaging, well-structured blog posts
- **Multi-Agent Collaboration**: Two specialized AI agents work together seamlessly
- **YouTube Integration**: Direct integration with YouTube channels for content discovery
- **Automated Workflow**: End-to-end automation from research to published blog content
- **Memory & Caching**: Intelligent memory system for context retention and performance optimization

## 🎯 Use Cases

- **Content Creators**: Automatically generate blog content from your YouTube videos
- **Researchers**: Quickly summarize and analyze educational YouTube content
- **Marketers**: Transform video content into written marketing materials
- **Educators**: Create written summaries of educational video content
- **Bloggers**: Efficiently research and write about trending topics

## 🏗️ Architecture

The system consists of two specialized AI agents:

### 🔍 Blog Researcher Agent
- **Role**: YouTube Video Research Specialist
- **Responsibilities**: 
  - Searches relevant videos on specified topics
  - Extracts detailed information from video content
  - Analyzes and summarizes video insights
- **Tools**: YouTube Channel Search Tool

### ✍️ Blog Writer Agent
- **Role**: Technical Content Writer
- **Responsibilities**:
  - Creates compelling narratives from research data
  - Simplifies complex technical topics
  - Generates well-structured blog posts
- **Tools**: YouTube Channel Search Tool

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Azure OpenAI API access (or OpenAI API)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd crewaicourse
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv crewenv
   # On Windows
   crewenv\Scripts\activate
   # On macOS/Linux
   source crewenv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r req.txt
   ```

4. **Configure environment variables**
   
   Create a `.env` file in the project root with your API credentials:
   ```env
   # Azure OpenAI Settings
   AZURE_OPENAI_API_KEY=your_azure_openai_api_key
   AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com/
   AZURE_OPENAI_API_VERSION=2025-01-01-preview
   
   # OpenAI Compatibility (Required for CrewAI Tools)
   OPENAI_API_KEY=your_azure_openai_api_key
   OPENAI_BASE_URL=https://your-endpoint.openai.azure.com/
   OPENAI_API_VERSION=2025-01-01-preview
   OPENAI_API_TYPE=azure
   
   # Model Settings
   OPENAI_DEPLOYMENT_NAME=gpt-4o
   ```

### Usage

1. **Run the automation system**
   ```bash
   python cre.py
   ```

2. **Customize the topic**
   
   Edit the topic in `cre.py`:
   ```python
   result = crew.kickoff(inputs={'topic':'Your desired topic here'})
   ```

3. **Check the output**
   
   The generated blog post will be saved as `new-blog-post.md`

## 📁 Project Structure

```
crewaicourse/
├── agents.py          # AI agent definitions and configurations
├── tasks.py           # Task definitions for each agent
├── tools.py           # YouTube integration tools
├── cre.py             # Main execution script
├── req.txt            # Python dependencies
├── .env               # Environment variables (not in repo)
├── crewenv/           # Virtual environment
└── new-blog-post.md   # Generated output (created after execution)
```

## 🔧 Configuration

### Agents Configuration

The system uses two main agents defined in `agents.py`:

- **Blog Researcher**: Configured for YouTube video analysis and research
- **Blog Writer**: Configured for content creation and narrative writing

### Tasks Configuration

Tasks are defined in `tasks.py`:

- **Research Task**: Identifies and analyzes relevant videos
- **Writing Task**: Creates comprehensive blog content

### Tools Configuration

YouTube integration is configured in `tools.py`:

```python
from crewai_tools import YoutubeChannelSearchTool
ytool = YoutubeChannelSearchTool(youtube_channel_handle='krishnaik06')
```

## 🎛️ Customization

### Change YouTube Channel

Modify the channel in `tools.py`:
```python
ytool = YoutubeChannelSearchTool(youtube_channel_handle='your_channel_handle')
```

### Adjust Agent Behavior

Modify agent roles, goals, and backstories in `agents.py` to change how they behave.

### Customize Output Format

Edit the `expected_output` in `tasks.py` to change the blog post format.

## 📊 Performance Features

- **Memory System**: Agents retain context across interactions
- **Caching**: Reduces redundant API calls and improves performance
- **Rate Limiting**: Built-in rate limiting (100 RPM) for API compliance
- **Sequential Processing**: Ensures proper task execution order

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📋 Requirements

See `req.txt` for the complete list of dependencies:
- `crewai` - Multi-agent AI framework
- `crewai_tools` - Pre-built tools for CrewAI

## ⚠️ Important Notes

- Ensure you have valid API credentials before running
- The system is configured for Azure OpenAI but can be adapted for standard OpenAI
- Generated content should be reviewed before publishing
- Respect YouTube's terms of service and rate limits

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [CrewAI](https://www.crewai.com/) for the amazing multi-agent framework
- [Krish Naik](https://www.youtube.com/@krishnaik06) for educational content
- OpenAI/Azure OpenAI for the underlying AI capabilities

---

**Made with ❤️ and AI agents**
