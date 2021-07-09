import requests
# district_base_url = ""
# telegram_base_url = ""
pincode_base_url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=110001&date=08-07-2021"
response = requests.get(pincode_base_url)
response = response.json()

def fetch_required_data(response):
    for center in response['centers']:
        for session in center['sessions']:
            print('Centre Name :',center["name"])
            print('Address :',center["address"])
            print('Fee_type :',center["fee_type"])
            print('Vaccine Name :',session["vaccine"])
            print('Min Age Limit :',session["min_age_limit"])
            print('Avaliable Dose 1 :',session["available_capacity_dose1"])
            print('Avaliable Dose 2 :',session["available_capacity_dose2"])
            print("Slots : ",session['slots'])
            print('------------------------------------------')
    


if __name__=='__main__':
    fetch_required_data(response)


