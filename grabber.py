import urllib2 # URL Fetching Library
import bs4 # HTML Parsing Library
import sys

products = {}

def getProducts(url):
	#Obtain Source Code
	sourceCode = urllib2.urlopen(url).read()
 
	# Covert Source Code to a soup
	soup = bs4.BeautifulSoup(sourceCode)
	          
	# Get the product-list element from source code
	productList1 = soup.find("ul", {'class':"product-list"})

	if productList1 is None:
		return
	
	# Get the name of each product
	productSet1 = productList1.findAll("li")
	
	# Initialize an empty list
	global products
	 
	# Get product name, and append to list
	for i in productSet1:
		x = i.find('h2', {'class': 'name'})
		y = i.find('span', {'class': 'price-old'})
		z = i.find('span', {'class': 'price-new'})
		products[x.text]=(y.text, z.text)
	
	op = open("public_html/grab_out.txt", 'a')
	for i in sorted(products.keys()):
		str_print = i+'|'+products[i][0]+'|'+products[i][1]+'\n'
		op.write(str_print.encode('utf-8').strip())
		op.write('\n')
#try:
#op.write(i+', '+str(products[i][0].encode('utf8'))+', '+str(products[i][1].encode('utf8'))+'\n')
#		except UnicodeEncodeError:
#			print products[i]
	op.close()
	
#for i in sorted(products.keys()):
#		print "%s, %s"%(i, products[i])
def getURLs():
	masterURL = "http://www.mygrahak.com//index.php"
	source = urllib2.urlopen(masterURL).read()
	soup = bs4.BeautifulSoup(source)
	urlList = soup.find('ul', {'id': 'nav'})
	urls = []
	x = urlList.findAll('a')
	for i in x:
		try:	
			urls.append(i['href'])
		except KeyError:
			print i
#		except UnicodeEncodeError:
#			print >> sys.stderr, i['href']
	print len(urls)
	for i in range(1235, len(urls)):
		print urls[i]
		try:
		    getProducts(urls[i]+'?limit=100')
		except UnicodeEncodeError:
			print urls[i]
		print "%s of %s done..." % (i, len(urls))



if __name__ == '__main__':
	getURLs()
	print "Done..."

