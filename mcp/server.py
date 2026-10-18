from fastmcp import FastMCP

from src.roadmap_engine import get_career_paths, generate_roadmap
from src.resource_finder import find_resources

mcp = FastMCP("AI Learning Path Generator")


@mcp.tool()
def available_career_paths():
    """Get all available career paths."""
    return get_career_paths()


@mcp.tool()
def create_learning_roadmap(
    career_goal: str,
    current_skills: str = "",
    level: str = "Beginner"
):
    """Create a personalized learning roadmap."""
    return generate_roadmap(
        career_goal,
        current_skills,
        level
    )


@mcp.tool()
def get_learning_resources(topic: str):
    """Find learning resources for a topic."""
    return find_resources(topic)


if __name__ == "__main__":
    mcp.run()