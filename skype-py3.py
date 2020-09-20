from skpy import Skype, SkypeEventLoop, SkypeNewMessageEvent
import stdiomask
import time
import requests
from bs4 import BeautifulSoup

def send_message(sk):    
    # Create new/existing conversation with contact/skype name
    # ch = sk.chats.create(['riza.irlan','live:kevinkurnia13']) # group conversation
    ch = sk.contacts['live:kevinkurnia13'].chat # 1-to-1 conversation

    # Send message
    msg_content = 'This is an automated message - Kevin'
    ch.sendMsg(msg_content)
    #################################
    # Upload file
    ch.sendFile(open("C:/Users/kevin.kurnia/Desktop/MacroCode.txt", "rb"), "MacroCode.txt") 
    #################################
    # Share contact
    ch.sendContacts(sk.contacts['riza.irlan'])
    #################################
    # Retrieve recent messages
    msg_log = ch.getMsgs() 
    # print(msg_log)

    print('Message sent successfully')

class SkypePing(SkypeEventLoop):
    def __init__(self):
        super(SkypePing, self).__init__(username, password)
    def onEvent(self, event): # Create an event method
        # if isinstance(event, SkypeNewMessageEvent) and not event.msg.userId == self.userId and "ping" in event.msg.content:
        #     event.msg.chat.sendMsg("This is an Auto-Reply!")
        #     print('Reply success')

        if isinstance(event, SkypeNewMessageEvent) and (event.msg.userId == 'live:239cbcaf9e66f162' or event.msg.userId == 'riza.irlan' or event.msg.userId == 'live:kevinkurnia13' or event.msg.userId == 'sonny.guozhizhang' or event.msg.userId == 'live:steven.suwandi') and 'report' in event.msg.content:
            print(event.msg)
            ch = event.msg.chat

            # Random message
            url = 'https://sentence-generator.appspot.com/'
            req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            soup = BeautifulSoup(req.text, 'html.parser')

            random_sentence = soup.find('div', class_='jumbotron').p.text
            print(random_sentence)
            msg_content = 'Ts'    
            ch.sendMsg(msg_content)
            ch.sendMsg(random_sentence)
            # ch.sendFile(open("C:/Users/kevin.kurnia/Desktop/MacroCode.txt", "rb"), "MacroCode.txt") 
            # ch.sendContacts(sk.contacts['riza.irlan'])

            print('Auto-Reply successful')

######################################################################

# Connect with skype - FOR USERNAME, use phone number or email
username = '+6287782006746'
print('Username:', username)
password = stdiomask.getpass()
# password = 'boker'
sk = Skype(username, password) 
print('User info:')
print(sk.user)

# Automatic send message
# print('---------------------')
# send_message(sk)

# Automatic reply message
auto_reply = SkypePing()
print('---------------------')
print('Auto-Reply ON')
print('---------------------')
print(auto_reply.loop())

