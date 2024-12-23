"""
Instructions:
1. Ensure llama.cpp is installed and compiled on your system.
2. Use one of the quantized models already downloaded in your `models` directory.
3. This script uses the `llama-cpp-python` wrapper for Python. Install it with:
   pip install llama-cpp-python

4. Run the script:
   python test_llama_cpp.py

5. It will generate a C# function to compute the Fibonacci sequence using the specified model.
"""

import os
from llama_cpp import Llama

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(SCRIPT_DIR, "../../models/Llama3.2-3B-Instruct/consolidated.00.pth")

# Initialize the model
print("Loading the model...")
llm = Llama(model_path=MODEL_PATH)

# Define the prompt
PROMPT = """
You are a helpful assistant specialized in generating code. Write a C# function to calculate the Fibonacci sequence:
"""

# Generate response
print("Generating code...")
response = llm(
    PROMPT,
    max_tokens=150,  # Limit the number of tokens
    temperature=0.7,  # Adjust for creativity
    top_p=0.9
)

# Print the result
print("\nGenerated Code:")
print(response["choices"][0]["text"].strip())
