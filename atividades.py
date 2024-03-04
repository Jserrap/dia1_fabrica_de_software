# Atividade fabrica 

def funcaoIdade():
    # recebe idade
    idade = input('Digite sua idade: ');
    # se for numerico, escreve idade, se não, escreve valor invalido
    if (idade.isnumeric()):
        print(f"sua idade é: {idade}");
    else:
        print('Valor inválido');

def somaMedia():
    acum = 0;
    # laço de repetição para não ter que escrever 5 inputs
    for i in range (1,6):
        # soma os valores de cada nota ao acumumlador
        acum += int(input(f"Digite a nota do aluno {i}: "));
    # escreve média
    print(acum/5);

def cincoTimes():
    # array que contem times
    times = ['Real Madrid', 'Manchester City',
    'Manchester United', 'Barcelona', 'Paysandu'];
    # Percorre o array imprimindo o conteudo de seus indices
    for time in times:
        print(time);

def maiorIdade():
    idade = input('Digite a idade: ');
    # se idade maior ou igual a 18, escreve maior de idade, caso não seja, escreve menor de idade
    if (idade >= 18):
        print('Maior de idade');
    else:
        print('Menor de idade');
        
def imparOuPar():
    # Recebe numero
    numero = float(input('Digite um número: '));
    # Operador ternario, se resto da divisão por 2 = 0 é par, se não, impar
    numero = 'par' if numero % 2 == 0 else 'Impar';
    print(numero);

def ePrimo():
    numero = int(input('Digite  um número: '));
    # cria array vazio
    divisores = [];
    
    # loop percorendo todos os numeros de 0 a ele mesmo, e vendo os divisiveis
    for i in range (1, numero):
        # se for divisivel entra no array de divisores
        if (numero % i == 0):
            divisores.append(i);
    
    # se o array for igual a um array que contenha apenas 1, é primo
    if (divisores == [1]):
        print('É primo');
    else:
        print('Não é primo');