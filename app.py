from google import genai

client = genai.Client(api_key="AIzaSyBhwR6bbd5t4neTkSVB3i3DHqYFyA_Zy-w")

chat = client.chats.create(model="gemini-2.5-flash")

print("Gemini Chat (type 'exit' to stop)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chat ended.")
        break

    response = chat.send_message(user_input)
    print("Gemini:", response.text)
