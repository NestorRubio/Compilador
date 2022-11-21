import ply.lex as lex
import sys

#TOEKNS DEL LENGUAJE
tokens = [
    'PTOCOMA',
    'COMMA',
    'CORIZQ',
    'CORDER',
    'PARIZQ',
    'PARDER',
    'LLVEIZQ',
    'LLVEDER',
    'MAS',
    'MENOS',
    'MULT',
    'DIV',
    'GT',
    'GTE',
    'LT',
    'LTE',
    'DIFF',
    'EQUAL',
    'ASIGN',
    'AND',
    'OR',
    'ID',
    'CTE_INT',
    'CTE_FLT',
    'CTE_STR',
    'CTE_CHAR',
    'COMMENT'
]

#PALABRAS RESERVADAS DEL LENGUAJE
palabrasResv = {
    'program' : 'PROGRAM',
    'var' : 'VAR',
    'int' : 'INT',
    'float' : 'FLOAT',
    'char' : 'CHAR',
    'bool' : 'BOOL', 
    'void' : 'VOID',
    'return' : 'RETURN',
    'main' : 'MAIN',
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'print' : 'PRINT',
    'read' : 'READ',
    'func' : 'FUNC'
}

tokens += palabrasResv.values()

#REGLAS PARA LOS TOKENS

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in palabrasResv:
        t.type = palabrasResv[t.value]
    return t

def t_CTE_FLT(t):
    r'-?\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_CTE_INT(t):
    r'-?\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_CTE_STR(t):
    r'\"[^\"\~]*\"'
    return t

def t_CTE_CHAR(t):
    r'[a-zA-Z]'
    return t

def t_COMMENT(t):
    r'/\*[^*]*\*+(?:[^/*][^*]*\*+)*/'
    pass

#FUNCION PARA EL CONTEO DE LINEAS
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

#FUNCION PARA CARACTERES ILEGALES
def t_error(t):
    print("Illegal character %s on line %s" % (t.value[0], t.lexer.lineno))
    t.lexer.skip(1)
    sys.exit()
#REGLAS PARA SYMBOLOS

t_PTOCOMA = r'\;'
t_COMMA = r'\,'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_LLVEIZQ = r'\{'
t_LLVEDER = r'\}'
t_MAS = r'\+'
t_MENOS = r'\-'
t_MULT = r'\*'
t_DIV = r'\/'
t_GT = r'\>'
t_GTE = r'\>\='
t_LT = r'\<'
t_LTE = r'\<\='
t_DIFF = r'\!\='
t_EQUAL = r'\=\='
t_ASIGN = r'\='
t_AND = r'\&\&'
t_OR = r'\|\|'
t_ignore = " \t" #ignora todos los espacios en blanco

lexer = lex.lex()