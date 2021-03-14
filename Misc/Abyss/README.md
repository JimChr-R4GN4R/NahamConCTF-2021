Connect with:

# Password is userpass
ssh -p 32140 user@challenge.nahamcon.com


#########################################

I ssh and put password it and it was showing random chunks.

So decided to grep the results.


> sshpass -p userpass ssh -p 32140 user@challenge.nahamcon.com | grep 'flag'


After some minutes decided to stop the process (ctrl+c),so it printed all greps, and got the flag.


Flag: flag{db758a0cc25523993416c305ef15f9ad}