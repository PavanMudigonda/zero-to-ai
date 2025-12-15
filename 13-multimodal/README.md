# Phase 12: Multimodal AI

## 🎯 Overview

Go beyond text! Learn to work with Vision-Language Models, Audio AI, and multimodal systems that combine text, images, audio, and video.

**Prerequisites:**
- ✅ Neural Networks & Transformers (Phase 5)
- ✅ LLMs & Prompt Engineering (Phase 10)
- ✅ Python & PyTorch

**Time:** 3-4 weeks | 60-80 hours  
**Outcome:** Build AI systems that understand and generate across multiple modalities

---

## 📚 What You'll Learn

### Vision-Language Models (VLMs)

- [ ] CLIP (Contrastive Language-Image Pretraining)
- [ ] LLaVA (Large Language and Vision Assistant)
- [ ] GPT-4V capabilities and API
- [ ] Gemini Pro Vision
- [ ] Image captioning and VQA (Visual Question Answering)
- [ ] Zero-shot image classification

### Image Generation

- [ ] Stable Diffusion architecture
- [ ] DALL-E 3 API
- [ ] Midjourney concepts
- [ ] ControlNet for guided generation
- [ ] LoRA for Stable Diffusion
- [ ] Prompt engineering for images

### Audio & Speech

- [ ] Whisper (speech-to-text)
- [ ] Text-to-Speech models (Bark, XTTS)
- [ ] Audio classification
- [ ] Music generation (MusicGen)
- [ ] Voice cloning
- [ ] Audio embeddings

### Video Understanding

- [ ] Video captioning
- [ ] Action recognition
- [ ] Temporal understanding
- [ ] Video generation (emerging)

### Multimodal RAG

- [ ] Image + text search
- [ ] Document understanding (OCR + LLM)
- [ ] Multimodal embeddings
- [ ] Cross-modal retrieval

---

## 🗂️ Module Structure

```
12-multimodal/
├── 00_START_HERE.ipynb                # Overview & capabilities
├── vision-language/
│   ├── 01_clip_basics.ipynb           # CLIP fundamentals
│   ├── 02_llava.ipynb                 # Open-source VLM
│   ├── 03_gpt4v.ipynb                 # GPT-4 Vision
│   ├── 04_image_captioning.ipynb      # Generate descriptions
│   ├── 05_visual_qa.ipynb             # Answer image questions
│   └── 06_zero_shot_classification.ipynb
├── image-generation/
│   ├── 01_stable_diffusion_basics.ipynb
│   ├── 02_prompt_engineering.ipynb    # Image prompts
│   ├── 03_controlnet.ipynb            # Guided generation
│   ├── 04_lora_training.ipynb         # Custom styles
│   ├── 05_dalle3_api.ipynb            # OpenAI API
│   └── 06_image_editing.ipynb         # Inpainting, etc.
├── audio/
│   ├── 01_whisper_speech_to_text.ipynb
│   ├── 02_text_to_speech.ipynb
│   ├── 03_audio_classification.ipynb
│   ├── 04_music_generation.ipynb
│   └── 05_voice_cloning.ipynb
├── video/
│   ├── 01_video_understanding.ipynb
│   ├── 02_action_recognition.ipynb
│   └── 03_video_captioning.ipynb
├── multimodal-rag/
│   ├── 01_image_text_search.ipynb
│   ├── 02_document_understanding.ipynb
│   ├── 03_multimodal_embeddings.ipynb
│   └── 04_cross_modal_retrieval.ipynb
└── projects/
    ├── image_analyzer.py              # Analyze and caption images
    ├── visual_chatbot.py              # Chat about images
    ├── audio_transcriber.py           # Full transcription system
    ├── image_generator.py             # Custom image generation
    └── multimodal_search.py           # Search images by text
```

---

## 🚀 Quick Start

### Example 1: CLIP - Zero-Shot Classification

