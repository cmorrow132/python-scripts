import sys

#//Setup initial variables //
programVersion="1.0"
programInfo=["Aircrack-wpadict "+programVersion,"Copyright 2016, Matt M. cmorrow132@gmail.com"," ","Usage:","   python aircrack-wpadict.py -o <outfile>"]
minLength=8
maxLength=64
maxPerDict=10000
currentDictIndex=0
currentWordCount=0
outFile=""

specialCharList=['`','~','!','@','$','%','^','&','*','(',')','-','_','+',':','{','}','[',']',':',';','"',",","<",">",".","?","/","|"]

argsTable=dict()

#//Functions
def printHelp():
	print " "
	for i in programInfo:
		print(i)
	print " "
	print " "
	quit()

#//Main code //

#strip program name from arguments list
sys.argv.pop(0)

numArgs=len(sys.argv)
if numArgs==0:
	printHelp()

if sys.argv[0]=='-help':
	printHelp()

#split arguments into key->pair

curArg=0

while curArg < numArgs:
	argsTable[sys.argv[curArg]]=sys.argv[curArg+1]
	curArg+=2

#Check arguments
for k,v in argsTable.items():
	if k=="-o":
		outFile=v
		print "Outfile:",outFile

if len(outFile)==0:
	printHelp()

#Create dictionaries
