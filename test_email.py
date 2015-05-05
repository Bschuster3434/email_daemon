import smtplib
import datetime
from email.mime.text import MIMEText
from random import choice
import os

## Change Directory to Correct CWD

os.chdir('/home/pi/email_daemon')

## Grabbing Server Information as Global Variables

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
GMAIL_USERNAME = 'schuster.pi.server@gmail.com'

## Collecting Password information

gmail_email_location = 'pi_server_password.txt'
with open('pi_server_password.txt', 'r') as f:
	GMAIL_PASSWORD = f.read()

## Which email are we sending this to?

recipient = "brian.daniel.schuster@gmail.com"

## What file are the messages coming from?

email_files = 'test_text_messages'

def grab_file():
	"""Grabbing a random file from the repository."""
	all_files = [f for f in os.listdir(email_files)]
	random_file = choice(all_files)	
	return random_file

def return_email_message(message_file):
	"""Creates the MIME message object based off the
	   data in the message file. Supports html and
	   txt formatted files."""
	message_type = message_file.split('.')[-1]
	if message_type == 'txt':
		with open(os.path.join(email_files, message_file), 'r') as f:
			msg = MIMEText(f.read())
	msg['Subject'] = "File_Contents_%s" %message_file
	msg['From'] = GMAIL_USERNAME
	msg['To'] = recipient

	return msg

def send_message(message_contents):
	"""Send message via gmail account set-up for the Pi Server"""
	
	session = start_session()
	session.sendmail(GMAIL_USERNAME, recipient, message_contents.as_string())
	session.quit()
	return "Message Successful"

def start_session():
	"""Start session based off of server settings and return the object"""
	session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
	session.ehlo()
	session.starttls()
	session.ehlo
	session.login(GMAIL_USERNAME, GMAIL_PASSWORD)
	return session

def test():
	"""Testing my functions"""
	file = grab_file()
	all_files = [f for f in os.listdir(email_files)]
	assert file in all_files
	
	test_file = 'message_4.txt'
	four_message = return_email_message(test_file)
	
	assert four_message['Subject'] == "File_Contents_message_4.txt"
	assert four_message['From'] == GMAIL_USERNAME
	assert four_message['To'] == recipient
	assert four_message.as_string().split('\n')[-2]
	
	print "All Tests Passed"

def send_file():
	f = grab_file()
	msg = return_email_message(f)
	result = send_message(msg)
	print result

if __name__ == "__main__":
	test()
	send_file()
