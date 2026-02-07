---
name: tool-generator
description: Generate custom Pydantic AI tools with templates for data processing, API integration, file operations, calculations, and more
version: "1.0.0"
author: "Agent Template"
tags: ["tools", "generation", "automation", "templates"]
---

# Tool Generator Skill

## When to Use This Skill

Use this skill when you need to:
- Create custom tools for Pydantic AI agents
- Generate boilerplate code for common tool patterns
- Implement data processing and analysis tools
- Add API integrations and external service connections
- Create file operation and management tools
- Generate calculation and mathematical tools
- Build communication and notification tools

## Instructions

### Tool Generation Process

1. **Identify Requirements** - Understand the tool's purpose, inputs, and outputs
2. **Select Tool Type** - Choose appropriate pattern (data, API, file, calculation, etc.)
3. **Define Interface** - Specify function signature and parameters
4. **Implement Logic** - Write core functionality with error handling
5. **Add Validation** - Implement input validation and security checks
6. **Test and Debug** - Verify tool functionality and edge cases
7. **Document** - Add comprehensive documentation and examples

## Available Scripts

### generate_tool
Generate a complete tool implementation based on specifications.

**Arguments:**
- `tool_type` (required): Type of tool to generate (data_processor, api_client, file_handler, calculator, communicator, validator, formatter)
- `tool_name` (required): Name for the tool function
- `description` (required): Brief description of what the tool does
- `parameters` (optional): JSON string defining parameters and their types
- `features` (optional): Comma-separated list of additional features

**Example Usage:**
```python
run_skill_script(
    skill_name="tool-generator",
    script_name="generate_tool",
    args=["data_processor", "analyze_sales_data", "Analyze sales data and generate insights", '{"data_source": "string", "analysis_type": "string"}', "error_handling,logging,caching"]
)
```

### create_api_tool
Generate a tool for integrating with external APIs.

**Arguments:**
- `service_name` (required): Name of the service/API
- `base_url` (required): Base URL for the API
- `auth_type` (required): Authentication type (none, api_key, oauth, basic)
- `endpoints` (optional): JSON string of endpoint configurations

**Example Usage:**
```python
run_skill_script(
    skill_name="tool-generator",
    script_name="create_api_tool",
    args=["stripe", "https://api.stripe.com/v1", "api_key", '{"charges": "GET /charges", "customers": "POST /customers"}']
)
```

### generate_file_tool
Create file operation tools with security features.

**Arguments:**
- `operation` (required): File operation type (read, write, analyze, convert)
- `file_types` (required): Supported file types (csv, json, txt, xml, etc.)
- `security_level` (optional): Security level (basic, strict, custom)

**Example Usage:**
```python
run_skill_script(
    skill_name="tool-generator",
    script_name="generate_file_tool",
    args=["analyze", "csv,json,xlsx", "strict"]
)
```

## Tool Templates and Patterns

### Data Processing Tools

#### Basic Data Processor Template
```python
@agent.tool_plain
def {tool_name}(input_data: str, processing_type: str = "default") -> str:
    """{description}
    
    Args:
        input_data: Raw data to process
        processing_type: Type of processing to apply
    """
    try:
        # Input validation
        if not input_data or not isinstance(input_data, str):
            return "Error: Invalid input data"
        
        # Processing logic based on type
        if processing_type == "clean":
            result = input_data.strip().lower()
        elif processing_type == "analyze":
            # Add analysis logic here
            result = f"Analysis: {len(input_data)} characters"
        else:
            result = input_data
            
        return f"Processed result: {result}"
        
    except Exception as e:
        return f"Processing error: {str(e)}"
```

