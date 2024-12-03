# Comparação Cupy, Threads e OpenMP - Guilherme Moura

| Código       | Linguagem    | Tamanho do Vetor     | Tempo de Execução do Somatório em Segundos |
|--------------|--------------|--------------|--------------|
| Cupy  | Python   | 100000000   | 0.6935608386993408   |
| Threads   | Python   | 100000000   |  1.001660 |
| OpenMP   | C  | 100000000   |  0.169000  |

## Conclusões:
- **Eficiência do OpenMP (C):**

    O OpenMP em C apresenta o menor tempo de execução (0,169 segundos), destacando-se como a solução mais eficiente para o somatório de um vetor de tamanho 100.000.000. Isso indica que implementações paralelas em linguagens compiladas podem ser significativamente mais rápidas do que suas contrapartes em linguagens interpretadas, como Python.
- **Threads em Python:**

    A abordagem com threads em Python levou 1,001 segundos, um desempenho inferior ao CuPy e ao OpenMP. Isso pode ser atribuído à presença do GIL (Global Interpreter Lock) no Python, que limita a execução paralela real em muitas situações, mesmo quando são utilizadas múltiplas threads.
- **CuPy (Python com GPU):**

    CuPy, que utiliza a GPU, apresentou um desempenho intermediário (0,694 segundos). Isso demonstra que soluções baseadas em GPU podem ser competitivas, mas sua eficiência depende de fatores como a complexidade da operação e a comunicação entre CPU e GPU.
