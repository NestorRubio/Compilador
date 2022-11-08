import ply.yacc as yacc
import sys
import pprint

from NySemantics import cuboSemantico 

from NyLex import tokens


pOperands = []
pOperators = []
constTable = {}


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
    EXPRESION_P : OR pila_operadores_add EXPR
                | AND pila_operadores_add EXPR
                | empty
    '''

def p_EXPR(p):
    '''
    EXPR : EXP EXPR_P
    '''

def p_EXPR_P(p):
    '''
    EXPR_P : LT pila_operadores_add EXP
           | GT pila_operadores_add EXP
           | DIFF pila_operadores_add EXP
           | LTE pila_operadores_add EXP
           | GTE pila_operadores_add EXP
           | EQUAL pila_operadores_add EXP
           | empty
    '''

def p_EXP(p):
    '''
    EXP : TERM  EXP_P
    '''

def p_EXP_P(p):
    '''
    EXP_P : MAS pila_operadores_add TERM EXP_P
          | MENOS pila_operadores_add TERM EXP_P
          | empty
    '''

def p_TERM(p):
    '''
    TERM : FACTOR TERM_P
    '''

def p_TERM_P(p):
    '''
    TERM_P : MULT pila_operadores_add FACTOR TERM_P
           | DIV pila_operadores_add FACTOR TERM_P
           | empty
    '''

def p_FACTOR(p):
    '''
    FACTOR : PARIZQ pila_operadores_add EXPRESION PARDER pila_operadores_add
           | FACTOR_P VAR_CTE
    '''

def p_FACTOR_P(p):
    '''
    FACTOR_P : MAS pila_operadores_add
             | MENOS pila_operadores_add
             | empty
    '''

def p_VAR_CTE(p):
    '''
    VAR_CTE : ID pila_operando_id
            | CTE_INT pila_operando_int
            | CTE_FLT pila_operando_float
            | CTE_CHAR pila_operando_char
    '''

def p_empty(p):
    'empty :'
    pass


def p_error(p):
    print("Syntax error in line " + str(p.lineno) + " " + str(p.value))
    sys.exit()

#DIRECCIONES DE MEMORIA VIRTUAL
global_int_addr = 5000
module_int_addr = 7000
cte_int_addr = 9000
temp_int_addr = 11000

global_float_addr = 13000
module_float_addr = 15000
cte_float_addr = 17000
temp_float_addr = 19000

global_bool_addr = 21000
module_bool_addr = 23000
temp_bool_addr = 25000

global_char_addr = 27000
module_char_addr = 29000
cte_char_addr = 31000
temp_char_addr = 33000

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
       dirFunc[currentFunc]['symbolTable'][currentId] = {'name' : currentId, 'type' : currentType, 'address' : 0, 'dim' : 0}
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

def p_pila_operando_id(p):
    'pila_operando_id :'
    global currentFunc, pOperands, dirFunc
    idName = p[-1]
    if(idName in dirFunc[currentFunc]['symbolTable']):     
        idType = dirFunc[currentFunc]['symbolTable'][idName].get('type')
        idAddress = dirFunc[currentFunc]['symbolTable'][idName].get('address')
    elif(idName in dirFunc['global']['symbolTable']):
        idType = dirFunc['global']['symbolTable'][idName].get('type')
        idAddress = dirFunc['global']['symbolTable'][idName].get('address')
    else:
        print('Variable ' + idName + ' address not found in global nor ' + currentFunc) 
        sys.exit()

    pOperands.append({'name' : idName, 'type' : idType, 'address' : idAddress})

def p_pila_operando_int(p):
    'pila_operando_int :'
    global currentFunc, pOperands, dirFunc
    idName = p[-1]
    pOperands.append({'name' : idName, 'type' : 'int', 'address' : 0})

def p_pila_operando_float(p):
    'pila_operando_float :'
    global currentFunc, pOperands, dirFunc
    idName = p[-1]
    pOperands.append({'name' : idName, 'type' : 'float', 'address' : 0})

def p_pila_operando_char(p):
    'pila_operando_char :'
    idName = p[-1]
    pOperands.append({'name' : idName, 'type' : 'char', 'address' : 0})

def p_pila_operadores_add(p):
    'pila_operadores_add :'
    operador = p[-1]
    pOperators.append(operador)

#def p_ver_exp_p(p):
#   if(str(pOperators[-1]) ==  )

parser = yacc.yacc()
f = open("./test1.txt", "r")
input = f.read()
print(input)
parser.parse(input)
pprint.pprint(dirFunc)
pprint.pprint(pOperands)
pprint.pprint(pOperators)

