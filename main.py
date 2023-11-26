from helper_functions import*
#create a browser
chrome=Browser()

while(not chrome.exit):
    
    inputuser=input("1. Open Tab 2. Close Tab 3. Switch Tab 4. Display All Tabs 5. Open Nested Tab 6. Sort All Tabs 7. Save Tabs 8. Import Tabs 9. Exit")
    if inputuser=="1":
        #open tab
        chrome.openTab()
    elif inputuser=="2":
        chrome.closeTab()
    elif inputuser=="3":
        chrome.switchTab()
    elif inputuser=="4":
        chrome.diplayAllTabs()
    elif inputuser=="5":
        chrome.openNestedTab()
    elif inputuser=="6":
        chrome.sortAllTabs()
    elif inputuser=="7":
        chrome.saveTabs()
    elif inputuser=="8":
        chrome.importTabs()
    elif inputuser=="9":
        chrome.exitBrowser()
        
        
        