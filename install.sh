#!/bin/bash
# DarkForge Toolkit Installer (Root@OSINT:~#)
# Supports: Kali Linux & Termux

# ANSI Colors
RED="\033[1;31m"
GREEN="\033[1;32m"
YELLOW="\033[1;33m"
BLUE="\033[1;34m"
PURPLE="\033[1;35m"
CYAN="\033[1;36m"
WHITE="\033[1;37m"
RESET="\033[0m"

# Анимационные эффекты
function animate_text() {
    text=$1
    delay=$2
    for (( i=0; i<${#text}; i++ )); do
        echo -n -e "${PURPLE}${text:$i:1}${RESET}"
        sleep $delay
    done
    echo
}

function progress_bar() {
    duration=$1
    chars=('▰' '▱')
    echo -ne "${CYAN}"
    for i in {1..30}; do
        pos=$((i % 10))
        bar=""
        for (( j=0; j<30; j++ )); do
            if [ $j -le $i ]; then
                bar+="${chars[0]}"
            else
                bar+="${chars[1]}"
            fi
        done
        echo -ne "\r[${bar}] ${WHITE}$((i*3))%${RESET}"
        sleep $(bc -l <<< "$duration/30")
    done
    echo -e "\n"
}

function matrix_effect() {
    echo -e "${GREEN}"
    for i in {1..12}; do
        printf "%0.s0 1 " {1..40}
        sleep 0.05
        echo -ne "\r\033[K"
    done
    echo -e "${RESET}"
}

# Заголовок установщика
function show_header() {
    clear
    matrix_effect
    
    echo -e "${PURPLE}"
    cat << "EOF"
     _____             _    ______          _       
    |  __ \           | |  |  ____|        | |      
    | |  | | __ _ _ __| | _| |__ ___   ___ | | ___  
    | |  | |/ _` | '__| |/ /  __/ _ \ / _ \| |/ _ \ 
    | |__| | (_| | |  |   <| | | (_) | (_) | |  __/ 
    |_____/ \__,_|_|  |_|\_\_|  \___/ \___/|_|\___| 
EOF

    echo -e "${RESET}"
    animate_text ":: ADVANCED CYBER OPERATIONS FRAMEWORK ::" 0.03
    echo -e "${BLUE}----------------------------------------------${RESET}"
    animate_text "> Preparing system for DarkForge installation" 0.02
    echo
}

# Определение платформы
function detect_platform() {
    echo -e "${YELLOW}[*] Detecting platform...${RESET}"
    sleep 1
    
    if [ -f "/etc/os-release" ] && grep -q "Kali" /etc/os-release; then
        OS="kali"
        echo -e "${GREEN}[+] Kali Linux detected${RESET}"
    elif [ -d "/data/data/com.termux" ]; then
        OS="termux"
        echo -e "${GREEN}[+] Termux environment detected${RESET}"
    else
        echo -e "${RED}[!] Unsupported OS${RESET}"
        exit 1
    fi
}

# Установка зависимостей
function install_dependencies() {
    echo -e "\n${YELLOW}[*] Installing dependencies${RESET}"
    
    if [ "$OS" = "kali" ]; then
        animate_text "> Updating package database..." 0.01
        sudo apt update -y &> /dev/null
        
        echo -e "${CYAN}[+] Installing core packages${RESET}"
        progress_bar 2
        
        sudo apt install -y python3 python3-pip metasploit-framework aircrack-ng hydra git \
        libffi-dev libssl-dev zsh qrencode wireless-tools &> /dev/null
        
        echo -e "${CYAN}[+] Installing Python modules${RESET}"
        progress_bar 1
        sudo pip3 install pycryptodome &> /dev/null

    elif [ "$OS" = "termux" ]; then
        animate_text "> Updating Termux packages..." 0.01
        pkg update -y &> /dev/null
        
        echo -e "${CYAN}[+] Installing core packages${RESET}"
        progress_bar 2
        
        pkg install -y python python-pip metasploit hydra git libffi openssl \
        root-repo termux-api qrencode ncurses-utils &> /dev/null
        
        echo -e "${CYAN}[+] Installing Python modules${RESET}"
        progress_bar 1
        pip install pycryptodome &> /dev/null
    fi

    echo -e "${GREEN}[✓] Dependencies installed successfully${RESET}"
}

# Установка DarkForge
function install_darkforge() {
    echo -e "\n${YELLOW}[*] Installing DarkForge Toolkit${RESET}"
    
    # Анимация скачивания
    echo -e "${CYAN}[+] Downloading from GitHub${RESET}"
    progress_bar 1.5
    
    # ИЗМЕНЕННАЯ ССЫЛКА НА РЕПОЗИТОРИЙ
    git clone https://github.com/2OTERATAR/darkforge-toolkit.git &> /dev/null
    cd darkforge-toolkit || exit
    
    # Настройка прав
    chmod +x darkforge.py
    
    # Создание ярлыка (Kali)
    if [ "$OS" = "kali" ]; then
        echo -e "${CYAN}[+] Creating desktop shortcut${RESET}"
        cat > ~/Desktop/DarkForge.desktop << EOF
[Desktop Entry]
Name=DarkForge Toolkit
Exec=python3 $PWD/darkforge.py
Icon=terminal
Type=Application
Categories=System;
Terminal=true
EOF
        chmod +x ~/Desktop/DarkForge.desktop
    fi
    
    # Добавление в PATH
    echo -e "${CYAN}[+] Adding to PATH${RESET}"
    if [ "$OS" = "kali" ]; then
        echo "export PATH=\$PATH:$PWD" >> ~/.bashrc
        source ~/.bashrc
    elif [ "$OS" = "termux" ]; then
        echo "export PATH=\$PATH:$PWD" >> ~/.bash_profile
        source ~/.bash_profile
    fi
    
    echo -e "${GREEN}[✓] Installation complete!${RESET}"
}

# Завершение установки
function finalize() {
    echo -e "\n${PURPLE}"
    cat << "EOF"
    ██████╗  █████╗ ██████╗ ██╗  ██╗███████╗ ██████╗ ██████╗  ██████╗ ███████╗
    ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██╔════╝ ██╔══██╗██╔═══██╗██╔════╝
    ██║  ██║███████║██████╔╝█████╔╝ █████╗  ██║  ███╗██████╔╝██║   ██║█████╗  
    ██║  ██║██╔══██║██╔══██╗██╔═██╗ ██╔══╝  ██║   ██║██╔══██╗██║   ██║██╔══╝  
    ██████╔╝██║  ██║██║  ██║██║  ██╗███████╗╚██████╔╝██║  ██║╚██████╔╝███████╗
    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
EOF
    echo -e "${RESET}"
    
    echo -e "${GREEN}======================================================"
    echo -e " DarkForge Toolkit успешно установлен!"
    echo -e "======================================================${RESET}"
    echo -e "${YELLOW}Запуск:${RESET}"
    echo -e "  ${CYAN}./darkforge.py${RESET} или ${CYAN}python3 darkforge.py${RESET}"
    echo
    echo -e "${YELLOW}Для Termux:${RESET}"
    echo -e "  ${CYAN}termux-setup-storage${RESET} (для доступа к файлам)"
    echo
    echo -e "${RED}ВНИМАНИЕ:${RESET} Используйте только в образовательных целях!"
    echo -e "${BLUE}======================================================${RESET}"
}

# Главный процесс установки
show_header
detect_platform
install_dependencies
install_darkforge
finalize
