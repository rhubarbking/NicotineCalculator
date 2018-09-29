#import the math and OS library
import math, os, platform, textwrap

#This is a Raise function
def Raise():
	if platform.system() == "Windows":
		os.system('cls')
	else:
		os.system('clear')
	PrintTitle()
	print (" 	    __________________");
	print ("	   |  RAISE NICOTINE  |");
	print ("	   |__________________|");
	print ("");
	print ("");
	# Get input from User
	OriginalVolume = raw_input("	Volume of the e juice you wish to raise the levels of (ml): ")
	# Make sure it is a number:
	try:
		OriginalVolume = float(OriginalVolume)
	except ValueError:
		# If it is not a number, start the process again
   		print("	That's not a number.")
   		if platform.system() == "Windows":
			os.system('pause')
		else:
			os.system('read -s -n 1 -p "	Press any key to try again..."')
   		Raise();
	print ("");

	OriginalStrength = raw_input("	Current strength of the e juice (mg/ml): ")
	try:
		OriginalStrength = float(OriginalStrength)
	except ValueError:
   		print("	That's not a number.")
   		if platform.system() == "Windows":
			os.system('pause')
		else:
			os.system('read -s -n 1 -p "	Press any key to try again..."')
   		Raise();
	print ("");

	DesiredStrength = raw_input("	Desired strength for the ejuice (mg/ml): ")
	try:
		DesiredStrength = float(DesiredStrength)
	except ValueError:
   		print("	That's not a number.")
   		if platform.system() == "Windows":
			os.system('pause')
		else:
			os.system('read -s -n 1 -p "	Press any key to try again..."')
   		Raise();
   	# Validate that the desired strength can't be less than the original strength
	if DesiredStrength <= OriginalStrength:
		print ("");
		print ("");
		print ("	You specify a desired nicotine level which is higher than what the juice currently is.");
		print ("");
		print ("");
		if platform.system() == "Windows":
			os.system('pause')
		else:
			os.system('read -s -n 1 -p "	Press any key to return to the menu..."')
		Menu();

	print ("");
	BaseNicStrength = raw_input("	Concentration of nicotine concentrate (mg/ml): ")
	try:
		BaseNicStrength = float(BaseNicStrength)
	except ValueError:
   		print("	That's not a number.")
   		if platform.system() == "Windows":
			os.system('pause')
		else:
			os.system('read -s -n 1 -p "	Press any key to try again..."')
   		Raise();
   	# Validate that the desired strength cannot be stronger than the concentrate
	if DesiredStrength > BaseNicStrength:
		print ("");
		print ("");
		print ("	Impossible - You cannot mix a higher nicotine level than the concentrate!");
		print ("");
		print ("");
		if platform.system() == "Windows":
			os.system('pause')
		else:
			os.system('read -s -n 1 -p "	Press any key to return to the menu..."');
		Menu();
	Mean = 1/BaseNicStrength;
	# The line beneath describes the amount of ejuice as if no base nic was ever added to it, based on the BaseNicStrength
	UndilutedVolume = OriginalVolume-(OriginalStrength*Mean);	
	print ("");
#	print ("Undiluted, the volume is " + str(UndilutedVolume) + " ml.");	
	AmountAlreadyInThere = float((OriginalStrength*Mean*UndilutedVolume));
	AmountAlreadyInThere = round(AmountAlreadyInThere, 2)
	print ("");
#		print ("	The equivilent amount of nic base (@ " + str(BaseNicStrength) + " per mg) which is already in there, is " + str(AmountAlreadyInThere) + "ml")
	TheoreticalAmountToAdd = float(((1/((BaseNicStrength/DesiredStrength)-1))*UndilutedVolume));
	AmountToAdd = TheoreticalAmountToAdd-AmountAlreadyInThere;
	AmountToAdd = round(AmountToAdd, 2)
#	print ("");
#	print ("");
#	print ("");
#	print ("");
	print ("		Total amount of " + str(BaseNicStrength) + "mg nicotine concentrate fluid to add, is ");
	print ("	==>	" + str(AmountToAdd) + "ml");
	print ("");
	print ("");
	TotalVolume = AmountToAdd+OriginalVolume
	TotalVolume = round(TotalVolume, 2)
	print ("		This will result in a total mixed volume of ");
	print ("	==>	" + str(TotalVolume) + "ml");
	print ("");
	print ("");
	print ("	Would you like to calculate the PG/VG ratio to use when mixing in the nicotine? YES/NO (NO will return to menu)");
	print ("");
	DoPGVG = raw_input("	");
	DoPGVG = DoPGVG.lower()
	if DoPGVG == "yes" or DoPGVG =="y":
		Pgvg(float(OriginalVolume), float(AmountToAdd), float(TotalVolume), "Raise");
	else:
		Menu();



