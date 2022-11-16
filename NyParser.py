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
pSaltos = []
paramCount = 0
tempCounter = 0
paramPtr = 0
callFunc = ''
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
    FUNCS : FUNC TYPE ID ADD_FUNC PARIZQ PARAMS PARDER LLVEIZQ func_jump ESTATUTO_P RETURN EXPRESION cuad_return PTOCOMA LLVEDER endFunc
          | FUNC VOID CURR_TYPE ID ADD_FUNC PARIZQ PARAMS PARDER LLVEIZQ func_jump ESTATUTO_P LLVEDER endFunc
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

def p_PARAMS(p):
    '''
    PARAMS : TYPE ID ADD_VAR update_param_table PARAMS_P
           | empty
    '''

def p_PARAMS_P(p):
    '''
    PARAMS_P : COMMA TYPE ID ADD_VAR update_param_table PARAMS_P
             | empty
    '''

def p_MAIN_G(p):
    '''
    MAIN_G : VOID MAIN change_func PARIZQ PARDER LLVEIZQ ESTATUTO_P LLVEDER endProg
    '''

def p_ESTATUTO(p):
    '''
    ESTATUTO : ASIGNACION
             | CONDICION
             | LOOP_WHILE
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
    CONDICION : IF PARIZQ EXPRESION PARDER ver_if LLVEIZQ ESTATUTO_P LLVEDER CONDICION_P
    '''

def p_CONDICION_P(p):
    '''
    CONDICION_P : ELSE else_jump LLVEIZQ ESTATUTO_P LLVEDER if_end
                | if_end
    '''

def p_LOOP_WHILE(p):
    '''
    LOOP_WHILE : WHILE add_jump PARIZQ EXPRESION PARDER ver_while LLVEIZQ ESTATUTO_P LLVEDER while_end
    '''

def p_ESCRITURA(p):
    '''
    ESCRITURA : PRINT PARIZQ PRINTABLE PARDER
    '''

def p_PRINTABLE(p):
    '''
    PRINTABLE : EXPRESION cuad_print PRINTABLE_P
              | CTE_STR cuad_print_str PRINTABLE_P
    '''

def p_PRINTABLE_P(p):
    '''
    PRINTABLE_P : COMMA PRINTABLE
                | empty
    '''

def p_FUNC_CALL(p):
    '''
    FUNC_CALL : ID ver_func_id_era PARIZQ PARM ver_param_num PARDER cuad_gosub 
    '''

def p_PARM(p):
    '''
    PARM : EXPRESION ver_param PARM_P
         | empty
    '''

