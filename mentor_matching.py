import pandas as pd

def match_mentors():


# Load alumni helping score data
    alumni = pd.read_excel("outputs/alumni_helping_score.xlsx")

# Load student data
    students = pd.read_excel("data/students_dataset_5000.xlsx")

# Example mentor matching logic
    matches = []

    for _, student in students.iterrows():
     mentor = alumni.iloc[0]   # Example: choose top alumni

     matches.append({
        "StudentName": student["Name"],
        "MentorName": mentor["Name"],
        "MentorHelpingScore": mentor["HelpingScore"]
     })

    matches_df = pd.DataFrame(matches)

# Save mentor matches
    matches_df.to_excel("outputs/mentor_recommendations.xlsx", index=False)

    print("Mentor matching completed!")


if __name__== "__main__":
        match_mentors()
