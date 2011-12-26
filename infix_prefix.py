#!/usr/bin/python
import string,argparse
from stack import Stack

#algorithm for infix to prefix. Strung out if statements ground in a for loop of mince meat for the masses

#init an empty list to store output
output = []


#define a precedence dictionary to look up values
prec = {}
prec['*'] = 3
prec['/'] = 3
prec['-'] = 2
prec['+'] = 2
prec['('] = 1
prec[')'] = 1
#define a function to retrieve our infix string from the command line. Argparse is awesome, so why done we use it??
def parse_args():
        parser = argparse.ArgumentParser()
        parser.add_argument('-s', action='store',dest='infix_string',help="use infix_prefix.py -s 'A * (B+ C)' ",required=True)
        return parser.parse_args()

#get our arguments in a neat result variable
results = parse_args()

#lets split our string directly from the results variable
split_infix_string = results.infix_string

print 'infix stringzee to be proccessed: ',split_infix_string
#test our infix string out
#print split_infix_string
operatorStack = Stack()
operandStack = Stack()


for token in split_infix_string:
    print "First Token thru: ",token,"\n"
    if token.isalpha() or token in ['+','-','/','*',')','(']:
        if token.isalpha():
            operandStack.push(token)
            print 'Pushing Operand:',token,"\n"
        elif token == '(' or operatorStack.is_empty() or (prec[token] >= prec[operatorStack.peek()]):
                print 'pushing token: ', token, "\n"
                operatorStack.push(token)
        elif token == ')':
            print 'right paren found'
            while(operatorStack.peek() != '('):
                operator = operatorStack.pop()
                right = operandStack.pop()
                left = operandStack.pop()
                operand = operator + left + right
                operandStack.push(operand)
            operatorStack.pop()    
            
        elif prec[token] <= prec[operatorStack.peek()]:
            while( not operatorStack.is_empty() and prec[token] <= prec[operatorStack.peek()]):
                operator = operatorStack.pop()
                right = operandStack.pop()
                left = operandStack.pop()
                operand = operator + left + right
                operandStack.push(operand)
                  
            operandStack.push(token)    

while (not operatorStack.is_empty()):
    operator = operatorStack.pop()
    right = operandStack.pop()
    left = operandStack.pop()
    operand = operator + left + right
    operandStack.push(operand)

print operandStack.peek()


