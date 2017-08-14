# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#
import json
import time
import copy

SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """
    #define the dictionary of the mapped courses
    subjects_dic = {}
    # The following sample code reads lines from the specified file and prints
    # each one.
    inputFile = open(filename)
    for line in inputFile:
        #remove the white space from eachline
        line = line.strip()
        #split the line to a list of items
        line = line.split(',')
        #the first value should be a string which is the name of the course
        subjects_dic[line[0]] = int(line[1]),int(line[2])        
        #inside the the name of the course is a tuble with the value and hours

    return subjects_dic
        
    # done: Instead of printing each line, modify the above to parse the name,
    # value, and work of each subject and create a dictionary mapping the name
    # to the (value, work).




def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2

#
# Problem 2: Subject Selection By Greedy Optimization
#
def greedyAdvisor(subjects, maxWork, comparator,memo):
    """
    The idea is to map the whole dictionary I have with a ranking depending on their valuses
    this way I can chose the subject I want to delete very fast and with minimum calculations
    """
    subjects_keys = subjects.keys()
    work_hours = []
    for key in subjects_keys:
        work_hours.append(subjects[key][1])
    minimum_working_hours = min(work_hours)
    global s
    s = 0
    chosen_subjects = {}
    memo[len(subjects_keys)] = copy.deepcopy(subjects)
    counter = len(memo[len(subjects_keys)])
    z = 1
    
    while maxWork > 0:
        try:
            memo[1]
            print memo[1]
            sorted_keys = sorted(memo.keys())
            for x in sorted_keys:
                #print 'Before sorting',memo[x].keys()
                subject_keys = sorted(memo[x].keys(), key = lambda subject: memo[x][subject][1])
                #print subject_keys
                
                                      
                for t in range(0,len(memo[x].keys())):
                    s+=1
                    if memo[x][memo[x].keys()[t]][1] < maxWork:
                        maxWork = maxWork - memo[x][memo[x].keys()[t]][1]
                        chosen_subjects[memo[x].keys()[t]] =  memo[x][memo[x].keys()[t]]
            return chosen_subjects
        except KeyError:
            keys = memo[counter].keys()
            i = 0
            memo[counter/2] = {}
            for x in range (0, counter/2):     
                checker = comparator(memo[counter][keys[i]],memo[counter][keys[i + 1]])
                #print 'checker is ',checker , 'for ',memo[counter][keys[i]],memo[counter][keys[i + 1]]
                if checker == False:
                    memo[counter/2][keys[i + 1]] = {}
                    memo[counter/2][keys[i + 1]] = memo[counter][keys[i + 1]]
                if checker == True:
                    memo[counter/2][keys[i]] = {}
                    memo[counter/2][keys[i]] = memo[counter][keys[i]]
                
                i +=2
            counter = counter / 2
##        if maxWork < minimum_working_hours:
##            #print 'luckely ended computation earlier because of low MaxWork'
##            #print chosen_subjects
##            return chosen_subjects
##        #check if we have one item left
##        #check if we can substract it
##        #remove it from the subjects and substract
##        if len(refined_list.keys()) == 1:
##            if refined_list[refined_list.keys()[0]][1] <= maxWork:
##                maxWork = maxWork - refined_list[refined_list.keys()[0]][1]
##                #print 'max work is now ', maxWork
##                chosen_subjects[refined_list.keys()[0]] = refined_list[refined_list.keys()[0]]
##                #print chosen_subjects
##                del subjects[refined_list.keys()[0]]
##                refined_list = copy.deepcopy(subjects)
##            if refined_list[refined_list.keys()[0]][1] > maxWork:
##                del subjects[refined_list.keys()[0]]
##                refined_list = copy.deepcopy(subjects)
##        if len(refined_list.keys()) < 1:
##            #print chosen_subjects
##            return chosen_subjects
##        else:  
##            #find the subjects keys
##            keys = refined_list.keys()
##            #compare every two elements
##            i = 0
##            #print 'length of possibilities is ', len(keys)
##            for x in range (0, len(keys)/2):
##                try:
##                    checker = memo[keys[i] + keys[i+1]]
##                except KeyError:
##                    checker = comparator(refined_list[keys[i]],refined_list[keys[i+1]])
##                    memo[keys[i] + keys[i+1]] = checker
##                #print 'checker is ',checker , 'for ',refined_list[keys[i]],refined_list[keys[i+1]]
##                if checker == False:
##                    del refined_list[keys[i]]
##                if checker == True:
##                    del refined_list[keys[i + 1]]
##                #print refined_list
##                i +=2
##        s += 1
##    
##    return chosen_subjects
        

def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = subjects.keys()
    tupleList = subjects.values()
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue

#
# Problem 3: Subject Selection By Brute Force



#
def bruteForceTime():
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    # TODO...
    smallCatalog = copy.deepcopy(subjects_dic)
    begin = time.time()
    chosen = greedyAdvisor(smallCatalog, 15, cmpWork)
    end = time.time()
    printSubjects(chosen)
    #print 'Calculated in ',end - begin
    smallCatalog = subjects_dic
    begin_brute = time.time()
    chosen_brute = bruteForceAdvisor(smallCatalog, 15)
    end_brute = time.time()
    printSubjects(chosen_brute)
    #print 'calculated in ',end_brute - begin_brute

# Problem 3 Observations
# ======================
#
# TODO: write here your observations regarding bruteForceTime's performance
"""
First test:
on a list of 50 courses the two methods were tested.
The greedy method finished in 0.0310001373291
the brute force method finished in 0.285000085831

Second test:
The bruteforce method and the greedy method were tested on a list of 320 courses.
The greedy method solved the problem in 0.0130000114441
I have waited for the brute force to finish for 53 minutes. And it didn't finish.
On second try:
The greedy method finished in 0.0149998664856
I have waited for hte brute force for 26 minutes to finish and still didn't get an answer


"""
#
# Problem 4: Subject Selection By Dynamic Programming
#
def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """


    

#
# Problem 5: Performance Comparison
#
def dpTime():
    """
    Runs tests on dpAdvisor and measures the time required compute an answer.
    """
    # TODO...

# Problem 5 Observations
# ======================
#
# TODO: write here your observations regarding dpAdvisor's performance and
# how its performance compares to that of bruteForceAdvisor.

if __name__ == '__main__':
    #subjects_dic = loadSubjects(SUBJECT_FILENAME)
    with open('data.txt') as json_data:
        subjects_dic = json.load(json_data)
    #smallCatalog = subjects_dic
    smallCatalog = {'6.00': (16, 8),'1.00': (7, 7),'6.01': (5, 3),'15.01': (9, 6)} 
    dpAdvisor(smallCatalog,15)
##    keys = smallCatalog.keys()
##    print 'List length is ', len(keys)
##    begin = time.time()
##    memo = {}
##    chosen = greedyAdvisor(smallCatalog, 30, cmpValue,memo)
##    end = time.time()
##    printSubjects(chosen)
##    print 'Calculated in ',end - begin
##    print 'Iterated ', s

    
