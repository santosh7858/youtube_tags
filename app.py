from flask import Flask, render_template, request
from tags import generate_tags

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    tags = ""
    if request.method == "POST":
        input_text = request.form.get("text")
        if input_text:
            tags = generate_tags(input_text, max_phrases=15)
    return render_template("index.html", tags=tags)

if __name__ == "__main__":
    app.run(debug=True)
