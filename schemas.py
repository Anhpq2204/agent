from typing import List
from pydantic import BaseModel, Field

class PaperSummary(BaseModel):
    title: str = Field(description="The title of the paper, used as citation")
    problem: str = Field(description="The problem the paper addresses")
    method: str = Field(description="The method proposed or used")
    key_contribution: str = Field(description="The key contribution of the paper")
    main_biological_insight: str = Field(description="The main biological insight derived")

class StructuredExtraction(BaseModel):
    datasets: str = Field(description="Dataset(s) used in the paper")
    data_type: str = Field(description="Type of gene expression (bulk / single-cell / spatial)")
    model_method: str = Field(description="Model / method (statistical / ML / DL / graph / transformer)")
    evaluation_metrics: str = Field(description="Evaluation metrics used")
    baselines: str = Field(description="Baselines compared against")

class PaperAnalysis(BaseModel):
    summary: PaperSummary
    extraction: StructuredExtraction

class ResearchIdea(BaseModel):
    problem_motivation: str = Field(description="Problem motivation")
    proposed_method: str = Field(description="Proposed method to solve the problem")
    expected_contribution: str = Field(description="Expected contribution to the field")
    possible_dataset: str = Field(description="Possible dataset to use for this idea")

class ResearchIdeas(BaseModel):
    ideas: List[ResearchIdea] = Field(description="List of 3 to 7 research ideas")
