import requests
import time
import winsound

apikey = {'Authorization': 'your_api_key_here'}
minimum_size = 900 # in MBs
torrent_age = 200 # in seconds

def timeNow():
    return int(time.time())

def getData():
    js = requests.get("https://redacted.ch/ajax.php?action=browse&searchstr=&group_results=0", headers=apikey).json()
    return js['response']['results']

def redFile(data=None):
    with open("reds_beeped.txt", "a+", encoding="utf-8") as redFile:
        redFile.seek(0)
        if(data):
            redFile.write(data + "\n")
            return False
        else:
            return redFile.read()

def beep():
    frequency = 2500 # Change beep settings here
    duration = 1000
    return winsound.Beep(frequency, duration)


def main():
    print("working...")
    while True:
        try:
            data = getData()
            for torrent in data:
                if(torrent['size'] > minimum_size*1024**2 and timeNow()-int(torrent['groupTime'])<torrent_age and torrent['groupName'] not in redFile()):
                    print("Torrent found: " + torrent['groupName'] + " | Size: " + str(torrent['size']/1024**2)[:-7] + " MB")
                    redFile(torrent['groupName'])
                    beep()
            time.sleep(5)
        except Exception as e:
            print(str(e) + "\n Probably experiencing high server load. Backing-off for 15s...")
            time.sleep(15)
            print("Retrying...")
            continue

if __name__ == "__main__":
    main()
