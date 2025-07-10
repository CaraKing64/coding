#include <stdio.h>
#include <stdlib.h>

int main(void) {
  int n_grades;
  // get number of grades to be entered and check it is valid
  printf("How many grades to be entered: ");
  scanf("%d", &n_grades);
  if (n_grades <= 0) {
    printf("Please enter an amount of 1 or greater.\n");
    return 1;
  }

  int n_failures;

  // read all the grades into an array
  float* grade_array = malloc(sizeof(float) * n_grades);
  for (int i = 0; i < n_grades; i++) {
    float grade;
    printf("Enter a grade: ");
    scanf("%f", &grade);
    // check the grade is between 0 and 100
    while (grade < 0 || grade > 100) {
      printf("Invalid grade ignored\nEnter a grade: ");
      scanf("%f", &grade);
    }

    // count failure grades
    if (grade < 50) {
      n_failures++;
    }

    // assign grade to array
    grade_array[i] = grade;
  }

  // assign all failures to an array
  float* failure_array = malloc(sizeof(float) * n_failures);
  int j = 0;
  for (int i = 0; i < n_grades; i++) {
    float grade = grade_array[i];
    if (grade < 50) {
      failure_array[j] = grade;
      j++;
    }
  }

  // print all grades
  printf("You entered the grades: ");
  for (int i = 0; i < n_grades; i++) {
    printf("%.1f", grade_array[i]);
    if (i != n_grades - 1) {
      printf(", ");
    }
  }

  // print all failures
  printf("\nThe failed grades were: ");
  for (int i = 0; i < n_failures; i++) {
    printf("%.1f", failure_array[i]);
    if (i != n_failures - 1) {
      printf(", ");
    }
  }

  printf("\n");
  return 0;
}