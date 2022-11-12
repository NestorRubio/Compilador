import ply.yacc as yacc
import sys
import pprint

from NySemantics import cuboSemantico
import Direcciones as dir

from NyLex import tokens


pOperands = []
pOperators = []
constTable = {}
cuadruplos = []
tabla_var_dim = []


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
    FUNCS : FUNC TYPE_P ID ADD_FUNC PARIZQ PARAMS PARDER LLVEIZQ ESTATUTO_P RETURN EXPRESION cuad_return PTOCOMA LLVEDER
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
    ASIGNACION : ID pila_operando_id ASIGN pila_operadores_add EXPRESION cuad_asign PTOCOMA 
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
    EXPRESION : EXPRE cuad_or OR pila_operadores_add EXPRESION
              | EXPRE cuad_or 
    '''

def p_EXPRE(p):
    '''
    EXPRE : EXPR cuad_and AND pila_operadores_add EXPRE
          | EXPR cuad_and
    '''

def p_EXPR(p):
    '''
    EXPR : EXP cuad_comp EXPR_P
    '''

def p_EXPR_P(p):
    '''
    EXPR_P : LT pila_operadores_add EXPR
           | GT pila_operadores_add EXPR
           | DIFF pila_operadores_add EXPR
           | LTE pila_operadores_add EXPR
           | GTE pila_operadores_add EXPR
           | EQUAL pila_operadores_add EXPR
           | empty
    '''

def p_EXP(p):
    '''
    EXP : TERM cuad_sumres EXP_P
    '''

def p_EXP_P(p):
    '''
    EXP_P : MAS pila_operadores_add EXP
          | MENOS pila_operadores_add EXP
          | empty
    '''

def p_TERM(p):
    '''
    TERM : FACTOR cuad_muldiv TERM_P
    '''

def p_TERM_P(p):
    '''
    TERM_P : MULT pila_operadores_add TERM
           | DIV pila_operadores_add TERM
           | empty
    '''

def p_FACTOR(p):
    '''
    FACTOR : PARIZQ fondo_falso_add EXPRESION PARDER fondo_falso_pop
            | VAR_CTE
    '''

#def p_FACTOR_P(p):
#    '''
#    FACTOR_P : MAS pila_operadores_add
#             | MENOS pila_operadores_add
#             | empty
#    '''

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
global_float_addr = 13000
global_char_addr = 21000
global_bool_addr = 29000

asigna_direccion = dir.Direcciones(global_int_addr, global_float_addr, global_char_addr, global_bool_addr)


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
    dirFunc[currentFunc] = {'type' : currentType, 'varsTable' : {}, 'start_Address' : 0, 'memSize' : 0}

def p_CURR_TYPE(p):
    'CURR_TYPE :'
    global currentType 
    currentType = p[-1]

def p_ADD_VAR(p):
    'ADD_VAR :'
    global currentId, currentType, asigna_direccion
    currentId = p[-1]
    if(dirFunc[currentFunc]['varsTable'].get(currentId) == None):
        if(currentFunc == 'global'):
            addr = asigna_direccion.global_var_addr(currentType)
        else:
            addr = asigna_direccion.module_var_addr(currentType)
        dirFunc[currentFunc]['varsTable'][currentId] = {'name' : currentId, 'type' : currentType, 'address' : addr, 'dim' : 0}
    else:
        print('multiple variables cannot have the same name in the same scope', currentId)
        sys.exit()

def p_ADD_FUNC(p):
    'ADD_FUNC :'
    global currentFunc, currentType
    currentFunc = p[-1]
    if(dirFunc.get(currentFunc) == None):
      dirFunc[currentFunc] = {'type' : currentType, 'varsTable' : {}, 'start_Address' : 0, 'memSize' : 0}
    else:
        print('more than one function declared with ', currentFunc, ' name')
        sys.exit()

def p_pila_operando_id(p):
    'pila_operando_id :'
    global currentFunc, pOperands, dirFunc
    idName = p[-1]
    if(idName in dirFunc[currentFunc]['varsTable']):     
        idType = dirFunc[currentFunc]['varsTable'][idName].get('type')
        idAddress = dirFunc[currentFunc]['varsTable'][idName].get('address')
    elif(idName in dirFunc['global']['varsTable']):
        idType = dirFunc['global']['varsTable'][idName].get('type')
        idAddress = dirFunc['global']['varsTable'][idName].get('address')
    else:
        print('Variable ' + idName + ' address not found in global nor ' + currentFunc) 
        sys.exit()

    pOperands.append({'name' : idName, 'type' : idType, 'address' : idAddress})

