import os
from dotenv import load_dotenv

# Force the code to load the secret from your .env file
load_dotenv()

from google.adk.agents import LlmAgent, SequentialAgent

# 1. The Scriptwriter Agent
scriptwriter_agent = LlmAgent(
    name="scriptwriter_agent",
    model="gemini-2.5-flash", 
    description="Writes the script for the YouTube short based on the user's topic.",
    instruction="You are an expert scriptwriter. Write a 60-second, highly engaging script about the topic provided. Include a hook at the beginning."
)

# 2. The Visualizer Agent
visualizer_agent = LlmAgent(
    name="visualizer_agent",
    model="gemini-2.5-flash",
    description="Creates visual cues and b-roll ideas for the video.",
    instruction="Based on the script provided, suggest visual scenes, text-on-screen, and b-roll to match the narration perfectly."
)

# 3. The Formatter Agent
formatter_agent = LlmAgent(
    name="formatter_agent",
    model="gemini-2.5-flash",
    description="Formats the final output for the user.",
    instruction="Combine the script and the visual ideas into a clean, easy-to-read final document for a video editor to follow."
)

# 4. The Orchestrator (Manager) Agent
youtube_shorts_agent = SequentialAgent( 
    name="youtube_shorts_agent",
    description="You orchestrate the creation of a YouTube short by managing the scriptwriter, visualizer, and formatter.",
    sub_agents=[scriptwriter_agent, visualizer_agent, formatter_agent]
)

# Tell the ADK which agent to run when the server starts
root_agent = youtube_shorts_agent