import time
import argparse
from transformers import AutoModelForCausalLM, AutoTokenizer

def chat_with_transformer(model_name):
    print(f"Loading model: {model_name}...")
    start_time = time.time()
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    elapsed_load_time = time.time() - start_time
    print(f"Model loaded in {elapsed_load_time:.2f} seconds.\n")

    print("Chat with the model. Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            print("Exiting chat. Goodbye!")
            break

        start_time = time.time()
        inputs = tokenizer(user_input, return_tensors="pt")
        outputs = model.generate(**inputs, max_length=50)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        elapsed_time = time.time() - start_time

        print(f"Llama: {response}")
        print(f"(Response generated in {elapsed_time:.2f} seconds)\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Chat with a Hugging Face Transformer model")
    parser.add_argument("--model-name", required=True, help="The name of the Hugging Face model to use")
    args = parser.parse_args()

    chat_with_transformer(args.model_name)
