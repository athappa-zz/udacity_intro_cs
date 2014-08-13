#Get next target
import urllib

def get_page(url):#This function is just to return the webpage contents; the source of the webpage when a url is given.
	try:
		f = urllib.urlopen(url)
		page = f.read()
  		f.close()
  		#print page
  		return page
 	except: 
  		return ""
 		return ""
print get_page('http://xkcd.com/353')

#Goal: to take in a web page and get all the links from the web page

def get_next_target(page):

	if page.find('<a href=') == -1: 
		url = None
		end_quote = 0
		return url, end_quote
		
	else:
		start_link = page.find('<a href=')
		print "start_link = %d" %start_link
	
		start_quote = page.find('"', start_link)
		print "start_quote = %d" %start_quote
	
		end_quote = page.find('"', start_quote + 1)
		print "end_quote = %d" %end_quote
	
		url = page[start_quote + 1:end_quote]
		print "url = %r" %url
	
		return url, end_quote
	
url, endpos = get_next_target(get_page('http://xkcd.com/353'))
print url, endpos

def print_all_links(page):
	while True:
		url, endpos = get_next_target(page)
		if url:
			print url
			page = page[endpos:]
		else:
			break

print print_all_links('http://xkcd.com/353')
#this gets printed out as a tuple or ('string', position)


#this is wrong. doesn't find the link and so the fxn returns -1 and so when
#we get to the url fxn which takes page[-1+1:-1] which returns everything
#but the last letter.


#start_link returns a -1 when it doesn't find a target
#start_link = page.find('<a href=')