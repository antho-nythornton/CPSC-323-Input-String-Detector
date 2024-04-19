def parser(input_string):
    stack = ['$']  # Initialize stack with '$'
    stack.append('E')  # Push start symbol 'E' onto stack
    input_index = 0

    


parsing_table = {
    'E': {'a': ['TQ'], '(': ['TQ']},
    'Q': {'+': ['+TQ'], '-': ['-TQ'], ')': ['ɛ'], '$': ['ɛ']},
    'T': {'a': ['FR'], '(': ['FR']},
    'R': {'*': ['*FR'], '/': ['/FR'], '+': ['ɛ'], '-': ['ɛ'], ')': ['ɛ'], '$': ['ɛ']},
    'F': {'a': ['a'], '(': ['(E)']}
}

# Test input strings
input_strings = [
    "(a+a) $",
    "(a+a) e $",
]