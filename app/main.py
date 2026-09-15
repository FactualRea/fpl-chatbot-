from openai import OpenAI
from app.config import OpenAI_API_KEY

client = OpenAI(api_key=OpenAI_API_KEY)

response = client.responses.create(model = "gpt-4.1-nano", input = "Exaplain FPL in simple terms?")

print(response.output_text)