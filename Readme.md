# Lexicon Scanner

The Lexical Analyzer is responsible for separating the source code into lexemes, which are the words that compose the code. After separating all lexemes, the LA classifies them using Token classification. Keywords, Special Symbols, Identifiers and Operators, are examples of tokens. Removing white spaces and comments from the compiled code is also a role played by the Lexical Analyzer. The output of this process is a table containing the lexemes and their token classification.

## Recognize Tokens
The Lexical Analyzer of this project recognizes the following classes of tokens:
-Identifier 
-String Literal 
-Int Literal 
-Real Literal 
-Key words {"boolean", "break", "continue", "else", "for", "float", "if", "int", "return", "void", "while"} -Operator 
-Separator 

## Setup & Installation

Make sure you have the latest version of Python installed.

```bash
git clone https://github.com/nquang1417/LexiconScanner.git
```

```bash
pip install -r requirements.txt
```

## Running The App

```bash
python main.py
```