#This function will calculate Dilution Ratios
def Dilute():
	if platform.system() == "Windows":
		os.system('cls')
	else:
		os.system('clear')
	PrintTitle()	
	print (" 	    __________________");
	print ("	   | DILUTE NICOTINE  |");
	print ("	   |__________________|");
	print ("");
	print ("");
	OriginalVolume = raw_input("	Volume of the e juice to be diluted (ml): ")
	try:
		OriginalVolume = float(OriginalVolume)
	except ValueError:
   		print("	That's not a number.")
   		if platform.system() == "Windows":
			os.system('pause')
		else:
			os.system('read -s -n 1 -p "	Press any key to try again..."')
		Dilute();
	print ("");
	OriginalStrength = raw_input("	Current strength of undiluted e juice (mg/ml): ")
	try:
		OriginalStrength = float(OriginalStrength)
	except ValueError:
   		print("	That's not a number.")
   		if platform.system() == "Windows":
			os.system('pause')
		else:
			os.system('read -s -n 1 -p "	Press any key to try again..."')
		Dilute();
	print ("");
	DesiredStrength = raw_input("	Desired diluted strength for the ejuice (mg/ml): ")
	try:
		DesiredStrength = float(DesiredStrength)
	except ValueError:
   		print("	That's not a number.")
   		if platform.system() == "Windows":
			os.system('pause')
		else:
			os.system('read -s -n 1 -p "	Press any key to try again..."')
		Dilute();
	if DesiredStrength > OriginalStrength:
		print ("");
		print ("");
		print ("	Cannot acheive a higher concentration by diluting it. You want to RAISE the nicotine content");
		print ("");
		print ("");
		if platform.system() == "Windows":
			os.system('pause')
		else:
			os.system('read -s -n 1 -p "	Press any key to return to the menu..."')
		Menu();
	else:
		print ("");
		AmountToAdd = ((OriginalStrength / DesiredStrength)*OriginalVolume)-OriginalVolume;
		AmountToAdd = round(AmountToAdd, 2)
		TotalVolume = AmountToAdd + OriginalVolume;
		TotalVolume = round(TotalVolume, 2)
		print ("");
		print ("		Amount of zero nicotine diluter to add: ");
		print ("	==>	" + str(AmountToAdd) + "ml");
		print ("");
		print ("		Total volume:");
		print ("	==>	" + str(TotalVolume) + "ml");
		print ("");
		print ("");
		print ("	Would you like to calculate the PG/VG ratio to use when making the diluter? YES/NO (NO will return to menu)");
		print ("");
		DoPGVG = raw_input("	");
		DoPGVG = DoPGVG.lower()
		if DoPGVG == "yes" or DoPGVG =="y":
			Pgvg(OriginalVolume, AmountToAdd, TotalVolume, "Dilute");
		else:
			Menu();



# This function calculates the PG VG ratio to use in the mixer, whether concentrating or diluting a mixture
def Pgvg(OriginalVolume, AmountToAdd, TotalVolume, Method):
#	print ("DEBUG! OriginalVol = " + str(OriginalVolume) + " AmountToAdd = " + str(AmountToAdd) + " TotalVol = " + str(TotalVolume));
	print ("");
	if Method == "Dilute":
		print ("	What is the current PG % of the undiluted volume?");
	elif Method == "Raise":	
		print ("	What is the current PG % of the juice to be strengthened?");
	else:
		print ("	What is the current PG % of the original volume?");
	OriginalPGPercent = raw_input("	")
	try:
		OriginalPGPercent = float(OriginalPGPercent)
	except ValueError:
   		print("	That's not a number.")
   		if platform.system() == "Windows":
			os.system('pause')
		else:
			os.system('read -s -n 1 -p "	Press any key to try again..."')
		Pgvg(OriginalVolume, AmountToAdd, TotalVolume, Method);
	print ("");
	CurrentPGMils = OriginalVolume * (OriginalPGPercent/100)
	LeastPossPGPercent = ((OriginalVolume * (OriginalPGPercent/100))/TotalVolume)*100
	MaxPossPGPercent = ((OriginalVolume * (OriginalPGPercent/100) + AmountToAdd)/TotalVolume)*100
	print ("");
