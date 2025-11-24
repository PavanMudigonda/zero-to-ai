"""
Basic Tokenization Example
===========================
Learn the fundamentals of tokenization using tiktoken.

This example demonstrates:
1. Loading a tokenization encoding
2. Converting text to tokens (encoding)
3. Converting tokens back to text (decoding)
4. Understanding the text → tokens → IDs pipeline

Prerequisites:
    pip install tiktoken

Related files:
    - intro.md: Theory and detailed explanations
    - token_exploration.py: Advanced examples
    - token_exercises.py: Interactive practice
"""

import tiktoken

def main():
    """
    Demonstrate basic tokenization with tiktoken.
    
    The cl100k_base encoding is used by:
    - GPT-4
    - GPT-3.5-turbo
    - text-embedding-ada-002
    """
    
    print("=" * 70)
    print("BASIC TOKENIZATION EXAMPLE")
    print("=" * 70 + "\n")
    
    # Step 1: Load the encoding
    # This encoding is used by GPT-4 and GPT-3.5
    print("Loading cl100k_base encoding (used by GPT-4)...")
    encoding = tiktoken.get_encoding("cl100k_base")
    print("✓ Encoding loaded\n")
    
    # Step 2: Define example text
    text = "hello how are you ?"
    print(f"Original text: '{text}'")
    print(f"Character count: {len(text)}\n")
    
    # Step 3: Encode text into token IDs
    # This converts human-readable text into numbers the model understands
    token_ids = encoding.encode(text)
    print("=" * 70)
    print("ENCODING: Text → Token IDs")
    print("=" * 70)
    print(f"Token IDs: {token_ids}")
    print(f"Number of tokens: {len(token_ids)}\n")
    
    # Step 4: Decode token IDs back to text
    # This reverses the process: numbers → human-readable text
    decoded_text = encoding.decode(token_ids)
    print("=" * 70)
    print("DECODING: Token IDs → Text")
    print("=" * 70)
    print(f"Decoded text: '{decoded_text}'")
    print(f"Match original? {decoded_text == text}\n")
    
    # Step 5: Show the token breakdown
    # Each token ID corresponds to a piece of text
    print("=" * 70)
    print("TOKEN BREAKDOWN")
    print("=" * 70)
    print(f"{'Token ID':<12} {'Text Piece'}")
    print("-" * 70)
    
    for tid in token_ids:
        # Decode each individual token ID to see what text it represents
        token_text = encoding.decode([tid])
        print(f"{tid:<12} '{token_text}'")
    
    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Input: '{text}'")
    print(f"Tokens: {len(token_ids)}")
    print(f"Characters: {len(text)}")
    print(f"Ratio: {len(text)/len(token_ids):.2f} characters per token")
    
    # Additional examples
    print("\n" + "=" * 70)
    print("TRY THESE EXAMPLES")
    print("=" * 70)
    
    examples = [
        "The quick brown fox jumps over the lazy dog",
        "I love AI and machine learning!",
        "GPT-4 is amazing",
        "print('Hello, World!')",
        "supercalifragilisticexpialidocious"
    ]
    
    print("\nSee how different texts tokenize:\n")
    for example in examples:
        tokens = encoding.encode(example)
        print(f"{len(tokens):2d} tokens: '{example}'")
    
    print("\n" + "=" * 70)
    print("NEXT STEPS")
    print("=" * 70)
    print("1. Read intro.md for detailed explanations")
    print("2. Run token_exploration.py for advanced examples")
    print("3. Try token_exercises.py for interactive practice")
    print("4. Experiment by changing the 'text' variable above!")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    main()