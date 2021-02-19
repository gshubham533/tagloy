from flask import Flask
from flask import request
from datetime import datetime
import requests
import urllib3
import json
import csv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#payloads to send for each function of restaurant flow
publ = "Welcome to the Publisher Submenu"
high = "Welcome to the Highlights Submenu"
lbs = "Welcome to the Live Box Status"
Trbsht = "Welcome to the Trouble shoot menu"
cta = "Welcome to the Extra"

url1 = "https://100.24.50.36:9090"
url_template = url1 + "/v1/messages/"
url_register = url1 + "/v1/contacts/"

app = Flask(__name__)


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

    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer " + authkey,
        'Accept': "*/*",
        'cache-control': "no-cache"
    }
    response = requests.request("POST", url_register, data=payload, headers=headers, verify=False)
    rs = response.text
    json_data = json.loads(rs)
    status = json_data["contacts"][0]["status"]
    if status == "valid":
        print("valid")
        payload1 = '{"to": "' + str(x) + '","recipient_type": "individual","type":"text", {"text": "Whattup?"}}'
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer " + authkey,
            'User-Agent': "PostmanRuntime/7.20.1",
            'Accept': "*/*",
            'Cache-Control': "no-cache",

        }
        response1 = requests.request("POST", url_template, data=payload1, headers=headers, verify=False)
        print(response1.text)


def send_message(rcvr, body, type1):
    authkey = update_authkey()
    url2 = url1 + "/v1/messages"
    # print(type1)
    if body == "a1":
        body = publ
    elif body == "a2":
        body = high
    elif body == "a3":
        body = lbs
    elif body == "a4":
        body = Trbsht
    elif body == "a5":
        body = cta

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
    thelist = ["hi", "hello", "hey", "3"]
    now = str(datetime.now().date())
    now_time = str(datetime.now())

    response = request.json
    try:
        frm = str(response["messages"][0]["from"])
        type1 = str(response["messages"][0]["type"])
        if type1 == "text":
            text = str(response["messages"][0]["text"]["body"])
            if text.lower() == '1':
                send_message(frm, "a1", type1)
            elif text.lower() == '2':
                send_message(frm, "a2", type1)
            elif text.lower() == "3":
                send_message(frm, "a3",type1)
            elif text.lower() == '4':
                send_message(frm, "a4", type1)
            elif text.lower() == '5':
                send_message(frm, "a5", type1)
            elif text.lower() in thelist:
                send_template(frm)

        else:
            send_message(frm, "menu", type1)
    except Exception as e:
        print(e)

    return ''







if __name__ == '__main__':
    app.debug = False
    app.run(host='127.0.0.1', port=4000)


