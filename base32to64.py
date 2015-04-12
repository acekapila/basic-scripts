#!/usr/bin/python


def convbin(hex32):
	k=''
	if hex32.count('=')==4:
		lenh=16
	elif hex32.count('='):
		lenh=24
	elif hex32.count('=')==1:
		lenh=32
	elif hex32.count('=')==6:
		lenh=8
	else:
		lenh=40
	for i in range(len(hex32)-hex32.count('=')):
		for j in range(32):
			if dict32[j]==hex32[i].upper():
				l=j
				break
		bina=bin(int(l))
		bina=bina[2:]
		bina='0'*(5-len(bina))+bina
		k=k+bina
	return k[:lenh]

def conv64(binary):
	r=''
	if len(binary)%24==16:
		binary=binary+'00'
		lenh=18
		pad='='
	elif len(binary)%24==8:
		binary=binary+'0000'
		lenh=12
		pad='=='
	else:
		lenh=24
		pad=''
	for i in range(0,lenh,6):
		tmp=binary[i:i+6]
		#print tmp
		for j in range(64):
			if str('0'*(6-len(bin(j)[2:]))+bin(j)[2:])==tmp:
		        	r=r+str(dict64[j])
		        	break
		#print x
	return r+ pad

dict32={}
for i in range(32):
	if i<26:
		dict32[i]=chr(65+i)
	else:
		dict32[i]=str(i-24)

dict64={}
for i in range(62):
	if i<26:
		dict64[i]=chr(65+i)
	elif i<52:
		dict64[i]=chr(71+i)
	else:
		dict64[i]=str(i-52)
dict64[62]='+'
dict64[63]='/'


n=raw_input('Number of hash inputs :')
for i in range(0,int(n)):
	base32hex=raw_input('Enter Base32 Hash : ')
	binary=''
	for word in range(0,len(base32hex)-1,8):
		binary=binary+convbin(str(base32hex[word:word+8]))


	base_64=''
	for j in range(0,len(binary)-1,24):
		base_64=base_64+conv64(binary[j:j+24])
	
	print 'Base64 hash is : '+str(base_64)

