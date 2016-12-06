/**
 * --- Day 1: Not Quite Lisp ---

Santa was hoping for a white Christmas,
but his weather machine's "snow" function
is powered by stars, and he's fresh out!
To save Christmas,
he needs you to collect fifty stars by December 25th.

Collect stars by helping Santa solve puzzles.
Two puzzles will be made available on each day in the advent calendar;
the second puzzle is unlocked when you complete the first.
Each puzzle grants one star. Good luck!

Here's an easy puzzle to warm you up.

Santa is trying to deliver presents in a large apartment building,
but he can't find the right floor -
the directions he got are a little confusing.
He starts on the ground floor (floor 0) and
then follows the instructions one character at a time.

An opening parenthesis, (, means he should go up one floor,
and a closing parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep;
he will never find the top or bottom floors.

For example:

(()) and ()() both result in floor 0.
((( and (()(()( both result in floor 3.
))((((( also results in floor 3.
()) and ))( both result in floor -1 (the first basement level).
))) and )())()) both result in floor -3.
To what floor do the instructions take Santa?

--- Part Two ---

Now, given the same instructions, find the position of the
first character that causes him to enter the basement (floor -1).
The first character in the instructions has position 1,
the second character has position 2, and so on.

For example:

) causes him to enter the basement at character position 1.
()()) causes him to enter the basement at character position 5.
What is the position of the character
that causes Santa to first enter the basement?*/


#include <stdio.h>


int main(int args, char **argv)
{
    FILE *fp;
    // Initial floor is the GROUND FLOOR
    int floors = 0;
    int i = 0;
    long basement_position = 0;
    char input = 'a';

    // Open file for reading
    fp = fopen("./input.txt", "r");
    // Read one character from file until EOF
    for(i=1; input!=EOF; i++) {
    // while((input=fgetc(fp)) != EOF) {
        input = fgetc(fp);
        // If (, go one floor up
        // If ), go one floor down
        // Else, ignore
        if (input == '(') {
            floors += 1;
        } else if (input == ')') {
            floors -= 1;
        } else {

        }

        // If the basement position has not been set,
        // check if the current floor is the basement
        // and save it if it is.
        // The index in enumeration starts from 0,
        // so we add 1 since the starting character position is 1.
        if (!basement_position) {
            if (floors == -1) {
                basement_position = i;
            }
        }
    }

    // Close the file
    fclose(fp);

    printf("Santa is at floor %d.", floors);
    printf("\nSanta reaches the basement at character %ld.", basement_position);

    return 0;
}
