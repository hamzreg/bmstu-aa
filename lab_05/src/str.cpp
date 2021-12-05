#include "str.h"

void create_str(std::string& str, const int len, 
                const int is_palindrome)
{
    const char alphabet[] =
               " abcdefghijklmnopqrstuwxyz"
               "ABCDEFGHIJKLMNOPQRSTUWXYZ";

    int size = len;

    if ( is_palindrome )
    {
        size = len / 2;
    }
    
    for ( int i = 0; i < size; ++i )
    {
        str.push_back(alphabet[rand() % (sizeof(alphabet) - 1)]);
    }

    if ( is_palindrome )
    {
        if ( len % 2 )
        {
            str.push_back(alphabet[rand() % (sizeof(alphabet) - 1)]);
        }
        
        for ( int i = 0; i < size; ++i)
        {
            str.push_back(str[size - i - 1]);
        }
    }
}


void remove_spaces(std::string& str)
{
    const char space = ' ';
    int len = str.length();

    for ( int i = 0; i < len; ++i )
    {
        if ( str[i] == space )
        {
            str.erase(i, 1);
            i--;
        }
    }
}


void change_register(std::string& str)
{
    int len = str.length();

    for ( int i = 0; i < len; ++i )
    {
        if ( str[i] >= 'A' && str[i] <= 'Z' )
        {
            str[i] += 32;
        }
        else if ( str[i] >= 'a' && str[i] <= 'z' )
        {
            str[i] -= 32;
        }
    }
}


int check_palindrome(std::string& str)
{
    int result = PALINDROME;
    int len = str.length();

    for ( int i = 0; i < len / 2; ++i )
    {
        if ( str[i] != str[len - i - 1] )
        {
            result = NOT_PALINDROME;
            break;
        }
    }

    return result;
}
