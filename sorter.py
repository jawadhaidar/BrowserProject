# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 12:04:40 2023

@author: mcc
"""
#sorter from the last assignment
def compare_alpha(in1,in2):#check nif in1 less than in2
    #loop acc to min length
    in1_length=len(in1)
    in2_length=len(in2)
    #compare
    for id in range(min(in1_length,in2_length)):
        in1_status=in1[id].isupper()
        in2_status=in2[id].isupper()
        #case both are small or capital
        if in1_status==in2_status:
            if in1[id]<in2[id]:
                return True
        #case first is capital and second small
        elif in1_status and not in2_status:
            if in1[id].lower() < in2[id]:
                return True

        #case second is capital
        elif not in1_status and in2_status:
            if in1[id] <= in2[id].lower(): #= to give privilege for lower case
                return True
            
    return False
#order matters once you call func inside func
def selectionSort(list1): #O(n^2)
  border=0
  while border <len(list1)-1: #O(n), n being the length of the list
    minIndex=border # contain the index of the minimum element
    for i in range(border+1, len(list1)): # to find the index of the minimum element, O(n)
      if compare_alpha(list1[i],list1[minIndex]): #O(1), is the line that specifies the order
        minIndex=i
    #swap the two elements
    temp=list1[border] #O(1)
    list1[border]=list1[minIndex]
    list1[minIndex]=temp

    # list1[border],list1[minIndex]=list1[minIndex],list1[border]

    border=border+1