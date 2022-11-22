import ply.yacc
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

dimVarAux = ''
dimCounter = 0


cuadruplos.append(['GOTO', '', '', ''])

############
#GRAMATICA#
###########

def p_PROGRAMA(p):
    '''
    PROGRAMA : PROGRAM CREATE_DIRFUNC ID PTOCOMA VARS_P FUNCS_P MAIN_G
    '''

def p_VARS(p):
    '''
    VARS : VAR TYPE ID ADD_VAR VARS_PP PTOCOMA
         | VAR TYPE ID ADD_VAR CORIZQ CTE_INT add_dim CORDER MAT_AUX actAddr PTOCOMA
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

def p_MAT_AUX(p):
    '''
    MAT_AUX : CORIZQ CTE_INT add_dim CORDER
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
    MAIN_G : VOID MAIN set_start change_func PARIZQ PARDER LLVEIZQ ESTATUTO_P LLVEDER endProg
    '''

def p_ESTATUTO(p):
    '''
    ESTATUTO : ASIGNACION
             | CONDICION
             | LOOP_WHILE
             | ESCRITURA
             | LECTURA 
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
               | VAR_DIM ASIGN pila_operadores_add EXPRESION cuad_asign PTOCOMA
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

def p_LECTURA(p):
    '''
    LECTURA : READ PARIZQ ID cuad_read PARDER
    '''

def p_FUNC_CALL(p):
    '''
    FUNC_CALL : ID ver_func_id_era PARIZQ fondo_falso_add PARM ver_param_num PARDER fondo_falso_pop cuad_gosub 
    '''

def p_FUNC_CALL_EXP(p):
    '''
    FUNC_CALL_EXP : ID ver_func_id_era_exp PARIZQ fondo_falso_add PARM ver_param_num PARDER fondo_falso_pop cuad_gosub
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
            | FUNC_CALL_EXP
            | VAR_DIM
    '''

##Invocacion de variables dimensionadas
def p_VAR_DIM(p):
    '''
    VAR_DIM : ID pila_operando_id CORIZQ ver_dim fondo_falso_add EXPRESION cuad_ver CORDER fondo_falso_pop matAux ver_dir_num cuad_var_dim
    '''

def p_matAux(p):
    '''
    matAux : CORIZQ ver_dim fondo_falso_add EXPRESION cuad_ver CORDER fondo_falso_pop
           | empty
    '''

def p_empty(p):
    'empty :'
    pass


def p_error(p):
    print("Syntax error in line " + str(p.lineno) + " " + str(p.value))
    sys.exit()

#################################
#DIRECCIONES DE MEMORIA VIRTUAL#
################################
global_int_addr = 5000
global_float_addr = 13000
global_char_addr = 21000
global_bool_addr = 29000
cte_string_addr = 37000

#Iniciiasion de generador de direcciones
asigna_direccion = dir.Direcciones(global_int_addr, global_float_addr, global_char_addr, global_bool_addr, cte_string_addr)


#ESPACIO DE MEMORIA DEFAULT DE TIPOS DE DATOS
INT_MEM_SIZE = 32
FLOAT_MEM_SIZE = 32
BOOL_MEM_SIZE = 8
CHAR_MEM_SIZE = 8

dirFunc = {} #Directorio de funciones

currentId = ''
currentFunc = 'global'
currentType = 'void'

##############################################
#PUNTOS NEURALGICOS Y FUNCIONES DE ASISTENCIA#
##############################################

#CREACION DE "GLOBAL" EN DIRECTORIO DE FUNCIONES
def p_CREATE_DIRFUNC(p):
    'CREATE_DIRFUNC :'
    global currentFunc, currentType
    dirFunc[currentFunc] = {'type' : currentType, 'varsTable' : {}, 'paramTable' : [],'start_Address' : 0, 'memSize' : 0}

#ACTUALIZACION DE TIPO ACTUAL FUNCION/VARIABLE
def p_CURR_TYPE(p):
    'CURR_TYPE :'
    global currentType 
    currentType = p[-1]

