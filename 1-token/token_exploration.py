"""
Token Exploration - Advanced Examples
======================================
Explore how different types of text get tokenized.

Learning objectives:
- See how common vs uncommon words tokenize
- Understand context-dependent tokenization
- Compare different languages
- Analyze code tokenization
- Explore special characters and numbers

Run this after understanding the basics in tiktoken_example.py
"""

import tiktoken

def print_section(title):
    """Helper to print section headers"""
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

def analyze_text(text, encoding, label=""):
    """Analyze and display tokenization details for given text"""
    tokens = encoding.encode(text)
    decoded_tokens = [encoding.decode([t]) for t in tokens]
    
    print(f"\n{label}")
    print(f"Text: '{text}'")
    print(f"Token count: {len(tokens)}")
    print(f"Character count: {len(text)}")
    print(f"Ratio: {len(text)/len(tokens):.2f} chars/token")
    print(f"\nToken breakdown:")
    for tid, tok in zip(tokens, decoded_tokens):
        print(f"  {tid:6d} → '{tok}'")

def main():
    # Initialize encoding (GPT-4)
    encoding = tiktoken.get_encoding("cl100k_base")
    
    # =================================================================
    # PART 1: Common vs Uncommon Words
    # =================================================================
    print_section("PART 1: COMMON VS UNCOMMON WORDS")
    
    common_words = [
        "hello",
        "world",
        "computer",
        "artificial intelligence"
    ]
    
    print("\n📌 Common words (usually 1 token each):")
    for word in common_words:
        analyze_text(word, encoding, f"Word: {word}")
    
    uncommon_words = [
        "supercalifragilisticexpialidocious",
        "pneumonoultramicroscopicsilicovolcanoconiosis",
        "antidisestablishmentarianism"
    ]
    
    print("\n📌 Uncommon words (split into multiple subword tokens):")
    for word in uncommon_words:
        tokens = encoding.encode(word)
        print(f"\n'{word}': {len(tokens)} tokens")
        decoded = [encoding.decode([t]) for t in tokens]
        print(f"  Split as: {decoded}")
    
    # =================================================================
    # PART 2: Context-Dependent Tokenization
    # =================================================================
    print_section("PART 2: CONTEXT-DEPENDENT TOKENIZATION")
    
    print("\n📌 Same word, different tokens based on context:")
    
    contexts = [
        "red",           # No space, lowercase
        " red",          # Leading space
        "Red",           # Capitalized, no space
        " Red",          # Leading space + capitalized
        "RED",           # All caps
        " RED"           # Leading space + all caps
    ]
    
    for ctx in contexts:
        tokens = encoding.encode(ctx)
        print(f"'{ctx}' → Token ID: {tokens[0]}")
    
    print("\n📌 Why? Tokenizers learn from real text patterns:")
    print("  - Words mid-sentence usually have leading space")
    print("  - Sentence starts are capitalized without space")
    print("  - This context-awareness improves efficiency")
    
    # =================================================================
    # PART 3: Code Tokenization
    # =================================================================
    print_section("PART 3: CODE TOKENIZATION")
    
    code_samples = [
        'def hello_world():',
        'print("Hello, World!")',
        'x = [1, 2, 3, 4, 5]',
        'if x > 10:',
        '    return True',
        '// This is a comment',
        'const greeting = "hello";'
    ]
    
    print("\n📌 How code gets tokenized:")
    for code in code_samples:
        analyze_text(code, encoding, f"Code: {code}")
    
    # =================================================================
    # PART 4: Numbers and Special Characters
    # =================================================================
    print_section("PART 4: NUMBERS AND SPECIAL CHARACTERS")
    
    print("\n📌 Numbers:")
    numbers = ["123", "1234", "12345", "123456", "1,234,567", "3.14159"]
    for num in numbers:
        tokens = encoding.encode(num)
        print(f"'{num}' → {len(tokens)} tokens: {tokens}")
    
    print("\n📌 Special characters:")
    special = ["!!!", "???", "...", "---", "***", "@@", "###"]
    for spec in special:
        tokens = encoding.encode(spec)
        print(f"'{spec}' → {len(tokens)} tokens: {tokens}")
    
    print("\n📌 Emojis:")
    emojis = ["😀", "👍", "❤️", "🚀", "🎉"]
    for emoji in emojis:
        tokens = encoding.encode(emoji)
        print(f"'{emoji}' → {len(tokens)} tokens: {tokens}")
    
    # =================================================================
    # PART 5: Different Languages
    # =================================================================
    print_section("PART 5: MULTILINGUAL TOKENIZATION")
    
    translations = {
        "English": "How are you?",
        "Spanish": "¿Cómo estás?",
        "French": "Comment allez-vous?",
        "German": "Wie geht es dir?",
        "Chinese": "你好吗?",
        "Japanese": "元気ですか?",
        "Arabic": "كيف حالك؟",
        "Russian": "Как дела?",
        "Korean": "어떻게 지내세요?"
    }
    
    print("\n📌 Same question in different languages:")
    print(f"{'Language':<12} {'Text':<25} {'Tokens':<8} {'Chars':<8} {'Ratio'}")
    print("-" * 70)
    
    for lang, text in translations.items():
        tokens = encoding.encode(text)
        ratio = len(text) / len(tokens)
        print(f"{lang:<12} {text:<25} {len(tokens):<8} {len(text):<8} {ratio:.2f}")
    
    print("\n💡 Notice: Non-English languages often need more tokens!")
    print("   This means:")
    print("   - Higher API costs for same semantic content")
    print("   - Less text fits in the same context window")
    print("   - Processing may be slower")
    
    # =================================================================
    # PART 6: Token Efficiency Comparison
    # =================================================================
    print_section("PART 6: TOKEN EFFICIENCY ANALYSIS")
    
    print("\n📌 Comparing different ways to express the same idea:")
    
    variations = [
        "Please help me with this problem.",
        "Please assist me with this issue.",
        "Could you please help me solve this?",
        "I need help with this.",
        "Help me with this."
    ]
    
    print("\nSame request, different token counts:")
    for var in variations:
        tokens = encoding.encode(var)
        print(f"{len(tokens):2d} tokens: '{var}'")
    
    print("\n💡 Tip: Concise language = fewer tokens = lower costs!")
    
    # =================================================================
    # PART 7: Whitespace Handling
    # =================================================================
    print_section("PART 7: WHITESPACE AND FORMATTING")
    
    print("\n📌 How whitespace affects tokenization:")
    
    whitespace_examples = [
        "hello world",           # Single space
        "hello  world",          # Double space
        "hello   world",         # Triple space
        "hello\nworld",          # Newline
        "hello\tworld",          # Tab
        "hello world ",          # Trailing space
        " hello world",          # Leading space
    ]
    
    for example in whitespace_examples:
        tokens = encoding.encode(example)
        visual = example.replace(' ', '·').replace('\n', '↵').replace('\t', '→')
        print(f"'{visual}' → {len(tokens)} tokens")
    
    # =================================================================
    # PART 8: Real-World Examples
    # =================================================================
    print_section("PART 8: REAL-WORLD EXAMPLES")
    
    print("\n📌 Typical text samples:")
    
    samples = {
        "Tweet": "Just learned about tokenization! 🚀 It's how LLMs process text. #AI #MachineLearning",
        "Email": "Dear John,\n\nI hope this email finds you well. I wanted to follow up on our meeting yesterday.",
        "Code comment": "# Calculate the sum of all even numbers in the list",
        "Function name": "calculate_total_revenue_for_quarter",
        "URL": "https://platform.openai.com/docs/api-reference",
        "JSON": '{"name": "John", "age": 30, "city": "New York"}',
        "SQL": "SELECT * FROM users WHERE age > 18 ORDER BY created_at DESC;"
    }
    
    print(f"\n{'Type':<15} {'Tokens':<8} {'Characters':<12} {'Efficiency'}")
    print("-" * 55)
    
    for text_type, text in samples.items():
        tokens = encoding.encode(text)
        efficiency = len(text) / len(tokens)
        print(f"{text_type:<15} {len(tokens):<8} {len(text):<12} {efficiency:.2f} c/t")
    
    print("\n💡 Different content types have different token efficiency!")
    
    # =================================================================
    # SUMMARY
    # =================================================================
    print_section("KEY TAKEAWAYS")
    
    print("""
    1. Common words → 1 token, uncommon words → multiple tokens
    
    2. Context matters: " red" ≠ "red" ≠ "Red" ≠ " Red"
    
    3. Code is tokenized efficiently (keywords, operators, identifiers)
    
    4. Numbers: Usually 1-3 digits per token
    
    5. Non-English languages need MORE tokens for same content
       → Higher costs, less context window space
    
    6. Whitespace (spaces, newlines, tabs) affects tokenization
    
    7. Token efficiency varies by content type:
       - Code: ~3-4 chars/token
       - English text: ~4 chars/token
       - Non-English: ~2-3 chars/token
    
    8. To minimize tokens:
       ✓ Use concise language
       ✓ Avoid repetition
       ✓ Remove unnecessary whitespace
       ✓ Stick to common words when possible
    """)
    
    print("\n" + "=" * 70)
    print("Experiment with your own text! Modify the examples above.")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    main()
