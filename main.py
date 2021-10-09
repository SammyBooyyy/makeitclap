from re import M
import requests, json, os, time, speedtest, shutil
from colorama import Fore as F

def tentar():
    try:

        def logo():
            r = requests.get('https://pastebin.com/raw/15r4d3yE')
            print(F.LIGHTYELLOW_EX + r.text)

        def clear():
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')

        def main():
            clear()
            logo()
            print(f'{F.LIGHTGREEN_EX}[{F.LIGHTWHITE_EX}01{F.LIGHTGREEN_EX}] {F.LIGHTYELLOW_EX}Check if site is up/down          {F.LIGHTGREEN_EX}[{F.LIGHTWHITE_EX}04{F.LIGHTGREEN_EX}] {F.LIGHTYELLOW_EX}Check Internet Speed')
            print(f'{F.LIGHTGREEN_EX}[{F.LIGHTWHITE_EX}02{F.LIGHTGREEN_EX}] {F.LIGHTYELLOW_EX}Check if email is valid')
            print(f'{F.LIGHTGREEN_EX}[{F.LIGHTWHITE_EX}03{F.LIGHTGREEN_EX}] {F.LIGHTYELLOW_EX}IP Tracker')
            print(f'\n\n\n{F.LIGHTGREEN_EX}[{F.LIGHTWHITE_EX}99{F.LIGHTGREEN_EX}] {F.LIGHTRED_EX}Exit')

            x = input(f'{F.LIGHTGREEN_EX}[*] Choose an option > {F.RESET}')
            if x == '1':
                check_site()
            elif x == '2':
                check_email()
            elif x == '3':
                ip_tracker()
            elif x == '99':
                sair()
            elif x == '4':
                Speedtest()
            else:
                print(F.RED + 'ERROR')
                print(F.RESET + 'Returning to main area in:')
                print(3)
                time.sleep(1)
                print(2)
                time.sleep(1)
                print(1)
                time.sleep(1)
                return tentar()

        def check_site():
            site = input(f'{F.LIGHTGREEN_EX}[*] Website > {F.RESET}')
            r = requests.get(site)
            if r.status_code == 200:
                print(f'{F.LIGHTYELLOW_EX}Site is {F.LIGHTGREEN_EX} ONLINE {F.RESET}')
            else:
                print(f'{F.LIGHTYELLOW_EX}Site is {F.LIGHTRED_EX} OFFLINE {F.RESET}')

            time.sleep(5)
            return tentar()

        def check_email():
            email = input(f'{F.LIGHTGREEN_EX}[*] Check email > {F.RESET}')
            r = requests.get(f'https://api.2ip.me/email.txt?email={email}')
            if r.text == 'true':
                print(f'{F.LIGHTGREEN_EX}[*] Mail "{email}" is VALID!{F.RESET}')
                time.sleep(5)
                return tentar()
            else:
                print(f'{F.LIGHTYELLOW_EX}[!] Invalid email!')
                time.sleep(5)
                return tentar()

        def ip_tracker():
            ip = input(f'{F.LIGHTGREEN_EX}[*] IP Address > {F.RESET}')
            r = requests.get(f'https://ipinfo.io/{ip}/?token=195ace11ca99b7')
            dados = json.loads(r.text)
            print(f'{F.LIGHTGREEN_EX}[{F.LIGHTWHITE_EX}IP{F.LIGHTGREEN_EX}] {F.LIGHTYELLOW_EX}      {dados["ip"]}')
            print(f'{F.LIGHTGREEN_EX}[{F.LIGHTWHITE_EX}Hostname{F.LIGHTGREEN_EX}] {F.LIGHTYELLOW_EX}{dados["hostname"]}')
            print(f'{F.LIGHTGREEN_EX}[{F.LIGHTWHITE_EX}Country{F.LIGHTGREEN_EX}] {F.LIGHTYELLOW_EX} {dados["country"]}')
            print(f'{F.LIGHTGREEN_EX}[{F.LIGHTWHITE_EX}Region{F.LIGHTGREEN_EX}] {F.LIGHTYELLOW_EX}  {dados["region"]}')
            print(f'{F.LIGHTGREEN_EX}[{F.LIGHTWHITE_EX}City{F.LIGHTGREEN_EX}] {F.LIGHTYELLOW_EX}    {dados["city"]}')

        def Speedtest():
            st = speedtest.Speedtest()
            threads = None
            st.get_best_server()
            st.download(threads=threads)
            st.upload(threads=threads)
            
            filename = 'SpeedTest.png'

            r = requests.get(st.results.share(), stream=True)
            
            if r.status_code == 200:
                r.raw.decode_content = True
                with open(filename, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
                
                os.system('SpeedTest.png')

                return tentar()
            else:
                print('Aconteceu um erro!')
                time.sleep(3)
                return tentar()
        
        def sair():
            r = requests.get('https://pastebin.com/raw/0C9TP130')
            print(F.RED + r.text)
            time.sleep(3)
            clear()
            F.RESET
            exit()

        main()


    except KeyboardInterrupt:
        clear()
        sure = input(f'{F.LIGHTGREEN_EX}[*] Are you sure that you want to leave? y/n > {F.RESET}')
        if sure == 'y':
            sair()
        else:
            return tentar()


if __name__ == '__main__':
    tentar()