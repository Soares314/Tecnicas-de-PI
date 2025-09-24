from imports import *

class histograma:
    def __init__(self, imagem):
        self.quantidadeCadaPixel = {}
        for pixel in imagem.ravel():
            self.quantidadeCadaPixel[pixel] = self.quantidadeCadaPixel.get(pixel, 0) + 1

        self.corCadaPixel = sorted(self.quantidadeCadaPixel.keys())
        self.numeroPixels = imagem.size
        
    def probabilidadeCadaPixel(self):
        pr = {}
        
        for pixel in self.corCadaPixel:
            pr[pixel] = self.quantidadeCadaPixel[pixel]/self.numeroPixels
            
        return pr
    
    def equalizacaoCadaPixel(self):
        probabiliCadaPixel = self.probabilidadeCadaPixel()
        equalizadorCadaPixel = {}
        
        soma = 0.0
        
        max_pixel = 255
        
        for pixel in self.corCadaPixel:
            soma += probabiliCadaPixel[pixel]
            equalizadorCadaPixel[pixel] = round(max_pixel * soma)
            
        return equalizadorCadaPixel
        

def EqualizacaoDoHistograma(imagemCinza):
    linhasOri, colunasOri = imagemCinza.shape
    imagemEqualizada = np.zeros((linhasOri, colunasOri), dtype=np.uint8)
    histogramaImagem = histograma(imagemCinza)
    equalizacaoHistograma = histogramaImagem.equalizacaoCadaPixel()
    
    # Percorre cada pixel da imagem
    for linha in range(linhasOri):
        for coluna in range(colunasOri):
            pixel = imagemCinza[linha, coluna]
            imagemEqualizada[linha, coluna] = equalizacaoHistograma[pixel]
            
    return imagemEqualizada