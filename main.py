from imports import *
import redimensionamento
import rotulacao
import negativo
import rotação
    
def main():

    imagemLida = ski.io.imread("imagensOri/image6.jpg")
    imagemCinza = ski.color.rgb2gray(imagemLida)
    
    thresh = ski.filters.threshold_otsu(imagemCinza)
    imagemBinaria = imagemCinza > thresh
    
    imagemNegativa = negativo.NegativarImagem(imagemLida)
    imagemRotacionada = rotação.RotacionarImagem(imagemLida, angulo_graus=90)
    imagemBinariaReduzida = redimensionamento.ReducaoPorBilinear(imagemBinaria)
    imagemRotulada = rotulacao.Rotulacao(imagemBinariaReduzida)
    
    if os.path.exists("imagensGer"):
        shutil.rmtree("imagensGer")
    
    os.makedirs("imagensGer")
    SalvarNovaImagem(imagemCinza, "imagemCinza")
    SalvarNovaImagem(imagemBinaria, "imagemBinaria")
    SalvarNovaImagem(imagemNegativa, "imagemNegativa")
    SalvarNovaImagem(imagemRotacionada, "imagemRotacionada")
    SalvarNovaImagem(imagemBinariaReduzida, "imagemBinariaReduzida")
    SalvarNovaImagem(imagemRotulada, "imagemRotulada")

main()