from enum import Enum

class Token:
    def __init__(self, state, value):
        self.ending_state = state
        self.value = value

class LexicalScanner:    
    KEYWORD = {"boolean", "break", "continue", "else", "for", "float", "if", "int", "return", "void", "while"}        
    OPERATOR = "&|+-*/%=<>!:"
    SEPARATOR = "[]{}(),;"
    ALPHABET = "abcdefghijklmnopqrstuvwxyz_QWERTYUIOPASDFGHJKLZXCVBNM"
    NUMBER = "0123456789"
    ESCAPE = {'\b', '\n', '\f', '\r', '\t', '\'', '\"', '\\'}

    @staticmethod
    def isKeyWord(token): 
        return token in LexicalScanner.KEYWORD
    
    @staticmethod
    def isNumber(char):
        return char in LexicalScanner.NUMBER
    
    @staticmethod
    def isAlphatbet(char):
        return char in LexicalScanner.ALPHABET
    
    @staticmethod
    def isSeparator(char):
        return char in LexicalScanner.SEPARATOR
    
    @staticmethod
    def isOperator(char):
        return char in LexicalScanner.OPERATOR
    
    @staticmethod
    def isExponent(char):
        return char == 'E' or char == 'e'
    
    @staticmethod
    def isEscape(char):
        return char in LexicalScanner.ESCAPE
    
    
class LexicalType(Enum):
    Identifier = 0
    Keyword = 1
    Operator = 2
    Separator = 3
    IntLiteral = 4
    RealLiteral = 5
    StrLiteral = 6
    Unknown = 7


