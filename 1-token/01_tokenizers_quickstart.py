"""
HuggingFace Tokenizers - Quick Start Examples
=============================================

This script demonstrates the basics of the tokenizers library.
Run each example to understand core concepts.

Installation:
    pip install tokenizers

Time: 15 minutes
"""

# =============================================================================
# Example 1: Load a Pretrained Tokenizer (Easiest Start)
# =============================================================================

def example_1_pretrained_tokenizer():
    """Load and use a pretrained tokenizer from Hugging Face Hub"""
    print("\n" + "=" * 70)
    print("EXAMPLE 1: Load Pretrained Tokenizer")
    print("=" * 70)
    
    from tokenizers import Tokenizer
    
    # Load BERT tokenizer from Hugging Face Hub
    print("\n📥 Loading bert-base-uncased tokenizer...")
    tokenizer = Tokenizer.from_pretrained("bert-base-uncased")
    
    # Encode a simple sentence
    text = "Hello, world! How are you?"
    output = tokenizer.encode(text)
    
    print(f"\n📝 Input text: {text}")
    print(f"🔢 Tokens: {output.tokens}")
    print(f"🆔 Token IDs: {output.ids}")
    print(f"📊 Number of tokens: {len(output.tokens)}")
    
    # Decode back to text
    decoded = tokenizer.decode(output.ids)
    print(f"🔄 Decoded text: {decoded}")


# =============================================================================
# Example 2: Build a Simple Tokenizer from Scratch
# =============================================================================

def example_2_build_from_scratch():
    """Build and train a simple BPE tokenizer"""
    print("\n" + "=" * 70)
    print("EXAMPLE 2: Build Tokenizer from Scratch")
    print("=" * 70)
    
    from tokenizers import Tokenizer
    from tokenizers.models import BPE
    from tokenizers.trainers import BpeTrainer
    from tokenizers.pre_tokenizers import Whitespace
    
    # Step 1: Initialize with BPE model
    print("\n📦 Creating BPE tokenizer...")
    tokenizer = Tokenizer(BPE(unk_token="[UNK]"))
    
    # Step 2: Configure pre-tokenizer
    tokenizer.pre_tokenizer = Whitespace()
    
    # Step 3: Create trainer
    trainer = BpeTrainer(
        special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"],
        vocab_size=1000,
        min_frequency=2
    )
    
    # Step 4: Train on sample data
    print("📚 Training on sample sentences...")
    training_data = [
        "The quick brown fox jumps over the lazy dog.",
        "Machine learning is awesome!",
        "Tokenizers make NLP easier and faster.",
        "Natural language processing helps computers understand text.",
        "The tokenizer library is very fast and easy to use.",
    ] * 100  # Repeat for better training
    
    tokenizer.train_from_iterator(training_data, trainer=trainer)
    
    # Step 5: Test the tokenizer
    test_text = "The tokenizer is learning!"
    output = tokenizer.encode(test_text)
    
    print(f"\n📝 Test text: {test_text}")
    print(f"🔢 Tokens: {output.tokens}")
    print(f"🆔 Token IDs: {output.ids}")
    print(f"📊 Vocabulary size: {tokenizer.get_vocab_size()}")


# =============================================================================
# Example 3: Understanding the Encoding Object
# =============================================================================

def example_3_encoding_object():
    """Explore all properties of the Encoding object"""
    print("\n" + "=" * 70)
    print("EXAMPLE 3: Understanding the Encoding Object")
    print("=" * 70)
    
    from tokenizers import Tokenizer
    
    # Load a tokenizer
    tokenizer = Tokenizer.from_pretrained("bert-base-uncased")
    
    # Encode with special tokens
    text = "Hello, world!"
    output = tokenizer.encode(text)
    
    print(f"\n📝 Input: '{text}'")
    print(f"\n🔢 Tokens: {output.tokens}")
    print(f"🆔 IDs: {output.ids}")
    print(f"📏 Offsets: {output.offsets}")
    print(f"👁️ Attention mask: {output.attention_mask}")
    print(f"🏷️ Type IDs: {output.type_ids}")
    print(f"🔖 Word IDs: {output.word_ids}")
    
    # Demonstrate alignment tracking
    print("\n" + "-" * 70)
    print("ALIGNMENT TRACKING:")
    print("-" * 70)
    
    for i, token in enumerate(output.tokens):
        start, end = output.offsets[i]
        original = text[start:end]
        print(f"Token '{token}' (ID: {output.ids[i]}) -> Original: '{original}'")


# =============================================================================
# Example 4: Batch Encoding
# =============================================================================

