# Complete Usage Guide for Coding Agents

This comprehensive guide helps coding agents understand user commands and implement complete solutions using the agent template repository.

## Quick Reference Matrix

| User Request | Implementation Steps | Code Pattern |
|--------------|---------------------|--------------|
| "Create a new agent" | 1. Update SYSTEM_PROMPT<br>2. Add/modify tools<br>3. Test with `./run_interface.sh` | See Basic Setup |
| "Add [feature] functionality" | 1. Create tool function<br>2. Add error handling<br>3. Test in isolation | See Tool Patterns |
| "Make it work with [model]" | 1. Add API key to .env<br>2. Update models list<br>3. Test connectivity | See Model Integration |
| "Add [service] integration" | 1. Add dependency to pyproject.toml<br>2. Create API tool<br>3. Handle auth/errors | See API Integration |
| "Customize the interface" | 1. Modify main.py app config<br>2. Update run_interface.sh<br>3. Add styling if needed | See Web Interface |

## End-to-End Implementation Workflows

### Workflow 1: Creating a Domain-Specific Agent

**User Request**: "Create an AI assistant for medical researchers"

#### Step 1: Analyze Requirements
```python
# Domain: Medical Research
# Key Features: Paper search, data analysis, citation formatting
# Privacy: High - medical data sensitivity
# Models: Claude Sonnet (best for analysis)
```

#### Step 2: Implement Agent
```python
from pydantic_ai import Agent
from dotenv import load_dotenv
import requests
import json

# Specialized system prompt
SYSTEM_PROMPT = """
You are a medical research assistant. Your expertise includes:
- Literature search and analysis
- Clinical trial data interpretation
- Citation formatting (APA, Vancouver, etc.)
- Medical terminology and concepts

Always maintain patient privacy and HIPAA compliance.
Provide evidence-based information and cite sources clearly.
""".strip()

# Setup specialized agent
agent = Agent(
    system_prompt=SYSTEM_PROMPT,
    output_type=str,
)

# Tool 1: PubMed search
@agent.tool_plain
def search_pubmed(query: str, max_results: int = 10) -> str:
    """Search PubMed for medical literature."""
    try:
        # PubMed API implementation
        base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        params = {
            "db": "pubmed",
            "term": query,
            "retmode": "json",
            "retmax": max_results
        }
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if data.get("esearchresult", {}).get("idlist"):
            ids = data["esearchresult"]["idlist"]
            return f"Found {len(ids)} papers. IDs: {', '.join(ids[:5])}"
        else:
            return "No results found"
    except Exception as e:
        return f"Search error: {str(e)}"

# Tool 2: Citation formatter
@agent.tool_plain
def format_citation(pmid: str, style: str = "apa") -> str:
    """Format citation in specified style."""
    try:
        # Citation formatting logic
        return f"Citation for PMID {pmid} in {style} style: [Formatted citation]"
    except Exception as e:
        return f"Citation error: {str(e)}"

# Tool 3: Medical dictionary
@agent.tool_plain
def define_medical_term(term: str) -> str:
    """Define medical terminology."""
    medical_terms = {
        "rct": "Randomized Controlled Trial",
        "double-blind": "Study where neither participants nor researchers know treatment assignments",
        "placebo": "Inactive substance used as control in clinical trials"
    }
    
    definition = medical_terms.get(term.lower(), f"Definition for '{term}' not found")
    return f"{term}: {definition}"

# Configure web interface
load_dotenv()
app = agent.to_web(
    models=[
        "anthropic:claude-3-5-sonnet",  # Best for medical analysis
        "openai:gpt-4o"  # Backup
    ]
)
```

#### Step 3: Update Dependencies
```toml
# pyproject.toml
dependencies = [
    "pydantic-ai>=1.54.0",
    "python-dotenv>=1.2.1",
    "uvicorn>=0.40.0",
    "requests>=2.31.0",
    "beautifulsoup4>=4.12.0",  # For web scraping
]
```

#### Step 4: Test Implementation
```bash
uv sync  # Install new dependencies
./run_interface.sh
# Test queries:
# - "Search PubMed for COVID-19 vaccine trials"
# - "What is a double-blind study?"
# - "Format this citation in APA style: PMID 12345678"
```

### Workflow 2: Adding API Integration

**User Request**: "Connect this agent to the Stripe API for payment processing"

