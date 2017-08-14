import ps10; reload(ps10)
from ps10 import *

def isClose(float1, float2):
    """
    Helper function - are two floating point values close?
    """
    return abs(float1 - float2) < .01

def testResult(boolean):
    """
    Helper function - print 'Test Failed' if boolean is false, 'Test
    Succeeded' otherwise.
    """
    if boolean:
        print 'Test Succeeded'
    else:
        print 'Test Failed'

def testHand():
    """
    Test the hand class. Add your own test cases
    """
    h = Hand(8, {'a':3, 'b':2, 'd':3})
    h.update('bad')
    testResult(h.containsLetters('aabdd') and not h.isEmpty())
    h.update('dad')
    testResult(h.containsLetters('ab') or not h.isEmpty())
    h.update('ab')
    print h.isEmpty()
    testResult(h.isEmpty())

    h = Hand(14, {'a':3, 'm':2,'x':1,'f':1,'u':1,'r':2,'y':1,'o':1, 'd':2})
    h.update('mad')
    testResult(h.containsLetters('maxfuryroad') and not h.isEmpty())
    h.update('max')
    testResult(h.containsLetters('furyroad') or not h.isEmpty())
    h.update('fury')
    testResult(h.containsLetters('road') or not h.isEmpty())
    h.update('road')
    print h.isEmpty()
    testResult(h.isEmpty())

def testPlayer():
    """
    Test the Player class. Add your own test cases.
    """
    p = Player(1, Hand(6, {'c':1, 'a':1, 'b':1 ,'d':1, 'o':1, 'e':1}))
    testResult(type(p.getHand()) == Hand)
    p.addPoints(5.)
    p.addPoints(12.)
    testResult(isClose(p.getPoints(), 17))
    p = Player(2, Hand(6, {'c':3, 'a':1, 'b':1 ,'d':1, 'o':1, 'e':1}))
    testResult(type(p.getHand()) == Hand)
    p.addPoints(5.)
    p.addPoints(12.)
    testResult(isClose(p.getPoints(), 17))

def testComputerPlayer():
    """
    Test the ComputerPlayer class. Add your own test cases.
    """
    wordlist = Wordlist()
    p = ComputerPlayer(1, Hand(30, {'a':2, 'c':1, 'b':1 ,'e':3, 'd':1,'g':2,'i':2,'h':2,'o':1,'n':3,'p':1,'s':1,'r':1,'u':2,'w':3,'v':1,'x':2,'z':1}))
    print p.pickBestWord(wordlist)
    testResult(getWordScore(p.pickBestWord(wordlist)) == getWordScore('bobbed'))

def testAll():
    """
    Run all Tests
    """

    #print "Uncomment the tests in this file as you complete each problem."

    #print 'PROBLEM 2 -----------------------------------------'
    #testHand()

    #print 'PROBLEM 3 -----------------------------------------'
    #testPlayer()

    # print 'PROBLEM 4 -----------------------------------------'
    testComputerPlayer()

testAll()
