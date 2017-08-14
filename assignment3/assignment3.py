import string
def countSubStringMatch(target,key):
	locationsTuble = ()
	location = 0
	for x in range(0,int(len(target)/len(key))):
	    	if (string.find(target,key) >= 0):
	    		if(string.find(target,key,location) >= 0 ):
			    	location =  string.find(target,key,location) + len(key)
			    	locationsTuble = locationsTuble + ((location - len(key)),)
	return locationsTuble
	    	
        
st = countSubStringMatch('atgacatgcacaagtatgcat',"atg")
print st

# repeation = 0
# def countSubStringMatchRecursive(target,key,location):
# 	if (string.find(target,key,location) >= 0):
# 		global repeation
# 		repeation +=1
# 		return countSubStringMatchRecursive(target,key,string.find(target,key,location) + len(key))
# 	else:
# 		print repeation

# countSubStringMatchRecursive("abcabcdefacdafdsabc","abc",0)