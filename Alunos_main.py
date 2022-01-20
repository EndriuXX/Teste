import math
from time import sleep

opção = 0
while opção != 17:
    print('-=' * 20)
    print('''    
    [ 1 ] Somar
    [ 2 ] Subtrair
    [ 3 ] Multiplicar
    [ 4 ] Dividir
    [ 5 ] Divisão inteira
    [ 6 ] Resto da divisão
    [ 7 ] Raiz quadrada
    [ 8 ] Cálculo de fatorial
    [ 9 ] Elevar número
    [ 10 ] Calcular equação do segundo grau
    [ 11 ] Raiz cubica
    [ 12 ] Números de PI
    [ 13 ] Calcular área
    [ 14 ] Calcular média
    [ 15 ] Calcular vértice de delta
    [ 16 ] Conversor de medidas
    [ 17 ] Sair do programa''')
    opção = int(input("Qual a sua opção? "))
    if opção == 1:
        s1 = float(input('Digite um valor: '))
        s2 = float(input("Digite um valor: "))
        soma = s1 + s2
        print("-=" * 20)
        print("A soma de {} + {} é {}".format(s1, s2, soma))
        print("-=" * 20)
        sleep(2)
    elif opção == 2:
        sub1 = float(input("Primeiro valor: "))
        sub2 = float(input("Segundo valor: "))
        sub = sub1 - sub2
        print("-=" * 20)
        print("O resultado de {} - {} é {}".format(sub1, sub2, sub))
        print("-=" * 20)
        sleep(2)
    elif opção == 3:
        m1 = float(input("Primeiro valor: "))
        m2 = float(input("Segundo valor: "))
        mult = m1 * m2
        print("-=" * 20)
        print("{} * {} é {}".format(m1, m2, mult))
        print("-=" * 20)
        sleep(2)
    elif opção == 4:
        d1 = float(input("Primeiro valor: "))
        d2 = float(input("Segundo valor: "))
        divi = d1 / d2
        print("-=" * 20)
        print("{} dividido por {} é {}".format(d1, d2, divi))
        print("-=" * 20)
        sleep(2)
    elif opção == 5:
        di1 = float(input("Primeiro valor: "))
        di2 = float(input("Segundo valor: "))
        diviint = di1 // di2
        print("-=" * 20)
        print("A divisão inteira de {} com {} é {}".format(di1, di2, diviint))
        print("-=" * 20)
        sleep(2)
    elif opção == 6:
        rd1 = float(input("Primeiro valor: "))
        rd2 = float(input("Segundo valor: "))
        resto = rd1 % rd2
        print("-=" * 20)
        print("O resto da divisão de {} com {} é {}".format(rd1, rd2, resto))
        print("-=" * 20)
        sleep(2)
    elif opção == 7:
        ra1 = float(input("Informe o valor: "))
        raiz = math.sqrt(ra1)
        print("-=" * 20)
        print("A raiz quadrada de {} é {}".format(ra1, raiz))
        print("-=" * 20)
        sleep(2)
    elif opção == 8:
        fa1 = int(input("Digite o valor: "))
        fac = math.factorial(fa1)
        print("-=" * 20)
        print("O fatorial de {} é {}".format(fa1, fac))
        print("-=" * 20)
        sleep(2)
    elif opção == 9:
        e1 = int(input("Digite a base: "))
        e2 = int(input("Digite o expoente: "))
        elev = e1 ** e2
        print("-=" * 20)
        print("{} elevado a {} é {}".format(e1, e2, elev))
        print("-=" * 20)
        sleep(2)
    elif opção == 10:
        a = int(input("Qual o coeficiente de a? "))
        b = int(input("Qual o coeficiente de b? "))
        c = int(input("Qual o coeficiente de c? "))
        delta = b ** 2 - 4 * a * c
        while delta < 0:
            print("Não há raiz de numeros negativos.")
            break
        while delta >= 0:
            raizdelta = math.sqrt(delta)
            raizdelta1 = math.floor(raizdelta)
            x1 = (- b + raizdelta) / (2 * a)
            x2 = (- b - raizdelta) / (2 * a)
            print("-=" * 20)
            print("O valor de delta é {}".format(delta))
            print("O valor da raiz de delta é {}".format(raizdelta1))
            print("O valor de x1 é {:.4}".format(x1))
            print("O valor de x2 é {:.5}".format(x2))
            print("-=" * 20)
            break
        sleep(2)
    elif opção == 11:
        r1 = float(input("Digite um numero inteiro: "))
        raiz = r1 ** (1 / 3)
        print("A raiz cubica de {} é {}".format(r1, raiz))
    elif opção == 12:
        p = float(input("Digite um valor: "))
        p1 = p * 3.14
        print("-=" * 20)
        print("Valor de {} * PI é {}".format(p, p1))
        print("-=" * 20)
        sleep(2)
    elif opção == 13:
        opcao = 0
        while opção != 3:
            print('''    [ 1 ] Quadrado
    [ 2 ] Retangulo
    [ 3 ] Triângulo''')
            break
        opção = int(input("Digite sua opção: "))
        if opção == 1:
            n1 = float(input("Digite o lado: "))
            area = n1 ** 2
            print("A área do quadrado é de {}".format(area))
        elif opção == 2:
            n1 = float(input("Primeiro lado: "))
            n2 = float(input("Segundo lado: "))
            area = n1 * n2
            print("A área de {} * {} é {}".format(n1, n2, area))
        elif opção == 3:
            b = float(input("Digite a base: "))
            a = float(input("Digite a altura: "))
            area = b * a
            area1 = area / 2
            print("A área do triângulo é {}".format(area1))
        else:
            print("ok")
    elif opção == 14:
        opção = 0
        while opção != 4:
            print('''    
    [ 1 ] calcular 2 valores
    [ 2 ] calcular 3 valores
    [ 3 ] calcular 4 valores
    [ 4 ] calcular 5 valores''')
            break
        opção = int(input("Qual a sua opção? "))
        if opção == 1:
            n1 = float(input("Primeiro valor: "))
            n2 = float(input("Segundo valor: "))
            media = (n1 + n2) / 2
            print("-=" * 20)
            print("A média entre {} e {} é {}".format(n1, n2, media))
            print("-=" * 20)
            sleep(2)
        elif opção == 2:
            n1 = float(input("Primeiro valor: "))
            n2 = float(input("Segundo valor: "))
            n3 = float(input("Terceiro valor: "))
            media = (n1 + n2 + n3) / 3
            print("-=" * 20)
            print("A média entre {}, {} e {} é {}".format(n1, n2, n3, media))
            print("-=" * 20)
            sleep(2)
        elif opção == 3:
            n1 = float(input("Primeiro valor: "))
            n2 = float(input("Segundo valor: "))
            n3 = float(input("Terceiro valor: "))
            n4 = float(input("Quarto valor: "))
            media = (n1 + n2 + n3 + n4) / 4
            print("-=" * 20)
            print("A média entre {}, {}, {} e {} é {}".format(n1, n2, n3, n4, media))
            print("-=" * 20)
            sleep(2)
        elif opção == 4:
            n1 = float(input("Primeiro valor: "))
            n2 = float(input("Segundo valor: "))
            n3 = float(input("Terceiro valor: "))
            n4 = float(input("Quarto valor: "))
            n5 = float(input("Quinto valor: "))
            media = (n1 + n2 + n3 + n4 + n5) / 5
            print("-=" * 23)
            print("A média entre {}, {}, {}, {} e {} é {}".format(n1, n2, n3, n4, n5, media))
            print("-=" * 23)
            sleep(2)
        else:
            print("Opção Invalida tente novamente ")
            sleep(1)
    elif opção == 15:
        a = int(input("Qual o coeficiente de a? "))
        b = int(input("Qual o coeficiente de b? "))
        c = int(input("Qual o coeficiente de c? "))
        delta = b ** 2 - 4 * a * c
        print("-=" * 23)
        print("O valor de delta é {}".format(delta))
        if delta > 0:
            raizdelta = math.sqrt(delta)
            raizdelta1 = math.floor(raizdelta)
            x1 = (- b + raizdelta1) / (2 * a)
            x2 = (- b - raizdelta1) / (2 * a)
            print("O valor de x` é {}".format(x1))
            print("O valor de x`` é {}".format(x2))
            v1 = (- b) / (2 * a)
            v2 = (- delta) / (4 * a)
            print("O valor da vértice é (x){} e (y){}".format(v1, v2))
            sleep(2)
        elif delta == 0:
            raizdelta = math.sqrt(delta)
            raizdelta1 = math.floor(raizdelta)
            x1 = (- b + raizdelta1) / (2 * a)
            x2 = (- b - raizdelta1) / (2 * a)
            print("O valor de x` é {}".format(x1))
            print("O valor de x`` é {}".format(x2))
            v1 = (- b) / (2 * a)
            v2 = (- delta) / (4 * a)
            print("O valor da vértice é (x){} e (y){}".format(v1, v2))
            sleep(2)
        elif delta < 0:
            v1 = (- b) / (2 * a)
            v2 = (- delta) / (4 * a)
            print("O valor da vértice é (x){:.2} e (y){:.4}".format(v1, v2))
            sleep(2)
    elif opção == 16:
        opção = 0
        while opção != 10:
            print("Converter:")
            print('''    
    [ 1 ] Kilômetros
    [ 2 ] Metros
    [ 3 ] Centimetros
    [ 4 ] Milímetros
    [ 5 ] Litro
    [ 6 ] Mililitro
    [ 7 ] Gramas
    [ 8 ] Kilos
    [ 9 ] Toneladas
    [ 10 ] Voltar''')
            opção = int(input(("Qual a sua opção? ")))
            if opção == 1:
                print("-=" * 23)
                k = float(input("Quantos kilômetros deseja converter? "))
                print("-=" * 23)
                opção = 0
                while opção != 4:
                    print('''Converter "{}" kilômetros em:
    [ 1 ] Metros
    [ 2 ] Centímetros
    [ 3 ] Milímetros
    [ 4 ] Voltar'''.format(k))
                    opção = int(input("Qual a sua opção? "))
                    if opção == 1:
                        m = k * 1000
                        print("-=" * 23)
                        print("{} kilômetros são {} metros".format(k, m))
                        print("-=" * 23)
                        sleep(2)
                    elif opção == 2:
                        mi = k * 100000
                        print("-=" * 23)
                        print("{} kilômetros são {} centímetros".format(k, mi))
                        print("-=" * 23)
                        sleep(2)
                    elif opção == 3:
                        mili = k * 1e+6
                        print("-=" * 23)
                        print("{} kiÔmetros são {} milímetros".format(k, mili))
                        print("-=" * 23)
                        sleep(2)
                    elif opção == 4:
                        print()
                    else:
                        print("Opção inválida! Tente novamente.")
            elif opção == 2:
                m = float(input("Quantos metros deseja converter?"))
                opção = 0
                while opção != 4:
                    print('''Converter {} metros em:
    [ 1 ] Kilômetros
    [ 2 ] Centímetros
    [ 3 ] Milímetros
    [ 4 ] Voltar'''.format(m))
                    opção = int(input("Qual a sua opção? "))
                    if opção == 1:
                        k = m / 1000
                        print("{}  metros são {} kilômetros".format(m, k))
                    elif opção == 2:
                        c = m * 100
                        print("{} são {} centímetros".format(m, c))
                    elif opção == 3:
                        mili = m * 1000
                        print("{} são {} milímetros".format(m, mili))
                    elif opção == 4:
                        print()
                    else:
                        print("Opção inválida! Tente novamente.")
            elif opção == 3:
                c = float(input("Quantos centímetros deseja converter? "))
                opção = 0
                while opção != 4:
                    print('''Converter {} centímetros em:
    [ 1 ] Kilômetros
    [ 2 ] Metros
    [ 3 ] Milímetros
    [ 4 ] Voltar'''.format(c))
                    opção = int(input("Qual a sua opção? "))
                    if opção == 1:
                        k = c / 100000
                        print("{} centímetros são {} kilômetros".format(c, k))
                    elif opção == 2:
                        m = c / 100
                        print("{} centímetros são {} metros".format(c, m))
                    elif opção == 3:
                        mm = c * 10
                        print("{} centímetros são {} milímetros".format(c, mm))
                    elif opção == 4:
                        print()
                    else:
                        print("Opção inválida! Tente novamente. ")
            elif opção == 4:
                mm = float(input("Quantos milímetros deseja converter? "))
                opção = 0
                while opção != 4:
                    print('''Converter {} milímetros em:
    [ 1 ] Kilômetros
    [ 2 ] Metros
    [ 3 ] Centímetros
    [ 4 ] Voltar'''.format(mm))
                    opção = int(input("Qual a sua opção? "))
                    if opção == 1:
                        k = mm / 1e+6
                        print("{} milímetros são {} kilômetros".format(mm, k))
                    elif opção == 2:
                        m = mm / 1000
                        print("{} milímetros são {} metros".format(mm, m))
                    elif opção == 3:
                        c = mm / 10
                        print("{} milímetros são {} centímetros".format(mm, c))
                    elif opção == 4:
                        print()
                    else:
                        print("Opção inválida! Tente novamente. ")

            elif opção == 5:
                l = float(input("Quantos litros deseja converter? "))
                opção = 0
                while opção != 2:
                    print('''Converter {} litros em:
    [ 1 ] Mililitros
    [ 2 ] Voltar'''.format(l))
                    opção = int(input("Qual a sua opção? "))
                    if opção == 1:
                        ml = l * 1000
                        print("{} litros são {} mililitros".format(l, ml))
                    elif opção == 2:
                        print()
                    else:
                        print("Opção inválida! Tente novamente. ")
            elif opção == 6:
                ml = float(input("Quantos mililitros deseja converter? "))
                opção = 0
                while opção != 2:
                    print('''Converter {} mililitros em:
    [ 1 ] Litros
    [ 2 ] Voltar'''.format(ml))
                    opção = int(input("Qual a sua opção? "))
                    if opção == 1:
                        l = ml / 1000
                        print("{} mililitros são {} litros".format(ml, l))
                    elif opção == 2:
                        print()
                    else:
                        print("Opção inválida! Tente novamente. ")



            elif opção == 7:
                g = float(input("Quantas gramas deseja converter? "))
                opção = 0
                while opção != 3:
                    print('''Converter {} gramas em:
    [ 1 ] Toneladas
    [ 2 ] Kilos
    [ 3 ] Voltar'''.format(g))
                    opção = int(input("Qual a sua opção? "))
                    if opção == 1:
                        t = g / 1e+6
                        print("{} gramas são {} toneladas".format(g, t))
                    elif opção == 2:
                        k = g / 1000
                        print("{} gramas são {} kilos".format(g, k))
                    elif opção == 3:
                        print()
                    else:
                        print("Opção inválida! tente novamente.")



    else:
        print("Opção invalida")
        print("-=" * 20)
print("Fim do programa! Volte sempre.")
