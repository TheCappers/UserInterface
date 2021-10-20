from recorders.recorded_data import RecordedData
import subprocess as s
from time import sleep
import threading as t
from datetime import datetime, timedelta

class SytemsCallRecorder(RecordedData):
	def __init__(self, ):
		RecordedData.__init__(self)
		self.__autorecording = True
		self._systemcall_data = self.get_recorded_data()
		self.reset_entrydata()
		self.willRecord = False
		self.syscall_thread = t.Thread()


	def startRecord(self):
		while self.__autorecording:
			now = datetime.now()
			start_formatted = (now+timedelta(seconds=-1)).strftime("%m/%d/%Y %H:%M:%S")
			end_formatted = now.strftime("%m/%d/%Y %H:%M:%S")
			cmd = "sudo ausearch -ts " + start_formatted + " -te " + end_formatted + " -i -m SYSCALL"
			output = s.Popen(cmd, shell=True, stdout=s.PIPE, stderr=s.PIPE)
			for line in output.stdout.readlines():
				# print(line)
				self.reset_entrydata()
				curline = line.decode().split()
				if curline[0] == 'type=SYSCALL':
					self.sysCallHandler(curline)
					self.insert_to_db(self._systemcall_data)
			sleep(1)


	def systemcallrecorder_start(self):
		self.syscall_thread = t.Thread(target=self.startRecord)
		print("==== SYSTEM CALL RECORDING STARTING =====")
		if not self.__autorecording:
			self.__autorecording = True
		s.Popen('sudo service auditd start', shell=True, stdout=s.PIPE, stderr=s.PIPE)
		self.syscall_thread.start()


	def systemcallrecorder_end(self):
		print("==== SYSTEM CALL RECORDING ENDING =====")
		# s.Popen('sudo service auditd stop', shell=True, stdout=s.PIPE, stderr=s.PIPE)
		# self.willRecord = False
		self.__autorecording = False
		# self.syscall_thread.join()

	def reset_entrydata(self):
		self._systemcall_data['name'] = "System_Call"
		self._systemcall_data['data']['systemcall_name'] = ''
		self._systemcall_data['data']['systemcall_argument'] = []
		self._systemcall_data['data']['systemcall_returnval'] = ''
		self._systemcall_data['data']['systemcall_calltype'] = ''


	def sysCallHandler(self, curline):
		for segment in curline:
			parts = segment.split('=')
			if parts[0] == 'exit':
				self._systemcall_data['data']['systemcall_returnval'] = parts[1]
			elif parts[0] == 'a0' or parts[0] == 'a1' or parts[0] == 'a2' or parts[0] == 'a3':
				self._systemcall_data['data']['systemcall_argument'].append(parts[1])
			elif parts[0] == 'syscall':
				self._systemcall_data['data']['systemcall_name'] = parts[1]
				self._systemcall_data['data']['systemcall_calltype'] = self.systemcalltypeIdentifier(parts[1]) #identify type


	def systemcalltypeIdentifier(self, systemcall):
		if systemcall in ['fork', 'exit', 'wait']:
			return 'Process Control'
		elif systemcall in ['open', 'read', 'write', 'close']:
			return 'File Management'
		elif systemcall in ['ioctl', 'read', 'write']:
			return 'Device Mnagement'
		elif systemcall in ['getpid', 'alarm', 'sleep']:
			return 'Information Maintenance'
		elif systemcall in ['pipe', 'shmget', 'mmap']:
			return 'Communication'

