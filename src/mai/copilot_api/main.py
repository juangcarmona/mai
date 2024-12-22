from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Initialize FastAPI
app = FastAPI(
    title="Copilot API",
    description="Code generation using the StarCoder model.",
    version="1.0.0",
)

# Load StarCoder model
print("Loading StarCoder model...")
tokenizer = AutoTokenizer.from_pretrained("bigcode/starcoder")
model = AutoModelForCausalLM.from_pretrained("bigcode/starcoder", torch_dtype=torch.float16).cuda()

# Request model
class CodeRequest(BaseModel):
    prompt: str
    max_length: int = 100

# Endpoint for code generation
@app.post("/generate_code/")
async def generate_code(request: CodeRequest):
    """
    Generates code based on the provided prompt.
    """
    inputs = tokenizer(request.prompt, return_tensors="pt").to("cuda")
    outputs = model.generate(inputs.input_ids, max_length=request.max_length)
    code = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"prompt": request.prompt, "generated_code": code}
