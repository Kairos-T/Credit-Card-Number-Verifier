import re 

pattern = r'^\d{4}-\d{4}-\d{4}-\d{4}$'

def luhn_algorithm(card_number):
    card_digits = [int(digit) for digit in card_number.replace('-', '')]
    check_digit = card_digits.pop()

    doubled_digits = [2 * digit if i % 2 == 0 else digit for i, digit in enumerate(card_digits)]
    summed_digits = [sum(map(int, str(doubled))) for doubled in doubled_digits]
    total_sum = sum(summed_digits) + check_digit

    if total_sum % 10 == 0:
        return True
    else:
        return False
    
while True:
    card_number = input("Please enter your credit card number in the format XXXX-XXXX-XXXX-XXXX: ")
    
    try:
        if re.match(pattern, card_number):
            if luhn_algorithm(card_number):
                print("Credit card number is valid!")
                break

            else:
                print("Credit card number is invalid. Please try again.")
        else:
            print("Credit card number is invalid. Please check the number of digits and try again.")
    except re.error as e:
          print(f"Error occurred: {e}. Please try again.")