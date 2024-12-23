import time
from transformers import AutoModelForCausalLM, AutoTokenizer

def benchmark_transformer(model_name, prompt):
    start_time = time.time()
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=50)
    elapsed_time = time.time() - start_time
    print(f"Response: {tokenizer.decode(outputs[0])}")
    print(f"Elapsed Time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    model_name = "gpt2"  # Replace with your desired Hugging Face model
    prompt = "What is the capital of France?"
    benchmark_transformer(model_name, prompt)
