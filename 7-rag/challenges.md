# Challenges: RAG Systems

> **Hands-on challenges to master Retrieval-Augmented Generation**

## 🚀 Challenge 1: The Chunking Optimization Game

**Difficulty:** ⭐⭐ Beginner-Intermediate  
**Time:** 45-60 minutes  
**Concepts:** Text chunking, retrieval accuracy, semantic boundaries

### The Problem
Chunking is critical for RAG - bad chunks = bad retrieval = bad answers. Find the optimal chunking strategy!

### Your Task
1. Take a long technical document (e.g., Python documentation, research paper)
2. Create 10 test questions that require specific passages
3. Try 5 different chunking strategies:
   - Fixed size (256, 512, 1024 tokens)
   - Sentence-based
   - Paragraph-based
   - Semantic (embeddings-based)
   - Hierarchical (sections → paragraphs → sentences)
4. Measure which strategy retrieves the right passages most often

### Evaluation Metrics
```python
# For each question, check if correct passage is in top-3 results
hit_rate = correct_chunks_retrieved / total_questions

# Average position of correct chunk
mrr = mean([1/rank for rank in chunk_positions])
```

### Success Criteria
- [ ] Test all 5 chunking methods
- [ ] Create visualization comparing methods
- [ ] Identify when each method works best
- [ ] Provide recommendations

<details>
<summary>💡 Hint</summary>
Different content types need different strategies:
- Code documentation: Semantic chunking works well
- Narrative text: Paragraph-based is often good
- Q&A: Sentence-based can work
</details>

---

## 🚀 Challenge 2: Query Expansion Techniques

**Difficulty:** ⭐⭐⭐ Intermediate  
**Time:** 1-2 hours  
**Concepts:** Query understanding, multi-query retrieval, HyDE

### The Problem
User queries are often vague or poorly worded. Expand them to improve retrieval!

### Your Task
Implement 3 query expansion techniques:

**Technique 1: Multi-Query Generation**
```python
# Original: "How to use python lists?"
# Expanded:
# - "Python list operations tutorial"
# - "Add items to Python list"
# - "List methods in Python"
# - "Python array vs list"
```

**Technique 2: Hypothetical Document Embeddings (HyDE)**
```python
# Original query: "What causes climate change?"
# Generate hypothetical answer, then search for it:
generated_answer = llm("Write a detailed answer about climate change causes...")
search_embedding = embed(generated_answer)
```

**Technique 3: Query Decomposition**
```python
# Complex: "Compare Python and JavaScript for web development"
# Decompose:
# - "Python for web development features"
# - "JavaScript for web development features"
# - "Python vs JavaScript comparison"
```

### Comparison Task
- Test on 20 diverse questions
- Compare retrieval accuracy for each method
- Analyze latency and cost tradeoffs
- Identify best use cases

<details>
<summary>💡 Hint</summary>
Multi-query can be parallelized for speed.
HyDE works great when you know the answer format.
Query decomposition is powerful for complex questions.
</details>

---

## 🚀 Challenge 3: The Hallucination Hunter

**Difficulty:** ⭐⭐⭐⭐ Advanced  
**Time:** 2-3 hours  
**Concepts:** Faithfulness, fact verification, hallucination detection

### The Problem
LLMs sometimes "hallucinate" - generate plausible-sounding but incorrect information. Catch them!

### Your Task
Build a hallucination detection system:

1. **Faithfulness Scoring**
   - Check if answer is supported by retrieved context
   - Use entailment model or LLM-as-judge
   - Score 0-1 for how well grounded the answer is

2. **Citation Verification**
   - Extract claims from answer
   - Verify each claim against source documents
   - Flag unsupported claims

3. **Confidence Calibration**
   - Estimate answer confidence
   - Compare with actual correctness
   - Calibrate model to be more honest

### Implementation
```python
class HallucinationDetector:
    def check_faithfulness(self, answer, context):
        """Score how well answer is supported by context."""
        # TODO: Implement
        pass
    
    def verify_citations(self, answer, sources):
        """Verify each claim in answer."""
        claims = self.extract_claims(answer)
        verified = []
        for claim in claims:
            is_supported = self.verify_claim(claim, sources)
            verified.append({
                "claim": claim,
                "supported": is_supported,
                "confidence": ...
            })
        return verified
```

### Test Dataset
Create 30 questions with known hallucination triggers:
- Questions outside knowledge base
- Ambiguous questions
- Questions with conflicting information
- Questions requiring calculation/reasoning

<details>
<summary>💡 Hint</summary>
Use models like "microsoft/deberta-v3-large" for entailment.
Compare multiple answer generations - consistent = likely correct.
Prompt engineering: "Only answer if you're certain. Otherwise say 'I don't know.'"
</details>

---

## 🚀 Challenge 4: Conversational RAG

**Difficulty:** ⭐⭐⭐⭐ Advanced  
**Time:** 3-4 hours  
**Concepts:** Dialogue management, context tracking, memory

### The Problem
Most RAG systems handle single questions. Build one that handles multi-turn conversations!

### Your Task
Handle conversation like this:
```
User: "What are the benefits of Python?"
Bot: "Python offers readability, extensive libraries..." [uses RAG]

User: "What about performance?"  # Implicit: Python performance
Bot: "Python is slower than compiled languages..." [understands context]

User: "Compare it to Java"  # Implicit: Python vs Java performance
Bot: "Java is generally faster because..." [maintains full context]
```

