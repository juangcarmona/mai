# Hugging Face Directory

This directory is intended to store Hugging Face models, datasets, and related resources.

## Download Models
You can download compatible models for `llama-cpp-python`, Hugging Face Transformers, and other frameworks from trusted sources like:
- [Hugging Face](https://huggingface.co)
- [Meta AI Research](https://ai.facebook.com/tools/llama/)
- [Unsloth AI](https://github.com/unslothai/unsloth) (fine-tuning and optimized models)

## Instructions for Using Hugging Face Models

To use models from Hugging Face with `llama.cpp` or Hugging Face Transformers, follow these steps:

1. **Create a Hugging Face Account**:  
   - Sign up or log in at [Hugging Face](https://huggingface.co/join).  
   - Generate an access token from [your profile](https://huggingface.co/settings/tokens) and store it locally. Use this token when downloading models.

2. **Model Compatibility**:  
   - Some models may need conversion to formats like `GGUF` to work with `llama.cpp`. Ensure you follow the appropriate steps for compatibility.

3. **Download Models**:  
   - Use the Hugging Face CLI to download models. See the examples below:

   Example 1:
   ```bash
   cd huggingface
   huggingface-cli download meta-llama/Llama-3.2-1B        --repository-type model        -p hub/models--meta-llama--Llama-3.2-1B --include-siblings
   ```

   Example 2:
   ```bash
   huggingface-cli download Qwen/Qwen2.5-Coder-7B-Instruct-GGUF --include "qwen2.5-coder-7b-instruct-q5_k_m*.gguf"        --local-dir hub/models--Qwen-Qwen2.5-Coder-7B-Instruct-GGUF        --local-dir-use-symlinks False
   ```

   - You can also use the experiments, setting the `--repo-id`and the `--filename` arguments in `launch.json`, so, `Llama.from_pretrained(repo_id=repo_id, filename=filename)` HF will download it for you. it will also work when using HF transformers, like, `model = AutoModelForCausalLM.from_pretrained(checkpoint)`.

   The idea is that you can always see what models you have available on your mai server adnd perform quick clean ups whenever necesary.

4. **Convert Models**:  
   - If required, convert models to `GGUF` format using tools provided in the `llama.cpp` repository. Example conversion:

   ```bash
   python convert.py  --input-dir hub/models--meta-llama--Llama-3.2-1B        --output-dir hub/models--meta-llama--Llama-3.2-1B-GGUF
   ```

   
   **NOTE**: convert.py does ot exists anymore, instead you can 
   ```bash
   pip install -r llama.cpp/requirements.txt
   ```

   And search and use the convertion script that best fits your case.   

5. **Run Models**:  
   - After setup, you can run models interactively. Example usage with `llama.cpp`:

   ```bash
   llama-cli -m hub/models--meta-llama--Llama-3.2-1B-GGUF --interactive --color
   ```
---

## Usage
Once you've downloaded the models, they will be stored in this directory under `hub/`. Reference their paths in your scripts or applications as needed. Make sure this directory is included in your `.gitignore` to prevent accidentally pushing large files to the repository.

---

### Notes
- These models are optimized for fine-tuning, low memory usage, and performance.
- Choose the one that best fits your use case, and consult the official documentation for further guidance.

---

### Sensitive Data
- The `token` and `stored_tokens` files store sensitive information and should not be shared. Ensure they are excluded from version control by using `.gitignore`.
