from imports import *
import redimensionamento
    
def main():

    imagemLida = ski.io.imread("imagensOri/image2.avif")
    imagemCinza = ski.color.rgb2gray(imagemLida)
    
    thresh = ski.filters.threshold_otsu(imagemCinza)
    imagemBinaria = imagemCinza > thresh
        
    imagemReduzidaViz = redimensionamento.ReduçãoPorVizinho(imagemCinza)
    imagemAmpliadaViz = redimensionamento.AmpliacaoPorVizinho(imagemCinza)
    imagemReduzidaBilinear = redimensionamento.ReducaoPorBilinear(imagemCinza)
    imagemAmpliadaBilinear = redimensionamento.AmpliacaoPorBilinear(imagemCinza)
    
    if os.path.exists("imagensGer"):
        shutil.rmtree("imagensGer")
    
    os.makedirs("imagensGer")
    SalvarNovaImagem(imagemCinza, "imagemCinza")
    SalvarNovaImagem(imagemBinaria, "imagemBinaria")

main()