### Requirements
- [ ] Track conversation history
- [ ] Rewrite queries with context (coreference resolution)
- [ ] Maintain entity tracking
- [ ] Handle follow-up questions
- [ ] Know when to retrieve vs use previous context
- [ ] Manage token budget (conversation history grows!)

### Conversation Management
```python
class ConversationalRAG:
    def __init__(self):
        self.conversation_history = []
        self.entity_tracker = {}
    
    def rewrite_query_with_context(self, current_query, history):
        """Rewrite query to be standalone using conversation context."""
        # "What about performance?" → "What about Python performance?"
        pass
    
    def should_retrieve(self, query, history):
        """Decide if we need new retrieval or can use context."""
        # Avoid unnecessary retrievals for clarification questions
        pass
    
    def chat(self, user_message):
        # Rewrite query
        # Retrieve if needed
        # Generate with conversation context
        # Update history
        pass
```

<details>
<summary>💡 Hint</summary>
Use LLM to rewrite queries: "Given conversation history, rewrite this query to be standalone"
Keep sliding window of last N turns to manage tokens.
Detect if query is clarification vs new topic.
</details>

---

## 🚀 Challenge 5: Multi-Modal RAG

**Difficulty:** ⭐⭐⭐⭐⭐ Expert  
**Time:** 4-6 hours  
**Concepts:** Multi-modal embeddings, vision-language models, hybrid retrieval

### The Problem
Real documents have images, tables, charts - not just text. Build RAG that handles it all!

### Your Task
Build a system that processes:
- **Text:** Standard RAG
- **Images:** Visual search with CLIP
- **Tables:** Structured data retrieval
- **Diagrams:** Caption extraction + visual search
- **Code:** Syntax-aware chunking

### Example Use Case: Technical Documentation
```
User: "Show me the architecture diagram and explain the components"

System should:
1. Retrieve relevant diagram (image similarity)
2. Extract/generate diagram description
3. Retrieve text about components
4. Combine image + text in answer
```

### Implementation Components
1. **Multi-Modal Embeddings:**
   - Text: sentence-transformers
   - Images: CLIP
   - Tables: Table-specific embedders

2. **Hybrid Retrieval:**
   - Combine results from different modalities
   - Weight by relevance and modality type

3. **Multi-Modal Generation:**
   - GPT-4 Vision for image understanding
   - Generate answers referencing both text and images

### Success Criteria
- [ ] Process PDFs with images/tables
- [ ] Retrieve relevant visuals for queries
- [ ] Generate answers combining modalities
- [ ] Handle queries like "show me", "diagram of", "table showing"

<details>
<summary>💡 Hint</summary>
Use GPT-4 Vision or LLaVA for image understanding.
CLIP for image-text similarity.
Separate vector stores per modality, then merge results.
</details>

---

## 🏆 Meta Challenge: RAG Optimization Competition

**Difficulty:** ⭐⭐⭐⭐⭐ Expert  
**Time:** 8-12 hours  
**Concepts:** End-to-end optimization, systematic evaluation

### The Ultimate Challenge
Build the best RAG system for a specific domain and prove it!

### Competition Format
1. **Choose Domain:** Medical, legal, technical docs, customer support, etc.
2. **Build System:** Full RAG pipeline
3. **Create Benchmark:** 100+ test questions with ground truth
4. **Optimize Everything:**
   - Chunking strategy
   - Embedding model
   - Retrieval method
   - Re-ranking
   - Generation prompts
   - Cost/latency tradeoffs

### Leaderboard Metrics
- **Accuracy:** % of correct answers
- **Faithfulness:** % of answers supported by context
- **Latency:** Average response time
- **Cost:** $ per 1000 queries
- **User Satisfaction:** Human evaluation (1-5)

### Deliverables
- Complete RAG system (code)
- Benchmark dataset (questions + answers)
- Evaluation results (metrics + analysis)
- Technical report (methodology + findings)
- Demo (Gradio/Streamlit app)

### Bonus Points
- Open-source your solution
- Deploy publicly
- Write blog post about optimizations
- Beat baseline by >20% accuracy

---

## 📊 Challenge Progress Tracker

- [ ] Challenge 1: Chunking Optimization
- [ ] Challenge 2: Query Expansion
- [ ] Challenge 3: Hallucination Hunter
- [ ] Challenge 4: Conversational RAG
- [ ] Challenge 5: Multi-Modal RAG
- [ ] Meta Challenge: RAG Optimization Competition

---

## 🏅 Share Your Work

Post your challenge solutions:
- **GitHub:** Share your repos
- **Discussions:** [Challenges Category](https://github.com/zero-to-ai/discussions/categories/challenges)
- **Blog:** Write about your learnings
- **Twitter:** Tag `#ZeroToAI` `#RAGChallenge`

---

## 💡 Tips for Success

1. **Start Simple:** Get basic version working first
2. **Measure Everything:** Metrics guide optimization
3. **Error Analysis:** Study failures to improve
4. **Read Papers:** Many techniques have research backing
5. **Use Tools:** LangChain, LlamaIndex can speed things up
6. **Iterate:** First version won't be perfect

---

## 📚 Helpful Resources

- [RAG Evaluation Framework](https://github.com/explodinggradients/ragas)
- [Advanced RAG Patterns](https://blog.langchain.dev/deconstructing-rag/)
- [BEIR Benchmark](https://github.com/beir-cellar/beir)
- [Multi-Modal RAG](https://blog.llamaindex.ai/multi-modal-rag-621de7525fea)

---

**Happy building! 🚀**

Remember: RAG is about the journey of optimization, not just the destination!
