from llama_cpp import Llama

# Ruta al modelo (asegúrate de especificar la ubicación correcta del archivo del modelo)
model_path = "/path/to/your/ggml-model.bin"

# Inicializa Llama con el modelo
llm = Llama(model_path=model_path)

# Genera una respuesta para el prompt "Hello, world!"
response = llm("Hello, world!")

# Imprime la salida generada por el modelo
print("Generated Response:")
print(response["choices"][0]["text"].strip())
