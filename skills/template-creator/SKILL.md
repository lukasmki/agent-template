---
name: template-creator
description: Create and customize Pydantic AI agent templates with specialized configurations, tools, and system prompts
version: "1.0.0"
author: "Agent Template"
tags: ["template", "agent", "generation", "configuration"]
---

# Template Creator Skill

## When to Use This Skill

Use this skill when you need to:
- Create new agent templates from scratch
- Generate specialized agent configurations
- Customize existing templates for specific domains
- Set up agent scaffolding with common patterns
- Generate boilerplate code for different agent types

## Instructions

### Template Generation Process

1. **Analyze Requirements** - Understand the agent's purpose, domain, and capabilities
2. **Select Base Template** - Choose appropriate starting point (basic, business, technical, etc.)
3. **Configure System Prompt** - Create specialized instructions and persona
4. **Design Tools** - Plan and implement required functionality
5. **Set Up Models** - Choose appropriate AI models for the task
6. **Configure Interface** - Set up web UI and integration patterns
7. **Add Documentation** - Generate relevant documentation and examples

## Available Scripts

### create_template
Generate a complete agent template with specified configuration.

**Arguments:**
- `agent_type` (required): Type of agent to create (business, technical, creative, support, research, custom)
- `agent_name` (required): Name for the agent project
- `description` (optional): Brief description of agent purpose
- `features` (optional): Comma-separated list of features to include
- `model` (optional): Preferred AI model (gpt-4o, claude-3-5-sonnet, gemini-3-flash)

**Example Usage:**
```python
run_skill_script(
    skill_name="template-creator",
    script_name="create_template",
    args=["business", "sales-assistant", "AI assistant for sales team", "lead-tracking,email-integration,reporting", "gpt-4o"]
)
```

### customize_template
Modify an existing template with new capabilities.

**Arguments:**
- `template_path` (required): Path to existing template or main.py
- `modifications` (required): JSON string of modifications to apply
- `backup` (optional): Create backup before modifying (true/false, default: true)

**Example Usage:**
```python
run_skill_script(
    skill_name="template-creator",
    script_name="customize_template",
    args=["./main.py", '{"add_tools": ["file_reader", "api_client"], "update_prompt": "You are now a data analyst"}', "true"]
)
```

### generate_config
Generate configuration files and environment setup.

**Arguments:**
- `config_type` (required): Type of configuration to generate (docker, deployment, development, testing)
- `output_path` (optional): Output directory for generated files (default: ./)

**Example Usage:**
```python
run_skill_script(
    skill_name="template-creator",
    script_name="generate_config",
    args=["docker", "./docker-setup"]
)
```

## Template Types

### Business Agent
- **Purpose**: Customer service, sales, marketing, HR functions
- **Common Tools**: CRM integration, email handling, report generation
- **Recommended Models**: GPT-4o (business context), Claude Sonnet (analysis)
- **Interface**: Professional web UI with authentication

### Technical Agent
- **Purpose**: Code assistance, debugging, documentation, API integration
- **Common Tools**: Code execution, file operations, API clients
- **Recommended Models**: Claude Sonnet (coding), GPT-4o (general tech)
- **Interface**: Developer-friendly with syntax highlighting

### Creative Agent
- **Purpose**: Content creation, writing assistance, design help
- **Common Tools**: Text generation, formatting, style guides
- **Recommended Models**: GPT-4o (creativity), Claude Sonnet (writing)
- **Interface**: Rich text editor with preview

### Support Agent
- **Purpose**: Customer support, troubleshooting, ticket management
- **Common Tools**: Knowledge base search, ticket integration, escalation
- **Recommended Models**: Claude Haiku (speed), GPT-4o-mini (cost-effective)
- **Interface**: Support dashboard with ticket tracking

### Research Agent
- **Purpose**: Academic research, data analysis, literature review
- **Common Tools**: Database search, data processing, citation formatting
- **Recommended Models**: Claude Sonnet (analysis), GPT-4o (comprehensive)
- **Interface**: Research workspace with document management

## Agent Configuration Patterns

### System Prompt Templates

**Business Pattern:**
```
You are a {role} specializing in {domain}. Your responsibilities include:
- {task_1}
- {task_2}
- {task_3}

Always maintain {tone} communication and follow {compliance} guidelines.
```

