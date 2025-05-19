from Lexicalanalyzer import *
current_token_index = 0

def grammar():
    return """
        Statement → AssignmentStmt | IfStmt | IfElseStmt | IfElseElifStmt | ForLoop | WhileLoop
        AssignmentStmt → "simon" "says" "set" Datatype Identifier "=" value ";"
        Datatype → "int" | "string" | "float" | "bool"
        Identifier → [A-Za-z_]\\w*
        value → "\\"[^\\"]*\\"" | \d+
        IfStmt → "simon" "says" "if" "(" Datatype Identifier comparisonoperator value ")" "{" AssignmentStmt "}"
        comparisonoperator → "==" | "!=" | ">" | "<" | ">=" | "<="
        IfElseStmt → "simon" "says" "if" "(" Datatype Identifier comparisonoperator value ")" "{" AssignmentStmt "}" "else" "{" AssignmentStmt "}"
    """

def assignment_parser(tokens):
    try:
        match(tokens, "KEYWORD", "simon")
        match(tokens, "KEYWORD", "says")
        match(tokens, "KEYWORD", "set")
        match(tokens, "KEYWORD")
        match(tokens, "IDENTIFIER")
        match(tokens, "OPERATOR", "=")
        if tokens[current_token_index]['type'] == "STRING":
            match(tokens, "STRING")
        elif tokens[current_token_index]['type'] == "NUMBER":
            match(tokens, "NUMBER")
        else:
            raise SyntaxError("Expected a STRING or NUMBER value.")
        match(tokens, "PUNCTUATION", ";")
    except SyntaxError as e:
        print(f"Syntax Error in assignment: {e}")

def if_stmt_parser(tokens):
    # Parsing the "if" part
    match(tokens, "KEYWORD", "simon")
    match(tokens, "KEYWORD", "says")
    match(tokens, "KEYWORD", "if")
    match(tokens, "PUNCTUATION", "(")   # Opening parenthesis
    match(tokens, "KEYWORD")            # Datatype (int, string, float, bool)
    match(tokens, "IDENTIFIER")         # Identifier
    match(tokens, "OPERATOR")           # Comparison operator (==, !=, >, <, >=, <=)

    # Check if the value is a string, number, or identifier
    if tokens[current_token_index]['type'] == 'STRING':
        match(tokens, "STRING")         # String value
    elif tokens[current_token_index]['type'] == 'NUMBER':
        match(tokens, "NUMBER")         # Numeric value
    elif tokens[current_token_index]['type'] == 'IDENTIFIER':
        match(tokens, "IDENTIFIER")     # Identifier as a value
    else:
        print(f"syntax error error: Expected a STRING, NUMBER, or IDENTIFIER as value.")
        return

    match(tokens, "PUNCTUATION", ")")   # Closing parenthesis
    match(tokens, "PUNCTUATION", "{")   # Opening curly brace
    assignment_parser(tokens)           # Inside the "if" block - parsing a single assignment statement
    match(tokens, "PUNCTUATION", "}")   # Closing curly brace

def if_else_stmt_parser(tokens):
    # Parsing the "if" part
    match(tokens, "KEYWORD", "simon")
    match(tokens, "KEYWORD", "says")
    match(tokens, "KEYWORD", "if")
    match(tokens, "PUNCTUATION", "(")   # Opening parenthesis
    match(tokens, "KEYWORD")            # Datatype (int, string, float, bool)
    match(tokens, "IDENTIFIER")         # Identifier
    match(tokens, "OPERATOR")           # Comparison operator (==, !=, >, <, >=, <=)

    # Check if the value is a string, number, or identifier
    if tokens[current_token_index]['type'] == 'STRING':
        match(tokens, "STRING")         # String value
    elif tokens[current_token_index]['type'] == 'NUMBER':
        match(tokens, "NUMBER")         # Numeric value
    elif tokens[current_token_index]['type'] == 'IDENTIFIER':
        match(tokens, "IDENTIFIER")     # Identifier as a value
    else:
        print(f"syntax error error: Expected a STRING, NUMBER, or IDENTIFIER as value.")
        return

    match(tokens, "PUNCTUATION", ")")   # Closing parenthesis
    match(tokens, "PUNCTUATION", "{")   # Opening curly brace
    assignment_parser(tokens)           # Inside the "if" block - parsing a single assignment statement
    match(tokens, "PUNCTUATION", "}")   # Closing curly brace

    # Parsing the "else" part
    match(tokens, "KEYWORD", "else")    # Else keyword
    match(tokens, "PUNCTUATION", "{")   # Opening curly brace for else block
    assignment_parser(tokens)           # Inside the "else" block - parsing a single assignment statement
    match(tokens, "PUNCTUATION", "}")   # Closing curly brace


def match(tokens, expected_type, expected_value=None):
    global current_token_index
    
    # Boundary check to prevent IndexError
    if current_token_index >= len(tokens):
        print(f"Syntax Error: unexpected end of input.")
        return None

    token = tokens[current_token_index]
    if token['type'] != expected_type:
        print(f"Syntax Error: expected token of type '{expected_type}' but got '{token['type']}'")
        return None
    if expected_value and token["value"] != expected_value:
        print(f"Syntax Error: expected value '{expected_value}' but got '{token['value']}'")
        return None

    current_token_index += 1  
    return token

def parse_statement(tokens):
    try:
        # Determine the type of statement based on the first few tokens
        if len(tokens) >= 3 and tokens[0]['type'] == 'KEYWORD' and tokens[0]['value'] == 'simon' and \
           tokens[1]['type'] == 'KEYWORD' and tokens[1]['value'] == 'says':
            if tokens[2]['type'] == 'KEYWORD' and tokens[2]['value'] == 'if':
                # Parse as if 
                try:
                    if_stmt_parser(tokens)
                except:
                    if_else_stmt_parser(tokens)
            elif tokens[2]['type'] == 'KEYWORD' and tokens[2]['value'] == 'set':
                # Parse as assignment statement
                assignment_parser(tokens)
            print("Parsed successfully")
        else:
            raise SyntaxError("Unknown statement or syntax error.")
    except SyntaxError as e:
        print(f"Error while parsing statement: {e}")
