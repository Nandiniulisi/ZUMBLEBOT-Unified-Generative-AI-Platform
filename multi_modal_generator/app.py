from flask import Flask, request, jsonify, render_template
from scripts.generate_text import generate_text
from scripts.generate_music import generate_music
from scripts.generate_image import generate_image
from scripts.generate_video import generate_video
from scripts.detect_content_type import detect_content_type
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt')

    # Automatically detect content type
    media_type = detect_content_type(prompt)
    
    try:
        if media_type == 'text':
            result = generate_text(prompt)
            content = {'result': result, 'media_type': media_type}
        elif media_type == 'music':
            result = generate_music(prompt)
            content = {'result': result, 'media_type': media_type}
        elif media_type == 'image':
            result = generate_image(prompt)
            content = {'result': result, 'media_type': media_type}
        elif media_type == 'video':
            # Generate video and save it to a file
            filename = generate_video(prompt)
            content = {'result': f"/static/{filename}", 'media_type': media_type}
        else:
            return jsonify({'error': 'Could not determine content type'}), 400

        return jsonify(content)

    except Exception as e:
        return jsonify({'error': f'Error generating content: {e}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
