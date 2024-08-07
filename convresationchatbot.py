from openai import OpenAI
import os
import dotenv

dotenv.load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
