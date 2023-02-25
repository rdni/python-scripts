import openai

# Set up your API key
openai.api_key = "asdffsdf"

def send_message(user_input, messages):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    assistant_response = response.choices[0].message["content"]
    messages.append({"role": "assistant", "content": assistant_response})
    return assistant_response

def main():
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    print("Assistant: I'm here to help! Please type your questions below.")

    while True:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Assistant: Goodbye!")
            break
        else:
            assistant_response = send_message(user_input, messages)
            print(f"Assistant: {assistant_response}")

if __name__ == "__main__":
    main()