// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <strings.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#include "dictionary.h"
#define N 26 // number of buckets in hash table, consider constant integer

// Global variables and functions
int total_w = 0;
int dic_count(const char *dictionary);

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Hash table, each of which is a node pointer
node *table[N] = {NULL};

// Returns true if word is in dictionary, else false----------------------------------Not WAI
bool check(const char *word)
{
    int x = hash(word);

    node *current = table[x]->next;
    while (current != NULL)
    {
        int result = 0;
        printf("%s \n", word);
        printf("%s \n", current->word);
        // char *comparison = word;
        // char *
        result = strcasecmp(current->word, word);
        if (result == 0) //--------------------------------------------fails HERE
        {
            return true;
        }
        else
        {
            current = current->next;
        }
    }
    return false;
}

// Hashes word to a number-----------------------------------------------------WAI, for now
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false------------Potentially WAI
bool load(const char *dictionary)
{
    total_w = dic_count(dictionary);
    // assert(total_w == 5); //------------------------------------------------ works delete

    FILE *doc;
    char text[LENGTH]; // TODO:What if I want to reduce the text to its actual size to save space?
    doc = fopen(dictionary, "r");
    // assert(doc != 0); // ----------------------------------------------------works, delte

    if (dictionary != NULL)
    {
        // initialize table array with memory allocation(maybe put outside of function?)
        for (int i = 0; i < N; i++)
        {
            table[i] = malloc(sizeof(node));
            table[i]->next = NULL;
        }
        // // check if it works
        // if (fscanf(doc, "%s", text) != 1)
        // {
        //     printf("scan failed");
        //     return false;
        // }

        for (int i = 0; i < total_w; i++)
        {
            // make pointer and allocate size
            node *w = malloc(sizeof(node));
            // assert(w != NULL); // ------------------------------------works, delete

            fgets(text, LENGTH, doc);
            int cutoff = strcspn(text, "\n");
            text[cutoff] = 0;
            // assert(strcmp(text, "cat") == 0); // ----------------------works, delete

            // append word to new node and  define link as the next in the hash
            strcpy(w->word, text);
            w->next = table[hash(text)]->next;

            // redefine hash's next link as the new node
            table[hash(text)]->next = w;
            // assert(strcmp(table[2]->next->word, w->word) == 0); //  ---------------ASSERTION passed
        }
    }
    else
    {
        printf("no dictionary");
        return false;
    }
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded----------WAI
unsigned int size(void)
{
    if (total_w != 0)
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
    // initialize deletion node, temp node, and verfication to count totals
    node *del_cursor;
    node *temp;
    int verify = 0;

    for (int i = 2; i < N; i++) // TODO: correct i to 0 once assertions are done
    {
        // go through next in hash table. If there is something, temp stays, del moves on, free temp
        del_cursor = table[i]->next;                                     // del_cursor->next = table[i]->next;
        assert(strcasecmp(table[2]->next->word, del_cursor->word) == 0); //---------------------------------ASSERTION failed, why? it was identical!

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
    // assert(count == 4); // ASSERTION successful
    fclose(doc);
    return count;
}

int main(void)
{
    load("dictionaries/small");
    assert(strcasecmp(table[2]->next->next->word, "clamp") == 0); //--------------------------Assertion pass
    assert(size() == 5);                                          //-------------------------ASSERTION pass
    assert(check("clamp") == true);                               //-------------------------ASSERTION fail
    unload();
}
