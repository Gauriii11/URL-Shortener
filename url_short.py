import pyshorteners
link=input("Enter the Link:")
shortener=pyshorteners.Shortener()
x=shortener.tinyurl.short(link)
print(x) 