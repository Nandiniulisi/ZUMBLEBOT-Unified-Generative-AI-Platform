import re

def analyze_context(prompt):
    """
    Analyze the user's prompt to determine tone, intent, and output format.
    """
    # Default context
    context = {
        "tone": "neutral",
        "intent": "general",
        "output_format": "paragraph"
    }

    # Determine tone
    if any(word in prompt.lower() for word in ["please", "kindly"]):
        context["tone"] = "polite"
    elif any(word in prompt.lower() for word in ["quick", "fast", "brief"]):
        context["tone"] = "concise"

    # Determine intent
    if "explain" in prompt.lower():
        context["intent"] = "explanatory"
    elif "summarize" in prompt.lower():
        context["intent"] = "summarization"

    # Determine output format
    if "list" in prompt.lower() or "bullet points" in prompt.lower():
        context["output_format"] = "bullets"
    elif "code" in prompt.lower():
        context["output_format"] = "code"

    return context

def format_output(output, context):
    """
    Format the output based on the context.
    """
    if context["output_format"] == "bullets":
        return "\n".join(f"- {line}" for line in output.split("\n"))
    elif context["output_format"] == "code":
        return f"```\n{output}\n```"
    # Default to paragraph format
    return output
