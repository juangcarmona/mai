
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

## Key Components

MAI integrates several components to provide a modular and efficient development experience. Some of the server-side functionalities have been adapted from existing projects, with proper attribution to their original authors.

### Adapted Components

1. **Endpoint Server**:
   - Source: [huggingface-vscode-endpoint-server](https://github.com/LucienShui/huggingface-vscode-endpoint-server)
   - The server provides an endpoint to handle requests from the VSCode extension. The original implementation was adapted and integrated into MAI for better customization and performance.

### Structure

The current structure of MAI reflects these integrations:

```plaintext
mai/
├── README.md              
├── huggingface/             # Models and Hugging Face cache.
│   ├── hub/                 # Cache of downloaded models.
│   └── config/              # HF_HOME environment setup.
├── scripts/                 # Scripts for setup and maintenance.
│   ├── configure_environment.sh
│   ├── install_server.sh
│   ├── install_extension.sh
│   └── update_components.sh
├── src/
│   ├── copilot_api/         # Copilot API.
│   │   ├── main.py
│   │   ├── README.md
│   │   └── ...
│   ├── core/                
│   ├── crosscutting/         
│   ├── generators/          # Multiple ready-to-use source code generators.      
│   ├── models/
│   └── utils/               # Utility scripts.
│       ├── check_gpu.py
│       ├── convert_pth_to_gguf.py
│       └── ...
.mai/                        # Local directory for runtime and tools.
├── venv/                    # Python virtual environment.
└── llama.cpp/               # Source code and builds for llama.cpp.
```

## Dependencies Installed

To enable a seamless AI development experience, the following dependencies are installed as part of the MAI setup. These libraries and tools are critical for building, experimenting, and deploying AI models and applications effectively.

### Core Libraries
- **[PyTorch](https://pytorch.org/)**: An open-source machine learning library for deep learning. It is optimized for both research and production workflows.
- **[Transformers](https://huggingface.co/docs/transformers/)**: Provides access to state-of-the-art pre-trained models like Llama and GPT for tasks such as text generation, translation, and more.
- **[Datasets](https://huggingface.co/docs/datasets/)**: A fast, efficient library for managing large datasets, especially for NLP tasks.
- **[Hugging Face Hub](https://huggingface.co/)**: Allows seamless sharing and retrieval of pre-trained models.

## New Additions

The integration of adapted server components enhances MAI with:

1. **Seamless Local Hosting**: Adapted servers allow self-hosting for cost-effective development.
2. **Modular and Scalable Design**: MAI can evolve by adding or updating components as needed.

## System Utilities

During the setup, the following utilities are installed to enhance system usability and streamline your workflow:

- **tree**: Visualize directory structures in a tree format. Essential for navigating complex directories.
- **htop**: Interactive system resource monitor to view and manage system processes.
- **curl**: Command-line tool to transfer data from or to a server. Widely used for API requests and downloads.
- **wget**: A non-interactive network downloader for files from the web.
- **unzip**: Utility to extract ZIP files directly from the terminal.
- **git**: Industry-standard version control system for managing source code.
- **jq**: Lightweight and flexible command-line JSON processor.
- **neofetch**: Display system information (OS, kernel, uptime, etc.) in a visually appealing format.

These utilities are installed as part of the script `install_utilities.sh` to ensure a productive development environment.

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