```python
from transformers import CLIPProcessor, CLIPModel
from PIL import Image

# Load CLIP
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Load image
image = Image.open("photo.jpg")

# Define categories
labels = ["a cat", "a dog", "a bird", "a car"]

# Process
inputs = processor(
    text=labels,
    images=image,
    return_tensors="pt",
    padding=True
)

# Get similarities
outputs = model(**inputs)
logits_per_image = outputs.logits_per_image
probs = logits_per_image.softmax(dim=1)

# Results
for label, prob in zip(labels, probs[0]):
    print(f"{label}: {prob:.2%}")
```

### Example 2: GPT-4 Vision API

```python
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "What's in this image? Describe in detail."},
            {
                "type": "image_url",
                "image_url": {
                    "url": "https://example.com/image.jpg"
                }
            }
        ]
    }],
    max_tokens=300
)

print(response.choices[0].message.content)
```

### Example 3: Whisper - Speech to Text

```python
import whisper

# Load model (tiny, base, small, medium, large)
model = whisper.load_model("base")

# Transcribe
result = model.transcribe("audio.mp3")

print(result["text"])
# Also available: word-level timestamps, language detection
```

### Example 4: Stable Diffusion

```python
from diffusers import StableDiffusionPipeline
import torch

# Load model
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16
).to("cuda")

# Generate
prompt = "A beautiful sunset over mountains, oil painting style"
image = pipe(
    prompt,
    negative_prompt="blurry, low quality",
    num_inference_steps=30,
    guidance_scale=7.5
).images[0]

image.save("output.png")
```

---

## 📋 Learning Path

### Week 1: Vision-Language Basics

- [ ] Complete `00_START_HERE.ipynb`
- [ ] CLIP fundamentals in `vision-language/01_clip_basics.ipynb`
- [ ] Try GPT-4V in `vision-language/03_gpt4v.ipynb`
- [ ] **Project:** Build image classifier

### Week 2: Image Generation

- [ ] Stable Diffusion in `image-generation/01_stable_diffusion_basics.ipynb`
- [ ] Prompt engineering in `image-generation/02_prompt_engineering.ipynb`
- [ ] ControlNet in `image-generation/03_controlnet.ipynb`
- [ ] **Project:** Custom image generator

### Week 3: Audio & Video

- [ ] Whisper in `audio/01_whisper_speech_to_text.ipynb`
- [ ] TTS in `audio/02_text_to_speech.ipynb`
- [ ] Video understanding in `video/`
- [ ] **Project:** Audio transcription system

### Week 4: Multimodal RAG

- [ ] Image+text search in `multimodal-rag/01_image_text_search.ipynb`
- [ ] Document understanding in `multimodal-rag/02_document_understanding.ipynb`
- [ ] Build complete system
- [ ] **Capstone:** Multimodal search engine

---

## 🛠️ Technologies You'll Use

**Vision-Language Models:**
- CLIP (OpenAI)
- LLaVA (open-source)
- GPT-4V (OpenAI)
- Gemini Pro Vision (Google)
- BLIP-2, InstructBLIP

**Image Generation:**
- Stable Diffusion (open-source)
- DALL-E 3 (OpenAI)
- Midjourney (via API)
- ControlNet, T2I-Adapter
- IP-Adapter

**Audio Models:**
- Whisper (OpenAI)
- Bark (Suno AI)
- XTTS (Coqui)
- MusicGen (Meta)
- AudioCraft

**Frameworks:**
- Hugging Face Transformers
- Diffusers
- OpenCV
- torchaudio
- librosa

---

## 📊 Key Concepts

### CLIP Architecture

```
Image → Vision Transformer → Image Embedding
Text → Text Transformer → Text Embedding

Training: Maximize similarity of matching pairs,
          minimize similarity of non-matching pairs
```

**Applications:**
- Zero-shot classification
- Image search by text
- Content moderation
- Feature extraction

### Stable Diffusion Pipeline

```
Text → CLIP → Text Embedding
         ↓
    U-Net (denoising)
         ↓
    VAE Decoder → Image
```

**Key Parameters:**
- `num_inference_steps`: Quality vs speed (20-50)
- `guidance_scale`: Prompt adherence (7-15)
- `negative_prompt`: What to avoid
- `seed`: Reproducibility

### Multimodal Embeddings

