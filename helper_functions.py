# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 09:17:59 2023

@author: mcc
"""
import requests
from sorter import*
import json

class Browser():
    def __init__(self):
        self.database={} 
        self.order_list=[]
        self.exit=False
        
    def openTab(self):
        tabTitle=input("please add the tab title ")
        tabURL=input("please add the tab URL ")
        #add it to the list 
        self.order_list.append(tabTitle)
        #add it to the database 
        self.database[tabTitle]={"parentURL":tabURL}
        #better to store {T:{}}
        
       
    def closeTab(self):
        tabTitle2close=input("please add the tab title to close ")
        #it might be a parent 
        #it might be a child
        #last in ordered list might not be the last in dictionary (due to nested)
        #I WILL ASSUME THAT CLOSING A PARENT WILL CLOSE ITS CHILDREN 
        #WHILE CLOSING A CHILDREN WILL NOT CLOSE THE PARENT 
        if tabTitle2close=='':
            tabTitle2close=self.order_list[-1] #if empty take it from the last element of list
            
        
        #is it a parent 
        if tabTitle2close in self.database.keys():
            #parent
            #remove it and its children from ordered list
            self.order_list.remove(tabTitle2close)
            for key,value in self.database[tabTitle2close].items():
                if key!="parentURL":
                    self.order_list.remove(key)
        
            #remove them from dictionary
            del self.database[tabTitle2close]
        else:#not parent
            
            #remove it from list 
            self.order_list.remove(tabTitle2close)
            #search inside each parent to remove it 
            #now remove from dictionary
            for key,value in self.database.items():
                
                #loop children    
                for ch_key,ch_value in value.items():
                    if ch_key==tabTitle2close:
                        del self.database[key][tabTitle2close] 
                        break
                        
    
            
            
        #search inside the nested dictionaries
        
        #     #remove from list
        #     self.order_list.remove(tabTitle2close)
        #     #remove from database
        #     del self.database[tabTitle2close]
        # else:
        #     #remove last
        #     self.database.popitem() #does not have to be the last in the database
        #     #remove last from list
        #     self.order_list.pop()
            
    def switchTab(self):#print content
        index=int(input("put the  index of tab: "))
        #TODO: you can include the nested tab 
        #it can be a parent
        #it can be a child
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
        for key,value in self.database.items():
            #loop children
            for ch_key,ch_value in value.items():
                if ch_key=="parentURL":
                    print(f"{key}")
                else: 
                    print(f'    {ch_key}')
                
    def openNestedTab(self):
        #index of parent tab is different than the index of ordered list tab 
        #you should choose index from the dictionary
        #TODO: you can do a loop for several children for same parent
        index=int(input("please input the index of the parent"))
        title=input("enter the title of the nested tab")
        url=input("enter the url")
        keyindex=list(self.database)[index] #key of parent
        self.database[keyindex][title]=url
        #add it to the ordered list 
        self.order_list.append(title)
        
              
    def sortAllTabs(self):
        print(f'self.order_list before {self.order_list}')
        selectionSort(self.order_list)
        print(f'self.order_list after {self.order_list}')
        
    def saveTabs(self):
        # Convert and write JSON object to file
        with open(r"C:\Users\mcc\Desktop\my folders\SeFactory\BrowserProject\database.json", "w") as outfile: 
            json.dump(self.database, outfile)
        

    def importTabs(self):
        # JSON file
        f = open (r"C:\Users\mcc\Desktop\my folders\SeFactory\BrowserProject\database.json", "r")
         
        # Reading from file
        self.database = json.loads(f.read())
        print(self.database)
        
        
    def exitBrowser(self):
        self.exit=True
    
    


        
    
if __name__ == '__main__':
    "test areana"
    chrome=Browser()
    chrome.openTab()
    chrome.saveTabs()
    chrome.importTabs()
    
    


    
    
    

    

