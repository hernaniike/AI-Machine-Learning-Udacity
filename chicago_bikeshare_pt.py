# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista

print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

#Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print('\nLinha 0: ')
print(data_list[0])

# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
#print(data_list[:20])
#Função imprimi os 20 primeiros linha por linha de forma mais organizada que a anterior.
linesum = 0
while linesum < 20:
    for line in data_list:
        print(line)
        linesum += 1
        if linesum > 20:
            break

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
#Função imprimi os 20 primeiros genêros.
gendersum = 0
while gendersum < 20:
    for line in data_list:
        if line[6] == '':
            print(f"Line {gendersum}: Gender: This line register don't have a gender")
            gendersum += 1
        else:
            print(f'Line {gendersum}: Gender: {line[6]}')
            gendersum += 1    
        if gendersum > 20:
            break

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
"""
      Função que coloca os dados de uma coluna em uma lista.
      Argumentos:
          data: variável que contém os dados a serem lidos.
          coluna: índice da coluna dentro da váriavel data.
      Retorna:
          Uma lista que contém os dados da coluna escolhida.
"""
def column_to_list(data, coluna):
    column_list = []
    for line in data:     
        #-- Solution changing '' for 'None'
        #if line[coluna] == '':
         #   line[coluna] = 'None'
          #  column_list.append(line[coluna])
        #else:
        column_list.append(line[coluna])
    return column_list

# Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.
#Para Cada linha da váriavel data_list ele análisa se a coluna do genero é male ou female e vai somando a contagem.
male = 0
female = 0
for line in data_list:
    if line[6] == 'Male' or line[6] == 'male':
        male += 1
    elif line[6] == 'Female' or line[6] == 'female':
        female += 1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
"""
      Função que conta os generos presentes no arquivo lido.
      Argumentos:
          data_list: variável que contem os dados a serem analisados.
      Retorna:
          Uma lista no formato [quantidade: male, quantidade: female].
"""
def count_gender(data_list):
    male = 0
    female = 0
    for line in data_list:
        if 'Male' in line[6]:
            male += 1
        elif 'Female' in line[6]:
            female += 1
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
"""
      Função que analisa qual genêro está mais presente nos dados analisados e retorna um texto.
      Argumentos:
          data_list: variável que contém os dados a serem lidos.
          Retorna: Um print com o resultado do maior genêro ou "Igual" no caso de empate.
"""
def most_popular_gender(data_list):
    if male > female:
        answer = "Masculino"
    elif male < female:
        answer = "Female"
    else:
        answer = "Igual"
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
"""
      Função que conta quantos usuários subscriber e customer existem e retorna uma lista.
      Argumentos:
          data_list: variável que contém os dados a serem lidos.
      Retorna:
          Uma lista que contém a quantidade dos usuários subscriber e customer.
"""
def count_user(data_list):
    Subscriber = 0
    Customer = 0
    for line in data_list:
        if 'Subscriber' in line[5]:
            Subscriber += 1
        elif 'Customer' in line[5]:
            Customer += 1

    return [Subscriber, Customer]

print("\nTAREFA 7: Verifique o gráfico!")
usertype_list = column_to_list(data_list, 5)[:20]
types = ["Subscriber", "Customer"]
usertype = count_user(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, usertype)
plt.ylabel('Quantidade')
plt.xlabel('Tipos')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo de Usuário')
plt.show(block=True)

input("Aperte Enter para continuar...")

# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque não existem apenas Males e Females na lista existem muitos ''. "
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------"""

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().
# cria uma lista de strings com os dados de tempo de uso da váriavel data_list função criada na tarefa 3.
trip_duration_list = column_to_list(data_list, 2)
"""
      Essa função faz várias coisas, soma a duração de viagem(trip) para tirar a média, verifica valores minimos e máximos da viagem,
      converte a lista de STR em lista de INT e ordena em ordem crescente.
      Argumentos:
            trip_duration_list: lista com os tempos de duração de aluguel em formato STR
      Retorna:
            lista[]: lista da lista(trip_duration_list) convertida de STR para INT
            elementmin: menor tempo de uso da bicicleta
            elementmax: maior tempo de uso da bicicleta
            trip_duration: soma de todos os tempos usados, para tirar a média de uso das bicicletas
"""
trip_duration = 0
elementmin = 99999
elementmax = 0
lista = []    
for element in trip_duration_list:
    element = int(element)
    trip_duration += element
    lista.append(element)
    if element < elementmin:
        elementmin = element
    if element > elementmax:
        elementmax = element
lista.sort()
"""
      Função que verifica se a lista é par ou impar para poder calcular a mediana.
      Argumentos:
          len(lista): tamanho da lista para verificar se é par ou ímpar
          se é par pega os 2 termos do meio soma e divide por 2
          se é impar pega o termo do meio e retorna no median_trip
      Retorna:
          median_trip: Um valor em float da mediana sendo a lista par ou ímpar 
"""
if len(lista) % 2 == 0:
    median_trip1 = lista[((int(len(lista) / 2) - 1))]
    median_trip2 = lista[((int(len(lista) / 2)))]
    median_trip = (median_trip1 + median_trip2) / 2
else:
    median_trip = lista[((int(len(lista) / 2)))]

min_trip = elementmin
max_trip = elementmax
mean_trip = round(trip_duration / len(lista))
print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
# Coloca em uma lista a coluna de estações iniciais.
start_stations_list = column_to_list(data_list, 3)
# Coloca a lista de estações dentro de um set, que não armazena estações repetidas, podendo contabilizar quantas estações existem.
user_types = set(start_stations_list)
print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
      
      #Função de exemplo com anotações.
      #Argumentos:
       #   param1: O primeiro parâmetro.
        #  param2: O segundo parâmetro.
      #Retorna:
       #   Uma lista de valores x.

# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.  
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

"""
      Função que transforma uma lista em set para pegar apenas os tipos existentes e conta quantos items existem nessa lista.
      Argumentos:
          column_list: Lista com os dados a serem analisados
      Retorna:
          item_types: Set da lista column_list, contém os tipos unicos.
          count_items: lista com o numero de tipos na lista, conta os repetidos também. 
"""
def count_items(column_list):
    item_types = set(column_list)
    count_items = []
    count = 0
    for item in column_list:
        count += 1
    count_items.append(count)
    return item_types, count_items
    

if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------