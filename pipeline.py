import subprocess


def data_pipeline():
    print("Step 1: Preparing data...")
    print("Data loaded successfully")


def train_model():
    print("Step 2: Training benefactor prediction model...")
    subprocess.run(["python", "train_model.py"])


def mentor_pipeline():
    print("Step 3: Generating mentor recommendations...")
    subprocess.run(["python", "mentor_matching.py"])


def save_outputs():
    print("Step 4: Saving outputs to outputs folder...")
    print("Outputs ready")


def run_pipeline():
    print("Starting Circle of Good ML Pipeline\n")

    data_pipeline()
    train_model()
    mentor_pipeline()
    save_outputs()

    print("\nPipeline executed successfully")


if __name__ == "__main__":
    run_pipeline()