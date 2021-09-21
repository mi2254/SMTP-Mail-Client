
from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
   msg = "\r\n SMTP Mail Client"
   endmsg = "\r\n.\r\n"

   # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope


   # Create socket called clientSocket and establish a TCP connection with mailserver and port

   # Fill in start
   clientSocket = socket(AF_INET, SOCK_STREAM)
   clientSocket.connect((mailserver, port))
   # Fill in end

   recv = clientSocket.recv(1024).decode()
   print(recv)
   if recv[:3] != '220':
       #print('220 reply not received from server.')
        print('220 reply not received from server.')
   # Send HELO command and print server response.
   heloCommand = 'HELO Alice\r\n'
   clientSocket.send(heloCommand.encode())
   recv1 = clientSocket.recv(1024).decode()
   print(recv1)
   if recv1[:3] != '250':
       #print('250 reply not received from server.')
        print('250 reply not received from server.')
   # Send MAIL FROM command and print server response.
   # Fill in start
   mailfromCommand = 'MAIL FROM: <mi2254@nyu.edu>\r\n.'
   clientSocket.send(mailfromCommand)
   recv1 = clientSocket.recv(1024).decode()
   print(recv1)
   if recv1[:3] != '250':
       print('mail from 250 reply not received from server.')
   # Fill in end

   # Send RCPT TO command and print server response.
   # Fill in start
   rcpttoCommand = 'RCPT TO: <myemail@gmail.com>\r\n'
   clientSocket.send(rcpttoCommand)
   recv1 = clientSocket.recv(1024)
   print(recv1)
   if recv1[:3] != '250':
       print('rcpt to 250 reply not received from server.')
   # Fill in end

   # Send DATA command and print server response.
   # Fill in start
   dataCommand = 'Data\r\n'

   clientSocket.send(dataCommand.encode())
   recv1 = clientSocket.recv(1024).decode()
   print(recv1)
   if recv1[:3] != '250':
       print('data 250 reply not received from server.')

   # Fill in end

   # Send message data.
   # Fill in start
   message = raw_input('Enter Message Here: ')


   # Fill in end

   # Message ends with a single period.
   # Fill in start
   mailMessageEnd = '\r\n.\r\n'
   clientSocket.send(message + mailMessageEnd)
   recv1 = clientSocket.recv(1024)
   print(recv1)
   if recv1[:3] != '250':
       print('end msg 250 reply not received from server.')
   # Fill in end

   # Send QUIT command and get server response.
   # Fill in start
   quitCommand = 'Quit\r\n'
   print(quitCommand)
   clientSocket.send(quitCommand.encode())
   recv1 = clientSocket.recv(1024).decode()
   print(recv1)
   if recv1[:3] != '250':
       print('quit 250 reply not received from server.')
       pass
   # Fill in end


if __name__ == '__main__':
   smtp_client(1025, '127.0.0.1')
