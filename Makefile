all: venv
	(python3 main.py)
	(make clean)

clean:
	(rm -rf __pycache__)
	(rm -rf configuration/__pycache__)
	(rm -rf controller/__pycache__)
	(rm -rf Database/__pycache__)
	(rm -rf recorders/__pycache__)
	(rm -rf view/__pycache__)
	(rm -rf view/components/__pycache__)
	(rm -rf view/configuration_tab/__pycache__)
	(rm -rf view/home_tab/__pycache__)
	(rm -rf view/sync_tab/__pycache__)
	(rm -rf view/assets/__pycache__)
	(rm -rf Sync/__pycache__)
	(rm -rf Script/__pycache__)
	(rm -rf recorders/.systemcall_recorder.py.swp)
	(rm -rf .idea)

venv:
	test -d venv || ./run.sh

strongclean: clean
	(rm -rf venv)