import requests
import random
import os 
import time

def hama():
 os.system("clear")
 username = 'dino'
 password='ani'
 print("Tkaya username tolaka bnwsa")
 print("--------")
 user=input("username :")
 os.system("clear")
 print("Tkaya password bnwsa ")
 print("--------")
 pas=input("password : ")
 if user==username and pas==password:
  time.sleep(2)
  print(" \033[1;32m login buy✓ \033[1;37.")
  time.sleep(3)
 else:
  print(" \033[1;31m xalata × \033[1;37m ")
  time.sleep(3)
  hama()
  
  

os.system("clear")
def ani():
 os.system("clear")
 hama="""\033[1;36m
########  #### ##    ##  #######  
##     ##  ##  ###   ## ##     ## 
##     ##  ##  ####  ## ##     ## 
##     ##  ##  ## ## ## ##     ## 
##     ##  ##  ##  #### ##     ## 
##     ##  ##  ##   ### ##     ## 
########  #### ##    ##  #######  

 \033[1;37m
 """
 print(hama)
 print("---------------------")
 op=open("user5.txt","w")
 anii=open("user5.txt","r").readlines()
 user=int(input(  "\033[1;32m chand user bet:  \033[1;37m"))
 for hama in range(user):
        d='qwer12i5678_opasdfghj9klmnbvcxz0'
        d1=random.choice(d)
        d2=random.choice(d)
        d3=random.choice(d)
        d4=random.choice(d)
        d5=random.choice(d)
        dino=d1+d2+d3+d4+d5
        print(dino)
        op.write(dino+"\n")
        print("")
        
        print(" \033[1;32m ------------------- \033[1;37m")
 print("\033[1;32m HAMU USERAKAN LA FILE USER5.TXT NUSRANAWA \033[1;37m")

def fahskrdn():
 os.system("clear")
 hama="""
      _ _             
    | (_)            
  | |_ _    _  
 / _` | | '_ \ / _ \ 
| (_| | | | | | (_) |
 \,_|_|_| |_|\___/ 
 
 
 """
 print(hama)
 print("----------")
 print("WAIT ")
 print("----------")
 op=open("user5.txt","r").readlines()
 for hama in op:
  u=hama.strip()
  re =requests.get('https://www.instagram.com/'+u).status_code
  if re==200:
   print("")
   print(u+"=\033[1;31m aw usera   haya ×  ")
   print("")
  else:
   print("")
   print(u+"=\033[1;32m aw usera  nya ✓ \033[1;37m")
   print("")
hama()
#password()
ani()
fahskrdn()
time.sleep(5)