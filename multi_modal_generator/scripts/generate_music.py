from transformers import pipeline
import scipy.io.wavfile
import os

# Initialize the synthesizer
synthesiser = pipeline("text-to-audio", "facebook/musicgen-small")

def generate_music(prompt):
    try:
        # Generate music
        music = synthesiser(prompt, forward_params={"do_sample": True})
        
        # Save the generated music to a file
        filename = 'generated_music.wav'
        file_path = os.path.join('static', filename)
        scipy.io.wavfile.write(file_path, rate=music["sampling_rate"], data=music["audio"])

        return filename

    except Exception as e:
        return f"Error generating music: {e}"
