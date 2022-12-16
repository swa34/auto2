import win32com.client

ol = win32com.client.Dispatch("Outlook.Application")
olNameSpace = ol.GetNamespace("MAPI")


def send_email():
    newmail = ol.CreateItem(0)
    newmail.Subject = 'News-wire Published'
    newmail.BodyFormat = 1
    newmail.Body = 'This is an email to alert that AEM bot script has been run.  Please verify that new stories have ' \
                   'been published to the newswire site.. '
    newmail.To = 'sa69508@uga.edu; bwhet@uga.edu; erjeya@uga.edu'
    newmail._oleobj_.Invoke(*(64209, 0, 8, 0, olNameSpace.Accounts.Item('1')))

    newmail.Display()
    newmail.Send()


def error_email():
    newmail = ol.CreateItem(0)
    newmail.Subject = 'Error in Publishing'
    newmail.BodyFormat = 1
    newmail.Body = 'Hello, this is a test for the error message.'
    newmail.To = 'scottwallen3434@gmail.com'
    newmail._oleobj_.Invoke(*(64209, 0, 8, 0, olNameSpace.Accounts.Item('1')))

    newmail.Display()
    newmail.Send()
# newmail.BodyFormat = 2
# newmail.HTMLBody = '<HTML Markup >'
