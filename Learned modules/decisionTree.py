#this is a basic example of the decision tree coding
#it's clean and basic so I can always return to it
#this decision tree represent the knapsack problem
#it has two branches: No take, Take
#it uses recursion
#takes weight,value,item,available weight as parameters
#returns the best value

def maxValue (w,v,i,aw):
    print 'max value called with ', i , aw
    global numCalls
    numCalls += 1
    if i == 0:
        if w[i] <= aw: return v[i]
        else: return 0
    without_i = maxValue(w,v, i - 1,aw)
    if w[i] > aw:
        return without_i
    else:
        with_i = v[i] + maxValue(w, v, i - 1, aw - w[i])
    return max(with_i, without_i)

            
