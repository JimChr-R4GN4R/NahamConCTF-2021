Firstly I checked for suspicious text by xoring all 255 possible bytes with the eaxy file. After a while I found that at some point there was a part which was saying 
'The XOR key you used to find string this is the X character index of the flag :)' 

So I pasted all the results which were containing the byte which was xored with the xored text and searched X character one by one and got the flag.

Flag: flag{16edfce5c12443b61828af6cab90dc79}