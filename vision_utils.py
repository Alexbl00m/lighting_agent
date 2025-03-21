from openai import OpenAI
client = OpenAI()

def analyze_image(image_path):
    with open(image_path, "rb") as img:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": [{"type": "image_url", "image_url": f"data:image/jpeg;base64,{img.read().decode('base64')}"}]},
                {"role": "user", "content": "Analysera produkten i bilden och sammanfatta tekniska nyckelvärden"}
            ]
        )
    return response.choices[0].message.content

