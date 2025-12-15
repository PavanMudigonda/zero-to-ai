# Production Tokenization Guide

## Real-World Tokenization Challenges & Solutions

This guide covers production-level considerations often overlooked in tutorials:
- Performance optimization
- Memory management
- Error handling
- Multilingual edge cases
- Security considerations
- Monitoring and debugging

---

## 1. Performance Optimization

### Batch Processing

```python
from tokenizers import Tokenizer
import time

tokenizer = Tokenizer.from_pretrained("bert-base-uncased")

texts = ["Sample text " + str(i) for i in range(10000)]

# ❌ BAD: Process one at a time (SLOW)
start = time.time()
results = []
for text in texts:
    results.append(tokenizer.encode(text))
slow_time = time.time() - start

# ✅ GOOD: Batch process (FAST)
start = time.time()
results = tokenizer.encode_batch(texts)
fast_time = time.time() - start

print(f"Sequential: {slow_time:.2f}s")
print(f"Batch: {fast_time:.2f}s")
print(f"Speedup: {slow_time/fast_time:.1f}x faster")
# Typical result: 10-20x speedup
```

### Optimal Batch Sizes

```python
def find_optimal_batch_size(tokenizer, sample_texts, max_batch=1024):
    """
    Find optimal batch size for your hardware.
    Larger batches = faster, but may cause OOM.
    """
    import time
    
    batch_sizes = [16, 32, 64, 128, 256, 512, 1024]
    results = {}
    
    for batch_size in batch_sizes:
        try:
            # Test with this batch size
            batches = [sample_texts[:batch_size] for _ in range(10)]
            
            start = time.time()
            for batch in batches:
                tokenizer.encode_batch(batch)
            elapsed = time.time() - start
            
            tokens_per_sec = (batch_size * 10) / elapsed
            results[batch_size] = tokens_per_sec
            print(f"Batch {batch_size}: {tokens_per_sec:.0f} texts/sec")
            
        except MemoryError:
            print(f"Batch {batch_size}: OOM - too large")
            break
    
    # Return best batch size
    best = max(results.items(), key=lambda x: x[1])
    return best[0]

# Usage
optimal = find_optimal_batch_size(tokenizer, texts)
print(f"\n✅ Optimal batch size: {optimal}")
```

### Parallel Processing

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import multiprocessing as mp

def parallel_tokenize(texts, num_workers=None):
    """
    Parallelize tokenization across CPU cores.
    Use for very large datasets (millions of texts).
    """
    if num_workers is None:
        num_workers = mp.cpu_count()
    
    # Split into chunks
    chunk_size = len(texts) // num_workers
    chunks = [texts[i:i+chunk_size] for i in range(0, len(texts), chunk_size)]
    
    def process_chunk(chunk):
        tokenizer = Tokenizer.from_pretrained("bert-base-uncased")
        return tokenizer.encode_batch(chunk)
    
    # Process in parallel
    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        results = list(executor.map(process_chunk, chunks))
    
    # Flatten results
    return [item for sublist in results for item in sublist]

# For 1M+ texts, this can be 4-8x faster than single-core
```

---

## 2. Memory Management

### Streaming Large Files

```python
def tokenize_large_file_streaming(file_path, output_path, batch_size=1000):
    """
    Tokenize files too large to fit in memory.
    Processes in batches and streams to disk.
    """
    tokenizer = Tokenizer.from_pretrained("bert-base-uncased")
    
    with open(file_path, 'r', encoding='utf-8') as infile, \
         open(output_path, 'w', encoding='utf-8') as outfile:
        
        batch = []
        total_processed = 0
        
        for line in infile:
            batch.append(line.strip())
            
            if len(batch) >= batch_size:
                # Process batch
                encodings = tokenizer.encode_batch(batch)
                
                # Write to output (token IDs as JSON)
                import json
                for enc in encodings:
                    outfile.write(json.dumps(enc.ids) + '\n')
                
                total_processed += len(batch)
                print(f"Processed {total_processed:,} lines", end='\r')
                
                # Clear batch to free memory
                batch = []
        
        # Process remaining
        if batch:
            encodings = tokenizer.encode_batch(batch)
            import json
            for enc in encodings:
                outfile.write(json.dumps(enc.ids) + '\n')
            total_processed += len(batch)
        
        print(f"\n✅ Total processed: {total_processed:,} lines")

# Can handle files with millions of lines without OOM
```

### Memory-Efficient Vocabulary Loading

```python
def load_tokenizer_lazy(model_name):
    """
    Load tokenizer only when needed, not at import time.
    Reduces memory footprint for multi-model applications.
    """
    _tokenizer = None
    
    def get_tokenizer():
        nonlocal _tokenizer
        if _tokenizer is None:
            _tokenizer = Tokenizer.from_pretrained(model_name)
        return _tokenizer
    
    return get_tokenizer

