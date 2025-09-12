# Python-Practice

A basic learning repository to practice Python programming, Poetry package management, and various Python libraries including LangChain, FastAPI, and Hugging Face integrations.

## 🎯 Purpose

This repository is for learning and practicing:
- Python programming fundamentals
- Poetry for dependency management
- AI/ML libraries (LangChain, Hugging Face)
- Web frameworks (FastAPI)
- API integrations and chatbot development

## 📋 Prerequisites

- Python 3.13 or higher
- Poetry (for dependency management)

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/saivenkat346/Python-Practice.git
   cd Python-Practice
   ```

2. **Install dependencies:**
   ```bash
   poetry install
   ```

3. **Set up environment variables:**
   
   Create a `.env` file in the project root with your API keys:
   ```env
   # Add your API keys here
   OPENAI_API_KEY=your_openai_key_here
   HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here
   ```

## 🎮 Usage

### Run the Hugging Face Chatbot
```bash
poetry run python huggingFaceLLMModels.py
```

### Using Poetry Scripts
You can also use the configured script:
```bash
poetry run huggingface
```

## 📦 Dependencies

This project uses the following Python packages:

- **FastAPI** (>=0.116.1) - Modern web framework for APIs
- **Uvicorn** (>=0.35.0) - ASGI server for FastAPI
- **LangChain[all]** (>=0.3.27) - Framework for AI applications
- **OpenAI** (>=1.107.0) - OpenAI API client
- **LangChain-HuggingFace** (>=0.3.1) - Hugging Face integrations
- **LangChain-Community** (>=0.3.29) - Community integrations
- **Transformers** (>=4.56.1) - Hugging Face transformers library
- **Hugging Face Hub** (>=0.34.4) - Model hub client
- **Python-dotenv** (>=1.1.1) - Environment variable management

## 📁 Files

- `huggingFaceLLMModels.py` - Main chatbot script using Hugging Face models
- `firstPythonScript.py` - *(Ignore this file - personal practice script)*
- `pyproject.toml` - Poetry configuration and dependencies
- `README.md` - This file

## 🔧 Project Configuration

```toml
[project]
name = "practicerepository"
version = "0.1.0"
description = "this is just to practice python and practice poetry and other libraries"
requires-python = ">=3.13,<4.0"

[project.scripts]
huggingface = "huggingFaceLLMModels.console:run"
```

## 🤝 Getting API Keys

### Hugging Face Token
1. Go to [Hugging Face Settings](https://huggingface.co/settings/tokens)
2. Create a new token
3. Add it to your `.env` file

### OpenAI API Key (if using OpenAI models)
1. Go to [OpenAI API Keys](https://platform.openai.com/api-keys)
2. Create a new API key
3. Add it to your `.env` file

## 👨‍💻 Author

**Sai Venkat**
- Email: saisam346@gmail.com
- GitHub: [@saivenkat346](https://github.com/saivenkat346)

---

*This is a learning repository - feel free to explore, experiment, and break things!* 🚀
