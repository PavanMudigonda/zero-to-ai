# Phase 19: Real-Time & Streaming AI

## Overview
Learn how to build real-time AI applications with streaming responses, WebSocket connections, and progressive loading.

**Duration:** 8 hours (5 notebooks + materials)

**Topics Covered:**
1. Streaming LLM Responses
2. WebSocket Connections  
3. Chunked Generation
4. Real-Time RAG
5. Production Streaming Systems

## Learning Objectives

By the end of this phase, you will be able to:
- Implement Server-Sent Events (SSE) for streaming
- Build WebSocket-based real-time chat applications
- Handle progressive loading and chunked responses
- Create streaming RAG pipelines
- Deploy production-ready streaming systems
- Optimize for latency and throughput

## Prerequisites

- Strong Python programming skills
- Understanding of LLMs and APIs
- Basic knowledge of async/await
- Familiarity with web technologies
- Completed Phases 1-10

## Course Content

### 1. Streaming Responses (90 minutes)
**File:** `01_streaming_responses.ipynb`

**Topics:**
- OpenAI streaming API (`stream=True`)
- Server-Sent Events (SSE) protocol
- Handling stream chunks
- Real-time token processing
- Error handling in streams
- Progress indicators

**Key Code:**
```python
# OpenAI Streaming
for chunk in client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Tell me a story"}],
    stream=True
):
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")

# FastAPI SSE
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

@app.get("/stream")
async def stream_response():
    async def generate():
        for chunk in get_llm_stream():
            yield f"data: {chunk}\\n\\n"
    return StreamingResponse(generate(), media_type="text/event-stream")
```

### 2. WebSocket Connections (90 minutes)
**File:** `02_websocket_connections.ipynb`

**Topics:**
- WebSocket protocol basics
- Bidirectional communication
- FastAPI WebSocket endpoints
- Client-side WebSocket handling
- Connection management
- Heartbeat and reconnection

**Key Code:**
```python
# Server
from fastapi import WebSocket

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        response = await process_message(data)
        await websocket.send_text(response)

# Client
import websockets

async with websockets.connect("ws://localhost:8000/ws") as ws:
    await ws.send("Hello")
    response = await ws.recv()
```

### 3. Chunked Generation (75 minutes)
**File:** `03_chunked_generation.ipynb`

**Topics:**
- Progressive rendering
- Chunk size optimization
- Buffering strategies
- Token accumulation
- UI update patterns
- Performance optimization

**Key Techniques:**
- Sentence-level chunking
- Token buffering
- Delta updates
- Smooth rendering

### 4. Real-Time RAG (90 minutes)
**File:** `04_real_time_rag.ipynb`

**Topics:**
- Streaming search results
- Progressive context loading
- Incremental vector search
- Streaming summarization
- Real-time document processing
- Hybrid search streaming

**Architecture:**
```
User Query → Vector Search (stream) → Document Retrieval (progressive)
            ↓
        Context Assembly (incremental)
            ↓
        LLM Generation (streaming)
            ↓
        Response (real-time)
```

### 5. Production Streaming (120 minutes)
**File:** `05_production_streaming.ipynb`

**Topics:**
- Load balancing streaming connections
- Connection pooling
- Rate limiting
- Backpressure handling
- Monitoring and metrics
- Error recovery
- Scaling strategies

**Production Considerations:**
- Connection limits
- Timeout management
- Memory management
- Graceful degradation
- Observability

## Assessment

### Pre-Quiz (10 questions)
**File:** `pre-quiz.md`

Test your baseline knowledge of:
- Streaming protocols
- Async programming
- Real-time systems
- Performance concepts

### Post-Quiz (18 questions + 3 bonus)
**File:** `post-quiz.md`

Comprehensive assessment covering:
- SSE vs WebSocket trade-offs
- Streaming implementation patterns
- Production deployment
- Performance optimization
- Error handling strategies

### Assignment (100 points)
**File:** `assignment.md`

**Project:** Build a Production Streaming RAG Chatbot

**Requirements:**
1. **Streaming Backend (30 points)**
   - FastAPI with SSE or WebSocket
   - OpenAI streaming integration
   - Vector database connection
   - Error handling

2. **Real-Time Frontend (25 points)**
   - React or vanilla JS
   - Smooth typing animation
   - Progress indicators
   - Reconnection logic

3. **RAG Pipeline (25 points)**
   - Document indexing
   - Streaming search
   - Progressive context loading
   - Citation tracking

4. **Production Features (20 points)**
   - Rate limiting
   - Monitoring
   - Load testing
   - Documentation

