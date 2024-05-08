def main():                             # Main Funktion
    input_format = get_input()

    if input_format == 'b':            # If Abgrage die je nach wahl des nutzers in die entsprechend nächste funktion überspringt
        handle_binary_input()          # Funktion für binär
    elif input_format == 'd':
        handle_decimal_input()         # Funktion für dezimal
    elif input_format == 'h':
        handle_hexadecimal_input()     # Funktion für hexadezimal

def get_input():                        # Funktion die Abfragt welche Art von Zahl der Nutzer eingeben will
    while True:
        user_input = input("Bitte 'b' für Binär 'd' für dezimal oder 'h' hexadezimal eingeben: ").lower()   # fragt Nutzer input ab und covertiert ihn zu lower case
        if user_input in ['b', 'd', 'h']:                                                                   # if abfrage welche  überprüft ob der input gültig ist
            return user_input
        else:
            print("Ungültiger input bitte 'b', 'd', oder 'h' eingeben!")

def is_binary(input_str):               # Funktion welche überürüft ob der Input binär ist
    try:
        int(input_str, 2)  
        return True
    except ValueError:
        return False
        
def is_decimal(input_str):              # Funktion welche überürüft ob der Input dezimal ist
    try:
        int(input_str)
        return True
    except ValueError:
        return False
    
def is_hexadecimal(input_str):          # Funktion welche überürüft ob der Input hexadezimal ist
    try:
        int(input_str, 16)  
        return True  
    except ValueError:
        return False


def handle_binary_input():                                             # Funktion welche binär Zahlen konvertiert
    # while-lopp der erst verlassen wird wenn der user einen zugelassenen Input eingibt
    while True:
        # Nimmt Zahleninput des User entgegen
        user_input = input("Gib eine binär Zahl ein.")
        # If wird erst ausgeführt wenn useri_nput Richtig ist                                                       
        if is_binary(user_input):
            decimal_num = int(user_input, 2)
            hexadecimal_num = hex(decimal_num)[2:].upper() 
         # Outpbut der Resultate
            print(f"Dezimal: {decimal_num}")
            print(f"Hexadezimal: {hexadecimal_num}")
            print(f"Binär: {user_input}")
            break # Loop wird verlassen
        else:
            print("Falscher Input bitte eine binär Zahl") 

def handle_decimal_input():                                           # Funktion welche dezimal Zahlen konvertiert
    # while-lopp der erst verlassen wird wenn der user einen zugelassenen Input eingibt
    while True:     
        # Nimmt Zahleninput des User entgegen
        user_input = input("Gib eine dezimal Zahl ein.")
        # If wird erst ausgeführt wenn user_input Richtig ist
        if is_decimal(user_input):
            binary_num = bin(int(user_input))
            hexadecimal_num = hex(int(user_input))[2:].upper() 
         # Output der Resultate
            print(f"Dezimal: {user_input}")
            print(f"Hexadezimal: {hexadecimal_num}")
            print(f"Binär: {binary_num}")
            break # Loop wird verlassen
        else:
            print("Falscher Input bitte eine dezimal Zahl") 

def handle_hexadecimal_input():                                      # Funktion welche hexadezimal Zahlen konvertiert
    # while-lopp der erst verlassen wird wenn der user einen zugelassenen Input eingibt
    while True:
        # Nimmt Zahleninput des User entgegen
        user_input = input("Gib eine hexadezimal Zahl ein.")
        # If wird erst ausgeführt wenn user_input Richtig ist
        if is_hexadecimal(user_input):
            decimal_num = int(user_input, 16)
            binary_num = bin(decimal_num)[2:]
         # Output der Resultate
            print(f"Dezimal: {decimal_num}")
            print(f"Hexadezimal: {user_input}")
            print(f"Binär: {binary_num}")
            break # Loop wird verlassen
        else:
            print("Falscher Input bitte eine hexadezimal Zahl") 

main()                                                                                                          # Aufruf der main()-Funktion zu start des Programms