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
#https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
#Thanks for reading, this sure as hell wasn't easy to code!