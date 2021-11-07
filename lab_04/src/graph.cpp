#include "graph_t.h"

void init_graph(graph_t* graph)
{
    graph->order = 0;
    graph->matrix = nullptr;
}


int input_graph(graph_t* graph)
{
    cout << endl << "Введите порядок графа: ";
    cin >> graph->order;

    if (graph->order < MIN_ORDER)
    {
        cout << endl << "Порядок графа должен быть больше 3." << endl;
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
       }
    }

    return OK;
}


int print_graph(graph_t* graph)
{
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

void find_min_way(int **matrix, int i, int j, int k)
{
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

void floyd_multi_threaded(graph_t* graph)
{
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