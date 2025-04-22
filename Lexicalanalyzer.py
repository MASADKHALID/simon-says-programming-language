import re

# Define token patterns
token_specification = [
    ('KEYWORD',   r'\bsimon\b|\bsays\b|\bprint\b|\bint\b|\bfloat\b|\bchar\b|\bstring\b|\bbool\b|\bset\b|\bif\b|\belse\b|\belif\b|\bfor\b|\bwhile\b'),  # Keywords like int, float, char
    ('STRING',    r'"[^"]*"'),
    ('IDENTIFIER', r'[A-Za-z_]\w*'),              # Identifiers
    ('NUMBER',    r'\d+'),                       # Integer numbers
    ('OPERATOR', r'==|!=|>=|<=|&&|\|\||\+\+|--|\+=|-=|\*=|/=|=|>|<|\+|-|\*|/'),                  # Operators
    ('PUNCTUATION', r'[;\[\]\{\},\(\)\'\"]'),    # Punctuation
    ('SKIP',      r'[ \t]+'),                    # Skip spaces and tabs
    ('MISMATCH',  r'.'),                         # Any other character
]
symbol_table=[]
def symboltable():
    print(f"line no : class part : value part\n")
    for i in symbol_table:
        print(f"{i}\n")
def lexer(code,lineno):
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
    return symbol_table

line_no = 1
condition=True
while (condition):
    print(f"{line_no}| ", end="")
    code=input()
    if code=="symbol table":
        symboltable()
    if code=="q":
        condition=False
    lexer(code,line_no)
    line_no+=1

