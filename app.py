from flask import Flask, render_template, request
from transformers import pipeline
app = Flask(__name__)
generator = pipeline('text-generation',model='gpt2')

@app.route("/", methods=["GET", "POST"])
def home():
    original_text = ""
    ai_text = ""
    if request.method == "POST":
        original_text = request.form["entry"]
        ai_text = generator(f"Rewrite this diary entry to sound motivational: {original_text}", max_length=100)[0]['generated_text']
    return render_template("index.html", original=original_text, ai=ai_text)

if __name__ == "__main__":
    app.run(debug=True)
