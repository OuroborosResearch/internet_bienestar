import requests
import json  
# get_preferences, get_profile_data_clean, get_all_mb_plans, get_all_mifi_plans, get_offer_id, get_offer_price, UserProfile, ClienteProfile, Planes
# llamar UserProfile
def UserProfile():
    pass
# llamar get_preferences
def get_preferences(raw):
    pass

# llamar get_profile_data_clean
def get_profile_data_clean(cel):
    
    url = "https://jrmovil.pythonanywhere.com/jr_api/cm/1.0/get_profile_uf/"

    payload={'user_number': cel}
    files=[

    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    #print(response.text)
    return json.loads(response.text)


# llamar get_all_mb_plans
def get_all_mb_plans():
    pass

# llamar get_all_mifi_plans
def get_all_mifi_plans():
    pass

# llamar get_offer_id
def get_offer_id(paquete):
    pass

# llamar get_all_mifi_plans
def get_all_mifi_plans():
    pass

# llamar get_offer_price
def get_offer_price(planId):
    pass

# llamar ClienteProfile
def get_users_length():

    print("[Info][ApiRequests][get_users_length] - Calling ...")
    result = 0
    try:
        url = "https://jrmovil.pythonanywhere.com/webapp/api/1.0/get_user_len"

        payload={}
        headers = {
        'Cookie': 'csrftoken=nAdjIZkmqsTwBPSUZqKXa4LTjCpWdz6wFTOOFPUeFo8wrpaEBL4Cl3ZAbrBZHjOS'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        result = float(response.text)
        result = int(response.text)
        
    except:
        print("[Error][ApiRequests][get_users_length] - There was an Error in the call...")   

    return result

def get_all_plans():
    # https://jrmovil.pythonanywhere.com/media
    print("[Info][ApiRequests][get_all_plans] - Calling ...")
    data = None
    try:
        url = "https://jrmovil.pythonanywhere.com/pagos/cm/1.0/api/get_planes"

        payload={}
        headers = {
        'Cookie': 'csrftoken=nAdjIZkmqsTwBPSUZqKXa4LTjCpWdz6wFTOOFPUeFo8wrpaEBL4Cl3ZAbrBZHjOS'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        data = json.load(response)
        print(data[0]["imagen"])

    except:
        print("[Error][ApiRequests][get_all_plans] - There was an Error in the call...")

    return data


def getUserByNumber(cel): 
  pass

def send_subscriptions(prospect_dict):
    print("[Info][ApiRequests][send_subscriptions] - Calling ...")

    try:
        url = "https://jrmovil.pythonanywhere.com/analytics/cm/1.0/api/saveProspect"
        

        payload={'name': prospect_dict["name"],
                'email': prospect_dict["email"],
                'number': prospect_dict["number"]}
        
        files=[

        ]
        print(payload)
        headers = {
        'Cookie': 'csrftoken=nAdjIZkmqsTwBPSUZqKXa4LTjCpWdz6wFTOOFPUeFo8wrpaEBL4Cl3ZAbrBZHjOS'
        }

        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        
    except:
        print("[Error][ApiRequests][send_subscriptions] - There was an Error in the call...")  

def check_cobertura(lat, long):
    

    url = f"https://jrmovil.pythonanywhere.com/HBB/cm/1.0/checar_cobertura/?address={lat},{long}"
    print(url)
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    return response.text

def get_offerings(offerType):
    url = f"https://jrmovil.pythonanywhere.com/jr_api/cm/1.0/get_offers?offersType={offerType}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.content.decode('utf-8')