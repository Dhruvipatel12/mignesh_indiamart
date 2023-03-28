import frappe
import json
import requests
from datetime import datetime, timedelta


# /api/method/mignesh_indiamart_app.api.start_and_end
@frappe.whitelist()
def start_and_end():
    end_date = datetime.now()
    result = end_date - timedelta(hours=0, minutes=30)
    start_date = result
    start_date_str = start_date.strftime("%d/%m/%Y%H:%M:%S")
    print("start_date_str",start_date_str)
    return start_date, end_date


def Convert(result):
    res_dct = {result[i]: result[i + 1] for i in range(0, len(result), 2)}
    return res_dct
# /api/method/mignesh_indiamart_app.api.indiamart_api
# def indiamart_api(startdate,enddate):


@frappe.whitelist()
def indiamart_api():
    print("call...............Call..................Call.................")
    website_url = frappe.db.get_single_value("Indiamart Integration", "indiamart_url")
    glusr_crm_key = frappe.db.get_single_value("Indiamart Integration", "indiamart_key")
    start_date, end_date = start_and_end()
    creating_url=f"{website_url}?glusr_crm_key={glusr_crm_key}&start_time={start_date}&end_time={end_date}"
    # creating_url = website_url,"?",glusr_crm_key+"&"+"start_time="+start_date+"&"+"end_time="+end_date
    # print(creating_url)
    headers = {
    "accept": "application/json",
    }
    response =requests.post(creating_url, headers=headers)
    # print(response.text)
    
    y=response.text
    x=json.loads(y)
    print(x["RESPONSE"])
    result=[]
    list=[]
    for x2 in x['RESPONSE']:
        if 'UNIQUE_QUERY_ID' in x2:
            result.append("UNIQUE_QUERY_ID")
            result.append(x2['UNIQUE_QUERY_ID'])
        if 'SENDER_NAME' in x2:
            result.append("SENDER_NAME")
            result.append(x2['SENDER_NAME'])
        if 'SENDER_MOBILE' in x2:
            result.append("SENDER_MOBILE")
            result.append(x2['SENDER_MOBILE'])
        if 'SENDER_MOBILE_ALT' in x2:
            result.append("SENDER_MOBILE_ALT")
            result.append(x2['SENDER_MOBILE_ALT'])
        if 'SENDER_PHONE' in x2:
            result.append("SENDER_PHONE")
            result.append(x2['SENDER_PHONE'])
        if 'SENDER_PHONE_ALT' in x2:
            result.append("SENDER_PHONE_ALT")
            result.append(x2['SENDER_PHONE_ALT'])
        if 'SENDER_EMAIL' in x2:
            result.append("SENDER_EMAIL")
            result.append(x2['SENDER_EMAIL'])
        if 'SENDER_EMAIL_ALT' in x2:
            result.append("SENDER_EMAIL_ALT")
            result.append(x2['SENDER_EMAIL_ALT'])
        if 'SUBJECT' in x2:
            result.append("SUBJECT")
            result.append(x2['SUBJECT'])
        if 'SENDER_COMPANY' in x2:
            result.append("SENDER_COMPANY")
            result.append(x2['SENDER_COMPANY'])
        if 'SENDER_ADDRESS' in x2:
            result.append("SENDER_ADDRESS")
            result.append(x2['SENDER_ADDRESS'])
        if 'SENDER_CITY' in x2:
            result.append("SENDER_CITY")
            result.append(x2['SENDER_CITY'])
        if 'SENDER_STATE' in x2:
            result.append("SENDER_STATE")
            result.append(x2['SENDER_STATE'])
        if 'SENDER_COUNTRY_ISO' in x2:
            result.append("SENDER_COUNTRY_ISO")
            result.append(x2['SENDER_COUNTRY_ISO'])
        if 'QUERY_PRODUCT_NAME' in x2:
            result.append("QUERY_PRODUCT_NAME")
            result.append(x2['QUERY_PRODUCT_NAME'])
        if 'QUERY_MESSAGE' in x2:
            result.append("QUERY_MESSAGE")
            result.append(x2['QUERY_MESSAGE'])
        list.append(Convert(result))
        for i in list:
           
            print(i)    
            # check data is already exist in ouer system 
            data= frappe.db.sql("select sender_id from `tabEnquiry of Indiamart` where sender_id=%s",i["UNIQUE_QUERY_ID"])
            dt=""
            for i1 in data:
                for j1 in i1:
                    dt=j1
            if dt != i["UNIQUE_QUERY_ID"]:
                a= frappe.get_doc(({"doctype" : "Enquiry of Indiamart",  "sender_id": i['UNIQUE_QUERY_ID'], "full_name": i['SENDER_NAME'], 	"mobile": i['SENDER_MOBILE'], "mobile_2": i['SENDER_MOBILE_ALT']
		                    , "email": i['SENDER_EMAIL'], "email_2": i['SENDER_EMAIL_ALT'], "subjectj": i['SUBJECT'], "company": i['SENDER_COMPANY'], "address": i['SENDER_ADDRESS'], "city": i['SENDER_CITY'], "state": i['SENDER_STATE'], "country": i['SENDER_COUNTRY_ISO'], "product_name": i['QUERY_PRODUCT_NAME'], "message": i['QUERY_MESSAGE'] }))
                a.insert()
        print("------- EEEEEEEEEEEEEEEEEEEEEEEEEEeee--------")
        # frappe.db.commite()
    return response.text



