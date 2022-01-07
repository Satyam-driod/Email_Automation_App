import requests

def getWeatherDetails(cityname):

	api_key='8deef72eaf17ac2b466730b35f7d9314'
	url=f'https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={api_key}'
		
	response= requests.post(url).json()
	# print("success")
	temp=response['main']['temp']
	temp=temp-273
	return int(temp)
		