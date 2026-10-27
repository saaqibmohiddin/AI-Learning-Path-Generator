
from flask import Flask, render_template, request, jsonify, send_file
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.utils import simpleSplit
from xml.sax.saxutils import escape

from src.ai_generator import create_learning_path
from src.resource_finder import get_learning_resources
from src.progress_tracker import (
    load_progress,
    save_progress,
    calculate_progress
)

app = Flask(__name__)
app.secret_key = "learning-path-demo-secret-change-later"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/generate", methods=["POST"])
def generate():
    data = request.get_json() or {}

    name = data.get("name", "").strip()
    goal = data.get("career_goal", "AI Engineer")
    skills = data.get("current_skills", "")
    level = data.get("level", "Beginner")
    days = data.get("duration", 30)

    if not name:
        return jsonify({"error": "Please enter your name."}), 400

    try:
        days = int(days)
        if days not in [30, 45, 60, 90]:
            raise ValueError()
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid duration."}), 400

    roadmap = create_learning_path(
        career_goal=goal,
        current_skills=skills,
        level=level,
        days=days
    )

    profile_key = f"{name.lower()}_{goal.lower().replace(' ', '_')}"
    completed = load_progress(profile_key)

    topics = roadmap["roadmap"]

    for topic in topics:
        topic["resources"] = get_learning_resources(topic["topic"])

    return jsonify({
        "name": name,
        "profile_key": profile_key,
        "roadmap": roadmap,
        "completed_ids": completed,
        "percentage": calculate_progress(
            len(topics), len(completed)
        )
    })


@app.route("/api/progress", methods=["POST"])
def update_progress():
    data = request.get_json() or {}
    profile_key = data.get("profile_key", "")
    completed_ids = data.get("completed_ids", [])

    if not profile_key or not isinstance(completed_ids, list):
        return jsonify({"error": "Invalid progress data."}), 400

    save_progress(profile_key, completed_ids)

    return jsonify({"success": True})


@app.route("/api/download/markdown", methods=["POST"])
def download_markdown():
    data = request.get_json() or {}
    roadmap = data.get("roadmap", {})
    name = data.get("name", "Student")
    completed = set(data.get("completed_ids", []))

    lines = [
        "# AI Learning Path Generator",
        f"Student: {name}",
        f"Career Goal: {roadmap.get('career_goal', '')}",
        f"Level: {roadmap.get('level', '')}",
        f"Duration: {roadmap.get('duration_days', '')} days",
        ""
    ]

    for topic in roadmap.get("roadmap", []):
        status = "Completed" if topic["id"] in completed else "Not completed"
        lines.append(f"## {topic['topic']}")
        lines.append(f"Status: {status}")
        lines.append(topic["description"])

        for task in topic["tasks"]:
            lines.append(f"- {task}")

        lines.append("Resources:")
        for resource in topic.get("resources", []):
            lines.append(f"- [{resource['name']}]({resource['url']})")
        lines.append("")

    content = "\n".join(lines).encode("utf-8")

    return send_file(
        BytesIO(content),
        as_attachment=True,
        download_name="my_learning_roadmap.md",
        mimetype="text/markdown"
    )


@app.route("/api/download/pdf", methods=["POST"])
def download_pdf():
    data = request.get_json() or {}
    roadmap = data.get("roadmap", {})
    name = data.get("name", "Student")
    completed = set(data.get("completed_ids", []))

    buffer = BytesIO()
    document = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    content = [
        Paragraph("AI Learning Path Generator", styles["Title"]),
        Spacer(1, 12),
        Paragraph(f"Student: {escape(name)}", styles["Normal"]),
        Paragraph(
            f"Career Goal: {escape(str(roadmap.get('career_goal', '')))}",
            styles["Normal"]
        ),
        Paragraph(
            f"Level: {escape(str(roadmap.get('level', '')))}",
            styles["Normal"]
        ),
        Paragraph(
            f"Duration: {roadmap.get('duration_days', '')} days",
            styles["Normal"]
        ),
        Spacer(1, 16)
    ]

    for topic in roadmap.get("roadmap", []):
        status = "Completed" if topic["id"] in completed else "Not completed"
        content.append(
            Paragraph(escape(topic["topic"]), styles["Heading2"])
        )
        content.append(
            Paragraph(
                f"Days {topic['start_day']}–{topic['end_day']} | {status}",
                styles["Normal"]
            )
        )
        content.append(
            Paragraph(escape(topic["description"]), styles["Normal"])
        )

        for task in topic["tasks"]:
            content.append(
                Paragraph("&#8226; " + escape(task), styles["Normal"])
            )

        content.append(Spacer(1, 10))

    document.build(content)
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="my_learning_roadmap.pdf",
        mimetype="application/pdf"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
