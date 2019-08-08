class cmdGen:
	def __init__(self):
		self.out = ""
		self.begin = True
		self.firstArg = True
	def clearStr(self):
		self.__init__()
		self.input = ""
	def addToken(self, STR):
		self.input = self.input + STR
	def parse(self):
		self.tmp = self.input.split(',')
		for item in self.tmp:
			item = item.split(':')
			if(len(item)==1 or item[1]=='off'): #len(item)==1 --> nothing behind some option
				continue
			else:
				if(self.begin==True):		#beginning
					self.out += item[0].strip("[]\'")
					self.out += ' '
					self.out += item[1].strip("[]\'")
					self.begin = False
				elif('arg' in item[0].strip("\'")   and   self.firstArg==True): #arg1
					self.firstArg = False
					self.out += item[1].strip("[]\'") #append the item to the option directly
				elif('arg' in item[0].lower()):		#arg2+
					self.out += " "
					self.out += item[1].strip("[]\'")
				elif('opt' in item[0].lower()):
					self.out += " "
					self.out += item[1].strip("[]\'")
				else: #others
					self.firstArg = True
					self.out += " "
					self.out += item[0].strip("[]\'")
					self.out += ' '
					self.out += item[1].strip("[]\'")
		#print(self.out)
		return self.out

	#def getCmd(self, cmd):


#test = cmdGen("[-CPU:'cpu1', -MEM:'mem1', -POW:'pow1', option1:'-a', option2:'-h', OPT1:'--color=', arg1:'always', arg2:'never']")
#test.parse()


#before                     [-CPU:"cpu1", -MEM:"mem1", -POW:"pow1", option1:'-a', option2:'-h', OPT1:'--color=', arg1:'always', arg2:'never']
#splitted 					['CPU:1', 'MEM:'foo'', 'POW:'z'', 'option1:'three'', 'option2:'test'', 'OPT1:'--color='', 'arg1:'asdf'', 'arg2:'zxcv'']