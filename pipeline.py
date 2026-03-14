from predict_all_alumni import predict_all_alumni
from calculate_helping_score import calculate_helping_scores
from mentor_matching import match_mentors
from student_matching import match_students

def run_pipeline():

    print("Starting Alumni AI Pipeline...")

# Step 1: Predict alumni donation probability
    print("Running alumni prediction...")
    predict_all_alumni()

# Step 2: Calculate helping scores
    print("Calculating helping scores...")
    calculate_helping_scores()

# Step 3: Mentor matching
    print("Running mentor matching...")
    match_mentors()

# Step 4: Student matching
    print("Running student matching...")
    match_students()

    print("Pipeline completed successfully!")


if __name__ == "__main__":
    run_pipeline()
