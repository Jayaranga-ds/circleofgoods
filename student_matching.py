import pandas as pd

def match_students():


    students = pd.read_excel("data/students_dataset_5000.xlsx")
    alumni = pd.read_excel("data/alumni_dataset_1000.xlsx")

    def skill_match(student_skills, alumni_skills):

        if pd.isna(student_skills) or pd.isna(alumni_skills):
            return 0

        s = set(skill.strip().lower() for skill in student_skills.split(","))
        a = set(skill.strip().lower() for skill in alumni_skills.split(","))

        if len(a) == 0:
            return 0

        return len(s & a) / len(a)

    results = []

    for _, alum in alumni.iterrows():

        matches = []

        for _, student in students.iterrows():

            score = skill_match(student["Skills"], alum["Skills"])

            if score > 0:
                matches.append({
                "Alumni": alum["Name"],
                "Student": student["Name"],
                "MatchScore": round(score, 2)
            })

        top_students = sorted(matches, key=lambda x: x["MatchScore"], reverse=True)[:5]

        results.extend(top_students)

    df = pd.DataFrame(results)

    df = df.sort_values(["Alumni", "MatchScore"], ascending=[True, False])

    df.to_excel("outputs/student_recommendations_for_alumni.xlsx", index=False)

    print("Student recommendations for alumni created!")


if __name__ == "__main__":
        match_students()
