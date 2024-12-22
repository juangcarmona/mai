from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

from mai.crosscutting.logging import get_logger
from mai.core.constants import COPILOT_API_NAME

import debugpy
import os
import uvicorn

logger = get_logger(COPILOT_API_NAME)

# Initialize FastAPI
app = FastAPI(
    title="Copilot API",
    description="Code generation using the StarCoder model.",
    version="1.0.0",
)

# Load StarCoder model
logger.info("Loading StarCoder model...")
checkpoint = "bigcode/starcoder2-3b"
# device = "cuda" if torch.cuda.is_available() else "cpu"

# IN MY CASE, CPU is best  (my Graphic card is not too good)
device = "cpu"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)

# Configure tokenizer padding token
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# Request model
class CodeRequest(BaseModel):
    prompt: str
    max_length: int = 100
    fill_in_middle: bool = False  # Enable Fill-in-the-Middle (FIM)

# Endpoint for code generation
@app.post("/generate_code/")
async def generate_code(request: CodeRequest):
    """
    Generates code based on the provided prompt.
    Supports Fill-in-the-Middle (FIM) if enabled.
    """
    context = (
        "You are a code generation assistant. "
        "Your task is to assist in writing efficient and correct code snippets based on the user's input. "
        "Provide concise and accurate code suggestions.\n\n"
        "### Input:\n"
    )
    if request.fill_in_middle:
        logger.info("Using Fill-in-the-Middle (FIM) mode.")
        input_text = f"{context}### Task:\n<fim_prefix>{request.prompt}<fim_suffix><fim_middle>\n### Output:\n"
    else:
        logger.info("Using standard mode.")
        input_text = f"{context}### Task:\n{request.prompt}\n### Output:\n"

    # Tokenize the input
    inputs = tokenizer(
        input_text,
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=request.max_length
    ).to(model.device)

    # Generate output
    outputs = model.generate(
        inputs.input_ids,
        attention_mask=inputs.attention_mask,
        max_new_tokens=request.max_length,
        pad_token_id=tokenizer.pad_token_id,
        temperature=0.8,
        top_p=0.9,
        do_sample=True
    )

    # Decode and clean up the response
    generated_code = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Remove the context if included in the response
    if generated_code.startswith(context.strip()):
        generated_code = generated_code[len(context.strip()):].strip()

    return {"prompt": request.prompt, "generated_code": generated_code}



@app.get("/", include_in_schema=False, response_class=RedirectResponse)
async def redirect_to_swagger():    
    logger.info("Redirect to swagger...")
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    if os.getenv("DEBUG_MODE") == "true":
        debugpy.listen(("0.0.0.0", 5678))
        debugpy.wait_for_client()
    uvicorn.run(app, host="0.0.0.0", port=8000)
