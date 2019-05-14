#Written By Michael Canas
#Purpose:
#	Gets passed a file of Beep source code. It reads all lines and
#	prints them out and assigns a subscript with each line. As it read the file
#	it also interprets variables and labels to be saved in dictionaries.
#Input:
#	1 Text File
#
#Output:
#	Source Code with its subscrip
#	Formatted Variables Table
#	Formatted Label Table

import sys
import re
from p5Dict import declareVar,printVariables,printLabels
from p6Exec import assignVar,evalGreater,evalGreaterOrEql,evalAdd,evalSub,evalIf,replicateString,concatStrings,printLine

#class Executor:
 #  def __init__(self,line_list,varTypeD,varValueD,labelD):
#	self.line = line_list


def main():
   varTypeD = {}
   varValueD = {}
   labelD = {}

   vFlag = 0
   if len(sys.argv) == 3:
      if sys.argv[2] == "-v":
        vFlag = 1

   infile = open(sys.argv[1],"r")
   input_lines = []
   label_list = []

   i = 1
   
   #Traverse each line in the file
   for line in infile:

    #Print source code with subscripts
    print(str(i),". ",line)

    #print line,len(line)
    if(len(line) <= 5):
       continue

    input_lines.append(line)
    splitted_line = line.split()

    #If the first word is VAR, declare it as a varible in dictionary
    #print len(splitted_line)
    if splitted_line[0] == "VAR":

       #if splitted_line[1] == "string":
       if len(splitted_line) < 4:
        splitted_line.append("\"NULL\"")
        splitted_line[3] = splitted_line[3][1:-1]
       #print "Splitted LINE", splitted_line
       declareVar(splitted_line,varTypeD,varValueD)

    #If the first word ends with a colon, delare as label in labelD
    matched = re.search(r'.*:',splitted_line[0])
    splitted_line[0] = splitted_line[0][:-1].upper()
    #If the regex matches, then check if label has already been used
    if matched != None:
       #If label has already been used, print Error
       if splitted_line[0] in label_list:
        print("***Error: label ",splitted_line[0],"appears on multiple lines:",labelD[splitted_line[0]] ,"and",i)
       #Else add label to label_list and declare it the labeD dictionary
       else:
        label_list.append(splitted_line[0])
        labelD[splitted_line[0]] = i
    i+= 1


   infile.close()

   printVariables(varTypeD,varValueD);
   printLabels(labelD)
   print("execution begins ...")

   i = 0
   lines_executed = 0
   #loop through lines of beep source code
   while (i < len(input_lines)):
    lines_executed += 1

    if(lines_executed > 5000):
       print("Loop Error: Infinite Loop Likely Occured")
       break
    splitted_line = input_lines[i].split()
    # match for label
    matched = re.search(r'.*:',splitted_line[0])

    if vFlag == 1:
       print("executing line",i,":",input_lines[i])

    #pop label and execute the rest of the statemtn
    if matched != None:
       splitted_line.pop(0)
    if splitted_line[0] == "ASSIGN":
       assignVar(splitted_line,varValueD)
    elif splitted_line[0] == "PRINT":
       printLine(splitted_line[1:],varValueD)
    elif splitted_line[0] == "if" or splitted_line[0] == "IF":
       #print(splitted_line)
       i = evalIf(splitted_line,varValueD,labelD,i)
       #print "i after if",i

    elif splitted_line[0] == "GOTO":
       i = labelD[splitted_line[1].upper()] - 2
    i+=1
   #print "FINAL DITCITONRY: ",varValueD
   #print "Fineal Labels",labelD

   print("execution ends",lines_executed,"lines executed")

if __name__ == "__main__":
    main() 
