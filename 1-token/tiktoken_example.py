# Install tiktoken if not already installed:
# pip install tiktoken

import tiktoken

# Choose the encoding for your model gpt 4.1
encoding = tiktoken.get_encoding("cl100k_base")

# Example text
text = "hello how are you ?"

# Encode text into token IDs
token_ids = encoding.encode(text)
print("Encoded Token IDs:", token_ids)

# Decode token IDs back to text
decoded_text = encoding.decode(token_ids)
print("Decoded Text:", decoded_text)

# Bonus: Show each token with its ID
tokens = [encoding.decode([tid]) for tid in token_ids]
print("\nToken Breakdown:")
for tid, tok in zip(token_ids, tokens):
    print(f"{tid} -> '{tok}'")
    

print("\n--Total Number of Tokens--")
print(len(token_ids))