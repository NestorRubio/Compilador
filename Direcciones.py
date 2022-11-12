import sys

class Direcciones:

    def __init__(self, integers, floats, chars, bools):

        self.integers = integers
        self.module_int = integers + 2000
        self.cte_int = self.module_int + 2000
        self.temp_int = self.cte_int + 2000

        self.floats = floats
        self.module_float = floats + 2000
        self.cte_float = self.module_float + 2000
        self.temp_float = self.cte_float + 2000

        self.chars = chars
        self.module_char = chars + 2000
        self.cte_char = self.module_char + 2000
        self.temp_char = self.cte_char + 2000

        self.bools = bools
        self.module_bool = self.bools + 2000
        self.cte_bool = self.module_bool + 2000
        self.temp_bool = self.cte_bool + 2000

        self.GI = 0
        self.GF = 0
        self.GC = 0
        self.GB = 0

        self.MI = 0
        self.MF = 0
        self.MC = 0
        self.MB = 0

        self.CI = 0
        self.CF = 0
        self.CC =0
        self.CB = 0

        self.TI = 0
        self.TF = 0
        self.TC = 0
        self.TB = 0

    def global_var_addr(self, type):
        if(type == 'int'):
            if(self.GI >= self.module_int):
                print("Out of memory")
                sys.exit()
            else:
                self.GI = self.GI + 1
                return self.GI + self.integers - 1
        elif(type == 'float'):
            if(self.GF >= self.module_float):
                print("Out of memory")
                sys.exit()
            else:
                self.GF = self.GF + 1
                return self.GF + self.floats - 1
        elif(type == 'char'):
            if(self.GC >= self.module_char):
                print("Out of memory")
                sys.exit()
            else:
                self.GC = self.GC + 1
                return self.GC + self.chars - 1
        elif(type == 'bool'):
            if(self.GB >= self.module_bool):
                print("Out of memory")
                sys.exit()
            else:
                self.GB = self.GB + 1
                return self.GB + self.bools - 1


    def module_var_addr(self, type):
        if(type == 'int'):
            if(self.MI >= self.cte_int):
                print("Out of memory")
                sys.exit()
            else:
                self.MI = self.MI + 1
                return self.MI + self.module_int - 1
        elif(type == 'float'):
            if(self.MF >= self.cte_float):
                print("Out of memory")
                sys.exit()
            else:
                self.MF = self.MF + 1
                return self.MF + self.module_float - 1
        elif(type == 'char'):
            if(self.MC >= self.cte_char):
                print("Out of memory")
                sys.exit()
            else:
                self.MC = self.MC + 1
                return self.MC + self.module_char - 1
        elif(type == 'bool'):
            if(self.MB >= self.cte_bool):
                print("Out of memory")
                sys.exit()
            else:
                self.MB = self.MB + 1
                return self.MB + self.module_bool - 1


    def temp_var_addr(self, type):
        if(type == 'int'):
            if(self.TI >= self.temp_int + 2000):
                print("Out of memory")
                sys.exit()
            else:
                self.TI = self.TI + 1
                return self.TI + self.temp_int - 1
        elif(type == 'float'):
            if(self.TF >= self.temp_float + 2000):
                print("Out of memory")
                sys.exit()
            else:
                self.TF = self.TF + 1
                return self.TF + self.temp_float - 1
        elif(type == 'char'):
            if(self.TC >= self.temp_char + 2000):
                print("Out of memory")
                sys.exit()
            else:
                self.TC = self.TC + 1
                return self.TC + self.temp_char - 1
        elif(type == 'bool'):
            if(self.TB >= self.temp_bool + 2000):
                print("Out of memory")
                sys.exit()
            else:
                self.TB = self.TB + 1
                return self.TB + self.temp_bool - 1


    def cte_var_addr(self, type):
        if(type == 'int'):
            if(self.CI >= self.temp_int):
                print("Out of memory")
                sys.exit()
            else:
                self.CI = self.CI + 1
                return self.CI + self.cte_int - 1
        elif(type == 'float'):
            if(self.CF >= self.temp_float):
                print("Out of memory")
                sys.exit()
            else:
                self.CF = self.CF + 1
                return self.CF + self.cte_float - 1
        elif(type == 'char'):
            if(self.CC >= self.temp_char):
                print("Out of memory")
                sys.exit()
            else:
                self.CC = self.CC + 1
                return self.CC + self.cte_char - 1
        elif(type == 'bool'):
            if(self.CB >= self.temp_bool):
                print("Out of memory")
                sys.exit()
            else:
                self.CB = self.CB + 1
                return self.CB + self.cte_bool - 1
    