from transformers import AutoModelForCausalLM, AutoTokenizer

def test_model(model_path):
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForCausalLM.from_pretrained(model_path).cuda()
        print("Modelo cargado correctamente.")
        return tokenizer, model
    except Exception as e:
        print(f"Error al cargar el modelo: {e}")

if __name__ == "__main__":
    model_path = "models/Starcoder"
    test_model(model_path)
