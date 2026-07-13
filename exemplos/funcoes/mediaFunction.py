def lerNotas() :
    n = int(input("Digite a nota do aluno:"))
    return n

def resultadoMedia(n1, n2) :
    media = (n1 + n2) / 2
    print("Notas: ", n1, " e ", n2)
    print("Media: ", media, ", Resultado: ", end="")

    if(media >=6) :
        print("Aprovado")
    else :
        print("Reprovado")

nota1 = lerNotas()
nota2 = lerNotas()

resultadoMedia(nota1, nota2)