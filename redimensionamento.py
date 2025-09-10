from imports import *

def ReduçãoPorVizinho(imagemCinza):
    
    linhasOri, colunasOri = imagemCinza.shape
    
    linhas = linhasOri // 2
    colunas = colunasOri // 2
    
    imagemReduzidaViz = np.zeros((linhas, colunas), dtype=np.float64)

    iRed = 0
    for i in range(0, linhasOri, 2):  
        jRed = 0
        for j in range(0, colunasOri, 2):  
            if iRed < linhas and jRed < colunas:
                imagemReduzidaViz[iRed, jRed] = imagemCinza[i, j]
                jRed += 1
        iRed += 1

    return imagemReduzidaViz

def AmpliacaoPorVizinho(imagemCinza):
    
    linhasOri, colunasOri = imagemCinza.shape
    
    linhas = linhasOri * 2 - 1
    colunas = colunasOri * 2 - 1
    
    imagemAmpliadaViz = np.zeros((linhas, colunas), dtype=np.float64)
    
    iOri = 0
    for i in range(0, linhas, 2):
        jOri = 0
        for j in range(0, colunas, 2):
            imagemAmpliadaViz[i, j] = imagemCinza[iOri, jOri]
            
            if i + 1 < linhas and j + 1 < colunas:
                imagemAmpliadaViz[i + 1, j + 1] = imagemCinza[iOri, jOri]
            if i + 1 < linhas:
                imagemAmpliadaViz[i + 1, j] = imagemCinza[iOri, jOri]
            if j + 1 < colunas:
                imagemAmpliadaViz[i, j + 1] = imagemCinza[iOri, jOri]
            
            if i + 2 < linhas and j + 1 < colunas:
                imagemAmpliadaViz[i + 2, j + 1] = imagemCinza[iOri, jOri + 1]
            if i + 1 < linhas and j + 2 < colunas:
                imagemAmpliadaViz[i + 1, j + 2] = imagemCinza[iOri + 1, jOri]
            
            jOri += 1
        iOri += 1
        
    return imagemAmpliadaViz
    
def ReducaoPorBilinear(imagemCinza):
    linhasOri, colunasOri = imagemCinza.shape
    
    linhas = linhasOri // 2
    colunas = colunasOri // 2
    
    imagemReduzidaBilinear = np.zeros((linhas, colunas), dtype=np.float64)

    iRed = 0
    for i in range(0, linhasOri, 2):
        jRed = 0
        for j in range(0, colunasOri, 2):
            if iRed < linhas and jRed < colunas:
                soma = 0
                divisor = 0

                if i < linhasOri and j < colunasOri:
                    soma = imagemCinza[i, j]
                    divisor += 1 
                    
                if i + 1 < linhasOri:
                    soma += imagemCinza[i + 1, j] 
                    divisor += 1
                
                if j + 1 < colunasOri:
                    soma += imagemCinza[i, j + 1] 
                    divisor += 1
                    
                if i + 1 < linhasOri and j + 1 < colunasOri:
                    soma += imagemCinza[i + 1, j + 1]
                    divisor += 1
                    
                imagemReduzidaBilinear[iRed, jRed] = soma/divisor if divisor != 0 else 0
                
                jRed += 1
        iRed += 1
            

    return imagemReduzidaBilinear    

def AmpliacaoPorBilinear(imagemCinza):
    
    linhasOri, colunasOri = imagemCinza.shape
    
    linhas = linhasOri * 2 - 1
    colunas = colunasOri * 2 - 1

    imagemAmpliadaBilinear = np.zeros((linhas, colunas), dtype=np.float64)

    iOri = 0
    for i in range(0, linhas, 2):
        jOri = 0
        for j in range(0, colunas, 2):
            imagemAmpliadaBilinear[i, j] = imagemCinza[iOri, jOri]
            
            if i + 1 < linhas and j + 1 < colunas:
                imagemAmpliadaBilinear[i + 1, j + 1] = (imagemCinza[iOri, jOri] + imagemCinza[iOri + 1, jOri] + imagemCinza[iOri, jOri + 1] + imagemCinza[iOri + 1, jOri + 1]) / 4
            if i + 1 < linhas:
                imagemAmpliadaBilinear[i + 1, j] = (imagemCinza[iOri, jOri] + imagemCinza[iOri + 1, jOri]) / 2
            if j + 1 < colunas:
                imagemAmpliadaBilinear[i, j + 1] = (imagemCinza[iOri, jOri] + imagemCinza[iOri, jOri + 1]) / 2

            if i + 2 < linhas and j + 1 < colunas:
                imagemAmpliadaBilinear[i + 2, j + 1] = (imagemCinza[iOri, jOri + 1] + imagemCinza[iOri + 1, jOri + 1]) / 2
            if i + 1 < linhas and j + 2 < colunas:
                imagemAmpliadaBilinear[i + 1, j + 2] = (imagemCinza[iOri + 1, jOri] + imagemCinza[iOri + 1, jOri + 1]) / 2

            jOri += 1
        iOri += 1
    
    return imagemAmpliadaBilinear