#### Step 1: Security Planning
```python
# API Keys: Use environment variables only
# Data: Never log sensitive payment information
# Error Handling: Generic error messages for users
# Compliance: PCI DSS considerations
```

#### Step 2: Implement Integration
```python
import os
import stripe
from pydantic_ai import Agent

# Configure Stripe (in production, load from environment)
stripe.api_key = os.getenv('STRIPE_API_KEY')

@agent.tool_plain
def create_payment_intent(amount_cents: int, currency: str = "usd") -> str:
    """Create a payment intent for processing."""
    try:
        intent = stripe.PaymentIntent.create(
            amount=amount_cents,
            currency=currency,
            payment_method_types=["card"],
        )
        return f"Payment Intent created: {intent.id} for ${amount_cents/100:.2f}"
    except stripe.error.StripeError as e:
        return f"Payment error: Unable to process request"
    except Exception as e:
        return f"System error: Please try again later"

@agent.tool_plain
def check_payment_status(payment_intent_id: str) -> str:
    """Check status of a payment intent."""
    try:
        intent = stripe.PaymentIntent.retrieve(payment_intent_id)
        return f"Payment status: {intent.status}"
    except stripe.error.StripeError:
        return "Payment not found"
    except Exception:
        return "Unable to check payment status"

@agent.tool_plain
def refund_payment(payment_intent_id: str, amount_cents: int = None) -> str:
    """Process a refund for a payment."""
    try:
        # Get payment intent to verify amount if not specified
        if not amount_cents:
            intent = stripe.PaymentIntent.retrieve(payment_intent_id)
            amount_cents = intent.amount
            
        refund = stripe.Refund.create(
            payment_intent=payment_intent_id,
            amount=amount_cents
        )
        return f"Refund processed: ${amount_cents/100:.2f}"
    except stripe.error.StripeError as e:
        return f"Refund failed: Unable to process at this time"
```

#### Step 3: Environment Configuration
```env
# .env file
OPENAI_API_KEY=your_openai_key
STRIPE_API_KEY=sk_live_your_stripe_key  # Use sk_test_ for development
STRIPE_WEBHOOK_SECRET=whsec_your_webhook_secret
```

#### Step 4: Testing Strategy
```python
# Add test at bottom of main.py
if __name__ == "__main__":
    import asyncio
    
    async def test_payment_flow():
        # Test creating a payment intent
        result = await agent.run(
            "Create a payment intent for $19.99"
        )
        print("Payment test:", result.output)
    
    asyncio.run(test_payment_flow())
```

### Workflow 3: Creating Multi-Agent System

**User Request**: "Build a customer service system with separate agents for sales, support, and billing"

#### Step 1: Agent Architecture
```python
# agents.py - Separate agent definitions
from pydantic_ai import Agent
from typing import Dict, Any

# Sales Agent
sales_agent = Agent(
    system_prompt="""
    You are a sales assistant. Help customers with:
    - Product information and recommendations
    - Pricing and package details
    - Demo scheduling
    - Trial setup
    """.strip(),
    output_type=str,
)

# Support Agent
support_agent = Agent(
    system_prompt="""
    You are a technical support assistant. Help with:
    - Troubleshooting technical issues
    - Account access problems
    - Feature usage guidance
    - Bug reporting and escalation
    """.strip(),
    output_type=str,
)

# Billing Agent
billing_agent = Agent(
    system_prompt="""
    You are a billing assistant. Help with:
    - Invoice inquiries
    - Payment processing
    - Subscription management
    - Refund requests
    """.strip(),
    output_type=str,
)

# Router Agent - Determines which agent to use
router_agent = Agent(
    system_prompt="""
    You are a customer service router. Analyze the customer's request
    and route to the appropriate specialized agent:
    
    - Sales: Product questions, pricing, demos
    - Support: Technical issues, account problems
    - Billing: Invoices, payments, subscriptions
    
    Respond with one of: SALES, SUPPORT, BILLING, or GENERAL
    """.strip(),
    output_type=str,
)
```

