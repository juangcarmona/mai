import time
import argparse
from transformers import AutoModelForCausalLM, AutoTokenizer

def chat_with_transformer(model_name):
    print(f"Loading model: {model_name}...")
    start_time = time.time()
    device = "cpu" # "cuda" for GPU usage or "cpu" for CPU usage
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name).to(device)
    elapsed_load_time = time.time() - start_time
    print(f"Model loaded in {elapsed_load_time:.2f} seconds.\n")

    print("Chat with the model. Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            print("Exiting chat. Goodbye!")
            break
         # Handle "tc" command to send a predefined prompt
        if user_input.lower() == "tc":
            user_input = "# write a fibonacci function in python"
        try:
            start_time = time.time()
            inputs = tokenizer(user_input, return_tensors="pt").to(device)
            outputs = model.generate(
                        inputs.input_ids,
                        max_length=50,
                        temperature=0.7,
                        top_p=0.9,
                        do_sample=False,
                        attention_mask=inputs.attention_mask,
                        repetition_penalty=1.2,
                        num_return_sequences=1,
                        eos_token_id=tokenizer.eos_token_id,
                        pad_token_id=tokenizer.pad_token_id,
                    )
            response = tokenizer.decode(outputs[0], skip_special_tokens=True)
            elapsed_time = time.time() - start_time

            print(f"Llama: {response}")
            print(f"(Response generated in {elapsed_time:.2f} seconds)\n")
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Debugging details:")
            print(f"User input: {user_input}")
            print(f"Inputs object: {inputs if 'inputs' in locals() else 'N/A'}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Chat with a Hugging Face Transformer model")
    parser.add_argument("--model-name", required=True, help="The name of the Hugging Face model to use")
    args = parser.parse_args()

    chat_with_transformer(args.model_name)

# write a fibonacci function in python

