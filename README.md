# MAI

MAI - My Artificial Intelligence - Working on Ubuntu on WSL

## Original Idea

MAI was born from the need to simplify the setup of an AI-powered development environment tailored for WSL-based Linux systems on Windows workstations. After encountering multiple challenges while adapting existing scripts to my local environment, I decided to create a replicable and streamlined process for others facing similar setups.

This project draws significant inspiration from the efforts of Mitko Vasilev and his work on [ODA (On Device AI)](https://github.com/mitkox/oda). His dedication and vision have been invaluable as a starting point. However, after facing various hurdles and adapting ODA to meet the specific requirements of my environment, I realized the necessity to create a project with a distinct focus and tailored goals—thus, MAI was born.

MAI is designed to help developers quickly set up an instance of their own AI environment with minimal friction. MAI is designed to help developers quickly set up an instance of their own AI environment with minimal friction.

## Purpose

The primary purpose of MAI is to enable developers to:

1. Build a dedicated Ubuntu environment on WSL that integrates seamlessly with modern AI tools.
2. Automate the installation and configuration of essential components like Zsh, CUDA, and AI frameworks.
3. Provide a customizable platform that can evolve with advancements in AI and development needs.

MAI is not just about setup—it’s about empowerment. The ultimate vision is to free developers from reliance on tools like ChatGPT and GitHub Copilot by enabling them to create their own AI-based assistant and coding companion.

## Goals

1. **Create Independence:** Build a personal AI model capable of serving as an alternative to tools like ChatGPT for natural language assistance and reasoning.
2. **Code Smarter:** Develop a VSCode Copilot alternative integrated directly into the MAI environment.
3. **Empower Developers:** Provide scripts and steps that are easy to replicate, fostering a deeper understanding of the AI and development stack.
4. **Leverage Local Resources:** Optimize for environments with NVIDIA GPUs, ensuring that users can fully utilize their hardware for AI model training and inference.

## Dependencies Installed

To enable a seamless AI development experience, the following dependencies are installed as part of the MAI setup. These libraries and tools are critical for building, experimenting, and deploying AI models and applications effectively.

### Core Libraries
- **[PyTorch](https://pytorch.org/)**: An open-source machine learning library for deep learning. It is optimized for both research and production workflows.
- **[Transformers](https://huggingface.co/docs/transformers/)**: Provides access to state-of-the-art pre-trained models like Llama and GPT for tasks such as text generation, translation, and more.
- **[Datasets](https://huggingface.co/docs/datasets/)**: A fast, efficient library for managing large datasets, especially for NLP tasks.
- **[Hugging Face Hub](https://huggingface.co/)**: Allows seamless sharing and retrieval of pre-trained models.

### Tokenization and Preprocessing
- **[SentencePiece](https://github.com/google/sentencepiece)**: A text tokenizer and detokenizer for handling complex linguistic structures in NLP tasks.

### Optimization and GPU Support
- **[Accelerate](https://huggingface.co/docs/accelerate/)**: Enables efficient distributed training and inference for large models.
- **[Optimum](https://huggingface.co/docs/optimum/)**: Hardware-optimized tools for inference and training on various platforms, perfect for maximizing GPU usage.

### Model Execution
- **[Llama-Cpp-Python](https://github.com/ggerganov/llama.cpp)**: Allows execution of Llama models with optimized performance for lightweight systems.

### API and Deployment
- **[FastAPI](https://fastapi.tiangolo.com/)**: A modern web framework for building APIs quickly and efficiently.
- **[Uvicorn](https://www.uvicorn.org/)**: A lightning-fast ASGI server for deploying FastAPI applications.

### Advanced Development
- **[LangChain](https://www.langchain.com/)**: Provides building blocks for creating complex chains of reasoning with LLMs.
- **[OpenAI](https://platform.openai.com/docs/)**: Integration library for accessing OpenAI's GPT models.
- **[Autograd](https://github.com/HIPS/autograd)**: A Python package for automatic differentiation to enable custom training loops.

## Color Palette

I’ve chosen **Deep Teal (#1E5F74)** as the primary color for MAI. This color reflects sophistication, modernity, and a sense of intelligence and elegance. It embodies the forward-thinking vision of MAI.

Complementary accents include:
- **Golden Yellow (#FFC857):** For a vibrant and energetic contrast.
- **Soft Mint (#ADEFD1):** To represent approachability and technical clarity.
- **Dark Indigo (#002855):** Adding depth and professionalism.

---

MAI is more than a set of scripts; it’s a philosophy of independence and innovation. Let’s build something incredible together.

---

## Before You Start

To ensure a smooth start, follow these essential steps for setting up your development environment:

### Configure Git
1. Set your name and email for Git:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```
2. Verify the configuration:
   ```bash
   git config --global --list
   ```

### Generate and Add SSH Key
1. Generate a new SSH key:
   ```bash
   ssh-keygen -t ed25519 -C "your.email@example.com"
   ```
   - Save the key in the default location (`~/.ssh/id_ed25519`).
   - Use a passphrase for added security.

2. Start the SSH agent:
   ```bash
   eval "$(ssh-agent -s)"
   ```

3. Add the SSH key to the agent:
   ```bash
   ssh-add ~/.ssh/id_ed25519
   ```

4. Copy the SSH key to your clipboard:
   ```bash
   cat ~/.ssh/id_ed25519.pub | xclip -selection clipboard
   ```
   *(If `xclip` is not installed, you can manually copy the output of the command.)*

5. Add the SSH key to your GitHub account:
   - Go to [GitHub SSH Settings](https://github.com/settings/keys).
   - Click **New SSH Key**.
   - Paste your key and save.

6. Test the connection:
   ```bash
   ssh -T git@github.com
   ```

   You should see a success message.


---

MAI is more than a set of scripts; it’s a philosophy of independence and innovation. Let’s build something incredible together.

---
