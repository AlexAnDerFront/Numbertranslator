def main():
    input_format = get_input()

    if input_format == 'b':
        handle_binary_input()
    elif input_format == 'd':
        handle_decimal_input()
    elif input_format == 'h':
        handle_hexadecimal_input()

def get_input():
    while True:
        user_input = input("Bitte 'b' für Binär 'd' für dezimal oder 'h' hexadezimal eingeben: ").lower()
        if user_input in ['b', 'd', 'h']:
            return user_input
        else:
            print("Ungültiger input bitte 'b', 'd', oder 'h' eingeben!")

def is_binary(input_str):
    try:
        int(input_str, 2)  
        return True
    except ValueError:
        return False
        
def is_decimal(input_str):
    try:
        int(input_str)
        return True
    except ValueError:
        return False
    
def is_hexadecimal(input_str):
    try:
        int(input_str, 16)  
        return True  
    except ValueError:
        return False


def handle_binary_input():
    while True:
        user_input = input("Gib eine binär Zahl ein.")
        if is_binary(user_input):
            decimal_num = int(user_input, 2)
            hexadecimal_num = hex(decimal_num)[2:].upper() 
         #Outpbut der Resultate
            print(f"Dezimal: {decimal_num}")
            print(f"Hexadezimal: {hexadecimal_num}")
            print(f"Binär: {user_input}")
            break #Loop wird verlassen
        else:
            print("Falscher Input bitte eine binär Zahl") 

def handle_decimal_input():
    while True:
        user_input = int(input("Gib eine dezimal Zahl ein."))
        if is_decimal(user_input):
            binary_num = bin(user_input)
            hexadecimal_num = hex(user_input)[2:].upper() 
         #Output der Resultate
            print(f"Dezimal: {user_input}")
            print(f"Hexadezimal: {hexadecimal_num}")
            print(f"Binär: {binary_num}")
            break #Loop wird verlassen
        else:
            print("Falscher Input bitte eine dezimal Zahl") 

def handle_hexadecimal_input():
    while True:
        user_input = input("Gib eine hexadezimal Zahl ein.")
        if is_hexadecimal(user_input):
            decimal_num = int(user_input, 16)
            binary_num = bin(decimal_num)[2:]
         #Output der Resultate
            print(f"Dezimal: {decimal_num}")
            print(f"Hexadezimal: {user_input}")
            print(f"Binär: {binary_num}")
            break #Loop wird verlassen
        else:
            print("Falscher Input bitte eine hexadezimal Zahl") 

main()