import pychrome
#brave --remote-debugging-port=9222
#pip install pychrome
#use ctrl+c to stop program in terminal

def check_title(tab):
    response = tab.Runtime.evaluate(expression="document.title")
    print(response)
    title = response['result']['value']
    return title

# create a browser instance
browser = pychrome.Browser(url="http://127.0.0.1:9222")

# create a tab
tab = browser.new_tab()


tab.start()

tab.Network.enable()

tab.Page.navigate(url="https://youtube.com/", _timeout=5)

'''
tab.DOM.enable()
response = tab.Runtime.evaluate(expression="document.title")
print(response)

html = response['result']['value']

print(html)
'''

# wait for loading
while(True):
    tab.wait(10)
    title = check_title(tab)
    title = title.replace(' - YouTube','')
    with open("Now_Playing.txt", "w") as text_file:
        text_file.write("{0}".format(title))

