// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <strings.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#include "dictionary.h"
#define N 26 // number of buckets in hash table

// Global variables and functions
int total_w = 0;
int dic_count(const char *dictionary);

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose
// const unsigned int N = 26;

// Hash table, each of which is a node pointer
node *table[N] = {NULL};

// Returns true if word is in dictionary, else false
bool check(const char *word)
{

    // Hash table, each of which is a node pointer
    // node *table[N];
    int length = strlen(word);

    // RESult is the lowercase letters put together. before, I used: char *res = NULL;
    // strncat expects a valid destination string, so you need to allocate memory for res before appending characters to it.
    char *res = malloc((length + 1) * sizeof(char));
    res[0] = '\0';

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
        for (int i = 0; i < total_w; i++) // handle each word immediately, EOF
        {
            // make pointer and allocate size
            node *w;
            w = malloc(sizeof(node));

            // dictionary[i] represents a character from the dictionary string and not the length of the string itself.
            // use strlen(dictionary) + 1 to allocate enough memory to store the word.
            // char *text = malloc(sizeof(dictionary[i]));
            //  *text = dictionary[i];
            char *text = malloc((strlen(dictionary) + 1) * sizeof(char));

            // check if it works
            // previously: if (fscanf(doc, "%s", text) == true)
            if (fscanf(doc, "%s", text) == 1)
            {
                // append word to new node
                strcpy(w->word, text);
                // define link as the next in the hash
                // hash is defined so it should work off of the buckets (this should also catch the NULL)
                w->next = table[hash(text)]->next; // TODO: segmentation fault
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

    // initialize table array with memory allocation
    for (int i = 0; i < N; i++)
    {
        table[i] = malloc(sizeof(node));
        table[i]->next = NULL;
    }

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
    // open file as doc
    FILE *doc;
    doc = fopen(dictionary, "r");

    // check to see if doc is available
    if (doc == NULL)
    {
        printf("Failed to open dictionary file");
        return 0;
    }

    // initialize count and go through document to count
    int count = 0;
    char word[LENGTH + 1];
    while (fscanf(doc, "%s", word) == 1)
    {
        count++;
    }
    fclose(doc);
    return count;
}

int main(void)
{
    FILE *doc;
    char word[N];
    doc = fopen("dictionaries/small.txt", "r");

    fgets(&word[0], N, doc);
    assert(word == "cat");
    // assert(load("dictionaries/small") == true);
}