def p_pila_operando_int(p):
    'pila_operando_int :'
    global currentFunc, pOperands, dirFunc, asigna_direccion, constTable
    idName = p[-1]
    addr = asigna_direccion.cte_var_addr('int')
    if(p[-1] not in constTable):
        constTable[p[-1]] = { 'address' : addr, 'type' : 'int'}
    pOperands.append({'name' : idName, 'type' : 'int', 'address' : addr})

def p_pila_operando_float(p):
    'pila_operando_float :'
    global currentFunc, pOperands, dirFunc, asigna_direccion
    idName = p[-1]
    addr = asigna_direccion.cte_var_addr('float')
    if(p[-1] not in constTable):
        constTable[p[-1]] = { 'address' : addr, 'type' : 'float'}
    pOperands.append({'name' : idName, 'type' : 'float', 'address' : addr})

def p_pila_operando_char(p):
    'pila_operando_char :'
    global currentFunc, pOperands, dirFunc, asigna_direccion
    idName = p[-1]
    addr = asigna_direccion.cte_var_addr('char')
    if(p[-1] not in constTable):
        constTable[p[-1]] = { 'address' : addr, 'type' : 'char'}
    pOperands.append({'name' : idName, 'type' : 'char', 'address' : addr})

def p_pila_operadores_add(p):
    'pila_operadores_add :'
    operador = p[-1]
    pOperators.append(operador)

def p_fondo_falso_add(p):
    'fondo_falso_add :'
    global pOperators
    pOperators.append('(')

def p_fondo_falso_pop(p):
    'fondo_falso_pop :'
    global pOperators
    if(pOperators[-1] == '('):
        pOperators.pop()
    else:
        print("parentheses mismatch")
        sys.exit()

def p_cuad_and(p):
    'cuad_and :'
    cuad_gen(['&&'])

def p_cuad_or(p):
    'cuad_or :'
    cuad_gen(['||'])


def p_cuad_comp(p):
    'cuad_comp :'
    cuad_gen(['>', '>=', '<', '<=', '!=', '=='])


def p_cuad_sumres(p):
    'cuad_sumres :'
    cuad_gen(['+', '-'])


def p_cuad_muldiv(p):
    'cuad_muldiv :'
    cuad_gen(['/', '*'])

def p_cuad_asign(p):
    'cuad_asign :'
    global pOperands, pOperators, cuboSemantico, cuadruplos, currentType, currentFunc
    operando = pOperands.pop()
    resType = operando['type']
    res = operando['address']
    idOp = pOperands.pop()
    idType = idOp['type']
    id = idOp['address']
    operator = pOperators.pop()
    asign_ver = cuboSemantico[idType][resType][operator]
    if(asign_ver != 'err' and operator == '='):
        cuadruplos.append([operator, res, '', id])
    else:
        print("Type mismatch", idOp['name'], idType, operando['name'], operando['type'], operator)
        sys.exit()


def cuad_gen(op):
    global pOperands, pOperators, cuboSemantico, cuadruplos
    if(len(pOperators) > 0):
        if(pOperators[-1] in op):
            right_operando = pOperands.pop()
            left_operando = pOperands.pop()
            operator = pOperators.pop()
            resType = cuboSemantico[left_operando['type']][right_operando['type']][operator]
            if(resType != 'err'):
                addr = asigna_direccion.temp_var_addr(resType)
                cuadruplos.append([operator, left_operando, right_operando, addr])
                pOperands.append({'address' : addr, 'name' : 'temp', 'type' : resType })
            else:
                print("Type Mismatch", right_operando['name'], right_operando['type'], left_operando['name'], left_operando['type'], operator)
                sys.exit()

def p_cuad_return(p):
    'cuad_return :'
    global pOperands, pOperators, cuboSemantico, cuadruplos, currentFunc, dirFunc
    ret = pOperands.pop()
    funcType = dirFunc[currentFunc]['type']
    if(ret['type'] == funcType):
        cuadruplos.append(['RET', '-', '-', ret])

parser = yacc.yacc()
f = open("./test1.txt", "r")
input = f.read()
print(input)
parser.parse(input)
pprint.pprint(dirFunc)
pprint.pprint(pOperands)
pprint.pprint(pOperators)
pprint.pprint(constTable)
pprint.pprint(cuadruplos)
