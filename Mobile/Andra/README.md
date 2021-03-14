You know what to do. :) 

##############################

Firstly installed the app with https://appetize.io/app/76cz0p96719qua63dubpby96ug?device=nexus5&scale=75&orientation=portrait&osVersion=8.1 and saw that there is a login form:

![image](https://user-images.githubusercontent.com/59511698/111085489-3932a480-8520-11eb-8fba-f8a91cf273e1.png)

Tried to login and was getting message `ERROR`.

After that I opened the app with `jadx` and searched for words like `flag`,`password`, etc. with no results.

After much analysis, I decided to check MainActivity class and saw that it has the variables of the name,password and Login button.
And at the bottom it had this:

![image](https://user-images.githubusercontent.com/59511698/111085020-130c0500-851e-11eb-84f4-42ab21e9f88b.png)

```
button.setOnClickListener(new MainActivity$onCreate$1(this, "Nahamcom", "pink_panther@786"));
```

So tried as username: `Nahamcom`
and password: `pink_panther@786`

and got the flag:

![image](https://user-images.githubusercontent.com/59511698/111085570-8dd61f80-8520-11eb-9d6d-b24e3cad5392.png)

Flag: flag{d9f72316dbe7ceab0db10bed1a738482}
