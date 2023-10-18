import save_file2
#************AYAZ*********
import clear_com
import colorama
clear_com.clear()
from colorama import Fore
arr1 = []
arr2=[]
print(Fore.LIGHTRED_EX+"please enter ant number for arry items : (press * to finish) :")
while True:

   num= input(Fore.LIGHTMAGENTA_EX +"") 
   if num =="*" :
      break
   else :
      arr1.append(num)   
ind=int(len(arr1)/2)
arr2.append(arr1[0:ind])
arr2.append(arr1[ind:len(arr1)])
print(arr2)
save_file2.save_file(str(arr2),"output.txt")
part2=input(Fore.CYAN +"do you want to convert your list from 2 dimentionl to 1 dimentionl, y/n ?  ")
if part2=="y":
   arr3 =[]
   for x in arr2[0]:
      for x1 in x:
         arr3.append(x1)
   for y1 in arr2[1]:
      arr3.append(y1)
   print(arr3)