def example_4_batch_encoding():
    """Encode multiple sequences at once"""
    print("\n" + "=" * 70)
    print("EXAMPLE 4: Batch Encoding")
    print("=" * 70)
    
    from tokenizers import Tokenizer
    
    tokenizer = Tokenizer.from_pretrained("bert-base-uncased")
    
    # Encode multiple sequences
    sequences = [
        "The quick brown fox",
        "jumps over the lazy dog",
        "Machine learning is fun!"
    ]
    
    print("📦 Encoding batch of sequences...")
    outputs = tokenizer.encode_batch(sequences)
    
    print(f"\n📊 Encoded {len(outputs)} sequences:")
    for i, (seq, output) in enumerate(zip(sequences, outputs)):
        print(f"\n  [{i+1}] '{seq}'")
        print(f"      Tokens: {output.tokens}")
        print(f"      Length: {len(output.tokens)} tokens")


# =============================================================================
# Example 5: Padding and Truncation
# =============================================================================

def example_5_padding_truncation():
    """Demonstrate padding and truncation"""
    print("\n" + "=" * 70)
    print("EXAMPLE 5: Padding and Truncation")
    print("=" * 70)
    
    from tokenizers import Tokenizer
    
    tokenizer = Tokenizer.from_pretrained("bert-base-uncased")
    
    # Enable padding
    print("\n📏 Enabling padding...")
    tokenizer.enable_padding(pad_id=0, pad_token="[PAD]")
    
    sequences = [
        "Short",
        "A bit longer sentence",
        "This is an even longer sentence with more words"
    ]
    
    outputs = tokenizer.encode_batch(sequences)
    
    print("\n📊 Padded sequences (all same length):")
    for i, output in enumerate(outputs):
        print(f"\n  [{i+1}] Tokens: {output.tokens}")
        print(f"      Length: {len(output.tokens)}")
        print(f"      Attention mask: {output.attention_mask}")
    
    # Enable truncation
    print("\n" + "-" * 70)
    print("✂️ Enabling truncation (max_length=10)...")
    tokenizer.enable_truncation(max_length=10)
    
    long_text = "This is a very long sentence that will definitely be truncated because it exceeds the maximum length"
    output = tokenizer.encode(long_text)
    
    print(f"\n📝 Original: {long_text}")
    print(f"🔢 Truncated tokens: {output.tokens}")
    print(f"📊 Length: {len(output.tokens)} (max: 10)")


# =============================================================================
# Example 6: Encode and Decode
# =============================================================================

def example_6_encode_decode():
    """Round-trip encoding and decoding"""
    print("\n" + "=" * 70)
    print("EXAMPLE 6: Encode and Decode")
    print("=" * 70)
    
    from tokenizers import Tokenizer
    
    tokenizer = Tokenizer.from_pretrained("bert-base-uncased")
    
    original_texts = [
        "Hello, world!",
        "Machine learning is awesome.",
        "Tokenizers are fast!"
    ]
    
    print("\n🔄 Round-trip encoding/decoding:")
    for text in original_texts:
        # Encode
        output = tokenizer.encode(text)
        
        # Decode
        decoded = tokenizer.decode(output.ids)
        
        print(f"\n  Original:  {text}")
        print(f"  Tokens:    {output.tokens}")
        print(f"  Decoded:   {decoded}")
        print(f"  Match:     {'✓' if text.lower() == decoded else '✗'}")


# =============================================================================
# Example 7: Working with Sentence Pairs
# =============================================================================

def example_7_sentence_pairs():
    """Encode pairs of sentences (for tasks like NLI, QA)"""
    print("\n" + "=" * 70)
    print("EXAMPLE 7: Sentence Pairs")
    print("=" * 70)
    
    from tokenizers import Tokenizer
    
    tokenizer = Tokenizer.from_pretrained("bert-base-uncased")
    
    # Encode a pair
    sentence_a = "The cat sat on the mat"
    sentence_b = "A feline rested on the rug"
    
    output = tokenizer.encode(sentence_a, sentence_b)
    
    print(f"\n📝 Sentence A: {sentence_a}")
    print(f"📝 Sentence B: {sentence_b}")
    print(f"\n🔢 Combined tokens: {output.tokens}")
    print(f"🏷️ Type IDs: {output.type_ids}")
    print(f"   (0 = sentence A, 1 = sentence B)")
    
    # Show which tokens belong to which sentence
    print("\n" + "-" * 70)
    print("TOKEN BREAKDOWN:")
    print("-" * 70)
    for i, (token, type_id) in enumerate(zip(output.tokens, output.type_ids)):
        sentence = "Special/A" if type_id == 0 else "B"
        print(f"  {token:20s} -> Sentence {sentence}")


# =============================================================================
# Example 8: Vocabulary Inspection
# =============================================================================

