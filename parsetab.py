
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASIGN BOOL CHAR COMMA COMMENT CORDER CORIZQ CTE_FLT CTE_INT CTE_STR DIFF DIV DOSPTOS ELSE EQUAL FLOAT FOR FUNC GT GTE ID IF INT LLVEDER LLVEIZQ LT LTE MAIN MAS MAT MENOS MULT OR PARDER PARIZQ PRINT PROGRAM PTOCOMA PUNTO RETURN VAR VOID\n    PROGRAMA : PROGRAM CREATE_DIRFUNC ID PTOCOMA VARS_P FUNCS_P MAIN_G\n    \n    VARS : VAR TYPE ID ADD_VAR VARS_PP PTOCOMA\n         | MAT TYPE ID CORIZQ CTE_INT CORDER VARS_PPP PTOCOMA\n    \n    VARS_P : VARS VARS_P\n           | empty   \n    \n    VARS_PP : COMMA ID ADD_VAR VARS_PP\n            | empty\n    \n    VARS_PPP : CORIZQ CTE_INT CORDER\n             | empty\n    \n    FUNCS : FUNC TYPE_P ID ADD_FUNC PARIZQ PARAMS PARDER LLVEIZQ ESTATUTO_P RETURN EXPRESION PTOCOMA LLVEDER\n    \n    FUNCS_P : FUNCS FUNCS_P\n            | empty\n    \n    TYPE : INT CURR_TYPE\n         | FLOAT CURR_TYPE\n         | BOOL CURR_TYPE\n         | CHAR CURR_TYPE\n    \n    TYPE_P : TYPE\n           | VOID CURR_TYPE\n    \n    PARAMS : TYPE ID ADD_VAR PARAMS_P\n           | empty\n    \n    PARAMS_P : COMMA TYPE ID ADD_VAR PARAMS_P\n             | empty\n    \n    MAIN_G : VOID MAIN PARIZQ PARDER LLVEIZQ ESTATUTO_P LLVEDER\n    \n    ESTATUTO : ASIGNACION\n             | CONDICION\n             | LOOP_FOR\n             | ESCRITURA\n             | FUNC_CALL   \n    \n    ESTATUTO_P : ESTATUTO ESTATUTO_P\n               | empty\n    \n    ASIGNACION : ID ASIGN EXPRESION PTOCOMA\n               | ID ASIGN FUNC_CALL\n    \n    CONDICION : IF PARIZQ EXPRESION PARDER LLVEIZQ ESTATUTO_P LLVEDER CONDICION_P\n    \n    CONDICION_P : ELSE LLVEIZQ ESTATUTO_P LLVEDER\n                | empty\n    \n    LOOP_FOR : FOR PARIZQ CTE_INT COMMA CTE_INT COMMA CTE_INT PARDER LLVEIZQ ESTATUTO_P LLVEDER\n    \n    ESCRITURA : PRINT PARIZQ PRINTABLE PRINTABLE_P PARDER\n    \n    PRINTABLE : EXPRESION\n              | CTE_STR\n    \n    PRINTABLE_P : COMMA PRINTABLE PRINTABLE_P\n                | empty\n    \n    FUNC_CALL : ID PARIZQ PARM PARDER\n    \n    PARM : PARM_P\n         | empty\n    \n    PARM_P : CTE_INT PARM_PP\n           | CTE_FLT PARM_PP\n           | ID PARM_PP\n    \n    PARM_PP : COMMA PARM_P\n             | empty\n    \n    EXPRESION : EXPR EXPRESION_P\n    \n    EXPRESION_P : OR EXPR\n                | AND EXPR\n                | empty\n    \n    EXPR : EXP EXPR_P\n    \n    EXPR_P : LT EXP\n           | GT EXP\n           | DIFF EXP\n           | LTE EXP\n           | GTE EXP\n           | EQUAL EXP\n           | empty\n    \n    EXP : TERM EXP_P\n    \n    EXP_P : MAS TERM EXP_P\n          | MENOS TERM EXP_P\n          | empty\n    \n    TERM : FACTOR TERM_P\n    \n    TERM_P : MULT  FACTOR TERM_P\n           | DIV FACTOR TERM_P\n           | empty\n    \n    FACTOR : PARIZQ EXPRESION PARDER\n           | FACTOR_P VAR_CTE\n    \n    FACTOR_P : MAS\n             | MENOS\n             | empty\n    \n    VAR_CTE : ID\n            | CTE_INT\n            | CTE_FLT\n    empty :CREATE_DIRFUNC :CURR_TYPE :ADD_VAR :ADD_FUNC :ID_CUAD :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,22,75,],[0,-1,-23,]),'ID':([2,3,16,17,18,19,20,21,25,26,27,29,30,31,32,36,42,50,52,59,61,62,63,64,65,77,78,79,81,82,87,89,93,94,95,96,112,114,115,119,120,121,122,123,124,127,128,131,132,139,141,147,149,150,165,167,180,184,186,188,189,192,193,],[-79,4,28,-80,-80,-80,-80,33,35,-17,-80,-13,-14,-15,-16,-18,48,66,71,66,-24,-25,-26,-27,-28,85,97,-78,-78,66,-32,-78,135,-72,-73,-74,-31,-78,-78,-78,-78,-78,-78,-78,-78,-78,-78,-78,-78,97,-42,-78,-78,170,66,-37,-78,-33,-35,66,66,-34,-36,]),'PTOCOMA':([4,28,37,41,43,48,49,54,56,57,72,84,86,88,90,91,92,113,116,118,125,126,129,130,133,134,135,136,137,151,152,153,154,155,156,157,158,159,160,161,162,163,169,171,172,173,174,],[5,-81,-78,47,-7,-81,-78,-78,74,-9,-6,-8,112,-78,-78,-78,-78,-50,-53,-54,-61,-62,-65,-66,-69,-71,-75,-76,-77,-51,-52,-70,-55,-56,-57,-58,-59,-60,-78,-78,-78,-78,178,-63,-64,-67,-68,]),'VAR':([5,7,47,74,],[9,9,-2,-3,]),'MAT':([5,7,47,74,],[10,10,-2,-3,]),'FUNC':([5,6,7,8,12,15,47,74,182,],[-78,14,-78,-5,14,-4,-2,-3,-10,]),'VOID':([5,6,7,8,11,12,13,14,15,24,47,74,182,],[-78,-78,-78,-5,23,-78,-12,27,-4,-11,-2,-3,-10,]),'INT':([9,10,14,46,110,],[17,17,17,17,17,]),'FLOAT':([9,10,14,46,110,],[18,18,18,18,18,]),'BOOL':([9,10,14,46,110,],[19,19,19,19,19,]),'CHAR':([9,10,14,46,110,],[20,20,20,20,20,]),'MAIN':([23,],[34,]),'COMMA':([28,37,48,54,71,83,88,90,91,92,97,101,102,104,105,106,107,113,116,118,125,126,129,130,133,134,135,136,137,151,152,153,154,155,156,157,158,159,160,161,162,163,166,168,170,171,172,173,174,179,],[-81,42,-81,42,-81,110,-78,-78,-78,-78,139,139,139,145,147,-38,-39,-50,-53,-54,-61,-62,-65,-66,-69,-71,-75,-76,-77,-51,-52,-70,-55,-56,-57,-58,-59,-60,-78,-78,-78,-78,176,147,-81,-63,-64,-67,-68,110,]),'CORIZQ':([33,49,],[38,55,]),'PARIZQ':([34,35,40,66,67,68,69,77,79,81,85,89,114,115,119,120,121,122,123,124,127,128,131,132,147,149,],[39,-82,46,78,79,80,81,89,89,89,78,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,]),'CTE_INT':([38,55,77,78,79,80,81,89,93,94,95,96,114,115,119,120,121,122,123,124,127,128,131,132,139,145,147,149,176,],[44,73,-78,101,-78,104,-78,-78,136,-72,-73,-74,-78,-78,-78,-78,-78,-78,-78,-78,-78,-78,-78,-78,101,166,-78,-78,181,]),'PARDER':([39,46,51,53,71,78,83,88,90,91,92,97,98,99,100,101,102,103,105,106,107,109,111,113,116,117,118,125,126,129,130,133,134,135,136,137,138,140,142,143,146,148,151,152,153,154,155,156,157,158,159,160,161,162,163,164,168,170,171,172,173,174,177,179,181,183,],[45,-78,70,-20,-81,-78,-78,-78,-78,-78,-78,-78,141,-43,-44,-78,-78,144,-78,-38,-39,-19,-22,-50,-53,153,-54,-61,-62,-65,-66,-69,-71,-75,-76,-77,-47,-49,-45,-46,167,-41,-51,-52,-70,-55,-56,-57,-58,-59,-60,-78,-78,-78,-78,-48,-78,-81,-63,-64,-67,-68,-40,-78,187,-21,]),'CORDER':([44,73,],[49,84,]),'LLVEIZQ':([45,70,144,185,187,],[50,82,165,188,189,]),'LLVEDER':([50,58,59,60,61,62,63,64,65,76,87,112,141,165,167,175,178,180,184,186,188,189,190,191,192,193,],[-78,75,-78,-30,-24,-25,-26,-27,-28,-29,-32,-31,-42,-78,-37,180,182,-78,-33,-35,-78,-78,192,193,-34,-36,]),'IF':([50,59,61,62,63,64,65,82,87,112,141,165,167,180,184,186,188,189,192,193,],[67,67,-24,-25,-26,-27,-28,67,-32,-31,-42,67,-37,-78,-33,-35,67,67,-34,-36,]),'FOR':([50,59,61,62,63,64,65,82,87,112,141,165,167,180,184,186,188,189,192,193,],[68,68,-24,-25,-26,-27,-28,68,-32,-31,-42,68,-37,-78,-33,-35,68,68,-34,-36,]),'PRINT':([50,59,61,62,63,64,65,82,87,112,141,165,167,180,184,186,188,189,192,193,],[69,69,-24,-25,-26,-27,-28,69,-32,-31,-42,69,-37,-78,-33,-35,69,69,-34,-36,]),'RETURN':([59,60,61,62,63,64,65,76,82,87,108,112,141,167,180,184,186,192,193,],[-78,-30,-24,-25,-26,-27,-28,-29,-78,-32,149,-31,-42,-37,-78,-33,-35,-34,-36,]),'ASIGN':([66,],[77,]),'MAS':([77,79,81,89,91,92,114,115,119,120,121,122,123,124,127,128,130,131,132,133,134,135,136,137,147,149,153,160,161,162,163,173,174,],[94,94,94,94,127,-78,94,94,94,94,94,94,94,94,94,94,-66,94,94,-69,-71,-75,-76,-77,94,94,-70,127,127,-78,-78,-67,-68,]),'MENOS':([77,79,81,89,91,92,114,115,119,120,121,122,123,124,127,128,130,131,132,133,134,135,136,137,147,149,153,160,161,162,163,173,174,],[95,95,95,95,128,-78,95,95,95,95,95,95,95,95,95,95,-66,95,95,-69,-71,-75,-76,-77,95,95,-70,128,128,-78,-78,-67,-68,]),'CTE_FLT':([77,78,79,81,89,93,94,95,96,114,115,119,120,121,122,123,124,127,128,131,132,139,147,149,],[-78,102,-78,-78,-78,137,-72,-73,-74,-78,-78,-78,-78,-78,-78,-78,-78,-78,-78,-78,-78,102,-78,-78,]),'CTE_STR':([81,147,],[107,107,]),'OR':([88,90,91,92,118,125,126,129,130,133,134,135,136,137,153,154,155,156,157,158,159,160,161,162,163,171,172,173,174,],[114,-78,-78,-78,-54,-61,-62,-65,-66,-69,-71,-75,-76,-77,-70,-55,-56,-57,-58,-59,-60,-78,-78,-78,-78,-63,-64,-67,-68,]),'AND':([88,90,91,92,118,125,126,129,130,133,134,135,136,137,153,154,155,156,157,158,159,160,161,162,163,171,172,173,174,],[115,-78,-78,-78,-54,-61,-62,-65,-66,-69,-71,-75,-76,-77,-70,-55,-56,-57,-58,-59,-60,-78,-78,-78,-78,-63,-64,-67,-68,]),'LT':([90,91,92,126,129,130,133,134,135,136,137,153,160,161,162,163,171,172,173,174,],[119,-78,-78,-62,-65,-66,-69,-71,-75,-76,-77,-70,-78,-78,-78,-78,-63,-64,-67,-68,]),'GT':([90,91,92,126,129,130,133,134,135,136,137,153,160,161,162,163,171,172,173,174,],[120,-78,-78,-62,-65,-66,-69,-71,-75,-76,-77,-70,-78,-78,-78,-78,-63,-64,-67,-68,]),'DIFF':([90,91,92,126,129,130,133,134,135,136,137,153,160,161,162,163,171,172,173,174,],[121,-78,-78,-62,-65,-66,-69,-71,-75,-76,-77,-70,-78,-78,-78,-78,-63,-64,-67,-68,]),'LTE':([90,91,92,126,129,130,133,134,135,136,137,153,160,161,162,163,171,172,173,174,],[122,-78,-78,-62,-65,-66,-69,-71,-75,-76,-77,-70,-78,-78,-78,-78,-63,-64,-67,-68,]),'GTE':([90,91,92,126,129,130,133,134,135,136,137,153,160,161,162,163,171,172,173,174,],[123,-78,-78,-62,-65,-66,-69,-71,-75,-76,-77,-70,-78,-78,-78,-78,-63,-64,-67,-68,]),'EQUAL':([90,91,92,126,129,130,133,134,135,136,137,153,160,161,162,163,171,172,173,174,],[124,-78,-78,-62,-65,-66,-69,-71,-75,-76,-77,-70,-78,-78,-78,-78,-63,-64,-67,-68,]),'MULT':([92,134,135,136,137,153,162,163,],[131,-71,-75,-76,-77,-70,131,131,]),'DIV':([92,134,135,136,137,153,162,163,],[132,-71,-75,-76,-77,-70,132,132,]),'ELSE':([180,],[185,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'PROGRAMA':([0,],[1,]),'CREATE_DIRFUNC':([2,],[3,]),'VARS_P':([5,7,],[6,15,]),'VARS':([5,7,],[7,7,]),'empty':([5,6,7,12,37,46,49,50,54,59,77,78,79,81,82,83,88,89,90,91,92,97,101,102,105,114,115,119,120,121,122,123,124,127,128,131,132,147,149,160,161,162,163,165,168,179,180,188,189,],[8,13,8,13,43,53,57,60,43,60,96,100,96,96,60,111,116,96,125,129,133,140,140,140,148,96,96,96,96,96,96,96,96,96,96,96,96,96,96,129,129,133,133,60,148,111,186,60,60,]),'FUNCS_P':([6,12,],[11,24,]),'FUNCS':([6,12,],[12,12,]),'TYPE':([9,10,14,46,110,],[16,21,26,52,150,]),'MAIN_G':([11,],[22,]),'TYPE_P':([14,],[25,]),'CURR_TYPE':([17,18,19,20,27,],[29,30,31,32,36,]),'ADD_VAR':([28,48,71,170,],[37,54,83,179,]),'ADD_FUNC':([35,],[40,]),'VARS_PP':([37,54,],[41,72,]),'PARAMS':([46,],[51,]),'VARS_PPP':([49,],[56,]),'ESTATUTO_P':([50,59,82,165,188,189,],[58,76,108,175,190,191,]),'ESTATUTO':([50,59,82,165,188,189,],[59,59,59,59,59,59,]),'ASIGNACION':([50,59,82,165,188,189,],[61,61,61,61,61,61,]),'CONDICION':([50,59,82,165,188,189,],[62,62,62,62,62,62,]),'LOOP_FOR':([50,59,82,165,188,189,],[63,63,63,63,63,63,]),'ESCRITURA':([50,59,82,165,188,189,],[64,64,64,64,64,64,]),'FUNC_CALL':([50,59,77,82,165,188,189,],[65,65,87,65,65,65,65,]),'EXPRESION':([77,79,81,89,147,149,],[86,103,106,117,106,169,]),'EXPR':([77,79,81,89,114,115,147,149,],[88,88,88,88,151,152,88,88,]),'EXP':([77,79,81,89,114,115,119,120,121,122,123,124,147,149,],[90,90,90,90,90,90,154,155,156,157,158,159,90,90,]),'TERM':([77,79,81,89,114,115,119,120,121,122,123,124,127,128,147,149,],[91,91,91,91,91,91,91,91,91,91,91,91,160,161,91,91,]),'FACTOR':([77,79,81,89,114,115,119,120,121,122,123,124,127,128,131,132,147,149,],[92,92,92,92,92,92,92,92,92,92,92,92,92,92,162,163,92,92,]),'FACTOR_P':([77,79,81,89,114,115,119,120,121,122,123,124,127,128,131,132,147,149,],[93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,]),'PARM':([78,],[98,]),'PARM_P':([78,139,],[99,164,]),'PRINTABLE':([81,147,],[105,168,]),'PARAMS_P':([83,179,],[109,183,]),'EXPRESION_P':([88,],[113,]),'EXPR_P':([90,],[118,]),'EXP_P':([91,160,161,],[126,171,172,]),'TERM_P':([92,162,163,],[130,173,174,]),'VAR_CTE':([93,],[134,]),'PARM_PP':([97,101,102,],[138,142,143,]),'PRINTABLE_P':([105,168,],[146,177,]),'CONDICION_P':([180,],[184,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAMA","S'",1,None,None,None),
  ('PROGRAMA -> PROGRAM CREATE_DIRFUNC ID PTOCOMA VARS_P FUNCS_P MAIN_G','PROGRAMA',7,'p_PROGRAMA','NyParser.py',16),
  ('VARS -> VAR TYPE ID ADD_VAR VARS_PP PTOCOMA','VARS',6,'p_VARS','NyParser.py',21),
  ('VARS -> MAT TYPE ID CORIZQ CTE_INT CORDER VARS_PPP PTOCOMA','VARS',8,'p_VARS','NyParser.py',22),
  ('VARS_P -> VARS VARS_P','VARS_P',2,'p_VARS_P','NyParser.py',27),
  ('VARS_P -> empty','VARS_P',1,'p_VARS_P','NyParser.py',28),
  ('VARS_PP -> COMMA ID ADD_VAR VARS_PP','VARS_PP',4,'p_VARS_PP','NyParser.py',33),
  ('VARS_PP -> empty','VARS_PP',1,'p_VARS_PP','NyParser.py',34),
  ('VARS_PPP -> CORIZQ CTE_INT CORDER','VARS_PPP',3,'p_VARS_PPP','NyParser.py',39),
  ('VARS_PPP -> empty','VARS_PPP',1,'p_VARS_PPP','NyParser.py',40),
  ('FUNCS -> FUNC TYPE_P ID ADD_FUNC PARIZQ PARAMS PARDER LLVEIZQ ESTATUTO_P RETURN EXPRESION PTOCOMA LLVEDER','FUNCS',13,'p_FUNCS','NyParser.py',45),
  ('FUNCS_P -> FUNCS FUNCS_P','FUNCS_P',2,'p_FUNCS_P','NyParser.py',50),
  ('FUNCS_P -> empty','FUNCS_P',1,'p_FUNCS_P','NyParser.py',51),
  ('TYPE -> INT CURR_TYPE','TYPE',2,'p_TYPE','NyParser.py',56),
  ('TYPE -> FLOAT CURR_TYPE','TYPE',2,'p_TYPE','NyParser.py',57),
  ('TYPE -> BOOL CURR_TYPE','TYPE',2,'p_TYPE','NyParser.py',58),
  ('TYPE -> CHAR CURR_TYPE','TYPE',2,'p_TYPE','NyParser.py',59),
  ('TYPE_P -> TYPE','TYPE_P',1,'p_TYPE_P','NyParser.py',64),
  ('TYPE_P -> VOID CURR_TYPE','TYPE_P',2,'p_TYPE_P','NyParser.py',65),
  ('PARAMS -> TYPE ID ADD_VAR PARAMS_P','PARAMS',4,'p_PARAMS','NyParser.py',70),
  ('PARAMS -> empty','PARAMS',1,'p_PARAMS','NyParser.py',71),
  ('PARAMS_P -> COMMA TYPE ID ADD_VAR PARAMS_P','PARAMS_P',5,'p_PARAMS_P','NyParser.py',76),
  ('PARAMS_P -> empty','PARAMS_P',1,'p_PARAMS_P','NyParser.py',77),
  ('MAIN_G -> VOID MAIN PARIZQ PARDER LLVEIZQ ESTATUTO_P LLVEDER','MAIN_G',7,'p_MAIN_G','NyParser.py',82),
  ('ESTATUTO -> ASIGNACION','ESTATUTO',1,'p_ESTATUTO','NyParser.py',87),
  ('ESTATUTO -> CONDICION','ESTATUTO',1,'p_ESTATUTO','NyParser.py',88),
  ('ESTATUTO -> LOOP_FOR','ESTATUTO',1,'p_ESTATUTO','NyParser.py',89),
  ('ESTATUTO -> ESCRITURA','ESTATUTO',1,'p_ESTATUTO','NyParser.py',90),
  ('ESTATUTO -> FUNC_CALL','ESTATUTO',1,'p_ESTATUTO','NyParser.py',91),
  ('ESTATUTO_P -> ESTATUTO ESTATUTO_P','ESTATUTO_P',2,'p_ESTATUTO_P','NyParser.py',96),
  ('ESTATUTO_P -> empty','ESTATUTO_P',1,'p_ESTATUTO_P','NyParser.py',97),
  ('ASIGNACION -> ID ASIGN EXPRESION PTOCOMA','ASIGNACION',4,'p_ASIGNACION','NyParser.py',102),
  ('ASIGNACION -> ID ASIGN FUNC_CALL','ASIGNACION',3,'p_ASIGNACION','NyParser.py',103),
  ('CONDICION -> IF PARIZQ EXPRESION PARDER LLVEIZQ ESTATUTO_P LLVEDER CONDICION_P','CONDICION',8,'p_CONDICION','NyParser.py',108),
  ('CONDICION_P -> ELSE LLVEIZQ ESTATUTO_P LLVEDER','CONDICION_P',4,'p_CONDICION_P','NyParser.py',113),
  ('CONDICION_P -> empty','CONDICION_P',1,'p_CONDICION_P','NyParser.py',114),
  ('LOOP_FOR -> FOR PARIZQ CTE_INT COMMA CTE_INT COMMA CTE_INT PARDER LLVEIZQ ESTATUTO_P LLVEDER','LOOP_FOR',11,'p_LOOP_FOR','NyParser.py',119),
  ('ESCRITURA -> PRINT PARIZQ PRINTABLE PRINTABLE_P PARDER','ESCRITURA',5,'p_ESCRITURA','NyParser.py',124),
  ('PRINTABLE -> EXPRESION','PRINTABLE',1,'p_PRINTABLE','NyParser.py',129),
  ('PRINTABLE -> CTE_STR','PRINTABLE',1,'p_PRINTABLE','NyParser.py',130),
  ('PRINTABLE_P -> COMMA PRINTABLE PRINTABLE_P','PRINTABLE_P',3,'p_PRINTABLE_P','NyParser.py',135),
  ('PRINTABLE_P -> empty','PRINTABLE_P',1,'p_PRINTABLE_P','NyParser.py',136),
  ('FUNC_CALL -> ID PARIZQ PARM PARDER','FUNC_CALL',4,'p_FUNC_CALL','NyParser.py',141),
  ('PARM -> PARM_P','PARM',1,'p_PARM','NyParser.py',146),
  ('PARM -> empty','PARM',1,'p_PARM','NyParser.py',147),
  ('PARM_P -> CTE_INT PARM_PP','PARM_P',2,'p_PARM_P','NyParser.py',152),
  ('PARM_P -> CTE_FLT PARM_PP','PARM_P',2,'p_PARM_P','NyParser.py',153),
  ('PARM_P -> ID PARM_PP','PARM_P',2,'p_PARM_P','NyParser.py',154),
  ('PARM_PP -> COMMA PARM_P','PARM_PP',2,'p_PARM_PP','NyParser.py',159),
  ('PARM_PP -> empty','PARM_PP',1,'p_PARM_PP','NyParser.py',160),
  ('EXPRESION -> EXPR EXPRESION_P','EXPRESION',2,'p_EXPRESION','NyParser.py',165),
  ('EXPRESION_P -> OR EXPR','EXPRESION_P',2,'p_EXPRESION_P','NyParser.py',170),
  ('EXPRESION_P -> AND EXPR','EXPRESION_P',2,'p_EXPRESION_P','NyParser.py',171),
  ('EXPRESION_P -> empty','EXPRESION_P',1,'p_EXPRESION_P','NyParser.py',172),
  ('EXPR -> EXP EXPR_P','EXPR',2,'p_EXPR','NyParser.py',177),
  ('EXPR_P -> LT EXP','EXPR_P',2,'p_EXPR_P','NyParser.py',182),
  ('EXPR_P -> GT EXP','EXPR_P',2,'p_EXPR_P','NyParser.py',183),
  ('EXPR_P -> DIFF EXP','EXPR_P',2,'p_EXPR_P','NyParser.py',184),
  ('EXPR_P -> LTE EXP','EXPR_P',2,'p_EXPR_P','NyParser.py',185),
  ('EXPR_P -> GTE EXP','EXPR_P',2,'p_EXPR_P','NyParser.py',186),
  ('EXPR_P -> EQUAL EXP','EXPR_P',2,'p_EXPR_P','NyParser.py',187),
  ('EXPR_P -> empty','EXPR_P',1,'p_EXPR_P','NyParser.py',188),
  ('EXP -> TERM EXP_P','EXP',2,'p_EXP','NyParser.py',193),
  ('EXP_P -> MAS TERM EXP_P','EXP_P',3,'p_EXP_P','NyParser.py',198),
  ('EXP_P -> MENOS TERM EXP_P','EXP_P',3,'p_EXP_P','NyParser.py',199),
  ('EXP_P -> empty','EXP_P',1,'p_EXP_P','NyParser.py',200),
  ('TERM -> FACTOR TERM_P','TERM',2,'p_TERM','NyParser.py',205),
  ('TERM_P -> MULT FACTOR TERM_P','TERM_P',3,'p_TERM_P','NyParser.py',210),
  ('TERM_P -> DIV FACTOR TERM_P','TERM_P',3,'p_TERM_P','NyParser.py',211),
  ('TERM_P -> empty','TERM_P',1,'p_TERM_P','NyParser.py',212),
  ('FACTOR -> PARIZQ EXPRESION PARDER','FACTOR',3,'p_FACTOR','NyParser.py',217),
  ('FACTOR -> FACTOR_P VAR_CTE','FACTOR',2,'p_FACTOR','NyParser.py',218),
  ('FACTOR_P -> MAS','FACTOR_P',1,'p_FACTOR_P','NyParser.py',223),
  ('FACTOR_P -> MENOS','FACTOR_P',1,'p_FACTOR_P','NyParser.py',224),
  ('FACTOR_P -> empty','FACTOR_P',1,'p_FACTOR_P','NyParser.py',225),
  ('VAR_CTE -> ID','VAR_CTE',1,'p_VAR_CTE','NyParser.py',230),
  ('VAR_CTE -> CTE_INT','VAR_CTE',1,'p_VAR_CTE','NyParser.py',231),
  ('VAR_CTE -> CTE_FLT','VAR_CTE',1,'p_VAR_CTE','NyParser.py',232),
  ('empty -> <empty>','empty',0,'p_empty','NyParser.py',236),
  ('CREATE_DIRFUNC -> <empty>','CREATE_DIRFUNC',0,'p_CREATE_DIRFUNC','NyParser.py',275),
  ('CURR_TYPE -> <empty>','CURR_TYPE',0,'p_CURR_TYPE','NyParser.py',280),
  ('ADD_VAR -> <empty>','ADD_VAR',0,'p_ADD_VAR','NyParser.py',285),
  ('ADD_FUNC -> <empty>','ADD_FUNC',0,'p_ADD_FUNC','NyParser.py',295),
  ('ID_CUAD -> <empty>','ID_CUAD',0,'p_ID_CUAD','NyParser.py',305),
]
