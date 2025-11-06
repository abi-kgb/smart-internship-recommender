from flask import Flask, render_template_string, request

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Smart Internship & Project Recommender</title>
  <style>
    body {
      background-image: url('{{ bg }}');
      background-size: cover;
      background-position: center;
      background-attachment: fixed;
      font-family: 'Poppins', sans-serif;
      color: white;
    }
    .overlay {
      background-color: rgba(0,0,0,0.6);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      padding: 2rem;
    }
    .card {
      background-color: rgba(0,0,0,0.7);
      border-radius: 20px;
      padding: 2rem;
      width: 90%;
      max-width: 800px;
      margin-top: 2rem;
      color: #ffffff;
    }
    h2, h3, h4, h5 {
      color: #ffffff;
    }
    a { 
      color: {% if domain=='ai' %}#ffff99
             {% elif domain=='web' %}#00bfff
             {% elif domain=='cloud' %}#00ffff
             {% elif domain=='cybersecurity' %}#ff6347
             {% elif domain=='devops' %}#7CFC00
             {% elif domain=='robotics' %}#ff69b4
             {% else %}#ffcc70{% endif %};
      text-decoration: none; 
      font-weight: 600;
    }
    a:hover { text-decoration: underline; }
    .btn {
      background-color: #ffb347;
      color: black;
      border: none;
      padding: 10px 20px;
      border-radius: 10px;
      font-weight: 600;
      cursor: pointer;
      margin-top: 1rem;
    }
    #lottie {
      width: 300px;
      height: 300px;
      margin: auto;
    }
  </style>
</head>
<body>
  <div class="overlay">
    {% if not domain %}
      <div id="lottie">
        <iframe src="https://lottie.host/embed/eBolNfIgIj.json" style="width:300px;height:300px;border:none;"></iframe>
      </div>
      <h1>Smart Internship & Project Recommender</h1>
      <form method="post">
        <input type="text" name="domain" placeholder="Enter a domain (e.g. AI, Web, Cloud, etc.)" required
               style="padding:10px;width:60%;border-radius:10px;border:none;">
        <button type="submit" class="btn">Get Recommendations</button>
      </form>
    {% else %}
      <div class="card">
        <h2>{{ domain|title }} Recommendations</h2>
        <h4>Suggested Projects:</h4>
        <ul>
          {% for project in projects %}
            <li>{{ project }}</li>
          {% endfor %}
        </ul>

        <h4>Languages to Learn:</h4>
        <p>{{ languages }}</p>

        <h4>Free Certification Course:</h4>
        <p><a href="{{ course_link }}" target="_blank">{{ course_link }}</a></p>

        <a href="/" class="btn">Back</a>
      </div>
    {% endif %}
  </div>
</body>
</html>
"""

# Domain-wise data
domains = {
    "ai": {
        "bg": "https://en.sepoin.com/wp-content/uploads/2020/01/AI-ML-4.jpg",
        "projects": [
            "AI Resume Screener",
            "Face Emotion Detection",
            "AI Chatbot Assistant"
        ],
        "languages": "Python, TensorFlow, OpenCV",
        "course_link": "https://www.coursera.org/specializations/deep-learning"
    },
    "web": {
        "bg": "https://static.vecteezy.com/system/resources/previews/000/523/309/original/web-development-and-programming-coding-concept-seo-optimization-modern-web-design-on-laptop-screen-vector.jpg",
        "projects": [
            "Portfolio Website",
            "Online Food Ordering System",
            "Mini Blogging Platform"
        ],
        "languages": "HTML, CSS, JavaScript, Flask",
        "course_link": "https://www.freecodecamp.org/"
    },
    "cloud": {
        "bg": "https://cdn.pixabay.com/photo/2024/01/26/08/07/ai-generated-8533603_1280.jpg",
        "projects": [
            "Cloud File Storage App",
            "Serverless Web API",
            "Smart Backup System"
        ],
        "languages": "Python, AWS, Docker",
        "course_link": "https://aws.amazon.com/training/"
    },
    "cybersecurity": {
        "bg": "https://images.wallpapersden.com/image/download/cybersecurity-core_bmdrZ2mUmZqaraWkpJRmbmdsrWZlbWU.jpg",
        "projects": [
            "Password Strength Analyzer",
            "Phishing Detection Tool",
            "Secure Chat Application"
        ],
        "languages": "Python, Kali Linux, Wireshark",
        "course_link": "https://www.udemy.com/course/cybersecurity-for-beginners/"
    },
    "devops": {
        "bg": "https://www.tekcent.com/media/yncjty2t/devops-1600x900-1423173157.jpg",
        "projects": [
            "CI/CD Pipeline Setup",
            "Automated Docker Deployment",
            "Monitoring Dashboard"
        ],
        "languages": "Python, Jenkins, Docker, Kubernetes",
        "course_link": "https://www.coursera.org/specializations/devops"
    },
    "robotics": {
        "bg": "https://tse4.mm.bing.net/th/id/OIP.CgeybFxfhad-Jo8HU0HpfwHaD5?pid=Api&P=0&h=180",
        "projects": [
            "Line Following Robot",
            "Object Avoiding Robot",
            "Gesture Controlled Bot"
        ],
        "languages": "Python, Arduino, ROS",
        "course_link": "https://www.udemy.com/course/robotics/"
    }
}

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        domain = request.form["domain"].lower().strip()
        if domain in domains:
            data = domains[domain]
            return render_template_string(
                TEMPLATE, 
                domain=domain, 
                bg=data["bg"],
                projects=data["projects"],
                languages=data["languages"],
                course_link=data["course_link"]
            )
        else:
            return render_template_string(TEMPLATE, domain=None, bg="", error="Domain not found")
    return render_template_string(TEMPLATE, domain=None, bg="")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
