from django.core.mail import send_mail

send_mail('Welcome!', 'Hi, welcome to bitbet! ', 'haiwei93@gmail.com', 'hs843@cornell.edu', fail_silently = False)
