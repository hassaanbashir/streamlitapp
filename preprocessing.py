# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 23:43:12 2021
file name : preprocessing.py
@author: farhan
"""

# Define a function which takes 2 numberic list as an input
# and find the common element in the list

# ---------------- Reading file containing sentence ID's ----------------
# path_1 --> file that contains only conversation_ids
# path_1 --> file that contains conversation_id with sentences

def my_function(path_1,path_2):
    convs_list = open(path_1).read().split('\n')

    conv_line_list = []
    _conv_list = ""
    for conv_list in convs_list:
        #creating a list for conersational ID's 
           _conv_list = conv_list.split(' +++$+++ ')[-1].replace("'", "").replace(" ","").replace("[","").replace("]","")
           conv_line_list.append(_conv_list.split(','))
       
    conv_line_list[1:3]
    
    # ------ Reading file containing sentence ID's and sentences -------
    dialog_lines_list = open(path_2).read().split('\n')
    
    # Making two lists one for conversation ID's and other for  conversation 
    # Using both list in dictionariies in a way that ;
    # key   =  conversation ID's
    # value =  conversation / sentence
    
    dialog_dict = {dialog_lines_list[counter].split(' +++$+++ ')[0]:    dialog_lines_list[counter].split(' +++$+++ ')[-1] for counter in range(0,len(dialog_lines_list))}
    
     # ----------- Extracting final list for conversations ----------
    convs_dialogs = []
    for convs in conv_line_list:
        conv_dialog = []
        for conv in convs: 
            conv_dialog.append(dialog_dict[conv])
    
        convs_dialogs.append(conv_dialog)
   
    # Returning required list
    return convs_dialogs

