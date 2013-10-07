README 

CalCalc (tries to) answers questions. 

Command line syntax: python CalCalc.py -question (insert question here) -search
The "-search" option will send the question directly to wolframalpha. If you leave it out, python's internal eval() will be tried first, as it is faster. If this fails, it will warn you and tell you it is searching wolframalpha for the answer to youre question.

In a python script, after you do "from CalCalc import calculate": calculate(question, True/False). True will use wolframalpha, False will try eval().

Ambiguous questions will be returned, and you will be asked to rephrase your question. You can do this as many times as you want, until you get an answer. 

To install, command line type: "python setup.py install" from within the respository.