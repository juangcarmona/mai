import time
from mlx_lm import load, generate

def chat_with_mlx(model_name):
    print("Loading model...")
    model, tokenizer = load(model_name)
    print("Model loaded successfully!")

    # Persistent chat history
    history = []

    print("\nEnter your message below. Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            print("Exiting chat. Goodbye!")
            break

        # Prepare the input for the model
        if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template is not None:
            messages = [{"role": "user", "content": user_input}]
            prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        else:
            prompt = user_input

        # Generate the response
        start_time = time.time()
        print("Assistant: ", end="", flush=True)

        response = generate(model, tokenizer, prompt=prompt, verbose=True)
        elapsed_time = time.time() - start_time
        print(response)

        print(f"\n(Response generated in {elapsed_time:.2f} seconds)\n")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Chat with MLX Model")
    parser.add_argument("--model-name", required=True, help="Name of the MLX model to load")
    args = parser.parse_args()

    chat_with_mlx(args.model_name)
