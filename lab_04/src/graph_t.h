#ifndef GRAPH_T_H
#define GRAPH_T_H

#include <iostream>
using namespace std;

typedef struct
{
    int order;
    int **matrix;
} graph_t;

#define NOT_EXISTS  1
#define ORDER_ERROR 2
#define OK          0

#define MIN_ORDER   3
#define NO_WAY      -1

void init_graph(graph_t* graph);
int input_graph(graph_t* graph);
int print_graph(graph_t* graph);
int free_graph(graph_t* graph);

void floyd(graph_t* graph);

#endif
