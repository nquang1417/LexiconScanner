from enum import Enum

class Token:
    def __init__(self, type, value):
        self.lexicalType = type
        self.value = value

class LexicalScanner:    
    KEYWORD = {"boolean", "break", "continue", "else", "for", "float", "if", "int", "return", "void", "while"}
    OPERATOR = {"+","-","*","/","=","==","!=","<", "<=",">",">=","||","&&","!"}    
    OPERATOR_CHARSET = "&|+-*/%=<>!:"
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
    words = []

    current_token = ""
    current_operator = ""
    in_single_line_comment = False
    in_multi_line_comment = False
    in_string = False
    str_content = ""
    start_operator = False
    for char_index, char in enumerate(content):
        if in_single_line_comment:
            if char == '\n':
                in_single_line_comment = False
            continue
        elif in_multi_line_comment:
            if char == '/' and content[char_index - 1] == '*':
                in_multi_line_comment = False
            continue
        elif char == '/' and content[char_index + 1] == '/':
            in_single_line_comment = True
            continue
        elif char == '/' and content[char_index + 1] == '*':
            in_multi_line_comment = True
            continue
        elif char == '"' and not (in_single_line_comment or in_multi_line_comment):
            str_content += char
            if in_string:
                if str_content:                
                    tokens.append(Token(LexicalType.StrLiteral, str_content))
                    words.append(str_content)
                str_content = ""
            in_string = not in_string            
            continue
                
        if in_string: 
            str_content += char
            continue
        
        if char.isspace() or char in LexicalScanner.SEPARATOR or char in LexicalScanner.OPERATOR_CHARSET:
            if current_token:
                if LexicalScanner.isKeyWord(current_token):
                    tokens.append(Token(LexicalType.Keyword, current_token))
                    words.append(current_token)                    
                elif LexicalScanner.isNumber(current_token):
                    if '.' in current_token:
                        if LexicalScanner.isRealNumber(current_token): 
                            tokens.append(Token(LexicalType.RealLiteral, current_token))
                            words.append(current_token)
                        else:
                            print("Unknown Token: ", current_token)
                    else:
                        tokens.append(Token(LexicalType.IntLiteral, current_token))
                        words.append(current_token)
                elif LexicalScanner.isAlphatbet(current_token):
                    tokens.append(Token(LexicalType.Identifier, current_token))
                    words.append(current_token)
                elif LexicalScanner.isOperator(current_token):
                    tokens.append(Token(LexicalType.Operator, current_token))
                    words.append(current_token)
                else:
                    print("Unknown Token: ", current_token)
                current_token = ""
            
            if char in LexicalScanner.SEPARATOR:
                tokens.append(Token(LexicalType.Separator, char))
                words.append(char)
            if char in LexicalScanner.OPERATOR_CHARSET:             
                current_operator += char                                                   
                if start_operator:
                    start_operator = False
                    tokens.append(Token(LexicalType.Operator, current_operator))
                    words.append(current_operator)  
                    current_operator = ""
                    continue
                if content[char_index + 1] in LexicalScanner.OPERATOR_CHARSET:
                    start_operator = True    
                    continue
                tokens.append(Token(LexicalType.Operator, current_operator))
                words.append(current_operator)  
                current_operator = ""
                
                    
        else:
            current_token += char

    return words


