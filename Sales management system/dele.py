def pos(s):
	a=open("product.txt")
	lines = a.readlines()
	a.close()
	p=-1
	q=0
	for i in lines:
		q=q+1
		p=i.find(s)
		if p!=-1:
			flag=i
			break
	if p!=-1:
		del lines[q-1]
		b=open("product.txt","w+")
		for line in lines:
			b.write(line)
		b.close()

def pos1(s):
	a=open("product2.txt")
	lines = a.readlines()
	a.close()
	p=-1
	q=0
	for i in lines:
		q=q+1
		p=i.find(s)
		if p!=-1:
			flag=i
			break
	if p!=-1:
		del lines[q-1]
		b=open("product2.txt","w+")
		for line in lines:
			b.write(line)
		b.close()
		
def pos2(s):
	a=open("result.txt")
	lines = a.readlines()
	a.close()
	p=-1
	q=0
	for i in lines:
		q=q+1
		p=i.find(s)
		if p!=-1:
			flag=i
			break
	if p!=-1:
		del lines[q-1]
		b=open("result.txt","w+")
		for line in lines:
			b.write(line)
		b.close()