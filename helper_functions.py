# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 09:17:59 2023

@author: mcc
"""
import requests
from sorter import*
import json

#do helper function for request
#helper for loop

class Browser():
    def __init__(self):
        self.database={} 
        self.order_list=[]
        self.exit=False
    def _search4ParenttTab(self,soughtTab):
        for key,value in self.database.items(): # O(n) n is the number of databse keys
            
            #loop children    
            for ch_key,ch_value in value.items(): # O(m) m is the number of value ch_keys
                if ch_key==soughtTab:
                    parent=key
                    break
        return parent
        
        
    def _html(url):
        # create request
        x = requests.get(url)
        #convert request to string datatype
        text = x.text 
        return  text
        
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
        if tabTitle2close in self.database.keys():# search algo depends how they implemented it: o(n)
            #parent
            #remove it and its children from ordered list
            self.order_list.remove(tabTitle2close)
            for key,value in self.database[tabTitle2close].items(): # O(n) n is the number of databse keys
                if key!="parentURL":
                    self.order_list.remove(key)
        
            #remove them from dictionary
            del self.database[tabTitle2close]
        else:#not parent
            
            
            self.order_list.remove(tabTitle2close) #remove it from list 
            #search inside each parent to remove it 
            #now remove from dictionary
            #O(mn)
            parent=self._search4ParenttTab(self,tabTitle2close) #check who is the parent
            del self.database[parent][tabTitle2close] #remove children from dictionary
            
            # for key,value in self.database.items(): # O(n) n is the number of databse keys
                
            #     #loop children    
            #     for ch_key,ch_value in value.items(): # O(m) m is the number of value ch_keys
            #         if ch_key==tabTitle2close:
            #             del self.database[key][tabTitle2close] 
            #             break
                        
    
        
            
    def switchTab(self):#print content
        index=input("put the  index of tab acc to orderedlist: ") #acc to list
        #TODO: you can include the nested tab 
        #it can be a parent
        #it can be a child
        
        if index=='':
            tabTitle2display=self.order_list[-1] #choose last title
        else:
            tabTitle2display=self.order_list[int(index)] #get the title corr to the index in the list
        
        
        #is it a parent 
        if tabTitle2display in self.database.keys(): # search algo depends how they implemented it: o(n)
            #display content of chosen title
            urlIndexed=self.database[tabTitle2display]['parentURL']
            
        else: #it is a child
            for key,value in self.database.items(): # O(n) n is the number of databse keys
                
                #loop children    
                for ch_key,ch_value in value.items():  # O(m) m is the number of value ch_keys
                    if ch_key==tabTitle2display:
                        urlIndexed=self.database[key][tabTitle2display] 
                        break
        
        text=self._html(urlIndexed)
        print(text)
        
        
    def diplayAllTabs(self):
        #loop parents
        for key,value in self.database.items():# O(n) n is the number of databse keys
            #loop children
            for ch_key,ch_value in value.items(): # O(m) m is the number of value ch_keys
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
        selectionSort(self.order_list) #O(n^2)
        print(f'self.order_list after {self.order_list}')
        
    def saveTabs(self):
        # Convert and write JSON object to file
        #since my database have the same information except for the content
        #add content only for parents (or it will get messy)
        for key,value in self.database.items(): #O(n)
            text=self._html(self.database[key]["parentURL"])
            self.database[key]["content"]=text
            
        with open(r"C:\Users\mcc\Desktop\my folders\SeFactory\BrowserProject\database.json", "w") as outfile: 
            json.dump(self.database, outfile)
        

    def importTabs(self):
        # JSON file
        #I AM ASSUMING THAT WE ARE IMPORTING THE SAME FILE THAT WE SAVED OR A FILE THAT THE USER CREATED
        #IN THIS WAY THE USER EITHER USES OPEN TABS OPTION TO FILL OR FILLS THE JSON THEN IMPORTS IT
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
    
    


    
    
    

    

