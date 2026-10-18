
CAREER_PATHS = {
    "AI Engineer": [
        ("Python Programming", "Learn Python syntax, variables, loops, functions and OOP."),
        ("Mathematics for AI", "Study linear algebra, probability and basic statistics."),
        ("NumPy and Pandas", "Practise numerical computing and data analysis."),
        ("Machine Learning", "Learn regression, classification and model evaluation."),
        ("Deep Learning", "Understand neural networks and introductory deep learning."),
        ("NLP and Generative AI", "Explore text processing, LLM concepts and prompt engineering."),
        ("AI Project", "Build and test a small AI application.")
    ],
    "Python Developer": [
        ("Python Fundamentals", "Learn variables, data types, loops and functions."),
        ("Object-Oriented Python", "Practise classes, objects and inheritance."),
        ("File Handling and APIs", "Work with files, JSON and REST APIs."),
        ("SQL and Databases", "Learn SQL queries and database connections."),
        ("Flask or FastAPI", "Build backend applications and API endpoints."),
        ("Testing and Git", "Practise debugging, testing and version control."),
        ("Python Project", "Build and document a complete Python application.")
    ],
    "Data Scientist": [
        ("Python Fundamentals", "Learn Python programming and functions."),
        ("Statistics", "Study descriptive statistics and probability."),
        ("NumPy and Pandas", "Clean, transform and analyse datasets."),
        ("Data Visualization", "Create charts using Matplotlib."),
        ("Machine Learning", "Train and evaluate introductory ML models."),
        ("SQL", "Retrieve and analyse data using SQL."),
        ("Data Science Project", "Complete an end-to-end data analysis project.")
    ],
    "Web Developer": [
        ("HTML", "Build the structure of web pages."),
        ("CSS", "Learn layouts, styling and responsive design."),
        ("JavaScript", "Practise variables, functions and DOM manipulation."),
        ("Frontend Framework", "Build reusable components with React."),
        ("Python Backend", "Learn Flask or FastAPI basics."),
        ("Databases and APIs", "Connect applications to databases and APIs."),
        ("Web Project", "Build and test a complete web application.")
    ]
}

def generate_roadmap(career_goal, current_skills="", level="Beginner", days=30):
    if career_goal not in CAREER_PATHS:
        career_goal = "AI Engineer"

    topics = CAREER_PATHS[career_goal]
    skills = [s.strip() for s in current_skills.split(",") if s.strip()]

    days = max(7, min(int(days), 90))
    total_topics = len(topics)
    roadmap = []

    for index, (topic, description) in enumerate(topics):
        start_day = (index * days // total_topics) + 1
        end_day = ((index + 1) * days // total_topics)

        roadmap.append({
            "id": f"topic_{index + 1}",
            "topic": topic,
            "description": description,
            "start_day": start_day,
            "end_day": max(start_day, end_day),
            "tasks": [
                f"Study the fundamentals of {topic}.",
                f"Practise {topic} with a hands-on exercise.",
                f"Create a small task or mini-project using {topic}."
            ]
        })

    return {
        "career_goal": career_goal,
        "current_skills": skills,
        "level": level,
        "duration_days": days,
        "roadmap": roadmap
    }

def get_available_career_paths():
    return list(CAREER_PATHS.keys())