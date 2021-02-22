from flask import Flask
from flask import request
from datetime import datetime
import requests
import urllib3
import json
import csv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
status1 = {
    "ScreenFrontgate": "online",
    "ScreeDiningarea": "offline",
    "ScreenParking": "online",
}
#payloads to send for each function of restaurant flow
newline = "\\n"
default = f"Dear Owner/Manager/Staff{newline}Welcome to Tagloy. Please select an option:  {newline}1. Publisher {newline}2. Highlights {newline}3. Live Box Status {newline}4. Troubleshoot {newline}5. Connect to Agent"
res_req = f"Please select the venues of the restaurant to be selected{newline}{newline}1. Viman Nagar{newline}2. Koregaon Par{newline}3. Kalyani Nagar{newline}4. *All locations*"
publ = f"Dear *Owner/Manager/Staff* {newline}{newline}Kindly send the *video/image* that you wish to display on screen"
high = f"Dear *Owner/Manager/Staff*{newline}{newline}Kindly send the Highlights video/image that you wish to display on the tagloy screen"
lbs = f"Welcome to Live box status{newline}{newline}Screen Front gate:online{newline}Screen Dining area: offline{newline}ScreenParking: online"
Trbsht = f"Welcome to Trouble shoot menu{newline}{newline}Please select your query{newline}1. My live box is not working properly.{newline}2. Unable to upload picture/video{newline}3. My content is not displayed{newline}4. Another problem{newline}5. End"
cta = f"Please stay online{newline}We are connecting you to our agent"

url1 = "https://100.24.50.36:9090"
url_template = url1 + "/v1/messages/"
url_register = url1 + "/v1/contacts/"


app = Flask(__name__)

def publisher(phone, text):
    body = 'publisher'
    send_message(phone, body)
    int_text = text

def pub1(phone):
    body = 'sub'



def update_authkey():  # upadting authkey repetatively
    url = url1 + "/v1/users/login"
    payload = "{\n\t\"new_password\": \"Khairnar@123\"\n}"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic <base64(username:password)>',
        'Authorization': 'Basic YWRtaW46S2hhaXJuYXJAMTIz'
    }
    response = requests.request("POST", url, headers=headers, data=payload, verify=False, timeout=5)

    rs = response.text
    # print(rs)
    json_data = json.loads(str(rs))
    response.close()
    return json_data["users"][0]["token"]

def send_template(phone):
    x = phone
    authkey = update_authkey()
    payload = '{"blocking": "wait","contacts": ["+' + str(x) + '"] }'
    print(x)
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer " + authkey,
        'Accept': "*/*",
        'cache-control': "no-cache"
    }
    response = requests.request("POST", url_register, data=payload, headers=headers, verify=False)
    rs = response.text
    print(rs)
    json_data = json.loads(rs)
    status = json_data["contacts"][0]["status"]
    if status == "valid":
        print("valid")
        body = f"Dear Owner/Manager/Staff{newline}Welcome to Tagloy. Please select an option:  {newline}1. Publisher {newline}2. Highlights {newline}3. Live Box Status {newline}4. Troubleshoot {newline}5. Connect to Agent"
        payl = body
        payload1 = "{\n  \"to\": \"" + str(x) + "\",\n  \"type\": \"text\",\n  \"recipient_type\": \"individual\",\n  \"text\": {\n    \"body\": \" " + payl + " \"\n  }\n}\n"
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer " + authkey,
            'User-Agent': "PostmanRuntime/7.20.1",
            'Accept': "*/*",
            'Cache-Control': "no-cache",

        }
        response1 = requests.request("POST", url_template, data=payload1, headers=headers, verify=False)
        print(response1.text)


def send_message(rcvr, body):
    authkey = update_authkey()
    url2 = url1 + "/v1/messages"
    # print(type1)
    if body == "publisher":
        body = publ
    elif body == "highlights":
        body = high
    elif body == "lbs":
        body = lbs
    elif body == "troubleshoot":
        body = Trbsht
    elif body == "cta":
        body = cta
    elif body == "image":
        body = "*Image Received*\\n\\n" + res_req
    elif body == "default":
        body = default
    else:
        body = "Default"

    to = rcvr
    payload = "{\n  \"to\": \"" + to + "\",\n  \"type\": \"text\",\n  \"recipient_type\": \"individual\",\n  \"text\": {\n    \"body\": \" " + body + " \"\n  }\n}\n"

    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer " + authkey
    }
    # print("hello again0")
    try:
        response = requests.request("POST", url2.rstrip(), data=payload, headers=headers, verify=False)
        rs = response.text
        print(rs)
    except Exception as e:
        print(e)


@app.route('/', methods=['POST', 'GET'])
def Get_Message():
    thelist = ["hi", "hello", "hey"]
    now = str(datetime.now().date())
    now_time = str(datetime.now())

    response = request.json
    try:
        frm = str(response["messages"][0]["from"])
        type1 = str(response["messages"][0]["type"])
        print(type1)
        if type1 == "text":
            text = str(response["messages"][0]["text"]["body"])
            if text.lower() == ('1' or 'publisher') :
                send_message(frm, 'publisher')
            elif text.lower() == '2':
                send_message(frm,"highlights")
            elif text.lower() == "3":
                send_message(frm, "lbs")
            elif text.lower() == '4':
                send_message(frm, "troubleshoot")
            elif text.lower() == '5':
                send_message(frm, "cta")
            elif text.lower() in thelist:
                send_message(frm, "default")
            else:
                send_message(frm, "menu")

        if type1 == "image":
            send_message(frm,"image")
    except Exception as e:
        print(e)

    return ''


if __name__ == '__main__':
    app.debug = False
    app.run(host='127.0.0.1', port=4000)


