from openai import OpenAI
import os
import dotenv

dotenv.load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Create an instruction for the bot
conversation = [{"role": "system", "content": "You are an assistant."}]

def ask_question(inputquestion):
    # Append the user's question to the conversation array
    conversation.append({"role": "user","content": inputquestion})

    # Request gpt-3.5-turbo for chat completion or a response
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    # Access the response from the API to display it
    assistant_response = response.choices[0].message.content
    
    return response

ask_question("Where is the moon?")