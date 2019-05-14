import re


#Purpose:
#	Passed a statement that checks for correct amount of input to 
#	evaluate an expression. Parses list for expression and evaluates
#	it to be stored in the varaible dictionary
#
#Parameters:
#	line_list: Splitted statement from beep
#	varValueD: Dictionary of Variable Values
#
def assignVar(line_list,varValueD):
   # if only 3 args then save second variable into the first
   if len(line_list) == 3:
     try:
       varValueD[line_list[1].upper()] = varValueD[line_list[2].upper()]
     except:
       InvalidValueType("Variable Not Defined",line_list[2])
   if len(line_list) > 3:
    var = line_list[1].upper() # variable that will be assigned
    var2 = line_list[3].upper() #variable that will be the operand

    #evaluate for given expression
    if line_list[2] == "+":
       if len(line_list) <= 4:
         raise TooFewOperands("Too few operands")
       varValueD[var] = evalAdd(varValueD[var2],line_list[4])
    elif line_list[2] == "*":
       if len(line_list) <= 4:
         raise TooFewOperands("Too few operands")
       varValueD[var] = replicateString(varValueD[var2],varValueD[line_list[4].upper()])
    elif line_list[2] == "-":
       if len(line_list) <= 4:
         raise TooFewOperands("Too few operands")
       varValueD[var] = evalSub(varValueD[var2],line_list[4])
    elif line_list[2] == "&":
       if len(line_list) <= 4:
         raise TooFewOperands("Too few operands")
       varValueD[var] = concatStrings(varValueD[var2],varValueD[line_list[4].upper()])
    else:
       raise InvalidExpression("Invalid Expression",line_list[2])

#Purpose:
#	Evaluate if op1 is greater than op2. Returns true if 
#	op1 is greater than op2. Returns false otherwise.
# 	Exception raised if given value is not numeric.
#
#Parameters:
#	op1: operand1
#	op2: operand2
def evalGreater( op1, op2):
    try:
        iVal1 = int(op1)
    except:
        raise InvalidValueType("'%s' is not numeric" % (op1))
    try:
        iVal2 = int(op2)
    except:
        raise InvalidValueType("'%s' is not numeric" % (op2))
    return iVal1 > iVal2

#Purpose:
#	Evaluate whether op1 is greater than or equal to op2.
#	Returns true if true, false otherwise. Exception raised
#	if given value is not numeric
#
#Parameters:
#	op1: operand1
#	op2: operand2
def evalGreaterOrEql(op1,op2):
    try:
        iVal1 = int(op1)
    except:
        raise InvalidValueType("'%s' is not numeric" % (op1))
    try:
        iVal2 = int(op2)
    except:
        raise InvalidValueType("'%s' is not numeric" % (op2))
    return iVal1 >= iVal2

#Purpose:
#	Checks if given varNum2 is a string or int.	
#	Evaluates and returns the sum of the two parameters
#
#Parameters:
#	varNum1: int or variable from dictionary
#	varNum2: int or or variable from dictionary
def evalAdd(varNum1,varNum2):
  #print varNum1,varNum2
  if isinstance(varNum2,str):
        return int(varNum1)+int(varNum2)
  elif isinstance(varNum2,int):
        return int(varNum1)+varNum2

#Purpose:
#	Checks if given varNum2 is a string or int.
#	Evaluates and returns difference of two parameters
#
#Parameters:
#	varNum1:int or var from dictionary
#	varNum2:int or var from dictionary
def evalSub(varNum1,varNum2):
  if isinstance(varNum2,str):
        return int(varNum1)-int(varNum2)
  elif isinstance(varNum2,int):
        return int(varNum1)-varNum2

#Purpose:
#	Evaluates a given if statement. Checks given expression and 
#	calls its given function. Return i, to the main driver if 
#	statement is true. i will allow for the code to jump to another line
#	of the beep source code. Raised exception if operand are not numeric,
#	if a given label is not define, or a given variable is not defined.
#
#Parameters:
#	line_list: array of words
#	varValueD: value Dictionary
#	labeD: label Dictionary
#	i: int of current subscript
def evalIf(line_list,varValueD,labelD,i):
   #var1 = int(line_list[2])
   #print "var1",var1
   try:
    var1 = int(line_list[2])
   except:
    try:
       var1 = varValueD[line_list[2].upper()]
    except:
       raise InvalidValueType("'%s' is not numeric" % line_list[2])

   try:
    var2 = int(line_list[3])
   except:
    try:
       var2 = varValueD[line_list[3].upper()]
    except:
       raise VarNotDefined("'%s' Variable is not defined" % line_list[3])

   if line_list[1] == ">":
    if evalGreater(var1,var2):
       #print("GREATER TAHN")
       try:
        label = labelD[line_list[4].upper()]
       except:
        raise LabelNotDefined("'%s' Label is not defined" % line_list[4])

       i = int(label) - 2
       #print "I is",i,"Label:",label
       return i
    else:
       #print("not greate than")
       return i
   if line_list[1] == ">=":
        if evalGreaterOrEql(var1,var2):
            i = int(labelD[line_list[4].upper()]) - 2
            return i
        else:
            return i

#Purpose:
#	Returns varstring multiplied by varNumber
#
#Parameters:
#	varString: string
#	varNumber: int or var from dictionary
def replicateString(varString,varNumber):
  #print varString,varNumber
  if isinstance(varNumber,str):
    return varString*int(varNumber)
  elif isinstance(varNumber,int):
    return varString*varNumber

#Purpose:
#	Returns str1 and str2 concatenated together
#
#Parameters:
#	str1: string
#	str2: string
def concatStrings(str1,str2):
   str1 += str2
   return str1


#Purpose:
#	Prints tokens from line_list. If token is surounded by ""
#	then print that without the "". If token is a variable, then
#	print the given value from dictionary
#Parameters:
#	line_list: list of strings
#	varValueD: value Dictionary
def printLine(line_list,varValueD):
   printList = []
   for word in line_list:
    matched = re.search(r'^".*"$',word)
    if matched != None:
       printList.append(word[1:-1])
    else:
       printList.append(str(varValueD[word.upper()]))
   printString = ' '.join(printList)
   print(printString)

#Purpose:
#	Raised when variable that is not defined is called for execution
#
#Parameters:
#	Exception:
class InvalidValueType(Exception):
   def __init__(self,*args,**kwargs):
      super().__init__(self,*args,**kwargs)

#Purpose:
#	Raised when label that is not defined is called for execution
#
#	Exception:
class LabelNotDefined(Exception):
   pass

#Purpose:
#	Raised when not enough operands for expresson
#
#	Exception:
class TooFewOperands(Exception):
   pass

#Purpose:
#	Raised when invalid expression is used
#
#	Exception:
class InvalidExpression(Exception):
   pass
