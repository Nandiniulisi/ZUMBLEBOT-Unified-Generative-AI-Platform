from diffusers import CogVideoXPipeline
import torch
from moviepy.editor import ImageSequenceClip
import os
from PIL import Image

def generate_video(prompt):
    try:
        # Initialize the pipeline
        pipe = CogVideoXPipeline.from_pretrained(
            "THUDM/CogVideoX-5b",
            torch_dtype=torch.bfloat16
        )
        pipe.enable_model_cpu_offload()
        pipe.vae.enable_tiling()

        # Generate video frames
        video_frames = pipe(
            prompt=prompt,
            num_videos_per_prompt=1,
            num_inference_steps=50,
            num_frames=49,
            guidance_scale=6,
            generator=torch.Generator(device="cuda").manual_seed(42),
        ).frames[0]

        # Define the path to save the video
        video_path = 'static/generated_video.mp4'

        # Export frames to video
        export_to_video(video_frames, video_path, fps=8)

        return 'generated_video.mp4'

    except Exception as e:
        raise RuntimeError(f"Error generating video: {e}")

def export_to_video(frames, filename, fps=24):
    try:
        # Convert frames to a list of PIL Images
        pil_frames = [Image.fromarray(frame.numpy()) for frame in frames]

        # Create a video clip from frames
        clip = ImageSequenceClip([frame for frame in pil_frames], fps=fps)
        clip.write_videofile(filename, codec='libx264')
    except Exception as e:
        raise RuntimeError(f"Error exporting video: {e}")
