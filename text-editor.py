import os
import sys
from pythonds.basic.stack import Stack
global s
global s1
s=Stack()
s1=Stack()
text = []

loaded = []
filename = "file.txt"
autosave = False

def open_text(name=filename):
	global text

	f = open(name, "rU")
	text[:] = []
	for line in f:
		text.append(line.replace("\n",""))
	f.close()

def print_text():
	x = 0
	for line in text:
		print x, line
		x+=1

def print_t(n,m):
	x = 0
	for line in text:
		if x >= int(n) and x <= int(m):
			print x, line
			x+=1

def insert(n,t):
	x = 0
	text.insert(int(n),t)

def ins(n,m,te):
	x = int(n)
	for i in te:
		text.insert(x,i)
		x += 1


def delete(n):
	del text[int(n)]

def dele(n,m):
	global temp
	x = 0
	temp = []
	while x <= int(m)-int(n):
		temp.append(text[int(n)])
		del text[int(n)]
		x += 1
		
def cpy(n,m):
	global buf
	buf = []
	x = 0
	for line in text:
		if x >= int(n) and x <= int(m):
			buf.append(line)
		x += 1

def pas(n):
	if buf is not None:
		final = " ".join(buf)
		text.insert(int(n),final)


def interperit(command):
	global text
	global filename
	global autosave
	global buf
	global temp
	command_list = command.split(".")
	if len(command_list) == 1:
		if command_list[0] == "d":
			print_text()
		elif command_list[0] == "z":
			if not s.isEmpty():
				comm = s.pop()
				comm_list = comm.split(".")
				if comm_list[0] == "dd":
					n = comm_list[1]
					p = text[int(n)]
					s1.push("i." + n + "." + p)
					delete(n)
				elif comm_list[0] == "i" and len(comm_list) == 3:
					n = comm_list[1]
					t = comm_list[2]
					s1.push("dd." + n)
					insert(n,t)
				elif comm_list[0] == "i" and len(comm_list) == 4:
					n = comm_list[1]
					m = comm_list[2]
					te = comm_list[3]
					fi = te.split(",")
					s1.push("dd." + n + "." + m)
					ins(n,m,fi)
			else:
				print "You have no command for undo"

		elif command_list[0] == "r":
			if not s1.isEmpty():
				comm = s1.pop()
				comm_list = comm.split(".")
				if comm_list[0] == "dd" and len(comm_list) == 2:
					n = comm_list[1]
					delete(n)
				elif comm_list[0] == "dd" and len(comm_list) == 3:
					n = comm_list[1]
					m = comm_list[2]
					dele(n,m)
				elif comm_list[0] == "i":
					n = comm_list[1]
					t = comm_list[2]
					insert(n,t)
			else:
				print "You have no command to be undone"

			
	elif len(command_list) != 1:
		if command_list[0] == "d":
			n = command_list[1]
			m = command_list[2]
			print_t(n,m)
		elif command_list[0] == "i":
			n = command_list[1]
			t = command_list[2]
			s.push("dd." + n)
			insert(n,t)
			
		elif command_list[0] == "dd" and len(command_list) == 2:
			n = command_list[1]
			p = text[int(n)]
			s.push("i." + n + "." + p)
			delete(n)
			
		elif command_list[0] == "dd" and len(command_list) == 3:
			n = command_list[1]
			m = command_list[2]
			dele(n,m)
			a = ",".join(temp)
			s.push("i." + n + "." + m + "." + a)

		elif command_list[0] == "yy":
			n = command_list[1]
			m = command_list[2]
			cpy(n,m)
		elif command_list[0] == "p":
			n = command_list[1]
			s.push("dd." + n)
			pas(n)

def main():
	os.system("cls")
	global filename

	if len(sys.argv) > 1:
		filename = sys.argv[1]

	global text
	try: open_text(filename)
	except: print("Default file not found\n\t\"file.txt\" is missing")

	while 1:
		a = raw_input(">>>")
		interperit(a)
		if autosave: save_text()

main()