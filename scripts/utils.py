import re

TITLE_OVERRIDES = {
    'ai': 'AI', 'ml': 'ML', 'llm': 'LLM', 'llms': 'LLMs', 'rag': 'RAG', 
    'mlops': 'MLOps', 'nlp': 'NLP', 'cv': 'CV', 'gan': 'GAN', 'vae': 'VAE',
    'api': 'API', 'apis': 'APIs', 'sdk': 'SDK', 'mcp': 'MCP', 'tts': 'TTS',
    'rl': 'RL', 'lora': 'LoRA', 'qlora': 'QLoRA', 'peft': 'PEFT', 
    'finetuning': 'Fine-tuning', 'redteaming': 'Red Teaming', 
    'langchain': 'LangChain', 'llamaindex': 'LlamaIndex', 'graphrag': 'GraphRAG',
    'hyde': 'HyDE', 'gpt': 'GPT', 'vscode': 'VS Code', 'pytorch': 'PyTorch',
    'tensorflow': 'TensorFlow', 'numpy': 'NumPy', 'pandas': 'Pandas',
    'huggingface': 'Hugging Face', 'openai': 'OpenAI', 'ide': 'IDE', 'ides': 'IDEs',
}

PHRASE_OVERRIDES = {
    'Debugging Troubleshooting': 'Debugging & Troubleshooting',
    'AI Safety Redteaming': 'AI Safety & Red Teaming',
    'AI Safety Red Teaming': 'AI Safety & Red Teaming',
    'AI Hardware LLM Validation': 'AI Hardware & LLM Validation',
    'Low Code AI Tools': 'Low-Code AI Tools',
    'Real Time Streaming': 'Real-Time Streaming',
    'Time Series Analysis': 'Time-Series Analysis',
    'AI Powered Dev Tools': 'AI-Powered Dev Tools',
}

def clean_title(name: str, strip_prefix: bool = False) -> str:
    """
    Cleans a filename string into a formatted title.
    If strip_prefix is True, removes leading 'XX-' numeric prefixes.
    Otherwise, leaves the numeric prefix.
    """
    if strip_prefix:
        name = re.sub(r'^\d+[_-]', '', name)
        
    words = name.replace('_', ' ').replace('-', ' ').split()
    cleaned_words = []
    
    for word in words:
        override = TITLE_OVERRIDES.get(word.lower())
        if override:
            cleaned_words.append(override)
        else:
            cleaned_words.append(word.capitalize())
            
    title = ' '.join(cleaned_words)
    title = title.replace('Specializations ', '')
    
    number_prefix_match = re.match(r'^(\d+)\s+(.*)$', title)
    if not number_prefix_match:
        return PHRASE_OVERRIDES.get(title, title)
        
    number_prefix, remainder = number_prefix_match.groups()
    return f"{number_prefix} {PHRASE_OVERRIDES.get(remainder, remainder)}"
