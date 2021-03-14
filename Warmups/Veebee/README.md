After searching decode a VB script file,
downloaded this tool http://scriptbox.toll.at/index.php?showcontent=Decode%20VBE%20to%20VBS.vbs&list=1

Then just drag and drop the veebee.vbe to Decode VBE to VBS.vbs and you will get veebee.vbs .

> strings veebee.vbs

```
' VeeBee goes buzz buzz
MsgBox("Sorry, not that easy!")
MsgBox("Okay, actually, you're right. It is that easy.")
MsgBox("flag{f805593d933f5433f2a04f082f400d8c}")
```

flag: flag{f805593d933f5433f2a04f082f400d8c}