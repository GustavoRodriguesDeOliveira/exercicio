from random import randint

def exercicio01():
    A = 10
    B = 20
    msg = "Antes da troca: A = {}, B = {}".format(A, B)
    aux = A
    A = B
    B = aux
    msg = msg + "\nDepois da troca: A = {}, B = {}" .format(A, B)
    return  msg

def exercicio02():
    n = int(input('Digite um número: '))
    print('Analisando o valor {}, seu antecessor é {}'.format(n, (n-1)))
    return

def exercicio03():
   n = int(input('Digite a base: '))
   h = int(input('Digite a altura: '))
   z = n * h
   print('Area é {}'.format(z))




def exercicio05():
    r1 = int(input("Digitea quantidade de eleitores do município X: "))

    r2 = int(input("Quantidade de votos nulos: "))
    r3 = int(input("Quantidade de votos brancos: "))
    r4 = int(input("Quantidade de votos válidos:"))

    if (r2 + r3 + r4 > r1):
        print("Mais votos que eleitores")
        exit()

    print("Quantidade de votos")
    print("Brancos: ", (r3 * 100) / r1, "%")
    print("Nulos: ", (r2 * 100) / r1, "%")
    print("Válidos: ", (r4 * 100) / r1)

def exercicio06():
    r1 = int(input("Digite o valor do salario: "))

    r2 = int(input("Reajuste em porcentagem: "))
    aux = r1 * (r2 / 100)
    aux = r1 + aux
    print("Valor com reajuste: ", aux)

def exercicio07():
    r1 = int(input("Valor do custo fabrica: "))

    imp = 0.45
    pct = 0.28

    custo = (r1 * imp) + (r1 * pct) + r1

    print("Custo do carro final: ", custo)

def exercicio08():
    n1 = int(input("Nota1"))
    n2 = int(input("Nota2"))
    n3 = int(input("Nota3"))

    media = (n1 + n2 + n3) / 3

    print("Media: ", media)

def exercicio09():
    n1 = int(input("Macas compradas"))

    if n1 >= 12:
        print("Valor totalé: ", n1 * 1)

    else:
        print("VALOR totalé: ", n1 * 1.3)

def exercicio10():
    from random import randint

    n1 = []
    continua = True
    for i in range(0, 10):
        n2 = randint(0, 9)
        n3 = len(n1)
        for j in range(0, n3):

            if n2 == n1[j]:
                i = i - 1
                break
        if continua == True:
            n1.append(n2)

def exercicio11():
    sf = int(input("Salario fixo"))

    vdv = int(input("Valor de vendas: "))

    salarionovo = sf + (0.03 * vdv)
    if vdv > 1500:

        valordiferente = vdv - 1500
        salarionovo = salarionovo + (valordiferente * 0.05)
        print("Valor salario: ", salarionovo)

    else:
        print("Valor do salario: ", salarionovo)

def exercicio12():
    sld = float(input("Saldo: "))
    deb = float(input("Debito: "))
    cred = float(input("Crédito: "))

    soma = (sld - deb) + cred

    if soma >= 0:
        print("ASaldo positivo")

    if soma < 0:
        print("Saldo negativo")


def exercicio13():
    n = int(input("Numero "))

    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

def exercicio14():
    n = int(input("Valor: "))
    print(n)
    while n != 1:
        n = n - 1
        print(n)

def exercicio15():
    n = []

    ngtv = 0
    pstv = 0
    for i in range(1, 11):
        n.append(int(input("Valor:")))

    print(n)
    for j in range(0, 10):

        if n[j] < 0:
            ngtv = ngtv + 1

        if n[j] > 0:
            pstv = pstv + 1

    print("Negativos: ", ngtv)
    print("Positivos: ", pstv)

def exercicio16():
    n = []
    sm = 0
    for i in range(1, 11):
        n.append(int(input("Valor: ")))

    for j in range(0, 10):

        if n[j] < 40:
            sm = sm + n[j]

    print("Valor total: ", sm)

def exercicio17():
    soma = 0
    qt = 0
    for i in range(15, 101):
        soma = soma + i
        print("soma atual", soma)
        qt = qt + 1

    media = soma / qt
    print("quantidade de numeros", qt)
    print("Media: ", media)

def exercicio18():

    n = []
    media = 0
    for i in range(1, 10):
        rn = randint(10, 200)
        print("numero gerado", rn)
        n.append(rn)
        media = media + rn

    media = media / 10
    print("MAIOR NUMERO", max(n))
    print("Media", media)

def exercicio19():

    notas = []
    media = 0
    for i in range(1, 21):
        adc = randint(1, 10)
        notas.append(adc)
        media = notas[i - 1] + media

    media = media / 20

    print("Media da turma: ", media)
    tt = 0
    for j in range(0, 20):

        if notas[j] > media:
            tt = tt + 1

    print("Alunos com nota maior que a media = ", tt)












