#app.py
import requests
from flask import Flask,request,jsonify
import re
public_api_key="https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1"


app=Flask(__name__)
@app.route("/comments",methods=["POST"])

#input data->data_딕셔너리, json을 파싱해서 원하는 정보를 리턴

#다른 파일에서 comments_data_list를 제공하기 위해(함수를 빠져나오면 json_data가 소멸하기 때문)
class dstore_data_list():
    ds_data_list=[]
    page=1
    req_url=""
    ds_lng=[]
    ds_lat=[]
    ds_name=[]
    ds_remain=[]
#input:video_id, output:video_comment-video id를 인풋으로 주면, comments_data_list 클래스에 각종 데이터 업데이트

def address_to_xy(address):
    gmaps_api_key="AIzaSyCkRgQLNhEqJHPgAVEZE_bXM1JZ8dPbuuM"
    request_url=f"https://maps.googleapis.com/maps/api/geocode/json?key="


def find_masks_stores(address,page):
    #f-string->문자열에서 %나 +를 사용하지 않고도 편리하게 문자열 조립
    #ex)name="Sam", age=15
    # f"{name} is {age}years old"-> Sam is 15 years old
    public_api_key = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1"

    request_url=f"{public_api_key}/storesByAddr/json?address={address}&page={page}&perPage=500"
    ds.req_url=request_url
    print(ds.req_url)
    json_data=requests.get(ds.req_url)
    json_data=json_data.json()
    data_list=json_data["stores"]
    print(data_list)
    ds.ds_data_list=json_data["stores"]#ds_data_list=data_list의 복사본

ds=dstore_data_list()
#find_masks_stores("인천광역시 서구",1)