# Usage
tokenizer_getter = load_tokenizer_lazy("bert-base-uncased")
# Tokenizer not loaded yet - zero memory

# Load only when needed
tokenizer = tokenizer_getter()
# Now loaded
```

---

## 3. Error Handling & Edge Cases

### Robust Tokenization with Fallbacks

```python
def robust_tokenize(text, tokenizer, max_length=512):
    """
    Handle edge cases gracefully:
    - Empty text
    - Very long text
    - Invalid UTF-8
    - Control characters
    """
    if not text or not text.strip():
        # Handle empty
        return {
            'ids': [],
            'tokens': [],
            'warning': 'Empty input'
        }
    
    # Clean control characters (but preserve newlines/tabs)
    import re
    text = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', '', text)
    
    try:
        # Try normal encoding
        encoding = tokenizer.encode(text, truncation=True, max_length=max_length)
        
        if len(encoding.ids) == 0:
            return {
                'ids': [],
                'tokens': [],
                'warning': 'Tokenization produced no tokens'
            }
        
        return {
            'ids': encoding.ids,
            'tokens': encoding.tokens,
            'attention_mask': encoding.attention_mask,
            'truncated': len(encoding.ids) >= max_length
        }
        
    except UnicodeDecodeError:
        return {
            'ids': [],
            'tokens': [],
            'error': 'Invalid UTF-8 encoding'
        }
    except Exception as e:
        return {
            'ids': [],
            'tokens': [],
            'error': f'Tokenization failed: {str(e)}'
        }

# Usage
result = robust_tokenize("Your text here", tokenizer)
if 'error' in result:
    print(f"Error: {result['error']}")
elif 'warning' in result:
    print(f"Warning: {result['warning']}")
else:
    print(f"Success: {len(result['ids'])} tokens")
```

### Handling Multilingual Edge Cases

```python
def multilingual_safe_tokenize(text, tokenizer):
    """
    Handle multilingual text edge cases:
    - Mixed scripts (English + Chinese + Arabic)
    - Right-to-left languages
    - Emojis and special characters
    """
    import unicodedata
    
    # Normalize Unicode (NFC form)
    text = unicodedata.normalize('NFC', text)
    
    # Detect if text contains multiple scripts
    scripts = set()
    for char in text:
        try:
            scripts.add(unicodedata.name(char).split()[0])
        except:
            pass
    
    if len(scripts) > 3:
        print(f"⚠️  Mixed scripts detected: {len(scripts)} different scripts")
    
    # Tokenize
    encoding = tokenizer.encode(text)
    
    # Calculate efficiency (tokens per character)
    efficiency = len(text) / len(encoding.ids) if encoding.ids else 0
    
    if efficiency < 1.5:
        print(f"⚠️  Low efficiency: {efficiency:.2f} chars/token")
        print(f"   Consider using multilingual tokenizer")
    
    return encoding

# Test with mixed text
mixed_text = "Hello 世界 مرحبا 🌍"  # English, Chinese, Arabic, Emoji
result = multilingual_safe_tokenize(mixed_text, tokenizer)
```

---

## 4. Security Considerations

### Input Sanitization

```python
def sanitize_input(text, max_length=10000):
    """
    Prevent malicious inputs from causing issues:
    - Extremely long inputs (DOS)
    - Repeated characters (token explosion)
    - Null bytes
    - Script injection
    """
    if text is None:
        return ""
    
    # Check length
    if len(text) > max_length:
        print(f"⚠️  Input too long ({len(text)} chars), truncating to {max_length}")
        text = text[:max_length]
    
    # Remove null bytes
    text = text.replace('\0', '')
    
    # Detect repeated character attacks (e.g., "aaaaaaa..." x 100000)
    import re
    if re.search(r'(.)\1{100,}', text):
        print("⚠️  Suspicious repeated character pattern detected")
        # Collapse repeated chars to max 100
        text = re.sub(r'(.)\1{100,}', r'\1' * 100, text)
    
    # Remove other dangerous patterns
    text = text.replace('\x00', '')  # Null bytes
    
    return text

def safe_tokenize(text, tokenizer):
    """Wrapper that sanitizes before tokenizing"""
    clean_text = sanitize_input(text)
    return tokenizer.encode(clean_text)
```

### Rate Limiting (for APIs)

```python
from collections import deque
from time import time