def example_8_vocabulary():
    """Inspect tokenizer vocabulary"""
    print("\n" + "=" * 70)
    print("EXAMPLE 8: Vocabulary Inspection")
    print("=" * 70)
    
    from tokenizers import Tokenizer
    
    tokenizer = Tokenizer.from_pretrained("bert-base-uncased")
    
    # Get vocabulary
    vocab = tokenizer.get_vocab()
    vocab_size = tokenizer.get_vocab_size()
    
    print(f"\n📊 Vocabulary size: {vocab_size:,} tokens")
    
    # Show first 20 tokens
    print("\n🔤 First 20 tokens in vocabulary:")
    for token, token_id in list(vocab.items())[:20]:
        print(f"  ID {token_id:5d}: '{token}'")
    
    # Test token lookup
    print("\n" + "-" * 70)
    print("TOKEN LOOKUP:")
    print("-" * 70)
    
    test_tokens = ["hello", "world", "[CLS]", "[SEP]", "[MASK]", "##ing"]
    for token in test_tokens:
        token_id = tokenizer.token_to_id(token)
        if token_id is not None:
            print(f"  '{token}' -> ID: {token_id}")
        else:
            print(f"  '{token}' -> Not in vocabulary")


# =============================================================================
# Example 9: Special Tokens
# =============================================================================

def example_9_special_tokens():
    """Working with special tokens"""
    print("\n" + "=" * 70)
    print("EXAMPLE 9: Special Tokens")
    print("=" * 70)
    
    from tokenizers import Tokenizer
    from tokenizers.models import BPE
    from tokenizers.trainers import BpeTrainer
    
    # Create tokenizer with custom special tokens
    tokenizer = Tokenizer(BPE(unk_token="[UNK]"))
    
    trainer = BpeTrainer(
        special_tokens=[
            "[UNK]",   # Unknown token
            "[CLS]",   # Start of sequence
            "[SEP]",   # Separator
            "[PAD]",   # Padding
            "[MASK]",  # Masked token
            "[USER]",  # Custom: user message
            "[BOT]"    # Custom: bot response
        ],
        vocab_size=1000
    )
    
    # Train on simple data
    training_data = ["Hello world", "How are you"] * 100
    tokenizer.train_from_iterator(training_data, trainer=trainer)
    
    print("\n🔖 Special tokens and their IDs:")
    special_token_names = ["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]", "[USER]", "[BOT]"]
    
    for token in special_token_names:
        token_id = tokenizer.token_to_id(token)
        print(f"  {token:10s} -> ID: {token_id}")
    
    # Test encoding with special tokens
    print("\n" + "-" * 70)
    text = "Hello world"
    output = tokenizer.encode(text)
    print(f"\n📝 Text: '{text}'")
    print(f"🔢 Tokens: {output.tokens}")


# =============================================================================
# Example 10: Performance Comparison
# =============================================================================

def example_10_performance():
    """Compare single vs batch encoding performance"""
    print("\n" + "=" * 70)
    print("EXAMPLE 10: Performance Comparison")
    print("=" * 70)
    
    import time
    from tokenizers import Tokenizer
    
    tokenizer = Tokenizer.from_pretrained("bert-base-uncased")
    
    # Prepare test data
    texts = [
        "The quick brown fox jumps over the lazy dog.",
        "Machine learning is transforming the world.",
        "Natural language processing enables computers to understand text.",
        "Tokenizers are essential for NLP applications."
    ] * 250  # 1000 sequences
    
    print(f"\n⏱️ Encoding {len(texts)} sequences...")
    
    # Method 1: One by one
    start = time.time()
    for text in texts:
        _ = tokenizer.encode(text)
    time_single = time.time() - start
    
    # Method 2: Batch encoding
    start = time.time()
    _ = tokenizer.encode_batch(texts)
    time_batch = time.time() - start
    
    print(f"\n📊 Results:")
    print(f"  Single encoding: {time_single:.3f}s")
    print(f"  Batch encoding:  {time_batch:.3f}s")
    print(f"  Speedup:         {time_single/time_batch:.1f}x faster! 🚀")


# =============================================================================
# Main Function - Run All Examples
# =============================================================================

def main():
    """Run all examples"""
    print("\n" + "=" * 70)
    print("HUGGINGFACE TOKENIZERS - QUICK START EXAMPLES")
    print("=" * 70)
    print("\nThis script demonstrates 10 key concepts:")
    print("  1. Loading pretrained tokenizers")
    print("  2. Building from scratch")
    print("  3. Understanding encodings")
    print("  4. Batch processing")
    print("  5. Padding and truncation")
    print("  6. Encoding and decoding")
    print("  7. Sentence pairs")
    print("  8. Vocabulary inspection")
    print("  9. Special tokens")
    print(" 10. Performance optimization")
    
    try:
        example_1_pretrained_tokenizer()
        example_2_build_from_scratch()
        example_3_encoding_object()
        example_4_batch_encoding()
        example_5_padding_truncation()
        example_6_encode_decode()
        example_7_sentence_pairs()
        example_8_vocabulary()
        example_9_special_tokens()
        example_10_performance()
        
        print("\n" + "=" * 70)
        print("✅ ALL EXAMPLES COMPLETED SUCCESSFULLY!")
        print("=" * 70)
        print("\n📚 Next steps:")
        print("  - Read the full guide: huggingface_tokenizers_guide.md")
        print("  - Try training on your own data")
        print("  - Explore advanced examples")
        print("\n")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("💡 Make sure you have installed: pip install tokenizers")


if __name__ == "__main__":
    main()
