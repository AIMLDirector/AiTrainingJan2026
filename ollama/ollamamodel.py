from ollama import chat

user_input =input("Enter your question for the AI assistant: ")

response = chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "system",
            "content": (
                "You are an AI assistant for Data Engineers and SMEs. "
                "Please provide answers with examples and sample code."
            )
        },
        {
            "role": "user",
            "content": user_input
        }
    ],
    format="json",
    options={
        "temperature": 0.7
    }
)

print(response["message"]["content"])
