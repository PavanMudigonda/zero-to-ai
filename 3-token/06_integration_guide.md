# Integration Guide: Using Tokenizers with Popular Frameworks

## Connecting Tokenizers to ML Workflows

This guide shows how to integrate tokenizers with:
- 🤗 Transformers
- PyTorch & TensorFlow
- FastAPI / Flask (APIs)
- Streaming applications
- Database storage

---

## 1. HuggingFace Transformers Integration

### Loading Pretrained Models with Tokenizers

```python
from transformers import AutoTokenizer, AutoModel
import torch

# Load tokenizer and model together
model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Tokenize and get embeddings
text = "Hello, world!"
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)

# Extract embeddings
embeddings = outputs.last_hidden_state
print(f"Shape: {embeddings.shape}")  # [batch_size, seq_len, hidden_dim]
```

### Batch Processing with Transformers

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased")

# Batch of texts
texts = [
    "This movie is great!",
    "I didn't like it.",
    "Amazing performance!",
]

# Tokenize with padding and truncation
inputs = tokenizer(
    texts,
    padding=True,           # Pad to longest in batch
    truncation=True,        # Truncate if too long
    max_length=512,         # Max sequence length
    return_tensors="pt"     # Return PyTorch tensors
)

# Forward pass
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.softmax(outputs.logits, dim=-1)

print(f"Predictions shape: {predictions.shape}")  # [3, num_classes]
```

### Custom Dataset with Tokenization

```python
from torch.utils.data import Dataset, DataLoader
from transformers import AutoTokenizer

class TextDataset(Dataset):
    """Custom dataset with tokenization"""
    def __init__(self, texts, labels, tokenizer, max_length=128):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_length = max_length
    
    def __len__(self):
        return len(self.texts)
    
    def __getitem__(self, idx):
        text = self.texts[idx]
        label = self.labels[idx]
        
        # Tokenize
        encoding = self.tokenizer(
            text,
            add_special_tokens=True,
            max_length=self.max_length,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )
        
        return {
            'input_ids': encoding['input_ids'].flatten(),
            'attention_mask': encoding['attention_mask'].flatten(),
            'label': torch.tensor(label, dtype=torch.long)
        }

# Usage
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
texts = ["Text 1", "Text 2", "Text 3"]
labels = [0, 1, 0]

dataset = TextDataset(texts, labels, tokenizer)
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

for batch in dataloader:
    print(f"Input IDs shape: {batch['input_ids'].shape}")
    print(f"Attention mask shape: {batch['attention_mask'].shape}")
    print(f"Labels shape: {batch['label'].shape}")
    break
```

---

## 2. PyTorch Integration

### Using Tokenizers in PyTorch Models

```python
import torch
import torch.nn as nn
from tokenizers import Tokenizer

class TextClassifier(nn.Module):
    """Simple classifier using tokenized input"""
    def __init__(self, vocab_size, embedding_dim, hidden_dim, num_classes):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim, padding_idx=0)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, num_classes)
    
    def forward(self, input_ids, attention_mask):
        # input_ids: [batch_size, seq_len]
        embedded = self.embedding(input_ids)  # [batch, seq, embed]
        
        # Pack padded sequence (using attention_mask)
        lengths = attention_mask.sum(dim=1).cpu()
        packed = nn.utils.rnn.pack_padded_sequence(
            embedded, lengths, batch_first=True, enforce_sorted=False
        )
        
        # LSTM
        _, (hidden, _) = self.lstm(packed)  # hidden: [1, batch, hidden]
        
        # Classify
        output = self.fc(hidden.squeeze(0))  # [batch, num_classes]
        return output

# Load tokenizer
tokenizer = Tokenizer.from_pretrained("bert-base-uncased")
vocab_size = tokenizer.get_vocab_size()

# Create model
model = TextClassifier(vocab_size=vocab_size, embedding_dim=128, hidden_dim=256, num_classes=2)

# Tokenize input
texts = ["This is great!", "Not good."]
encodings = tokenizer.encode_batch(texts)

# Convert to tensors
input_ids = torch.tensor([enc.ids for enc in encodings])
attention_mask = torch.tensor([enc.attention_mask for enc in encodings])

# Forward pass
outputs = model(input_ids, attention_mask)
print(f"Outputs: {outputs.shape}")  # [2, 2]
```

---

## 3. TensorFlow / Keras Integration

### TensorFlow Dataset Pipeline

```python
import tensorflow as tf
from transformers import AutoTokenizer

def create_tf_dataset(texts, labels, tokenizer, max_length=128, batch_size=32):
    """Create TensorFlow dataset with tokenization"""
    
    # Tokenize all texts
    encodings = tokenizer(
        texts,
        padding='max_length',
        truncation=True,
        max_length=max_length,
        return_tensors='tf'
    )
    
    # Create dataset
    dataset = tf.data.Dataset.from_tensor_slices((
        {
            'input_ids': encodings['input_ids'],
            'attention_mask': encodings['attention_mask']
        },
        labels
    ))
    
    return dataset.batch(batch_size)

