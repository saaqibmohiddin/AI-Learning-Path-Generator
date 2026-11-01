<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:080B1A,45:172554,100:6D28D9&height=230&section=header&text=AI%20LEARNING%20PATH%20GENERATOR&fontSize=34&fontColor=FFFFFF&fontAlignY=38&desc=Your%20Skills.%20Your%20Goals.%20Your%20Personalized%20Roadmap.&descSize=14&descAlignY=58&animation=fadeIn" width="100%" />AI Learning Path Generator

Build Skills. Follow a Roadmap. Achieve Your Career Goals.

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/MCP-7C3AED?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Active-14B8A6?style=for-the-badge"/>
</p></div>---

◈ PROJECT OVERVIEW

AI Learning Path Generator is a Python-based learning roadmap application designed to help users plan their career development through structured, day-wise learning paths.

Users can select a career goal, enter their current skills, choose their experience level, and select a learning duration. The application organizes predefined career-related topics into a structured roadmap with practical tasks and learning resources.

The platform also supports progress tracking and roadmap exports, helping users organize their learning in one place.

---

✦ CORE FEATURES

<table>
<tr>
<td width="50%">🎯 Career-Based Roadmaps

Choose from different career paths:

- AI Engineer
- Python Developer
- Data Scientist
- Web Developer

</td>
<td width="50%">🧠 Personalized Inputs

Provide your:

- Name
- Current skills
- Experience level
- Learning duration

</td>
</tr>
<tr>
<td width="50%">📅 Day-Wise Planning

- 30-day roadmap
- 45-day roadmap
- 60-day roadmap
- 90-day roadmap

</td>
<td width="50%">📚 Learning Resources

Find topic-related learning links and useful study resources.

</td>
</tr>
<tr>
<td width="50%">📊 Progress Tracking

- Mark topics as completed
- Monitor completed tasks
- Calculate completion percentage

</td>
<td width="50%">📄 Roadmap Export

Export your learning roadmap in:

- Markdown
- PDF

</td>
</tr>
</table>---

◈ APPLICATION INTERFACES

Interface| Description
Streamlit| Interactive Python-based application
Flask| Web application interface
MCP| Model Context Protocol integration

---

⚡ TECHNOLOGY STACK

<p align="center">
<img src="https://skillicons.dev/icons?i=python,flask,html,css,js,vscode,git,github" />
</p>Category| Technologies
Programming Language| Python
Web Framework| Flask
Interactive Interface| Streamlit
Frontend| HTML, CSS, JavaScript
Data Storage| JSON
AI Integration| AI-related generation modules
Tool Integration| Model Context Protocol (MCP)
Development Tools| VS Code, Git, GitHub

---

◈ PROJECT ARCHITECTURE

AI-Learning-Path-Generator/
│
├── .vscode/
│   └── mcp.json
│
├── mcp/
│   └── server.py
│
├── src/
│   ├── ai_generator.py
│   ├── __init__.py
│   ├── progress_tracker.py
│   ├── resource_finder.py
│   └── roadmap_engine.py
│
├── templates/
│   └── index.html
│
├── .env.example
├── .gitignore
├── README.md
├── __init__.py
├── ai_engineer_30_day_roadmap.md
├── app.py
├── index.html
├── learning_path_mcp.py
├── learning_progress.json
├── requirements.txt
└── web_app.py

---

⚙️ INSTALLATION & SETUP

Follow these steps to download, configure, and run the AI Learning Path Generator locally.

01. Clone the Repository

Open your terminal or VS Code terminal:

git clone https://github.com/saaqibmohiddin/AI-Learning-Path-Generator.git

02. Navigate to the Project

cd AI-Learning-Path-Generator

03. Create a Virtual Environment

python -m venv venv

04. Activate the Virtual Environment

Windows (PowerShell):

.\venv\Scripts\Activate.ps1

Windows (Command Prompt):

venv\Scripts\activate.bat

05. Install Required Packages

python -m pip install --upgrade pip
pip install -r requirements.txt
pip install streamlit

06. Configure Environment Variables

If the project requires environment variables:

1. Open the project folder.
2. Create a copy of ".env.example".
3. Rename the copy to ".env".
4. Add the required configuration values.

Keep your ".env" file private. Never upload API keys or secrets to GitHub.

07. Launch the Application

Choose the interface you want to run.

Option A — Streamlit Interface

streamlit run app.py

Option B — Flask Web Interface

python web_app.py

08. Open the Application

After starting the application, check the terminal for the local URL.

For Streamlit, it is usually:

http://localhost:8501

For Flask, use the local address printed by the application in your terminal.

---

💡 TROUBLESHOOTING

Issue| Suggested solution
Python not recognized| Install Python and enable PATH during installation
Module not found| Activate the virtual environment and install dependencies
Streamlit not found| Run "pip install streamlit"
Port already in use| Stop the other process or configure a different port
Environment variable error| Check your ".env" configuration

<sub>Note: Run commands from the project's root directory. Keep the virtual environment activated while running the application.</sub>

---
<div align="center">

<img src="https://img.shields.io/badge/DEVELOPER-MOHAMMED%20SAAQIB%20MOHIDDIN-6D28D9?style=for-the-badge" />MOHAMMED SAAQIB MOHIDDIN

Computer Science & Engineering (Artificial Intelligence)

Aspiring AI Engineer | Python Developer 

---

AREAS OF INTEREST

<p>
<img src="https://img.shields.io/badge/Artificial%20Intelligence-7C3AED?style=flat-square"/>
<img src="https://img.shields.io/badge/Machine%20Learning-2563EB?style=flat-square"/>
<img src="https://img.shields.io/badge/Generative%20AI-0891B2?style=flat-square"/>
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
</p>CONNECT WITH ME

<a href="https://github.com/saaqibmohiddin">
<img src="https://img.shields.io/badge/GitHub-Explore%20My%20Projects-181717?style=for-the-badge&logo=github"/>
</a><br/><sub>Building practical projects and continuously exploring emerging technologies.</sub>

</div>