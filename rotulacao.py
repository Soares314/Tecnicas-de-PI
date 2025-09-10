from imports import *

def Rotulacao(imagemBinaria):
    linhasOri, colunasOri = imagemBinaria.shape
    
    linhasRot = linhasOri // 2
    colunasRot = colunasOri // 2
    
    imagemRotulos = np.zeros((linhasRot, colunasRot), dtype=np.float64)
    
    for linha in imagemBinaria:
        for coluna in imagemBinaria[linha]:
            if(imagemBinaria[linha][coluna] == False):
                imagemRotulos[linha][coluna] = 0