from imports import *

def FiltragemMedia(imagemCinza):
    linhasOri, colunasOri = imagemCinza.shape
    
    imagemFiltrada = np.zeros((linhasOri, colunasOri), dtype=np.float64)
    
    for linha in range(1, linhasOri-1):
        for coluna in range(1, colunasOri-1):
            soma = 0.0
            soma = imagemCinza[linha, coluna] + imagemCinza[linha, coluna - 1] + imagemCinza[linha, coluna + 1]
            soma += imagemCinza[linha - 1, coluna] + imagemCinza[linha - 1, coluna - 1] + imagemCinza[linha - 1, coluna + 1]
            soma += imagemCinza[linha + 1, coluna] + imagemCinza[linha + 1, coluna - 1] + imagemCinza[linha + 1, coluna + 1]
            
            imagemFiltrada[linha, coluna] = soma / 9.0
            
    return imagemFiltrada
