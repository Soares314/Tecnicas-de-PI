import skimage as ski
import shutil, os
import matplotlib.pyplot as plt
import numpy as np
import random

def SalvarNovaImagem(imagem, nomeImagem):
    
    if imagem.dtype == np.float64:
        imagem = (imagem * 255).astype(np.uint8)
    elif imagem.dtype == bool:
        imagem = ski.img_as_ubyte(imagem)
    
    ski.io.imsave(f"imagensGer/{nomeImagem}.png", imagem)