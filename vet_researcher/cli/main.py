"""
Command-line interface for veterinary research tool.
"""

import os
from typing import Optional

import click
from dotenv import load_dotenv

from vet_researcher.core.workflow import create_research_workflow


@click.group()
def cli():
    """Veterinary research and analysis tools."""
    load_dotenv()


@cli.command()
@click.argument("query")
@click.option(
    "--output",
    "-o",
    type=click.Path(),
    help="Path to save the analysis results.",
)
def analyze(query: str, output: Optional[str] = None):
    """
    Analyze a veterinary case or medical query.
    
    Args:
        query: The veterinary case or question to analyze
        output: Optional path to save the analysis results
    """
    workflow = create_research_workflow()
    result = workflow.run(query)
    
    if output:
        os.makedirs(os.path.dirname(output) or ".", exist_ok=True)
        with open(output, "w") as f:
            f.write(result)
    else:
        click.echo(result)


if __name__ == "__main__":
    cli() 