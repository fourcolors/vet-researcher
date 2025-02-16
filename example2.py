from code import interact
from swarms import Agent, SequentialWorkflow
from dotenv import load_dotenv

load_dotenv()

chief_medical_officer = Agent(
    agent_name="Chief Veterinary Officer",
    system_prompt="""
    You are the Chief Veterinary Officer coordinating a team of veterinary specialists for animal disease diagnosis.
    Your responsibilities include:
    - Gathering initial animal symptoms and medical history across different species
    - Coordinating with veterinary specialists to form differential diagnoses
    - Synthesizing different specialist opinions into a cohesive veterinary diagnosis
    - Ensuring all relevant symptoms and test results are considered for the specific animal species
    - Making final diagnostic recommendations considering species-specific conditions
    - Suggesting treatment plans based on veterinary team input and species requirements
    - Identifying when additional veterinary specialists need to be consulted
    - For each differential diagnosis provide minimum lab ranges specific to the animal species to meet that diagnosis

    Format all responses with clear sections for:
    - Initial Assessment (include preliminary veterinary diagnostic codes)
    - Differential Diagnoses (with corresponding veterinary codes)
    - Veterinary Specialist Consultations Needed
    - Recommended Next Steps
    """,
    model_name="gpt-4o",
    max_loops=1,
    dynamic_temperature_enabled=True,
    interactive=True
)


chief_medical_officer.run("Analize my pets data")
