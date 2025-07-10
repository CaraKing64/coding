#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* strnstr(char* string, char* key, int pos) {
  // initialise variables
  int string_size = strlen(string);
  int key_size = strlen(key);
  char* new_string = NULL;

  // iterate through each position in string
  for (int i = pos; i < string_size; i++) {
    char c = string[i];

    // check to see if key is located at this position in string
    int valid = 1;
    // check if each character in key lines up with the characters in string
    for (int j = 0; j < key_size; j++) {
      if (string[i + j] != key[j]) {
        valid = 0;
      }
    }

    // if the key is at this index
    if (valid == 1) {
      // allocate to a new array
      new_string = malloc(sizeof(char) * (string_size - i));
      for (int j = 0; j < (string_size - i); j++) {
        new_string[j] = string[i + j];
      }
      break;
    }
  }