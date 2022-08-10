# N-Queen-Problem

Find how many different ways are for queens to stand on chess board, so they wouldn't cross paths. Board can have blocked tiles.

---

## Task analysis

Each data file has a maximum of 10 test cases. Each case has an integer n (3 ≤ n ≤ 15) in the first row. The next n rows represent chess board, where empty cells are marked with dots '.' and blocked cells are marked with asterisks '*'. The last case is followed by a 0, at which the program must be stopped.

## Test samples

### First test

Input

        1
        .
        0

Output

        Case 1: 1
        Program finished

### Second test

Input

        8
        ........
        ........
        ........
        ........
        ........
        ........
        ........
        ........
        4
        .*..
        ....
        ....
        ....
        0

Output

        Case 1: 92
        Case 2: 1
        Program finished

### Third test

Input

        5
        ....*
        ...*.
        .....
        *...*
        ..*..
        5
        *****
        *****
        *****
        *****
        *****
        0

Output

        Case 1: 4
        Case 2: 0
        Program finished
