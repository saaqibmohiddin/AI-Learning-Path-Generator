🚀 AI Learning Path Generator

Your Career Goals. Your Skills. Your Personalized Learning Journey.

An AI-assisted learning roadmap application that helps learners plan their career development through structured, day-wise learning paths, topic-based resources, and progress tracking.

---

✨ About the Project

AI Learning Path Generator helps learners organize their technical learning based on their career goals, current skills, experience level, and available learning time.

Instead of following a random collection of tutorials, users can generate a structured learning roadmap for a selected career path, explore relevant learning resources, complete practical tasks, and track their progress.

The project supports multiple interfaces and provides roadmap export options to make learning easier to manage.

💡 Key Features

Feature| Description
🎯 Career Selection| Choose a career path based on your goal.
🧭 Personalized Roadmap| Generate a structured schedule using your selected skills and experience level.
📅 Flexible Duration| Choose 30, 45, 60, or 90 days.
📚 Learning Resources| Find learning links related to roadmap topics.
✅ Progress Tracking| Mark topics as completed and monitor completion percentage.
📄 Roadmap Export| Export your learning roadmap in Markdown or PDF format.
🖥️ Multiple Interfaces| Use the Streamlit or Flask application.
🔌 MCP Integration| Access learning-path and resource-finding tools through the MCP server.

🎓 Supported Career Paths

The application currently includes these career options:

- AI Engineer
- Python Developer
- Data Scientist
- Web Developer

⚙️ How It Works

01 — Choose Your Career

Select the career path you want to pursue.

02 — Enter Your Learning Profile

Provide your name, current skills, and experience level.

03 — Select Your Duration

Choose a learning period of 30, 45, 60, or 90 days.

04 — Generate Your Roadmap

The roadmap engine organizes career-related topics into a day-wise learning schedule with practical tasks.

05 — Explore Learning Resources

Find relevant learning links for the topics in your roadmap.

06 — Track Your Progress

Mark completed topics and monitor your learning progress.

07 — Export Your Roadmap

Save your roadmap as a Markdown or PDF document.

🛠️ Technology Stack

Technology| Purpose
Python| Core application logic
Streamlit| Interactive application interface
Flask| Web application interface
ReportLab| PDF generation
FastMCP| Model Context Protocol integration
Markdown| Roadmap export format

📁 Project Structure

AI-Learning-Path-Generator/
│
├── app.py
├── web_app.py
├── learning_path_mcp.py
├── requirements.txt
│
└── src/
    ├── roadmap_engine.py
    ├── resource_finder.py
    ├── progress_tracker.py
    └── ai_generator.py

💻 Installation and Setup

1. Clone the Repository

git clone https://github.com/saaqibmohiddin/AI-Learning-Path-Generator.git

2. Open the Project Folder

cd AI-Learning-Path-Generator

3. Create a Virtual Environment

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

4. Install Dependencies

pip install -r requirements.txt

The Streamlit interface also requires Streamlit:

pip install streamlit

▶️ Run the Application

Option 1: Streamlit Interface

streamlit run app.py

Option 2: Flask Interface

python web_app.py

Open the local address displayed in your terminal to access the application.

🔌 MCP Integration

The project also includes an MCP server through "learning_path_mcp.py".

It provides tools related to:

- Career learning paths
- Learning roadmap generation
- Learning resource discovery

🌟 Project Goals

- Make technical learning more structured.
- Help beginners choose a clear career-learning direction.
- Reduce the difficulty of planning learning schedules.
- Encourage practical, consistent learning.
- Help learners monitor their progress.

🔮 Future Improvements

- More career paths and technology tracks.
- AI-powered topic recommendations.
- More learning resource providers.
- Interactive visual roadmap.
- Improved user accounts and cloud-based progress storage.
- Mobile-friendly experience.
- More detailed project-based learning tasks.

👨‍💻 Developer

Saaqib Mohiddin

Computer Science and Engineering (Artificial Intelligence)

GitHub: @saaqibmohiddin (https://github.com/saaqibmohiddin)

---

⭐ If you find this project useful, consider giving the repository a star!