**Bonus (10 points):**
- Multi-user support
- Advanced caching
- WebSocket fallback

### Challenges (7 progressive tasks)
**File:** `challenges.md`

1. **Basic Streaming** - Implement OpenAI streaming (30 min)
2. **SSE Endpoint** - Create FastAPI SSE endpoint (45 min)
3. **WebSocket Chat** - Build bi-directional chat (60 min)
4. **Chunked UI** - Progressive rendering (45 min)
5. **Streaming RAG** - Real-time document search (90 min)
6. **Load Testing** - Handle 100 concurrent connections (60 min)
7. **Production Deploy** - Deploy with monitoring (120 min)

## Technical Stack

**Backend:**
- FastAPI
- OpenAI Python SDK
- WebSockets library
- asyncio

**Frontend:**
- HTML/CSS/JavaScript
- EventSource API
- WebSocket API
- React (optional)

**Infrastructure:**
- Nginx (reverse proxy)
- Redis (connection management)
- Prometheus (monitoring)
- Docker

## Best Practices

### Performance
- Use connection pooling
- Implement backpressure
- Buffer appropriately
- Monitor latency

### Reliability
- Handle disconnections gracefully
- Implement retry logic
- Timeout management
- Circuit breakers

### Security
- Rate limiting per user
- Input validation
- Authentication tokens
- CORS configuration

### User Experience
- Loading indicators
- Smooth animations
- Error messages
- Offline support

## Common Patterns

### Pattern 1: Simple SSE Streaming
```python
async def stream_generator():
    async for chunk in llm_stream():
        yield f"data: {json.dumps({'text': chunk})}\\n\\n"
```

### Pattern 2: WebSocket with Heartbeat
```python
async def heartbeat(websocket):
    while True:
        await asyncio.sleep(30)
        await websocket.send_json({"type": "ping"})
```

### Pattern 3: Streaming RAG
```python
async def streaming_rag(query):
    # Search
    docs = await vector_search(query)
    yield {"type": "sources", "data": docs}
    
    # Generate
    async for chunk in llm_generate(query, docs):
        yield {"type": "text", "data": chunk}
```

## Real-World Examples

1. **ChatGPT-style Interface**
   - Streaming responses
   - Typing indicators
   - Stop generation
   - Copy/retry

2. **Live Document Q&A**
   - Upload and index
   - Real-time search
   - Streaming answers
   - Source citations

3. **Multi-User Chat**
   - WebSocket rooms
   - Broadcast messages
   - User presence
   - Typing indicators

## Resources

### Documentation
- [OpenAI Streaming](https://platform.openai.com/docs/api-reference/streaming)
- [FastAPI WebSockets](https://fastapi.tiangolo.com/advanced/websockets/)
- [MDN Server-Sent Events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)
- [WebSocket Protocol](https://datatracker.ietf.org/doc/html/rfc6455)

### Libraries
- `fastapi` - Modern Python web framework
- `websockets` - WebSocket client/server
- `sse-starlette` - SSE for Starlette/FastAPI
- `httpx` - Async HTTP client

### Tools
- Postman - API testing with WebSocket support
- k6 - Load testing
- WebSocket King - WebSocket client tester

## Troubleshooting

### Issue: Stream stops unexpectedly
**Solution:** Check timeout settings, implement heartbeat

### Issue: High latency
**Solution:** Optimize chunk size, reduce buffering, check network

### Issue: Connection drops
**Solution:** Implement reconnection logic, use exponential backoff

### Issue: Memory leaks
**Solution:** Close connections properly, cleanup event listeners

## Next Steps

After completing this phase:
1. Review Phase 18 (AI Safety) for securing streaming apps
2. Explore Phase 14 (AI Agents) for multi-agent streaming
3. Check Phase 17 (Low-Code) for Gradio/Streamlit streaming
4. Build your own production streaming application

## Time Estimates

- **Total Duration:** 8 hours
- **Notebooks:** 6-7 hours
- **Assignment:** 4-6 hours  
- **Challenges:** 6-8 hours
- **Total with Practice:** 16-20 hours

## Success Criteria

- ✅ Implement SSE and WebSocket endpoints
- ✅ Build real-time chat interface
- ✅ Create streaming RAG pipeline
- ✅ Handle 100+ concurrent connections
- ✅ Deploy production streaming app
- ✅ Monitor and optimize performance

---

**Note:** This is a foundational module for building modern AI applications. Master these concepts to create responsive, real-time user experiences.
