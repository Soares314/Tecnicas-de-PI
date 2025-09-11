from imports import *

# ROTAÇÃO DE IMAGENS
# implementa rotação.
# calcula as novas dimensões da imagem para conter toda a rotação,
# depois mapeia cada pixel da nova imagem para sua posição original

def RotacionarImagem(imagem, angulo_graus):
    angulo_rad = np.radians(angulo_graus)
    altura_ori, largura_ori = imagem.shape[:2]
    centro_x = largura_ori // 2
    centro_y = altura_ori // 2
    
    cos_ang = abs(np.cos(angulo_rad))
    sin_ang = abs(np.sin(angulo_rad))
    nova_largura = int(largura_ori * cos_ang + altura_ori * sin_ang)
    nova_altura = int(altura_ori * cos_ang + largura_ori * sin_ang)
    novo_centro_x = nova_largura // 2
    novo_centro_y = nova_altura // 2
    
    if len(imagem.shape) == 3:
        imagem_rotacionada = np.zeros((nova_altura, nova_largura, imagem.shape[2]), dtype=imagem.dtype)
    else:
        imagem_rotacionada = np.zeros((nova_altura, nova_largura), dtype=imagem.dtype)
    
    cos_inv = np.cos(-angulo_rad)
    sin_inv = np.sin(-angulo_rad)
    
    for y in range(nova_altura):
        for x in range(nova_largura):
            x_temp = x - novo_centro_x
            y_temp = y - novo_centro_y
            x_ori = int(x_temp * cos_inv - y_temp * sin_inv + centro_x)
            y_ori = int(x_temp * sin_inv + y_temp * cos_inv + centro_y)
            
            if 0 <= x_ori < largura_ori and 0 <= y_ori < altura_ori:
                imagem_rotacionada[y, x] = imagem[y_ori, x_ori]
    
    return imagem_rotacionada

# PROCESSAMENTO E EXECUÇÃO
# Funções para carregar imagens, aplicar rotação e salvar resultados.
# Inclui exemplos de uso com diferentes ângulos de rotação.

def ProcessarRotacao(caminho_imagem, angulo_graus, salvar_resultado=True):
    imagem = ski.io.imread(caminho_imagem)
    resultado = RotacionarImagem(imagem, angulo_graus)
    
    if salvar_resultado:
        nome_arquivo = f"imagemRotacao_{angulo_graus}graus"
        SalvarNovaImagem(resultado, nome_arquivo)
        print(f"Imagem rotacionada salva como: imagensGer/{nome_arquivo}.png")
    
    return resultado

if __name__ == "__main__":
    try:
        print("=== Rotação de Imagem ===")
        
        print("Rotacionando 180 graus...")
        ProcessarRotacao("imagensOri/image.png", angulo_graus=180)
        
    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o caminho em imagensOri/")
    except Exception as e:
        print(f"Erro: {e}")