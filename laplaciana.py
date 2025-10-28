from imports import *
from scipy import ndimage

def AplicarFiltroLaplaciano(imagem):
    kernel = np.array([[0, -1, 0],
                      [-1, 4, -1],
                      [0, -1, 0]], dtype=np.float32)
 
    imagemFiltrada = ndimage.convolve(imagem.astype(np.float32), kernel, mode='reflect')
    imagemFiltrada = imagemFiltrada + 128
    imagemFiltrada = np.clip(imagemFiltrada, 0, 255)
    
    return imagemFiltrada.astype(np.uint8)

def ConverterParaCinza(imagem):
    if len(imagem.shape) == 3:
        imagemCinza = np.dot(imagem[...,:3], [0.299, 0.587, 0.114])
        return imagemCinza.astype(np.uint8)
    return imagem

def ProcessarLaplaciana(caminhoImagem, salvarResultado=True):
    try:
        imagem = ski.io.imread(caminhoImagem)
        print(f"Imagem carregada: {imagem.shape}")
        
        if len(imagem.shape) == 3:
            imagemCinza = ConverterParaCinza(imagem)
            print("Imagem convertida para escala de cinza")
        else:
            imagemCinza = imagem
        
        imagemProcessada = AplicarFiltroLaplaciano(imagemCinza)
        nomeArquivo = "imagemLaplaciana"
        print("Filtro laplaciano aplicado")
        
        if salvarResultado:
            SalvarNovaImagem(imagemProcessada, nomeArquivo)
            print(f"Imagem processada salva como: imagensGer/{nomeArquivo}.png")
        
        return imagemProcessada
        
    except FileNotFoundError:
        print("Arquivo de imagem não encontrado. Verifique o caminho em imagensOri/")
        return None
    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")
        return None

if __name__ == "__main__":
    print("=== PROCESSAMENTO COM FILTRO LAPLACIANO ===\n")
    
    caminhoImagem = "imagensOri/Demiurgo.png"
    
    print("Aplicando Filtro Laplaciano:")
    ProcessarLaplaciana(caminhoImagem)
    
    print("\n=== PROCESSAMENTO CONCLUÍDO ===")