import os
import random
from datetime import datetime
from git import Repo

# --- CONFIGURAÇÕES ---
# Caminho para o seu repositório local (altere para o seu)
REPO_PATH = "C:/Users/gasometro/Documents/Projeto"

# Nome do arquivo que será alterado em cada commit
FILENAME_TO_MODIFY = "modulo_1_logica_de_programacao/zcommit.txt"

# --- LÓGICA DO SCRIPT ---

def make_commits():
    """
    Realiza um número aleatório de commits (entre 2 e 10) no repositório.
    """
    if not os.path.isdir(REPO_PATH):
        print(f"Erro: O diretório do repositório '{REPO_PATH}' não foi encontrado.")
        return

    try:
        # Abre o repositório
        repo = Repo(REPO_PATH)

        # Garante que o repositório remoto está configurado (geralmente 'origin')
        if not repo.remotes:
            print("Erro: Nenhum repositório remoto configurado.")
            return
        origin = repo.remotes.origin

        # Puxa as últimas alterações para evitar conflitos
        print("Puxando as últimas alterações do repositório...")
        origin.pull()
        print("Pull concluído.")

        # Define o número de commits a serem feitos hoje
        num_commits = random.randint(2, 10)
        print(f"Iniciando automação. Serão feitos {num_commits} commits hoje.")

        for i in range(num_commits):
            # Caminho completo do arquivo a ser modificado
            file_path = os.path.join(REPO_PATH, FILENAME_TO_MODIFY)

            # Adiciona uma nova linha ao arquivo com data e hora
            with open(file_path, "a+") as f:
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"Commit automatico #{i+1} de {num_commits} em: {now}\n")

            # Adiciona o arquivo ao 'staging'
            repo.git.add(file_path)

            # Cria a mensagem do commit
            commit_message = f"feat: adiciona log de atividade automática ({i+1}/{num_commits})"
            
            # Realiza o commit
            repo.index.commit(commit_message)
            print(f"Commit #{i+1} criado com sucesso: '{commit_message}'")

        # Envia todos os commits para o repositório remoto
        print("Enviando todos os commits para o GitHub...")
        origin.push()
        print("Todos os commits foram enviados com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro durante a execução: {e}")

if __name__ == "__main__":
    make_commits()
