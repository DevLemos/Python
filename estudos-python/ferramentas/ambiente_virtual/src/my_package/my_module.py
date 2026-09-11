import os

# Instale o pacote: python-dotenv
from dotenv import load_dotenv

# Essa função DEVE ser carregada antes do import dos módulos
# que forem usar variáveis de ambiente
load_dotenv()


def soma(x: int, y: int) -> int:
    return x + y


def lendo_variaveis_ambiente() -> None:
    # Testando as variáveis de ambiente
    variavel_arquivo = os.getenv(
        "VARIAVEL_TESTE", "Variável de ambiente não encontrada."
    )
    print("Verifique dotenv:", variavel_arquivo)

    # Seguindo a programação normal
    meu_resultado = soma(1, 2)
    print(f"Resultado: {meu_resultado}")


if __name__ == "__main__":
    lendo_variaveis_ambiente()