#### Step 2: Main Integration
```python
# main.py
from pydantic_ai import Agent, RunContext
from agents import sales_agent, support_agent, billing_agent, router_agent
from dotenv import load_dotenv

# Router tool
@router_agent.tool_plain
def route_request(customer_query: str) -> str:
    """Route customer request to appropriate agent."""
    # Simple keyword-based routing
    query_lower = customer_query.lower()
    
    if any(word in query_lower for word in ["buy", "price", "cost", "demo"]):
        return "SALES"
    elif any(word in query_lower for word in ["broken", "error", "login", "account"]):
        return "SUPPORT"
    elif any(word in query_lower for word in ["invoice", "bill", "payment", "refund"]):
        return "BILLING"
    else:
        return "GENERAL"

# Main dispatcher
async def handle_customer_request(query: str) -> str:
    """Route and handle customer request."""
    # First determine routing
    route_result = await router_agent.run(f"Route this request: {query}")
    agent_type = route_result.output.strip().upper()
    
    # Route to appropriate agent
    if agent_type == "SALES":
        result = await sales_agent.run(query)
    elif agent_type == "SUPPORT":
        result = await support_agent.run(query)
    elif agent_type == "BILLING":
        result = await billing_agent.run(query)
    else:
        result = await sales_agent.run(query)  # Default to sales
    
    return result.output

# Create web interface
load_dotenv()
app = router_agent.to_web(
    models=["openai:gpt-4o"]  # Good for routing decisions
)
```

### Workflow 4: Adding Advanced Features

**User Request**: "Add file upload, data processing, and report generation capabilities"

#### Step 1: File Upload Implementation
```python
from fastapi import FastAPI, UploadFile, File
from pydantic_ai import Agent
import pandas as pd
import io
import json

# Add file processing tools
@agent.tool_plain
def process_uploaded_file(file_content: str, file_type: str) -> str:
    """Process uploaded file and return summary."""
    try:
        if file_type == "csv":
            df = pd.read_csv(io.StringIO(file_content))
            summary = f"""
            File Analysis:
            - Rows: {len(df)}
            - Columns: {len(df.columns)}
            - Column names: {', '.join(df.columns.tolist())}
            - Data types: {df.dtypes.to_dict()}
            - First 3 rows: {df.head(3).to_string()}
            """
            return summary
        
        elif file_type == "json":
            data = json.loads(file_content)
            if isinstance(data, list):
                return f"JSON array with {len(data)} items"
            elif isinstance(data, dict):
                return f"JSON object with keys: {list(data.keys())}"
            else:
                return f"JSON data: {type(data).__name__}"
        
        else:
            return f"Unsupported file type: {file_type}"
            
    except Exception as e:
        return f"Error processing file: {str(e)}"

@agent.tool_plain
def generate_report(data_summary: str, report_type: str = "summary") -> str:
    """Generate a report based on processed data."""
    try:
        if report_type == "summary":
            return f"""
            # Data Summary Report
            
            {data_summary}
            
            ## Recommendations
            - Review data quality metrics
            - Consider data cleaning steps
            - Plan visualization strategy
            """
        elif report_type == "detailed":
            return f"""
            # Detailed Analysis Report
            
            ## Overview
            {data_summary}
            
            ## Next Steps
            1. Data validation
            2. Statistical analysis
            3. Visualization creation
            4. Insight generation
            """
        else:
            return f"Report type '{report_type}' not supported"
            
    except Exception as e:
        return f"Error generating report: {str(e)}"
```

#### Step 2: Enhanced Web Interface
```python
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
import uvicorn

# Enhanced app with file upload
app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """Handle file upload and processing."""
    try:
        content = await file.read()
        content_str = content.decode('utf-8')
        file_type = file.filename.split('.')[-1]
        
        # Process with agent
        result = await agent.run(
            f"Process this {file_type} file: {content_str[:1000]}..."
        )
        
        return {"result": result.output, "status": "success"}
        
    except Exception as e:
        return {"error": str(e), "status": "error"}

# Enhanced homepage with upload UI
@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
        <body>
            <h1>AI Agent Interface</h1>
            <form action="/upload" method="post" enctype="multipart/form-data">
                <input type="file" name="file" accept=".csv,.json,.txt">
                <button type="submit">Upload and Process</button>
            </form>
            <hr>
            <!-- Regular chat interface would go here -->
        </body>
    </html>
    """
```

## Common Implementation Patterns

