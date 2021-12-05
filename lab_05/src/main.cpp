#include <iostream>

#include "str.h"
#include "constants.h"
#include "conveyor.h"
#include "time_test.h"

using namespace std;

int main(void)
{
    bool process = true;
    int command;
    int count_src, len;

    while (process)
    {
        cout << endl << MSG;
        cin >> command;

        if ( command == LINEAR )
        {
            cout << "\nДлина строк: ";
            cin >> len;

            if ( len < 1 )
                cout << endl << "Неверная длина строк";

            cout << endl << "Число строк: ";
            cin >> count_src;

            if ( count_src < 1 )
                cout << endl << "Неверное число строк";

            linear_mode(count_src, len, PALINDROME);
        }
        else if ( command == PARALLEL )
        {
            cout << "\nДлина строк: ";
            cin >> len;

            if ( len < 1 )
                cout << endl << "Неверная длина строк";

            cout << endl << "Число строк: ";
            cin >> count_src;

            if ( count_src < 1 )
                cout << endl << "Неверное число строк";
            cout << endl;

            parallel_mode(count_src, len, PALINDROME);
        }
        else if ( command == TIME_LEN )
        {
            test_len();
        }
        else if ( command == TIME_COUNT_STR )
        {
            test_task_count();
        }
        else if ( command == FINISH )
        {
            process = false;
        }
        else
        {
            cout << endl << "Неверный пункт меню";
        }
    }
    return OK;
}
