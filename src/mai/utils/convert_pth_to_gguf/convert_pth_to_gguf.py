import os
import subprocess
import argparse
from pathlib import Path


def convert_model(model_path: str, output_dir: str):
    """
    Converts a Hugging Face model in .pth format to GGUF format for llama.cpp.

    Args:
        model_path (str): Path to the Hugging Face model directory (containing .pth files).
        output_dir (str): Directory to save the converted GGUF model.

    Raises:
        RuntimeError: If the conversion script fails.
    """
    # Ensure output directory exists
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Path to the llama.cpp conversion script
    conversion_script = Path("mai/scripts/convert-hf-to-gguf.py")

    if not conversion_script.exists():
        raise FileNotFoundError(
            f"Conversion script not found: {conversion_script}. "
            "Make sure llama.cpp is installed and the script is available."
        )

    # Run the conversion script
    command = [
        "python3",
        str(conversion_script),
        "--model-path",
        model_path,
        "--output",
        output_dir,
    ]

    print(f"Running command: {' '.join(command)}")
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        raise RuntimeError(
            f"Conversion failed with error:\n{result.stderr.decode('utf-8')}"
        )

    print(f"Model converted successfully. Saved to {output_dir}")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert .pth model to GGUF format.")
    parser.add_argument(
        "--model-path", type=str, required=True, help="Path to the Hugging Face model directory"
    )
    parser.add_argument(
        "--output-dir", type=str, required=True, help="Output directory for the GGUF model"
    )

    args = parser.parse_args()

    convert_model(args.model_path, args.output_dir)