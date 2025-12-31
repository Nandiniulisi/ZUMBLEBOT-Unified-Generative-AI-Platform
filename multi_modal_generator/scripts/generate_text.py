import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# Load the pre-trained Microsoft Phi-3-mini-4k-instruct model and tokenizer
model_name = "microsoft/Phi-3-mini-4k-instruct"
device = "cuda" if torch.cuda.is_available() else "cpu"

# Initialize the model and tokenizer
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",  # Use 'auto' to let transformers handle the device placement
    torch_dtype="auto",
    trust_remote_code=True
)

tokenizer = AutoTokenizer.from_pretrained(model_name)

# Initialize the text generation pipeline
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device=0 if torch.cuda.is_available() else -1
)

def generate_text(prompt):
    # Set generation parameters
    generation_args = {
        "max_new_tokens": 150,       # Maximum number of tokens to generate
        "return_full_text": False,   # Return only the generated portion
        "temperature": 0.7,          # Creativity control (lower = more focused, higher = more creative)
        "do_sample": True,           # Randomness in text generation
        "top_k": 50,                 # Limit to top-k tokens for sampling
        "top_p": 0.95,               # Nucleus sampling to improve diversity
    }
    
    # Generate text using the pipeline
    output = pipe(prompt, **generation_args)
    return output[0]['generated_text']

