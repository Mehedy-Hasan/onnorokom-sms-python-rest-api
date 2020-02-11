#OnnoRokom SMS Website For Registration - https://onnorokomsms.com
import requests

# BASE URL
URL = 'https://api2.onnorokomsms.com/HttpSendSms.ashx'
#All Options Params
op              = 'NumberSms' #Request Method (Change as your requirement)
apiKey          = '' #API Key
smsText         = '' #SMS Text
mobile          = '' #Recipient Mobile Number (Single and Multiple Number Support (Comma Sperated) )
type            = 'TEXT' #SMS Type
maskName        = ''
campaignName    = ''

# data to be sent to api
PARAMS = {
    'op'            : op,
    'apiKey'        : apiKey,
    'smsText'       : smsText,
    'mobile'        : mobile,
    'type'          : type,
    'maskName'      : maskName,
    'campaignName'  : campaignName
}
# sending post request and saving response
res = requests.post(url = URL, data=PARAMS)
data = res.text
# Response Print
print("SMS Response: ", data)