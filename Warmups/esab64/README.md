Was it a car or a cat I saw? 

#############################

From the title I realized that it was `inversed base64`.

So just run this python script:
```
a = 'mxWYntnZiVjMxEjY0kDOhZWZ4cjYxIGZwQmY2ATMxEzNlFjNl13X'
a[::-1] == 'X31lNjFlNzExMTA2YmQwZGIxYjc4ZWZhODk0YjExMjViZntnYWxm'
```

base64 decode: `_}e61e711106bd0db1b78efa894b1125bf{galf`

```
flag = ' _}e61e711106bd0db1b78efa894b1125bf{galf'
flag[::-1] == flag{fb5211b498afe87b1bd0db601117e16e}
```

Flag: flag{fb5211b498afe87b1bd0db601117e16e}
