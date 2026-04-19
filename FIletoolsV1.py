#███████╗██╗██╗     ███████╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗   ██╗   ██╗ ██╗
#██╔════╝██║██║     ██╔════╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝   ██║   ██║███║
#█████╗  ██║██║     █████╗         ██║   ██║   ██║██║   ██║██║     ███████╗   ██║   ██║╚██║
#██╔══╝  ██║██║     ██╔══╝         ██║   ██║   ██║██║   ██║██║     ╚════██║   ╚██╗ ██╔╝ ██║
#██║     ██║███████╗███████╗       ██║   ╚██████╔╝╚██████╔╝███████╗███████║    ╚████╔╝  ██║
#╚═╝     ╚═╝╚══════╝╚══════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝     ╚═══╝   ╚═╝

import os
active = 1

def func_write(filename):
    data = input("Enter data to be written into file:")
    with open(filename, "w") as pq:
        pq.write(data)
    with open(filename, "r") as pq:
        test = pq.read()
    if test == data:
        print(f"Successfully wrote {len(data)} characters into {filename}")

def func_read(filename):
    with open(filename, "r") as pq:
        a = pq.read()
    print(f'\t{filename} : {a}')

def func_clear(filename):
    with open(filename, "w") as pq:
        pq.write('')
    with open(filename, "r") as pq:
        if len(pq.read()) == 0:
            print(f"Successfully cleared data from file {filename}.")
        else:
            print(f"Error encountered whilst clearing {filename}, could not clear data.")

def func_append(filename):
    data = input("Enter data to be appended to file:")
    with open(filename, "r") as pq:
        initial = pq.read()
        final = initial + data
    with open(filename, "w") as pq:
        pq.write(final)
    print(f"Successfully appended {len(data)} characters into {filename}")

files = []

include = ["txt", "md", "py", "json", "csv", "xml",
    "html", "css", "js", "yml", "yaml"] 
for f in os.listdir():
    a = [str(q) for q in f.split('.')]
    for i in include:
        if i in a:
            files.append(f)
                      
print('''╭────────────╮
│  FileTools │
╰────────────╯''')
if input('Welcome to Filetools! Would you like to start?\t').lower() in ['yes','y','1']:
    print('Select file to carry operation on:\n')
    f_name = input(("\t\n".join(f" - {f}" for f in files[:5]))+f' ... ({len(files)-5} more)\t')
    while active:
        op = int(input("Select operation:\n\t1.Write\n\t2.Read\n\t3.Append\n\t4.Clear\t"))
        if op == 1:
            func_write(f_name)
        elif op == 2:
            func_read(f_name)
        elif op == 3:
            func_append(f_name)
        elif op == 4:
            func_clear(f_name)
        else:
            print("Error: Invalid Operation")
        repeat = input("Would you like to carry out more operations on the same file (y/n) ?\t")
        if repeat.lower() == 'n':
            print('Thank you for using FileTools\nVisit github.com/mans-birb/filetools to leave feedback and recieve updates!')
            break
else:
    active = 0
