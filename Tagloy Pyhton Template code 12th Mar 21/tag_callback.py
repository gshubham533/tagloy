import requests
import json
import urllib3
import csv

urllib3.disable_warnings()


url1 = "https://3.15.186.220"
count = 1

def update_authkey():
    url = url1 + "/v1/users/login"
    payload = "{\n\t\"new_password\": \"Khairnar@123\"\n}"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic <base64(username:password)>',
        'Authorization': 'Basic YWRtaW46S2hhaXJuYXJAMTIz'
    }
    response = requests.request("POST", url, headers=headers, data=payload, verify=False, timeout=5)

    rs = response.text
    #print(rs)
    json_data = json.loads(str(rs))
    response.close()
    return json_data["users"][0]["token"]

def check_contact(phone):
    url = url1 + "/v1/contacts"
    authkey = update_authkey()
    payload = '{"blocking": "wait","contacts": ["+91'+str(phone)+'"]}'
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer " + authkey
    }

    try:
        response = requests.request("POST", url.rstrip(), data=payload, headers=headers, verify=False)
        rs = response.text
        print(rs)
    except Exception as e:
        print(e)
    return ""

def send_quick_reply(phone):
    url = url1 + "/v1/messages/"
    authkey = update_authkey()
    # Payload of tag_callback
    payload = '{"to": "91'+str(phone)+'","type": "template","template": {"namespace": "f53c59d0_208b_4e32_afc8_cc646e53ee2a","name": "tag_callback","language": {"policy": "deterministic","code": "en"},"components": [{"type": "header","parameters": [{"type": "image","image": {"link": "https://media.licdn.com/dms/image/C511BAQEyh5yVhfOamQ/company-background_10000/0?e=2159024400&v=beta&t=njRC5VrfpXiSa4XJmTFP9PWlHHDDNLeyS3qcXgqReQY"}}]},{"type": "body","parameters": [{"type": "text","text": "Tagtalk and Diageo"},{"type": "text","text": "on behalf of *Diageo*."},{"type": "text","text": "9022811811"},{"type": "text","text": "9028811811"}]},{"type": "button","sub_type": "quick_reply","index": "1","parameters": [{"type": "payload","payload": "More Information"}]}]}}'
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer " + authkey
    }
    try:
        response = requests.request("POST", url.rstrip(), data=payload, headers=headers, verify=False)
        rs = response.text
        print(rs)
    except Exception as e:
        print(e)
    return ""

with open('phone.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    for row in csv_reader:
        # check_contact(row[1])
        # send_quick_reply(row[1])
        print(row[1])
        print("Sent to " + str(count) + " contact")
        count += 1






