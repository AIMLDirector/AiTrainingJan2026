from dotenv import load_dotenv
load_dotenv()

from agents.supervisor import run_pipeline

if __name__ == "__main__":
    print(run_pipeline())