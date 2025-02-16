"""
FastAPI application for the veterinary research service.
"""

import logging
from typing import Union

import uvicorn
from api.models import AnalysisRequest, AnalysisResponse, ErrorResponse
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from vet_researcher.core.workflow import create_research_workflow

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="Veterinary Research API",
    description="API for analyzing veterinary medical cases using AI agents",
    version="0.1.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.post(
    "/analyze",
    response_model=Union[AnalysisResponse, ErrorResponse],
    description="Analyze a veterinary case using AI agents",
    responses={
        200: {"model": AnalysisResponse, "description": "Successful analysis"},
        422: {"model": ErrorResponse, "description": "Invalid input"},
        500: {"model": ErrorResponse, "description": "Server error"},
    },
)
async def analyze_case(request: AnalysisRequest) -> Union[AnalysisResponse, ErrorResponse]:
    """
    Analyze a veterinary case using the AI agent workflow.
    
    Args:
        request: The analysis request containing the query
        
    Returns:
        The analysis response with results or error
        
    Raises:
        HTTPException: If there's an error processing the request
    """
    try:
        logger.info(f"Analyzing case with query: {request.query[:100]}...")
        
        # Create and run the workflow
        workflow = create_research_workflow()
        result = workflow.run(request.query)
        
        logger.info("Analysis completed successfully")
        return AnalysisResponse(result=result)
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Error processing request: {str(e)}",
        )


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


if __name__ == "__main__":
    logger.info("Starting API server...")
    uvicorn.run(
        "api.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info",
    ) 