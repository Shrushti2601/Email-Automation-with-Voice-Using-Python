import smtplib
import speech_recognition as sr
from email.message import EmailMessage

import pyttsx3
listenser=sr.Recognizer()
tts=pyttsx3.Engine()

def talking_tom(text):
    tts.say(text)
    tts.runAndWait()
    
def mic():
    with sr.Microphone() as source:
        print("program is listening.....") 
        voice=listenser.listen(source)
        data=listenser.recognize_google(voice)
        print(data) 
        return data.lower()
dict={"jojo":"anandgandhamwar2009@gmail.com"}
def send_mail(receiver,subject,body):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("shrushtimahajan2601@gmail.com","ezxy fuwr etdi rosx")
    email=EmailMessage()
    email["From"]="shrushtimahajan2601@gmail.com"
    email["To"]=receiver
    email["Subject"]=subject
    email.set_content(body)
    server.send_message(email)
    
def main_poc():
    talking_tom("To whom do you want to send")
    name= mic()
    receiver=dict[name]
    talking_tom("speak subject")
    subject= mic()
    talking_tom("speak msg of email")
    body=mic()
    send_mail(receiver,subject,body)
    print("your mail has been sent!")
main_poc()
