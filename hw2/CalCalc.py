#import my modules 
import os
import sys
import argparse
import urllib2
from xml.dom.minidom import parseString

def calculate(question,search):
    """ Pass it your question. For search option, True uses wolframalpha, false uses Python's eval().
        You need to put your quesetion as a string. If eval() can't find answer, it will try with wolframalpha
        example sytax caclulate('tallest man alive', True)"""
    appid = '9RVGAP-TWG3EKG2W5'
    if search == False:
        try: 
            if question.find('os.') != -1: #don't let anyone use os calls, protect from deleting my files
                print "We don't do OS calls, try again!" 
                output = 1.0
                return output
            else:
                output = eval(question)
                return output
                print output
        except (NameError,SyntaxError): #this should appropriately catch errors from eval() not finding answer
            print 'Pythons eval() could not find answer, searching the internet with wolframalpha'
            while True:
                try:
                    query = question
                    print 'You asked the internet: ' + question
                    file = urllib2.urlopen('http://api.wolframalpha.com/v2/query?input=' + urllib2.quote(query, "") + '&' + 'appid=' + appid)
                    data = file.read()
                    dom = parseString(data)
                    xmlTag = dom.getElementsByTagName("plaintext")[1].toxml()
                    xmlData = xmlTag.replace("<plaintext>", "").replace("</plaintext>", "")
                    output = xmlData
                    file.close()
                    print output
                    return output
                    break
                except IndexError:
                    print "Your question is too ambiquous. Try again!"
                    question = raw_input("Give me a new, less ambiquous, question: ")
    else:
        while True:
            try:
                query = question
                print 'You asked the internet: ' + question
                file = urllib2.urlopen('http://api.wolframalpha.com/v2/query?input=' + urllib2.quote(query, "") + '&' + 'appid=' + appid)
                data = file.read()
                dom = parseString(data)
                xmlTag = dom.getElementsByTagName("plaintext")[1].toxml()
                xmlData = xmlTag.replace("<plaintext>", "").replace("</plaintext>", "")
                output = xmlData
                file.close()
                print output
                return output
                break
            except IndexError:
                print "Your question is too ambiquous. Try again!"
                question = raw_input("Give me a new, less ambiquous, question: ") 



def test1(): #really basic math in eval()
    assert abs(4. - calculate('2**2', False)) < .001
def test2(): #really basic math in wolframalpha
    assert abs(4. - float(calculate('2**2', True))) < .001
def test3(): #equality of math across wolframalpha and eval()
    assert abs(4. - float(calculate('2**2', True))) == abs(4. - calculate('2**2', False))
def test4(): #pass something eval can't handle to wolframalpha
    assert calculate('distance new york to san francisco', True)  == '2577 miles'
def test5(): #pass same thing to eval(), making sure it gets sent to wolframalpha and computed properly
    assert calculate('distance new york to san francisco', False)  == '2577 miles'
def test6(): #ask about some philosophy, trying with eval(), knowing it will pass it to wolframalpha
    assert calculate('what is symbolic logic', False) == 'The study of the meaning and relationships of statements used to represent precise mathematical ideas. Symbolic logic is also called formal logic.'
def test7(): #make sure my os saftey net is working 
    assert calculate('os.removesstuff', False) == 1.0
def test8(): #works from command line
    assert os.system('python CalCalc.py -question "how many miles in a lightyear" -search') == 0
def test9(): #works from command line, even if eval can't handle it. 
    assert os.system('python CalCalc.py -question "how many miles in a lightyear"') == 0
def test10(): #works from command line using eval 
    assert os.system('python CalCalc.py -question "7*7"') == 0 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculation Module')
    parser.add_argument('-question', action='store', dest='question',
                        help='Enter a question or equation')
    parser.add_argument('-search', action='store_true', default=False,
                        dest='search',
                        help='Do you want to search the internet for your answer?')
    results = parser.parse_args()
    result = calculate(results.question, results.search)




