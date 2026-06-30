from ai import ask_ai, generate_profile
import json

# def main():
#     print("=" * 40)
#     print("CareerPilot AI")
#     print("=" * 40)

#     job = """
# Title: Senior DevOps Engineer

# Company: ABC Technologies

# Location: Kochi

# Skills:
# AWS
# Terraform
# Kubernetes
# Docker
# Linux
# Python
# """

#     prompt = f"""
# You are a Senior Technical Recruiter specializing in DevOps hiring.

# Your task is to evaluate whether the candidate should apply for the role.

# Candidate Profile:
# - 5 years of DevOps experience
# - AWS
# - Kubernetes
# - Terraform
# - Docker
# - Linux
# - Jenkins

# Job Description:
# {job}

# Evaluation Rules:

# 1. AWS, Kubernetes and Terraform are CORE skills.
# 2. Missing one non-core skill should NOT result in rejecting the candidate.
# 3. If the candidate matches 70% or more of the required skills, recommend APPLY.
# 4. Consider transferable skills.
# 5. Assume the candidate can learn missing skills if they are not core requirements.

# Return ONLY in this format:

# Match Score: <0-100>

# Matched Skills:
# - ...

# Missing Skills:
# - ...
# Reason:
# - ...
# Recommendation:
# APPLY or SKIP
# """
#     answer = ask_ai(prompt)
#     print(answer)
# if __name__ == "__main__":
#     main()

from resume import extract_text


def main():
    
    print("Reading resume...\n")
    resume_text = extract_text("resumes/resume.pdf")
    
    print("Generating profile...\n")
    profile_json = generate_profile(resume_text)
    profile_data = json.loads(profile_json)
    
    with open("data/profile.json", "w") as file:
        json.dump(profile_data, file, indent=4)

    print("Profile saved successfully!")
    print(profile_data)

if __name__ == "__main__":
    main()