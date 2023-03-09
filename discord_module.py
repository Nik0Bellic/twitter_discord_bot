import base64
import requests
from seleniumrequests import Chrome
import time


def accept_invite(token, inv_code):
    headers = {'authorization': token}
    link = "https://discordapp.com/api/v6/invites/" + inv_code

    return (requests.post(link, headers=headers)).text

# class DSmod:
#     def __init__(self):
#         self.driver = Chrome(r"C:\Users\X507\Documents\chromedriver.exe")
#         self.driver.get('https://discord.com/')
#         self.driver.execute_script(
#             '''function login() {
#     setInterval(() => {
#       document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"OTQwMjA4NzQ1OTY1ODM4Mzg4.YgED3g.ZYJ3RLlwB3MaS8RK4yiIxhPuS8Y"`
#     }, 50);
#     setTimeout(() => {
#       location.reload();
#     }, 2500);
#   }
#
# login();'''
#         )
#         self.driver.get('https://discord.com/app')
#         time.sleep(20)

