from flask import Flask, render_template, request
from tags import generate_tags
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    tags = ""
    if request.method == "POST":
        title = request.form.get("title", "")
        if title:
            tags = generate_tags(title)
    return render_template("index.html", tags=tags)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
