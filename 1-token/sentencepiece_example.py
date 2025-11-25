"""
SentencePiece Tokenization Examples

SentencePiece is a language-agnostic tokenizer that doesn't require
pre-tokenization. Used by LLaMA, T5, ALBERT, XLM-R, and many production LLMs.

Install: pip install sentencepiece
"""

import sentencepiece as spm
import os


def example_1_train_bpe():
    """Train SentencePiece BPE tokenizer"""
    print("\n" + "="*60)
    print("Example 1: Train SentencePiece BPE")
    print("="*60)
    
    # Create sample training data
    os.makedirs("data", exist_ok=True)
    with open("data/sample.txt", "w", encoding="utf-8") as f:
        f.write("""
        Machine learning is the study of computer algorithms.
        Deep learning uses neural networks with many layers.
        Natural language processing helps computers understand human language.
        Tokenization is the process of breaking text into tokens.
        SentencePiece is a language-agnostic tokenizer.
        """ * 100)
    
    # Train BPE model
    print("\nTraining SentencePiece BPE model...")
    spm.SentencePieceTrainer.train(
        input='data/sample.txt',
        model_prefix='models/sentencepiece_bpe',
        vocab_size=1000,
        model_type='bpe',
        character_coverage=1.0,  # Cover all characters
        pad_id=0,
        unk_id=1,
        bos_id=2,
        eos_id=3,
    )
    
    # Load and test
    sp = spm.SentencePieceProcessor()
    sp.load('models/sentencepiece_bpe.model')
    
    test_text = "Machine learning tokenization"
    pieces = sp.encode_as_pieces(test_text)
    ids = sp.encode_as_ids(test_text)
    
    print(f"\nTest: '{test_text}'")
    print(f"Pieces: {pieces}")
    print(f"IDs: {ids}")
    print(f"Decoded: {sp.decode_pieces(pieces)}")


def example_2_train_unigram():
    """Train SentencePiece Unigram tokenizer"""
    print("\n" + "="*60)
    print("Example 2: Train SentencePiece Unigram")
    print("="*60)
    
    # Train Unigram model (better for multilingual)
    print("\nTraining SentencePiece Unigram model...")
    spm.SentencePieceTrainer.train(
        input='data/sample.txt',
        model_prefix='models/sentencepiece_unigram',
        vocab_size=1000,
        model_type='unigram',  # Probabilistic model
        character_coverage=1.0,
    )
    
    # Load and test
    sp = spm.SentencePieceProcessor()
    sp.load('models/sentencepiece_unigram.model')
    
    test_text = "Natural language processing"
    
    # Get multiple segmentation options
    pieces = sp.encode_as_pieces(test_text)
    ids = sp.encode_as_ids(test_text)
    
    print(f"\nTest: '{test_text}'")
    print(f"Pieces: {pieces}")
    print(f"IDs: {ids}")
    
    # NBest segmentation (Unigram can provide alternatives)
    nbest = sp.nbest_encode_as_pieces(test_text, nbest_size=3)
    print(f"\nTop 3 segmentations:")
    for i, segmentation in enumerate(nbest, 1):
        print(f"  {i}. {segmentation}")


