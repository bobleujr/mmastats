import urllib2

# opener = urllib.request.FancyURLopener({})
url = "http://www.sherdog.com/fighter/"

for i in xrange(2105,4000):
	print 'Getting page '+str(i)
	try: 
		response = urllib2.urlopen(url+str(i))
		html = response.read()

		text_file = open("fighter"+str(i)+".html", "w")
		text_file.write(html)
		text_file.close()
	except:
		print 'pulou'