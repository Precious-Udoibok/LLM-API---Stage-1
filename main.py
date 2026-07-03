import argparse
import requests
import json
import os

from dotenv import load_dotenv

load_dotenv()

# Function to call the OpenRouter API, that accept a prompt and returns the response
def call_openrouter_api(prompt):
    """
    Sends a user prompt to the OpenRouter Chat Completion API
    and returns the generated response.
    """
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
            "Content-Type": "application/json",
        },
        data=json.dumps(
            {
                "model": os.getenv("MODEL_NAME"),
                "messages": [
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
            }
        ),
    )

    data = response.json()
    print("Model used:", data["model"])
    return data["choices"][0]["message"]["content"]


#For the CLI 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Call OpenRouter API with a prompt.")
    parser.add_argument(
        "prompt", type=str, help="The prompt to send to the OpenRouter API."
    )
    args = parser.parse_args()
    response = call_openrouter_api(args.prompt)
    print(response)
