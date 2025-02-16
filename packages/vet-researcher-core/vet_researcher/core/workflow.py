"""
Workflow management for veterinary research and analysis.
"""

from swarms import SequentialWorkflow

from vet_researcher.core.agents import (
    create_chief_medical_officer,
    create_internist,
    create_lab_matcher,
    create_medical_coder,
    create_summarizer,
    create_synthesizer,
)


def create_research_workflow() -> SequentialWorkflow:
    """
    Create a sequential workflow of veterinary research agents.
    
    Returns:
        SequentialWorkflow: The configured workflow with all agents.
    """
    return SequentialWorkflow(
        agents=[
            create_chief_medical_officer(),
            create_internist(),
            create_medical_coder(),
            create_synthesizer(),
            create_summarizer(),
            create_lab_matcher(),
        ],
        workflow_name="veterinary-research-workflow",
    ) 