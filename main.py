from Lexicalanalyzer import *
from syntaxanalyzer import grammar
'''
line_no = 1
condition=True
while (condition):
    print(f"{line_no}| ", end="")
    code=input()
    if code=="symbol table":
        symboltable()
    if code=="print grammar":
        print(grammar())
        break
    if code=="q":
        condition=False
    lexer(code,line_no)
    line_no+=1
'''
with open("code.simon", "r") as file:
    line_no = 1
    for code in file:
        code = code.strip()  # Remove any extra spaces or newlines
        print(f"{line_no}| {code}")
                
        # Only process lines that start with "simon says"
        if code == "symbol table":
            symboltable()
        elif code == "print grammar":
            print(grammar())
        elif code == "q":
            break
                
        # Call the lexer to process the line
        lexer(code, line_no)
        line_no += 1