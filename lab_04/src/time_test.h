#ifndef TIME_TEST_H
#define TIME_TEST_H

#include <fstream>
#include <string>

#include "graph_t.h"
#include "constants.h"

#define ITERS  100
#define IN_SEC 1e9

#define NAME_MULTI        "time_multi.csv"
#define NAME_SINGLE       "time_single.csv"
#define NAME_ORDER_MULTI  "time_multi_order.csv"
#define NAME_ORDER_SINGLE "time_single_order.csv"

#define FILE_MULTI        1
#define FILE_SINGLE       2
#define FILE_ORDER_MULTI  3
#define FILE_ORDER_SINGLE 4

#define FILE_MSG "Выберите файл для записи:\n" \
                 "1. time_multi.csv\n" \
                 "2. time_single.csv\n" \
                 "3. time_multi_order.csv\n" \
                 "4. time_single_order.csv\n" \
                 "Выбор: "

double measure_time(int order, int measure_type, int count_threads);
void write_in_file(int measure_type, int order, 
                   int count_threads, double time_result);
void test_count_threads();
void test_order();
#endif