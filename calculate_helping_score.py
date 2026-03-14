import pandas as pd

def calculate_helping_scores():

# Load ranking file
    data = pd.read_excel("outputs/alumni_benefactor_ranking.xlsx")

# Normalize engagement and experience
    data["EngagementNormalized"] = data["EngagementScore"] / 10
    data["ExperienceNormalized"] = data["YearsExperience"] / data["YearsExperience"].max()

# Calculate Helping Score
    data["HelpingScore"] = (
    0.5 * data["DonationProbability"] +
    0.3 * data["EngagementNormalized"] +
    0.2 * data["ExperienceNormalized"]
    ).round(3)

# Sort by helping score
    ranked = data.sort_values(by="HelpingScore", ascending=False)

# Save result
    ranked.to_excel("outputs/alumni_helping_score.xlsx", index=False)

    print("Helping score created!")


if __name__ == "__main__":
        calculate_helping_scores()
