import random
import datetime
import maskpass
def time():
     print("\t\t Delhi:  " ,datetime.datetime.now())
time()
def line():
     print("_"*80)
def captcha():
     print("Please fill up the below captcha so we know you're not a bot")
     f=""
     while True:
          for i in range(4):
               e=random.randrange(48,122)
               f+=chr(e)
          print(f)
          h=input("Enter the above captcha: ")     
          if h==f:
               print("You can access the next page")
               break
          else:
               f=""
               continue
def register_page():
     line()
     print("Welcome to MEDITATION WORLD!", "\nPlease give your details below to register your account")
     while True:
          pwd = maskpass.askpass(prompt = 'Enter the password->')
          if pwd == 'Admin':
               print('Password Unlocked!')
               line()
               #x=(input("Roll no. - ")
               #y=input("Class-Section - ")
               print("Namaste!"+'u"\u0905\u0928\u093F\u0915\u093E"')
                     #+"\nRoll no.- "+ x +"\nClass-Section: "+y)
               line()
               captcha()
               line()
               break
          else:
               print('You entered wrong password')
               break
