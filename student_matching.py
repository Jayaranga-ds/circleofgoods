
import pandas as pd
import os


def match_students():

    os.makedirs("outputs", exist_ok=True)

    # Load datasets
    students = pd.read_excel("data/students_dataset_5000.xlsx")
    alumni = pd.read_excel("outputs/alumni_helping_score.xlsx")

    recommendations = []

    for _, student in students.iterrows():

        student_skills = set(str(student["Skills"]).lower().split(","))
        interest = str(student["Interested"]).lower()

        scores = []

        for _, alum in alumni.iterrows():

            alumni_skills = set(str(alum["Skills"]).lower().split(","))

            # Skill overlap
            skill_overlap = len(student_skills & alumni_skills)

            # Interest match
            interest_match = 1 if interest in alumni_skills else 0

            # Match score
            score = (
                2 * skill_overlap
                + interest_match
                + alum["HelpingScore"]
            )

            scores.append((alum["Company"], alum["JobTitle"], score))

        # Sort and take top 5 mentors
        top5 = sorted(scores, key=lambda x: x[2], reverse=True)[:5]

        for mentor in top5:
            recommendations.append({
                "Student": student["Name"],
                "MentorCompany": mentor[0],
                "MentorRole": mentor[1],
                "MatchScore": mentor[2]
            })

    df = pd.DataFrame(recommendations)

    df.to_excel("outputs/student_mentor_recommendations.xlsx", index=False)

    print("Student mentor recommendations generated!")
