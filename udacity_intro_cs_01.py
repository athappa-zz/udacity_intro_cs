
string = "Andrew"
print string[0]
print (string+string)[0]

print string[1]
print (string+'ity')[1]

print string[-1]
print (string+string)[-1]

word = 'assume'
print word[3]
#just like in R, a colon will give us from pos 3 to pos 6
print word[3:6]
print word[:]

print 'clear'

s = '12'
print s[:]
print s+s[0:-1+1]
print s[0:]
print s[:-1]
print s[:3]+s[3:]

#Find strings in strings
pythogoras = 'There is geometry in the humming of the strings'
print pythogoras.find('string')
print pythogoras[40:]
print pythogoras.find(pythogoras)
print pythogoras.find(pythogoras+'!!!')+1

page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
print page
start_link = page.find('<a href=')
print start_link

start_http = page.find('http:',start_link)
print start_http

stop_http = page.find(">",start_http)-1
print stop_http

url = page[start_http:stop_http]
print url 