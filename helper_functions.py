# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 09:17:59 2023

@author: mcc
"""
import requests

class Browser():
    def __init__(self):
        self.database={} 
        self.order_list=[]
        
    def openTab(self):
        tabTitle=input("please add the tab title ")
        tabURL=input("please add the tab URL ")
        #add it to the list 
        self.order_list.append(tabTitle)
        #add it to the database 
        self.database[tabTitle]={"parentURL":tabURL}
        
       
    def closeTab(self):
        tabTitle2close=input("please add the tab title to close ")
        if tabTitle2close!='':
            #remove from list
            self.order_list.remove(tabTitle2close)
            #remove from database
            del self.database[tabTitle2close]
        else:
            #remove last
            self.database.popitem()
            #remove last from list
            self.order_list.pop()
            
    def switchTab(self):
        index=int(input("put the  index of tab: "))
        #TODO: you can include the nested tab 
        if index!='':
            #display content of chosen title
            keyIndex=self.order_list[index]
            urlIndexed=self.database[keyIndex]['parentURL']
            print(f'urlIndexed {urlIndexed}')
            
        else:

            keyIndex=self.order_list[-1]
            urlIndexed=self.database[keyIndex]['parentURL']
            #remove last openned tab
            pass
        # create request
        x = requests.get(urlIndexed)
        #convert request to string datatype
        text = x.text 
        print(text)
    def diplayAllTabs(self):
        #loop parents
        for key,value in self.database:
            #loop children
            for ch_key,ch_value in value:
                if ch_key=="parentURL":
                    print("key")
                else: 
                    print(f'    {ch_key}')
                
    def openNestedTab(self):
        #index of parent tab is different than the index of ordered list tab 
        #you should choose index from the dictionary
        index=int("please input the index of the parent")
        keyindex=list(self.database)[index]
        
        
    def sortAllTabs(self):
        pass
    def saveTabs(self):
        pass
    def importTabs(self):
        pass
    def exitBrowser(self):
        pass
        
    
if __name__ == '__main__':
    "test areana"
    chrome=Browser()
    chrome.openTab()
    chrome.switchTab()
    


    
    
    

    

