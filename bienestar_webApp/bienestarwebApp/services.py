import requests

def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

'''def get_address(params={}):
    response = generate_request('https://jrmovil.pythonanywhere.com/HBB/cm/1.0/?address=19.1111111,-99.2222222', params)
    
    return '''