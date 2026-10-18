
from fastmcp import FastMCP

from src.roadmap_engine import (
    generate_roadmap,
    get_available_career_paths
)
from src.resource_finder import get_learning_resources as find_learning_resources

mcp = FastMCP("AI Learning Path Generator")

@mcp.tool()
def get_career_paths():
    """List all career paths supported by the application."""
    return get_available_career_paths()

@mcp.tool()
def generate_learning_roadmap(
    career_goal: str,
    current_skills: str = "",
    level: str = "Beginner"
):
    """Generate a personalized 30-day learning roadmap."""
    return generate_roadmap(
        career_goal=career_goal,
        current_skills=current_skills,
        level=level,
        days=30
    )

@mcp.tool()
def get_learning_resources(topic: str):
    """Find recommended learning resources for a topic."""
    return find_learning_resources(topic)

if __name__ == "__main__":
    mcp.run(transport="stdio")