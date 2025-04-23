import argparse
import logging
import json
import os
from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import Prompt

from agent_center.chain import CodeExplainerAgent

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

# Initialize Rich console for prettier output
console = Console()


def main():
    """Main entry point for the code explainer agent."""
    parser = argparse.ArgumentParser(
        description="Code Explainer Agent - Analyze and explain code functions"
    )
    parser.add_argument(
        "--input",
        type=str,
        default="examples/dummy_input.json",
        help="Path to input JSON file containing code functions"
    )
    parser.add_argument(
        "--model",
        type=str,
        default="gpt-4o-mini",
        help="OpenAI model to use (default: gpt-4o-mini)"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="outputs/analysis.md",
        help="Path to save output markdown file"
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Run in interactive mode"
    )
    parser.add_argument(
        "--query",
        type=str,
        help="Query to analyze (if not in interactive mode)"
    )

    args = parser.parse_args()

    # Ensure OPENAI_API_KEY is set
    if not os.getenv("OPENAI_API_KEY"):
        console.print("[bold red]Error: OPENAI_API_KEY environment variable not set[/bold red]")
        return

    # Display welcome message
    console.print(
        "[bold blue]🧠 Code Explainer Agent[/bold blue]"
        "\n[bold]This agent analyzes code and explains what it does.[/bold]"
    )
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(args.output), exist_ok=True)

    # Initialize agent
    agent = CodeExplainerAgent(model=args.model)
    
    try:
        if args.interactive:
            # Interactive mode
            console.print("\n[bold]Interactive mode:[/bold] Type 'exit' to quit")
            
            while True:
                query = Prompt.ask("\n[bold green]What would you like to know about the code?[/bold green]")
                
                if query.lower() == 'exit':
                    break
                    
                # Process query
                console.print(f"[bold]Processing query:[/bold] {query}")
                result = agent.process_query(query, args.input)
                
                # Save to file if markdown is available
                if "markdown" in result:
                    with open(args.output, "w") as f:
                        f.write(result["markdown"])
                    console.print(f"[bold]Results saved to:[/bold] {args.output}")
                
                # Display results
                display_results(result)
                
        else:
            # Single query mode
            if not args.query:
                console.print("[bold yellow]No query provided. Use --query or --interactive[/bold yellow]")
                return
                
            console.print(f"[bold]Processing query:[/bold] {args.query}")
            result = agent.process_query(args.query, args.input)
            
            # Save to file if markdown is available
            if "markdown" in result:
                with open(args.output, "w") as f:
                    f.write(result["markdown"])
                console.print(f"[bold]Results saved to:[/bold] {args.output}")
            
            # Display results
            display_results(result)
            
    except Exception as e:
        console.print(f"[bold red]Error: {str(e)}[/bold red]")
        logger.exception("An error occurred during execution")


def display_results(result):
    """Display results to the console"""
    
    if "error" in result:
        console.print(f"[bold red]Error:[/bold red] {result['error']}")
        return
        
    # Display overall analysis if available
    if "overall_analysis" in result:
        console.print("\n[bold]Overall Analysis:[/bold]")
        console.print(Markdown(result["overall_analysis"]))
    
    # Display function summaries
    if "summarized_functions" in result:
        console.print("\n[bold]Function Summaries:[/bold]")
        for func in result["summarized_functions"]:
            console.print(f"\n[bold cyan]{func['name']}[/bold cyan]")
            console.print(Markdown(func["explanation"]))
            
    elif "important_functions" in result:
        console.print("\n[bold]Important Functions:[/bold]")
        for func in result["important_functions"]:
            console.print(f"\n[bold cyan]{func['name']}[/bold cyan]")
            console.print(Markdown(func["explanation"]))
            
    elif "function_summary" in result:
        console.print("\n[bold]Function Summary:[/bold]")
        for func in result["function_summary"]:
            console.print(f"\n[bold cyan]{func['name']}[/bold cyan]")
            console.print(Markdown(func["explanation"]))


if __name__ == "__main__":
    main()
