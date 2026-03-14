
import pandas as pd
import os


def calculate_helping_scores():

    os.makedirs("outputs", exist_ok=True)

    # Load prediction ranking
    data = pd.read_excel("outputs/alumni_benefactor_ranking.xlsx")

    # Normalize engagement score
    data["EngagementNormalized"] = data["EngagementScore"] / 10

    # Normalize experience
    max_exp = data["YearsExperience"].max()
    data["ExperienceNormalized"] = data["YearsExperience"] / max_exp

    # Calculate Helping Score
    data["HelpingScore"] = (
        0.5 * data["DonationProbability"]
        + 0.3 * data["EngagementNormalized"]
        + 0.2 * data["ExperienceNormalized"]
    ).round(3)

    # Sort alumni by helping score
    ranked = data.sort_values(by="HelpingScore", ascending=False)

    # Save result
    ranked.to_excel("outputs/alumni_helping_score.xlsx", index=False)

    print("Helping score calculation completed.")
    print("Saved to outputs/alumni_helping_score.xlsx")


if __name__ == "__main__":
    calculate_helping_scores()