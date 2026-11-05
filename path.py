import requests
import os
import time
import requests

print("""escolha sua opção abaixo
============  =======
[1]reco path
[2]reco dns
[3]path transversal
============  ========
""")
rs=input(": ")
caminho=("wordlist.txt")
url=[]

if rs == "1":
    print("iniciando reco de path ...")
    time.sleep(2)
    os.system("clear")
    print("digite a url do alvo")
    rs=input(": ")
    with open(caminho, "r", encoding="utf-8")as arquivo:
        for linha in arquivo:

            linha=linha.strip()
            nv_url=rs + linha

            url.append(nv_url)

            for resultado in url:
                res=requests.get(resultado)
                if res.status_code in [200, 403]:
                    print(resultado, res.status_code
            
)
                
    
