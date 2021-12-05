#ifndef TIME_TEST_H
#define TIME_TEST_H

#include <iostream>
#include "conveyor.h"

#define TYPE_MSG "Тип обработки:\n" \
                 "1. последовательный\n" \
                 "2. параллельный\n" \
                 "Выбор: "

#define LINEAR    1
#define PARALLEL  2

void test_len();

void test_task_count();

#endif
