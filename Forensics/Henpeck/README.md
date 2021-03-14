So I'll be honest, I never actually went through the Mavis Beacon program... 

###########################################################################

Got help from here: https://www.programmersought.com/article/52335860604/


> tshark -r henpeck.pcap -T fields -e usb.capdata > usbdata.txt

Then edited the file to be like this:
```
00:00:00:00:00:00:00:00
00:00:0b:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:08:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:2c:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:04:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:11:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:16:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:1a:00:00:00:00:00
```
(without empty lines or other chunks like small hexes like 18:00:00)

and then:

> python keys_extr.py

and get:
```
output :
SO THE ANSWER IS FLAGF7733E0093B7D281DD0A30FCF34A9634 HAHAHAH LOL
```



Flag: flag{f7733e0093b7d281dd0a30fcf34a9634}
