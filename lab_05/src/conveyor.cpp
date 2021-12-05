#include "conveyor.h"

double cur_time;

std::vector<double> cur_time1;
std::vector<double> cur_time2;
std::vector<double> cur_time3;


void linear_log(std::string& str, const int belt, const int task)
{
    std::chrono::time_point<std::chrono::system_clock> start, end;
    double result = 0;

    if ( belt == FIRST )
    {
        start = std::chrono::system_clock::now();
        remove_spaces(str);
        end = std::chrono::system_clock::now();
    }
    else if ( belt == SECOND )
    {
        start = std::chrono::system_clock::now();
        change_register(str);
        end = std::chrono::system_clock::now();
    }
    else if ( belt == THIRD )
    {
        start = std::chrono::system_clock::now();
        check_palindrome(str);
        end = std::chrono::system_clock::now();
    }

    result = (std::chrono::duration_cast<std::chrono::nanoseconds>(end - start).count()) / IN_SEC;
    printf("Tape: %d  Task: %d  Start Time: %.6f  End Time: %.6f\n", belt, task, cur_time, cur_time + result);
    cur_time += result;
}


void linear_mode(const int count, const int len,
                 const int is_palindrome)
{
    std::queue<std::string> q1;
    std::queue<std::string> q2;
    std::queue<std::string> q3;

    for ( int i =0; i < count; ++i )
    {
        std::string new_str;
        create_str(new_str, len, is_palindrome);

        q1.push(new_str);
    }

    cur_time = 0;

    for ( int i = 0; i < count; ++i )
    {
        std::string str = q1.front();
        linear_log(str, 1, i + 1);
        q2.push(str);
        q1.pop();

        str = q2.front();
        linear_log(str, 2, i + 1);
        q3.push(str);
        q2.pop();

        str = q3.front();
        linear_log(str, 3, i + 1);
        q3.pop();
    }

    //std::cout << "Time test:" << cur_time << endl;
}


void parallel_log(std::string& str, const int belt, const int task)
{
    std::chrono::time_point<std::chrono::system_clock> start, end;
    double result = 0, start_time;

    if ( belt == FIRST )
    {
        start = std::chrono::system_clock::now();
        remove_spaces(str);
        end = std::chrono::system_clock::now();
        result = (std::chrono::duration_cast<std::chrono::nanoseconds>(end - start).count()) / IN_SEC;

        start_time = cur_time1[task - 1];
        cur_time1[task] = start_time + result;
        cur_time2[task - 1] = cur_time1[task];
    }
    else if ( belt == SECOND )
    {
        start = std::chrono::system_clock::now();
        change_register(str);
        end = std::chrono::system_clock::now();
        result = (std::chrono::duration_cast<std::chrono::nanoseconds>(end - start).count()) / 1e9;

        start_time = cur_time2[task - 1];
        cur_time2[task] = start_time + result;
        cur_time3[task - 1] = cur_time2[task];
    }
    else if ( belt == THIRD )
    {
        start = std::chrono::system_clock::now();
        check_palindrome(str);
        end = std::chrono::system_clock::now();
        result = (std::chrono::duration_cast<std::chrono::nanoseconds>(end - start).count()) / IN_SEC;

        start_time = cur_time3[task - 1];
        cur_time3[task] = start_time + result;
    }

    
    printf("Tape: %d  Task: %d  Start Time: %.6f  End Time: %.6f\n", belt, task, start_time, start_time + result);
}


void first_belt(std::queue<std::string>& q1, std::queue<std::string>& q2)
{
    int task = 0;
    std::mutex m;

    while ( !q1.empty())
    {
        m.lock();
        std::string str = q1.front();
        m.unlock();

        parallel_log(str, 1, ++task);

        m.lock();
        q2.push(str);
        q1.pop();
        m.unlock();
    }
}


void second_belt(std::queue<std::string>& q1, std::queue<std::string>& q2, std::queue<std::string>& q3)
{
    int task = 0;
    std::mutex m;

    do
    {
        if ( !q2.empty() )
        {
            m.lock();
            std::string str = q2.front();
            m.unlock();

            parallel_log(str, 2, ++task);

            m.lock();
            q3.push(str);
            q2.pop();
            m.unlock();
        }
    } while ( !q1.empty() || !q2.empty() );
}


void third_belt(std::queue<std::string>& q1, std::queue<std::string>& q2, std::queue<std::string>& q3)
{
    int task = 0;
    std::mutex m;

    do
    {
        if ( !q3.empty() )
        {
            m.lock();
            std::string str = q3.front();
            m.unlock();

            parallel_log(str, 3, ++task);

            m.lock();
            q3.pop();
            m.unlock();
        }
    } while ( !q1.empty() || !q2.empty() || !q3.empty() );
}


void parallel_mode(const int count, const int len,
                 const int is_palindrome)
{
    std::queue<std::string> q1;
    std::queue<std::string> q2;
    std::queue<std::string> q3;

    for ( int i = 0; i < count; ++i )
    {
        std::string str;
        create_str(str, len, is_palindrome);

        q1.push(str);
    }
    
    for ( int i = 0; i < count + 1; ++i )
    {
        cur_time1.push_back(0);
        cur_time2.push_back(0);
        cur_time3.push_back(0);
    }

    std::vector<std::thread> threads(COUNT_THREADS);

    threads[0] = std::thread(first_belt, std::ref(q1), std::ref(q2));
    threads[1] = std::thread(second_belt, std::ref(q1), std::ref(q2), std::ref(q3));
    threads[2] = std::thread(third_belt, std::ref(q1), std::ref(q2), std::ref(q3));

    for ( int i = 0; i < COUNT_THREADS; ++i )
    {
        threads[i].join();
    }

    //std::cout << "Time test:" << cur_time3[count] << endl;
}
 