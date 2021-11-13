#ifndef GRAPH_T_H
#define GRAPH_T_H

#include <iostream>
using namespace std;

#include <thread>
#include <chrono>
#include <vector>
#include <ctime>

typedef struct
{
    int order;
    int **matrix;
} graph_t;

#define NOT_EXISTS   1
#define ORDER_ERROR  2
#define WEIGHT_ERROR 3
#define OK           0

#define MIN_ORDER    3
#define NO_WAY      -1
#define MAX_NUM     20

void init_graph(graph_t* graph);
int input_graph(graph_t* graph);
int print_graph(graph_t* graph);
int free_graph(graph_t* graph);
void create_random_graph(graph_t* graph);

void floyd(graph_t* graph);
void parallel_floyd(graph_t* graph, int count_threads, int thread_index);
void multithreading(int count_threads, graph_t* graph);

#endif
