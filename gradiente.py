from imports import *
from scipy import ndimage

def AplicarFiltroSobel(imagem):
    
    sobelX = np.array([[-1, 0, 1],
                       [-2, 0, 2],
                       [-1, 0, 1]], dtype=np.float32)
    
    sobelY = np.array([[-1, -2, -1],
                       [ 0,  0,  0],
                       [ 1,  2,  1]], dtype=np.float32)
    
    gradienteX = ndimage.convolve(imagem.astype(np.float32), sobelX, mode='reflect')
    gradienteY = ndimage.convolve(imagem.astype(np.float32), sobelY, mode='reflect')
    gradiente = np.sqrt(gradienteX**2 + gradienteY**2)
    
    gradiente = np.clip(gradiente, 0, 255)
    return gradiente.astype(np.uint8)

def ConverterParaCinza(imagem):
    if len(imagem.shape) == 3:
        imagemCinza = np.dot(imagem[...,:3], [0.299, 0.587, 0.114])
        return imagemCinza.astype(np.uint8)
    return imagem

def ProcessarGradiente(caminhoImagem, salvarResultado=True):
    
    try:
        imagem = ski.io.imread(caminhoImagem)
        print(f"Imagem carregada: {imagem.shape}")
        
        if len(imagem.shape) == 3:
            imagemCinza = ConverterParaCinza(imagem)
            print("Imagem convertida para escala de cinza")
        else:
            imagemCinza = imagem
        
        imagemProcessada = AplicarFiltroSobel(imagemCinza)
        nomeArquivo = "imagemGradiente_Sobel"
        print("Filtro Sobel aplicado (ambas direções)")
        
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
    print("=== PROCESSAMENTO COM FILTRO SOBEL ===\n")
    
    caminhoImagem = "imagensOri/Demiurgo.png"
    
    print("Aplicando Filtro Sobel (ambas direções):")
    ProcessarGradiente(caminhoImagem)
    
    print("\n=== PROCESSAMENTO CONCLUÍDO ===")
