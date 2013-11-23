#!/usr/bin/env python 

import sys

def ave_word_length(filename):
    try:
        f = open(filename)
	
	contents = f.read()
	lst_content = contents.split()
	set_content = list(set(lst_content))
	length = 0

	for el in set_content:
	    num = lst_content.count(el)
	    length += num*len(el)
  
	avg_w_length  = int(length) / int(len(lst_content))
        return avg_w_length

    except:
        return (-1)


if __name__=="__main__":

    if len(sys.argv) < 2:
        print "python avg_word_length filename"
	print "filename according to u "
	sys.exit(-1)
    else:
        avg_w_length = ave_word_length(sys.argv[1])
	if avg_w_length ==-1:
            print 
	    print "file does not exit"
	    print "python avg_word_length filename"
	    print "filename according to u "
            print 
	    sys.exit(-1)
        else:
            print 
	    print " the sum of all the lengths of the word tokens in the text, divided by the number of word tokens is:",
	    print avg_w_length 
            print 


     

    
