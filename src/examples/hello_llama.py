import os

model_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../models/Llama3.2-3B-Instruct/consolidated.00.pth")
)

from llama_cpp import Llama
llm = Llama(model_path=model_path)

prompt = "Hello, world! What can you tell me about Llama models?"
response = llm(prompt)

print("Generated Response:")
print(response["choices"][0]["text"].strip())
