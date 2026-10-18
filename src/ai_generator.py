
from src.roadmap_engine import generate_roadmap

def create_learning_path(career_goal, current_skills="", level="Beginner", days=30):
    """Create a personalized learning path."""
    return generate_roadmap(
        career_goal=career_goal,
        current_skills=current_skills,
        level=level,
        days=days
    )