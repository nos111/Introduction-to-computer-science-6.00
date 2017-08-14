"""
This is a basic model of the greedy algorithm
everytime is evaluated to take the item or not based on it's value and what fits in the bag
It's made for chosing the courses with the biggest value with the avaiable
amount of time


"""
def greedyAdvisor(subjects, maxWork, comparator):
    #find the minimum value of the working hours so we can stop when we hit it.
    subjects_keys = subjects.keys()
    work_hours = []
    for key in subjects_keys:
        work_hours.append(subjects[key][1])
    minimum_working_hours = min(work_hours)
    #introduce answer and condition with true
    chosen_subjects = {}
    #introduce iterator
    i = 1
    hold = 0
    #do a while maxwork is bigger than 0
    while maxWork > 0:
        #build the keys list
        keys = subjects.keys()
        print 'list length is ',len(keys), 'and iterator is at ',i
        #check if the list is only one item than we are done
        if len(keys) == 1:
            #can we still add this item to the chosen subjects?
            if subjects[keys[0]][1] <= maxWork:
                    maxWork = maxWork - subjects[keys[hold]][1]
                    print 'Max work is now ', maxWork
                    chosen_subjects[keys[hold]] = subjects[keys[hold]]
                    del subjects[keys[hold]]
                    print chosen_subjects
                    return chosen_subjects
            #if not return the chosen subjects list
            else:
                print chosen_subjects
                return chosen_subjects
            
        #check the first two items of the subjects
        max_value = comparator(subjects[keys[hold]],subjects[keys[i]])
        #if the first item is bigger continue with comparision
        #and make sure the list is not over
        if max_value == True:
            print subjects[keys[hold]],subjects[keys[i]],'comparision is true'
            print 'max work is ',maxWork
            
            #check if we have reached the end of the list
            if i + 1 >= len(keys):
                #if the value is bigger than max work delete the course from the list
                if subjects[keys[hold]][1] > maxWork:
                    i = 1
                    hold = 0
                    print 'Removed ', subjects[keys[hold]]
                    del subjects[keys[hold]]
                    continue
                #if we have than minus from max work(if possible) and add the subject to chosen
                if subjects[keys[hold]][1] <= maxWork:
                    maxWork = maxWork - subjects[keys[hold]][1]
                    print 'Max work is now ', maxWork
                    chosen_subjects[keys[hold]] = subjects[keys[hold]]
                    if maxWork < minimum_working_hours:
                        print 'luckely ended computation earlier because of low MaxWork'
                        print chosen_subjects
                        return chosen_subjects
                        
                    #remove this item because it's bigger than maxwork now
                    del subjects[keys[hold]]
                    #reset the counters to start comparing
                    i = 1
                    hold = 0
                    continue
            #continue iteration if no valid situation is found
            i += 1
                
        #if the second item is bigger(false) make the holder the second item
        #check first to make sure we are not at the end of the list
        #if we are at the end of the list than we need to make the second decision tree with a
        #take of the values on the other hand
        if max_value == False:
            print subjects[keys[hold]],subjects[keys[i]],'comparision is false'
            if i + 1 >= len(keys):
                #if the value is bigger than max work delete the course from the list
                if subjects[keys[i]][1] > maxWork:
                    i = 1
                    hold = 0
                    print 'Removed ', subjects[keys[i]]
                    del subjects[keys[i]]
                    continue
                #if we have than minus from max work(if possible) and add the subject to chosen
                if subjects[keys[i]][1] <= maxWork:
                    maxWork = maxWork - subjects[keys[i]][1]
                    print 'Max work is now ', maxWork
                    chosen_subjects[keys[i]] = subjects[keys[i]]
                    if maxWork < minimum_working_hours:
                        print 'luckely ended computation earlier because of low MaxWork'
                        print chosen_subjects
                        return chosen_subjects
                    #remove this item because it's bigger than maxwork now
                    del subjects[keys[i]]
                    #reset the counters to start comparing
                    i = 1
                    hold = 0
                    continue
            #continue iteration if no valid situation is found
            hold = i
            i += 1
            print 'next comparision is ', subjects[keys[hold]],subjects[keys[i]]

    print chosen_subjects

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
        
smallCatalog = {'6.00': (16, 8),'1.00': (7, 7),'2.00': (20,6),'6.01': (5, 3),'15.01': (9, 6)}
greedyAdvisor(smallCatalog,15,cmpValue)

