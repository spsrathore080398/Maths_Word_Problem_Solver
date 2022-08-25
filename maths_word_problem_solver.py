# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 13:07:00 2020

@author: Shiv Pratap Singh Rathore
"""

import tkinter as tk
import tkinter.font as font
master=tk.Tk()
master.title("Maths Word Problem Solver")
myFont=font.Font(size=30)

a=tk.Label(master,text="Enter  your question",).grid(row=0)
e1=tk.Entry(master,width=80,font=("Helvetica",28))
e1.grid(row=0,column=1)

t=tk.Text(master,width=25,height=1,font=("Helvetica",32))
t.grid(row=25,column=1)
def clickButton():
    text=e1.get()
    class Tree(object):
	    def __init__(self,data):
	        self.data=data
	        self.children=[]
	
    def childismax(obj): 	
        if obj.data in ["subtraction","division"]:
            maxchild=2
        elif obj.data in ["sum","multiplication","lcm"]:
            return False
        elif obj.data=="square":
            maxchild=1
        else :
            maxchild=0
        count=len(obj.children)
        if count < maxchild :
            return False
        else :
            return True 
    entries=[] 
    input1=text.lower()
    input1=input1.replace(',',' ')
    print(input1)
    abc=list(input1.split(" "))
    operations=["sum","subtraction","multiplication","division","square","lcm","percentage"]
    li=[]
    for j in abc :
        if j in operations or j.isdigit():
            li.append(j)  
    for j in li :
        a=Tree(j)
        for i in reversed(entries):
            if childismax(i):
                continue		
            else:
                i.children.append(a)
                break
        entries.append(a)
			    
	    
	
    for j in reversed(entries):
	    if j.data.isdigit():
		    j.data=int(j.data)
		    continue
	    else :
                
		    if j.data=="square":
			    for k in j.children:
				    a=int(k.data)
			    j.data=a*a

                
                
		    elif j.data=="sum":
			    sum=0
			    for k in j.children:
			       p=int(k.data)
			       sum=sum+p
			    j.data=sum
			
		    elif j.data=="subtraction":
			    operands=[]
			    for k in j.children:
                    
			       p=int(k.data)
			       operands.append(p)
			    a=operands[0]
			    b=operands[1]
			    j.data=b-a
			
		    elif j.data=="multiplication":
			    mul=1
			    for k in j.children:
			   	         p=int(k.data)
			   	         mul=mul*p
			    j.data=mul    
		
		    elif j.data=="division":
			    operands=[]
			    for k in j.children:
			       p=int(k.data)
			       operands.append(p)
			    a=operands[0]
			    b=operands[1]
			    j.data=a/b
                          
                     
                
		    elif j.data=="lcm":
			    operands=[]
			    for k in j.children:
				    p=int(k.data)
				    operands.append(p)
			    operands.sort(reverse=True)
			    a=operands[0]
			    x=1;z=1
			    while(1):
				    b=a*x
				    for y in operands :
					    if b%y==0:
						    z=1
					    else :
						    z=0
						    break
				    if z==0:
					    x=x+1
				    if z==1:
					    break
			    j.data=b
            

           
                
            
                
            
            
                                      
                
                
                
                
            
                
    
  out=(entries[0].data)
  t.insert(tk.END,out)
        


					
			
		



b=tk.Button(master,text="Solve",command=clickButton,font=("Helvetica",32)).grid(row=13,column=1)



master.mainloop()