class RateLimitedTokenizer:
    """
    Tokenizer with rate limiting to prevent abuse.
    Useful when exposing tokenization as an API.
    """
    def __init__(self, tokenizer, max_requests=100, window_seconds=60):
        self.tokenizer = tokenizer
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = deque()
    
    def _clean_old_requests(self):
        """Remove requests outside the time window"""
        cutoff = time() - self.window_seconds
        while self.requests and self.requests[0] < cutoff:
            self.requests.popleft()
    
    def tokenize(self, text):
        """Tokenize with rate limiting"""
        self._clean_old_requests()
        
        if len(self.requests) >= self.max_requests:
            raise Exception(f"Rate limit exceeded: {self.max_requests} requests per {self.window_seconds}s")
        
        # Record this request
        self.requests.append(time())
        
        # Perform tokenization
        return self.tokenizer.encode(text)

# Usage
tokenizer = Tokenizer.from_pretrained("bert-base-uncased")
rate_limited = RateLimitedTokenizer(tokenizer, max_requests=10, window_seconds=60)

# Will work for first 10 requests in a minute, then block
```

---

## 5. Monitoring & Debugging

### Tokenization Statistics

```python
class TokenizationMonitor:
    """
    Monitor tokenization patterns to detect issues.
    """
    def __init__(self):
        self.stats = {
            'total_texts': 0,
            'total_tokens': 0,
            'empty_texts': 0,
            'truncated_texts': 0,
            'errors': 0,
            'token_lengths': [],
        }
    
    def record(self, text, encoding, error=None):
        """Record tokenization result"""
        self.stats['total_texts'] += 1
        
        if error:
            self.stats['errors'] += 1
            return
        
        if not text or not text.strip():
            self.stats['empty_texts'] += 1
            return
        
        num_tokens = len(encoding.ids)
        self.stats['total_tokens'] += num_tokens
        self.stats['token_lengths'].append(num_tokens)
        
        if encoding.truncated if hasattr(encoding, 'truncated') else False:
            self.stats['truncated_texts'] += 1
    
    def report(self):
        """Generate statistics report"""
        import statistics
        
        print("\n" + "="*60)
        print("TOKENIZATION STATISTICS")
        print("="*60)
        print(f"Total texts processed: {self.stats['total_texts']:,}")
        print(f"Total tokens generated: {self.stats['total_tokens']:,}")
        print(f"Empty texts: {self.stats['empty_texts']:,}")
        print(f"Truncated texts: {self.stats['truncated_texts']:,}")
        print(f"Errors: {self.stats['errors']:,}")
        
        if self.stats['token_lengths']:
            print(f"\nToken Length Statistics:")
            print(f"  Mean: {statistics.mean(self.stats['token_lengths']):.1f}")
            print(f"  Median: {statistics.median(self.stats['token_lengths']):.1f}")
            print(f"  Min: {min(self.stats['token_lengths'])}")
            print(f"  Max: {max(self.stats['token_lengths'])}")
            print(f"  Std Dev: {statistics.stdev(self.stats['token_lengths']):.1f}")
        
        # Calculate efficiency
        if self.stats['total_texts'] > 0:
            avg_tokens = self.stats['total_tokens'] / self.stats['total_texts']
            print(f"\nAverage tokens per text: {avg_tokens:.1f}")
        
        print("="*60)

# Usage
monitor = TokenizationMonitor()

texts = ["Sample text 1", "Sample text 2", ""]
for text in texts:
    try:
        encoding = tokenizer.encode(text)
        monitor.record(text, encoding)
    except Exception as e:
        monitor.record(text, None, error=str(e))

monitor.report()
```

### Debugging Tokenization Issues

```python
def debug_tokenization(text, tokenizer):
    """
    Detailed debugging info for problematic tokenization.
    """
    print("\n" + "="*60)
    print("TOKENIZATION DEBUG INFO")
    print("="*60)
    
    # Basic info
    print(f"\nInput text: '{text}'")
    print(f"Length: {len(text)} characters")
    print(f"Bytes: {len(text.encode('utf-8'))} bytes")
    
    # Character analysis
    import unicodedata
    print(f"\nCharacter breakdown:")
    for i, char in enumerate(text[:50]):  # First 50 chars
        name = unicodedata.name(char, "UNKNOWN")
        print(f"  [{i}] '{char}' (U+{ord(char):04X}) - {name}")
    
    if len(text) > 50:
        print(f"  ... and {len(text)-50} more characters")
    
    # Tokenization
    try:
        encoding = tokenizer.encode(text)
        
        print(f"\nTokenization result:")
        print(f"  Tokens: {len(encoding.ids)}")
        print(f"  Token IDs: {encoding.ids[:20]}")  # First 20
        print(f"  Token strings: {encoding.tokens[:20]}")
        
        # Alignment
        if hasattr(encoding, 'offsets') and encoding.offsets:
            print(f"\nToken alignment (first 10):")
            for i, (token, (start, end)) in enumerate(zip(encoding.tokens[:10], encoding.offsets[:10])):
                original = text[start:end]
                print(f"  Token {i}: '{token}' <- '{original}' (chars {start}-{end})")
        
        # Efficiency metrics
        chars_per_token = len(text) / len(encoding.ids) if encoding.ids else 0
        print(f"\nEfficiency:")
        print(f"  {chars_per_token:.2f} characters per token")
        
        if chars_per_token < 2:
            print("  ⚠️  Low efficiency - text may be unusual or multilingual")
        elif chars_per_token > 6:
            print("  ⚠️  Very high efficiency - check if tokenization is correct")
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
    
    print("="*60)

