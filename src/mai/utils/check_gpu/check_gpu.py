import torch

def check_gpu():
    if torch.cuda.is_available():
        gpu_name = torch.cuda.get_device_name(0)
        print(f"GPU disponible: {gpu_name}")
    else:
        print("No hay GPU disponible en este sistema.")
