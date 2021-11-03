import psutil


def find_procs_by_name(name):
	"Return a list of processes matching 'name'."
	ls = []
	for p in psutil.process_iter(['name']):
			if p.info['name'] == name:
					ls.append(p)
	return ls

	
process = find_procs_by_name('qterminal')
# process.cmdline()
for p in process:
	print(p.cmdline())