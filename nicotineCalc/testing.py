def GetAndPrint():
	this = mustbeNumber()
	print ("Yay you got a number!");
	print (this);



def FetchNumbersOnly():
	mustbeNumber = raw_input("Gimme a number ")
	if mustbeNumber == int or mustbeNumber == float:
		return mustbeNumber
	else:
		FetchNumbersOnly()

GetAndPrint();