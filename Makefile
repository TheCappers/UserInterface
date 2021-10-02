all:
	(python3 main.py)

clean:
	(rm -rf __pycache__)
	(cd components; rm -rf __pycache__; cd ..)
	(cd configuration; rm -rf __pycache__; cd ..)
	(cd controller; rm -rf __pycache__; cd ..)
	(cd view; rm -rf __pycache__; cd ..)
	(cd view/components; rm -rf __pycache__; cd ../..)