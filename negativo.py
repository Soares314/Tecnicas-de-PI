from imports import *

# INVERSÃO DE PIXELS (NEGATIVO)
# Aplica transformação de negativo invertendo valores dos pixels.
# Para imagens float (0-1): subtrai de 1.0
# Para imagens int (0-255): subtrai de 255

def NegativarImagemCinza(imagemCinza):
    if imagemCinza.dtype == np.float64:
        imagemNegativa = 1.0 - imagemCinza
    else:
        imagemNegativa = 255 - imagemCinza
    
    return imagemNegativa

def NegativarImagem(imagemColorida):
    if imagemColorida.dtype == np.float64:
        imagemNegativa = 1.0 - imagemColorida
    else:
        imagemNegativa = 255 - imagemColorida
    
    return imagemNegativa

# PROCESSAMENTO E EXECUÇÃO
# Carrega imagem, detecta tipo (colorida/cinza), aplica negativo e salva resultado.

def ProcessarNegativo(caminhoImagem, salvarResultado=True):
    imagem = ski.io.imread(caminhoImagem)
    
    if len(imagem.shape) == 3:
        imagemNegativa = NegativarImagem(imagem)
        nomeArquivo = "imagemNegativaColorida"
    else:
        imagemNegativa = NegativarImagem(imagem)
        nomeArquivo = "imagemNegativaCinza"
    
    if salvarResultado:
        SalvarNovaImagem(imagemNegativa, nomeArquivo)
        print(f"Imagem negativa salva como: imagensGer/{nomeArquivo}.png")
    
    return imagemNegativa
if __name__ == "__main__":
    try:
        imagemNegativa = ProcessarNegativo("imagensOri/Demiurgo.png")
        
    except FileNotFoundError:
        print("Arquivo de imagem não encontrado. Verifique o caminho em imagensOri/")
    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")