def p_PARM_P(p):
    '''
    PARM_P : COMMA EXPRESION ver_param PARM_P
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
cte_string_addr = 37000

asigna_direccion = dir.Direcciones(global_int_addr, global_float_addr, global_char_addr, global_bool_addr, cte_string_addr)


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
    dirFunc[currentFunc] = {'type' : currentType, 'varsTable' : {}, 'paramTable' : [],'start_Address' : 0, 'memSize' : 0}

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
      dirFunc[currentFunc] = {'type' : currentType, 'varsTable' : {}, 'paramTable' : [], 'start_Address' : 0, 'memSize' : 0}
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
#    elif(idName in dirFunc['global']['varsTable']):
#        idType = dirFunc['global']['varsTable'][idName].get('type')
#        idAddress = dirFunc['global']['varsTable'][idName].get('address')
    else:
        print('Variable ' + idName + ' address not found in ' + currentFunc) 
        sys.exit()

    pOperands.append({'name' : idName, 'type' : idType, 'address' : idAddress})

def p_pila_operando_int(p):
    'pila_operando_int :'
    global currentFunc, pOperands, dirFunc, asigna_direccion, constTable
    idName = p[-1]
    addr = asigna_direccion.cte_var_addr('int')
    if(p[-1] not in constTable):
        constTable[idName] = { 'address' : addr, 'type' : 'int'}
    pOperands.append({'name' : idName, 'type' : 'int', 'address' : addr})

def p_pila_operando_float(p):
    'pila_operando_float :'
    global currentFunc, pOperands, dirFunc, asigna_direccion
    idName = p[-1]
    addr = asigna_direccion.cte_var_addr('float')
    if(p[-1] not in constTable):
        constTable[idName] = { 'address' : addr, 'type' : 'float'}
    pOperands.append({'name' : idName, 'type' : 'float', 'address' : addr})

def p_pila_operando_char(p):
    'pila_operando_char :'
    global currentFunc, pOperands, dirFunc, asigna_direccion
    idName = p[-1]
    addr = asigna_direccion.cte_var_addr('char')
    if(p[-1] not in constTable):
        constTable[idName] = { 'address' : addr, 'type' : 'char'}
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
    global pOperands, pOperators, cuboSemantico, cuadruplos, tempCounter
    if(len(pOperators) > 0):
        if(pOperators[-1] in op):
            right_operando = pOperands.pop()
            left_operando = pOperands.pop()
            operator = pOperators.pop()
            resType = cuboSemantico[left_operando['type']][right_operando['type']][operator]
            if(resType != 'err'):
                addr = asigna_direccion.temp_var_addr(resType)
                cuadruplos.append([operator, left_operando['address'], right_operando['address'], addr])
                pOperands.append({'address' : addr, 'name' : 'temp', 'type' : resType })
                tempCounter += 1
            else:
                print("Type Mismatch", right_operando['name'], right_operando['type'], left_operando['name'], left_operando['type'], operator)
                sys.exit()

def p_cuad_return(p):
    'cuad_return :'
    global pOperands, pOperators, cuboSemantico, cuadruplos, currentFunc, dirFunc
    ret = pOperands.pop()
    funcType = dirFunc[currentFunc]['type']
    if(ret['type'] == funcType):
        cuadruplos.append(['RET', '-', '-', ret['address']])
    else:
        print("Return must be same type as function")
        sys.exit()

def p_ver_if(p):
    'ver_if :'
    global pOperands, cuadruplos, pSaltos
    exp = pOperands.pop()
    if(exp['type'] != 'bool'):
        print("Expreson in IF statement needs to be boolean")
        sys.exit()
    else:
        cuadruplos.append(['GOTOF', exp['address'], '', ''])
        pSaltos.append(len(cuadruplos) - 1)

def p_if_end(p):
    'if_end :'
    global pSaltos, cuadruplos
    end = pSaltos.pop()
    cuadruplos[end][3] = len(cuadruplos)

def p_else_jump(p):
    'else_jump :'
    global pSaltos, cuadruplos
    cuadruplos.append(['GOTO', '', '', ''])
    false = pSaltos.pop()
    pSaltos.append(len(cuadruplos)-1)
    cuadruplos[false][3] = len(cuadruplos)

def p_add_jump(p):
    'add_jump :'
    global pSaltos, cuadruplos
    pSaltos.append(len(cuadruplos))

def p_ver_while(p):
    'ver_while :'
    global pSaltos, cuadruplos, pOperands
    exp = pOperands.pop()
    if(exp['type'] != 'bool'):
        print("resulting type of while expresion must be boolean")
        sys.exit()
    else:
        cuadruplos.append(['GOTOF', exp['address'], '', ''])
        pSaltos.append(len(cuadruplos)-1)


def p_while_end(p):
    'while_end :'
    global pSaltos, cuadruplos
    end = pSaltos.pop()
    ret = pSaltos.pop()
    cuadruplos.append(['GOTO', '', '', ret])
    cuadruplos[end][3] = len(cuadruplos)

def p_cuad_print(p):
    'cuad_print :'
    global pOperands, cuadruplos
    result = pOperands.pop()
    cuadruplos.append(['PRINT', '', '', result['address']])

def p_cuad_print_str(p):
    'cuad_print_str :'
    global pOperands, cuadruplos
    addr = asigna_direccion.cte_var_addr('string')
    constTable[p[-1]] = {'address' : addr, 'type' : 'string'}
    cuadruplos.append(['PRINT', '', '', addr])

def p_change_func(p):
    'change_func :'
    global currentFunc
    currentFunc = 'global'


##Function Declaration##
def p_update_param_table(p):
    'update_param_table :'
    global dirFunc, currentFunc, currentType, currentId, paramCount
    addr = dirFunc[currentFunc]['varsTable'][currentId].get('address')
    type = dirFunc[currentFunc]['varsTable'][currentId].get('type')
    dirFunc[currentFunc]['paramTable'].append([type, addr])
    paramCount += 1

def p_func_jump(p):
    'func_jump :'
    global dirFunc, cuadruplos, currentFunc, paramCount
    dirFunc[currentFunc]['start_Address'] = len(cuadruplos)
    dirFunc[currentFunc]['memSize'] += paramCount
    paramCount = 0
    #print(len(cuadruplos), "Numero de cuadruplos")
    
def p_endFunc(p):
    'endFunc :'
    global cuadruplos, currentFunc, dirFunc, tempCounter
    dirFunc[currentFunc]['memSize'] += tempCounter
    cuadruplos.append(['ENDFUNC', '', '' , ''])
    tempCounter = 0

##Function Call

def p_ver_func_id_era(p):
    'ver_func_id_era :'
    global dirFunc, cuadruplos, callFunc
    callFunc = p[-1]
    if(dirFunc.get(p[-1]) == None):
        print("Funcion ", p[-1], " no existe")
        sys.exit()
    else:
        size = dirFunc[p[-1]]['memSize']
        cuadruplos.append(['ERA', '', '', size])



def p_ver_param(p):
    'ver_param :'
    global pOperands, cuadruplos, callFunc, paramPtr, dirFunc
    arg = pOperands.pop()
    argType = arg.get('type')
    paramType = dirFunc[callFunc]['paramTable'][paramPtr][0]
    if(argType != paramType):
        print("Wrong argument type in function", callFunc, "call. Argument", paramPtr, "should be", paramType, "but", argType, "was given instead")
        sys.exit()
    else:
        paramAddr = dirFunc[callFunc]['paramTable'][paramPtr][1]
        argAddr = arg.get('address')
        cuadruplos.append(['PARAM', '',argAddr, paramAddr])
        paramPtr += 1

def p_ver_param_num(p):
    'ver_param_num :'
    global paramPtr , dirFunc, callFunc
    paramNum = len(dirFunc[callFunc]['paramTable'])
    if(paramNum != paramPtr):
        print("Wrong amount of arguments for func", callFunc, "call")
        sys.exit()

def p_cuad_gosub(p):
    'cuad_gosub :'
    global cuadruplos, callFunc, dirFunc
    dirIni = dirFunc[callFunc].get('start_Address')
    cuadruplos.append(['GOSUB', callFunc, '', dirIni]) 

#contador de variables temporales
#reiniciarlo al inicio de cada modulo


def p_endProg(p):
    'endProg :'
    global cuadruplos
    cuadruplos.append(['ENDPROG', '', '', ''])

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