**Technical Pattern:**
```
You are a {role} with expertise in {technologies}. Help with:
- {capability_1}
- {capability_2}
- {capability_3}

Provide clear, working code examples and explain technical concepts.
```

**Creative Pattern:**
```
You are a {role} specializing in {creative_field}. Assist with:
- {creative_task_1}
- {creative_task_2}
- {creative_task_3}

Follow {style_guidelines} and maintain {brand_voice}.
```

### Tool Generation Patterns

**Data Processing Tool:**
```python
@agent.tool_plain
def process_{data_type}(input_data: str) -> str:
    """Process {data_type} and return formatted results."""
    try:
        # Processing logic
        result = input_data.strip().{transformation}
        return f"Processed {data_type}: {result}"
    except Exception as e:
        return f"Error processing {data_type}: {str(e)}"
```

**API Integration Tool:**
```python
@agent.tool_plain
def {service_name}_api(action: str, params: dict = None) -> str:
    """Interact with {service_name} API."""
    try:
        # API implementation
        response = requests.{method}("{api_endpoint}", data=params)
        return f"API Response: {response.json()}"
    except Exception as e:
        return f"API Error: {str(e)}"
```

**File Operation Tool:**
```python
@agent.tool_plain
def handle_{file_format}(file_path: str, operation: str) -> str:
    """Handle {file_format} files with specified operation."""
    try:
        # File handling logic
        with open(file_path, '{mode}') as f:
            content = f.{operation}()
        return f"File {operation} completed"
    except Exception as e:
        return f"File Error: {str(e)}"
```

## Best Practices

### Template Structure
1. **Clear Purpose** - Define specific use case and target audience
2. **Modular Design** - Separate concerns into distinct tools and functions
3. **Error Handling** - Implement comprehensive error management
4. **Security** - Follow security best practices for all operations
5. **Documentation** - Include clear documentation and examples

### Configuration Management
1. **Environment Variables** - Use .env files for sensitive configuration
2. **Dependency Management** - Declare all dependencies in pyproject.toml
3. **Model Selection** - Choose appropriate models based on task requirements
4. **Performance** - Optimize for response time and token usage

### Testing Strategy
1. **Unit Tests** - Test individual tools and functions
2. **Integration Tests** - Test complete workflows
3. **Performance Tests** - Measure response times and resource usage
4. **Security Tests** - Verify input validation and access controls

## Common Customization Options

### Model Configuration
- **GPT-4o**: Best for general business and creative tasks
- **Claude Sonnet**: Excellent for analysis, writing, and coding
- **Gemini Flash**: Fast and cost-effective for simple tasks
- **Multi-model**: Use multiple models for different capabilities

### Interface Customization
- **Authentication**: Add user authentication and authorization
- **Styling**: Customize CSS and UI components
- **Features**: Add file upload, data visualization, or real-time updates
- **Integration**: Connect to external systems and databases

### Tool Categories
- **Data Tools**: File processing, data analysis, validation
- **Communication**: Email, messaging, notifications
- **Integration**: API clients, database connections, webhooks
- **Productivity**: Scheduling, reporting, automation

## Example Templates

### Basic Business Agent
```python
SYSTEM_PROMPT = """
You are a business assistant for {company_name}. Help with:
- Customer inquiries and support
- Sales process assistance
- Report generation and analysis
- Administrative tasks

Always maintain professional communication and confidentiality.
""".strip()
```

### Technical Documentation Agent
```python
SYSTEM_PROMPT = """
You are a technical documentation specialist. Assist with:
- API documentation writing
- Code documentation and comments
- Technical guides and tutorials
- README and documentation reviews

Provide clear, accurate, and comprehensive technical content.
""".strip()
```

## Troubleshooting

### Common Issues
1. **Template Generation Fails** - Check input parameters and dependencies
2. **Configuration Errors** - Verify JSON syntax and required fields
3. **Import Errors** - Ensure all required packages are installed
4. **Runtime Errors** - Check error logs and validate input data

### Debug Mode
Enable debug logging for detailed troubleshooting:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Support Resources
- Check generated template comments for guidance
- Review error messages for specific issues
- Consult the repository documentation for patterns
- Test components individually before integration

This skill provides comprehensive template generation capabilities, enabling rapid creation of specialized AI agents for various use cases and domains.