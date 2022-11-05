import ply.yacc as yacc
import sys
import pprint

from NyLex import tokens


pOperands = []
pTypes = []
pOperators = []


#GRAMATICA
def p_PROGRAMA(p):
    '''
    PROGRAMA : PROGRAM CREATE_DIRFUNC ID PTOCOMA VARS_P FUNCS_P MAIN_G
    '''

def p_VARS(p):
    '''
    VARS : VAR TYPE ID ADD_VAR VARS_PP PTOCOMA
         | MAT TYPE ID CORIZQ CTE_INT CORDER VARS_PPP PTOCOMA
    '''

def p_VARS_P(p):
    '''
    VARS_P : VARS VARS_P
           | empty   
    '''

def p_VARS_PP(p):
    '''
    VARS_PP : COMMA ID ADD_VAR VARS_PP
            | empty
    '''

def p_VARS_PPP(p):
    '''
    VARS_PPP : CORIZQ CTE_INT CORDER
             | empty
    '''

def p_FUNCS(p):
    '''
    FUNCS : FUNC TYPE_P ID ADD_FUNC PARIZQ PARAMS PARDER LLVEIZQ ESTATUTO_P RETURN EXPRESION PTOCOMA LLVEDER
    '''

def p_FUNCS_P(p):
    '''
    FUNCS_P : FUNCS FUNCS_P
            | empty
    '''

def p_TYPE(p):
    '''
    TYPE : INT CURR_TYPE
         | FLOAT CURR_TYPE
         | BOOL CURR_TYPE
         | CHAR CURR_TYPE
    '''

def p_TYPE_P(p):
    '''
    TYPE_P : TYPE
           | VOID CURR_TYPE
    '''

def p_PARAMS(p):
    '''
    PARAMS : TYPE ID ADD_VAR PARAMS_P
           | empty
    '''

def p_PARAMS_P(p):
    '''
    PARAMS_P : COMMA TYPE ID ADD_VAR PARAMS_P
             | empty
    '''

def p_MAIN_G(p):
    '''
    MAIN_G : VOID MAIN PARIZQ PARDER LLVEIZQ ESTATUTO_P LLVEDER
    '''

def p_ESTATUTO(p):
    '''
    ESTATUTO : ASIGNACION
             | CONDICION
             | LOOP_FOR
             | ESCRITURA
             | FUNC_CALL   
    '''

def p_ESTATUTO_P(p):
    '''
    ESTATUTO_P : ESTATUTO ESTATUTO_P
               | empty
    '''

def p_ASIGNACION(p):
    '''
    ASIGNACION : ID ASIGN EXPRESION PTOCOMA
               | ID ASIGN FUNC_CALL
    '''

def p_CONDICION(p):
    '''
    CONDICION : IF PARIZQ EXPRESION PARDER LLVEIZQ ESTATUTO_P LLVEDER CONDICION_P
    '''

def p_CONDICION_P(p):
    '''
    CONDICION_P : ELSE LLVEIZQ ESTATUTO_P LLVEDER
                | empty
    '''

def p_LOOP_FOR(p):
    '''
    LOOP_FOR : FOR PARIZQ CTE_INT COMMA CTE_INT COMMA CTE_INT PARDER LLVEIZQ ESTATUTO_P LLVEDER
    '''

def p_ESCRITURA(p):
    '''
    ESCRITURA : PRINT PARIZQ PRINTABLE PRINTABLE_P PARDER
    '''

def p_PRINTABLE(p):
    '''
    PRINTABLE : EXPRESION
              | CTE_STR
    '''

def p_PRINTABLE_P(p):
    '''
    PRINTABLE_P : COMMA PRINTABLE PRINTABLE_P
                | empty
    '''

def p_FUNC_CALL(p):
    '''
    FUNC_CALL : ID PARIZQ PARM PARDER
    '''

def p_PARM(p):
    '''
    PARM : PARM_P
         | empty
    '''

def p_PARM_P(p):
    '''
    PARM_P : CTE_INT PARM_PP
           | CTE_FLT PARM_PP
           | ID PARM_PP
    '''

def p_PARM_PP(p):
    '''
    PARM_PP : COMMA PARM_P
             | empty
    '''

def p_EXPRESION(p):
    '''
    EXPRESION : EXPR EXPRESION_P
    '''

