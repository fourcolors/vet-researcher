"""
API models for the veterinary research service.
"""

from pydantic import BaseModel, Field


class AnalysisRequest(BaseModel):
    """Request model for veterinary analysis."""
    query: str = Field(
        ...,
        description="The veterinary case or question to analyze",
        min_length=10,
        example="My 5-year-old golden retriever has been limping on his right front leg for 2 days",
    )


class AnalysisResponse(BaseModel):
    """Response model for veterinary analysis."""
    result: str = Field(
        ...,
        description="The detailed analysis result from the veterinary workflow",
    )
    success: bool = Field(
        default=True,
        description="Whether the analysis was successful",
    )


class ErrorResponse(BaseModel):
    """Error response model."""
    success: bool = Field(
        default=False,
        description="Whether the request was successful",
    )
    error: str = Field(
        ...,
        description="Error message describing what went wrong",
    ) 