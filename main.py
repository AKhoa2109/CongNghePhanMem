import torch

print("Welcome the MyClip project.")
device = "cuda" if torch.cuda.is_available() else "cpu"
print('Use device: ',device)
    