#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#define LENGTH 42

typedef struct node
{
    char word[LENGTH];
    struct node *next;
} node;

int main()
{
    char *str = "hello!";
    char *str0 = "howdy!";
    char *str1 = "bonjour!";

    // make node pointer n
    node *n;

    // allocates data size to pointer
    n = malloc(sizeof(node));

    // set member word of node to a string
    strcpy(n->word, str);
    n->next = NULL;

    // set up the node connecting to n
    node *m;
    m = malloc(sizeof(node));
    strcpy(m->word, str0);
    m->next = n;

    // and again!
    node *o;
    o = malloc(sizeof(node));
    strcpy(o->word, str1);
    o->next = m;

    printf("hello!");
}
