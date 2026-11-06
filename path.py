
import requests
import os
from pathlib import Path
from urllib.parse import urlsplit
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import local

print("""escolha sua opção abaixo
============  =======
[1] reco path
[2] reco dns
============  ========
""")

opcao = input(": ")

BASE_DIR = Path(__file__).resolve().parent
caminho = BASE_DIR / "wordlist" / "common.txt"
caminho2 = BASE_DIR / "wordlist" / "dns-Jhaddix.txt"



palavras_usadas = set()
dados_thread = local()

def obter_sessao():
    if not hasattr(dados_thread, "sessao"):
        dados_thread.sessao = requests.Session()

    return dados_thread.sessao


def verificar_path(palavra):
    url = url_base + "/" + palavra.lstrip("/")

    try:
        res = obter_sessao().get(
            url,
            timeout=(3, 7),
            allow_redirects=False
        )

        status = res.status_code
        res.close()

        return url, status

    except requests.RequestException:
        return url, None


def verificar_dns(palavra):
    dominios = [
        f"{palavra}.{host_base}",
        f"{primeiro_rotulo}.{palavra}.{restante_dominio}"
    ]

    resultados = []

    for dominio in dict.fromkeys(dominios):
        url = f"{esquema}://{dominio}{porta}/"

        try:
            res = obter_sessao().get(
                url,
                timeout=(3, 7),
                allow_redirects=False
            )

            status = res.status_code
            res.close()

            resultados.append((url, status))

        except requests.RequestException:
            resultados.append((url, None))

    return resultados


if opcao == "1":

    print("Iniciando reconhecimento de paths...")
    os.system("clear")

    url_base = input("Digite a URL do alvo: ").strip().rstrip("/")

    palavras = []

    with open(caminho, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()

            if not linha or linha in palavras_usadas:
                continue

            palavras_usadas.add(linha)
            palavras.append(linha)

    print(f"\nPalavras carregadas: {len(palavras)}")
    print("Iniciando requisições...\n")

    encontrados = 0
    falhas = 0

    with ThreadPoolExecutor(max_workers=8) as executor:

        tarefas = [
            executor.submit(verificar_path, palavra)
            for palavra in palavras
        ]

        for tarefa in as_completed(tarefas):

            url, status = tarefa.result()

            if status in [200, 204, 301, 302, 307, 308, 401, 403, 405, 429]:
                print(f"[{status}] {url}")
                encontrados += 1

            elif status is None:
                falhas += 1

    print("\nReconhecimento finalizado!")
    print(f"Resultados encontrados: {encontrados}")
    print(f"Falhas de conexão: {falhas}")


elif opcao == "2":

    print("Iniciando reconhecimento de DNS...")
    os.system("clear")

    entrada = input("Digite o domínio base: ").strip()

    if "://" not in entrada:
        entrada = "https://" + entrada

    partes = urlsplit(entrada)

    host_base = partes.hostname
    esquema = partes.scheme
    porta = f":{partes.port}" if partes.port else ""

    if not host_base or len(host_base.split(".")) < 2:
        print("Domínio inválido!")
        exit()

    rotulos = host_base.split(".")
    primeiro_rotulo = rotulos[0]
    restante_dominio = ".".join(rotulos[1:])

    palavras = []

    with open(caminho2, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()

            if not linha or linha in palavras_usadas:
                continue

            palavras_usadas.add(linha)
            palavras.append(linha)

    print(f"\nPalavras carregadas: {len(palavras)}")
    print("Iniciando reconhecimento...\n")

    encontrados = 0
    falhas = 0

    with ThreadPoolExecutor(max_workers=8) as executor:

        tarefas = [
            executor.submit(verificar_dns, palavra)
            for palavra in palavras
        ]

        for tarefa in as_completed(tarefas):

            resultados = tarefa.result()

            for url, status in resultados:

                if status in [200, 204, 301, 302, 307, 308, 401, 403, 405]:
                    print(f"[{status}] {url}")
                    encontrados += 1

                elif status is None:
                    falhas += 1

    print("\nReconhecimento finalizado!")
    print(f"Resultados encontrados: {encontrados}")
    print(f"Falhas de conexão: {falhas}")
