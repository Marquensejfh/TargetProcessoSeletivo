
def pertence_a_fibonacci(numero):
    if numero < 0:
        return False
    
    # Função para gerar a sequência de Fibonacci até o valor máximo fornecido
    def gerar_fibonacci_ate(maximo):
        sequencia_fib = [0, 1]
        while True:
            proximo_fib = sequencia_fib[-1] + sequencia_fib[-2]
            if proximo_fib > maximo:
                break
            sequencia_fib.append(proximo_fib)
        return sequencia_fib
    
    # Gerar a sequência de Fibonacci até o valor de numero
    sequencia_fib = gerar_fibonacci_ate(numero)
    
    # Verificar se numero está na sequência gerada
    return numero in sequencia_fib

def main():
    try:
        numero = int(input("Informe um número: "))
        if pertence_a_fibonacci(numero):
            print(f"O número {numero} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {numero} não pertence à sequência de Fibonacci.")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    main()
