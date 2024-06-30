import os
import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Back, Style
import string
import re

# Colorama'nın başlatılması
init(autoreset=True)

# ASCII sanatı
ascii_art = f"""
{Fore.BLUE}
 __    __  ________  ________  ________  ______  _______  
|  \  /  \|        \|        \|        \|      \|       \ 
| $$ /  $$| $$$$$$$$ \$$$$$$$$ \$$$$$$$$ \$$$$$$| $$$$$$$\
| $$/  $$ | $$__       | $$      | $$     | $$  | $$__/ $$
| $$  $$  | $$  \      | $$      | $$     | $$  | $$    $$
| $$$$$\  | $$$$$      | $$      | $$     | $$  | $$$$$$$ 
| $$ \$$\ | $$_____    | $$      | $$    _| $$_ | $$      
| $$  \$$\| $$     \   | $$      | $$   |   $$ \| $$      
 \$$   \$$ \$$$$$$$$    \$$       \$$    \$$$$$$ \$$      

  ______    ______   _______   ______  _______  ________   ______  
 /      \  /      \ |       \ |      \|       \|        \ /      \ 
|  $$$$$$\|  $$$$$$\| $$$$$$$\ \$$$$$$| $$$$$$$\\$$$$$$$$|  $$$$$$\
| $$___\$$| $$   \$$| $$__| $$  | $$  | $$__/ $$  | $$   | $$___\$$
 \$$    \ | $$      | $$    $$  | $$  | $$    $$  | $$    \$$    \ 
 _\$$$$$$\| $$   __ | $$$$$$$\  | $$  | $$$$$$$   | $$    _\$$$$$$\
|  \__| $$| $$__/  \| $$  | $$ _| $$_ | $$        | $$   |  \__| $$
 \$$    $$ \$$    $$| $$  | $$|   $$ \| $$        | $$    \$$    $$
  \$$$$$$   \$$$$$$  \$$   \$$ \$$$$$$ \$$         \$$     \$$$$$$ 
                                                                   
                                                                   
                                                                   
"""

def print_header():
    print(ascii_art)
    print(f"{Fore.CYAN}Discord Sunucumuz: {Fore.GREEN}https://discord.gg/msNr2fPaTP{Fore.RESET}\n{Fore.YELLOW}NOT:veri kümesi oluşturma çalışmamıyor şuanlık yapmaya üşendim yapınca duyuru atarım sunucuda")
    print()

def html_copy():
    site_link = input(f"{Fore.YELLOW}Lütfen HTML kopyalamak istediğiniz sitenin linkini girin: ")
    response = requests.get(site_link)
    if response.status_code == 200:
        html_content = response.text
        file_name = f"{site_link.split('//')[1].replace('/', '_')}.html"
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(html_content)
        print(f"{Fore.GREEN}{file_name} dosyası başarıyla kaydedildi.")
        clean_and_tokenize(file_name)
    else:
        print(f"{Fore.RED}Bağlantı hatası! Siteye erişilemiyor.")

def get_page_content():
    site_link = input(f"{Fore.YELLOW}Lütfen sayfa içeriğini almak istediğiniz sitenin linkini girin: ")
    response = requests.get(site_link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        page_content = soup.get_text()
        file_name = f"{site_link.split('//')[1].replace('/', '_')}.txt"
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(page_content)
        print(f"{Fore.GREEN}{file_name} dosyası başarıyla kaydedildi.")
        clean_and_tokenize(file_name)
    else:
        print(f"{Fore.RED}Bağlantı hatası! Siteye erişilemiyor.")

def xml_copy():
    site_link = input(f"{Fore.YELLOW}Lütfen XML kopyalamak istediğiniz sitenin linkini girin: ")
    response = requests.get(site_link)
    if response.status_code == 200:
        xml_content = response.text
        file_name = f"{site_link.split('//')[1].replace('/', '_')}.xml"
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(xml_content)
        print(f"{Fore.GREEN}{file_name} dosyası başarıyla kaydedildi.")
        clean_and_tokenize(file_name)
    else:
        print(f"{Fore.RED}Bağlantı hatası! Siteye erişilemiyor.")

def create_dataset():
    site_link = input(f"{Fore.YELLOW}Lütfen veri kümesi oluşturmak istediğiniz sitenin linkini girin: ")
    response = requests.get(site_link)
    if response.status_code == 200:

        print(f"{Fore.GREEN}Veri kümesi başarıyla oluşturuldu.")
        file_name = f"{site_link.split('//')[1].replace('/', '_')}.txt"
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write("Veri kümesi oluşturuldu.")
        clean_and_tokenize(file_name)
    else:
        print(f"{Fore.RED}Bağlantı hatası! Siteye erişilemiyor.")

def clean_and_tokenize(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()

    content = re.sub(r'\s+', ' ', content)

    printable = set(string.printable)
    content = ''.join(filter(lambda x: x in printable, content))

    clean_file_name = f"cleaned_{file_name}"
    with open(clean_file_name, 'w', encoding='utf-8') as clean_file:
        clean_file.write(content)

    print(f"{Fore.GREEN}Veri başarıyla temizlendi ve tokenized edilip {clean_file_name} dosyasına kaydedildi.")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header()
        print(f"{Fore.YELLOW}Seçenekler:")
        print(f"{Fore.MAGENTA}1) HTML Kopyalama")
        print(f"{Fore.MAGENTA}2) Sayfa İçeriği Alma")
        print(f"{Fore.MAGENTA}3) XML Kopyalama")
        print(f"{Fore.MAGENTA}4) Veri Kümesi Oluşturma")
        print()

        choice = input(f"{Fore.YELLOW}Lütfen yapmak istediğiniz işlemi seçin ({Fore.MAGENTA}1{Fore.YELLOW}/{Fore.MAGENTA}2{Fore.YELLOW}/{Fore.MAGENTA}3{Fore.YELLOW}/{Fore.MAGENTA}4{Fore.YELLOW}): ")

        if choice == '1':
            html_copy()
        elif choice == '2':
            get_page_content()
        elif choice == '3':
            xml_copy()
        elif choice == '4':
            create_dataset()
        else:
            print(f"{Fore.RED}Geçersiz seçenek! Lütfen tekrar deneyin.")

        input(f"\n{Fore.YELLOW}Devam etmek için Enter tuşuna basın...")

if __name__ == "__main__":
    main()
