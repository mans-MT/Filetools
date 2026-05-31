#███████╗██╗██╗     ███████╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗
#██╔════╝██║██║     ██╔════╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
#█████╗  ██║██║     █████╗         ██║   ██║   ██║██║   ██║██║     ███████╗
#██╔══╝  ██║██║     ██╔══╝         ██║   ██║   ██║██║   ██║██║     ╚════██║
#██║     ██║███████╗███████╗       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
#╚═╝     ╚═╝╚══════╝╚══════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝

import os
from cryptography.fernet import Fernet as fer
from cryptography.fernet import InvalidToken
active = 1

def func_write(filename):
    data = input("Enter data to be written into file:")
    with open(filename, "w+") as pq:
        pq.write(data)
        pq.seek(0)
        test = pq.read()
    if test == data:
        print(f"Successfully wrote {len(data)} characters into {filename}")

def func_read(filename):
    with open(filename, "r") as pq:
        a = pq.read()
    print(f'\t{filename} : {a}')

def func_clear(filename):
    with open(filename, "w+") as pq:
        pq.write('')
        pq.seek(0)
        if len(pq.read()) == 0:
            print(f"Successfully cleared data from file {filename}.")
        else:
            print(f"Error encountered whilst clearing {filename}, could not clear data.")

def func_append(filename):
    data = input("Enter data to be appended to file:")
    with open(filename, "a") as pq:
        pq.write(data)
    print(f"Successfully appended {len(data)} characters into {filename}")
    
def func_encrypt(filename):
    key = fer.generate_key()
    with open(filename,'rb') as pq:
        initial = pq.read()
        encrypted = fer(key).encrypt(initial)
    with open(filename,'wb') as pq:
        pq.write(encrypted)
    with open(filename,'rb') as pq:
        final = pq.read()
        if final == encrypted:
            print(f'Successfully encrypted {filename}\nYour key is < {key.decode()} >')
        else:
            print(f'Couldn\'t encrypt file.')
    
def func_decrypt(filename):
    key = input("Enter file key: ").strip().encode()

    try:
        with open(filename, "rb") as pq:
            encrypted_data = pq.read()

        decrypted_data = fer(key).decrypt(encrypted_data)

        with open(filename, "wb") as pq:
            pq.write(decrypted_data)

        print(f"Successfully decrypted {filename}")

    except InvalidToken:
        print("Error: Invalid key or corrupted file.")

    except Exception as e:
        print(f"Unexpected error: {e}")

files = []

include = ["txt", "md", "py", "json", "csv", "xml",
    "html", "css", "js", "yml", "yaml"] 
for f in os.listdir():
    a = [str(q) for q in f.split('.')]
    for i in include:
        if i in a:
            files.append(f)
                      
print('''╭────────────╮\n│  FileTools │\n╰────────────╯''')
if input('Welcome to Filetools! Would you like to start?\t').lower() in ['yes','y','1','']:
    print('Select file to carry operation on:\n')
    f_name = input(("\t\n".join(f" - {f}" for f in files[:5]))+f' ... ({len(files)-5} more)\t')
    while active:
        op = int(input("Select operation:\n\t1.Write\n\t2.Read\n\t3.Append\n\t4.Clear\n\t5.Encrypt\n\t6.Decrypt\t"))
        print('\n')
        if op == 1:
            func_write(f_name)
        elif op == 2:
            func_read(f_name)
        elif op == 3:
            func_append(f_name)
        elif op == 4:
            func_clear(f_name)
        elif op == 5:
            print(f'WARNING: THIS IS AN EXPERIMENTAL FEATURE AND MAY LEAD TO DATA LOSS. BACK UP YOUR FILES BEFORE USING THIS.')
            if input('Do you want to proceed with encryption?\t').lower() in ['yes', 'y', '1', '']:
                func_encrypt(f_name)
        elif op == 6:
            print(f'WARNING: THIS IS AN EXPERIMENTAL FEATURE AND MAY LEAD TO DATA LOSS. BACK UP YOUR FILES BEFORE USING THIS.')
            if input('Do you want to proceed with decryption?\t').lower() in ['yes', 'y', '1', '']:
                func_decrypt(f_name)
        else:
            print("Error: Invalid Operation")
        repeat = input("\nWould you like to carry out more operations on the same file (Y/n) ?\t")
        if repeat.lower() == 'n':
            print('\nThank you for using FileTools\nVisit github.com/mans-MT/Filetools to leave feedback and recieve updates!')
            break
else:
    print(f'Closing FileTools')
    active = 0