def p_EXPRESION_P(p):
    '''
    EXPRESION_P : OR EXPR
                | AND EXPR
                | empty
    '''

def p_EXPR(p):
    '''
    EXPR : EXP EXPR_P
    '''

def p_EXPR_P(p):
    '''
    EXPR_P : LT EXP
           | GT EXP
           | DIFF EXP
           | LTE EXP
           | GTE EXP
           | EQUAL EXP
           | empty
    '''

def p_EXP(p):
    '''
    EXP : TERM EXP_P
    '''

def p_EXP_P(p):
    '''
    EXP_P : MAS TERM EXP_P
          | MENOS TERM EXP_P
          | empty
    '''

def p_TERM(p):
    '''
    TERM : FACTOR TERM_P
    '''

def p_TERM_P(p):
    '''
    TERM_P : MULT  FACTOR TERM_P
           | DIV FACTOR TERM_P
           | empty
    '''

def p_FACTOR(p):
    '''
    FACTOR : PARIZQ EXPRESION PARDER
           | FACTOR_P VAR_CTE
    '''

def p_FACTOR_P(p):
    '''
    FACTOR_P : MAS
             | MENOS
             | empty
    '''

def p_VAR_CTE(p):
    '''
    VAR_CTE : ID
            | CTE_INT
            | CTE_FLT
    '''

def p_empty(p):
    'empty :'
    pass


def p_error(p):
    print("Syntax error in line " + str(p.lineno) + " " + str(p.value))
    sys.exit()

#DIRECCIONES DE MEMORIA VIRTUAL
GLOBAL_INT_ADDR = 5000
MODULE_INT_ADDR = 7000
CTE_INT_ADDR = 9000

GLOBAL_FLOAT_ADDR = 11000
MODULE_FLOAT_ADDR = 13000
CTE_FLOAT_ADDR = 15000

GLOBAL_BOOL_ADDR = 17000
MODULE_BOOL_ADDR = 19000
CTE_BOOL_ADDR = 21000

GLOBAL_CHAR_ADDR = 23000
MODULE_CHAR_ADDR = 25000
CTE_CHAR_ADDR = 27000

#ESPACIO DE MEMORIA DEFAULT DE TIPOS DE DATOS
INT_MEM_SIZE = 32
FLOAT_MEM_SIZE = 32
BOOL_MEM_SIZE = 8
CHAR_MEM_SIZE = 8

dirFunc = {}

currentId = ''
currentFunc = 'global'
currentType = 'void'

#PUNTOS NEURALGICOS
def p_CREATE_DIRFUNC(p):
    'CREATE_DIRFUNC :'
    global currentFunc, currentType
    dirFunc[currentFunc] = {'type' : currentType, 'symbolTable' : {}, 'start_Address' : 0, 'memSize' : 0}

def p_CURR_TYPE(p):
    'CURR_TYPE :'
    global currentType 
    currentType = p[-1]

def p_ADD_VAR(p):
    'ADD_VAR :'
    global currentId, currentType
    currentId = p[-1]
    if(dirFunc[currentFunc]['symbolTable'].get(currentId) == None):
       dirFunc[currentFunc]['symbolTable'][currentId] = {'name' : currentId, 'type' : currentType, 'address' : 0, 'size' : 0}
    else:
        print('multiple variables cannot have the same name in the same scope', currentId)
        sys.exit()

def p_ADD_FUNC(p):
    'ADD_FUNC :'
    global currentFunc, currentType
    currentFunc = p[-1]
    if(dirFunc.get(currentFunc) == None):
      dirFunc[currentFunc] = {'type' : currentType, 'symbolTable' : {}, 'start_Address' : 0, 'memSize' : 0}
    else:
        print('more than one function declared with ', currentFunc, ' name')
        sys.exit()

def p_ID_CUAD(p):
    'ID_CUAD :'
   # idName = p[-1]
   # idType = dirFunc[currentFunc]['symbolTable'][idName].get('type')
   # idAddress = dirFunc[currentFunc]['symbolTable'][idName].get('address')
   # pOperands.append({'idName' : idName, 'idType' : idType, 'idAddress' : idAddress})





parser = yacc.yacc()
f = open("./test1.txt", "r")
input = f.read()
print(input)
parser.parse(input)
pprint.pprint(dirFunc)