### Pattern 1: Configuration Management
```python
# config.py
from dataclasses import dataclass
from typing import Dict, List
import os

@dataclass
class AgentConfig:
    name: str
    system_prompt: str
    models: List[str]
    tools: List[str]
    skills_directories: List[str]

def load_agent_config(config_path: str = "agent_config.json") -> AgentConfig:
    """Load agent configuration from file."""
    try:
        with open(config_path, 'r') as f:
            config_data = json.load(f)
        return AgentConfig(**config_data)
    except FileNotFoundError:
        # Return default configuration
        return AgentConfig(
            name="default_agent",
            system_prompt="You are a helpful AI assistant.",
            models=["google-gla:gemini-3-flash"],
            tools=["roll_dice"],
            skills_directories=["./skills"]
        )
```

### Pattern 2: Error Handling Wrapper
```python
def safe_tool_wrapper(tool_func):
    """Decorator for safe tool execution with error handling."""
    def wrapper(*args, **kwargs):
        try:
            return tool_func(*args, **kwargs)
        except ValueError as e:
            return f"Invalid input: {str(e)}"
        except PermissionError:
            return "Permission denied: Check file/folder permissions"
        except ConnectionError:
            return "Connection error: Check network connectivity"
        except Exception as e:
            return f"Unexpected error: Please try again later"
    return wrapper

# Usage
@agent.tool_plain
@safe_tool_wrapper
def risky_operation(file_path: str) -> str:
    """Tool with automatic error handling."""
    # Risky operation code here
    return "Operation completed successfully"
```

### Pattern 3: Logging and Monitoring
```python
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('agent_activity.log'),
        logging.StreamHandler()
    ]
)

def log_agent_activity(activity_type: str, details: Dict[str, Any]):
    """Log agent activities for monitoring."""
    timestamp = datetime.now().isoformat()
    log_entry = {
        "timestamp": timestamp,
        "activity": activity_type,
        "details": details
    }
    logging.info(f"Agent Activity: {json.dumps(log_entry)}")

# Usage in tools
@agent.tool_plain
def monitored_tool(param: str) -> str:
    """Tool with activity monitoring."""
    log_agent_activity("tool_call", {"tool": "monitored_tool", "param": param})
    
    try:
        result = f"Processed: {param}"
        log_agent_activity("tool_success", {"result": result})
        return result
    except Exception as e:
        log_agent_activity("tool_error", {"error": str(e)})
        raise
```

## Testing Strategies

### 1. Unit Testing Tools
```python
import pytest
from main import agent

@pytest.mark.asyncio
async def test_roll_dice_tool():
    """Test the roll_dice tool returns valid results."""
    result = await agent.run("Roll a dice for me")
    assert result.output in ["1", "2", "3", "4", "5", "6"]

@pytest.mark.asyncio
async def test_file_processing():
    """Test file processing capabilities."""
    test_csv = "name,age\nJohn,25\nJane,30"
    result = await agent.run(f"Process this CSV: {test_csv}")
    assert "Rows: 2" in result.output
```

### 2. Integration Testing
```python
@pytest.mark.asyncio
async def test_full_workflow():
    """Test complete user workflow."""
    # Test file upload
    # Test data processing
    # Test report generation
    pass
```

### 3. Performance Testing
```python
import time
import asyncio

async def measure_response_time(query: str) -> float:
    """Measure agent response time."""
    start_time = time.time()
    await agent.run(query)
    end_time = time.time()
    return end_time - start_time

async def performance_test():
    """Run performance tests."""
    queries = [
        "Roll a dice",
        "What's 2+2?",
        "Tell me a joke"
    ]
    
    times = []
    for query in queries:
        response_time = await measure_response_time(query)
        times.append(response_time)
        print(f"Query: {query} - Time: {response_time:.2f}s")
    
    avg_time = sum(times) / len(times)
    print(f"Average response time: {avg_time:.2f}s")
```

## Deployment Checklist

### Pre-Deployment
- [ ] All tests passing
- [ ] API keys configured (use environment variables)
- [ ] Dependencies up to date
- [ ] Error handling implemented
- [ ] Logging configured
- [ ] Documentation updated

### Security Review
- [ ] No hardcoded secrets
- [ ] Input validation implemented
- [ ] File access restrictions
- [ ] API rate limiting considered
- [ ] HTTPS for production

### Performance Optimization
- [ ] Caching implemented where appropriate
- [ ] Database queries optimized
- [ ] Memory usage monitored
- [ ] Response times acceptable
- [ ] Scalability considerations

This guide provides coding agents with comprehensive patterns for implementing complete, production-ready AI solutions using the template repository.