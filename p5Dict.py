#Purpose:
#	Inserts variable name into varTypeD as key and gives variable type as value.
#	Also inserts variable name as key in varValueD and stores value as value
#Parameter:
#	tokenM     - List of strings for a given line in the file
#	varTypeD   - Dictionary of variable types
#	vaarValueD - Dictionary of values
def declareVar(tokenM,varTypeD,varValueD):
   varTypeD[tokenM[2].upper()] = tokenM[1]
   varValueD[tokenM[2].upper()] = tokenM[3]


#Purpose:
#	Prints out the keys and values for varTypeD and varValueD in a table format
#Parameters:
#	varTypeD   - Dictionary of variable types
#       vaarValueD - Dictionary of values
def printVariables(varTypeD,varValueD):
   print("Variables")
   print("\tVariable\tType\tValue")
   
   keys = sorted(varTypeD.keys())
   for var in keys:
    formatted = "\t" + var + "\t\t" + varTypeD[var] + "\t" + varValueD[var]
    print(formatted)


#Purpose:
#	Prints out the keys and values for labelD in a table format
#Parameters:
#	labelD - Dictionary for labels
#
def printLabels(labelD):
   print("Labels")
   print("\tLabel\tStatement")

   keys = sorted(labelD.keys())
   for var in keys:
    formatted = "\t" + var + "\t"+ str(labelD[var])
    print(formatted)


