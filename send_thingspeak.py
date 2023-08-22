import urllib.request
import threading

def thingspeak_send(luz):
    # threading.Timer(15, thingspeak_send).start()
    url = 'https://api.thingspeak.com/update?api_key='
    key = 'R8XEHQMC7RS54H86'
    header = '&field1={}'.format(luz)
    new_url = url + key + header
    print(f"url: {new_url}")
    data = urllib.request.urlopen(new_url)

# if __name__ == '__main__':
#     thingspeak_send(250)