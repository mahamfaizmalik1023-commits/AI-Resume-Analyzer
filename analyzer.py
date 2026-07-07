from rapidfuzz import fuzz


def analyze_resume(resume_text, job_description):

    # Calculate similarity score (0-100)
    score = fuzz.token_set_ratio(resume_text, job_description)

    # List of common skills
    skills = [
        "python",
        "java",
        "c++",
        "flask",
        "django",
        "html",
        "css",
        "javascript",
        "sql",
        "mysql",
        "postgresql",
        "machine learning",
        "data analysis",
        "git",
        "github",
        "docker",
        "aws",
        "linux",
        "react",
        "node.js",
        "mongodb",
        "pandas",
        "numpy",
        "tensorflow",
        "pytorch"
    ]

    resume_lower = resume_text.lower()
    jd_lower = job_description.lower()

    matched_skills = []
    missing_skills = []

    for skill in skills:
        if skill in jd_lower:
            if skill in resume_lower:
                matched_skills.append(skill.title())
            else:
                missing_skills.append(skill.title())

    suggestions = []

    if score < 40:
        suggestions.append(
            "Your resume has a low match with the job description."
        )

    if missing_skills:
        suggestions.append(
            "Add the missing skills if you have experience with them."
        )

    suggestions.append(
        "Use measurable achievements (e.g. 'Improved performance by 25%')."
    )

    suggestions.append(
        "Customize your resume for each job application."
    )

    return {
        "score": round(score, 2),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "suggestions": suggestions
    }