```python
# Same embedding space for text and images!
text_embedding = clip.encode_text("a red car")
image_embedding = clip.encode_image(car_image)

# Compute similarity
similarity = cosine_similarity(text_embedding, image_embedding)
```

---

## 🎯 Projects

### 1. Visual Chatbot

Chat with images using GPT-4V or LLaVA.

**Skills:** VLM integration, conversation memory

### 2. Image Generator App

Stable Diffusion with custom UI and parameters.

**Skills:** Diffusion models, prompt engineering, UI

### 3. Meeting Transcriber

Record, transcribe, summarize with Whisper + LLM.

**Skills:** Audio processing, LLM integration

### 4. Visual Search Engine

Search image library by text description.

**Skills:** CLIP embeddings, vector search, multimodal RAG

### 5. Document QA System

Answer questions about PDFs with images/charts.

**Skills:** OCR, vision models, RAG

---

## 💡 Best Practices

### Vision-Language

**DO ✅**
- Use specific, detailed prompts
- Provide image context
- Chain vision → reasoning → action
- Handle image quality issues
- Validate outputs

**DON'T ❌**
- Assume perfect OCR
- Ignore image resolution
- Skip error handling
- Trust all outputs blindly

### Image Generation

**DO ✅**
- Use negative prompts
- Iterate on prompts
- Control with ControlNet
- Use appropriate steps (30-50)
- Set random seed for consistency

**DON'T ❌**
- Use default prompts only
- Expect perfection first try
- Ignore quality settings
- Generate at max resolution always (slow!)

### Audio Processing

**DO ✅**
- Preprocess audio (denoise)
- Use appropriate model size
- Check language detection
- Validate transcriptions
- Handle silence/noise

**DON'T ❌**
- Process very long files without chunking
- Ignore audio quality
- Skip timestamp alignment

---

## 🔗 Resources

### Courses

- [Hugging Face Diffusion Models Course](https://huggingface.co/learn/diffusion-course/unit0/1)
- [DeepLearning.AI - Vision Transformers](https://www.deeplearning.ai/courses/)
- [Fast.ai - Stable Diffusion](https://www.fast.ai/)

### Papers

- [CLIP: Learning Transferable Visual Models](https://arxiv.org/abs/2103.00020)
- [Stable Diffusion](https://arxiv.org/abs/2112.10752)
- [LLaVA: Visual Instruction Tuning](https://arxiv.org/abs/2304.08485)
- [Whisper: Robust Speech Recognition](https://arxiv.org/abs/2212.04356)

### Tools & APIs

- [Hugging Face Diffusers](https://github.com/huggingface/diffusers)
- [AUTOMATIC1111 Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- [OpenAI Vision API](https://platform.openai.com/docs/guides/vision)

### Models

- [CLIP Models](https://github.com/openai/CLIP)
- [Stable Diffusion Models](https://huggingface.co/stabilityai)
- [Whisper Models](https://github.com/openai/whisper)
- [LLaVA Models](https://github.com/haotian-liu/LLaVA)

---

## ✅ Completion Checklist

Before moving forward, you should be able to:

- [ ] Use CLIP for zero-shot classification
- [ ] Build image captioning systems
- [ ] Generate images with Stable Diffusion
- [ ] Optimize image prompts
- [ ] Transcribe audio with Whisper
- [ ] Understand VLM architectures
- [ ] Build multimodal RAG systems
- [ ] Combine text and visual search
- [ ] Deploy multimodal applications
- [ ] Handle edge cases (quality, errors)

---

## 🎓 What's Next?

**Phase 9: AI Agents** →
- Agents with vision capabilities
- Tool use with multimodal inputs
- Autonomous systems

**Phase 11: LLM Fine-tuning** →
- Fine-tune vision-language models
- Custom image generation models
- Specialized multimodal systems

**Real-World Applications** →
- Accessibility tools
- Content moderation
- Visual search
- Creative tools

---

**Ready to go multimodal?** → Start with `00_START_HERE.ipynb`

**Questions?** → Check the projects/ folder for complete examples

**🎨 Remember: A picture is worth a thousand tokens!**
