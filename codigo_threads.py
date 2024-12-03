import time
import _thread

# Define uma função que calcula a soma dos elementos de uma lista e armazena o resultado em uma lista de resultados
def calcular_soma(lista, resultados, index):
    soma_parcial = 0
    for num in lista:
        soma_parcial += num
    resultados[index] = soma_parcial

# Define o tamanho padrão da lista
TAMANHO_LISTA = 135

# Gera uma lista de números de 1 até TAMANHO_LISTA
lista_numeros = list(range(1, TAMANHO_LISTA + 1))

# Divide a lista em duas partes
meio_lista = len(lista_numeros) // 2
lista_numeros_1 = lista_numeros[:meio_lista]
lista_numeros_2 = lista_numeros[meio_lista:]

# Inicializa uma lista de resultados com duas posições, uma para cada thread
resultados = [0, 0]

# Captura o tempo antes do início das threads
start_time = time.time()

# Inicia duas threads que executam a função 'calcular_soma' para cada metade da lista
_thread.start_new_thread(calcular_soma, (lista_numeros_1, resultados, 0))
_thread.start_new_thread(calcular_soma, (lista_numeros_2, resultados, 1))

# Pausa a execução para garantir que as threads terminem (máximo 1 segundo nesse caso)
time.sleep(1)

# Captura o tempo após o término das threads
end_time = time.time()

# Calcula a soma total somando os resultados parciais de ambas as threads
soma_total = sum(resultados)

# Exibe os resultados e o tempo de execução
print("Soma total:", soma_total)
print(f"Tempo total de execução: {end_time - start_time:.6f} segundos")