# Usage
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
texts = ["Text 1", "Text 2", "Text 3"] * 10
labels = [0, 1, 0] * 10

dataset = create_tf_dataset(texts, labels, tokenizer)

for batch in dataset.take(1):
    inputs, labels = batch
    print(f"Input IDs: {inputs['input_ids'].shape}")
    print(f"Labels: {labels.shape}")
```

### Custom Keras Layer

```python
import tensorflow as tf
from transformers import TFAutoModel

class TokenizedTextModel(tf.keras.Model):
    """Keras model with tokenization"""
    def __init__(self, model_name, num_classes):
        super().__init__()
        self.transformer = TFAutoModel.from_pretrained(model_name)
        self.dropout = tf.keras.layers.Dropout(0.3)
        self.classifier = tf.keras.layers.Dense(num_classes, activation='softmax')
    
    def call(self, inputs, training=False):
        # inputs: dict with 'input_ids' and 'attention_mask'
        outputs = self.transformer(inputs, training=training)
        
        # Use [CLS] token representation
        cls_output = outputs.last_hidden_state[:, 0, :]
        
        # Classify
        dropped = self.dropout(cls_output, training=training)
        return self.classifier(dropped)

# Create model
model = TokenizedTextModel('bert-base-uncased', num_classes=2)

# Compile
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train (dataset from above)
# model.fit(dataset, epochs=3)
```

---

## 4. FastAPI Integration (REST API)

### Creating a Tokenization API

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoTokenizer
from typing import List, Optional
import uvicorn

app = FastAPI(title="Tokenization API")

# Load tokenizer at startup
tokenizer = None

@app.on_event("startup")
async def load_tokenizer():
    global tokenizer
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
    print("✅ Tokenizer loaded")

# Request/Response models
class TokenizeRequest(BaseModel):
    text: str
    max_length: Optional[int] = 512
    add_special_tokens: Optional[bool] = True

class TokenizeResponse(BaseModel):
    tokens: List[str]
    token_ids: List[int]
    attention_mask: List[int]
    num_tokens: int

class BatchTokenizeRequest(BaseModel):
    texts: List[str]
    max_length: Optional[int] = 512
    padding: Optional[bool] = True

# Endpoints
@app.post("/tokenize", response_model=TokenizeResponse)
async def tokenize_text(request: TokenizeRequest):
    """Tokenize a single text"""
    try:
        encoding = tokenizer(
            request.text,
            max_length=request.max_length,
            truncation=True,
            add_special_tokens=request.add_special_tokens,
            return_attention_mask=True
        )
        
        tokens = tokenizer.convert_ids_to_tokens(encoding['input_ids'])
        
        return TokenizeResponse(
            tokens=tokens,
            token_ids=encoding['input_ids'],
            attention_mask=encoding['attention_mask'],
            num_tokens=len(encoding['input_ids'])
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/batch_tokenize")
async def batch_tokenize(request: BatchTokenizeRequest):
    """Tokenize multiple texts"""
    try:
        encodings = tokenizer(
            request.texts,
            max_length=request.max_length,
            truncation=True,
            padding=request.padding,
            return_attention_mask=True
        )
        
        results = []
        for i in range(len(request.texts)):
            tokens = tokenizer.convert_ids_to_tokens(encodings['input_ids'][i])
            results.append({
                'text': request.texts[i],
                'tokens': tokens,
                'token_ids': encodings['input_ids'][i],
                'num_tokens': len(encodings['input_ids'][i])
            })
        
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/vocab_size")
async def get_vocab_size():
    """Get tokenizer vocabulary size"""
    return {"vocab_size": len(tokenizer)}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "tokenizer_loaded": tokenizer is not None}

# Run: uvicorn api:app --reload
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### Client Example

```python
import requests

# Tokenize single text
response = requests.post(
    "http://localhost:8000/tokenize",
    json={"text": "Hello, world!", "max_length": 512}
)
print(response.json())

# Batch tokenize
response = requests.post(
    "http://localhost:8000/batch_tokenize",
    json={"texts": ["Text 1", "Text 2", "Text 3"], "padding": True}
)
print(response.json())
```

---

## 5. Flask Integration (Simple API)

```python
from flask import Flask, request, jsonify
from transformers import AutoTokenizer

app = Flask(__name__)
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

