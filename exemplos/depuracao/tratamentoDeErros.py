try:
    number = int(input("Digite um número: "))
    result = 10 / number
except (ValueError, ZeroDivisionError) as error:
    print(f"Erro ocorrido: {error}")
else:
    print(f"O resultado é: {result}")
finally:
    print("Esse bloco sempre será chamado")



#raise sem argumento
#def process_data(data):
    #try:
        #result = int(data)
        #return result
    #except ValueError:
        #print("Dado inválido recebido")
        #raise

#process_data('abc')



#raise personalizado
def check_age(age):
    if age < 0:
        raise ValueError("Idade não pode ser negativa")
    return age

try:
    check_age(-6)
except ValueError as error:
    print(f"Erro: {error}")



#raise e from
#def parse_config(filename):
    #try:
        #with open(filename, 'r') as file:
            #data = file.read()
            #return int(data)
    #except FileNotFoundError:
        #raise ValueError('Arquivo de configuração não encontrado') from None
    #except ValueError as e:
        #raise ValueError('Formato de configuração inválido') from e

#config = parse_config('config.txt')



#assert
def calculate_square_root(number):
    assert number >= 0, 'Não é possivel calcular a raiz quadrada de número negativos'
    return number ** 0.5

try:
    calculate_square_root(-3)
except AssertionError as error:
    print(f"Erro: {error}")