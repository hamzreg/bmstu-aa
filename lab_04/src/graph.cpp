#include "graph_t.h"

void init_graph(graph_t* graph)
{
    /*
    * Инициализация графа.
    */

    graph->order = 0;
    graph->matrix = nullptr;
}


int input_graph(graph_t* graph)
{
    /*
    * Ввод матрицы смежности графа.
    */

    cout << endl << "Введите порядок графа: ";
    cin >> graph->order;

    if (graph->order < MIN_ORDER)
    {
        cout << endl << "Порядок графа должен быть больше 3." << endl;
        graph->order = 0;
        return ORDER_ERROR;
    }

    graph->matrix = new int* [graph->order];

    for (int i = 0; i < graph->order; i++)
    {
       (graph->matrix)[i] = new int[graph->order];
    }

    cout << endl << "Введите матрицу смежности графа:" << endl;

    for (int i = 0; i < graph->order; i++)
    {
       for (int j = 0; j < graph->order; j++)
       {
           cin >> graph->matrix[i][j];

           if (graph->matrix[i][j] < NO_WAY)
           {
               cout << endl << "Неверный вес ребра." << endl;
               free_graph(graph);
               return WEIGHT_ERROR;
           }
       }
    }

    return OK;
}


int print_graph(graph_t* graph)
{
    /*
    * Вывод матрицы смежности графа.
    */

    if (graph->order == 0)
    {
        cout << endl << "Граф не задан." << endl;
        return NOT_EXISTS; 
    }

    for (int i = 0; i < graph->order; i++)
    {
       for (int j = 0; j < graph->order; j++)
       {
           cout << graph->matrix[i][j] << " ";
       }

       cout << endl;
    }

    return OK;

}


int free_graph(graph_t* graph)
{
    /*
    * Освобождение памяти
    * матрицы смежности
    * графа.
    */

    if (graph->order == 0)
    {
        cout << endl << "Граф не задан." << endl;
        return NOT_EXISTS;
    }

    graph->order = 0;

    for (int i = 0; i < graph->order; i++)
    {
        delete [] graph->matrix[i];
    }

    delete [] graph->matrix;

    cout << endl << "Граф удален." << endl;

    return OK;
}


void create_random_graph(graph_t* graph)
{
    /*
    * Создание графа,
    * веса ребер которого - 
    * случайные целые числа.
    */

    srand(time(NULL));

    graph->matrix = new int* [graph->order];

    for (int i = 0; i < graph->order; i++)
    {
       (graph->matrix)[i] = new int[graph->order];
    }

    for (int i = 0; i < graph->order; i++)
    {
        for (int j = 0; j < graph->order; j++)
        {
            graph->matrix[i][j] = rand() % MAX_NUM;
        }
    }
}


void find_min_way(int **matrix, int i, int j, int k)
{
    /*
    * Нахождение кратчайшего пути\
    * между вершинами i и j.
    */

    if (i != j && matrix[i][k] != NO_WAY && matrix[k][j] != NO_WAY)
    {
        if (matrix[i][j] == NO_WAY)
            matrix[i][j] = matrix[i][k] + matrix[k][j];
        else
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j]);
    }
}

void floyd(graph_t* graph)
{
    /*
    * Алгоритм Флойда нахождения
    * кратчайших путей графа.
    */

    for (int k = 0; k < graph->order; k++)
    {
        for (int i = 0; i < graph->order; i++)
        {
            for (int j = 0; j < graph->order; j++)
            {
                find_min_way(graph->matrix, i, j, k);
            }
        }
    }
}

void parallel_floyd(graph_t* graph, int count_threads, int thread_index)
{
    /*
    * Параллельный алгоритм Флойда 
    * нахождения кратчайших путей графа.
    */

    cout << endl << "======== THREAD " << thread_index + 1 << " START" << endl;

    int step = graph->order / count_threads;
    int start = thread_index * step;

    if (thread_index + 1 == count_threads)
    {
        step += + (graph->order - step * count_threads);
    }

    for (int k = start; k < start + step; k++)
    {
        for (int i = 0; i < graph->order; i++)
        {
            for (int j = 0; j < graph->order; j++)
            {
                find_min_way(graph->matrix, i, j, k);
            }
        }
    }

    cout << endl << "======== THREAD " << thread_index + 1 << " END" << endl;
}

void multithreading(int count_threads, graph_t* graph)
{
    /*
    * Распараллеливание.
    */

    std::vector<std::thread> threads(count_threads);

    for (int i = 0; i < count_threads; i++)
    {
        threads[i] = std::thread(parallel_floyd, std::ref(graph), count_threads, i);
    }

    for (int i = 0; i < count_threads; i++)
    {
        threads[i].join();
    }
}
