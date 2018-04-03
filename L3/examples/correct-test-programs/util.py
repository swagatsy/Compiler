import sys

class Node:
    def __init__(self):
        self.list = []

    def addChild(self,node):
        self.list.append(node)
        
    def printTree(self, x=0):
        s=""
        for i in range(x):
            s+='\t'
        s+=self.value
        print s
        if len(self.list)==0:
            return
        s1=""
        for i in range(x):
            s1+='\t'
        s1+='('
        print s1
        k=0
        for node in self.list:
            if (k!=0):
                s2=""
                for i in range(x+1):
                    s2+='\t'
                s2+=","
                print s2
            k+=1
            node.printTree(x+1)
        s3=""
        for i in range(x):
            s3+='\t'
        s3+=')'
        print s3
        # log = open("text.txt", "w")
        # print >>log, s 