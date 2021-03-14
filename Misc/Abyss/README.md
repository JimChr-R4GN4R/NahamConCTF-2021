A Vortex? No... an Abyss.

Connect with: Password is userpass
ssh -p XXXXX user@challenge.nahamcon.com

#########################################

I ssh and put password it and it was showing random chunks.
![image](https://user-images.githubusercontent.com/59511698/111084487-45683300-851b-11eb-9729-dba7f8e29da2.png)

So decided to grep the results.


> sshpass -p userpass ssh -p 32140 user@challenge.nahamcon.com | grep 'flag'


After some minutes decided to stop the process (ctrl+c),so it printed all greps, and got the flag:
![image](https://user-images.githubusercontent.com/59511698/111084804-eefbf400-851c-11eb-9052-c1faa23ea7be.png)


Flag: flag{db758a0cc25523993416c305ef15f9ad}
