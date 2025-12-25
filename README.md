# 🚀 ZUMBLEBOT – Unified Generative AI Platform

ZumbleBot is a multimodal Generative AI web application that enables users to generate **text, images, music, and videos from a single text prompt**.  
The platform integrates multiple pre-trained AI models into one unified system, eliminating the need to use separate tools for different content types.


## 📌 Problem Statement
Most generative AI tools work independently for text, image, music, and video generation. This forces users to switch between multiple platforms.  
ZumbleBot solves this problem by providing a **single interface** for multi-format AI content generation.


## 🎯 Key Features
- Single text prompt for multiple content types  
- Automatic content-type detection  
- Text, Image, Music, and Video generation  
- REST API–based backend  
- User-friendly web interface  
- GPU-accelerated video generation using Google Colab  


## 🛠️ Tech Stack

### Frontend
- HTML  
- CSS  
- JavaScript  
- Bootstrap  

### Backend
- Python  
- Flask (REST APIs)

### AI Models (Pre-trained)
- Text Generation: Qwen 2.5 Instruct  
- Image Generation: Stable Diffusion v1.5  
- Music Generation: MusicGen-Small  
- Video Generation: AnimateDiff (Google Colab GPU)


## ⚙️ System Workflow
1. User enters a text prompt  
2. Backend analyzes user intent  
3. Request is routed to the appropriate AI model  
4. Generated output is returned to the frontend  
5. User can view, play, or download the content  


## 👩‍💻 My Contribution
- Integrated AI models using Flask APIs  
- Implemented request routing logic  
- Worked on frontend–backend integration  
- Contributed to text-to-music generation module  
- Participated in testing and UI integration  


## 🚀 How to Run the Project

```bash
git clone https://github.com/your-username/zumblebot.git
cd zumblebot
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate    # Linux / Mac
pip install -r requirements.txt
python app.py
