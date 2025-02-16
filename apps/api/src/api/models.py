"""
API models for request and response data.
"""

from pydantic import BaseModel


class AnalysisRequest(BaseModel):
    """
    Request model for case analysis.
    
    Attributes:
        query: The veterinary case query to analyze
    """
    query: str


class AnalysisResponse(BaseModel):
    """
    Response model for case analysis results.
    
    Attributes:
        result: The analysis result
    """
    result: str


class ErrorResponse(BaseModel):
    """
    Error response model.
    
    Attributes:
        detail: Error message details
    """
    detail: str 