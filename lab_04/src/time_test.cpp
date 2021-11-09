#include "time_test.h"

double measure_time(int order, int measure_type, int count_threads)
{
    /*
    * Замер времени.
    */

    std::chrono::time_point<std::chrono::system_clock> start, end;
    double result = 0;

    graph_t graph;
    init_graph(&graph);

    for (int i = 0; i < ITERS; i++)
    {
        graph.order = order;
        create_random_graph(&graph);

        if (measure_type == SINGLE)
        {
            start = std::chrono::system_clock::now();
            floyd(&graph);
            end = std::chrono::system_clock::now();

            result += (std::chrono::duration_cast<std::chrono::nanoseconds> 
            (end - start).count());
        }
        else if (measure_type == MULTI)
        {
            start = std::chrono::system_clock::now();
            multithreading(count_threads, &graph);
            end = std::chrono::system_clock::now();

            result += (std::chrono::duration_cast<std::chrono::nanoseconds> 
            (end - start).count());
        }

        cout << endl << i << " iter";
        free_graph(&graph);
    }

    result /= ITERS;

    return result / IN_SEC;
}

void write_in_file(int measure_type, int order, 
int count_threads, double time_result)
{
    /*
    * Запись результатов замеров в файл.
    */
    
    cout << endl << FILE_MSG;
    int choice;
    cin >> choice;

    if (choice == FILE_MULTI) 
    {
        ofstream fout(NAME_MULTI, ios_base::app);
        fout << to_string(measure_type) << " " << to_string(count_threads);
        fout << " " << to_string(order) << " " << to_string(time_result) << "\n";
        fout.close();
    }
    else if (choice == FILE_SINGLE)
    {
        ofstream fout(NAME_SINGLE, ios_base::app);
        fout << to_string(measure_type) << " " << to_string(count_threads);
        fout << " " << to_string(order) << " " << to_string(time_result) << "\n";
        fout.close();
    }
    else if (choice == FILE_ORDER_MULTI)
    {
        ofstream fout(NAME_ORDER_MULTI, ios_base::app);
        fout << to_string(measure_type) << " " << to_string(count_threads);
        fout << " " << to_string(order) << " " << to_string(time_result) << "\n";
        fout.close();
    }
    else if (choice == FILE_ORDER_SINGLE)
    {
        ofstream fout(NAME_ORDER_SINGLE, ios_base::app);
        fout << to_string(measure_type) << " " << to_string(count_threads);
        fout << " " << to_string(order) << " " << to_string(time_result) << "\n";
        fout.close();
    }
}

void test_count_threads()
{
    int measure_type = MULTI;
    int order = 150;
    
    for (int i = 1; i < 33; i++)
    {
        double result = measure_time(order, measure_type, i);
        cout << endl << "Полученное время = " << result << endl;

        ofstream fout(NAME_MULTI, ios_base::app);
        fout << to_string(measure_type) << " " << to_string(i);
        fout << " " << to_string(order) << " " << to_string(result) << "\n";
        fout.close();
    }
}

void test_order()
{
    int measure_type = MULTI;
    int count_threads = 4;
    
    for (int i = 100; i < 210; i += 10)
    {
        double result = measure_time(i, measure_type, count_threads);
        cout << endl << "Полученное время = " << result << endl;

        ofstream fout(NAME_ORDER_MULTI, ios_base::app);
        fout << to_string(measure_type) << " " << to_string(count_threads);
        fout << " " << to_string(i) << " " << to_string(result) << "\n";
        fout.close();
    }

    measure_type = SINGLE;
    count_threads = 1;

    for (int i = 100; i < 210; i += 10)
    {
        double result = measure_time(i, measure_type, count_threads);
        cout << endl << "Полученное время = " << result << endl;

        ofstream fout(NAME_ORDER_SINGLE, ios_base::app);
        fout << to_string(measure_type) << " " << to_string(count_threads);
        fout << " " << to_string(i) << " " << to_string(result) << "\n";
        fout.close();
    }
}
