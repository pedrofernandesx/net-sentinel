import sys
import os

# Adiciona a pasta src ao caminho do Python
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from scanner import scan_url
from report import print_report

def main():
    print("\n💀 NET SENTINEL v1.0 - Threat Intelligence CLI")
    target = input("Digite a URL para verificar: ").strip()
    
    if target:
        print(f"\n[*] Consultando VirusTotal...")
        stats = scan_url(target)
        print_report(target, stats)
    else:
        print("URL inválida.")

if __name__ == "__main__":
    main()