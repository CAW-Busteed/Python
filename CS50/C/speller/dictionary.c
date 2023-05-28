// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <stdio.h>

#include "dictionary.h"

// Global variables and functions
int total_w;
int dic_count(const char *dictionary);

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table, each of which is a node pointer
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{

    // Hash table, each of which is a node pointer
    // node *table[N];
    int length = strlen(word);

    // RESult is the lowercase letters put together
    char *res = NULL;

    // set up a baseline to compare dict to (all lowercase)
    // TODO: maybe get rid of it, consider the apostrophes
    for (int i = 0; i < length; i++)
    {
        char des = tolower(word[i]);
        strncat(res, &des, 1);
    }
    int x = hash(res);

    node *current = table[x]->next;
    while (current != NULL)
    {
        if (strcasecmp(current->word, res) == 0)
        {
            // printf("found it!");
            return true;
        }
        current = current->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    total_w = dic_count(dictionary);

    FILE *doc;
    doc = fopen(dictionary, "r");

    if (dictionary != NULL)
    {
        for (int i = 0; i < total_w; i++) // hndle each word immediately, EOF
        {
            // make pointer and allocate size
            node *w;
            w = malloc(sizeof(node));

            char *text = malloc(sizeof(dictionary[i])); // won't take doc, maybe problem. used vari dictionary instead
            *text = dictionary[i];
            // malloc lots of bytes at a time and
            // add more every time we hit a block

            if (fscanf(doc, "%s", text) == true)
            {
                // append word to new node
                strcpy(w->word, text);
                // define link as the next in the hash
                // hash is defined so it should work off of the buckets (this should also catch the NULL)
                w->next = table[hash(text)]->next;
                // redefine hash's next link as the new node
                table[hash(text)]->next = w;
                free(text);
            }
            else
            {
                printf("scan failed");
                return false;
            }
        }
    }
    else
    {
        printf("no dictionary");
        return false;
    }
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    if (total_w != 0) // error because pointer and integer cannot be compared (total_w != NULL)
    {
        return total_w;
    }
    printf("No dictionary loaded");
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
// free all the nodes by
bool unload(void)
{
    node *del_cursor;
    node *temp;
    int verify = 0;

    for (int i = 0; i < N; i++)
    {
        del_cursor = table[i]->next; // or del_cursor->next = table[i]->next;
        while (del_cursor != NULL)
        {
            temp = del_cursor;
            del_cursor = del_cursor->next;
            free(temp);
        }
        verify++;
    }
    if (verify != N)
    {
        return false;
    }
    return true;
}

int dic_count(const char *dictionary)
{
    // s is the complete string of words, which we count from spaces
    char *s = NULL;
    int count = 0;

    scanf(dictionary, s);
    for (int i = 0; s[i] != '\0'; i++)
    {
        if (s[i] == ' ' || s[i] == '\t' || s[i] == '\n' || s[i] == '\0')
            count++;
        else if (strcmp(&s[i], "EOF") == 0) // necessary string compare function
            break;
    }
    free(s);
    return count;
}
