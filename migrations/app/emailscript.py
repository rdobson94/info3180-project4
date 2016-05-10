import smtplib

def sendemail(toname,toemail,fromsubject,msg):
    fromname = 'Wishlist' 
    fromemail  = 'r.dobson1094@gmail.com'
    message = """From: {} <{}>\nTo: {} <{}>\nSubject: {}\n\n{}"""
    
    messagetosend = message.format(
                                 fromname,
                                 fromemail,
                                 toname,
                                 toemail,
                                 fromsubject,
                                 msg)
    
    # Credentials (if needed)
    username = 'r.dobson1094@gmail.com'
    password = 'gjwbmwhsctwrpzli'
    
    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromemail, toemail, messagetosend)
    server.quit()
    return