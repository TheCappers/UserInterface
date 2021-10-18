from os import system
from typing import Match
from recorders.recorded_data import RecordedData
import subprocess as s
from time import sleep
import threading as t
from datetime import datetime, timedelta
from Database.Database import DataBase

class SytemsCallRecorder(RecordedData, t.Thread):
		def __init__(self, ):
			RecordedData.__init__(self)
			t.Thread.__init__(self)
			self.reset_entrydata()
			self.willRecord = False
			self.isAutoRecord = False # get this value from config class
			# self.setRecorder()
			# self.initRecorder()


		def setRecorder(self, bool_record):
			if bool_record:
				print("==== SYSTEM CALL RECORDIN STARTING =====")
				self.willRecord = True
				s.Popen('service auditd start', shell=True, stdout=s.PIPE, stderr=s.PIPE)
			else:
				print("==== SYSTEM CALL RECORDIN ENDING =====")
				s.Popen('service auditd stop', shell=True, stdout=s.PIPE, stderr=s.PIPE)
				self.willRecord = False


		def run(self):
			print("just run")
			while True:
				i = 0
				while self.willRecord:
					print(i)
					now = datetime.now()
					start_formatted = (now+timedelta(seconds=-1)).strftime("%m/%d/%Y %H:%M:%S")
					end_formatted = now.strftime("%m/%d/%Y %H:%M:%S")
					# cmd = "sudo ausearch -ts " + start_formatted + " -te " + end_formatted + " -i"
					cmd = "sudo ausearch -ts " + start_formatted + " -te " + end_formatted + " -i -m SYSCALL"
					print(cmd)
					output = s.Popen(cmd, shell=True, stdout=s.PIPE, stderr=s.PIPE)
					# print(output.stderr)
					print(cmd)
					for line in output.stdout.readlines():
						print(line)
						self.reset_entrydata()
						curline = line.decode().split()
						# print(curline)
						if curline[0] == 'type=SYSCALL':
							self.sysCallHandler(curline)
							print(self._systemcall_data)
							self.insert_to_db(self._systemcall_data)
					sleep(1)
					i += 1


		def reset_entrydata(self):
			self._systemcall_data = self.get_recorded_data()
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
			# print(curline)

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