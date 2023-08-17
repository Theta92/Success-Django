import requests

AZURE_FUNCTION_URL="https://successdjangofunc.azurewebsites.net/api/httptriggernew"

def send_mail(email,subject,message):
    res=requests.get(f"{AZURE_FUNCTION_URL}?email={email}&subject={subject}&message={message}")
    return res
    


def get_educational_quote():
    url = "https://quotes.rest/qod?category=students"
    api_token = "YluVtr6xRlWf0e6viTLeNjs7YQQU2ykRjL5zfVA4r"
    headers = {'content-type': 'application/json', 'X-TheySaidSo-Api-Secret': format(api_token)}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if "contents" in data and "quotes" in data["contents"]:
            quote = data["contents"]["quotes"][0]["quote"]
            return quote
    import pdb; pdb.set_trace()
    return None

    

    # response = requests.get(url, headers=headers)
    # quotes=response.json()['contents']['quotes'][0]
    
