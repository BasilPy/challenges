import requests
import os
from datetime import datetime

USERNAME = os.environ['USERNAME']
TOKEN = os.environ['TOKEN_FOR_PIXELA']
GRAPH_ID = os.environ['GRAPH_ID']


pixela_endpoint = "https://pixe.la/v1/users"


# # TODO Create a USER
# # user_params = {
# #     "token": {TOKEN},
# #     "username": {USERNAME},
# #     "agreeTermsOfService": "yes",
# #     "notMinor": "yes",
# # }
# # response = requests.post(url=pixela_endpoint, json=user_params)
# # print(response.text)
# # TODO Create a GRAPH
# # graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# # graph_config = {
# #     "id": "graphpy1",
# #     "name": "Python Challenge",
# #     "unit": "h",
# #     "type": "float",
# #     "color": "ajisai",
# # }
# # headers = {
# #     "X-USER-TOKEN": TOKEN
# # }
# # req = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# # print(req.text)
#
# # TODO Post a PIXEL
#
# # #today = datetime.now().strftime("%Y%m%d")
# # today = datetime(year=2022, month=11, day=1)
# # #print(today)
# #
# # pix = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# # request_body = {
# #     "date": today.strftime("%Y%m%d"),
# #     "quantity": "12.5",
# # }
# # headers = {
# #     "X-USER-TOKEN": TOKEN
# # }
# # req_pix = requests.post(url=pix, json=request_body, headers=headers)
# # print(req_pix.text)
# # TODO update pixel DATA with PUT method
# # today = datetime(year=2022, month=11, day=1)
# # pix = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# # new_request_body = {
# #     "quantity": "3.0",
# # }
# # headers = {
# #     "X-USER-TOKEN": TOKEN
# # }
# # req_pix = requests.put(url=pix, json=new_request_body, headers=headers)
# # print(req_pix.text)
#
# # TODO delete pixel DATA with DELETE method
today = datetime(year=2022, month=11, day=1)
pix = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

headers = {
    "X-USER-TOKEN": TOKEN
}
req_pix = requests.delete(url=pix, headers=headers)
print(req_pix.text)
