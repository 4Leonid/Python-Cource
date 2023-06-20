file_path = '8H.txt'

def show_all_records():
    with(open(file_path, 'r', encoding='utf-8')) as f:
        for line in f:
            phonebook_data = line.replace(';', ' ') 
            print(phonebook_data, end='')


def search_records(contact):
    with open(file_path,"r",encoding="utf-8") as f:
        for line in f:
            if contact.lower() in line.split(';')[0].lower():
                print(line, end='')

    
def add_contact(fio, number):
    with open(file_path,"a",encoding="utf-8") as f:
        f.write("\n")
        f.write(fio.replace(" ",";"))
        f.write(';')
        f.write(number)

def delete(contact):
    with open(file_path, "r") as f:
        lines = f.readlines()
    with open(file_path, "w") as f:
        for line in lines:
            if line.strip("\n") != contact:
                f.write(line)

def main():
    print('Choose action: 1 - Show contacts,'
          '2 - Find contact,'
          '3 - add contact,'
          '4 - delete contact')
    select = int(input())
    if select == 1:
        show_all_records()
    elif select == 2:
        name = input('Input you last name: ')
        search_records(name)
    elif select == 3:
        fio = input("Input your full name: ")
        number = input("Input your phone number: ")
        add_contact(fio, number)
    elif select == 4:
        contact = input("Input your full name: ")
        delete(contact)
        
main()