"""Given the following CFG and the parsing table, write a program to trace
input strings over { id, +, *, ), ( } and ending with $."""

stack = ['$', 'E']  # Stack is initialized with the start symbol and end marker.
input_string = "(id*)$"  # The input string with the end marker.



# The parsing table, represented as a dictionary of dictionaries.
parsing_table = {
    'E': {'id': 'T E1', '(': 'T E1'},
    'E1': {'+': '+ T E1', ')': '', '$': '', '*': ''},
    'T': {'id': 'F T1', '(': 'F T1'},
    'T1': {'+': '', '*': '* F T1', ')': '', '$': ''},
    'F': {'id': 'id', '(': '( E )'}
}

# The parsing algorithm.
while stack:
    top = stack[-1]
    if top in parsing_table:
        rule = parsing_table[top].get(input_string[0])
        if rule is not None:
            stack.pop()
            if rule:
                stack.extend(rule.split()[::-1])
        else:
            print('String is not accepted.')
            break
    else:
        if top == input_string[0]:
            stack.pop()
            input_string = input_string[1:]
        else:
            print('String is not accepted.')
            break
else:
    print('String is accepted.')
