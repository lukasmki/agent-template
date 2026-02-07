# Agent Creation Patterns & Command Interpretation

This guide helps coding agents interpret user commands and generate appropriate Pydantic AI agent implementations using this repository template.

## Command Pattern Mapping

### Core Agent Commands

| User Command | Implementation | Code Example |
|--------------|----------------|-------------|
| "Create an agent that does X" | Modify `SYSTEM_PROMPT` in `main.py` | `SYSTEM_PROMPT = "You are an expert in X. Do specific tasks..."` |
| "Make it professional/friendly/casual" | Update system prompt tone | `SYSTEM_PROMPT = "You are a helpful and friendly assistant..."` |
| "Add functionality for Y" | Create new tool function | See Tool Creation section |
| "Use model Z" | Update models list in `agent.to_web()` | `"openai:gpt-4o"` or `"anthropic:claude-3-5-sonnet"` |

### Tool Creation Commands

| User Request | Implementation Pattern |
|--------------|----------------------|
| "Add a tool that analyzes text" | Create text analysis function |
| "Make it calculate something" | Implement calculation tool |
| "Connect to API/service" | Add HTTP request tool |
| "Read/write files" | Implement file I/O tool with safety checks |
| "Search the web" | Create web search tool |

## Implementation Templates

### 1. Basic Agent Setup

**Command**: "Create a basic agent for [purpose]"

```python
from pydantic_ai import Agent
from dotenv import load_dotenv
import random

# Update system prompt based on purpose
SYSTEM_PROMPT = """
You are a specialized AI assistant for [purpose].
Your main responsibilities are:
- [Task 1]
- [Task 2]
- [Task 3]

Always be helpful, accurate, and provide clear explanations.
""".strip()

# Setup the agent
agent = Agent(
    system_prompt=SYSTEM_PROMPT,
    output_type=str,
)

# Example tool - customize as needed
@agent.tool_plain
def example_tool() -> str:
    """Example tool description."""
    return "Tool result"

# Convert to chat interface
load_dotenv()
app = agent.to_web(
    models=[
        # Choose appropriate model(s)
        "google-gla:gemini-3-flash",  # Fast and cost-effective
        # "openai:gpt-4o",           # Good for complex tasks
        # "anthropic:claude-3-5-sonnet",  # Good for analysis
    ]
)
```

### 2. Tool Creation Patterns

#### Data Processing Tools
**Command**: "Add a tool that processes [data type]"

```python
@agent.tool_plain
def process_data(input_data: str) -> str:
    """Process [data type] and return formatted results."""
    try:
        # Add processing logic here
        processed = input_data.strip().upper()
        return f"Processed: {processed}"
    except Exception as e:
        return f"Error processing data: {str(e)}"
```

#### API Integration Tools
**Command**: "Connect to [service] API"

```python
import requests
from typing import Dict, Any

@agent.tool_plain
def api_request(endpoint: str, method: str = "GET") -> str:
    """Make API request to [service]."""
    try:
        if method.upper() == "GET":
            response = requests.get(endpoint)
        else:
            response = requests.post(endpoint)
        
        if response.status_code == 200:
            return f"Success: {response.text}"
        else:
            return f"Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"Request failed: {str(e)}"
```

#### File Operations Tools
**Command**: "Add file reading/writing capability"

```python
import os
from pathlib import Path

@agent.tool_plain
def read_file(file_path: str) -> str:
    """Read content from a file safely."""
    try:
        # Security: prevent path traversal
        safe_path = Path(file_path).resolve()
        if not str(safe_path).startswith(os.getcwd()):
            return "Error: Access denied - path traversal attempt"
        
        with open(safe_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return f"File content:\n{content}"
    except FileNotFoundError:
        return f"Error: File '{file_path}' not found"
    except Exception as e:
        return f"Error reading file: {str(e)}"
```

#### Calculation Tools
**Command**: "Add [mathematical] calculation"

```python
import math

@agent.tool_plain
def calculate(operation: str, a: float, b: float = None) -> str:
    """Perform mathematical calculations."""
    try:
        if operation.lower() == "square":
            result = a ** 2
            return f"The square of {a} is {result}"
        elif operation.lower() == "sqrt":
            result = math.sqrt(a)
            return f"The square root of {a} is {result}"
        elif b is not None:
            if operation.lower() == "add":
                result = a + b
                return f"{a} + {b} = {result}"
            elif operation.lower() == "multiply":
                result = a * b
                return f"{a} × {b} = {result}"
        else:
            return "Error: Invalid operation or missing second number"
    except Exception as e:
        return f"Calculation error: {str(e)}"
```

### 3. Multiple Agent Patterns

**Command**: "Create separate agents for different tasks"

```python
# Agent 1: Data Analyst
data_analyst = Agent(
    system_prompt="You are a data analyst. Focus on numbers, statistics, and patterns.",
    output_type=str,
)

# Agent 2: Content Creator  
content_creator = Agent(
    system_prompt="You are a content creator. Focus on writing, editing, and communication.",
    output_type=str,
)

# Choose which agent to convert to web interface
load_dotenv()
app = data_analyst.to_web(  # or content_creator.to_web()
    models=["google-gla:gemini-3-flash"]
)
```

### 4. Model Selection Guidelines

**Command**: "Use the best model for [task type]"