#	print ("*** DEBUG - MaxPossPGPercent = " + str(MaxPossPGPercent) + " MinPossPGPercent = " + str(LeastPossPGPercent));
	print ("	Please enter the desired percentage of PG. Please note - only possible range is between " + str(math.ceil(LeastPossPGPercent)) + " percent, and " + str(math.floor(MaxPossPGPercent)) + " percent.");
	print ("");

	DesiredRatio = raw_input("	Please enter an integer which is within range above: ")
	try:
		DesiredRatio = float(DesiredRatio)
	except ValueError:
   		print("	That's not a number.")
   		if platform.system() == "Windows":
			os.system('pause')
		else:
			os.system('read -s -n 1 -p "	Press any key to try again..."')
		Pgvg(OriginalVolume, AmountToAdd, TotalVolume, Method);
	if DesiredRatio <= MaxPossPGPercent and DesiredRatio >= LeastPossPGPercent:
		MlOfPgToAdd = (DesiredRatio/100)*TotalVolume - CurrentPGMils;
		MixerPGPercent = (MlOfPgToAdd/AmountToAdd) * 100
		MixerVGPercent = 100-(MlOfPgToAdd/AmountToAdd)*100	
		if MixerPGPercent > MixerVGPercent:
			MixerPGPercent = math.floor(MixerPGPercent)
			MixerVGPercent = math.ceil(MixerVGPercent)
		else:
			MixerPGPercent = math.ceil(MixerPGPercent)
			MixerVGPercent = math.floor(MixerVGPercent)
		print ("");
		if Method == "Dilute":
			print ("		The ratio you want your diluter to be, is " + str(MixerPGPercent) + "% PG / " + str(MixerVGPercent) + "% VG")
		elif Method == "Raise":	
			print ("		The ratio you want your nicotine concetrate to be, is " + str(MixerPGPercent) + "% PG / " + str(MixerVGPercent) + "% VG")
		else:
			print ("		The ratio make the concentrate or diluter, is " + str(MixerPGPercent) + "% PG / " + str(MixerVGPercent) + "% VG")
		print ("");
		if platform.system() == "Windows":
			os.system('pause')
		else:
			os.system('read -s -n 1 -p "	Press any key to return to the menu..."')
		Menu();
	else:
		print ("	Sorry, that ratio is not acheivable. It must be within the possible range. Let's try again")
		print ("")
		if platform.system() == "Windows":
			os.system('pause')
		else:
			os.system('read -s -n 1 -p "	Press any key to try again..."')
		Pgvg(OriginalVolume, AmountToAdd, TotalVolume, Method);



#This is the Menu
def Menu():
	if platform.system() == "Windows":
		os.system('cls')
	else:
		os.system('clear')
	PrintTitle()	
	print (" 	    __________________");
	print ("	   |       MENU       |");
	print ("	   |__________________|");
	print ("");
	print ("	Please type one of the following and press enter:")
	print ("");
	print ("	'r' to RAISE the nictotine in a juice")
	print ("	'd' to DILUTE a juice");
#	print ("	'pgvg' to calculate ratios");
	print ("	'q' to QUIT")
	print ("")
	MenuSelection = raw_input("	Selection: ")
	MenuSelection = MenuSelection.lower();
	if MenuSelection == 'r':
		Raise();
	elif MenuSelection == 'd':
		Dilute();
	elif MenuSelection == 'q':
		# Application Exit
		if platform.system() == "Windows":
			os.system('cls')
		else:
			os.system('clear')
		print ("")
		print ("...Goodbye! Happy Vaping :)")
		print ("")
		raise SystemExit;
	elif MenuSelection == "pg":
		Pgvg(10, 16, 26, "Blank");
	else:
		#Validation
		print ("")
		print ("	Does not compute! BEEP BEEP!")
		print ("")
		if platform.system() == "Windows":
			os.system('pause')
		else:
			os.system('read -s -n 1 -p "	Press any key to try again..."')
		Menu();

def PrintTitle():
	print ("")
	print ("""\
	            __      _              ______      __           __      __            
	  ___      / /_  __(_)_______     / ____/___ _/ /______  __/ /___ _/ /_____  _____
	 / _ \__  / / / / / / ___/ _ \   / /   / __ `/ / ___/ / / / / __ `/ __/ __ \/ ___/
	/  __/ /_/ / /_/ / / /__/  __/  / /___/ /_/ / / /__/ /_/ / / /_/ / /_/ /_/ / /    
	\___/\____/\__,_/_/\___/\___/   \____/\__,_/_/\___/\__,_/_/\__,_/\__/\____/_/     
	""")

#Initial App startup
Menu();

