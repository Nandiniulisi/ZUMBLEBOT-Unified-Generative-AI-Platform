import openai

# Set your OpenAI API key (make sure to store it securely)
openai.api_key = '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'

def generate_image(prompt):
    try:
        # Call OpenAI's image generation API
        response = openai.Image.create(
            prompt=prompt,   # The text prompt to generate the image from
            n=1,             # Number of images to generate
            size="1024x1024" # Image resolution
        )
        # Extract the URL of the generated image
        image_url = response['data'][0]['url']
        return image_url

    except Exception as e:
        return f"Error generating image: {e}"