#AGREGA VARIABLES A VARSTABLE DE SU FUNCION RESPECTIVA
def p_ADD_VAR(p):
    'ADD_VAR :'
    global currentId, currentType, asigna_direccion
    currentId = p[-1]
    if(dirFunc[currentFunc]['varsTable'].get(currentId) == None): #VERIFICAR QUE VARIABLE NO EXISTA EN CONTEXTO ACTUAL
        if(currentFunc == 'global'):
            addr = asigna_direccion.global_var_addr(currentType)
        else:
            addr = asigna_direccion.module_var_addr(currentType)
        dirFunc[currentFunc]['varsTable'][currentId] = {'type' : currentType, 'address' : addr, 'dim' : []}
    else:
        print('multiple variables cannot have the same name in the same scope', currentId)
        sys.exit()

#DAR DE ALTA NUEVA FUNCION CON SU INFORMACION RESPECTIVA EN EL DIRFUNC
def p_ADD_FUNC(p):
    'ADD_FUNC :'
    global currentFunc, currentType, asigna_direccion
    currentFunc = p[-1]
    if(dirFunc.get(currentFunc) == None):
        if(dirFunc['global']['varsTable'].get(currentFunc) == None):
            dirFunc[currentFunc] = {'type' : currentType, 'varsTable' : {}, 'paramTable' : [], 'start_Address' : 0, 'memSize' : 0}
            addr = asigna_direccion.global_var_addr(currentType)
            dirFunc['global']['varsTable'][currentFunc] = {'type' : currentType, 'address' : addr, 'dim' : []}
        else:
            print("Functions cannot have same name as global variables")
            sys.exit()
    else:
        print('more than one function declared with ', currentFunc, ' name')
        sys.exit()

#AGREGA IDs A PILA DE OPERANDOS
#VARIABLE DEBE ESTAR DECLARADA EN SU CONTEXTO
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
        print('Variable ', idName, ' address not found in ', currentFunc, 'nor global') 
        sys.exit()

    pOperands.append({'name' : idName, 'type' : idType, 'address' : idAddress})

#AGREGA CONSTANTES INT A PILA DE OPERANDOS
def p_pila_operando_int(p):
    'pila_operando_int :'
    global currentFunc, pOperands, dirFunc, asigna_direccion, constTable
    idName = p[-1]
    if(p[-1] not in constTable):
        addr = asigna_direccion.cte_var_addr('int')
        constTable[idName] = { 'address' : addr, 'type' : 'int'}
    else:
        addr = constTable[idName].get('address')
    pOperands.append({'name' : idName, 'type' : 'int', 'address' : addr})

#AGREGA CONSTANTES FLOAT A PILA DE OPERANDOS
def p_pila_operando_float(p):
    'pila_operando_float :'
    global currentFunc, pOperands, dirFunc, asigna_direccion
    idName = p[-1]
    if(p[-1] not in constTable):
        addr = asigna_direccion.cte_var_addr('float')
        constTable[idName] = { 'address' : addr, 'type' : 'float'}
    else:
        addr = constTable[idName].get('address')
    pOperands.append({'name' : idName, 'type' : 'float', 'address' : addr})

#AGREGA CONSTANTES CHARS A PILA DE OPERANDOS
def p_pila_operando_char(p):
    'pila_operando_char :'
    global currentFunc, pOperands, dirFunc, asigna_direccion
    idName = p[-1]
    if(p[-1] not in constTable):
        addr = asigna_direccion.cte_var_addr('char')
        constTable[idName] = { 'address' : addr, 'type' : 'char'}
    else:
        addr = constTable[idName].get('address')
    pOperands.append({'name' : idName, 'type' : 'char', 'address' : addr})

#AGREGA OPERADORES A LA PILA DE OPERADORES
def p_pila_operadores_add(p):
    'pila_operadores_add :'
    operador = p[-1]
    pOperators.append(operador)

#AGREGA FONDO FALSO A PILA DE OPERADORES
def p_fondo_falso_add(p):
    'fondo_falso_add :'
    global pOperators
    pOperators.append('(')

#SACA EL FONDO FALSO DE PILA DE OPERADORES
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

#CREACION DE CUADRUPLO '='
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

