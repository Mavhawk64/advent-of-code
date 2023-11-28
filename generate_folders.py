import os

year = 2023

if not os.path.isdir(f"./{year}"):
	os.mkdir(f"./{year}")

os.chdir(f"./{year}")

for i in range(1,26):
	if not os.path.isdir(f"./{i:02d}"):
		os.mkdir(f"./{i:02d}")
	f1 = open(f"./{i:02d}/1.py","w")
	f2 = open(f"./{i:02d}/2.py","w")
	f3 = open(f"./{i:02d}/input.txt","w")
	f1.close()
	f2.close()
	f3.close()