import urllib.request
import passwordsearch

webUrl = urllib.request.urlopen('https://www.facebook.com')

# Get the result code and print it
print("result code: " + str(webUrl.getcode()))

# Search for users password


# Print Users password to the screen
print("result password: " + str(webUrl.getpassword()))