#GENERADOR DE CUADRUPLOS DE EXPRESIONES ARITMETICAS, LOGICAS, Y BOOLEANAS
def cuad_gen(op):
    global pOperands, pOperators, cuboSemantico, cuadruplos, tempCounter, asigna_direccion
    if(len(pOperators) > 0):
        if(pOperators[-1] in op):
            right_operando = pOperands.pop()
            left_operando = pOperands.pop()
            operator = pOperators.pop()
            resType = cuboSemantico[left_operando['type']][right_operando['type']][operator]
            if(resType != 'err'):
                addr = asigna_direccion.temp_var_addr(resType)
                cuadruplos.append([operator, left_operando['address'], right_operando['address'], addr])
                pOperands.append({'name' : 'temp', 'type' : resType,'address' : addr })
                tempCounter += 1
            else:
                print("Type Mismatch", right_operando['name'], right_operando['type'], left_operando['name'], left_operando['type'], operator)
                sys.exit()

#GENERACION DEL CUADRUPLO DE LECTURA
def p_cuad_read(p):
    'cuad_read :'
    global dirFunc, currentFunc, cuadruplos
    if(dirFunc[currentFunc]['varsTable'].get(p[-1]) == None):
        print("Variable", p[-1], "that is being read does not exist in", currentFunc)
        sys.exit()
    else:
        addr = dirFunc[currentFunc]['varsTable'][p[-1]].get('address')
        cuadruplos.append(['READ', '', '', addr])

#GENERACION DEL CUADRUPLO DE RETURN
def p_cuad_return(p):
    'cuad_return :'
    global pOperands, pOperators, cuboSemantico, cuadruplos, currentFunc, dirFunc
    ret = pOperands.pop()
    funcType = dirFunc[currentFunc]['type']
    if(ret['type'] == funcType):
        cuadruplos.append(['RET', '', '', ret['address']])
    else:
        print("Return must be same type as function")
        sys.exit()

#CREACION DE CUADRUPLO PARA GOTOF PARA ESTATUTO-IF ASI COMO VERIFICACION DE TYPO DE RESULTADO DE EXPRESION
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

#ACTUALIZACION DE CUADRUPLO AL FINAL DE ESTATUTO-IF
def p_if_end(p):
    'if_end :'
    global pSaltos, cuadruplos
    end = pSaltos.pop()
    cuadruplos[end][3] = len(cuadruplos)

#ACTUALIZACION DE SALTO PARA CONTINUACION DESPUES DE ELSE
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

#GENERACION DE CUADRUPLO GOTOF PARA ESTATUTO-WHILE Y VERIFICACION DE TIPO DE EXPRESION 
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

#GENERACION DE CUADRUPLO DE REGRESO PARA ESTATUTO-WHILE
def p_while_end(p):
    'while_end :'
    global pSaltos, cuadruplos
    end = pSaltos.pop()
    ret = pSaltos.pop()
    cuadruplos.append(['GOTO', '', '', ret])
    cuadruplos[end][3] = len(cuadruplos)

#GENERACION DE CUADRUPLO PRINT PARA EXPRESIONES
def p_cuad_print(p):
    'cuad_print :'
    global pOperands, cuadruplos
    result = pOperands.pop()
    cuadruplos.append(['PRINT', '', '', result['address']])

#GENERACION DE CUADRUPLO PRINT PARA CTE STRINGS
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

############
#FUNCIONES#
##########

#ACTUALIZACION DE TABLA DE PARAMS(EN ORDEN) EN DIRFUNC
def p_update_param_table(p):
    'update_param_table :'
    global dirFunc, currentFunc, currentType, currentId, paramCount
    addr = dirFunc[currentFunc]['varsTable'][currentId].get('address')
    type = dirFunc[currentFunc]['varsTable'][currentId].get('type')
    dirFunc[currentFunc]['paramTable'].append([type, addr])
    paramCount += 1

#ACTUALIZACION DE DIRFUNC PARA INCLUIR LA DIRECCION DE INICIO ASI COMO EL NUMERO DE MEMORIA USADO(SUMA DE VARS)
def p_func_jump(p):
    'func_jump :'
    global dirFunc, cuadruplos, currentFunc, paramCount
    dirFunc[currentFunc]['start_Address'] = len(cuadruplos)
    dirFunc[currentFunc]['memSize'] += paramCount
    paramCount = 0
    #print(len(cuadruplos), "Numero de cuadruplos")
    
