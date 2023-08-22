import requests

def thingspeak_receive():
    channelid = '2244862'
    key = '4WSBEBXLNM7JDQAK'
    ultimos = 1
    url = f'https://api.thingspeak.com/channels/{channelid}/feeds.json?api_key={key}&results={ultimos}'
    print(f"url recepcion: {url}")
    data = requests.get(url).json()
    channel = data['channel']['id']
    descripcion = data['channel']['description']
    valor = data['feeds'][0]['field1']

    return int(valor)
# if __name__ == '__main__':
#     thingspeak_receive()