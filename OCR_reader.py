# Importando as bibliotecas necessárias
import cv2
import pytesseract


# Solicitando ao usuário que insira o caminho da imagem
input_path = input("Por favor, insira o caminho da imagem: ")

# Carregando a imagem
imagem = cv2.imread(input_path)

# Verificando se a imagem foi carregada corretamente
if imagem is None:
    print(f"Não foi possível abrir a imagem {input_path}")
else:
    # Utilizando o Tesseract para extrair o texto da imagem
    texto = pytesseract.image_to_string(imagem, lang='por')

    # Imprimindo o texto extraído
    print(texto)

''' pip3 install

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/joaohenriquemelodesouza/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"

brew install tesseract

brew install tesseract-lang

pip3 install opencv-python

pip3 install pytesseract
'''
