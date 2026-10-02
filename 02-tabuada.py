multiplicador = int(input('Digite o número\n'))
vezes_multiplicado = int(input('Digite a quantia de vezes que você deseja multiplicar\n'))
contador = 1

while (contador <= vezes_multiplicado) :
    resultado = (multiplicador * contador)
    print (f"{multiplicador} x {contador} = {resultado}")
    contador = contador +1