#### Advanced Data Analysis Tool
```python
@agent.tool_plain
def {tool_name}(data_source: str, analysis_type: str = "summary") -> str:
    """Perform comprehensive data analysis on the provided data.
    
    Args:
        data_source: Data to analyze (JSON, CSV, or text)
        analysis_type: Type of analysis (summary, detailed, statistical)
    """
    try:
        # Parse data format
        if data_source.startswith('[') or data_source.startswith('{'):
            import json
            data = json.loads(data_source)
        elif ',' in data_source and '\n' in data_source:
            import pandas as pd
            from io import StringIO
            data = pd.read_csv(StringIO(data_source))
        else:
            data = data_source.split()
        
        # Perform analysis
        if analysis_type == "summary":
            return f"Data Summary: {str(type(data).__name__)} with {len(data) if hasattr(data, '__len__') else 'unknown'} items"
        elif analysis_type == "detailed":
            return f"Detailed Analysis: {data}"
        else:
            # Statistical analysis
            return f"Statistical analysis completed"
            
    except Exception as e:
        return f"Analysis error: {str(e)}"
```

### API Integration Tools

#### REST API Client Template
```python
@agent.tool_plain
def {service_name}_api(endpoint: str, method: str = "GET", data: str = None) -> str:
    """Interact with {service_name} API.
    
    Args:
        endpoint: API endpoint to call
        method: HTTP method (GET, POST, PUT, DELETE)
        data: Request body data (JSON string)
    """
    try:
        import requests
        import os
        
        # Configuration
        base_url = "{base_url}"
        api_key = os.getenv('{service_upper}_API_KEY')
        
        # Setup headers
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Pydantic-AI-Agent/1.0"
        }
        
        # Add authentication
        if api_key:
            headers["Authorization"] = f"Bearer {api_key}"
        
        # Make request
        url = f"{base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        
        if method.upper() == "GET":
            response = requests.get(url, headers=headers)
        elif method.upper() == "POST":
            response = requests.post(url, headers=headers, json=json.loads(data) if data else None)
        else:
            return f"Unsupported method: {method}"
        
        # Process response
        if response.status_code == 200:
            return f"Success: {response.json() if response.headers.get('content-type', '').includes('json') else response.text}"
        else:
            return f"API Error ({response.status_code}): {response.text}"
            
    except Exception as e:
        return f"API request failed: {str(e)}"
```

#### GraphQL API Tool
```python
@agent.tool_plain
def {service_name}_graphql(query: str, variables: str = None) -> str:
    """Execute GraphQL query against {service_name}.
    
    Args:
        query: GraphQL query string
        variables: GraphQL variables (JSON string)
    """
    try:
        import requests
        import json
        import os
        
        # Configuration
        url = "{graphql_endpoint}"
        api_key = os.getenv('{service_upper}_API_KEY')
        
        # Setup headers
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        
        # Prepare request
        payload = {"query": query}
        if variables:
            payload["variables"] = json.loads(variables)
        
        # Make request
        response = requests.post(url, headers=headers, json=payload)
        
        if response.status_code == 200:
            result = response.json()
            return f"GraphQL Response: {json.dumps(result, indent=2)}"
        else:
            return f"GraphQL Error: {response.text}"
            
    except Exception as e:
        return f"GraphQL request failed: {str(e)}"
```

### File Operation Tools

#### Secure File Reader Template
```python
@agent.tool_plain
def {tool_name}(file_path: str, max_size: int = 1024) -> str:
    """Securely read file contents with size limits.
    
    Args:
        file_path: Path to file to read
        max_size: Maximum file size in bytes to read
    """
    try:
        import os
        from pathlib import Path
        
        # Security: Resolve absolute path and validate
        safe_path = Path(file_path).resolve()
        current_dir = Path.cwd()
        
        # Prevent path traversal
        if not str(safe_path).startswith(str(current_dir)):
            return "Error: Access denied - path outside allowed directory"
        
        # Check file size
        file_size = safe_path.stat().st_size
        if file_size > max_size * 1024:  # Convert KB to bytes
            return f"Error: File too large ({file_size} bytes, max {max_size * 1024})"
        
        # Read file
        with open(safe_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        return f"File content ({file_size} bytes):\n{content}"
        
    except FileNotFoundError:
        return f"Error: File '{file_path}' not found"
    except PermissionError:
        return f"Error: Permission denied accessing '{file_path}'"
    except Exception as e:
        return f"Error reading file: {str(e)}"
```