#GENERACION DE CUADRUPLO DE FIN DE FUNCION
def p_endFunc(p):
    'endFunc :'
    global cuadruplos, currentFunc, dirFunc, tempCounter, asigna_direccion
    dirFunc[currentFunc]['memSize'] += tempCounter
    cuadruplos.append(['ENDFUNC', '', '' , ''])
    tempCounter = 0
    asigna_direccion.reset_local_addr()


##Function Call - Estatuto

#VERIFICACION DE TIPO DE FUNCION COMO ESTATUTO
def p_ver_func_id_era(p):
    'ver_func_id_era :'
    global dirFunc, cuadruplos, callFunc
    callFunc = p[-1]
    if(dirFunc[callFunc].get('type') != 'void'):
        print("Lone function call must be made by a void function")
        sys.exit()
    if(dirFunc.get(p[-1]) == None):
        print("Funcion ", p[-1], " no existe")
        sys.exit()
    else:
        cuadruplos.append(['ERA', '', '', callFunc])

#VERIFICACION TIPO DE FUNCION COMO EXPRESION
def p_ver_func_id_era_exp(p):
    'ver_func_id_era_exp :'
    global dirFunc, cuadruplos, callFunc
    callFunc = p[-1]
    if(dirFunc[callFunc].get('type') == 'void'):
        print("Void function cannot be part of expresion")
        sys.exit()
    if(dirFunc.get(p[-1]) == None):
        print("Funcion ", p[-1], " no existe")
        sys.exit()
    else:
        cuadruplos.append(['ERA', '', '', callFunc])

#VERIFICAR TIPO DE PARAMETRO DE LLAMADA CON EL DECLARADO
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

#VERIFICACION DE NUMERO DE PARAMETROS
def p_ver_param_num(p):
    'ver_param_num :'
    global paramPtr , dirFunc, callFunc
    paramNum = len(dirFunc[callFunc]['paramTable'])
    if(paramNum != paramPtr):
        print("Wrong amount of arguments for func", callFunc, "call")
        sys.exit()

#GENERACION DE CUADRUPLO GOSUB
def p_cuad_gosub(p):
    'cuad_gosub :'
    global cuadruplos, callFunc, dirFunc, paramPtr, pOperands
    dirIni = dirFunc[callFunc].get('start_Address')
    cuadruplos.append(['GOSUB', '', '', callFunc])

    type = dirFunc['global']['varsTable'][callFunc].get('type')

    if(type != 'void'):
        dirResFuncCall = dirFunc['global']['varsTable'][callFunc].get('address')
        nextDir = asigna_direccion.temp_var_addr(type)
        cuadruplos.append(['=', dirResFuncCall, '', nextDir])
        pOperands.append({'name' : 'tempReturn', 'type' : type, 'address' : nextDir})

    paramPtr = 0 

##########################
#VARIABLES DIMENSIONADAS#
#########################

#DECLARACION DE VARIABLE DIMENSIONADA
def p_add_dim(p):
    'add_dim :'
    global dirFunc, currentFunc, currentId, constTable
    if(p[-1] <= 0):
        print("Array and Matrix delcaration index must be greater than 0")
        sys.exit()
    else:
        addr = asigna_direccion.cte_var_addr('int')
        dirFunc[currentFunc]['varsTable'][currentId]['dim'].append([p[-1]])
        if(p[-1] not in constTable):
            constTable[p[-1]] = { 'address' : addr, 'type' : 'int'}


#Funcion para el salto de direcciones al declarar variable dimensionada
def p_actAddr(p):
    'actAddr :'
    global dirFunc, currentFunc, currentId, currentType
    if(currentType == 'int' or currentType == 'float'):
        dim = len(dirFunc[currentFunc]['varsTable'][currentId]['dim'])
        size = 0
        val1 = dirFunc[currentFunc]['varsTable'][currentId]['dim'][0][0]
        if(dim == 2):
            val2 = dirFunc[currentFunc]['varsTable'][currentId]['dim'][1][0]
            size = val1 * val2
            asigna_direccion.next_addr_var_dim(currentType, size-1)
        elif(dim == 1):
            asigna_direccion.next_addr_var_dim(currentType, val1-1)
    else:
        print("Dimensioned Variables can only be int or float type")
        sys.exit()


