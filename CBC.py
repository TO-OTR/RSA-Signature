# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 19:48:43 2021

@author: to_ot
"""

"""
This part is mainly to simulate the CBC process, unlimited length of message.
"""
import MathWork as MW
import random
from operator import xor


"""
Accoding to definition, for each block size 0<B_S<n.
int -> int
"""
def SelectBlockSize(na):
    block_size = int(input("Please entre the length of block："))
    while block_size >= len(str(na)):
        block_size = int(input("The block size B_S should be 0 < B_S < length of na, entre another: "))
    return block_size


"""
Transfer the num_sec into blocks and do the padding
int,int -> list_int,int
"""
def Separate_block(msg,n): #To transfer the num_sec into blocks
    default_len = n
    str_msg = str(msg)
    block_list = []
    for i in range(0,len(str_msg),default_len):
        block_list.append(str_msg[i:i+default_len])
    res_list, n_pad = Padding(block_list,default_len) #res_list is a string list
    for i in range(0,len(res_list)):
        res_list[i]=int(res_list[i])
    return res_list, n_pad


def Padding(block_list,default_len): #To do padding to the block data
    n_pad = default_len - len(block_list[-1])
    if n_pad > 0:
        temp = block_list[-1]
        for i in range(default_len - n_pad,default_len):
            temp += '0'
        block_list[-1] = temp
    """
    else:
        temp = ''
        for i in range(0,default_len):
            temp += '0'
        block_list.append(temp)
    """
    return block_list, n_pad


def Combine_block(C,n,n_pad):#Combine the blocks
    S = dePadding(C,n,n_pad) #int list
    msg = CombineIntListToInt_add0(S,n,n_pad)
    return msg

"""
Add 0 back to blcoks who may lost some 0 on the left during the transform of str->int
"""
def CombineIntListToInt_add0(S,n,n_pad):#int list ->int
    S_str = ''
    for i in range(0,len(S)):
        temp = n - len(str(S[i]))
        if temp > 0 and i != len(S)-1:
            for j in range(0,temp):
                S_str += '0'
        if temp > 0 and i == len(S)-1:
            for j in range(0,n-n_pad-len(str(S[i]))):
                S_str += '0'
        S_str += str(S[i])
    return int(S_str)


"""
Do dePadding to blocks
"""
def dePadding(block_list,default_len,n_pad): #
    temp = str(block_list[-1])
    temp = temp[0:len(temp) - n_pad]
    temp = int(temp)
    block_list[-1] = temp
    return block_list #int list


"""
Combine the list to a large in number and get the list of length of each blocks
"""
def CombineIntListToInt_unitlen(M):
    res_str = ''
    unit_len = []
    for i in range(0,len(M)):
        res_str += str(M[i])
        unit_len.append(len(str(M[i])))
    res_int = int(res_str)
    return res_int,unit_len


"""
Separate the large number into list by using the list of length of each blocks
"""
def SeparateIntToIntList(C_int,unit_len):
    C_str = str(C_int)
    C = []
    j = 0
    for i in range (0,len(unit_len)):
        C.append(int(C_str[j:j+unit_len[i]]))
        j +=unit_len[i]
    return C


"""
The main process of CBC/RSA/Padding encryption
"""
def en_CBC(msg,ea,na,block_size):
    #very important
    #if block lenth = or > n there will be error in mod expnoent
    #Create new iv each time
    n = block_size
    str_iv = ''
    for i in range(0,n):
        str_iv += str(random.randint(0,9))
    iv = int(str_iv)
    C_cbc=[]
    S_block, n_pad = Separate_block(msg,n) #S_block is an int list
    print('After Padding the blocks are :',S_block)
    for i in range(0,len(S_block)):
        if i == 0:
            C_cbc.append(xor(iv,S_block[i])) #CBC encryption
        else:
            C_cbc.append(xor(C_cbc[i-1],S_block[i]))
    print('After Padding and CBC the blocks are:',C_cbc)
    C_cbc_rsa = []
    for i in range(0,len(C_cbc)):
        C_cbc_rsa.append(MW.home_mod_expnoent(C_cbc[i],ea,na))
    print('After Padding, CBC and RSA the blocks are:',C_cbc_rsa)
    C_int, unit_len= CombineIntListToInt_unitlen(C_cbc_rsa)
    return C_int,iv,n_pad,unit_len


"""
The main process of CBC/RSA/Padding decryption
"""
def de_CBC(C_int,n_pad,iv,da,na,unit_len,block_size):
    n = block_size
    C_cbc = []
    C_cbc_rsa = SeparateIntToIntList(C_int,unit_len)
    print('After trans message to Blocks:',C_cbc_rsa)
    print('The number of blocks:',len(unit_len))
    for i in range(0,len(C_cbc_rsa)):
        C_cbc.append(MW.home_mod_expnoent(C_cbc_rsa[i],da,na))
    print('After RSA the blcoks are:',C_cbc)
    P=[]
    for i in range(len(C_cbc)-1,-1,-1):
        if i == 0:
            P.append(xor(iv,C_cbc[i]))
        else:
            P.append(xor(C_cbc[i-1],C_cbc[i]))
    P.reverse()
    print('After RSA and CBC the blocks are:',P)
    S = Combine_block(P,n,n_pad)
    print('After RSA, CBC and depadding,the blcoks are:',S)
    return S