from pydantic_ai import Agent
from dotenv import load_dotenv
import random

# Load API keys
load_dotenv()

# Setup the agent
agent = Agent("google-gla:gemini-2.5-flash")


# Define a tool
@agent.tool_plain
def roll_dice() -> str:
    """Roll a six-sided die and return the result."""
    return str(random.randint(1, 6))


# Convert to chat interface
app = agent.to_web()