```python
models = []

# For general conversation and simple tasks
if task_type == "general":
    models.extend(["google-gla:gemini-3-flash"])

# For complex reasoning and analysis  
elif task_type == "analysis":
    models.extend(["anthropic:claude-3-5-sonnet"])

# For creative tasks and writing
elif task_type == "creative":
    models.extend(["openai:gpt-4o"])

# Fallback models (always include at least one)
models.extend(["google-gla:gemini-3-flash"])

app = agent.to_web(models=models)
```

## Common User Scenarios

### Scenario 1: Business Assistant
**User Request**: "Create an assistant for my small business"

```python
SYSTEM_PROMPT = """
You are a small business assistant. Help with:
- Customer service responses
- Basic bookkeeping calculations
- Scheduling and reminders
- Product/service recommendations

Always be professional and helpful.
""".strip()

@agent.tool_plain
def calculate_profit(revenue: float, costs: float) -> str:
    """Calculate profit margin and percentage."""
    profit = revenue - costs
    if revenue > 0:
        margin = (profit / revenue) * 100
        return f"Profit: ${profit:.2f} ({margin:.1f}% margin)"
    else:
        return "Error: Revenue must be greater than 0"
```

### Scenario 2: Educational Tutor
**User Request**: "Create a tutor for [subject]"

```python
SYSTEM_PROMPT = f"""
You are a {subject} tutor. Your role is to:
- Explain concepts clearly and simply
- Provide examples and practice problems
- Ask questions to check understanding
- Give constructive feedback

Adapt your explanations to the student's level.
""".strip()

@agent.tool_plain
def generate_practice_problem(topic: str, difficulty: str = "medium") -> str:
    """Generate a practice problem for the given topic."""
    # Problem generation logic based on topic and difficulty
    return f"Practice problem for {topic} ({difficulty} difficulty): [problem here]"
```

### Scenario 3: Technical Assistant
**User Request**: "Create a coding assistant for [language]"

```python
SYSTEM_PROMPT = f"""
You are a {language} programming assistant. Help with:
- Code writing and debugging
- Explaining concepts and syntax
- Best practices and optimization
- Error troubleshooting

Provide clear, working code examples.
""".strip()

@agent.tool_plain
def validate_code(code: str, language: str) -> str:
    """Basic code validation and syntax checking."""
    # Add language-specific validation logic
    return f"Code validation for {language}: [validation results]"
```

## Environment Setup Commands

### Initial Setup
**User Command**: "Set up the project" or "Get it running"

```bash
# Make script executable and run
chmod +x run_interface.sh
./run_interface.sh
```

### API Configuration
**User Command**: "Add OpenAI keys" or "Set up models"

1. Create `.env` file from `.env.sample`
2. Add appropriate API keys:
```env
OPENAI_API_KEY=sk-your-key-here
ANTHROPIC_API_KEY=sk-ant-your-key-here
GOOGLE_API_KEY=your-google-key-here
```

### Dependency Management
**User Command**: "Add [library] to the project"

```python
# Update pyproject.toml
dependencies = [
    "pydantic-ai>=1.54.0",
    "python-dotenv>=1.2.1", 
    "uvicorn>=0.40.0",
    "new-library>=1.0.0",  # Add this line
]
```

Then run: `uv sync`

## Testing and Validation

### Automated Testing
**User Command**: "Test the agent works"

```python
# Add test at bottom of main.py
if __name__ == "__main__":
    import asyncio
    
    async def test_agent():
        test_result = await agent.run("Hello, can you roll a dice for me?")
        print("Test result:", test_result.output)
    
    asyncio.run(test_agent())
```

### Manual Testing
1. Run `./run_interface.sh`
2. Open http://127.0.0.1:8000
3. Test each tool individually
4. Verify error handling

## Error Handling Patterns

### Tool Error Handling
```python
@agent.tool_plain
def safe_operation(param: str) -> str:
    """Perform operation with comprehensive error handling."""
    try:
        # Input validation
        if not param or not isinstance(param, str):
            return "Error: Invalid input - parameter must be a non-empty string"
        
        # Operation logic
        result = param.upper()
        
        # Success case
        return f"Success: {result}"
        
    except ValueError as e:
        return f"Value error: {str(e)}"
    except TypeError as e:
        return f"Type error: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"
```

## Best Practices for Coding Agents

1. **Always validate user inputs** before processing
2. **Use try-catch blocks** for all external operations
3. **Provide clear error messages** that help users fix issues
4. **Follow the existing code style** and patterns in the template
5. **Document tools** with clear docstrings for the agent
6. **Test each tool individually** before integration
7. **Consider security implications** of file I/O and API calls

## Advanced Patterns

### Conditional Tool Loading
```python
# Load tools based on user requirements
tools_to_add = []

if need_file_operations:
    @agent.tool_plain
    def read_file(file_path: str) -> str:
        """Read file content safely."""
        # Implementation
        
if need_calculations:
    @agent.tool_plain  
    def calculate(operation: str, a: float, b: float) -> str:
        """Perform calculations."""
        # Implementation
```

### Dynamic System Prompts
```python
def create_system_prompt(agent_type: str, specialization: str = None) -> str:
    base_prompts = {
        "assistant": "You are a helpful AI assistant.",
        "analyst": "You are a data analyst.",
        "tutor": "You are an educational tutor."
    }
    
    prompt = base_prompts.get(agent_type, base_prompts["assistant"])
    
    if specialization:
        prompt += f" Specializing in {specialization}."
    
    return prompt.strip()

SYSTEM_PROMPT = create_system_prompt("analyst", "financial data")
```

This guide provides comprehensive patterns for interpreting user commands and implementing robust AI agents using the repository template.