def example_3_multilingual():
    """Train multilingual SentencePiece"""
    print("\n" + "="*60)
    print("Example 3: Multilingual SentencePiece")
    print("="*60)
    
    # Create multilingual data
    with open("data/multilingual.txt", "w", encoding="utf-8") as f:
        f.write("""
        Hello, how are you?
        你好吗？
        こんにちは
        Bonjour, comment allez-vous?
        Hola, ¿cómo estás?
        Привет, как дела?
        مرحبا، كيف حالك؟
        """ * 50)
    
    # Train with language-agnostic settings
    print("\nTraining multilingual SentencePiece...")
    spm.SentencePieceTrainer.train(
        input='data/multilingual.txt',
        model_prefix='models/sentencepiece_multilingual',
        vocab_size=2000,
        model_type='unigram',
        character_coverage=0.9995,  # Cover 99.95% of characters
        normalization_rule_name='nmt_nfkc',  # Normalize text
    )
    
    # Load and test on different languages
    sp = spm.SentencePieceProcessor()
    sp.load('models/sentencepiece_multilingual.model')
    
    test_texts = {
        'English': 'Hello, how are you?',
        'Chinese': '你好吗？',
        'Japanese': 'こんにちは',
        'French': 'Bonjour!',
        'Spanish': '¿Cómo estás?',
        'Russian': 'Привет!',
        'Arabic': 'مرحبا',
    }
    
    print("\nMultilingual tokenization:")
    for lang, text in test_texts.items():
        pieces = sp.encode_as_pieces(text)
        print(f"  {lang:10s}: {text:20s} → {len(pieces):2d} tokens → {pieces}")


def example_4_llama_style():
    """Train LLaMA-style SentencePiece tokenizer"""
    print("\n" + "="*60)
    print("Example 4: LLaMA-Style Tokenizer")
    print("="*60)
    
    # LLaMA uses BPE with specific settings
    print("\nTraining LLaMA-style tokenizer...")
    spm.SentencePieceTrainer.train(
        input='data/multilingual.txt',
        model_prefix='models/llama_style',
        vocab_size=32000,  # LLaMA uses 32K
        model_type='bpe',
        character_coverage=0.9995,
        byte_fallback=True,  # Handle unknown characters
        split_digits=True,  # Split numbers digit-by-digit
        normalization_rule_name='identity',  # No normalization
        num_threads=16,
    )
    
    sp = spm.SentencePieceProcessor()
    sp.load('models/llama_style.model')
    
    print(f"\nVocabulary size: {sp.vocab_size()}")
    print(f"BOS ID: {sp.bos_id()}")
    print(f"EOS ID: {sp.eos_id()}")
    print(f"PAD ID: {sp.pad_id()}")
    print(f"UNK ID: {sp.unk_id()}")
    
    # Test on code (LLaMA handles code well)
    code = "def hello(): print('Hello, world!')"
    pieces = sp.encode_as_pieces(code)
    print(f"\nCode: {code}")
    print(f"Tokens: {pieces}")


def example_5_compare_with_huggingface():
    """Compare SentencePiece with HuggingFace Tokenizers"""
    print("\n" + "="*60)
    print("Example 5: SentencePiece vs HuggingFace Tokenizers")
    print("="*60)
    
    # Load SentencePiece
    sp = spm.SentencePieceProcessor()
    sp.load('models/sentencepiece_bpe.model')
    
    # Load HuggingFace tokenizer (if available)
    try:
        from transformers import GPT2Tokenizer
        hf_tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        
        test_text = "Machine learning is fascinating!"
        
        # SentencePiece
        sp_pieces = sp.encode_as_pieces(test_text)
        sp_ids = sp.encode_as_ids(test_text)
        
        # HuggingFace
        hf_tokens = hf_tokenizer.tokenize(test_text)
        hf_ids = hf_tokenizer.encode(test_text)
        
        print(f"\nTest: '{test_text}'")
        print(f"\nSentencePiece:")
        print(f"  Tokens: {sp_pieces}")
        print(f"  Count: {len(sp_ids)}")
        
        print(f"\nHuggingFace (GPT-2):")
        print(f"  Tokens: {hf_tokens}")
        print(f"  Count: {len(hf_ids)}")
        
        print("\nKey Differences:")
        print("  - SentencePiece: Language-agnostic, no pre-tokenization")
        print("  - HuggingFace: Faster (Rust), more integrations")
        
    except ImportError:
        print("Install transformers to compare: pip install transformers")