@app.route('/tokenize', methods=['POST'])
def tokenize():
    """Tokenize endpoint"""
    data = request.json
    text = data.get('text', '')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    # Tokenize
    encoding = tokenizer(text, return_attention_mask=True)
    tokens = tokenizer.convert_ids_to_tokens(encoding['input_ids'])
    
    return jsonify({
        'tokens': tokens,
        'token_ids': encoding['input_ids'],
        'num_tokens': len(tokens)
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

---

## 6. Database Integration

### Storing Tokenized Data

```python
import sqlite3
import json
from transformers import AutoTokenizer

class TokenizedDatabase:
    """Store pre-tokenized texts in database"""
    
    def __init__(self, db_path='tokenized_data.db'):
        self.db_path = db_path
        self.tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
        self._init_db()
    
    def _init_db(self):
        """Create database schema"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tokenized_texts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original_text TEXT NOT NULL,
                token_ids TEXT NOT NULL,
                num_tokens INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def add_text(self, text):
        """Tokenize and store text"""
        encoding = self.tokenizer(text)
        token_ids = json.dumps(encoding['input_ids'])
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO tokenized_texts (original_text, token_ids, num_tokens)
            VALUES (?, ?, ?)
        ''', (text, token_ids, len(encoding['input_ids'])))
        
        conn.commit()
        text_id = cursor.lastrowid
        conn.close()
        
        return text_id
    
    def get_tokenized(self, text_id):
        """Retrieve tokenized text"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT original_text, token_ids, num_tokens
            FROM tokenized_texts
            WHERE id = ?
        ''', (text_id,))
        
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return {
                'text': row[0],
                'token_ids': json.loads(row[1]),
                'num_tokens': row[2]
            }
        return None
    
    def batch_add(self, texts):
        """Batch insert tokenized texts"""
        encodings = self.tokenizer(texts)
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        data = [
            (text, json.dumps(ids), len(ids))
            for text, ids in zip(texts, encodings['input_ids'])
        ]
        
        cursor.executemany('''
            INSERT INTO tokenized_texts (original_text, token_ids, num_tokens)
            VALUES (?, ?, ?)
        ''', data)
        
        conn.commit()
        conn.close()

# Usage
db = TokenizedDatabase()
text_id = db.add_text("Hello, world!")
result = db.get_tokenized(text_id)
print(result)
```

---

## 7. Streaming Applications

### Process Streaming Data

```python
from transformers import AutoTokenizer
import time

class StreamingTokenizer:
    """Tokenize streaming data efficiently"""
    
    def __init__(self, model_name="bert-base-uncased", buffer_size=100):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.buffer = []
        self.buffer_size = buffer_size
    
    def add(self, text):
        """Add text to buffer"""
        self.buffer.append(text)
        
        # Process when buffer is full
        if len(self.buffer) >= self.buffer_size:
            return self.flush()
        
        return None
    
    def flush(self):
        """Process buffered texts"""
        if not self.buffer:
            return []
        
        # Batch tokenize
        encodings = self.tokenizer(
            self.buffer,
            padding=True,
            truncation=True,
            return_tensors='pt'
        )
        
        # Clear buffer
        texts = self.buffer.copy()
        self.buffer = []
        
        return list(zip(texts, encodings['input_ids'], encodings['attention_mask']))

# Usage - simulate streaming
stream_tokenizer = StreamingTokenizer(buffer_size=10)

# Simulate incoming data
for i in range(25):
    text = f"Streaming message {i}"
    result = stream_tokenizer.add(text)
    
    if result:
        print(f"Processed batch of {len(result)} texts")
        # Process the batch...
        time.sleep(0.1)

# Don't forget remaining items
final_batch = stream_tokenizer.flush()
if final_batch:
    print(f"Processed final batch of {len(final_batch)} texts")
```

---

## 8. Integration Checklist

```python
"""
INTEGRATION CHECKLIST
====================

Model Loading:
  ✅ Tokenizer loaded at startup (not per request)
  ✅ Model and tokenizer versions match
  ✅ Proper error handling for loading failures

Performance:
  ✅ Using batch encoding for multiple texts
  ✅ Appropriate max_length set
  ✅ Padding strategy chosen (max_length vs longest)
  ✅ Caching enabled if applicable

Memory Management:
  ✅ Tokenizer shared across requests (not recreated)
  ✅ Large batches split into smaller chunks
  ✅ Proper cleanup of large tensors

Error Handling:
  ✅ Empty input validation
  ✅ Unicode error handling
  ✅ Truncation warnings
  ✅ OOM protection

API Design (if applicable):
  ✅ Health check endpoint
  ✅ Batch processing endpoint
  ✅ Rate limiting
  ✅ Request validation

Testing:
  ✅ Unit tests for edge cases
  ✅ Integration tests with models
  ✅ Load testing
  ✅ Multilingual test cases
"""
```

---

## Summary

**Key Integration Points**:
1. **🤗 Transformers**: Use `AutoTokenizer` for seamless integration
2. **PyTorch/TF**: Create custom datasets with tokenization
3. **APIs**: Load tokenizer once at startup, use batch processing
4. **Databases**: Store pre-tokenized data for faster retrieval
5. **Streaming**: Buffer and batch process for efficiency

**Remember**: Always match tokenizer to your model! 🎯
