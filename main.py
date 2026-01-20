import os
import requests
import sys
from dotenv import load_dotenv
from colorama import Fore, Style, init

# Inicializa cores e carrega a chave secreta
init(autoreset=True)
load_dotenv()

API_KEY = os.getenv("VT_API_KEY")
BASE_URL = "https://www.virustotal.com/api/v3/urls"

def scan_url(url_to_scan):
    print(f"\n{Fore.CYAN}[*] Analisando: {url_to_scan} ... aguarde.")
    
    headers = {"x-apikey": API_KEY}
    
    # 1. Enviar URL para análise (POST)
    # Codificar URL para Base64 (Exigência do VirusTotal)
    import base64
    url_id = base64.urlsafe_b64encode(url_to_scan.encode()).decode().strip("=")
    
    # 2. Consultar o Relatório (GET)
    response = requests.get(f"{BASE_URL}/{url_id}", headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        stats = data['data']['attributes']['last_analysis_stats']
        
        malicious = stats['malicious']
        suspicious = stats['suspicious']
        clean = stats['harmless']
        
        print("\n" + "="*40)
        print(f"{Fore.YELLOW}🔍 RELATÓRIO DE AMEAÇA")
        print("="*40)
        
        if malicious > 0:
            print(f"{Fore.RED}🚨 PERIGO DETECTADO!")
            print(f"Detectado por {malicious} motores de segurança.")
        elif suspicious > 0:
            print(f"{Fore.YELLOW}⚠️ SUSPEITO.")
            print(f"Marcado como suspeito por {suspicious} motores.")
        else:
            print(f"{Fore.GREEN}✅ LIMPO.")
            print(f"Nenhuma ameaça encontrada ({clean} motores seguros).")
            
        print("="*40 + "\n")
    else:
        print(f"{Fore.RED}[!] Erro na consulta: {response.status_code}")
        # Dica: Se der 404, é pq a URL nunca foi escaneada antes.
        # Precisaríamos mandar escanear primeiro (POST), mas vamos testar com URLs conhecidas.

if __name__ == "__main__":
    print(f"{Fore.BLUE}🐟 PHISH-CATCHER v1.0")
    target = input("Digite a URL para verificar: ")
    scan_url(target)