# Usage
debug_tokenization("Problematic text here 你好", tokenizer)
```

---

## 6. Production Checklist

### Before Deploying to Production

```python
"""
PRODUCTION TOKENIZATION CHECKLIST
=================================

Performance:
  ✅ Using batch encoding (not sequential)
  ✅ Optimal batch size determined
  ✅ Parallel processing for large datasets
  ✅ Lazy loading for multi-model systems

Memory:
  ✅ Streaming for large files
  ✅ Proper cleanup after batches
  ✅ Memory limits enforced
  ✅ Tokenizer reuse (not recreation)

Robustness:
  ✅ Error handling for empty inputs
  ✅ Truncation for long inputs
  ✅ Handling of invalid UTF-8
  ✅ Fallback strategies defined

Security:
  ✅ Input sanitization
  ✅ Length limits enforced
  ✅ Rate limiting (for APIs)
  ✅ Suspicious pattern detection

Monitoring:
  ✅ Token count tracking
  ✅ Error rate monitoring
  ✅ Performance metrics
  ✅ Alerting on anomalies

Testing:
  ✅ Unit tests for edge cases
  ✅ Load testing with production data
  ✅ Multilingual test cases
  ✅ Performance benchmarks

Documentation:
  ✅ API documentation
  ✅ Error codes defined
  ✅ Rate limits documented
  ✅ Example usage provided
"""
```

---

## 7. Common Production Issues & Solutions

### Issue 1: Tokenization is Slow

**Problem**: Processing 1M texts takes hours

**Solutions**:
```python
# 1. Use batch encoding
encodings = tokenizer.encode_batch(texts, batch_size=1000)

# 2. Enable parallel processing
from joblib import Parallel, delayed
results = Parallel(n_jobs=-1)(delayed(tokenizer.encode)(text) for text in texts)

# 3. Use faster tokenizer
# HuggingFace Tokenizers (Rust) > Python implementations
```

### Issue 2: Out of Memory

**Problem**: Process crashes with OOM when tokenizing large dataset

**Solutions**:
```python
# 1. Stream processing
def stream_tokenize(file_path):
    with open(file_path) as f:
        for line in f:
            yield tokenizer.encode(line.strip())

# 2. Smaller batches
batch_size = 100  # Reduce from 1000

# 3. Free memory explicitly
import gc
for batch in batches:
    process_batch(batch)
    del batch
    gc.collect()
```

### Issue 3: Inconsistent Token Counts

**Problem**: Same text gives different token counts in different runs

**Solutions**:
```python
# Check for:
# 1. Leading/trailing whitespace
text = text.strip()

# 2. Different tokenizer versions
# Lock version in requirements.txt: tokenizers==0.15.0

# 3. Unicode normalization
import unicodedata
text = unicodedata.normalize('NFC', text)
```

### Issue 4: High API Costs

**Problem**: Tokenization costs are too high for API calls

**Solutions**:
```python
# 1. Cache tokenization results
from functools import lru_cache

@lru_cache(maxsize=10000)
def cached_tokenize(text):
    return tuple(tokenizer.encode(text).ids)

# 2. Estimate without tokenizing (for filtering)
def estimate_tokens(text):
    # Rough estimate: 1 token ≈ 4 characters for English
    return len(text) // 4

# 3. Pre-filter long texts
if estimate_tokens(text) > max_tokens:
    text = text[:max_tokens * 4]  # Rough truncation
```

---

## Summary

Production tokenization requires more than just calling `tokenizer.encode()`:

1. **Performance**: Batch processing, parallelization, optimal batch sizes
2. **Memory**: Streaming, lazy loading, proper cleanup
3. **Robustness**: Error handling, edge cases, fallbacks
4. **Security**: Input sanitization, rate limiting, monitoring
5. **Debugging**: Detailed logging, statistics, diagnostics

**Remember**: Test with real production data, not just clean examples!

---

## Additional Resources

- [HuggingFace Tokenizers Docs](https://huggingface.co/docs/tokenizers)
- [Performance Benchmarks](https://github.com/huggingface/tokenizers/tree/main/benchmarks)
- [Production Best Practices](https://huggingface.co/docs/transformers/performance)

---

Built for production environments 🏭
