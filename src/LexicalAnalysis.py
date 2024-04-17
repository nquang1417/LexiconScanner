from LexicalScanner import LexicalScanner, LexicalType, Token

class LexicalAnalysis:
    def __init__(self):
        self.final_states = {
            1: LexicalType.IntLiteral,
            3: LexicalType.RealLiteral,
            4: LexicalType.RealLiteral,
            6: LexicalType.RealLiteral,
            10: LexicalType.StrLiteral,
            11: LexicalType.Identifier,
            12: LexicalType.Separator,
            13: LexicalType.Operator,
            14: LexicalType.Operator,
            15: LexicalType.Operator,
            16: LexicalType.Operator,
            18: LexicalType.Operator
        }
        self.transition_table = {
            0: {'number':1, '.':7, '"':9, 'letter':11, 'E':11, 'seporator':12, '+':13, '-':13, '*':13, '/':13, '<':14, '>':14, '!':14, '=':16, '|':17, '&':19},
            1: {'number':1, '.':2, 'E':4},
            2: {'number':3, 'E': 4},
            3: {'number':3, 'E':4},
            4: {'number':6, '+':5, '-':5},
            5: {'number':6},
            6: {'number':6},
            7: {'number':8},
            8: {'number':8, 'E':4},
            9: {'number':9, '.':9, '"':10, 'letter':9, 'E':9, 'seporator':9, '+':9, '-':9, '*':9, '/':9, '<':9, '>':9, '!':9, '=':9, '|':9, '&':9},
            11: {'number':11, 'letter':11, 'E':11},
            14: {'=':15},
            16: {'=':15},
            17: {'|':18},
            19: {'&':18}
        }
        self.current_state = 0
        self.starting_state = 0
        self.ending_states = []
        self.tokens = []
    
    def getToken(self,char):
        if LexicalScanner.isNumber(char):
            return 'number'
        elif LexicalScanner.isAlphatbet(char):
            if char == 'E' or char == 'e':
                return 'E'
            else:
                return 'letter'
        elif char == '.':
            return '.'
        elif char == '"':
            return '"'
        elif LexicalScanner.isSeparator(char):
            return 'seporator'
        elif LexicalScanner.isOperator(char):
            return char
        elif LexicalScanner.isEscape(char):
            return 'escape'
        elif char.isspace():
            return 'space'
        elif char == '?':
            return 'punctuation'
        else:
            return None
        
    def scan(self, input_string):
        words = []
        current_token = ''
        in_single_line_comment = False
        in_multi_line_comment = False

        for char_index, char in enumerate(input_string):
            # Skip comments
            if in_single_line_comment:
                if char == '\n':
                    in_single_line_comment = False
                continue
            elif in_multi_line_comment:
                if char == '/' and input_string[char_index - 1] == '*':
                    in_multi_line_comment = False
                continue
            elif char == '/' and input_string[char_index + 1] == '/':
                in_single_line_comment = True
                continue
            elif char == '/' and input_string[char_index + 1] == '*':
                in_multi_line_comment = True
                continue
            token = self.getToken(char)
            if self.current_state == 9 and token is not None:
                current_token += char
            
            if token is not None and self.current_state in self.transition_table and token in self.transition_table[self.current_state]:
                next_state = self.transition_table[self.current_state][token]
                if self.current_state != 9:
                    current_token += char
                self.current_state = next_state                              
            else:
                if self.current_state in self.final_states:
                    words.append(current_token)
                    if LexicalScanner.isKeyWord(current_token):
                        self.tokens.append(Token(LexicalType.Keyword, current_token))
                    else:
                        self.tokens.append(Token(self.final_states[self.current_state], current_token))
                    current_token = ''
                    self.current_state = 0
                if token is not None and token in self.transition_table[0]:
                    self.current_state = self.transition_table[0][token]
                    current_token = char                     
        return words
    
    def export(self, file_path):
        with open(file_path, 'w') as output_file:
            output_file.write(f'Starting State: {self.starting_state}\n')

            output_file.write('\nEnding States:\n')
            for key, value in self.final_states.items():
                output_file.write(f'{key} {value.name}\n')

            output_file.write('\nTransition Table:\n')
            for state, transition in self.transition_table.items():
                output_file.write(f'{state} ')
                for symbol, next_state in transition.items():
                    output_file.write(f' ({symbol} {next_state})')
                output_file.write('\n')

            output_file.write('\nEnding States - Words Mapping:\n')
            for token in self.tokens:
                output_file.write(f'{token.ending_state.name}: {token.value}\n')
        print(f"Kết quả đã được ghi vào tệp {file_path}")
            

            
            