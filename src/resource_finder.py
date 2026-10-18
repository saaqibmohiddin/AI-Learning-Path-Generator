
RESOURCE_LIBRARY = {
    "python": [
        {"name": "Python Official Tutorial", "url": "https://docs.python.org/3/tutorial/"},
        {"name": "W3Schools Python", "url": "https://www.w3schools.com/python/"},
        {"name": "Kaggle Learn", "url": "https://www.kaggle.com/learn"}
    ],
    "mathematics": [
        {"name": "Khan Academy", "url": "https://www.khanacademy.org/math"},
        {"name": "3Blue1Brown", "url": "https://www.3blue1brown.com/"},
        {"name": "StatQuest", "url": "https://statquest.org/"}
    ],
    "numpy": [
        {"name": "NumPy Documentation", "url": "https://numpy.org/learn/"},
        {"name": "Pandas Documentation", "url": "https://pandas.pydata.org/docs/"},
        {"name": "Kaggle Learn", "url": "https://www.kaggle.com/learn"}
    ],
    "machine learning": [
        {"name": "Google Machine Learning Crash Course", "url": "https://developers.google.com/machine-learning/crash-course"},
        {"name": "Scikit-learn Guide", "url": "https://scikit-learn.org/stable/user_guide.html"},
        {"name": "Kaggle Learn", "url": "https://www.kaggle.com/learn"}
    ],
    "deep learning": [
        {"name": "PyTorch Tutorials", "url": "https://pytorch.org/tutorials/"},
        {"name": "TensorFlow Tutorials", "url": "https://www.tensorflow.org/tutorials"},
        {"name": "fast.ai", "url": "https://course.fast.ai/"}
    ],
    "nlp": [
        {"name": "Hugging Face NLP Course", "url": "https://huggingface.co/learn/nlp-course"},
        {"name": "NLTK Book", "url": "https://www.nltk.org/book/"},
        {"name": "spaCy Course", "url": "https://course.spacy.io/"}
    ],
    "generative ai": [
        {"name": "Microsoft Generative AI for Beginners", "url": "https://github.com/microsoft/generative-ai-for-beginners"},
        {"name": "Hugging Face Learn", "url": "https://huggingface.co/learn"},
        {"name": "Google AI Learning", "url": "https://ai.google/learn/"}
    ],
    "html": [
        {"name": "MDN HTML Guide", "url": "https://developer.mozilla.org/en-US/docs/Web/HTML"},
        {"name": "W3Schools HTML", "url": "https://www.w3schools.com/html/"}
    ],
    "css": [
        {"name": "MDN CSS Guide", "url": "https://developer.mozilla.org/en-US/docs/Web/CSS"},
        {"name": "CSS-Tricks", "url": "https://css-tricks.com/"}
    ],
    "javascript": [
        {"name": "MDN JavaScript Guide", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript"},
        {"name": "JavaScript.info", "url": "https://javascript.info/"}
    ],
    "react": [
        {"name": "React Official Learn", "url": "https://react.dev/learn"},
        {"name": "W3Schools React", "url": "https://www.w3schools.com/react/"}
    ],
    "sql": [
        {"name": "SQLBolt", "url": "https://sqlbolt.com/"},
        {"name": "W3Schools SQL", "url": "https://www.w3schools.com/sql/"}
    ],
    "statistics": [
        {"name": "Khan Academy Statistics", "url": "https://www.khanacademy.org/math/statistics-probability"},
        {"name": "StatQuest", "url": "https://statquest.org/"}
    ],
    "data visualization": [
        {"name": "Matplotlib Tutorials", "url": "https://matplotlib.org/stable/tutorials/"},
        {"name": "Plotly Python", "url": "https://plotly.com/python/"}
    ],
    "flask": [
        {"name": "Flask Documentation", "url": "https://flask.palletsprojects.com/"},
        {"name": "FastAPI Documentation", "url": "https://fastapi.tiangolo.com/"}
    ],
    "object-oriented python": [
        {"name": "Python Classes Tutorial", "url": "https://docs.python.org/3/tutorial/classes.html"},
        {"name": "Real Python OOP", "url": "https://realpython.com/python3-object-oriented-programming/"}
    ],
    "file handling and apis": [
        {"name": "Python File I/O", "url": "https://docs.python.org/3/tutorial/inputoutput.html"},
        {"name": "Requests Documentation", "url": "https://requests.readthedocs.io/"}
    ],
    "frontend framework": [
        {"name": "React Official Learn", "url": "https://react.dev/learn"},
        {"name": "JavaScript.info", "url": "https://javascript.info/"}
    ],
    "databases and apis": [
        {"name": "SQLBolt", "url": "https://sqlbolt.com/"},
        {"name": "REST API Tutorial", "url": "https://restfulapi.net/"}
    ],
    "testing and git": [
        {"name": "Git Documentation", "url": "https://git-scm.com/doc"},
        {"name": "Pytest Documentation", "url": "https://docs.pytest.org/"}
    ]
}

def get_learning_resources(topic):
    topic_lower = topic.lower()

    for keyword, resources in RESOURCE_LIBRARY.items():
        if keyword in topic_lower or topic_lower in keyword:
            return resources

    if "data" in topic_lower:
        return RESOURCE_LIBRARY["numpy"]

    if "ai" in topic_lower:
        return RESOURCE_LIBRARY["machine learning"]

    return [
        {"name": "Google Search for learning resources", "url": "https://www.google.com/search?q=" + topic.replace(" ", "+")},
        {"name": "YouTube Tutorials", "url": "https://www.youtube.com/results?search_query=" + topic.replace(" ", "+")}
    ]