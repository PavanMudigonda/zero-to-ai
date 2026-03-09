# Career Roadmap — Zero to AI Job Ready

> **Goal**: Navigate the AI/ML job market, build a compelling portfolio, and land your target role.

---

## Table of Contents

- [Target Roles & What They Do](#target-roles--what-they-do)
- [Skills Matrix by Role](#skills-matrix-by-role)
- [Your 30-60-90 Day Plan](#your-30-60-90-day-plan)
- [Resume Strategy](#resume-strategy)
- [Portfolio That Gets Interviews](#portfolio-that-gets-interviews)
- [Where to Apply](#where-to-apply)
- [Networking](#networking)
- [Certifications Worth Getting](#certifications-worth-getting)

---

## Target Roles & What They Do

### 1. AI Engineer / LLM Engineer ($140k–$280k)

**What you do**: Build production AI applications using LLMs — RAG systems, agents, prompt pipelines, fine-tuned models.

**Day-to-day:**
- Design and build RAG pipelines over enterprise documents
- Implement AI agents with tool calling and multi-step reasoning
- Fine-tune models for domain-specific tasks
- Evaluate and optimize LLM outputs (latency, cost, quality)
- Deploy and monitor AI systems in production

**Must-have skills:**
- RAG systems (chunking, retrieval, reranking, evaluation)
- Prompt engineering (CoT, ReAct, structured outputs)
- LLM APIs (OpenAI, Anthropic, local models via Ollama)
- Vector databases (ChromaDB, Qdrant, pgvector)
- Python, FastAPI, Docker

**Nice-to-have:**
- LLM fine-tuning (LoRA/QLoRA)
- AI agents and MCP
- LangChain / LlamaIndex / LangGraph
- MLOps (MLflow, CI/CD)

**Learning track**: [Track A in MASTER_STUDY_GUIDE.md](MASTER_STUDY_GUIDE.md) (4–6 months)

---

### 2. ML Engineer ($130k–$250k)

**What you do**: Build, train, deploy, and maintain ML models at scale. Bridge between data science and engineering.

**Day-to-day:**
- Train and optimize ML/DL models
- Build data pipelines and feature stores
- Deploy models as APIs (FastAPI, gRPC)
- Monitor model performance and data drift
- Maintain ML infrastructure (MLflow, Kubernetes, Docker)

**Must-have skills:**
- PyTorch or TensorFlow
- scikit-learn for classical ML
- Model training and evaluation
- Docker, CI/CD, cloud deployment (AWS/GCP/Azure)
- SQL, Python, APIs

**Nice-to-have:**
- Distributed training
- MLOps platforms (MLflow, W&B, Kubeflow)
- Spark / big data processing
- LLM serving (vLLM, TGI)

**Learning track**: [Track B in MASTER_STUDY_GUIDE.md](MASTER_STUDY_GUIDE.md) (8–10 months)

---

### 3. Data Scientist ($110k–$200k)

**What you do**: Analyze data, build models, run experiments, and communicate insights to drive business decisions.

**Day-to-day:**
- Exploratory data analysis and visualization
- A/B testing and experiment design
- Build predictive models (classification, regression, forecasting)
- Present findings to stakeholders
- Collaborate with engineering on productionizing models

**Must-have skills:**
- Python (pandas, NumPy, scikit-learn)
- Statistics (hypothesis testing, confidence intervals, regression)
- SQL (advanced queries, window functions)
- Data visualization (matplotlib, seaborn, Plotly)
- Communication and storytelling with data

**Nice-to-have:**
- Causal inference methods
- Time series forecasting
- Deep learning basics
- LLM/GenAI literacy

**Learning track**: [Track C in MASTER_STUDY_GUIDE.md](MASTER_STUDY_GUIDE.md) (6–8 months)

---

### 4. MLOps / AI Platform Engineer ($130k–$230k)

**What you do**: Build and maintain the infrastructure that ML/AI teams use to develop, deploy, and monitor models.

**Must-have skills:**
- Docker, Kubernetes
- CI/CD pipelines (GitHub Actions, GitLab CI)
- Cloud platforms (AWS SageMaker, GCP Vertex AI, Azure ML)
- MLflow or W&B for experiment tracking
- Monitoring (Prometheus, Grafana, Evidently)
- Infrastructure as code (Terraform)

---

## Skills Matrix by Role

| Skill | AI Engineer | ML Engineer | Data Scientist | MLOps |
|-------|:-----------:|:-----------:|:--------------:|:-----:|
| Python | ✅ | ✅ | ✅ | ✅ |
| SQL | ⚪ | ✅ | ✅ | ⚪ |
| Statistics | ⚪ | ✅ | ✅ | ⚪ |
| scikit-learn | ⚪ | ✅ | ✅ | ⚪ |
| PyTorch | ⚪ | ✅ | ⚪ | ⚪ |
| LLM APIs | ✅ | ⚪ | ⚪ | ⚪ |
| RAG systems | ✅ | ⚪ | ⚪ | ⚪ |
| Prompt engineering | ✅ | ⚪ | ⚪ | ⚪ |
| Fine-tuning (LoRA) | ✅ | ✅ | ⚪ | ⚪ |
| AI agents | ✅ | ⚪ | ⚪ | ⚪ |
| Vector databases | ✅ | ⚪ | ⚪ | ⚪ |
| Docker | ✅ | ✅ | ⚪ | ✅ |
| CI/CD | ⚪ | ✅ | ⚪ | ✅ |
| Cloud (AWS/GCP) | ⚪ | ✅ | ⚪ | ✅ |
| MLflow / W&B | ⚪ | ✅ | ⚪ | ✅ |
| Kubernetes | ⚪ | ⚪ | ⚪ | ✅ |
| A/B testing | ⚪ | ⚪ | ✅ | ⚪ |
| Causal inference | ⚪ | ⚪ | ✅ | ⚪ |

✅ = Required | ⚪ = Nice to have or not needed

---

## Your 30-60-90 Day Plan

### Days 1–30: Foundation & First Project

**Week 1–2:**
- Complete Phase 0 (Glossary, model landscape)
- Set up development environment
- Choose your learning track (AI Engineer / ML Engineer / Data Scientist)

**Week 3–4:**
- Complete Phase 1 foundations (NumPy, pandas, scikit-learn basics)
- Start your first small project (e.g., Iris classification)
- Create GitHub account, set up profile README

**Milestone**: Can clean a dataset, train a model, and evaluate it.

### Days 31–60: Core Skills & Portfolio Start

**AI Engineer track:**
- Complete embeddings, vector databases, basic RAG
- Build Project 1: RAG chatbot over PDF documents
- Deploy on HuggingFace Spaces

**ML Engineer track:**
- Complete mathematics, neural networks, PyTorch
- Build Project 1: End-to-end ML pipeline with MLflow
- Containerize with Docker

**Data Scientist track:**
- Complete statistics, causal inference basics
- Build Project 1: EDA + predictive model on a real dataset
- Write a blog post about your analysis

**Milestone**: First portfolio project live on GitHub with README.

### Days 61–90: Advanced Skills & Job Prep

**Week 9–10:**
- Complete advanced topics for your track
- Build Project 2 (see portfolio section below)
- Start interview prep with [INTERVIEW_PREP.md](INTERVIEW_PREP.md)

**Week 11–12:**
- Polish portfolio (READMEs, demos, documentation)
- Update resume and LinkedIn
- Start applying to jobs
- Practice mock interviews

**Milestone**: 2+ projects deployed, resume updated, applications sent.

---

## Resume Strategy

### Format
- **1 page** (2 pages max for senior roles)
- **ATS-friendly** (no tables, columns, or complex formatting)
- PDF format

### Structure

```
[Name]
[Email] | [LinkedIn] | [GitHub] | [Portfolio/Blog]

SUMMARY
AI/ML engineer with hands-on experience building RAG systems, fine-tuning LLMs,
and deploying models in production. Built [X] projects using [key technologies].

SKILLS
Languages: Python, SQL, JavaScript
ML/AI: PyTorch, scikit-learn, LangChain, Hugging Face Transformers
LLM: RAG, fine-tuning (LoRA/QLoRA), prompt engineering, AI agents
Infrastructure: Docker, FastAPI, MLflow, AWS/GCP, GitHub Actions

PROJECTS
[Project Name] — [One-line description]
• Built [what] using [technologies] achieving [measurable result]
• Deployed to [platform] with [feature]
• GitHub: [link] | Demo: [link]

EXPERIENCE
[Standard reverse-chronological work experience]

EDUCATION
[Degree] — [University] — [Year]
Relevant Coursework: [if applicable]

CERTIFICATIONS (optional)
[Certification name] — [Issuer] — [Year]
```

### Key Tips
- **Quantify everything**: "Reduced latency by 40%" not "Improved performance"
- **Lead with projects** if you're career-switching (before work experience)
- **Tailor per application**: Match keywords from the job description
- **Include GitHub link** prominently — hiring managers will look at your code

---

## Portfolio That Gets Interviews

### Minimum Viable Portfolio (3 projects)

| Project | What It Shows | Technologies |
|---------|---------------|-------------|
| **RAG Chatbot** | You can build modern AI apps | LangChain, ChromaDB, OpenAI/Ollama, FastAPI |
| **Fine-tuned Model** | You understand model training | QLoRA, Hugging Face, evaluation metrics |
| **MLOps Pipeline** | You can ship to production | MLflow, Docker, GitHub Actions, FastAPI |

### What Makes a Good Project README

```markdown
# Project Title

## What it does (1-2 sentences)

## Architecture diagram (even a simple one)

## How to run it
- Prerequisites
- Installation steps
- Usage examples

## Key design decisions
- Why this embedding model?
- Why this chunking strategy?
- What tradeoffs did you make?

## Results / Evaluation
- Metrics (accuracy, latency, cost)
- Before/after comparison (for fine-tuning)

## What I learned

## Future improvements
```

### Where to Deploy (Free)
- **HuggingFace Spaces** — Best for Gradio/Streamlit demos
- **Render** — Good for FastAPI backends
- **Railway** — Easy Docker deployments
- **Vercel** — Frontend + API routes
- **GitHub Pages** — Static sites and documentation

---

## Where to Apply

### Job Boards (AI/ML Focused)

| Platform | Strengths |
|----------|-----------|
| [ai-jobs.net](https://ai-jobs.net) | AI/ML specific |
| [MLOps.jobs](https://mlops.jobs) | MLOps roles |
| [HuggingFace Jobs](https://huggingface.co/jobs) | AI-native companies |
| LinkedIn Jobs | Largest volume, good filters |
| Indeed | High volume |
| Wellfound (AngelList) | Startups |
| Levels.fyi | Compensation data + jobs |

### Company Types to Target

**Best for first AI role:**
1. **AI-native startups** — Smaller teams, broader responsibilities, faster learning
2. **Mid-size tech companies** — Dedicated ML teams, good mentorship
3. **Consulting firms** — Variety of projects, rapid skill building

**Harder for first role (but great long-term):**
4. **FAANG/Big Tech** — Competitive, but excellent resources and compensation
5. **Research labs** — Usually require PhD or publications

### Application Strategy
- Apply to 5–10 jobs per week
- Customize cover letter for top-choice companies
- Follow up after 1 week if no response
- Track applications in a spreadsheet

---

## Networking

### High-Impact Activities

1. **Contribute to open source** — Even small PRs (docs, tests) on popular repos (LangChain, Hugging Face)
2. **Write blog posts** — 1 post per project. Share on LinkedIn, Twitter/X, Reddit
3. **Engage on social media** — Comment thoughtfully on AI posts (LinkedIn, Twitter/X)
4. **Join communities** — HuggingFace Discord, r/MachineLearning, r/LocalLLaMA
5. **Attend meetups** — Local AI/ML meetups, virtual events

### Who to Connect With
- AI engineers at companies you want to work at
- Recruiters who specialize in AI/ML roles
- Open-source maintainers of tools you use
- Fellow learners (study groups, accountability partners)

---

## Certifications Worth Getting

Certifications are **not required** but can help signal commitment, especially for career switchers.

### Recommended (in priority order)

| Certification | Provider | Cost | Value |
|--------------|----------|------|-------|
| AWS Machine Learning Specialty | AWS | $300 | High — widely recognized |
| Google Professional ML Engineer | Google Cloud | $200 | High — cloud ML skills |
| DeepLearning.AI TensorFlow Developer | Coursera | $49/mo | Medium — good for beginners |
| Hugging Face NLP Course Certificate | Hugging Face | Free | Medium — shows HF ecosystem knowledge |
| Azure AI Engineer Associate | Microsoft | $165 | Medium — good for Azure shops |

### Skip These
- Generic "AI fundamentals" certificates from non-technical platforms
- Certificates that only require watching videos (no hands-on component)
- Paid certificates from unknown providers

---

## Interview Preparation

For detailed interview questions, coding problems, and system design walkthroughs, see:

→ **[INTERVIEW_PREP.md](INTERVIEW_PREP.md)**

### Quick Prep Checklist
- [ ] Practice 15 core ML concept questions (see INTERVIEW_PREP.md)
- [ ] Solve 20+ pandas/scikit-learn coding problems
- [ ] Walk through 3 ML system design scenarios
- [ ] Prepare your "tell me about yourself" story (60 seconds)
- [ ] Prepare to explain each portfolio project in depth
- [ ] Practice whiteboarding/coding on a shared screen

---

## Timeline Summary

| Week | Activity | Output |
|------|----------|--------|
| 1–4 | Foundations + first project | GitHub profile + Project 1 |
| 5–8 | Core track + second project | Project 2 deployed |
| 9–12 | Advanced topics + portfolio polish | 3 projects, resume ready |
| 13–16 | Interview prep + applications | Interviews scheduled |
| 17–20 | Interview + iterate | Offers |

---

## Key Resources

| Need | Go To |
|------|-------|
| Learning plan | [MASTER_STUDY_GUIDE.md](MASTER_STUDY_GUIDE.md) |
| Progress tracking | [checklist.md](checklist.md) |
| Interview prep | [INTERVIEW_PREP.md](INTERVIEW_PREP.md) |
| Tool comparisons | [COMPARISON_MATRICES.md](COMPARISON_MATRICES.md) |
| Video courses & repos | [REFERENCES.md](REFERENCES.md) |

---

*Last Updated: March 2026*
*Repository: [zero-to-ai](https://github.com/PavanMudigonda/zero-to-ai)*