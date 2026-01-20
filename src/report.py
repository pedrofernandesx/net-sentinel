from colorama import Fore, Style, init

init(autoreset=True)

def print_report(url, stats):
    """Gera um relatório visual colorido no terminal."""
    
    print("\n" + "="*50)
    print(f"{Fore.CYAN}🛡️  NET SENTINEL - RELATÓRIO DE AMEAÇA")
    print("="*50)
    print(f"Alvo: {url}\n")
    
    if "error" in stats:
        print(f"{Fore.RED}[!] {stats['error']}")
        return

    malicious = stats.get('malicious', 0)
    suspicious = stats.get('suspicious', 0)
    clean = stats.get('harmless', 0)
    
    if malicious > 0:
        print(f"{Fore.RED}🚨 PERIGO DETECTADO!")
        print(f"{Fore.RED}➤ {malicious} motores marcaram como MALICIOSO.")
    elif suspicious > 0:
        print(f"{Fore.YELLOW}⚠️  SUSPEITO.")
        print(f"{Fore.YELLOW}➤ {suspicious} motores marcaram como SUSPEITO.")
    else:
        print(f"{Fore.GREEN}✅ LIMPO.")
        print(f"{Fore.GREEN}➤ {clean} motores indicaram que é seguro.")
        
    print("-" * 50)
    print(f"Malicious: {malicious} | Suspicious: {suspicious} | Clean: {clean}")
    print("="*50 + "\n")