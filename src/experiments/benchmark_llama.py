import argparse
import time
from llama_cpp import Llama

def benchmark_llama(model_path, prompt):
    start_time = time.time()
    model = Llama(model_path=model_path)
    response = model(prompt)
    elapsed_time = time.time() - start_time
    try:
        text = response['choices'][0]['text']
        print(f"Response: {text}")
    except KeyError:
        print(f"Unexpected response format: {response}")
    
    print(f"Elapsed Time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser(description="Benchmark Llama Model")
    parser.add_argument("--model-path", required=True, help="Path to the Llama model file")
    parser.add_argument("--prompt", required=True, help="Prompt to pass to the model")
    args = parser.parse_args()

    # Run benchmark
    benchmark_llama(args.model_path, args.prompt)
