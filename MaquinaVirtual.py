import sys
import types
import math

cuadruplos = []
dirFunc = {}
auxConstTable = {}
constTable = {}

currLevel = 0
breadCrumb = []
currentFunc = []

intMem = [{}]
floatMem = [{}]
boolMem = [{}]
charMem = [{}]

fName = input()

with open(fName, "r") as f:
    context = eval(f.read())
    cuadruplos = context['cuadruplos']
    dirFunc = context['dirFunc']
    auxConstTable = context['constTable']

#change key for address in var table
for key, info in auxConstTable.items():
    constTable[info['address']] = key

#def global_or_module(addr, currentFunc):
#    if((addr >= 7000 and addr < 9000) or (addr >= 15000 and addr < 17000) or (addr >= 23000 and addr < 25000) or (addr >= 31000 and addr < 33000)):
#        return 1
#    elif((addr >= 5000 and addr < 7000) or (addr >= 13000 and addr < 15000) or (addr >= 21000 and addr < 23000) or (addr >= 29000 and addr < 31000)):
#        return 0
#    elif(((addr >= 11000 and addr < 13000) or (addr >= 19000 and addr < 21000) or (addr >= 27000 and addr < 29000) or (addr >= 35000 and addr < 37000)) and currentFunc == 'global'):
#        return 0
#    elif(((addr >= 11000 and addr < 13000) or (addr >= 19000 and addr < 21000) or (addr >= 27000 and addr < 29000) or (addr >= 35000 and addr < 37000)) and currentFunc != 'global'):        
#        return 1

def update_memory(addr, val):
    address = int(addr)
    if(address >= 5000 and address < 13000):
        intMem[currLevel][address] = math.floor(val)
    elif(address >= 13000 and address < 21000):
        floatMem[currLevel][address] = val
    elif(address >= 21000 and address < 29000):
        charMem[currLevel][address] = val
    elif(address >= 29000 and address < 37000):
        boolMem[currLevel][address] = val


#Cuando se llegue al cuadruplo de endfunc en ejecucuion eleiminar nivel actual del dict

def get_val(addr, currentLevel):
    address = int(addr)
    if(address >= 5000 and address < 7000): #Int globales
        val = intMem[currentLevel][address]
    elif(address >= 7000 and address < 9000): #Int locales
        val = intMem[currentLevel][address]
    elif(address >= 9000 and address < 11000): #int cte
        val = constTable[address]
    elif(address >= 11000 and address < 13000): #Int temporales
        val = intMem[currentLevel][address]

    elif(address >= 13000 and address < 15000): #FLoat globales
        val = floatMem[currentLevel][address]
    elif(address >= 15000 and address < 17000): #float locales
        val = floatMem[currentLevel][address]
    elif(address >= 17000 and address < 19000): #float cte
        val = constTable[address]
    elif(address >= 19000 and address < 21000): #float temporales
        val = floatMem[currentLevel][address]

    elif(address >= 21000 and address < 23000): #char globales
        val = charMem[currentLevel][address]
    elif(address >= 23000 and address < 25000): #char locales
        val = charMem[currentLevel][address] 
    elif(address >= 25000 and address < 27000): #char cte
        val = constTable[address]
    elif(address >= 27000 and address < 29000): #char temporales
        val = charMem[currentLevel][address]

    elif(address >= 29000 and address < 31000): #bool global
        val = boolMem[currentLevel][address]
    elif(address >= 31000 and address < 33000): #bool local
        val = boolMem[currentLevel][address]
    elif(address >= 33000 and address < 35000): #bool cte
        val = constTable[address]
    elif(address >= 35000 and address < 37000): #bool temporales
        val = boolMem[currentLevel][address]

    elif(address >= 37000 and address < 39000): #CTE STRING - printables
        val = constTable[address]

    if(val is None):
        print("No assigned value to variable", addr)
        sys.exit()

    return val

currentCuad = 0

#print(globalMem)
#print(localMem)
#print(constTable)

