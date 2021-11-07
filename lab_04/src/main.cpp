#include <iostream>

using namespace std;

#include "graph_t.h"
#include "constants.h"


void single_threaded()
{
    graph_t graph;

    init_graph(&graph);
    input_graph(&graph);

    cout << endl << "Матрица смежности графа:" << endl;
    print_graph(&graph);

    floyd(&graph);
    cout << endl << "Матрица кратчайших путей графа:" << endl;;
    print_graph(&graph);

    free_graph(&graph);
}


void multi_threaded()
{
    graph_t graph;

    init_graph(&graph);
    input_graph(&graph);

    cout << endl << "Матрица смежности графа:" << endl;
    print_graph(&graph);

    floyd(&graph);
    cout << endl << "Матрица кратчайших путей графа:" << endl;;
    print_graph(&graph);

    free_graph(&graph);
}


int main(void)
{
    bool process = true;
    int command;

    while (process)
    {
        cout << MSG;
        cin >> command;

        if (command == SINGLE)
        {
            single_threaded();
        }
        else if (command == MULTI)
        {
            multi_threaded();
        }
        else
        {
            process = false;
        }
    }

    return OK;
}