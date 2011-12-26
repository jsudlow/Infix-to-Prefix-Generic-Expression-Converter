#!/usr/bin/python

import os

import subprocess as sub

class GP_Function:
    def __init__(self,name,commands):
        self.name = name
        self.infix_commands = commands
        self.prefix_commands = []

    def infix_to_prefix(self):
        for strings in self.infix_commands:
            command = "./infix_prefix.py -s' %s'" % strings
            #print "Commands: ", command , "\n"
            p = os.popen(command,"r")
            
            conversion_string = ""

            while 1:
                line = p.readline()
                if not line: break
                print "line: ",line
                conversion_string += line.rstrip("\r\n")
            self.prefix_commands.append(conversion_string)

        


max_commands = ['a+b*c','a-c+d']
max = GP_Function('max', max_commands)
max.infix_to_prefix()
print max.prefix_commands


