# AI Resume Analyzer

An intelligent web application that evaluates a candidate's resume against a job description to estimate an Applicant Tracking System (ATS) compatibility score. The application extracts text from PDF resumes, compares it with job requirements, identifies matched and missing skills, and provides actionable suggestions to improve the resume.

## Features

* 📄 Upload resumes in PDF format
* 📝 Enter or paste a job description
* 📊 Generate an ATS-style match score
* ✅ Identify matched skills
* ❌ Highlight missing skills
* 💡 Receive resume improvement suggestions
* 🔄 Analyze multiple resumes without restarting the application
* 🌐 Responsive and user-friendly web interface

## Tech Stack

**Backend**

* Python
* Flask

**Frontend**

* HTML5
* CSS3
* Bootstrap 5

**Libraries**

* PyMuPDF (or `pypdf`) – PDF text extraction
* RapidFuzz – Text similarity and matching

**Version Control**

* Git
* GitHub

## Project Structure

```text
Resume-Analyzer/
│
├── app.py
├── analyzer.py
├── parser.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   └── style.css
│
└── uploads/
```

## How It Works

1. Upload a PDF resume.
2. Paste the job description.
3. The application extracts text from the uploaded resume.
4. RapidFuzz compares the resume content with the job description.
5. The application:

   * Calculates an ATS match score.
   * Identifies matched skills.
   * Highlights missing skills.
   * Provides personalized suggestions to improve the resume.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/mahamfaizmalik1023/Resume-Analyzer.git
```

2. Navigate to the project directory:

```bash
cd Resume-Analyzer
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python app.py
```

5. Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Future Enhancements

* User authentication
* Resume ranking for multiple applicants
* AI-powered resume recommendations
* Resume keyword optimization
* Downloadable PDF analysis reports
* Interactive analytics dashboard
* Support for DOCX resumes
* Integration with Large Language Models (LLMs) for personalized feedback

## Author

**Maham Faiz Malik**

GitHub: https://github.com/mahamfaizmalik1023
