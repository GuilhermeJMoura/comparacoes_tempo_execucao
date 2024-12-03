#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int main() {
    int N;
    printf("Digite o tamanho do vetor: ");
    scanf("%d", &N);

    // Alocação de memória
    int *vetor = (int*) malloc(N * sizeof(int));
    if (vetor == NULL) {
        printf("Erro na alocação de memória.\n");
        return 1;
    }

    // Preenchendo o vetor com valores aleatórios
    for (int i = 0; i < N; i++) {
        vetor[i] = rand() % 100;
    }

    int somatorio_total = 0;

    // Medir o tempo de execução
    double start_time = omp_get_wtime();

    // Paralelização com OpenMP
    #pragma omp parallel
    {
        int soma_parcial = 0;

        #pragma omp for
        for (int i = 0; i < N; i++) {
            soma_parcial += vetor[i];
        }

        #pragma omp atomic
        somatorio_total += soma_parcial;
    }

    double end_time = omp_get_wtime();

    // Exibindo o somatório total e o tempo de execução
    printf("Somatorio total: %d\n", somatorio_total);
    printf("Tempo de execucao: %f segundos\n", end_time - start_time);

    // Liberando memória alocada
    free(vetor);

    return 0;
}