while(cuadruplos[currentCuad][0] != 'ENDPROG'):

    if(cuadruplos[currentCuad][0] == 'GOTO'):
        currentCuad = cuadruplos[currentCuad][3]

    elif(cuadruplos[currentCuad][0] == '||'):
        leftOp = get_val(cuadruplos[currentCuad][1], currLevel)
        rightOp = get_val(cuadruplos[currentCuad][2], currLevel)
        result = leftOp or rightOp
        update_memory(cuadruplos[currentCuad][3], result)
        currentCuad = currentCuad + 1

    elif(cuadruplos[currentCuad][0] == '&&'):
        leftOp = get_val(cuadruplos[currentCuad][1], currLevel)
        rightOp = get_val(cuadruplos[currentCuad][2], currLevel)
        result = leftOp and rightOp
        update_memory(cuadruplos[currentCuad][3], result)
        currentCuad = currentCuad + 1

    elif(cuadruplos[currentCuad][0] == '<'):
        leftOp = get_val(cuadruplos[currentCuad][1], currLevel)
        rightOp = get_val(cuadruplos[currentCuad][2], currLevel)
        result = leftOp < rightOp
        update_memory(cuadruplos[currentCuad][3], result)
        currentCuad = currentCuad + 1
    
    elif(cuadruplos[currentCuad][0] == '>'):
        leftOp = get_val(cuadruplos[currentCuad][1], currLevel)
        rightOp = get_val(cuadruplos[currentCuad][2], currLevel)
        result = leftOp > rightOp
        update_memory(cuadruplos[currentCuad][3], result)
        currentCuad = currentCuad + 1

    elif(cuadruplos[currentCuad][0] == '!='):
        leftOp = get_val(cuadruplos[currentCuad][1], currLevel)
        rightOp = get_val(cuadruplos[currentCuad][2], currLevel)
        result = leftOp != rightOp
        update_memory(cuadruplos[currentCuad][3], result)
        currentCuad = currentCuad + 1

    elif(cuadruplos[currentCuad][0] == '<='):
        leftOp = get_val(cuadruplos[currentCuad][1], currLevel)
        rightOp = get_val(cuadruplos[currentCuad][2], currLevel)
        result = leftOp <= rightOp
        update_memory(cuadruplos[currentCuad][3], result)
        currentCuad = currentCuad + 1

    elif(cuadruplos[currentCuad][0] == '>='):
        leftOp = get_val(cuadruplos[currentCuad][1], currLevel)
        rightOp = get_val(cuadruplos[currentCuad][2], currLevel)
        result = leftOp >= rightOp
        update_memory(cuadruplos[currentCuad][3], result)
        currentCuad = currentCuad + 1

    elif(cuadruplos[currentCuad][0] == '=='):
        leftOp = get_val(cuadruplos[currentCuad][1], currLevel)
        rightOp = get_val(cuadruplos[currentCuad][2], currLevel)
        result = leftOp == rightOp
        update_memory(cuadruplos[currentCuad][3], result)
        currentCuad = currentCuad + 1

    elif(cuadruplos[currentCuad][0] == '+'):
        leftOp = get_val(cuadruplos[currentCuad][1], currLevel)
        rightOp = get_val(cuadruplos[currentCuad][2], currLevel)
        result = leftOp + rightOp
        update_memory(cuadruplos[currentCuad][3], result)
        currentCuad = currentCuad + 1

    elif(cuadruplos[currentCuad][0] == '-'):
        leftOp = get_val(cuadruplos[currentCuad][1], currLevel)
        rightOp = get_val(cuadruplos[currentCuad][2], currLevel)
        result = leftOp - rightOp
        update_memory(cuadruplos[currentCuad][3], result)
        currentCuad = currentCuad + 1

    elif(cuadruplos[currentCuad][0] == '*'):
        leftOp = get_val(cuadruplos[currentCuad][1], currLevel)
        rightOp = get_val(cuadruplos[currentCuad][2], currLevel)
        result = leftOp * rightOp
        update_memory(cuadruplos[currentCuad][3], result)
        currentCuad = currentCuad + 1

    elif(cuadruplos[currentCuad][0] == '/'):
        leftOp = get_val(cuadruplos[currentCuad][1], currLevel)
        rightOp = get_val(cuadruplos[currentCuad][2], currLevel)
        result = leftOp / rightOp
        update_memory(cuadruplos[currentCuad][3], result)
        currentCuad = currentCuad + 1

    elif(cuadruplos[currentCuad][0] == '='):
        asigned = get_val(cuadruplos[currentCuad][1], currLevel)
        asignee = cuadruplos[currentCuad][3]
        update_memory(asignee, asigned)
        currentCuad = currentCuad + 1

    elif(cuadruplos[currentCuad][0] == 'GOTOF'):
        op = get_val(cuadruplos[currentCuad][1], currLevel)
        if(not op):
            currentCuad = cuadruplos[currentCuad][3]
        else:
            currentCuad = currentCuad + 1

    elif(cuadruplos[currentCuad][0] == 'PRINT'):
        printable = get_val(cuadruplos[currentCuad][3], currLevel)
        if(cuadruplos[currentCuad][3] >= 37000):
            printAux = printable.replace('"', '')
            print(printAux)
        else:
            print(printable)
        currentCuad = currentCuad + 1

    elif(cuadruplos[currentCuad][0] == 'READ'):

        inp = input()
        address = cuadruplos[currentCuad][3]

        if(address >= 5000 and address < 7000): #Int globales
            inpAux = int(inp)
            update_memory(address, inpAux)

        elif(address >= 7000 and address < 9000): #Int locales
            inpAux = int(inp)
            update_memory(address, inpAux)

        elif(address >= 13000 and address < 15000): #FLoat globales
            inpAux = float(inp)
            update_memory(address, inpAux)

        elif(address >= 15000 and address < 17000): #floar locales
            inpAux = float(inp)
            update_memory(address, inpAux)

        elif(address >= 21000 and address < 23000): #char globales
            inpAux = str(inp)
            if(len(inpAux) > 1):
                print("String not accepted as char")
                sys.exit()
            else:
                update_memory(address, inpAux)

        elif(address >= 23000 and address < 25000): #char locales
            inpAux = str(inp)
            if(len(inpAux) > 1):
                print("String not accepted as char")
                sys.exit()
            else:
                update_memory(address, inpAux)

        elif(address >= 29000 and address < 31000): #bool global
            if(inp != 'True' or inp != 'False'):
                print("Booleand value must be True or False")
                sys.exit()
            if(inp == 'True'):
                update_memory(address, True)
            else:
                update_memory(address, False)

        elif(address >= 31000 and address < 33000): #bool local
            if(inp != 'True' or inp != 'False'):
                print("Booleand value must be True or False")
                sys.exit()
            if(inp == 'True'):
                update_memory(address, True)
            else:
                update_memory(address, False)

        currentCuad = currentCuad + 1


    elif(cuadruplos[currentCuad][0] == 'ERA'):
        intMem.append({})
        floatMem.append({})
        charMem.append({})
        boolMem.append({})
        currentFunc.append(cuadruplos[currentCuad][3])

        currentCuad = currentCuad + 1

    elif(cuadruplos[currentCuad][0] == 'PARAM'): ############################REPARAR##########################

        val = get_val(cuadruplos[currentCuad][2], currLevel)
        currLevel = currLevel + 1
        update_memory(cuadruplos[currentCuad][3], val)
        currLevel = currLevel - 1

        currentCuad = currentCuad + 1

    elif(cuadruplos[currentCuad][0] == 'GOSUB'):
        breadCrumb.append(currentCuad + 1)
        jump = dirFunc[cuadruplos[currentCuad][3]]['start_Address']
        currentCuad = jump
        currLevel = currLevel + 1

    elif(cuadruplos[currentCuad][0] == 'RET'):
        return_val = get_val(cuadruplos[currentCuad][3], currLevel)
        func = currentFunc[-1]
        func_var_address = dirFunc['global']['varsTable'][func]['address']
        auxCurrLevel = currLevel
        currLevel = currLevel - 1
        update_memory(func_var_address, return_val)
        currLevel = auxCurrLevel

        currentCuad = currentCuad + 1

    elif(cuadruplos[currentCuad][0] == 'ENDFUNC'):
        currentCuad = breadCrumb.pop()
        del intMem[currLevel]
        del floatMem[currLevel]
        del charMem[currLevel]
        del boolMem[currLevel]
        currentFunc.pop()
        currLevel = currLevel - 1
    #elif(cuadruplos[currentCuad][0] == 'VER'):
    #    None
