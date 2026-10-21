#Use this code to confirm if Gemini is working or not

from google import genai
client = genai.Client(api_key="GEMINI_API_KEY")

response = client.models.generate_content(
    model="models/gemini-2.5-flash",   # use one from your list
    contents="Hello Gemini, confirm you're working!"
)

print(response.text)

