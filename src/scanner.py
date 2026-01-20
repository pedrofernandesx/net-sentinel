import os
import requests
import base64
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("VT_API_KEY")
BASE_URL = "https://www.virustotal.com/api/v3/urls"

def scan_url(url):
    """
    Consulta a reputação de uma URL no VirusTotal.
    Retorna um dicionário com estatísticas ou erro.
    """
    if not API_KEY:
        return {"error": "API Key não encontrada no .env"}

    # 1. Codificar URL para Base64 (padrão VirusTotal sem padding)
    url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
    
    headers = {"x-apikey": API_KEY}
    
    # 2. Tenta pegar o relatório
    response = requests.get(f"{BASE_URL}/{url_id}", headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data['data']['attributes']['last_analysis_stats']
    elif response.status_code == 404:
        return {"error": "URL nunca analisada. Envie para scan primeiro."}
    else:
        return {"error": f"Erro na API: {response.status_code}"}