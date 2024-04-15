from enum import Enum

class Token:
    def __init__(self, type, value):
        self.lexicalType = type
        self.value = value

class LexicalScanner:    
    KEYWORD = {"boolean", "break", "continue", "else", "for", "float", "if", "int", "return", "void", "while"}
    OPERATOR = "&|+-*/%=<>!:"
    SEPARATOR = "[]{}(),;"
    ALPHABET = "abcdefghijklmnopqrstuvwxyz_QWERTYUIOPASDFGHJKLZXCVBNM"
    NUMBER = "0123456789"

    @staticmethod
    def isKeyWord(token): 
        return token in LexicalScanner.KEYWORD
    
    @staticmethod
    def isNumber(token):
        return token.isdigit() or LexicalScanner.isRealNumber(token)
    
    @staticmethod
    def isAlphatbet(token):
        return token.isalpha()
    
    @staticmethod
    def isSeparator(token):
        return token in LexicalScanner.SEPARATOR
    
    @staticmethod
    def isOperator(token):
        return token in LexicalScanner.OPERATOR
    
    @staticmethod
    def isRealNumber(token):
        has_dot = False
        for char in token:
            if not char.isdigit() and char != '.':
                return False
            if char == '.':
                if has_dot:
                    return False
                has_dot = True
        if not token or token[-1] == '.':
            return False
        return True
    
class LexicalType(Enum):
    Identifier = 0
    Keyword = 1
    Operator = 2
    Separator = 3
    IntLiteral = 4
    RealLiteral = 5
    StrLiteral = 6
    Unknown = 7


def scan(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    tokens = []

    current_token = ""
    in_single_line_comment = False
    in_multi_line_comment = False
    for char_index, char in enumerate(content):
        if in_single_line_comment:
            if char == '\n':
                in_single_line_comment = False
            continue
        elif in_multi_line_comment:
            if char == '*' and content[char_index + 1] == '/':
                in_multi_line_comment = False
            continue
        elif char == '/' and content[char_index + 1] == '/':
            in_single_line_comment = True
            continue
        elif char == '/' and content[char_index + 1] == '*':
            in_multi_line_comment = True
            continue

        if char.isspace() or char in LexicalScanner.SEPARATOR or char in LexicalScanner.OPERATOR:
            if current_token:
                if LexicalScanner.isKeyWord(current_token):
                    tokens.append(Token(LexicalType.Keyword, current_token))
                elif LexicalScanner.isNumber(current_token):
                    if '.' in current_token:
                        if LexicalScanner.isRealNumber(current_token): 
                            tokens.append(Token(LexicalType.RealLiteral, current_token))
                        else:
                            print("Unknown Token: ", current_token)
                    else:
                        tokens.append(Token(LexicalType.IntLiteral, current_token))
                elif LexicalScanner.isAlphatbet(current_token):
                    tokens.append(Token(LexicalType.Identifier, current_token))
                else:
                    print("Unknown Token: ", current_token)
                current_token = ""
            
            if char in LexicalScanner.SEPARATOR:
                tokens.append(Token(LexicalType.Separator, current_token))
            elif char in LexicalScanner.OPERATOR:
                tokens.append(Token(LexicalType.Operator, current_token))
        else:
            current_token += char

    return tokens


