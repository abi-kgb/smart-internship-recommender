# app.py
from flask import Flask, render_template_string, request
import os

app = Flask(__name__)

recommendations = {
    "web": {
        "internships": ["Frontend Developer Intern", "Web Design Intern", "Full Stack Developer Intern"],
        "projects": ["Personal Portfolio Website", "College Event Management System", "E-commerce Website"]
    },
    "data": {
        "internships": ["Data Analyst Intern", "Business Intelligence Intern", "ML Assistant Intern"],
        "projects": ["Student Result Prediction", "Data Dashboard using Python", "Movie Recommendation System"]
    },
    "ai": {
        "internships": ["AI Research Intern", "Machine Learning Intern", "Deep Learning Intern"],
        "projects": ["Chatbot using Python", "Image Recognition System", "Voice Assistant"]
    },
    "app": {
        "internships": ["Android App Developer Intern", "Flutter Developer Intern"],
        "projects": ["Campus Navigation App", "Task Reminder App"]
    },
    "network": {
        "internships": ["Network Security Intern", "Cybersecurity Intern"],
        "projects": ["Firewall Simulation", "Network Traffic Analyzer"]
    },
    "iot": {
        "internships": ["IoT Engineer Intern", "Embedded Systems Intern"],
        "projects": ["Smart Home Automation", "IoT-based Health Monitor"]
    }
}

TEMPLATE = """
<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<title>Smart Internship & Project Recommender</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head><body>
<div class="container py-5">
  <div class="text-center mb-4">
    <h1 class="fw-bold text-primary">Smart Internship & Project Recommender</h1>
    <p class="text-muted">Enter your skills or interests to get personalized suggestions</p>
  </div>
  <form method="POST" class="mb-4">
    <div class="input-group input-group-lg">
      <input type="text" name="skills" class="form-control" placeholder="e.g. Web, AI, IoT, Data" required>
      <button class="btn btn-primary" type="submit">Recommend</button>
    </div>
  </form>

  {% if recs %}
  <div class="card shadow p-4">
    <h3 class="text-success">Recommended Internships</h3>
    <ul>
      {% for i in recs['internships'] %}
        <li>{{ i }}</li>
      {% endfor %}
    </ul>
    <h3 class="text-info mt-4">Suggested Mini Projects</h3>
    <ul>
      {% for p in recs['projects'] %}
        <li>{{ p }}</li>
      {% endfor %}
    </ul>
  </div>
  {% elif not first %}
  <div class="alert alert-warning">No matching recommendations found. Try "web", "data", "ai", "iot", etc.</div>
  {% endif %}
</div>
</body></html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    recs = None
    first = True
    if request.method == "POST":
        skills = request.form.get("skills", "").lower()
        first = False
        for key, val in recommendations.items():
            if key in skills:
                recs = val
                break
    return render_template_string(TEMPLATE, recs=recs, first=first)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
