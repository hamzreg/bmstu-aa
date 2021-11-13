#include <iostream>

using namespace std;

#include "graph_t.h"
#include "time_test.h"
#include "constants.h"


void single_threaded()
{
    /*
    * Однопоточный вариант.
    */

    graph_t graph;

    init_graph(&graph);
    
    if (input_graph(&graph))
        return;

    cout << endl << "Матрица смежности графа:" << endl;
    print_graph(&graph);

    floyd(&graph);
    cout << endl << "Матрица кратчайших путей графа:" << endl;;
    print_graph(&graph);

    free_graph(&graph);
}


void multi_threaded()
{
    /*
    * Многопоточный вариант.
    */

    graph_t graph;

    init_graph(&graph);

    if (input_graph(&graph))
        return;

    cout << endl << "Матрица смежности графа:" << endl;
    print_graph(&graph);

    cout << endl << "Введите число потоков:" << endl;
    int count_threads;
    cin >> count_threads;

    if (count_threads < 1)
    {
        cout << endl << "Неверное число потоков." << endl;
        free_graph(&graph);
        return;
    }

    multithreading(count_threads, &graph);
    cout << endl << "Матрица кратчайших путей графа:" << endl;;
    print_graph(&graph);

    free_graph(&graph);
}


int main(void)
{
    /*
    * Инициализация графа.
    */

    bool process = true;
    int command;
    int measure_type;
    int order;
    int count_threads = 1;

    while (process)
    {
        cout << endl << MSG;
        cin >> command;

        if (command == SINGLE)
        {
            single_threaded();
        }
        else if (command == MULTI)
        {
            multi_threaded();
        }
        else if (command == TIME_TEST)
        {
            cout << endl << TIME_MSG;
            cin >> measure_type;

            cout << endl << "Введите порядок графа: ";
            cin >> order;

            if (measure_type == MULTI)
            {
                cout << endl << "Введите число потоков:" << endl;
                cin >> count_threads;
            }
            else
                count_threads = 1;

            double result = measure_time(order, measure_type, count_threads);
            cout << endl << "Полученное время = " << result << endl;
            write_in_file(measure_type, order, count_threads, result);
        }
        else if (command == TEST1)
        {
            test_count_threads();
        }
        else if (command == TEST2)
        {
            test_order();
        }
        else
        {
            process = false;
        }
    }

    return OK;
}