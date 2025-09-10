import skimage as ski
import shutil, os
import matplotlib.pyplot as plt
import numpy as np

def SalvarNovaImagem(imagem, nomeImagem):
    
    if imagem.dtype == np.float64:
        imagem = (imagem * 255).astype(np.uint8)
    ski.io.imsave(f"imagensGer/{nomeImagem}.png", imagem)