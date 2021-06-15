from flask import Flask, request, jsonify
import json
from os.path import join
import foo
import requests
from requests.structures import CaseInsensitiveDict
from datetime import datetime
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = foo.MONGO_URI
mongo = PyMongo(app)
db_operations = mongo.db.users

def ticks(dt):
	return int((dt - datetime(1, 1, 1)).total_seconds() * 10000000)

def send_message(message, phone):
    url = foo.APIUrl

    headers = CaseInsensitiveDict()
    headers["Authorization"] = foo.API
    headers["Content-Type"] = "application/json"

    data = {
        "sender": phone,
        "data": {
            "code" : "initial - message",
            "userId": "ymbot",
            "type": "text",
            "message": message
        }
    }

    data = json.dumps(data)

    resp = requests.post(url, headers=headers, data=data).text
    return json.loads(resp)

def get_otp(MobileNo, Type="Signup"):
    url = foo.getOTP

    headers = CaseInsensitiveDict()
    headers["AuthKey"] = foo.TAuthKey
    headers["Content-Type"] = "application/json"

    data = {
        "MobileNo": MobileNo,
        "Type": Type
    }

    data = json.dumps(data)

    resp = requests.post(url, headers=headers, data=data).text
    return json.loads(resp)

def sign_up(MobileNo, password, OTP, Channel="Bot", Type="Signup"):
    url = foo.signUp

    headers = CaseInsensitiveDict()
    headers["AuthKey"] = foo.TAuthKey
    headers["Content-Type"] = "application/json"

    data = {
        "MobileNo": int(MobileNo),
        "password": password,
        "OTP": OTP,
        "Channel": Channel,
        "Type": Type
    }

    data = json.dumps(data)

    resp = requests.post(url, headers=headers, data=data).text
    return json.loads(resp)

def get_profile(phone):
    url = foo.getProfile

    headers = CaseInsensitiveDict()
    headers["AuthKey"] = foo.AuthKey
    headers["Content-Type"] = "application/json"

    data = {
        "MobileNo": phone
    }

    data = json.dumps(data)
    # current_time = datetime.now()
    # c_time = str(current_time)[11:]
    # current_datetime = f"{current_time.day}.{current_time.month}.{current_time.year} {c_time}"
    # with open("server.log", "a") as server:
    #     server.write("---------------------------\n")
    #     server.write(current_datetime)
    #     server.write("\n")
    #     server.write(data)
    #     server.write("\n")

    resp = requests.post(url, headers=headers, data=data).text
    return json.loads(resp)

def get_rate_card(dim, amt, wt, sender, receiver, cid, ct, pin=""):
    url = foo.getRateCard

    headers = CaseInsensitiveDict()
    headers["AuthKey"] = foo.AuthKey
    headers["Content-Type"] = "application/json"

    data = {
        "Pincode": pin,
        "L":"10",
        "W":"10",
        "H":"10",
        "CodAmount": str(amt),
        "Wt": wt,
        "CT": ct,
        "Cid": cid,
        "SLocalArea": sender['area'],
        "SCity": sender['city'],
        "SState": sender['state'],
        "RLocalArea": receiver['area'],
        "RCity": receiver['city'],
        "RState": receiver['state'],
        "drops": 0
    }

    if ct == 'C':
        data["L"] = dim['length']
        data["W"] = dim['width']
        data["H"] = dim['height']
    
    data = json.dumps(data)

    resp = requests.post(url, headers=headers, data=data).text
    return json.loads(resp)

def cancel_order(AWBNo, reason, CID):
    url = foo.cancelOrder

    headers = CaseInsensitiveDict()
    headers["AuthKey"] = foo.AuthKey
    headers["Content-Type"] = "application/json"

    data = {
        "AWBNo": AWBNo,
        "Reason": reason,
        "CID": CID
    }

    data = json.dumps(data)

    resp = requests.post(url, headers=headers, data=data).text
    return json.loads(resp)

def track_order(AWBNo):
    url = foo.trackOrder

    headers = CaseInsensitiveDict()
    headers["AuthKey"] = foo.AuthKey
    headers["Content-Type"] = "application/json"

    data = {
        "AWBNo": AWBNo
    }

    data = json.dumps(data)

    resp = requests.post(url, headers=headers, data=data).text
    return json.loads(resp)

def book_courier(CID, OrderType, OrderNo, PaymentStatus, PickupVendor, PickVendorPhoneNo, PickVendorAddress, PickVendorCity, PickVendorState, PickVendorPinCode, CustomerName, CustomerCity, CustomerState, ZipCode, CustomerAddress, CustomerMobileNo, CollectibleAmount, DeclaredValue, BillableWeight, VolWeight, PhyWeight, ShipLength, ShipWidth, ShipHeight, Quantity, Provider, OrderID, IsCod, CourierCharges, RateId, ProductJson, Tax, BP, CDiscount, CtoP, Coupon, P_latlng, D_latlng, Distance, Insurance=0, DCPO='W'):
    url = foo.bookCourier

    headers = CaseInsensitiveDict()
    headers["AuthKey"] = foo.AuthKey
    headers["Content-Type"] = "application/json"

    data = {
        "CID": CID,
        "OrderType": OrderType,
        "OrderNo": OrderNo,
        "PaymentStatus": PaymentStatus,
        "PickupVendor": PickupVendor,
        "PickVendorPhoneNo": str(PickVendorPhoneNo),
        "PickVendorAddress": PickVendorAddress,
        "PickVendorCity": PickVendorCity,
        "PickVendorState": PickVendorState,
        "PickVendorPinCode": str(PickVendorPinCode),
        "CustomerName": CustomerName,
        "CustomerCity": CustomerCity,
        "CustomerState": CustomerState,
        "ZipCode": str(ZipCode),
        "CustomerAddress": CustomerAddress,
        "CustomerMobileNo": str(CustomerMobileNo),
        "CollectibleAmount": str(CollectibleAmount),
        "DeclaredValue": DeclaredValue,
        "BillableWeight": str(BillableWeight),
        "VolWeight": VolWeight,
        "PhyWeight": PhyWeight,
        "ShipLength": ShipLength,
        "ShipWidth": ShipWidth,
        "ShipHeight": ShipHeight,
        "Quantity": Quantity,
        "Provider": Provider,
        "OrderID": OrderID,
        "IsCod": IsCod,
        "CourierCharges": str(CourierCharges),
        "RateId": RateId,
        "ProductJson": ProductJson,
        "Tax": Tax,
        "BP": str(BP),
        "CDiscount": CDiscount,
        "CtoP": str(CtoP),
        "Coupon": Coupon,
        "Insurance": Insurance,
        "DCPO": DCPO,
        "P_latlng": P_latlng,
        "D_latlng": D_latlng,
        "Distance": Distance
    }

    data = json.dumps(data)

    resp = requests.post(url, headers=headers, data=data).text
    return json.loads(resp)

def service_check(pin, origin):
    url = foo.serviceCheck

    headers = CaseInsensitiveDict()
    headers["AuthKey"] = foo.AuthKey
    headers["Content-Type"] = "application/json"

    data = {
        "Pincode": pin,
        "Origin": origin
    }

    data = json.dumps(data)

    resp = requests.post(url, headers=headers, data=data).text
    return json.loads(resp)

