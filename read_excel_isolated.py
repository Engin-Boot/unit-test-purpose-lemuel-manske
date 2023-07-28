import pandas


def read_email_data():
  emaildata = None
  try:
    emaildata = pandas.read_excel('emails-to-send.xlsx', sheet_name='Sheet1',
                                  engine='openpyxl'
    )
  except IOError:
    print('unable to read')
    return []

  mails = []
  for email, hike in zip(emaildata["email"], emaildata["hike"]):
    mails.append('to {email}: hike is {hike}')
  return mails
