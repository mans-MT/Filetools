import os
active = True

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
    print(a)

def func_append(filename):
    data = input("Enter data to be appended to file:")
    with open(filename, "r") as pq:
        initial = pq.read()
        final = initial + data
    with open(filename, "w") as pq:
        pq.write(final)
    print(f"Successfully appended {len(data)} characters into {filename}")

f_name = input("Enter filename with extension to carry operation on:")
while active:
    op = int(input("Select operation:\n\t1.Write\n\t2.Read\n\t3.Append\t"))
    if op == 1:
        func_write(f_name)
    elif op == 2:
        func_read(f_name)
    elif op == 3:
        func_append(f_name)
    else:
        print("Error: Invalid Operation")
    repeat = input("Would you like to carry out more operations on the same file (y/n) ?\t")
    if repeat.lower() == 'n':
        print('Thank you for using this tool\nVisit github.com/mans/filetools to leave feedback and recieve updates!')
        break
