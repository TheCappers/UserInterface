all:
	(python3 main.py)

clean:
	(rm -rf __pycache__)
	(cd components; rm -rf __pycache__; cd ..)