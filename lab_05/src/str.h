#ifndef STR_H
#define STR_H

#include <iostream>
#include <string>
#include "stdlib.h"

#include "constants.h"

using namespace std;

void create_str(std::string& str, const int len, 
                const int is_palindrome);
void remove_spaces(std::string& str);
void change_register(std::string& str);
int check_palindrome(std::string& str);

#endif