@frappe.whitelist()
def indiamart_api_btn(start_date,end_date):
    print("call...............Call..................Call.................")
    website_url = frappe.db.get_single_value("Indiamart Integration", "indiamart_url")
    glusr_crm_key = frappe.db.get_single_value("Indiamart Integration", "indiamart_key")
    # start_date, end_date = start_and_end()
    creating_url=f"{website_url}?glusr_crm_key={glusr_crm_key}&start_time={start_date}&end_time={end_date}"
    # creating_url = website_url,"?",glusr_crm_key+"&"+"start_time="+start_date+"&"+"end_time="+end_date
    # print(creating_url)
    headers = {
    "accept": "application/json",
    }
    response =requests.post(creating_url, headers=headers)
    # print(response.text)
    
    y=response.text
    x=json.loads(y)
    print(x["RESPONSE"])
    result=[]
    list=[]
    for x2 in x['RESPONSE']:
        if 'UNIQUE_QUERY_ID' in x2:
            result.append("UNIQUE_QUERY_ID")
            result.append(x2['UNIQUE_QUERY_ID'])
        if 'SENDER_NAME' in x2:
            result.append("SENDER_NAME")
            result.append(x2['SENDER_NAME'])
        if 'SENDER_MOBILE' in x2:
            result.append("SENDER_MOBILE")
            result.append(x2['SENDER_MOBILE'])
        if 'SENDER_MOBILE_ALT' in x2:
            result.append("SENDER_MOBILE_ALT")
            result.append(x2['SENDER_MOBILE_ALT'])
        if 'SENDER_PHONE' in x2:
            result.append("SENDER_PHONE")
            result.append(x2['SENDER_PHONE'])
        if 'SENDER_PHONE_ALT' in x2:
            result.append("SENDER_PHONE_ALT")
            result.append(x2['SENDER_PHONE_ALT'])
        if 'SENDER_EMAIL' in x2:
            result.append("SENDER_EMAIL")
            result.append(x2['SENDER_EMAIL'])
        if 'SENDER_EMAIL_ALT' in x2:
            result.append("SENDER_EMAIL_ALT")
            result.append(x2['SENDER_EMAIL_ALT'])
        if 'SUBJECT' in x2:
            result.append("SUBJECT")
            result.append(x2['SUBJECT'])
        if 'SENDER_COMPANY' in x2:
            result.append("SENDER_COMPANY")
            result.append(x2['SENDER_COMPANY'])
        if 'SENDER_ADDRESS' in x2:
            result.append("SENDER_ADDRESS")
            result.append(x2['SENDER_ADDRESS'])
        if 'SENDER_CITY' in x2:
            result.append("SENDER_CITY")
            result.append(x2['SENDER_CITY'])
        if 'SENDER_STATE' in x2:
            result.append("SENDER_STATE")
            result.append(x2['SENDER_STATE'])
        if 'SENDER_COUNTRY_ISO' in x2:
            result.append("SENDER_COUNTRY_ISO")
            result.append(x2['SENDER_COUNTRY_ISO'])
        if 'QUERY_PRODUCT_NAME' in x2:
            result.append("QUERY_PRODUCT_NAME")
            result.append(x2['QUERY_PRODUCT_NAME'])
        if 'QUERY_MESSAGE' in x2:
            result.append("QUERY_MESSAGE")
            result.append(x2['QUERY_MESSAGE'])
        list.append(Convert(result))
        for i in list:
           
            print(i)    
            # check data is already exist in ouer system 
            data= frappe.db.sql("select sender_id from `tabEnquiry of Indiamart` where sender_id=%s",i["UNIQUE_QUERY_ID"])
            dt=""
            for i1 in data:
                for j1 in i1:
                    dt=j1
            if dt != i["UNIQUE_QUERY_ID"]:
                a= frappe.get_doc(({"doctype" : "Enquiry of Indiamart",  "sender_id": i['UNIQUE_QUERY_ID'], "full_name": i['SENDER_NAME'], 	"mobile": i['SENDER_MOBILE'], "mobile_2": i['SENDER_MOBILE_ALT']
		                    , "email": i['SENDER_EMAIL'], "email_2": i['SENDER_EMAIL_ALT'], "subjectj": i['SUBJECT'], "company": i['SENDER_COMPANY'], "address": i['SENDER_ADDRESS'], "city": i['SENDER_CITY'], "state": i['SENDER_STATE'], "country": i['SENDER_COUNTRY_ISO'], "product_name": i['QUERY_PRODUCT_NAME'], "message": i['QUERY_MESSAGE'] }))
                a.insert()
        print("------- EEEEEEEEEEEEEEEEEEEEEEEEEEeee--------")
        # frappe.db.commite()
    return response.text
