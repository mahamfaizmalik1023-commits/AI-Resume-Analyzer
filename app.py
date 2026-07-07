print("THIS IS MY RESUME ANALYZER")

from flask import Flask, render_template, request
import os
import tempfile
from werkzeug.utils import secure_filename

# Import our own modules
from parser import extract_text_from_pdf
from analyzer import analyze_resume

app = Flask(__name__)

# Use Vercel's temporary directory
UPLOAD_FOLDER = tempfile.gettempdir()
ALLOWED_EXTENSIONS = {"pdf"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    # Check if a file was uploaded
    if "resume" not in request.files:
        return "No resume uploaded."

    file = request.files["resume"]

    if file.filename == "":
        return "Please select a PDF file."

    if not allowed_file(file.filename):
        return "Only PDF files are allowed."

    # Save uploaded file in Vercel's temporary directory
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(filepath)

    # Extract text from resume
    resume_text = extract_text_from_pdf(filepath)

    # Read job description
    job_description = request.form.get("job_description", "").strip()

    if not job_description:
        return "Please enter a job description."

    # Analyze resume
    result = analyze_resume(resume_text, job_description)

    # Show results
    return render_template(
        "result.html",
        result=result,
        resume_text=resume_text,
        job_description=job_description,
    )


if __name__ == "__main__":
    app.run(debug=True)
