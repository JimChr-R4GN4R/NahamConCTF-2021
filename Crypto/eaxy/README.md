Firstly I ensured that it's not a file like .png etc by bruteforcing with https://github.com/JimChr-R4GN4R/TaurusG4T3 .
So after getting no result,I decided to xor the file with all 255 possible bytes.
After a while I found that at some point there was a part which was saying 
'The XOR key you used to find string this is the X character index of the flag :)' 
Then I made a script that prints all xored results and the specific character that they were xored with and found the flag.
![image](https://user-images.githubusercontent.com/59511698/111084258-303ed480-851a-11eb-9c7a-0b0ae3ad94d8.png)

Flag: flag{16edfce5c12443b61828af6cab90dc79}
