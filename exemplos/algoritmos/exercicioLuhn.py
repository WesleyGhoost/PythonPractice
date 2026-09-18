# Exercicio com algoritmo de Luhn

def verify_card_number(digits):
    digits = digits.replace("-", "").replace(" ", "")

    total = 0
    reverse_digits = digits[::-1]

    for i, digit in enumerate(reverse_digits):
        digit = int(digit)

        if i % 2 == 1:
            digit *= 2

            if digit > 9:
                digit -= 9

        total += digit

    if total % 10 == 0:
        return 'VALID!'
    else:
        return 'INVALID!'