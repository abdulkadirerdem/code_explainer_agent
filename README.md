# Code Explainer Agent - Custom Implementation

## 1. Architecture Overview

For our code explainer agent, we're using a **Triaj-based Agent Architecture**. This architecture:
1. Analyzes the user's query to determine what they're asking about the code
2. Routes the query to the appropriate analysis method
3. Executes the relevant code analysis functions
4. Returns a structured response

## 2. Components

### 2.1 Core Components
- `types.py` - Response models and data types using Pydantic
- `prompt_templates.py` - Templates for various LLM prompts
- `chain.py` - Main implementation of the agent logic
- `main.py` - Entry point for running the agent

### 2.2 Supporting Components
- `core/input_loader.py` - Loads code function data
- `core/function_selector.py` - Selects important functions
- `core/summarizer.py` - Generates summaries of functions
- `core/formatter.py` - Formats outputs as markdown or JSON

## 3. How It Works

### Triaj Agent Approach
The agent uses a triaj approach to handle diverse queries:

1. **Query Analysis**: The agent analyzes the user query to determine what the user is asking about
2. **Action Selection**: Based on the query, the agent selects one or more actions to perform:
   - Explain all code functions
   - Find and explain important functions
   - Summarize a specific function
   - Provide an overall analysis
3. **Execution**: The agent executes the selected actions
4. **Response Generation**: Results are formatted and returned to the user

### Key Features
- Interactive mode for continuous querying
- Handles various types of code-related questions
- Uses OpenAI function calling for structured responses
- Generates markdown documentation for code explanations

## 4. Usage Instructions

### Prerequisites
- Python 3.8 or higher
- OpenAI API key

### Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/code_explainer_agent.git
cd code_explainer_agent
```

2. Install dependencies:
```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

3. Set your OpenAI API key:
```bash
export OPENAI_API_KEY=your-api-key-here
```

### Running the Agent

#### Interactive Mode
Run the agent in interactive mode to ask multiple questions:
```bash
python main.py --interactive --input examples/dummy_input.json
```

#### Single Query Mode
Run the agent with a specific query:
```bash
python main.py --query "What are the most important functions in this code?" --input examples/dummy_input.json
```

### Command Line Arguments
- `--input`: Path to input JSON file (default: "examples/dummy_input.json")
- `--model`: OpenAI model to use (default: "gpt-4o-mini")
- `--output`: Path to save output markdown file (default: "outputs/analysis.md")
- `--interactive`: Run in interactive mode
- `--query`: Specific query to analyze (when not in interactive mode)

### Example Queries
- "Explain what this code does"
- "What are the 5 most important functions?"
- "Summarize the create_user function"
- "Give me an overall analysis of this codebase"
- "What does the initialize_app function do?"
