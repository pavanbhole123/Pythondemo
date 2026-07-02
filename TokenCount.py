import tiktoken
def get_token_count(text: str, model: str = "gpt-5") -> int:
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))
token_count = 0

def get_token_cost(prompt: str, model: str = "gpt-5") -> float:
    global token_count
    token_count = get_token_count(prompt, model)
    # Assuming a hypothetical cost of $0.0001 per token for demonstration purposes
    cost_in_dollars = (token_count/1000) * 0.005 
    cost_in_indian_rupees = cost_in_dollars * 82.0  # Assuming 1 USD = 82 INR
    return cost_in_indian_rupees

print(f"Token cost: ₹{get_token_cost('நீங்கள் எப்படி இருக்கிறீர்கள்?', 'gpt-5'):.7f}")
print(f"Token count: {token_count}")