def example_6_advanced_features():
    """Advanced SentencePiece features"""
    print("\n" + "="*60)
    print("Example 6: Advanced SentencePiece Features")
    print("="*60)
    
    sp = spm.SentencePieceProcessor()
    sp.load('models/sentencepiece_unigram.model')
    
    test_text = "Natural language processing"
    
    # 1. Regular encoding
    print("\n1. Regular Encoding:")
    pieces = sp.encode_as_pieces(test_text)
    print(f"   {pieces}")
    
    # 2. With sampling (for data augmentation)
    print("\n2. Sampling (adds randomness for augmentation):")
    sp.set_encode_extra_options('alpha:0.1')  # Enable sampling
    for i in range(3):
        sampled = sp.encode_as_pieces(test_text)
        print(f"   Sample {i+1}: {sampled}")
    sp.set_encode_extra_options('')  # Disable sampling
    
    # 3. Get vocabulary
    print("\n3. Vocabulary info:")
    print(f"   Vocab size: {sp.vocab_size()}")
    print(f"   First 10 tokens:")
    for i in range(10):
        print(f"      {i}: {sp.id_to_piece(i)}")
    
    # 4. Decode with control
    ids = sp.encode_as_ids(test_text)
    print("\n4. Decoding:")
    print(f"   IDs: {ids}")
    print(f"   Decoded: {sp.decode_ids(ids)}")
    print(f"   Decoded (pieces): {sp.decode_pieces(pieces)}")
    
    # 5. Get scores
    print("\n5. Token scores (probabilities):")
    for piece in pieces[:5]:
        score = sp.get_score(sp.piece_to_id(piece))
        print(f"   {piece}: {score:.4f}")


def example_7_integration_with_transformers():
    """Use SentencePiece with Transformers library"""
    print("\n" + "="*60)
    print("Example 7: SentencePiece + Transformers")
    print("="*60)
    
    try:
        from transformers import T5Tokenizer, LlamaTokenizer
        
        # T5 uses SentencePiece Unigram
        print("\n1. T5 Tokenizer (SentencePiece Unigram):")
        t5_tokenizer = T5Tokenizer.from_pretrained('t5-small')
        text = "translate English to French: Hello, how are you?"
        tokens = t5_tokenizer.tokenize(text)
        print(f"   Text: {text}")
        print(f"   Tokens: {tokens}")
        print(f"   Note: ▁ represents spaces in SentencePiece")
        
        # LLaMA uses SentencePiece BPE
        print("\n2. LLaMA Tokenizer (SentencePiece BPE):")
        print("   LLaMA tokenizer requires authentication")
        print("   Example: tokenizer = LlamaTokenizer.from_pretrained('meta-llama/Llama-2-7b-hf')")
        print("   Both T5 and LLaMA use SentencePiece under the hood")
        
    except ImportError:
        print("Install transformers: pip install transformers")


def main():
    """Run all examples"""
    print("\n" + "="*70)
    print("SENTENCEPIECE TOKENIZATION EXAMPLES")
    print("="*70)
    
    # Create directories
    os.makedirs("models", exist_ok=True)
    os.makedirs("data", exist_ok=True)
    
    # Run examples
    example_1_train_bpe()
    example_2_train_unigram()
    example_3_multilingual()
    example_4_llama_style()
    example_5_compare_with_huggingface()
    example_6_advanced_features()
    example_7_integration_with_transformers()
    
    print("\n" + "="*70)
    print("KEY TAKEAWAYS")
    print("="*70)
    print("""
    1. SentencePiece is language-agnostic (no pre-tokenization needed)
    2. Supports both BPE and Unigram algorithms
    3. Used by production models: LLaMA, T5, ALBERT, XLM-R
    4. Treats text as raw Unicode characters
    5. Excellent for multilingual applications
    6. Integrates with HuggingFace Transformers
    7. Fast C++ implementation
    
    When to use SentencePiece:
    ✅ Multilingual applications
    ✅ Training LLMs from scratch
    ✅ Language-agnostic systems
    ✅ When you need both BPE and Unigram options
    
    Install: pip install sentencepiece
    """)


if __name__ == "__main__":
    main()
