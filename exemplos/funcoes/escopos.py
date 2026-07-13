## escopo local
def exemple_func_one():
    msg = "mensagem exemplo"
    print(msg)

exemple_func_one()


## escopo de contenção
def exemple_func_two():
    msg = "mensagem exemplo: "
    inner_msg = ""

    def inner_func():
        nonlocal inner_msg
        inner_msg = "Pastel de frango"
        print(msg + inner_msg)

    inner_func()

exemple_func_two()


## escopo global
my_var_one = "Variável global"

def exemple_func_three():
    global my_var_two
    my_var_two = "variável global na função"
    print(my_var_one)

exemple_func_three()
print(my_var_two)


## escopo embutido
print(str(35))
print(int('9'))
print(bool(False))
