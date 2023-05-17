// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <assert.h>

#include "dictionary.h"

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
    int length = strlen(word);
    char *res[length];

    // set up a baseline to compare dict to (all lowercase)
    for (int i = 0; i < length; i++)
    {
        char des = tolower(word[i]);
        strncat(res, des, 1);
    }
    // TODO: figure out the best way to compare
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
    // TODO
    if (dictionary != NULL)
    {
        file = fopen(dictionary);
        while // hndle each word immediately, EOF
        {
            char *word = malloc(sizeof(dictionary[i])); // malloc lots of bytes at a time and add more every time we hit a block
            fscanf(dictionary, "%s", word);
            if (word == "EOF")
            {
                break;
            }
            else
            {
                h
            }
            free(word);
        }
    }
    return false;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    return false;
}