#### File Format Converter
```python
@agent.tool_plain
def {tool_name}(input_file: str, output_format: str, output_file: str = None) -> str:
    """Convert file between different formats.
    
    Args:
        input_file: Path to input file
        output_format: Target format (json, csv, xml, txt)
        output_file: Path for output file (optional)
    """
    try:
        import json
        import csv
        from pathlib import Path
        
        input_path = Path(input_file)
        
        # Read input file
        if input_path.suffix.lower() == '.json':
            with open(input_path, 'r') as f:
                data = json.load(f)
        elif input_path.suffix.lower() == '.csv':
            with open(input_path, 'r') as f:
                reader = csv.DictReader(f)
                data = list(reader)
        else:
            # Try as text
            with open(input_path, 'r') as f:
                data = f.read()
        
        # Convert to output format
        if output_format.lower() == 'json':
            if isinstance(data, str):
                converted = {"text": data}
            else:
                converted = data
            output = json.dumps(converted, indent=2)
        elif output_format.lower() == 'csv':
            import pandas as pd
            df = pd.DataFrame(data if isinstance(data, list) else [data])
            output = df.to_csv(index=False)
        else:
            output = str(data)
        
        # Save or return
        if output_file:
            with open(output_file, 'w') as f:
                f.write(output)
            return f"Converted and saved to {output_file}"
        else:
            return f"Converted content:\n{output}"
            
    except Exception as e:
        return f"Conversion error: {str(e)}"
```

### Calculation Tools

#### Mathematical Calculator Template
```python
@agent.tool_plain
def {tool_name}(operation: str, a: float, b: float = None) -> str:
    """Perform mathematical calculations.
    
    Args:
        operation: Type of calculation (add, subtract, multiply, divide, power, sqrt, percent)
        a: First number
        b: Second number (optional for some operations)
    """
    try:
        import math
        
        if operation.lower() == "add":
            result = a + b
        elif operation.lower() == "subtract":
            result = a - b
        elif operation.lower() == "multiply":
            result = a * b
        elif operation.lower() == "divide":
            if b == 0:
                return "Error: Division by zero"
            result = a / b
        elif operation.lower() == "power":
            result = a ** b
        elif operation.lower() == "sqrt":
            result = math.sqrt(a)
        elif operation.lower() == "percent":
            if b is None:
                return "Error: Percentage requires two numbers"
            result = (a / b) * 100
        else:
            return f"Error: Unknown operation '{operation}'"
        
        return f"{operation.title()} result: {result}"
        
    except Exception as e:
        return f"Calculation error: {str(e)}"
```

#### Statistical Analysis Tool
```python
@agent.tool_plain
def {tool_name}(data: str, analysis_type: str = "basic") -> str:
    """Perform statistical analysis on numerical data.
    
    Args:
        data: Comma-separated numbers or JSON array
        analysis_type: Type of analysis (basic, advanced, distribution)
    """
    try:
        import json
        import math
        
        # Parse data
        if data.startswith('['):
            numbers = json.loads(data)
        else:
            numbers = [float(x.strip()) for x in data.split(',')]
        
        if not numbers:
            return "Error: No valid numbers found"
        
        # Basic statistics
        count = len(numbers)
        total = sum(numbers)
        mean = total / count
        
        if analysis_type == "basic":
            return f"""
            Basic Statistics:
            Count: {count}
            Sum: {total}
            Mean: {mean:.2f}
            Min: {min(numbers):.2f}
            Max: {max(numbers):.2f}
            """
        
        # Advanced statistics
        variance = sum((x - mean) ** 2 for x in numbers) / count
        std_dev = math.sqrt(variance)
        sorted_nums = sorted(numbers)
        median = sorted_nums[count // 2] if count % 2 == 1 else (sorted_nums[count // 2 - 1] + sorted_nums[count // 2]) / 2
        
        return f"""
        Statistical Analysis:
        Count: {count}
        Mean: {mean:.2f}
        Median: {median:.2f}
        Std Dev: {std_dev:.2f}
        Variance: {variance:.2f}
        Range: {min(numbers):.2f} - {max(numbers):.2f}
        """
        
    except Exception as e:
        return f"Statistical analysis error: {str(e)}"
```

