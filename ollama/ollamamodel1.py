from ollama import chat

SYSTEM_PROMPT = (
    "You are an AI assistant for Data Engineers and SMEs. "
    "Please provide answers with examples and sample code."
)

print("AI Assistant started. Type 'bye' or 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()

    # Exit condition
    if user_input.lower() in {"bye", "exit"}:
        print("👋 Goodbye!")
        break

    # Skip empty input
    if not user_input:
        print("Please enter a valid question.\n")
        continue

    try:
        response = chat(
            model="qwen3-vl:8b",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ],
            format="json",
            options={"temperature": 0.7}
        )

        print("\nAI:", response["message"]["content"], "\n")

    except Exception as e:
        print("Error communicating with AI:", e)
