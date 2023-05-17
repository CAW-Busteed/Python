#include <stdio.h>
#include <string.h>
#include <assert.h>

const char *hello()
{
    return "hik";
}

int main()
{
    assert(strcmp(hello(), "hi") == 0);
    return 0;
}
