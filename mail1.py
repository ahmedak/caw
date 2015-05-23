import smtplib
gmail_user = "vinodkgupta96@gmail.com"
gmail_pwd = "123@vision"
TO = 'b13226@students.iitmandi.ac.in;b13141@students.iitmandi.ac.in'
SUBJECT = "Design xcbjvjbkl PROJECT TEST"
TEXT = "Testing sending mail using gmail servers"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_user, gmail_pwd)
BODY = '\r\n'.join(['To: %s' % TO,'From: %s' % gmail_user,'Subject: %s' % SUBJECT,'', TEXT])
server.sendmail(gmail_user, [TO], BODY)
print ('email sent')
