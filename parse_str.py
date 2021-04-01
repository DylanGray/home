#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np

def parse_str(s,sl):
    ## parses a string, s, into a dict of strings each with maximum length of sl 
    ## dit keys are defined 0,1,2... 
    
    def split_str(s,n):
        #helper function
        ##takes string, s and splits it at nth character, returning two strings.
        tmp1 = s[0:n]
        tmp2 = s[n:]
        return tmp1, tmp2

    def search_str(s,n):
        #helper function 
        #returns the closest space PREVIOUS to the n-th character in str, s
        c = 1
        while not s[n-c-1:n-c].isspace():
            c += 1
        val = n-c
        return val

    
    l = len(s)
    limit_factor = np.floor(l/sl)+1
    q = 0
    text_dict = {}
    while q <= limit_factor:
        qkey = str(q)
        if len(s) < sl:
            text_dict[qkey] = s
        elif s[sl-1:sl].isspace():
            qval, s = split_str(s,sl)
            text_dict[qkey]= qval
        else:
            good_split = search_str(s,sl)
            qval, s = split_str(s,good_split)
            text_dict[qkey]= qval
        q += 1
        
    return text_dict


#### Testing Stuff 

def print_dict(d):
    ##prints each string in given dict of strings, d
    i = 0
    while i < len(d):
        key = str(i)
        i +=1
        print(d[key]) 
    

test1 = "Wow. What a great bit of text this is. Probably the best test text tested today. Surely there is no way this test text can be bested."
test2 = "A new contender for test text. This has some num3123sda and !@# other ^*>A< symbols sprinkled in with no real direction. Hopefully the output is still sensible. Oh, and this test text is even longer that then last on. So that's super, duper stellar and makes me so happy. Wow."
test3 = "Crest factor: Crest factor is a parameter of a waveform, such as alternating current or sound, showing the ratio of peak values to the effective value. In other words, crest factor indicates how extreme the peaks are in a waveform. Crest factor 1 indicates no peaks, such as direct current or a square wave. Higher crest factors indicate peaks, for example sound waves tend to have high crest factors.Crest factor is the peak amplitude of the waveform divided by the RMS value of the waveform. This is equivalent to the ratio of the L∞ norm to the L2 norm of the function of the waveform... From Wikipedia, the free encyclopedia."


B = parse_str(test2, 40)
print_dict(B)

C = parse_str(test3, 70)
print_dict(C)

### There is currently a bug in end lind duplication for certain combinations of input string and max string length
### uncomment below for example

#A1 = parse_str(test1, 24)
#AE1 = parse_str(test1, 25)   
#AE2 = parse_str(test1, 26)
#A2 = parse_str(test1, 27)
#print_dict(A1)
#print_dict(AE1)

