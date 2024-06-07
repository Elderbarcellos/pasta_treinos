import cv2
import os

# Dicionário para armazenar os dados dos usuários
usuarios = {}

# Função para cadastrar um novo usuário
def cadastrar_usuario(login, senha, caminho_imagem):
    usuarios[login] = {'senha': senha, 'caminho_imagem': caminho_imagem}

# Função para capturar e salvar a imagem do rosto
def capturar_imagem_rosto(login):
    # Inicializa a webcam
    cap = cv2.VideoCapture(0)
    
    # Captura a imagem
    ret, frame = cap.read()
    
    # Verifica se a captura foi bem-sucedida
    if ret:
        # Define o diretório para salvar a imagem do rosto
        pasta_destino = "imagens_rostos"
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)
        caminho_imagem = os.path.join(pasta_destino, f"{login}.png")
        
        # Salva a imagem
        cv2.imwrite(caminho_imagem, frame)
        print("Imagem do rosto capturada e salva com sucesso para o usuário:", login)
        return caminho_imagem
    else:
        print("Erro ao capturar imagem do rosto!")
        return None

# Função para cadastrar um novo usuário
def cadastrar_novo_usuario():
    login = input("Digite o login do novo usuário: ")
    senha = input("Digite a senha do novo usuário: ")
    
    caminho_imagem = capturar_imagem_rosto(login)
    if caminho_imagem:
        cadastrar_usuario(login, senha, caminho_imagem)

# Função para iniciar a aplicação de webcam e detectar rosto
def iniciar_aplicacao():
    # Inicializa a webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Captura a imagem
        ret, frame = cap.read()

        # Detecta rostos na imagem
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # Desenha retângulos ao redor dos rostos detectados
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Exibe a imagem com os rostos detectados
        cv2.imshow('Detectando Rostos', frame)

        # Verifica se a tecla 'q' foi pressionada para sair
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Verifica se a tecla Enter foi pressionada para fechar a câmera
        if cv2.waitKey(1) == 27:  # 27 ou 13 para esc ou tecla enter
            cap.release()
            cv2.destroyAllWindows()
            return

    # Libera a webcam
    cap.release()
    cv2.destroyAllWindows()

# Função principal
def main():
    while True:
        print("\nMenu:")
        print("1. Cadastrar um novo usuário")
        print("2. Iniciar a aplicação de detecção de rostos")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastrar_novo_usuario()
        elif escolha == "2":
            iniciar_aplicacao()
        elif escolha == "3":
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
