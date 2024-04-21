def parser(input_string):
    stack = ['$']  # Initialize stack with '$'
    stack.append('E')  # Push start symbol 'E' onto stack
    input_index = 0
    top = stack[-1]
    output = None
    
    while stack:
        print("Stack:", stack, "Input:'" + input_string + "'", "Output:", top, "->", output)
        output = None
        top = stack[-1]
        input = input_string[input_index]
        if top == input:
            stack.pop()
            input_string = input_string[1:]
            continue
        elif top == 'ɛ':
            stack.pop()
            continue
        elif top in parsing_table and input in parsing_table[top]:
            output = parsing_table[top][input]
        else:
            return "String is not accepted/Invalid."
        stack.pop()
        stack.extend(reversed(output))

    
    if not stack and input_index == len(input_string):
        return "String is accepted/valid."
    else:
        return "String is not accepted/Invalid."


parsing_table = {
    'E': {'a': ['T','Q'], '(': ['T','Q']},
    'Q': {'+': ['+','T','Q'], '-': ['-','T','Q'], ')': ['ɛ'], '$': ['ɛ']},
    'T': {'a': ['F','R'], '(': ['F','R']},
    'R': {'*': ['*','F','R'], '/': ['/','F','R'], '+': ['ɛ'], '-': ['ɛ'], ')': ['ɛ'], '$': ['ɛ']},
    'F': {'a': ['a'], '(': ['(','E',')']}
}

# Test input strings
input_strings = [
    "(a+a)$",
    "(a+a)e$",
]

print("Test 01:",input_strings[0], parser(input_strings[0]))
print("Test 02:",input_strings[1], parser(input_strings[1]))