def p_ver_dim(p):
    'ver_dim :'
    global dirFunc, pOperands, currentFunc, dimVarAux, dimCounter
    if(dimCounter == 0):
        top = pOperands.pop()
        dimVarAux = top.get('name')

    if(dirFunc[currentFunc]['varsTable'][dimVarAux]['dim'][dimCounter] == None):
        print("This variable does not have dimensions therefore cannot be indexed", dimVarAux)
        sys.exit()
    dimCounter = dimCounter + 1

def p_ver_dim_num(p):
    'ver_dir_num :'
    global dirFunc, dimVarAux, dimCounter, currentFunc
    if(len(dirFunc[currentFunc]['varsTable'][dimVarAux]['dim']) != dimCounter):
        print("Number of dimensions mismatch on variable", dimVarAux, "call")
        sys.exit()

def p_cuad_ver(p):
    'cuad_ver :'
    global pOperands, cuadruplos, dirFunc, constTable, currentFunc, dimCounter, dimVarAux
    top = pOperands[-1].get('address')
    val = dirFunc[currentFunc]['varsTable'][dimVarAux]['dim'][dimCounter-1][0]
    valAddr = constTable[val].get('address')
    cuadruplos.append(['VER', '', top, valAddr])

#
#   AQUI
#
#Cuadruplo para generar cuadruplo de direccion virtual de indexacion
def p_cuad_var_dim(p):
    'cuad_var_dim :'
    global dimCounter, pOperands, currentFunc, asigna_direccion, dirFunc, constTable, dimVarAux
    dirBase = dirFunc[currentFunc]['varsTable'][dimVarAux].get('address')
    type = dirFunc[currentFunc]['varsTable'][dimVarAux].get('type')

    if(dirBase not in constTable):
        addr = asigna_direccion.cte_var_addr('int')
        constTable[dirBase] = { 'address' : addr, 'type' : 'int'}

    if(dimCounter == 1):
        addr = constTable[dirBase].get('address')
        dim1 = pOperands.pop()
        addrPtrDir = asigna_direccion.pointer_var_addr(type)
        cuadruplos.append(['+', dim1.get('address'), addr, addrPtrDir])
        resDir = dim1.get('address') + addr
        pOperands.append({'name' : 'indexVal', 'type' : 'int', 'address' : addrPtrDir})    
    elif(dimCounter == 2):
        addr = constTable[dirBase].get('address')
        dim2 = pOperands.pop()
        dim1 = pOperands.pop()
        numCol = constTable[dirFunc[currentFunc]['varsTable'][dimVarAux]['dim'][1][0]].get('address')
        addrTempDir = asigna_direccion.temp_var_addr('int')
        cuadruplos.append(['*', dim1.get('address'), numCol, addrTempDir])
        addrTempDir2 = asigna_direccion.temp_var_addr('int')
        cuadruplos.append(['+', addrTempDir, dim2.get('address'), addrTempDir2])
        addrTempDir3 = asigna_direccion.pointer_var_addr(type)
        cuadruplos.append(['+', addrTempDir2, addr, addrTempDir3])
        resDir = (dim1.get('address') * numCol + dim2.get('address')) + addr
        pOperands.append({'name' : resDir, 'type' : 'int', 'address' : addrTempDir3})
    dimCounter = 0

#############
#INICIO-FIN#
###########

#ACTUALIZAR PRIMER CUADRUPLO PARA BRINCAR A MAIN
def p_set_start(p):
    'set_start :'
    global cuadruplos
    cuadruplos[0][3] = len(cuadruplos)

#CREACION DE CUADRUPLO PARA FINAL DE CODIGO
def p_endProg(p):
    'endProg :'
    global cuadruplos
    cuadruplos.append(['ENDPROG', '', '', ''])


parser = ply.yacc.yacc()

if __name__ == '__main__':

    fName = input()

    with open(fName, "r") as f:
        input = f.read()
        parser.parse(input)
        pprint.pprint(dirFunc)
        pprint.pprint(constTable)
        pprint.pprint(cuadruplos)
        print("Compiled Successfully")
        
        context = {'dirFunc' : dirFunc, 'constTable' : constTable, 'cuadruplos' : cuadruplos}
    with open(fName + ".o", "w") as f:
        f.write(str(context))
        
