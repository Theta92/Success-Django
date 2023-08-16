import requests

AZURE_FUNCTION_URL="https://successdjangofunc.azurewebsites.net/api/httptriggernew"

def send_mail(email,subject,message):
    res=requests.get(f"{AZURE_FUNCTION_URL}?email={email}&subject={subject}&message={message}")
    return res
    