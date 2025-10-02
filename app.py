from google.auth import default
from google.cloud import aiplatform


def call_gemini():
    # Uses default credentials (WIF in GitHub Actions will provide this)
    creds, project_id = default()

    # Initialize AI Platform client
    client = aiplatform.gapic.PredictionServiceClient(credentials=creds)

    endpoint = f"projects/{project_id}/locations/us-central1/publishers/google/models/gemini-1.5-pro"

    instance = {"content": "Write a haiku about autumn leaves."}
    response = client.predict(endpoint=endpoint, instances=[instance])

    print("Gemini response:", response)


if __name__ == "__main__":
    call_gemini()
