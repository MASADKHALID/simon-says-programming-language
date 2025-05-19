import re
#from syntaxanalyzer import parse_statement

# Define token patterns
token_specification = [
    ('KEYWORD',   r'\bsimon\b|\bsays\b|\bmain\b|\bdisplay\b|\bint\b|\bfloat\b|\bchar\b|\bstring\b|\bbool\b|\btrue\b|\bfalse\b|\blist\b|\bset\b|\bif\b|\belse\b|\belif\b|\bfor\b|\bwhile\b'),  # Keywords like int, float, char
    ('STRING',    r'"[^"]*"'),
    ('IDENTIFIER', r'[A-Za-z_]\w*'),              # Identifiers
    ('NUMBER', r'\d+(\.\d+)?')  ,                       # Integer numbers
    ('OPERATOR', r'==|!=|>=|<=|&&|\|\||\+\+|--|\+=|-=|\*=|/=|=|>|<|\+|-|\*|/'),                  # Operators
    ('PUNCTUATION', r'[;\[\]\{\},\(\)\'\"]'),    # Punctuation
    ('SKIP',      r'[ \t]+'),                    # Skip spaces and tabs
    ('MISMATCH',  r'.'),                         # Any other character
]
symbol_table=[]
tokens=[]
def symboltable():
    print(f"line no : class part : value part\n")
    for i in symbol_table:
        print(f"{i}\n")
def lexer(code,lineno):
    if not code.startswith("simon says"):
        return  # Considered as a comment, do not tokenize
    tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
    #print(tok_regex)
    # Use re.finditer() to match all patterns in the string
    for mo in re.finditer(tok_regex, code):
        #print(code)
        #print(mo)
        class_part = mo.lastgroup
        value_part = mo.group()
        if class_part == 'SKIP':
            continue
        # mismatch hae some some error so use alid words for checking
        elif class_part == 'MISMATCH': 
            raise RuntimeError(f'Unexpected character {value_part!r}')
        symbol_table.append(str(lineno)+" : "+class_part+" : "+value_part)
        tokens.append({'type': class_part, 'value': value_part})
    return symbol_table





