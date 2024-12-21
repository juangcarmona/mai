# Models Directory

This directory is intended to store your machine learning models.

## Download Models
You can download compatible models for `llama-cpp-python` and other frameworks from trusted sources like:
- [Hugging Face](https://huggingface.co)
- [Meta AI Research](https://ai.facebook.com/tools/llama/)
- [Unsloth AI](https://github.com/unslothai/unsloth) (finetuning and optimized models)

## Instructions for Using Hugging Face Models

To use models from Hugging Face with `llama.cpp`, you need to:

1. **Create a Hugging Face Account**:  
   - Sign up or log in at [Hugging Face](https://huggingface.co/join).  
   - Generate an access token from [your profile](https://huggingface.co/settings/tokens) and store it locally. Use this token when downloading models.

2. **Model Compatibility**:  
   - Models may need conversion to formats like `GGUF` to work with `llama.cpp`. Ensure you follow the appropriate steps for compatibility.

3. **Download Models**:  
   - Use the Hugging Face CLI to download models. See [bloquedecodigo1] for an example of downloading a Llama model.

   i.e.:
```bash
    cd models
    huggingface-cli download meta-llama/Llama-3.2-1B \
        --repository-type model \
        -p models/Llama-3.2-1B --include-siblings
```

    i.e. 2:
 ```bash
    huggingface-cli download Qwen/Qwen2.5-Coder-7B-Instruct-GGUF --include "qwen2.5-coder-7b-instruct-q5_k_m*.gguf" --local-dir . --local-dir-use-symlinks False
 ```
4. **Convert Models**:  
   - If required, convert models to `GGUF` format using tools provided in the `llama.cpp` repository. Refer to [bloquedecodigo2] for a conversion example.

   i.e.:
```bash
    python convert.py \
        --input-dir models/Llama-3.2-1B \
        --output-dir models/Llama-3.2-1B.gguf
```

5. **Run Models**:  
   - After setup, you can run models interactively. Refer to [bloquedecodigo3] for usage instructions.

```bash
    llama-cli -m models/Llama-3.2-1B.gguf --interactive --color
```


### Recommended Models
Here are some popular models you might consider:

#### **Llama 3.2 (3B)**
- **Performance**: 2x faster than Llama 2 with 60% less memory usage.
- **Features**: Excellent for general-purpose AI tasks.
- **Download**: [Start for Free](https://github.com/unslothai/unsloth)

#### **Llama 3.1 (8B)**
- **Performance**: Similar to Llama 3.2, supports larger datasets.
- **Features**: Optimal for more complex tasks requiring higher precision.
- **Download**: [Start for Free](https://github.com/unslothai/unsloth)

#### **Qwen 2.5 (7B)**
- **Performance**: 2x faster and uses 63% less memory.
- **Features**: Focused on efficiency and accuracy for conversational AI.
- **Download**: [Start for Free](https://github.com/unslothai/unsloth)

#### **Mistral v0.3 (7B)**
- **Performance**: 2.2x faster than previous versions, saving 73% memory.
- **Features**: Ideal for fine-tuning with resource constraints.
- **Download**: [Start for Free](https://github.com/unslothai/unsloth)

---

## Usage
Once you've downloaded the models, place them in this directory and reference their paths in your scripts or applications. Make sure this directory is included in your `.gitignore` to prevent accidentally pushing large files to the repository.

---

### Notes
These models are optimized for fine-tuning, low memory usage, and performance. Choose the one that best fits your use case, and consult the official documentation for further guidance.
