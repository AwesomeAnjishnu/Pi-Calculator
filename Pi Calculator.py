#MIT License

#Copyright (c) 2023 Anjishnu Roy Choudhury

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.


#Requisition of Library
import time 

#Declaring our global variables that we are trying to find-
pi = 0
Pilist = []
accuracyLimit = 5000 
#Note: The accuracyLimit variable influences the accuracy of the value of pi produced. Try to keep 5000 as a minimum 
#Increase for more accurate results! 
#Further Note, a larger accuracyLimit would increase the computing time taken...
#An infinite value would make the computing time infinite!

#Getting an approximation of the summation of Pi/4
print('We will now be carrying out summation calculations, this may produce a string of nonsensical numbers. Kindly ignore them and wait for the final result!')
time.sleep(5)
while pi <= accuracyLimit:
    truePi = float(((-1)**(pi))/(2*(pi)+1))
    print(truePi)
    Pilist.append(truePi)
    pi = pi + 1
#print(Pilist)    
#Derving Sigma Summation of Pi
PiSum = 0
for i in range(0, len(Pilist)):    
   PiSum = PiSum + float(Pilist[i])
   PiResult = 4 * float(PiSum)    

#Conclusion
print('Value of pi found! Wait 5 seconds before results are displayed.')
time.sleep(5)
print(PiResult)
print('Hope this helped!')

#References 
#https://en.wikipedia.org/wiki/Leibniz_formula_for_π
#Thanks for reading, this sure as hell wasn't easy to code!
