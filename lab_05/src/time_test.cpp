#include "time_test.h"


void test_len()
{
    int process_type;

    std::cout << TYPE_MSG;
    std::cin >> process_type;

    int count_str;

    std::cout << "\nЧисло строк : ";
    std::cin >> count_str;

    if ( process_type == LINEAR )
    {
        for ( int len = 20000; len < 31000; len += 1000 )
        {
            linear_mode(count_str, len, PALINDROME);
        }
    }
    else if ( process_type == PARALLEL ) 
    {
        for ( int len = 20000; len < 31000; len += 1000 )
        {
            parallel_mode(count_str, len, PALINDROME);
        }
    }
}


void test_task_count()
{
    int process_type;

    std::cout << TYPE_MSG;
    std::cin >> process_type;

    int len;

    std::cout << "\nДлина строк : ";
    std::cin >> len;

    if ( process_type == LINEAR )
    {
        for ( int count = 10; count < 60; count += 10 )
        {
            linear_mode(count, len, PALINDROME);
        }
    }
    else if ( process_type == PARALLEL ) 
    {
        for ( int count = 10; count < 60; count += 10 )
        {
            parallel_mode(count, len, PALINDROME);
        }
    }
}
