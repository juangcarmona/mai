import time
import argparse
from llama_cpp import Llama

def chat_with_llama(model_path=None, repo_id=None, filename=None):
    print("Loading model...")
    if repo_id and filename:
        # Load model from Hugging Face
        model = Llama.from_pretrained(repo_id=repo_id, filename=filename)
    elif model_path:
        # Load local model
        model = Llama(model_path=model_path)
    else:
        raise ValueError("You must specify either --model-path or both --repo-id and --filename.")
    
    print("Model loaded successfully!")

    # Persistent context
    history = []

    print("\nEnter your message below. Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            print("Exiting chat. Goodbye!")
            break

        # Add the user's message to the history
        history.append(f"User: {user_input}")

        # Construct the prompt with the history
        prompt = "\n".join(history) + "\nAssistant:"

        # Generate the response
        start_time = time.time()
        print("Llama: ", end="", flush=True)

        response = model(
            prompt,
            max_tokens=128,  # Limit response length
            temperature=0.7,  # Control creativity
            stop=["User:"],  # Stop generation at user input
            stream=True      # Stream tokens
        )

        assistant_response = ""
        for token in response:
            if "choices" in token and "text" in token["choices"][0]:
                token_text = token["choices"][0]["text"]
                print(token_text, end="", flush=True)
                assistant_response += token_text

        # Update history with the assistant's response
        history.append(f"Assistant: {assistant_response.strip()}")

        elapsed_time = time.time() - start_time
        print(f"\n(Response generated in {elapsed_time:.2f} seconds)\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Chat with Llama Model")
    parser.add_argument("--model-path", help="Path to the local Llama model file")
    parser.add_argument("--repo-id", help="Hugging Face repo ID for the model")
    parser.add_argument("--filename", help="Filename of the model file in Hugging Face repo")
    args = parser.parse_args()

    chat_with_llama(model_path=args.model_path, repo_id=args.repo_id, filename=args.filename)
