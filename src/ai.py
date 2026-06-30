import ollama

def ask_ai(prompt: str) -> str:
    """
    Sends a prompt to Ollama and returns the AI response.
    """
    response = ollama.chat(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]

import json
def generate_profile(resume_text: str) -> str:
    """
    Uses AI to extract a candidate profile from resume text.
    Returns the AI response as a string.
    """

    prompt = f"""
You are an expert technical resume parser.

Your task is to extract structured information from the resume.

Return ONLY a valid JSON object.

Do NOT:
- Add explanations.
- Add markdown.
- Wrap the response in ```json.
- Return any text before or after the JSON.

Use EXACTLY this JSON schema:

{{
    "name": "",
    "current_role": "",
    "experience_years": 0,
    "skills": []
}}

Rules:

1. "experience_years" must be a whole number.
2. "skills" must be a flat array of individual technical skills.
3. Normalize skill names using common industry terminology.
   Examples:
   - Amazon Web Services → AWS
   - K8s → Kubernetes
   - IaC (Terraform) → Terraform
4. Remove duplicate skills.
5. Do NOT include:
   - Certifications
   - Responsibilities
   - Soft skills
   - Job titles inside the skills list
6. Include only technologies, programming languages, cloud platforms, DevOps tools, CI/CD tools, container platforms, operating systems and infrastructure tools.

Resume:

{resume_text}
"""

    return ask_ai(prompt)