from twilio.rest import Client


# Account Sid and Auth Token
account_sid = 'ACe8e14e97fc9774c30e12b21f0c6f9819'
auth_token = '1728c48dda9763fded012ca7ffbfaaf6'
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Give me a name",
    to="+841647689122",
    from_="+15712574935"
)

print(message.sid)

