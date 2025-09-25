from imports import *

rotulos = []

def Rotulacao(imagemBinaria):
    linhasOri, colunasOri = imagemBinaria.shape
    
    imagemRotulos = np.zeros((linhasOri, colunasOri, 3), dtype=np.uint8)
    
    rotulosEquivalentes = []
    contador_cor = 1 
    
    for linha in range(linhasOri):
        for coluna in range(colunasOri):
        
            if not imagemBinaria[linha][coluna]:
                continue
                
            if linha == 0 and coluna == 0:
                novoRotulo = GerarCor()
                contador_cor += 1
                rotulos.append(novoRotulo)
                imagemRotulos[linha][coluna] = novoRotulo
                continue
                
            if linha == 0:
                if coluna > 0 and imagemBinaria[linha][coluna - 1]:
                    imagemRotulos[linha][coluna] = imagemRotulos[linha][coluna - 1]
                else:
                    novoRotulo = GerarCor()
                    contador_cor += 1
                    rotulos.append(novoRotulo)
                    imagemRotulos[linha][coluna] = novoRotulo
                continue
                
            # Primeira coluna - só verificar vizinho superior
            if coluna == 0:
                if imagemBinaria[linha - 1][coluna]:
                    imagemRotulos[linha][coluna] = imagemRotulos[linha - 1][coluna]
                else:
                    novoRotulo = GerarCor()
                    contador_cor += 1
                    rotulos.append(novoRotulo)
                    imagemRotulos[linha][coluna] = novoRotulo
                continue
            
            # Caso geral - verificar ambos vizinhos
            s = imagemBinaria[linha - 1][coluna]
            r = imagemBinaria[linha][coluna - 1]
            
            if not s and not r:
                novoRotulo = GerarCor()
                contador_cor += 1
                rotulos.append(novoRotulo)
                imagemRotulos[linha][coluna] = novoRotulo
                
            elif s and not r:
                imagemRotulos[linha][coluna] = imagemRotulos[linha - 1][coluna]
                
            elif not s and r:
                imagemRotulos[linha][coluna] = imagemRotulos[linha][coluna - 1]
                
            elif s and r:
                rotulo_s = imagemRotulos[linha - 1][coluna]
                rotulo_r = imagemRotulos[linha][coluna - 1]
                
                if np.array_equal(rotulo_s, rotulo_r):
                    imagemRotulos[linha][coluna] = rotulo_s
                else:
                    imagemRotulos[linha][coluna] = rotulo_r
                    
                    equivalencia_encontrada = False
                    for equivalentes in rotulosEquivalentes:
                        tem_s = ArrayEstaEmLista(rotulo_s, equivalentes)
                        tem_r = ArrayEstaEmLista(rotulo_r, equivalentes)
                        
                        if tem_s or tem_r:
                            if not tem_s:
                                equivalentes.append(rotulo_s.copy())
                            if not tem_r:
                                equivalentes.append(rotulo_r.copy())
                            equivalencia_encontrada = True
                            break
                    
                    if not equivalencia_encontrada:
                        rotulosEquivalentes.append([rotulo_r.copy(), rotulo_s.copy()])

    
    # Correção de equivalências - usar sempre o primeiro da lista
    for linha in range(linhasOri):
        for coluna in range(colunasOri):
            pixel = imagemRotulos[linha][coluna]
            
            # Verificar se não é pixel de fundo (preto)
            if np.any(pixel > 0):
                for equivalentes in rotulosEquivalentes:
                    if ArrayEstaEmLista(pixel, equivalentes):
                        imagemRotulos[linha][coluna] = equivalentes[0]
                        break

    return imagemRotulos

def ArrayEstaEmLista(array, lista):
    """print(lista)"""
    for item in lista:
        if np.array_equal(array, item):
            return True
    return False

def GerarCor():
    rgbAleatorio = np.random.randint(1, 255, size=3)
    while ArrayEstaEmLista(rgbAleatorio, rotulos):
        rgbAleatorio = np.random.randint(1, 255, size=3)
        
    return np.array(rgbAleatorio, dtype=np.uint8)