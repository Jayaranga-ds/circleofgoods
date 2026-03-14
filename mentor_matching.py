
import pandas as pd
import os


def match_mentors():

    os.makedirs("outputs", exist_ok=True)

    students = pd.read_excel("data/students_dataset_5000.xlsx")
    alumni = pd.read_excel("outputs/alumni_helping_score.xlsx")

    print("Students loaded:", len(students))
    print("Alumni loaded:", len(alumni))

    recommendations = []

    for _, alum in alumni.iterrows():

        alumni_skills = set(str(alum["Skills"]).lower().split(","))

        scores = []

        for _, student in students.iterrows():

            student_skills = set(str(student["Skills"]).lower().split(","))

            skill_overlap = len(student_skills & alumni_skills)

            score = (
                3 * skill_overlap
                + 2 * float(alum["HelpingScore"])
                + 0.1 * float(alum["YearsExperience"])
                + 0.1 * float(alum["EngagementScore"])
            )

            scores.append({
                "MentorCompany": alum["Company"],
                "MentorRole": alum["JobTitle"],
                "Student": student["Name"],
                "MatchScore": round(score, 3)
            })

        top5 = sorted(scores, key=lambda x: x["MatchScore"], reverse=True)[:5]

        recommendations.extend(top5)

    df = pd.DataFrame(recommendations)

    output_file = "outputs/mentor_student_recommendations.xlsx"
    df.to_excel(output_file, index=False)

    print("Mentor → Student recommendations generated!")
    print("Saved to:", output_file)


if __name__ == "__main__":
    match_mentors()