@app.route('/', methods=['POST'])
def home():
    if request.method == 'POST':
        message = request.json
        phone = message['phone']
        messageType = message['type']
        if messageType == 'text':
            message = message['text']
            returnMessage = ""
            user = db_operations.find_one({'_id': int(phone)})
            if user is None:
                new_user = {'_id': int(phone), 'returnMessage': "Foo"}
                db_operations.insert_one(new_user)
                user = db_operations.find_one({'_id': int(phone)})
            try:
                value = user['returnMessage']
            except:
                value = "Foo"
            if message in ["Hi", "hi", "Hello", "hello", "Hey", "hey", "0"]:
                resp = get_profile(phone=phone[2:])
                if resp['ReplyCode'] != 0:
                    returnMessage = "Please get yourself registered first!\n\nType *1* to register"
                else:
                    db_operations.delete_one({'_id': int(phone)})
                    new_user = {
                        '_id': int(phone),
                        "CT": "C",
                        'cid': resp['Cid']
                    }
                    db_operations.insert_one(new_user)
                    user = db_operations.find_one({'_id': int(phone)})
                    returnMessage = "Welcome to paapos, your preferred delivery partner\n\nTo Book Same Day Order Reply 1\nTo Book Courier Reply 2\nTo Track Your Order Reply 3\nTo cancel your order reply 4\nTo connect with our Executive reply 5\nFor feedback reply 6\n\nFor the main menu, type *0*\nFor the previous menu, type *9*"
                updated_user = {"$set": {'returnMessage' : returnMessage}}
                db_operations.update_one(user, updated_user)
                return send_message(message=returnMessage, phone=phone)
            elif "Please get yourself registered first" in value:
                if message == '1':
                    resp = get_otp(MobileNo=phone, Type="SignUp")
                    returnMessage = "You must have received an OTP from Paapos. Enter that OTP here"
                else:
                    returnMessage = "Please get yourself registered first!\n\nType *1* to register"
                updated_user = {"$set": {'returnMessage' : returnMessage}}
                db_operations.update_one(user, updated_user)
                return send_message(message=returnMessage, phone=phone)
            elif "Enter that OTP here" in value:
                resp = sign_up(MobileNo=phone, password="Foobar2021", OTP=message)
                if resp['ReplyCode'] != 0:
                    db_operations.delete_one({'_id': int(phone)})
                    new_user = {
                        '_id': int(phone),
                        "CT": "C",
                        'cid': resp['Cid']
                    }
                    db_operations.insert_one(new_user)
                    user = db_operations.find_one({'_id': int(phone)})
                    returnMessage = "Welcome to paapos, your preferred delivery partner\n\nTo Book Same Day Order Reply 1\nTo Book Courier Reply 2\nTo Track Your Order Reply 3\nTo cancel your order reply 4\nTo connect with our Executive reply 5\nFor feedback reply 6\n\nFor the main menu, type *0*\nFor the previous menu, type *9*"
                else:
                    returnMessage = "Invalid OTP!\nPlease get yourself registered first!\n\nType *1* to register"
                updated_user = {"$set": {'returnMessage' : returnMessage}}
                db_operations.update_one(user, updated_user)
                return send_message(message=returnMessage, phone=phone)
            elif "Welcome" in value:
                if message == '1':
                    returnMessage = "Please Select Your City\n\nFor Delhi Reply 1\nFor Noida Reply 2\nFor Gurgaon Reply 3\nFor Ghaziabad Reply 4\nFor Greater Noida Reply 5\nFor Faridabad Reply 6\nFor help dial 93782 93782"
                    updated_user = {"$set": {'returnMessage' : returnMessage, 'CT': "S"}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                elif message == '2':
                    returnMessage = "To check pickup availability, reply 1\nTo check drop availability, reply 2\nTo calculate rate, reply 3\nTo book courier, reply 4"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                elif message == '3':
                    returnMessage = "Enter AWBNo (Airway Bill number)"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                elif message == '4':
                    returnMessage = "Enter Airway Bill number (AWBNo)"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                elif message == '5':
                    returnMessage = "Please wait while we are connecting your call with our Executive.\n\nType *0* to go back to main menu"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                elif message == '6':
                    returnMessage = "On a scale of 1 to 5, please rate our service, 1 being the lowest."
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
            # 1
            elif "Please Select Your City" in value:
                cities = ["Delhi", "Noida", "Gurgaon", "Ghaziabad", "Greater Noida", "Faridabad"]
                if message == '9':
                    returnMessage = "Welcome to paapos, your preferred delivery partner\n\nTo Book Same Day Order Reply 1\nTo Book Courier Reply 2\nTo Track Your Order Reply 3\nTo cancel your order reply 4\nTo connect with our Executive reply 5\nFor feedback reply 6\n\nFor the main menu, type *0*\nFor the previous menu, type *9*"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                elif message in ["1", "2", "3", "4", "5", "6"]:
                    i = int(message) - 1
                    returnMessage = "Please enter pickup location e.g. b Block Amar colony lajpat nagar"
                    updated_user = {"$set": {'PickVendorCity' : cities[i]}}
                    db_operations.update_one(user, updated_user)
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                elif message != "0":
                    returnMessage = "Wrong entry!\nPlease Select Your City\n\nFor Delhi Reply 1\nFor Noida Reply 2\nFor Gurgaon Reply 3\nFor Ghaziabad Reply 4\nFor Greater Noida Reply 5\nFor Faridabad Reply 6\nFor help dial 93782 93782"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
            elif "Please enter pickup location e.g. b Block Amar colony lajpat nagar" in value:
                if message == '9':
                    returnMessage = "Please Select Your City\n\nFor Delhi Reply 1\nFor Noida Reply 2\nFor Gurgaon Reply 3\nFor Ghaziabad Reply 4\nFor Greater Noida Reply 5\nFor Faridabad Reply 6\nFor help dial 93782 93782"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                else:
                    updated_user = {"$set": {'PickArea' : message}}
                    db_operations.update_one(user, updated_user)
                    returnMessage = "Please enter Name of the Person at Pickup Location"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
            elif "Please enter Name of the Person at Pickup Location" in value:
                if message == '9':
                    returnMessage = "Please enter pickup location e.g. b Block Amar colony lajpat nagar"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                else:
                    returnMessage = "Please enter mobile number of the person at pickup location"
                    updated_user = {"$set": {'returnMessage' : returnMessage, 'PickupVendor' : message}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
            elif "Please enter mobile number of the person at pickup location" in value:
                returnMessage = ""
                if message == '9':
                    returnMessage = "Please enter Name of the Person at Pickup Location"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                else:
                    try:
                        if len(message) != 10:
                            raise Exception
                        mob = int(message)
                        returnMessage = "Please Enter complete pickup Address"
                        updated_user = {"$set": {'returnMessage' : returnMessage, 'PickVendorPhoneNo' : message}}
                        db_operations.update_one(user, updated_user)
                        return send_message(message=returnMessage, phone=phone)
                    except:
                        returnMessage = "Invalid mobile number.\nPlease enter mobile number of the person at pickup location, again"
                        updated_user = {"$set": {'returnMessage' : returnMessage}}
                        db_operations.update_one(user, updated_user)
                        return send_message(message=returnMessage, phone=phone)
            elif "Please Enter complete pickup Address" in value:
                if message == '9':
                    returnMessage = "Please enter mobile number of the person at pickup location"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                else:
                    returnMessage = "Enter Pickup PinCode"
                    updated_user = {"$set": {'returnMessage' : returnMessage, 'PickVendorAddress' : message}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
            elif "Enter Pickup PinCode" in value:
                if message == '9':
                    returnMessage = "Please Enter complete pickup Address"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                else:
                    try:
                        if len(message) != 6:
                            raise Exception
                        pin = int(message)
                        returnMessage = "Please Select Drop City\n\nFor Delhi Reply 1\nFor Noida Reply 2\nFor Gurgaon Reply 3\nFor Ghaziabad Reply 4\nFor Greater Noida Reply 5\nFor Faridabad Reply 6\nFor help dial 93782 93782"
                        updated_user = {"$set": {'returnMessage' : returnMessage, 'PickVendorPinCode' : message}}
                        db_operations.update_one(user, updated_user)
                        return send_message(message=returnMessage, phone=phone)
                    except:
                        returnMessage = "Incorrect Pickup Pincode. Enter Pickup PinCode\nFor help dial 93782 93782"
                        updated_user = {"$set": {'returnMessage' : returnMessage}}
                        db_operations.update_one(user, updated_user)
                        return send_message(message=returnMessage, phone=phone)
            elif "Please Select Drop City" in value:
                cities = ["Delhi", "Noida", "Gurgaon", "Ghaziabad", "Greater Noida", "Faridabad"]
                if message == '9':
                    returnMessage = "Enter Pickup PinCode"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                elif message in ["1", "2", "3", "4", "5", "6"]:
                    i = int(message) - 1
                    updated_user = {"$set": {'CustomerCity' : cities[i]}}
                    db_operations.update_one(user, updated_user)
                    returnMessage = "Enter Drop Location"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                elif message != "0":
                    returnMessage = "Wrong entry!\nPlease Select Drop City\n\nFor Delhi Reply 1\nFor Noida Reply 2\nFor Gurgaon Reply 3\nFor Ghaziabad Reply 4\nFor Greater Noida Reply 5\nFor Faridabad Reply 6\nFor help dial 93782 93782"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
            elif "Enter Drop Location" in value:
                if message == '9':
                    returnMessage = "Please Select Drop City\n\nFor Delhi Reply 1\nFor Noida Reply 2\nFor Gurgaon Reply 3\nFor Ghaziabad Reply 4\nFor Greater Noida Reply 5\nFor Faridabad Reply 6\nFor help dial 93782 93782"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                else:
                    returnMessage = "Please enter Name of the Person at Drop Location"
                    updated_user = {"$set": {'returnMessage' : returnMessage, 'CustomerArea' : message}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
            elif "Please enter Name of the Person at Drop Location" in value:
                if message == '9':
                    returnMessage = "Enter Drop Location"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                else:
                    returnMessage = "Please enter mobile number of the person at Drop Location"
                    updated_user = {"$set": {'returnMessage' : returnMessage, 'CustomerName' : message}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
            elif "Please enter mobile number of the person at Drop Location" in value:
                if message == '9':
                    returnMessage = "Please enter Name of the Person at Drop Location"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                else:
                    try:
                        if len(message) != 10:
                            raise Exception
                        mob = int(message)
                        returnMessage = "Please Enter Address"
                        updated_user = {"$set": {'returnMessage' : returnMessage, 'CustomerMobileNo' : message}}
                        db_operations.update_one(user, updated_user)
                        return send_message(message=returnMessage, phone=phone)
                    except:
                        returnMessage = "Invalid mobile number.\nPlease enter mobile number of the person at Drop Location, again"
                        updated_user = {"$set": {'returnMessage' : returnMessage}}
                        db_operations.update_one(user, updated_user)
                        return send_message(message=returnMessage, phone=phone)
            elif "Please Enter Address" in value:
                if message == '9':
                    returnMessage = "Please enter mobile number of the person at Drop Location"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                else:
                    returnMessage = "Enter Drop Pincode"
                    updated_user = {"$set": {'returnMessage' : returnMessage, 'CustomerAddress' : message}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
            elif "Enter Drop Pincode" in value and message != "1":
                if message == '9':
                    returnMessage = "Please Enter Address"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                else:
                    try:
                        if len(message) != 6:
                            raise Exception
                        pin = int(message)
                        returnMessage = "*Please Select Packet Type*\nFor Food reply 1\nFor Medicines reply 2\nFor Groceries reply 3\nFor Clothes reply 4\nFor Documents reply 5\nFor Electronics reply 6\nFor Others reply 7"
                        updated_user = {"$set": {'returnMessage' : returnMessage, 'ZipCode' : message}}
                        db_operations.update_one(user, updated_user)
                        return send_message(message=returnMessage, phone=phone)
                    except:
                        returnMessage = "Incorrect Drop Pincode. Enter Drop PinCode\nFor help dial 93782 93782"
                        updated_user = {"$set": {'returnMessage' : returnMessage}}
                        db_operations.update_one(user, updated_user)
                        return send_message(message=returnMessage, phone=phone)
            elif "Please Select Packet Type" in value and user["CT"] == "S":
                packets = ["Food", "Medicines", "Groceries", "Clothes", "Documents", "Electronics", "Others"]
                if message == '9':
                    returnMessage = "Enter Drop Pincode"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                elif message in ['1', '2', '3', '4', '5', '6', '7']:
                    i = int(message) - 1
                    returnMessage = "*Please select the package details*\nFor Small package reply 1\nFor Medium package reply 2\nFor Large package reply 3"
                    updated_user = {"$set": {'returnMessage' : returnMessage, 'packetType' : packets[i]}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                else:
                    returnMessage = "Invalid input!\n*Please Select Packet Type*\nFor Food reply 1\nFor Medicines reply 2\nFor Groceries reply 3\nFor Clothes reply 4\nFor Documents reply 5\nFor Electronics reply 6\nFor Others reply 7"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)	
            elif "Please select the package details" in value and user["CT"] == "S":
                package = ['Small', 'Medium', 'Large']
                if message == '9':
                    returnMessage = "*Please Select Packet Type*\nFor Food reply 1\nFor Medicines reply 2\nFor Groceries reply 3\nFor Clothes reply 4\nFor Documents reply 5\nFor Electronics reply 6\nFor Others reply 7"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                elif message in ['1', '2', '3']:
                    i = int(message) - 1
                    returnMessage = "Please enter the weight of the product in KGs (e.g. 0.50 or 1)"
                    updated_user = {"$set": {'returnMessage' : returnMessage, 'package' : package[i]}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                else:
                    returnMessage = "Invalid input!\n*Please select the package details*\nFor Small package reply 1\nFor Medium package reply 2\nFor Large package reply 3"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
            elif "Please enter the weight of the product in KGs (e.g. 0.50 or 1)" in value and user["CT"] == "S":
                if message == '9':
                    returnMessage = "*Please select the package details*\nFor Small package reply 1\nFor Medium package reply 2\nFor Large package reply 3"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                else:
                    try:
                        Wt = float(message)
                        returnMessage = "Please declare the value of the goods you are sending in INR (e.g. 1000, 199, 599, etc.)"
                        updated_user = {"$set": {'returnMessage' : returnMessage, 'PhyWeight' : message}}
                        db_operations.update_one(user, updated_user)
                        return send_message(message=returnMessage, phone=phone)
                    except:
                        returnMessage = "Invalid weight!\nPlease enter the weight of the product in KGs (e.g. 0.50 or 1)"
                        updated_user = {"$set": {'returnMessage' : returnMessage, 'PhyWeight' : message}}
                        db_operations.update_one(user, updated_user)
                        return send_message(message=returnMessage, phone=phone)
            elif "Please declare the value of the goods you are sending in INR" in value and user["CT"] == "S":
                if message == '9':
                    returnMessage = "Please enter the weight of the product in KGs (e.g. 0.50 or 1)"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                else:
                    try:
                        amt = float(message)
                        returnMessage = "Please let us know the number of products you are sending"
                        updated_user = {"$set": {'returnMessage' : returnMessage, 'DeclaredValue' : message}}
                        db_operations.update_one(user, updated_user)
                        return send_message(message=returnMessage, phone=phone)
                    except:
                        returnMessage = "Invalid entry!\nPlease declare the value of the goods you are sending in INR (e.g. 1000, 199, 599, etc.)"
                        updated_user = {"$set": {'returnMessage' : returnMessage}}
                        db_operations.update_one(user, updated_user)
                        return send_message(message=returnMessage, phone=phone)
            elif "Please let us know the number of products you are sending" in value and user["CT"] == "S":
                if message == '9':
                    returnMessage = "Please declare the value of the goods you are sending in INR (e.g. 1000, 199, 599, etc.)"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                else:
                    try:
                        qty = int(message)
                        returnMessage = "Do you want us to collect payment from the customer for the products you are sending?\nFor yes reply 1\nFor no reply 2"
                        # returnMessage = "To pay delivery charges\nAt pickup location, reply *1*\nAt drop location, reply *2*\nFrom wallet, reply *3*"
                        updated_user = {"$set": {'returnMessage' : returnMessage, 'Quantity' : message}}
                        db_operations.update_one(user, updated_user)
                        return send_message(message=returnMessage, phone=phone)
                    except:
                        returnMessage = "Invalid entry! It should be an integer.\nPlease let us know the number of products you are sending"
                        updated_user = {"$set": {'returnMessage' : returnMessage}}
                        db_operations.update_one(user, updated_user)
                        return send_message(message=returnMessage, phone=phone)
            elif "Do you want us to collect payment from the customer" in value and user["CT"] == "S":
                if message == '9':
                    returnMessage = "Please let us know the number of products you are sending"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                elif message in ['1', 'Yes', 'yes', 'Y', 'y']:
                    returnMessage = "Please let us know the amount to be collected from the customer"
                    updated_user = {"$set": {'returnMessage' : returnMessage, 'IsCod' : "1"}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                else:
                    returnMessage = "Do you want to avail insurance for the product you are sending?\nFor yes reply 1\nFor no reply 2"
                    updated_user = {"$set": {'returnMessage' : returnMessage, 'IsCod' : "0"}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
            elif "Do you want to avail insurance" in value and user["CT"] == "S":
                if message == '9':
                    returnMessage = "Do you want us to collect payment from the customer for the products you are sending?\nFor yes reply 1\nFor no reply 2"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                else:
                    if message in ['1', 'Yes', 'yes', 'Y', 'y']:
                        updated_user = {"$set": {'Insurance' : 1}}
                        db_operations.update_one(user, updated_user)
                    else:
                        updated_user = {"$set": {'Insurance' : 0}}
                        db_operations.update_one(user, updated_user)
                    amt = '0'
                    if user['IsCod'] == '1':
                        amt = user['CollectibleAmount']
                    sender = {
                        "pin": user['PickVendorPinCode'],
                        "area": user['PickArea'],
                        "city": user['PickVendorCity'],
                        "address": user['PickVendorAddress'],
                        "name": user['PickupVendor'],
                        "phone": user['PickVendorPhoneNo']
                    }
                    city = sender['city']
                    sender['state'] = "Delhi"
                    if city in ["Ghaziabad", "Noida", "Greater Noida"]:
                        sender['state'] = "Uttar Pradesh"
                    elif city in ["Gurgaon", "Faridabad"]:
                        sender['state'] = "Haryana"
                    receiver = {
                        "pin": user['ZipCode'],
                        "area": user['CustomerArea'],
                        "city": user['CustomerCity'],
                        "address": user['CustomerAddress'],
                        "name": user['CustomerName'],
                        "phone": user['CustomerMobileNo']
                    }
                    city = receiver['city']
                    receiver['state'] = "Delhi"
                    if city in ["Ghaziabad", "Noida", "Greater Noida"]:
                        receiver['state'] = "Uttar Pradesh"
                    elif city in ["Gurgaon", "Faridabad"]:
                        receiver['state'] = "Haryana"
                    cid = user['cid']
                    wt = user['PhyWeight']
                    resp = get_rate_card(dim="", amt=amt, wt=wt, sender=sender, receiver=receiver, cid=cid, ct="S")
                    if resp['ReplyCode'] == 0:
                        returnMessage = "_Available providers_\n\n"
                        providers = resp['Providers']
                        updated_user = {"$set": {'providers' : json.dumps(providers), 'P_latlng': resp['P_latlng'], 'D_latlng': resp['D_latlng'], 'Distance': resp['Distance']}}
                        db_operations.update_one(user, updated_user)
                        i = 1
                        for provider in providers:
                            returnMessage += f"Reply *{i}* for *{provider['ProviderName']}* at {provider['price']}\n"
                            i += 1
                        returnMessage += "\nEnter the index of the service provider of your choice"
                    else:
                        returnMessage = f"_{resp['ReplyMsg']}_"
                updated_user = {"$set": {'returnMessage' : returnMessage}}
                db_operations.update_one(user, updated_user)
                return send_message(message=returnMessage, phone=phone)
            elif "Please let us know the amount to be collected from the customer" in value and user["CT"] == "S":
                if message == '9':
                    returnMessage = "Do you want us to collect payment from the customer for the products you are sending?\nFor yes reply 1\nFor no reply 2"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                else:
                    try:
                        message = float(message)
                        returnMessage = "Do you want to avail insurance for the product you are sending?\nFor yes reply 1\nFor no reply 2"
                        updated_user = {"$set": {'returnMessage' : returnMessage, 'CollectibleAmount' : message}}
                        db_operations.update_one(user, updated_user)
                        return send_message(message=returnMessage, phone=phone)
                    except:
                        returnMessage = "Enter correct amount!\nPlease let us know the amount to be collected from the customer"
                        updated_user = {"$set": {'returnMessage' : returnMessage}}
                        db_operations.update_one(user, updated_user)
                        return send_message(message=returnMessage, phone=phone)
            elif "Enter the index of the service provider of your choice" in value and user["CT"] == "S":
                if message == '9':
                    returnMessage = "Do you want to avail insurance for the product you are sending?\nFor yes reply 1\nFor no reply 2"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                else:
                    providers = json.loads(user['providers'])
                    provider = providers[int(message) - 1]
                    # returnMessage = "Enter coupon code (if any) or type *No* if you don't have one"
                    returnMessage = "To pay delivery charges\nAt pickup location, reply *1*\nAt drop location, reply *2*\nFrom wallet, reply *3*"
                    updated_user = {
                        "$set": {
                            'rateid' : provider['rateid'],
                            'ctop': provider['ctop'],
                            'price': provider['price'],
                            'bp': provider['bp'],
                            'tax': provider['tax'],
                            'provider': provider['provider'],
                            'tat': provider['tat'],
                            'miniwt': provider['miniwt'],
                            'ProviderName': provider['ProviderName'],
                            'RateName': provider['RateName'],
                            'billwt': provider['billwt'],
                            'returnMessage' : returnMessage
                        }
                    }
                    db_operations.update_one(user, updated_user)
                    if user['IsCod'] == '1':
                        updated_user = {"$set": {'Codcharge' : provider['Codcharge']}}
                        db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
            elif "To pay delivery charges" in value:
                if message == '9':
                    returnMessage = "Enter the index of the service provider of your choice"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                elif message in ['1', '2', '3']:
                    payment = ['P', 'D', 'W']
                    returnMessage = "Enter coupon code (if any) or type *No* if you don't have one"
                    i = int(message) - 1
                    updated_user = {"$set": {'returnMessage' : returnMessage, 'DCPO': payment[i]}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                else:
                    returnMessage = "Invalid entry!\nTo pay delivery charges\nAt pickup location, reply *1*\nAt drop location, reply *2*\nFrom wallet, reply *3*"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
            elif "Enter coupon code (if any)" in value and user["CT"] == "S":
                if message == '9':
                    # returnMessage = "Enter the index of the service provider of your choice"
                    returnMessage = "To pay delivery charges\nAt pickup location, reply *1*\nAt drop location, reply *2*\nFrom wallet, reply *3*"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                else:
                    updated_user = {"$set": {'Coupon' : message}}
                    db_operations.update_one(user, updated_user)
                    returnMessage = "To confirm booking, press *Y*"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
            elif "To confirm booking, press" in value and user["CT"] == "S":
                if message == '9':
                    returnMessage = "Enter coupon code (if any) or type *No* if you don't have one"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                elif message in ['y', 'Y']:
                    cid = user['cid']
                    orderType = "COD"
                    if user['IsCod'] == '0':
                        orderType = "Prepaid"
                    orderNo = "0"
                    paymentStatus = orderType
                    sender = {
                        "pin": user['PickVendorPinCode'],
                        "area": user['PickArea'],
                        "city": user['PickVendorCity'],
                        "address": user['PickVendorAddress'],
                        "name": user['PickupVendor'],
                        "phone": user['PickVendorPhoneNo']
                    }
                    city = sender['city']
                    sender['state'] = "Delhi"
                    if city in ["Ghaziabad", "Noida", "Greater Noida"]:
                        sender['state'] = "Uttar Pradesh"
                    elif city in ["Gurgaon", "Faridabad"]:
                        sender['state'] = "Haryana"
                    receiver = {
                        "pin": user['ZipCode'],
                        "area": user['CustomerArea'],
                        "city": user['CustomerCity'],
                        "address": user['CustomerAddress'],
                        "name": user['CustomerName'],
                        "phone": user['CustomerMobileNo']
                    }
                    city = receiver['city']
                    receiver['state'] = "Delhi"
                    if city in ["Ghaziabad", "Noida", "Greater Noida"]:
                        receiver['state'] = "Uttar Pradesh"
                    elif city in ["Gurgaon", "Faridabad"]:
                        receiver['state'] = "Haryana"
                    qty = user['Quantity']
                    collectableAmt = "0"
                    if orderType == "COD":
                        collectableAmt = user['CollectibleAmount']
                    declaredValue = str(float(user['DeclaredValue']) * float(qty))
                    billWt = user['billwt']
                    wt = user['PhyWeight']
                    providerID = user['provider']
                    orderID = "0"
                    isCOD = user['IsCod']
                    if isCOD == '1':
                        collectableAmt = user['CollectibleAmount']
                    else:
                        collectableAmt = '0'
                    courierCharges = user['price']
                    rateID = user['rateid']
                    products = []
                    product = {
                        'pname': f"{user['package']}_{user['packetType']}",
                        'qty': user['Quantity'],
                        'price': declaredValue,
                    }
                    products.append(product)
                    tax = "0"
                    bp = user['bp']
                    cDiscount = '0'
                    cTop = user['ctop']
                    coupon = user['Coupon']
                    if coupon == "No":
                        coupon = ""
                    resp = book_courier(
                        CID=cid, 
                        OrderType=orderType, 
                        OrderNo=f"SD{ticks(datetime.utcnow())}", 
                        PaymentStatus=paymentStatus, 
                        PickupVendor=sender['name'], 
                        PickVendorPhoneNo=sender['phone'], 
                        PickVendorAddress=sender['address'], 
                        PickVendorCity=sender['city'], 
                        PickVendorState=sender['state'], 
                        PickVendorPinCode=sender['pin'], 
                        CustomerName=receiver['name'], 
                        CustomerCity=receiver['city'], 
                        CustomerState= receiver['state'], 
                        ZipCode= receiver['pin'], 
                        CustomerAddress= receiver['address'], 
                        CustomerMobileNo= receiver['phone'], 
                        CollectibleAmount= collectableAmt, 
                        DeclaredValue=declaredValue, 
                        BillableWeight=billWt, 
                        VolWeight="0", 
                        PhyWeight= wt, 
                        ShipLength="10", 
                        ShipWidth="10", 
                        ShipHeight="10", 
                        Quantity=qty, 
                        Provider=providerID,
                        OrderID=orderID,
                        IsCod=isCOD,
                        CourierCharges=courierCharges,
                        RateId=rateID, 
                        ProductJson=json.dumps(products), 
                        Tax=tax,
                        BP=bp,
                        CDiscount=cDiscount,
                        CtoP=cTop,
                        Coupon=coupon,
                        Insurance=user["Insurance"],
                        DCPO=user['DCPO'],
                        P_latlng=user['P_latlng'],
                        D_latlng=user['D_latlng'],
                        Distance=user['Distance']
                    )
                    if resp['ReplyCode'] == 0:
                        returnMessage = f"Booking successful\n\nHere's your AWBNo (Airway Bill Number)\n*{resp['AWBno']}\n\nhttps://paapos.com/OLabel.aspx?AWBno={resp['AWBno']}"
                    else:
                        returnMessage = resp['ReplyMsg']
                    returnMessage += "\n\nType *0* to go back to main menu."
                updated_user = {"$set": {'returnMessage' : returnMessage}}
                db_operations.update_one(user, updated_user)
                return send_message(message=returnMessage, phone=phone)
            # 2
            elif "To check pickup availability" in value:
                returnMessage = ""
                if message == '9':
                    returnMessage = "Welcome to paapos, your preferred delivery partner\n\nTo Book Same Day Order Reply 1\nTo Book Courier Reply 2\nTo Track Your Order Reply 3\nTo cancel your order reply 4\nTo connect with our Executive reply 5\nFor feedback reply 6\n\nFor the main menu, type *0*\nFor the previous menu, type *9*"
                elif message == '1':
                    returnMessage = "Enter Pickup pincode"
                    updated_user = {"$set": {'flow' : 2.1}}
                    db_operations.update_one(user, updated_user)
                elif message == '2':
                    returnMessage = "Enter Drop pincode"
                    updated_user = {"$set": {'flow' : 2.2}}
                    db_operations.update_one(user, updated_user)
                elif message == '3':
                    returnMessage = "Enter Correct Pickup PIN Code"
                    updated_user = {"$set": {'flow' : 2.3}}
                    db_operations.update_one(user, updated_user)
                elif message == '4':
                    returnMessage = "Enter 6 Digits Pickup Pincode"
                    updated_user = {"$set": {'flow' : 2.4}}
                    db_operations.update_one(user, updated_user)
                else:
                    returnMessage = "Invalid entry!\nTo check pickup availability, reply 1\nTo check drop availability, reply 2\nTo calculate rate, reply 3\nTo book courier, reply 4"
                updated_user = {"$set": {'returnMessage' : returnMessage}}
                db_operations.update_one(user, updated_user)
                return send_message(message=returnMessage, phone=phone)
            # 2 - 1 - Check pickup availability
            elif "Enter Pickup pincode" in value:
                if message == '9':
                    returnMessage = "To check pickup availability, reply 1\nTo check drop availability, reply 2\nTo calculate rate, reply 3\nTo book courier, reply 4"
                else:
                    try:
                        if len(message) != 6:
                            raise Exception
                        pin = int(message)
                        resp = service_check(pin=message, origin="1")
                        if resp['ReplyCode'] == 0:
                            repMsg = resp['ReplyMsg'].split("~")
                            _id = repMsg[0]
                            city = repMsg[1]
                            state = repMsg[2]
                            returnMessage = f"Pickup service available!\n\nCity = {city}\nState = {state}"
                        else:
                            returnMessage = "Pickup service not available!"
                    except:
                        returnMessage = "Invalid pickup pincode! Enter Pickup pincode again"
                    returnMessage += "\n\nType *0* to go back to main menu."
                updated_user = {"$set": {'returnMessage' : returnMessage}}
                db_operations.update_one(user, updated_user)
                return send_message(message=returnMessage, phone=phone)
            # 2 - 2 - Check drop availability
            elif "Enter Drop pincode" in value:
                if message == '9':
                    returnMessage = "To check pickup availability, reply 1\nTo check drop availability, reply 2\nTo calculate rate, reply 3\nTo book courier, reply 4"
                else:
                    try:
                        message = str(message)
                        if len(message) != 6:
                            raise Exception
                        pin = int(message)
                        resp = service_check(pin=message, origin="0")
                        if resp['ReplyCode'] == 0:
                            repMsg = resp['ReplyMsg'].split("~")
                            _id = repMsg[0]
                            city = repMsg[1]
                            state = repMsg[2]
                            returnMessage = f"Drop service available!\n\nCity = {city}\nState = {state}"
                        else:
                            returnMessage = "Drop service not available!"
                    except:
                        returnMessage = "Invalid drop pincode! Enter Drop pincode again"
                    returnMessage += "\n\nType *0* to go back to main menu."
                updated_user = {"$set": {'returnMessage' : returnMessage}}
                db_operations.update_one(user, updated_user)
                return send_message(message=returnMessage, phone=phone)
            # 2 - 3 - Get rate card
            elif "Enter Correct Pickup PIN Code" in value:
                if message == '9':
                    returnMessage = "To check pickup availability, reply 1\nTo check drop availability, reply 2\nTo calculate rate, reply 3\nTo book courier, reply 4"
                else:
                    try:
                        if len(message) != 6:
                            raise Exception
                        pin = int(message)
                        updated_user = {"$set": {'pPin' : message}}
                        db_operations.update_one(user, updated_user)
                        returnMessage = "Enter Correct Drop PIN Code"
                    except:
                        returnMessage = "Enter Correct Pickup PIN Code"
                updated_user = {"$set": {'returnMessage' : returnMessage}}
                db_operations.update_one(user, updated_user)
                return send_message(message=returnMessage, phone=phone)
            elif "Enter Correct Drop PIN Code" in value:
                if message == '9':
                    returnMessage = "Enter Correct Pickup PIN Code"
                else:
                    try:
                        if len(message) != 6:
                            raise Exception
                        pin = int(message)
                        updated_user = {"$set": {'dPin' : message}}
                        db_operations.update_one(user, updated_user)
                        returnMessage = "Please enter the weight of the product in KGs (e.g. 0.60 or 1)"
                    except:
                        returnMessage = "Enter Correct Drop PIN Code"
                updated_user = {"$set": {'returnMessage' : returnMessage}}
                db_operations.update_one(user, updated_user)
                return send_message(message=returnMessage, phone=phone)
            elif "Please enter the weight of the product in KGs (e.g. 0.60 or 1)" in value:
                if message == '9':
                    returnMessage = "Enter Correct Drop PIN Code"
                else:
                    try:
                        Wt = float(message)
                        updated_user = {"$set": {'Wt' : message}}
                        db_operations.update_one(user, updated_user)
                        returnMessage = "Enter the Dimensions of the item in the format - *LENGTH WIDTH HEIGHT* all dimensions being in centi-metres (cm) (e.g. 20 25 15, 10 15 10, etc.)"
                    except:
                        returnMessage = "Invalid weight!\nPlease enter the weight of the product in KGs (e.g. 0.60 or 1)"
                updated_user = {"$set": {'returnMessage' : returnMessage}}
                db_operations.update_one(user, updated_user)
                return send_message(message=returnMessage, phone=phone)
            elif "Enter the Dimensions" in value:
                if message == '9':
                    returnMessage = "Please enter the weight of the product in KGs (e.g. 0.60 or 1)"
                else:
                    updated_user = {"$set": {'dim' : message}}
                    db_operations.update_one(user, updated_user)
                    returnMessage = "Enter order type.\n\nFor Prepaid, reply 1\nFor COD, reply 2"
                updated_user = {"$set": {'returnMessage' : returnMessage}}
                db_operations.update_one(user, updated_user)
                return send_message(message=returnMessage, phone=phone)
            elif "Enter order type" in value:
                if message == '9':
                    returnMessage = "Enter the Dimensions of the item in the format - *LENGTH WIDTH HEIGHT* all dimensions being in centi-metres (cm) (e.g. 20 25 15, 10 15 10, etc.)"
                else:
                    if message == '2':
                        returnMessage = "Enter collectable amount"
                    else:
                        pin = f"{user['pPin']}{user['dPin']}"
                        dimensions = user['dim']
                        if " " in dimensions:
                            dimensions = dimensions.split()
                        elif "x" in dimensions:
                            dimensions = dimensions.split("x")
                        elif "," in dimensions:
                            dimensions = dimensions.split(",")
                        elif ", " in dimensions:
                            dimensions = dimensions.split(", ")
                        elif "*" in dimensions:
                            dimensions = dimensions.split("*")
                        elif "* " in dimensions:
                            dimensions = dimensions.split("* ")
                        dim = {
                            "length": dimensions[0],
                            "width": dimensions[1],
                            "height": dimensions[2]
                        }
                        sender = {
                            "pin": user['pPin'],
                            "area": "",
                            "city": "",
                            "state": "",
                            "name": "",
                            "phone": ""
                        }
                        receiver = {
                            "pin": user['dPin'],
                            "area": "",
                            "city": "",
                            "state": "",
                            "name": "",
                            "phone": ""
                        }
                        amt = '0'
                        wt = user['Wt']
                        cid = user['cid']
                        resp = get_rate_card(pin=pin, dim=dim, amt=amt, wt=wt, sender=sender, receiver=receiver, cid=cid, ct="C")
                        if resp['ReplyCode'] == 0:
                            returnMessage = "_Data found_\n\nAvailable providers\n"
                            providers = resp['Providers']
                            updated_user = {"$set": {'providers' : json.dumps(providers), 'P_latlng': resp['P_latlng'], 'D_latlng': resp['D_latlng'], 'Distance': resp['Distance']}}
                            db_operations.update_one(user, updated_user)
                            i = 1
                            for provider in providers:
                                returnMessage += f"*{i})* {provider['ProviderName']} at {provider['price']}\n"
                                i += 1
                        else:
                            returnMessage = f"_{resp['ReplyMsg']}_"
                        returnMessage += "\nType *0* to go back to main menu"
                updated_user = {"$set": {'returnMessage' : returnMessage}}
                db_operations.update_one(user, updated_user)
                return send_message(message=returnMessage, phone=phone)
            elif "Enter collectable amount" in value:
                if message == '9':
                    returnMessage = "Enter order type.\n\nFor Prepaid, reply 1\nFor COD, reply 2"
                else:
                    updated_user = {"$set": {'CodAmount' : message}}
                    db_operations.update_one(user, updated_user)
                    pin = f"{user['pPin']}{user['dPin']}"
                    dimensions = user['dim']
                    if " " in dimensions:
                        dimensions = dimensions.split()
                    elif "x" in dimensions:
                        dimensions = dimensions.split("x")
                    elif "," in dimensions:
                        dimensions = dimensions.split(",")
                    elif ", " in dimensions:
                        dimensions = dimensions.split(", ")
                    elif "*" in dimensions:
                        dimensions = dimensions.split("*")
                    elif "* " in dimensions:
                        dimensions = dimensions.split("* ")
                    dim = {
                        "length": dimensions[0],
                        "width": dimensions[1],
                        "height": dimensions[2]
                    }
                    amt = message
                    wt = user['Wt']
                    sender = {
                        "area": "",
                        "city": "",
                        "state": ""
                    }
                    receiver = {
                        "area": "",
                        "city": "",
                        "state": ""
                    }
                    cid = user['cid']
                    resp = get_rate_card(pin=pin, dim=dim, amt=amt, wt=wt, sender=sender, receiver=receiver, cid=cid, ct="C")
                    if resp['ReplyCode'] == 0:
                        returnMessage = "_Data found_\n\nAvailable providers\n\n"
                        providers = resp['Providers']
                        updated_user = {"$set": {'providers' : json.dumps(providers), 'P_latlng': resp['P_latlng'], 'D_latlng': resp['D_latlng'], 'Distance': resp['Distance']}}
                        db_operations.update_one(user, updated_user)
                        i = 1
                        for provider in providers:
                            returnMessage += f"*{i})* {provider['ProviderName']} at {provider['price']}\n"
                            i += 1
                    else:
                        returnMessage = f"_{resp['ReplyMsg']}_"
                    returnMessage += "\nType *0* to go back to main menu"
                updated_user = {"$set": {'returnMessage' : returnMessage}}
                db_operations.update_one(user, updated_user)
                return send_message(message=returnMessage, phone=phone)
            elif "_Data found_\n\nAvailable providers\n\n" in value and user['flow'] == 2.3:
                if message == '9':
                    returnMessage = "Enter order type.\n\nFor Prepaid, reply 1\nFor COD, reply 2"
                else:
                    returnMessage = "Type *0* to go back to main menu."
                updated_user = {"$set": {'returnMessage' : returnMessage}}
                db_operations.update_one(user, updated_user)
                return send_message(message=returnMessage, phone=phone)
            # 2 - 4 - Book courier
            elif "6 Digits Pickup Pincode" in value:
                if message == '9':
                    returnMessage = "To check pickup availability, reply 1\nTo check drop availability, reply 2\nTo calculate rate, reply 3\nTo book courier, reply 4"
                else:
                    try:
                        if len(message) != 6:
                            raise Exception
                        pin = int(message)
                        updated_user = {"$set": {'PickVendorPinCode' : message}}
                        db_operations.update_one(user, updated_user)
                        returnMessage = "Please Enter Name of the Person at Pickup Location"
                    except:
                        returnMessage = "Enter correct 6 Digits Pickup Pincode"
                updated_user = {"$set": {'returnMessage' : returnMessage}}
                db_operations.update_one(user, updated_user)
                return send_message(message=returnMessage, phone=phone)
            elif "Please Enter Name of the Person at Pickup Location" in value:
                if message == '9':
                    returnMessage = "Enter 6 Digits Pickup Pincode"
                else:
                    updated_user = {"$set": {'PickupVendor' : message}}
                    db_operations.update_one(user, updated_user)
                    returnMessage = "Please enter mobile number of the person at Pickup location"
                updated_user = {"$set": {'returnMessage' : returnMessage}}
                db_operations.update_one(user, updated_user)
                return send_message(message=returnMessage, phone=phone)
            elif "mobile number of the person at Pickup location" in value:
                if message == '9':
                    returnMessage = "Please Enter Name of the Person at Pickup Location"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                else:
                    try:
                        if len(message) != 10:
                            raise Exception
                        mob = int(message)
                        returnMessage = "Please enter complete Address"
                        updated_user = {"$set": {'returnMessage' : returnMessage, 'PickVendorPhoneNo' : message}}
                        db_operations.update_one(user, updated_user)
                        return send_message(message=returnMessage, phone=phone)
                    except:
                        returnMessage = "Please enter correct mobile number of the person at Pickup location"
                        updated_user = {"$set": {'returnMessage' : returnMessage}}
                        db_operations.update_one(user, updated_user)
                        return send_message(message=returnMessage, phone=phone)
            elif "Please enter complete Address" in value:
                if message == '9':
                    returnMessage = "Please enter mobile number of the person at Pickup location"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                else:
                    returnMessage = "Please enter Pickup City"
                    updated_user = {"$set": {'returnMessage' : returnMessage, 'PickVendorAddress' : message}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
            elif "Please enter Pickup City" in value:
                if message == '9':
                    returnMessage = "Please enter complete Address"
                else:
                    updated_user = {"$set": {'PickVendorCity' : message}}
                    db_operations.update_one(user, updated_user)
                    returnMessage = "Please enter Pickup State"
                updated_user = {"$set": {'returnMessage' : returnMessage}}
                db_operations.update_one(user, updated_user)
                return send_message(message=returnMessage, phone=phone)
            elif "Please enter Pickup State" in value:
                if message == '9':
                    returnMessage = "Please enter Pickup City"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                else:
                    returnMessage = "Enter 6 Digits Drop Pincode"
                    updated_user = {"$set": {'returnMessage' : returnMessage, 'state' : message}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
            elif "6 Digits Drop Pincode" in value:
                if message == '9':
                    returnMessage = "Please enter Pickup State"
                else:
                    try:
                        if len(message) != 6:
                            raise Exception
                        pin = int(message)
                        updated_user = {"$set": {'ZipCode' : message}}
                        db_operations.update_one(user, updated_user)
                        returnMessage = "Please Enter Name of the Person at Drop Location"
                    except:
                        returnMessage = "Enter correct 6 Digits Drop Pincode"				
                updated_user = {"$set": {'returnMessage' : returnMessage}}
                db_operations.update_one(user, updated_user)
                return send_message(message=returnMessage, phone=phone)
            elif "Please Enter Name of the Person at Drop Location" in value:
                if message == '9':
                    returnMessage = "Enter 6 Digits Drop Pincode"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                else:
                    returnMessage = "Please enter mobile number of the person at Drop location"
                    updated_user = {"$set": {'returnMessage' : returnMessage, 'CustomerName' : message}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
            elif "mobile number of the person at Drop location" in value:
                if message == '9':
                    returnMessage = "Please Enter Name of the Person at Drop Location"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                else:
                    try:
                        if len(message) != 10:
                            raise Exception
                        mob = int(message)
                        returnMessage = "Please Enter complete Address"
                        updated_user = {"$set": {'returnMessage' : returnMessage, 'CustomerMobileNo' : message}}
                        db_operations.update_one(user, updated_user)
                        return send_message(message=returnMessage, phone=phone)
                    except:
                        returnMessage = "Please enter correct mobile number of the person at Drop location"
                        updated_user = {"$set": {'returnMessage' : returnMessage}}
                        db_operations.update_one(user, updated_user)
                        return send_message(message=returnMessage, phone=phone)
            elif "Please Enter complete Address" in value:
                if message == '9':
                    returnMessage = "Please enter mobile number of the person at Drop location"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                else:
                    returnMessage = "Please enter Drop City"
                    updated_user = {"$set": {'returnMessage' : returnMessage, 'CustomerAddress' : message}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
            elif "Please enter Drop City" in value:
                if message == '9':
                    returnMessage = "Please Enter complete Address"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                else:
                    returnMessage = "Please enter Drop State"
                    updated_user = {"$set": {'returnMessage' : returnMessage, 'CustomerCity' : message}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
            elif "Please enter Drop State" in value:
                if message == '9':
                    returnMessage = "Please enter Drop City"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                else:
                    returnMessage = "*Please Select Packet Type*\nFor Food reply 1\nFor Medicines reply 2\nFor Groceries reply 3\nFor Clothes reply 4\nFor Documents reply 5\nFor Electronics reply 6\nFor Others reply 7"
                    updated_user = {"$set": {'returnMessage' : returnMessage, 'CustomerState' : message}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
            elif "Please Select Packet Type" in value:
                packets = ["Food", "Medicines", "Groceries", "Clothes", "Documents", "Electronics", "Others"]
                if message == '9':
                    returnMessage = "Please enter Drop State"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)	
                elif message in ['1', '2', '3', '4', '5', '6', '7']:
                    i = int(message) - 1
                    returnMessage = "Please enter the Weight of the product in KGs (e.g. 0.60 or 1)"
                    updated_user = {"$set": {'returnMessage' : returnMessage, 'packetType' : packets[i]}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)	
                else:
                    returnMessage = "Invalid input!\n*Please Select Packet Type*\nFor Food reply 1\nFor Medicines reply 2\nFor Groceries reply 3\nFor Clothes reply 4\nFor Documents reply 5\nFor Electronics reply 6\nFor Others reply 7"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)	
            elif "Please enter the Weight of the product in KGs (e.g. 0.60 or 1)" in value:
                if message == '9':
                    returnMessage = "*Please Select Packet Type*\nFor Food reply 1\nFor Medicines reply 2\nFor Groceries reply 3\nFor Clothes reply 4\nFor Documents reply 5\nFor Electronics reply 6\nFor Others reply 7"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)	
                else:
                    try:
                        Wt = float(message)
                        returnMessage = "Enter Dimensions of the item in the format - *LENGTH WIDTH HEIGHT* all dimensions being in centi-metres (cm) (e.g. 20 25 15, 10 15 10, etc.)"
                        updated_user = {"$set": {'returnMessage' : returnMessage, 'PhyWeight' : message}}
                        db_operations.update_one(user, updated_user)
                        return send_message(message=returnMessage, phone=phone)
                    except:
                        returnMessage = "Invalid entry!\nPlease enter the Weight of the product in KGs (e.g. 0.60 or 1)"
                        updated_user = {"$set": {'returnMessage' : returnMessage}}
                        db_operations.update_one(user, updated_user)
                        return send_message(message=returnMessage, phone=phone)
            elif "Enter Dimensions" in value:
                if message == '9':
                    returnMessage = "Please enter the Weight of the product in KGs (e.g. 0.60 or 1)"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                else:
                    returnMessage = "Please declare the value of the goods you are sending in INR (e.g. 1000, 199, 599, etc.)"
                    updated_user = {"$set": {'returnMessage' : returnMessage, 'dim' : message}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
            elif "Please declare the value of the goods you are sending in INR" in value:
                if message == '9':
                    returnMessage = "Enter Dimensions of the item in the format - *LENGTH WIDTH HEIGHT* all dimensions being in centi-metres (cm) (e.g. 20 25 15, 10 15 10, etc.)"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                else:
                    try:
                        amt = float(message)
                        returnMessage = "Please let us know the number of products you are sending"
                        updated_user = {"$set": {'returnMessage' : returnMessage, 'DeclaredValue' : message}}
                        db_operations.update_one(user, updated_user)
                        return send_message(message=returnMessage, phone=phone)
                    except:
                        returnMessage = "Invalid entry!\nPlease declare the value of the goods you are sending in INR (e.g. 1000, 199, 599, etc.)"
                        updated_user = {"$set": {'returnMessage' : returnMessage}}
                        db_operations.update_one(user, updated_user)
                        return send_message(message=returnMessage, phone=phone)
            elif "Please let us know the number of products you are sending" in value:
                if message == '9':
                    returnMessage = "Please declare the value of the goods you are sending in INR (e.g. 1000, 199, 599, etc.)"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                else:
                    try:
                        qty = int(message)
                        returnMessage = "Do you want us to collect payment from the customer for the products you are sending?\nFor yes reply 1\nFor no reply 2"
                        updated_user = {"$set": {'returnMessage' : returnMessage, 'Quantity' : message}}
                        db_operations.update_one(user, updated_user)
                        return send_message(message=returnMessage, phone=phone)
                    except:
                        returnMessage = "Invalid entry! It should be an integer.\nPlease let us know the number of products you are sending"
                        updated_user = {"$set": {'returnMessage' : returnMessage}}
                        db_operations.update_one(user, updated_user)
                        return send_message(message=returnMessage, phone=phone)
            elif "Do you want us to collect payment from the customer for the products you are sending?\nFor yes reply 1\nFor no reply 2" in value:
                if message == '9':
                    returnMessage = "Please let us know the number of products you are sending"
                elif message in ['1', 'Yes', 'yes', 'Y', 'y']:
                    updated_user = {"$set": {'IsCod' : "1"}}
                    db_operations.update_one(user, updated_user)
                    returnMessage = "Please let us know the Amount to be collected from the customer"
                else:
                    updated_user = {"$set": {'IsCod' : "0"}}
                    db_operations.update_one(user, updated_user)
                    amt = '0'
                    wt = user['PhyWeight']
                    pin = f"{user['PickVendorPinCode']}{user['ZipCode']}"
                    dimensions = user['dim']
                    if " " in dimensions:
                        dimensions = dimensions.split()
                    elif "x" in dimensions:
                        dimensions = dimensions.split("x")
                    elif "," in dimensions:
                        dimensions = dimensions.split(",")
                    elif ", " in dimensions:
                        dimensions = dimensions.split(", ")
                    l = float(dimensions[0])
                    w = float(dimensions[1])
                    h = float(dimensions[2])
                    dim = {
                        "length": dimensions[0],
                        "width": dimensions[1],
                        "height": dimensions[2]
                    }
                    sender = {
                        "pin": user['PickVendorPinCode'],
                        "area": user['PickVendorAddress'],
                        "city": user['PickVendorCity'],
                        "address": user['PickVendorAddress'],
                        "name": user['PickupVendor'],
                        "phone": user['PickVendorPhoneNo'],
                        "state": user['state']
                    }
                    receiver = {
                        "pin": user['ZipCode'],
                        "area": user['CustomerAddress'],
                        "city": user['CustomerCity'],
                        "address": user['CustomerAddress'],
                        "name": user['CustomerName'],
                        "phone": user['CustomerMobileNo'],
                        "state": user['CustomerState']
                    }
                    cid = user['cid']
                    resp = get_rate_card(pin=pin, dim=dim, amt=amt, wt=wt, sender=sender, receiver=receiver, cid=cid, ct="C")
                    if resp['ReplyCode'] == 0:
                        returnMessage = "_Data found_\n\nAvailable providers\n\n"
                        providers = resp['Providers']
                        updated_user = {"$set": {'providers' : json.dumps(providers), 'P_latlng': resp['P_latlng'], 'D_latlng': resp['D_latlng'], 'Distance': resp['Distance']}}
                        db_operations.update_one(user, updated_user)
                        i = 1
                        for provider in providers:
                            returnMessage += f"Reply *{i}* for *{provider['ProviderName']} ({provider['provider']})* at {provider['price']}\n"
                            i += 1
                        returnMessage += "\nEnter the index of the service provider of your choice"
                    else:
                        returnMessage = f"_{resp['ReplyMsg']}_"
                updated_user = {"$set": {'returnMessage' : returnMessage}}
                db_operations.update_one(user, updated_user)
                return send_message(message=returnMessage, phone=phone)
            elif "Enter the index of the service provider of your choice" in value and message == '9':
                returnMessage = "Do you want us to collect payment from the customer for the products you are sending?\nFor yes reply 1\nFor no reply 2"
                updated_user = {"$set": {'returnMessage' : returnMessage}}
                db_operations.update_one(user, updated_user)
                return send_message(message=returnMessage, phone=phone)
            elif "Enter the index of the service provider of your choice" in value:
                providers = json.loads(user['Providers'])
                provider = providers[int(message) - 1]
                updated_user = {
                    "$set": {
                        'rateid' : provider['rateid'],
                        'ctop': provider['ctop'],
                        'price': provider['price'],
                        'bp': provider['bp'],
                        'tax': provider['tax'],
                        'provider': provider['provider'],
                        'tat': provider['tat'],
                        'miniwt': provider['miniwt'],
                        'ProviderName': provider['ProviderName'],
                        'RateName': provider['RateName'],
                        'billwt': provider['billwt']
                    }
                }
                db_operations.update_one(user, updated_user)
                if user['IsCod'] == '1':
                    updated_user = {"$set": {'Codcharge' : provider['Codcharge']}}
                    db_operations.update_one(user, updated_user)
                # returnMessage = "Enter coupon code (if any) or type *No* if you don't have one"
                returnMessage = "To pay Delivery charges\nAt pickup location, reply *1*\nAt drop location, reply *2*\nFrom wallet, reply *3*"
                updated_user = {"$set": {'returnMessage' : returnMessage}}
                db_operations.update_one(user, updated_user)
                return send_message(message=returnMessage, phone=phone)
            elif "To pay Delivery charges" in value:
                if message == '9':
                    returnMessage = "Enter the index of the service provider of your choice"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                elif message in ['1', '2', '3']:
                    payment = ['P', 'D', 'W']
                    returnMessage = "Enter coupon code (if any) or type *No* if you don't have one"
                    i = int(message) - 1
                    updated_user = {"$set": {'returnMessage' : returnMessage, 'DCPO': payment[i]}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                else:
                    returnMessage = "Invalid entry!\nTo pay Delivery charges\nAt pickup location, reply *1*\nAt drop location, reply *2*\nFrom wallet, reply *3*"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
            elif "Enter coupon code (if any)" in value:
                if message == '9':
                    # returnMessage = "Enter the index of the service provider of your choice"
                    returnMessage = "To pay Delivery charges\nAt pickup location, reply *1*\nAt drop location, reply *2*\nFrom wallet, reply *3*"
                else:
                    updated_user = {"$set": {'Coupon' : message}}
                    db_operations.update_one(user, updated_user)
                    returnMessage = "To confirm booking, press *Y*"
                updated_user = {"$set": {'returnMessage' : returnMessage}}
                db_operations.update_one(user, updated_user)
                return send_message(message=returnMessage, phone=phone)
            elif "To confirm booking, press" in value:
                if message == '9':
                    returnMessage = "Enter coupon code (if any) or type *No* if you don't have one"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                elif message in ['y', 'Y']:
                    cid = user['cid']
                    orderType = "Prepaid"
                    if user['IsCod'] == "1":
                        orderType = "COD"
                    orderNo = "0"
                    paymentStatus = orderType
                    sender = {
                        "pin": user['PickVendorPinCode'],
                        "area": user['PickVendorAddress'],
                        "city": user['PickVendorCity'],
                        "address": user['PickVendorAddress'],
                        "name": user['PickupVendor'],
                        "phone": user['PickVendorPhoneNo'],
                        "state": user['state']
                    }
                    receiver = {
                        "pin": user['ZipCode'],
                        "area": user['CustomerAddress'],
                        "city": user['CustomerCity'],
                        "address": user['CustomerAddress'],
                        "name": user['CustomerName'],
                        "phone": user['CustomerMobileNo'],
                        "state": user['CustomerState']
                    }
                    collectableAmt = "0"
                    if orderType == "COD":
                        collectableAmt = user['CollectibleAmount']
                    declaredValue = str(float(user['DeclaredValue']) * float(qty))
                    billWt = user['billwt']
                    dimensions = user['dim']
                    if " " in dimensions:
                        dimensions = dimensions.split()
                    elif "x" in dimensions:
                        dimensions = dimensions.split("x")
                    elif "," in dimensions:
                        dimensions = dimensions.split(",")
                    elif ", " in dimensions:
                        dimensions = dimensions.split(", ")
                    elif "*" in dimensions:
                        dimensions = dimensions.split("*")
                    elif "* " in dimensions:
                        dimensions = dimensions.split("* ")
                    l = float(dimensions[0])
                    w = float(dimensions[1])
                    h = float(dimensions[2])
                    volWt = (l * w * h) / 5000
                    wt = user['PhyWeight']
                    providerID = user['provider']
                    orderID = "0"
                    isCOD = user['IsCod']
                    if orderType == "COD":
                        collectableAmt = user['CollectibleAmount']
                    courierCharges = user['price']
                    rateID = user['rateid']
                    products = []
                    product = {
                        'pname': f"{user['packetType']}",
                        'qty': f"{user['Quantity']}",
                        'price': f"{user['DeclaredValue']}"
                    }
                    products.append(product)
                    tax = user['tax']
                    bp = user['bp']
                    cDiscount = '0'
                    cTop = user['ctop']
                    coupon = user['Coupon']
                    if coupon in ["No", "no", "N", "n"]:
                        coupon = ""
                    resp = book_courier(
                        CID=cid,
                        OrderType=orderType, 
                        OrderNo=f"CR{ticks(datetime.utcnow())}", 
                        PaymentStatus=paymentStatus, 
                        PickupVendor=sender['name'], 
                        PickVendorPhoneNo=sender['phone'], 
                        PickVendorAddress=sender['area'], 
                        PickVendorCity=sender['city'], 
                        PickVendorState=sender['state'], 
                        PickVendorPinCode=sender['pin'], 
                        CustomerName=receiver['name'], 
                        CustomerCity=receiver['city'], 
                        CustomerState= receiver['state'], 
                        ZipCode= receiver['pin'], 
                        CustomerAddress= receiver['area'], 
                        CustomerMobileNo= receiver['phone'], 
                        CollectibleAmount= collectableAmt, 
                        DeclaredValue=declaredValue, 
                        BillableWeight=billWt, 
                        VolWeight=str(volWt), 
                        PhyWeight= wt, 
                        ShipLength= str(l), 
                        ShipWidth= str(w), 
                        ShipHeight= str(h), 
                        Quantity=product['qty'], 
                        Provider=providerID,
                        OrderID=orderID,
                        IsCod= isCOD,
                        CourierCharges=courierCharges,
                        RateId=rateID, 
                        ProductJson=json.dumps(products), 
                        Tax=str(tax),
                        BP=bp,
                        CDiscount=cDiscount,
                        CtoP=cTop,
                        Coupon=coupon,
                        Insurance=0,
                        DCPO=user['DCPO'],
                        P_latlng=user['P_latlng'],
                        D_latlng=user['D_latlng'],
                        Distance=user['Distance']
                    )
                    if resp['ReplyCode'] == 0:
                        returnMessage = f"Booking successful\n\nHere's your AWBNo (Airway Bill Number)\n*{resp['AWBno']}*\n\nhttps://paapos.com/OLabel.aspx?AWBno={resp['AWBno']}"
                    else:
                        returnMessage = resp['ReplyMsg']
                    returnMessage += "\nType *0* to go back to main menu."
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
            elif "Please let us know the Amount to be collected from the customer" in value:
                if message == '9':
                    returnMessage = "Do you want us to collect payment from the customer for the products you are sending?\nFor yes reply 1\nFor no reply 2"
                else:
                    try:
                        amount = float(message)
                        updated_user = {"$set": {'CollectibleAmount' : message}}
                        db_operations.update_one(user, updated_user)
                        amt = message
                        wt = user['PhyWeight']
                        pin = f"{user['PickVendorPinCode']}{user['ZipCode']}"
                        dimensions = user['dim']
                        if " " in dimensions:
                            dimensions = dimensions.split()
                        elif "x" in dimensions:
                            dimensions = dimensions.split("x")
                        elif "," in dimensions:
                            dimensions = dimensions.split(",")
                        elif ", " in dimensions:
                            dimensions = dimensions.split(", ")
                        elif "*" in dimensions:
                            dimensions = dimensions.split("*")
                        elif "* " in dimensions:
                            dimensions = dimensions.split("* ")
                        l = float(dimensions[0])
                        w = float(dimensions[1])
                        h = float(dimensions[2])
                        dim = {
                            "length": dimensions[0],
                            "width": dimensions[1],
                            "height": dimensions[2]
                        }
                        sender = {
                            "pin": user['PickVendorPinCode'],
                            "area": user['PickVendorAddress'],
                            "city": user['PickVendorCity'],
                            "address": user['PickVendorAddress'],
                            "name": user['PickupVendor'],
                            "phone": user['PickVendorPhoneNo'],
                            "state": user['state']
                        }
                        receiver = {
                            "pin": user['ZipCode'],
                            "area": user['CustomerAddress'],
                            "city": user['CustomerCity'],
                            "address": user['CustomerAddress'],
                            "name": user['CustomerName'],
                            "phone": user['CustomerMobileNo'],
                            "state": user['CustomerState']
                        }
                        cid = user['cid']
                        resp = get_rate_card(pin=pin, dim=dim, amt=amt, wt=wt, sender=sender, receiver=receiver, cid=cid, ct="C")
                        if resp['ReplyCode'] == 0:
                            returnMessage = "_Data found_\n\nAvailable providers\n\n"
                            providers = resp['Providers']
                            i = 1
                            for provider in providers:
                                returnMessage += f"*{i})* {provider['ProviderName']} at {provider['price']}\n"
                                i += 1
                            returnMessage += "\nEnter the index of the service provider of your choice"
                            updated_user = {"$set": {'returnMessage' : returnMessage, 'Providers' : json.dumps(providers)}}
                            db_operations.update_one(user, updated_user)
                            return send_message(message=returnMessage, phone=phone)
                        else:
                            returnMessage = f"_{resp['ReplyMsg']}_"
                            updated_user = {"$set": {'returnMessage' : returnMessage}}
                            db_operations.update_one(user, updated_user)
                            return send_message(message=returnMessage, phone=phone)
                    except Exception as e:
                        returnMessage = "Enter correct amount!\nPlease let us know the Amount to be collected from the customer"
                        updated_user = {"$set": {'returnMessage' : returnMessage}}
                        db_operations.update_one(user, updated_user)
                        return send_message(message=returnMessage, phone=phone)
            # 3 - Track order
            elif "Enter AWBNo (Airway Bill number)" in value:
                if message == '9':
                    returnMessage = "Welcome to paapos, your preferred delivery partner\n\nTo Book Same Day Order Reply 1\nTo Book Courier Reply 2\nTo Track Your Order Reply 3\nTo cancel your order reply 4\nTo connect with our Executive reply 5\nFor feedback reply 6\n\nFor the main menu, type *0*\nFor the previous menu, type *9*"
                else:
                    resp = track_order(AWBNo=message)
                    returnMessage = "_" + resp['ReplyMsg'] + "_"
                    if resp['ReplyCode'] == 0:
                        returnMessage += "\n\n*SUMMARY*\n"
                        summary = resp['ShipSum'][0]
                        returnMessage += "Status date: " + summary['StatusDate'] + "\n"
                        returnMessage += "Status time: " + summary['StatusTime'] + "\n"
                        returnMessage += "Status: " + summary['Status'] + "\n"
                        returnMessage += "Location: " + summary['Location'] + "\n"
                        returnMessage += "Comment: " + summary['Comment'] + "\n"
                        # returnMessage += "Status code: " + summary['StatusCode'] + "\n"
                        # returnMessage += "Weight: " + summary['Weight'] + "\n"
                    else:
                        returnMessage += "\n\nPlease enter correct tracking ID booked on Paapos."
                updated_user = {"$set": {'returnMessage' : returnMessage}}
                db_operations.update_one(user, updated_user)
                return send_message(message=returnMessage, phone=phone)
            elif "Please enter correct tracking ID booked on Paapos" in value:
                if message == '9':
                    returnMessage = "Enter AWBNo (Airway Bill number)"
                else:
                    resp = track_order(AWBNo=message)
                    returnMessage = "_" + resp['ReplyMsg'] + "_"
                    if resp['ReplyCode'] == '0':
                        returnMessage += "\n\n*SUMMARY*\n"
                        summary = resp['ShipSum']
                        returnMessage += "Status date: " + summary['StatusDate'] + "\n"
                        returnMessage += "Status time: " + summary['StatusTime'] + "\n"
                        returnMessage += "Status: " + summary['Status'] + "\n"
                        returnMessage += "Location: " + summary['Location'] + "\n"
                        returnMessage += "Comment: " + summary['Comment'] + "\n"
                        # returnMessage += "Status code: " + summary['StatusCode'] + "\n"
                        # returnMessage += "Weight: " + summary['Weight'] + "\n"
                    else:
                        returnMessage += "\n\nPlease enter correct tracking ID booked on Paapos."
                updated_user = {"$set": {'returnMessage' : returnMessage}}
                db_operations.update_one(user, updated_user)
                return send_message(message=returnMessage, phone=phone)
            # 4 - Order cancellation
            elif "Enter Airway Bill number (AWBNo)" in value:
                if message == '9':
                    returnMessage = "Welcome to paapos, your preferred delivery partner\n\nTo Book Same Day Order Reply 1\nTo Book Courier Reply 2\nTo Track Your Order Reply 3\nTo cancel your order reply 4\nTo connect with our Executive reply 5\nFor feedback reply 6\n\nFor the main menu, type *0*\nFor the previous menu, type *9*"
                    updated_user = {"$set": {'returnMessage' : returnMessage}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
                else:
                    returnMessage = "Enter the reason for cancellation"
                    updated_user = {"$set": {'returnMessage' : returnMessage, 'AWBNo' : message}}
                    db_operations.update_one(user, updated_user)
                    return send_message(message=returnMessage, phone=phone)
            elif "Enter the reason for cancellation" in value:
                if message == '9':
                    returnMessage = "Enter Airway Bill number (AWBNo)"
                else:
                    reason = message
                    AWBNo = user['AWBNo']
                    resp = cancel_order(AWBNo=AWBNo, reason=reason, CID=user['cid'])
                    if resp['ReplyCode'] == 0:
                        returnMessage = resp['ReplyMsg']
                    else:
                        returnMessage = "Invalid AWBNo. Enter Airway Bill number (AWBNo) again or type *0* to go back to main menu."
                updated_user = {"$set": {'returnMessage' : returnMessage}}
                db_operations.update_one(user, updated_user)
                return send_message(message=returnMessage, phone=phone)
            # 6 - Feedback
            elif "On a scale of 1 to 5" in value:
                returnMessage = ""
                if message == '9':
                    returnMessage = "Welcome to paapos, your preferred delivery partner\n\nTo Book Same Day Order Reply 1\nTo Book Courier Reply 2\nTo Track Your Order Reply 3\nTo cancel your order reply 4\nTo connect with our Executive reply 5\nFor feedback reply 6\n\nFor the main menu, type *0*\nFor the previous menu, type *9*"
                elif message in ["1", "2", "3", "4", "5"]:
                    returnMessage = "Thank you for your valuable feedback\n\nTo connect with our Executive reply 5 or call 9378293782.\n\nType *0* to go back to main menu."
                    updated_user = {"$set": {'rating' : message}}
                    db_operations.update_one(user, updated_user)
                elif message != "0":
                    returnMessage = "Invalid input!\nOn a scale of 1 to 5, please rate our service, 1 being the lowest."
                updated_user = {"$set": {'returnMessage' : returnMessage}}
                db_operations.update_one(user, updated_user)
                return send_message(message=returnMessage, phone=phone)
            elif "Thank you for your valuable feedback" in value:
                returnMessage = ""
                if message == '9':
                    returnMessage = "On a scale of 1 to 5, please rate our service, 1 being the lowest."
                elif message == '5':
                    returnMessage = "Please wait while we are connecting your call with our Executive.\n\nType *0* to go back to main menu"
                elif message == '0':
                    returnMessage = "Welcome to paapos, your preferred delivery partner\n\nTo Book Same Day Order Reply 1\nTo Book Courier Reply 2\nTo Track Your Order Reply 3\nTo cancel your order reply 4\nTo connect with our Executive reply 5\nFor feedback reply 6"
                updated_user = {"$set": {'returnMessage' : returnMessage}}
                db_operations.update_one(user, updated_user)
                return send_message(message=returnMessage, phone=phone)
            else:
                returnMessage = "Welcome to paapos, your preferred delivery partner\n\nTo Book Same Day Order Reply 1\nTo Book Courier Reply 2\nTo Track Your Order Reply 3\nTo cancel your order reply 4\nTo connect with our Executive reply 5\nFor feedback reply 6\n\nFor the main menu, type *0*\nFor the previous menu, type *9*"
                updated_user = {"$set": {'returnMessage' : returnMessage}}
                db_operations.update_one(user, updated_user)
                return send_message(message=returnMessage, phone=phone)
        # elif messageType == 'media':
        # 	url = message['url']
        # 	return send_message(message="Message received!", phone=phone)
        # elif messageType == 'doc':
        # 	url = message['url']
        # 	return send_message(message="Message received!", phone=phone)
        # workbook.save("data.xlsx")
        return ""

if(__name__) == '__main__':
    app.run(port=8000)