import csv
count=0;
a= []
b= []
x={}
k=0
with open ('marks.csv',newline='') as csvfile:
	 marksreader = csv.reader(csvfile, delimiter=',')
	 columns=len(next(marksreader))
	 csvfile.seek(0)
	 for i in range(columns):
	 	a.append([])
	 	b.append([])
	 for row in marksreader:
	 	if row[0].isdigit():
	 		for i in range(columns):
	 			a[i].append(row[i])
	 		count +=1
	 	elif row[0]=="Sno":
	 		for i in range(columns):
	 			x[row[i]]=k
	 			k+=1
for i in x:
	print(i,"->",x[i])

a.append([])

for j in range(count):
	for i in range(columns):
		if a[i][j] != "NA":
			a[columns][j]=a[i][j]+a[columns][j]
print(columns)
print(len(a[0]))
#for i in range(count):
	#print(a[6][i])