### Communication Tools

#### Email Sender Template
```python
@agent.tool_plain
def {tool_name}(to_email: str, subject: str, body: str, cc: str = None) -> str:
    """Send email notification.
    
    Args:
        to_email: Recipient email address
        subject: Email subject
        body: Email body content
        cc: CC recipients (comma-separated)
    """
    try:
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        import os
        
        # Configuration
        smtp_server = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
        smtp_port = int(os.getenv('SMTP_PORT', '587'))
        smtp_user = os.getenv('SMTP_USER')
        smtp_password = os.getenv('SMTP_PASSWORD')
        
        if not smtp_user or not smtp_password:
            return "Error: SMTP credentials not configured"
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = smtp_user
        msg['To'] = to_email
        msg['Subject'] = subject
        
        if cc:
            msg['Cc'] = cc
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        
        recipients = [to_email] + ([cc] if cc else [])
        server.send_message(msg, to_addrs=recipients)
        server.quit()
        
        return f"Email sent successfully to {to_email}"
        
    except Exception as e:
        return f"Email sending failed: {str(e)}"
```

## Tool Generation Features

### Error Handling Patterns
1. **Input Validation** - Check parameter types and values
2. **Exception Handling** - Catch and handle specific errors
3. **Security Checks** - Validate file paths and API calls
4. **Resource Limits** - Enforce size and time limits
5. **User-Friendly Messages** - Clear error descriptions

### Security Features
1. **Path Traversal Prevention** - Restrict file access to allowed directories
2. **Input Sanitization** - Clean user inputs before processing
3. **Rate Limiting** - Prevent abuse of external API calls
4. **Authentication** - Secure API key management
5. **Data Validation** - Verify data integrity and format

### Performance Optimizations
1. **Caching** - Cache frequently used results
2. **Async Support** - Asynchronous operations for I/O
3. **Resource Management** - Proper cleanup of resources
4. **Batch Processing** - Process multiple items efficiently
5. **Memory Management** - Limit memory usage for large operations

### Logging and Monitoring
1. **Operation Logging** - Log all tool operations
2. **Performance Metrics** - Track execution times
3. **Error Tracking** - Monitor and analyze errors
4. **Usage Statistics** - Track tool usage patterns
5. **Debug Information** - Provide detailed debug output

## Best Practices

### Tool Design
1. **Single Responsibility** - Each tool should do one thing well
2. **Clear Interface** - Simple, intuitive function signatures
3. **Comprehensive Documentation** - Clear docstrings and examples
4. **Robust Error Handling** - Graceful failure modes
5. **Consistent Patterns** - Follow established conventions

### Security Considerations
1. **Input Validation** - Never trust user inputs
2. **Principle of Least Privilege** - Minimal necessary permissions
3. **Secure Defaults** - Secure configuration by default
4. **Regular Auditing** - Review and update security measures
5. **Dependency Management** - Keep dependencies updated

### Testing Strategy
1. **Unit Tests** - Test individual components
2. **Integration Tests** - Test tool integration with agents
3. **Security Tests** - Test security measures
4. **Performance Tests** - Measure and optimize performance
5. **Edge Case Testing** - Test unusual scenarios

This skill provides comprehensive tool generation capabilities, enabling rapid development of secure, efficient, and reliable Pydantic AI agent tools.