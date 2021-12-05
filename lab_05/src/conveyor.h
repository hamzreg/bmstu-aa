#ifndef CONVEYOR_H
#define CONVEYOR_H

#include <iostream>
#include <string>
#include <queue>
#include <thread>
#include <mutex>
#include <vector>
#include <chrono>
#include "stdio.h"

#include "str.h"

#define IN_SEC        1e9
#define COUNT_THREADS 3

void linear_mode(const int count, const int len,
                 const int is_palindrome);
void parallel_mode(const int count, const int len,
                 const int is_palindrome);

#endif
