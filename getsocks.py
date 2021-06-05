import requests

f = open("socks5.txt",'wb')
try:
	r = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=true",timeout=5)
	f.write(r.content)
except:
	pass
try:
	r = requests.get("https://www.proxy-list.download/api/v1/get?type=socks5",timeout=5)
	f.write(r.content)
except:
	pass
try:
	r = requests.get("https://www.proxyscan.io/download?type=socks5",timeout=5)
	f.write(r.content)
except:
	pass
try:
	r = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",timeout=5)
	f.write(r.content)
except:
	pass
try:
	r = requests.get("https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",timeout=5)
	f.write(r.content)
	f.close()
except:
	f.close()
print("Downloaded")