from pwn import *
from randcrack import RandCrack



host = 'challenge.nahamcon.com'
port = 31000

while 1:
	s = remote(host,port)
	rc = RandCrack()
	s.recv()

	for i in range(624):
		s.sendline('2')
		answer = s.recv().decode('utf-8').split('\n')
		num = int(answer[1])
		rc.submit(num)
		print(answer,str(i))


	s.sendline('3')
	print(s.recv())
	s.sendline(str(rc.predict_randrange(0,4294967295)))
	print(s.recv())
	flag_ans = s.recv()
	if b'flag{' in flag_ans:
		break

	s.close()
