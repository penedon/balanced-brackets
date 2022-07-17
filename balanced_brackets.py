#!/bin/python3

# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING brackets as parameter.
def isBalanced(string):
    """
    DESCRIPTION:
        - Check if the string brackets are balanced.
    PARAMS:
        - string: (str)
    RETURN:
        - 'YES' or 'NO': (str)
    """
    left_brackets = '{[('
    right_brackets = '}])'
    unbalanced = []
    
    for char in string:
        if char in left_brackets:
            unbalanced.append(char)
        elif unbalanced and char == right_brackets[left_brackets.index(unbalanced[-1])]:
            unbalanced.pop()
        else:
            break

    return 'YES' if len(unbalanced) == 0 else 'NO'


if __name__ == '__main__':

    t = int(input().strip())

    results = []
    for t_itr in range(t):
        brackets = input()

        results.append(isBalanced(brackets))

    print(*results, sep='\n')
