import re

def detect_content_type(prompt):
    # Example rules for detecting content type based on the prompt
    # These rules can be refined or replaced with ML models

    # Convert prompt to lowercase to make detection case-insensitive
    prompt = prompt.lower()
    
    # Simple keyword-based detection (to be replaced with more sophisticated methods)
    if re.search(r'\b(who|what|explain|describe|define|determine|text|write|content)\b', prompt):
        return 'text'
    elif re.search(r'\b(music|song|melody|rhythm)\b', prompt):
        return 'music'
    elif re.search(r'\b(image|picture|photo|drawing|illustration)\b', prompt):
        return 'image'
    elif re.search(r'\b(video|film|clip|movie|animation)\b', prompt):
        return 'video'
    else:
        return 'text'

