# UFT - Universidade Federal do Tocantins
# Alunos: Thiago Soares Ribeiro Nunes de Carvalho e Vitor Leal

# Técnicas de PI

## Base do Projeto

A pasta **imagensOri** possui todas as imagens possíveis de se usar como entrada, caso o usuário queira processar uma imagem específica, ele pode carregar ela dentro desta pasta.
A **requirements.txt** possui todas as dependências necessárias para rodar o projeto. **imports** é o cabeçalho que toda a aplicação  do projeto vai ter que importar, carregando todas as bibliotecas e funções necessárias.
O projeto possui diferentes aplicações, cada uma sendo uma técnica de processamento de imagens diferente. A **main** é a aplicação que irá rodar todas as outras, carregando uma dada imagem de imagensOri, aplicando uma função de uma aplicação desejada nela e gerando uma imagem saída em **imagensGer**.

## Implementações

### Implementação 1 - Redimensionamento

Na aplicação **redimensionamento** está as implementações passadas para entregar data **28/08/2025**, nelas estão as funções de interpolação por vizinho mais próximo e interpolação bilinear, tanto para redução quanto para ampliação.

### Implementação 2 - Rotulação, Negativo, Rotação

Na aplicação **rotulacao** está a função de rotulação de uma imagem binária. Em **negativo** está a função que inverte as cores de uma imagem, tendo tanto para imagens cinzas quanto coloridas. Em **rotação** está a função que rotaciona uma imagem, dentro da main na chamada da função o usuário define em quantos graus ela será rotacionada, ajustando o parâmetro **angulo_graus**. Todas essas implementações foram passadas para a data **11/09/2025**. 