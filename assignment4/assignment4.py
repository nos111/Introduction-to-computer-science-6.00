# def nestEggFixed(salary, save, growthRate, years):
# 	accountSizeEachYer = ()
# 	yearSavings = ((salary * save) / 100)
# 	savedMoney = 0
# 	print savedMoney
# 	for x in range(0,years ):
# 		savedMoney = savedMoney + (((savedMoney * growthRate)/100) + yearSavings)
# 		accountSizeEachYer = accountSizeEachYer + (savedMoney,)
# 		#print accountSizeEachYer

# nestEggFixed(10000,10,15,5)

def nestEggVariable(salary, save, growthRate):
 	accountSizeEachYer = ()
	yearSavings = ((salary * save) / 100)
	savedMoney = 0
	print savedMoney
	for x in range(0,len(growthRate) ):
		savedMoney = savedMoney + (((savedMoney * growthRate[x])/100) + yearSavings)
		accountSizeEachYer = accountSizeEachYer + (savedMoney,)
		print accountSizeEachYer
		

nestEggVariable(10000,10,[3, 4, 5, 0, 3])

# def postRetirement(savings, growthRate,expenses):
# 	accountSizeEachYer = ()
# 	accountEachYear = savings
# 	for x in range(0,len(growthRate)):
# 		accountEachYear = accountEachYear*(1 + 0.01 * growthRate[x]) - expenses
# 		accountSizeEachYer = accountSizeEachYer + (accountEachYear,)
# 		#print accountSizeEachYer

# postRetirement(100000,[10, 5, 0, 5, 1],30000)

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):
	accountSizeEachYer = ()
	yearSavings = ((salary * save) / 100)
	savedMoney = 0
	print savedMoney
	for x in range(0,len(preRetireGrowthRates)):
		savedMoney = savedMoney + (((savedMoney * preRetireGrowthRates[x])/100) + yearSavings)
		accountSizeEachYer = accountSizeEachYer + (savedMoney,)
		print accountSizeEachYer

	for i in range(0,accountSizeEachYer[-1]):
		accountEachYear = accountSizeEachYer[-1]
		accountSizeEachYer = ()
		for x in range(0,len(postRetireGrowthRates)):
				accountEachYear = (accountEachYear*(1 + 0.01 * postRetireGrowthRates[x])) - i
				accountSizeEachYer = accountSizeEachYer + (accountEachYear,)
		if accountSizeEachYer[-1] <= 0:
			print i
			print accountSizeEachYer[-1]
			print accountSizeEachYer
			break

findMaxExpenses(10000,10,[3,4,5,0,3],[10, 5, 0, 5, 1],0)
