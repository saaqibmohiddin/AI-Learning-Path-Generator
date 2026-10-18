
import streamlit as st
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

from src.ai_generator import create_learning_path
from src.resource_finder import get_learning_resources
from src.progress_tracker import (
    load_progress,
    save_progress,
    calculate_progress
)

st.set_page_config(
    page_title="AI Learning Path Generator",
    page_icon="🎓",
    layout="wide"
)

def make_profile_key(name, career_goal):
    return f"{name.strip().lower()}_{career_goal.lower().replace(' ', '_')}"

def create_pdf(roadmap, completed_ids, student_name):
    buffer = BytesIO()
    document = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    content = []

    content.append(Paragraph("AI Learning Path Generator", styles["Title"]))
    content.append(Spacer(1, 12))
    content.append(Paragraph(f"Student: {student_name}", styles["Normal"]))
    content.append(Paragraph(
        f"Career Goal: {roadmap['career_goal']}", styles["Normal"]
    ))
    content.append(Paragraph(
        f"Level: {roadmap['level']}", styles["Normal"]
    ))
    content.append(Paragraph(
        f"Duration: {roadmap['duration_days']} days", styles["Normal"]
    ))
    content.append(Spacer(1, 16))

    for topic in roadmap["roadmap"]:
        status = "Completed" if topic["id"] in completed_ids else "Not completed"

        content.append(Paragraph(topic["topic"], styles["Heading2"]))
        content.append(Paragraph(
            f"Days {topic['start_day']}–{topic['end_day']} | {status}",
            styles["Normal"]
        ))
        content.append(Paragraph(topic["description"], styles["Normal"]))

        for task in topic["tasks"]:
            content.append(Paragraph(f"• {task}", styles["Normal"]))

        content.append(Spacer(1, 10))

    document.build(content)
    return buffer.getvalue()

st.title("🎓 AI Learning Path Generator")
st.write(
    "Create a personalized career learning roadmap, "
    "find learning resources and track your progress."
)

with st.sidebar:
    st.header("Your Learning Profile")

    with st.form("profile_form"):
        student_name = st.text_input("Your name", value="Student")

        career_goal = st.selectbox(
            "Select your career goal",
            [
                "AI Engineer",
                "Python Developer",
                "Data Scientist",
                "Web Developer"
            ]
        )

        current_skills = st.text_input(
            "Your current skills",
            placeholder="Python, HTML, SQL"
        )

        level = st.selectbox(
            "Your current level",
            ["Beginner", "Intermediate", "Advanced"]
        )

        duration = st.selectbox(
            "Learning plan duration",
            [30, 45, 60, 90],
            index=0,
            format_func=lambda x: f"{x} days"
        )

        generate_button = st.form_submit_button(
            "Generate My Learning Path",
            use_container_width=True
        )

    if generate_button:
        if not student_name.strip():
            st.error("Please enter your name.")
        else:
            st.session_state["student_name"] = student_name.strip()
            st.session_state["roadmap"] = create_learning_path(
                career_goal=career_goal,
                current_skills=current_skills,
                level=level,
                days=duration
            )
            st.session_state["profile_key"] = make_profile_key(
                student_name, career_goal
            )
            st.session_state["completed_ids"] = load_progress(
                st.session_state["profile_key"]
            )

if "roadmap" not in st.session_state:
    st.info(
        "Enter your details in the left panel and click "
        "**Generate My Learning Path** to begin."
    )
    st.stop()

roadmap = st.session_state["roadmap"]
student_name = st.session_state["student_name"]
profile_key = st.session_state["profile_key"]

st.subheader(f"Hello, {student_name}!")
st.write(f"**Your Career Goal:** {roadmap['career_goal']}")
st.write(f"**Your Level:** {roadmap['level']}")
st.write(f"**Your Duration:** {roadmap['duration_days']} days")
st.write(
    "**Your Current Skills:** "
    + (", ".join(roadmap["current_skills"]) or "Not specified")
)

st.divider()
st.header("📚 Your Learning Roadmap")

topics = roadmap["roadmap"]
completed_ids = set(load_progress(profile_key))

# Create checkboxes and save progress
for topic in topics:
    with st.expander(
        f"Day {topic['start_day']}–{topic['end_day']}: {topic['topic']}",
        expanded=True
    ):
        st.write(topic["description"])

        checkbox_key = f"{profile_key}_{topic['id']}"

        is_completed = st.checkbox(
            f"Mark {topic['topic']} as completed",
            value=topic["id"] in completed_ids,
            key=checkbox_key
        )

        if is_completed:
            completed_ids.add(topic["id"])
        else:
            completed_ids.discard(topic["id"])

        st.write("**Practical tasks:**")
        for task in topic["tasks"]:
            st.write(f"- {task}")

        st.write("**Recommended resources:**")
        resources = get_learning_resources(topic["topic"])

        for resource in resources:
            st.markdown(
                f"- [{resource['name']}]({resource['url']})"
            )

save_progress(profile_key, completed_ids)

st.divider()
st.header("📊 Your Learning Progress")

total = len(topics)
completed = len(completed_ids)
percentage = calculate_progress(total, completed)

st.progress(percentage / 100)
st.metric("Completion", f"{percentage}%")
st.write(f"Completed topics: {completed} / {total}")

if percentage == 100:
    st.success("Congratulations! You completed your learning roadmap.")
elif percentage > 0:
    st.info("Good progress! Continue learning and completing your topics.")
else:
    st.info("Start completing topics to track your progress.")

st.divider()
st.header("📥 Download Your Roadmap")

markdown_lines = [
    "# AI Learning Path Generator",
    f"Student: {student_name}",
    f"Career Goal: {roadmap['career_goal']}",
    f"Level: {roadmap['level']}",
    f"Duration: {roadmap['duration_days']} days",
    f"Progress: {percentage}%",
    ""
]

for topic in topics:
    status = "Completed" if topic["id"] in completed_ids else "Not completed"
    markdown_lines.append(
        f"## Days {topic['start_day']}–{topic['end_day']}: {topic['topic']}"
    )
    markdown_lines.append(f"Status: {status}")
    markdown_lines.append(topic["description"])

    for task in topic["tasks"]:
        markdown_lines.append(f"- {task}")

    markdown_lines.append("Resources:")
    for resource in get_learning_resources(topic["topic"]):
        markdown_lines.append(f"- {resource['name']}: {resource['url']}")

    markdown_lines.append("")

markdown_text = "\n".join(markdown_lines)

col1, col2 = st.columns(2)

with col1:
    st.download_button(
        "Download Markdown",
        data=markdown_text,
        file_name="my_learning_roadmap.md",
        mime="text/markdown",
        use_container_width=True
    )

with col2:
    pdf_data = create_pdf(roadmap, completed_ids, student_name)

    st.download_button(
        "Download PDF",
        data=pdf_data,
        file_name="my_learning_roadmap.pdf",
        mime="application/pdf",
        use_container_width=True
    )

st.caption(
    "Learning Path Generator | Built with Python, Streamlit and MCP"
)