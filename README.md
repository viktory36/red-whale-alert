# red-whale-alert
A script that alerts to large torrents recently uploaded onto redacted via a sound beep

This script is intended to be run on Windows, the `winsound` library is used for generating beeps (comes included with the pre-built Windows python installer). The `requests` library is used to facilitate http, and is a dependency.

<br />

## Usage
Modify the script and save it with your API key as generated in your profile settings. 
Configure the the `minimum_size` variable to specify the minimum file size in MBs a torrent must have before you are alerted to it. The `torrent_age` variable states the maximum torrent age in seconds possible before you stop receiving alerts for it.

The script generates a `reds_beeped.txt` file to record the torrents it has already alerted you to. It is recommended to run this script in it's own folder for that reason.

<br />

## Credits and acknowledgements
I give thanks to the lovely internet for making information and resources accessible to all.
