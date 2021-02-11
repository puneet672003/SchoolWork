import pickle
import platform
import os
from colorama import Fore, init

class StudentDb(): 
	def __init__(self, file_location): 
		self.file_location = file_location

	def __initialize(self):

		class_data = {}
		for std in self.standards: 
			for sec in self.sections: 
				class_name = f"{std} {sec}"
				class_data[class_name] = []

		with open(self.file_location, "wb") as f: 
			data = {
				"students_data": {},
				"groups": {
					"class_based": class_data
				}
			}

			pickle.dump(data, f)

	@property
	def total_students(self): 
		data = self._get_data()
		total = len(data["students_data"].keys())

		return total

	@property
	def standards(self):
		return [1,2,3,4,5,6,7,8,9,10,11,12] 

	@property
	def sections(self): 
		return "a b c d".split()

	def _get_data(self): 
		with open(self.file_location, "rb") as f: 
			try : 
				data = pickle.load(f)
			except : 
				self.__initialize()
				data = self._get_data()

		return data

	def get_student_info(self, admno): 

		student_data = self._get_data()["students_data"]
		student_info = student_data.get(admno)

		return student_info

	def get_group_data(self, type): 

		if type == "class": 

			data = self._get_data()
			class_data = data["groups"]

			return class_data

	def get_all_students(self): 
		data = self._get_data()
		return data["students_data"]

	def insert_new_info(self, admno, name, std, sec, mobile_no): 
		# Checks
		if std not in self.standards: 
			raise Exception("Invalid standard")

		if sec not in self.sections: 
			raise Exception("Invalid section")


		data = self._get_data()
		data["groups"]["class_based"][f"{std} {sec}"].append(admno)

		data["students_data"][admno] = {
			"name": name, 
			"class": {
				"std": std, 
				"sec": sec
			}, 
			"mobile_no": mobile_no
		}

		with open(self.file_location, "wb") as f: 
			pickle.dump(data, f)

	def update_info(self, admno, **kwargs): 
		data = self._get_data()
		student_data = data["students_data"].get(admno)

		if student_data is None: 
			raise Exception("No records for specified admission number")

		else : 
			for key, value in kwargs.items():
				if key in ["name", "admno", "std", "sec", "mobile_no"]: 
					student_data[key] = value
				else : 
					pass

			std = student_data["std"]
			sec = student_data["sec"]
			data["groups"]["class_based"][f"{std} {sec}"].append(admno)

			with open(self.file_location, "wb") as f: 
				pickle.dump(data, f)

	def remove_student(self, admno): 
		data = self._get_data()
		students = data["students_data"]
		info = students.get(admno)
		std, sec = info["class"]["std"], info["class"]["sec"]

		del data["students_data"][admno]
		data["groups"]["class_based"][f"{std} {sec}"].remove(admno)

		with open(self.file_location, "wb") as f: 
				pickle.dump(data, f)

class UI(): 
	def __init__(self): 
		self.db = StudentDb("data.bin")
		init(convert = True)

	def check_and_input(self, message, type): 
		if type == "admno": 
			while True:
				self.cls()
				admno = input("\n" + message)
				try : 
					admno = int(admno)
					if len(str(admno)) > 15: 
						print(f"{Fore.RESET}[ {Fore.RED}-{Fore.RESET} ] Admission number must be less than or equal to 15 digits.")
						self.pause("\nPress enter to try again!!!")
						continue
					break
				except: 
					print(f"{Fore.RESET}[ {Fore.RED}-{Fore.RESET} ] Please enter a valid admission number")
					self.pause("\nPress enter to try again!!!")
			return int(admno)

		elif type == "name": 
			while True:
				self.cls()
				name = input("\n" + message)
				
				if len(name) > 15: 
					print(f"{Fore.RESET}[ {Fore.RED}-{Fore.RESET} ] Name cannot have more than 15 characters!.")
					self.pause("\nPress enter to try again!!!")
					continue 

				break 
			return name

		elif type == "std": 
			while True:
				self.cls()
				std = input("\n" + message)
				try : 
					std = int(std)
					if not std in self.db.standards: 
						print(f"{Fore.RESET}[ {Fore.RED}-{Fore.RESET} ] Please enter a valid standard")
						self.pause("\nPress enter to try again!!!")
						continue
					break
				except: 
					print(f"{Fore.RESET}[ {Fore.RED}-{Fore.RESET} ] Please enter a valid standard")
					self.pause("\nPress enter to try again!!!")
			return int(std)

		elif type == "sec": 
			while True:
				self.cls()
				sec = input("\n" + message)
				
				if sec.lower() not in self.db.sections: 
					print(f"{Fore.RESET}[ {Fore.RED}-{Fore.RESET} ] Please enter a valid section")
					self.pause("\nPress enter to try again!!!")
					continue 

				break 
			return sec
		else: 
			while True:
				self.cls()
				mob = input("\n" + message)
				try : 
					admno = int(mob)
					if len(str(mob)) > 15: 
						print(f"{Fore.RESET}[ {Fore.RED}-{Fore.RESET} ] Mobile number must be less than or equal to 15 digits.")
						self.pause("\nPress enter to try again!!!")
						continue
					break
				except: 
					print(f"{Fore.RESET}[ {Fore.RED}-{Fore.RESET} ] Please enter a valid Mobile number")
					self.pause("\nPress enter to try again!!!")
			return int(mob)
                                    
	def cls(self): 
		if platform.system() == "Linux": 
			os.system("clear")
		elif platform.system() == "Windows": 
			os.system("cls")

	def pause(self, message = "press enter to continue....."): 
		input(f"\n{message}")

	def _print_data(self, adm_numbers): 
		all_data = self.db.get_all_students()
		headings = ["Admission no", "Name", "Class", "Section", "Mobile number"]

		self.cls()
		print("="*(15 * len(headings) + len(headings)))

		for i in headings: 
			print("{:^15}".format(i), end = "|")

		print()
		print("="*(15 * len(headings) + len(headings)))

		for adm_no in adm_numbers:
			student_data = all_data[adm_no]
			data_list = [adm_no, student_data["name"], student_data["class"]["std"], student_data["class"]["sec"], student_data["mobile_no"]]

			for i in data_list:
				print("{:^15}".format(str(i).title()), end = "|")

			print()
		print("="*(15 * len(headings) + len(headings)))


	def print_all(self): 
		all_data = self.db.get_all_students()
		adm_numbers = sorted(all_data.keys())

		self._print_data(adm_numbers)
		
		self.pause("Press enter to return to main menu....")

	def insert_new(self): 
		new_data = []

		for field in "admno name std sec mobile_no".split():
			if field == "admno":
				value = self.check_and_input("Please enter the Admission no. of new student: ", field)
				new_data.append(value)

			elif field == "name": 
				value = self.check_and_input("Please enter the Name of new student: ", field)
				new_data.append(value)
			elif field == "std": 
				value = self.check_and_input("Please enter the Standard of new student: ", field)
				new_data.append(value)
			elif field == "sec": 
				value = self.check_and_input("Please enter the Section of new student: ", field)
				new_data.append(value)
			else: 
				value = self.check_and_input("Please enter the Mobile no. of new student: ", field)
				new_data.append(value)

		self.db.insert_new_info(*new_data)
		print(f"{Fore.RESET}[ {Fore.GREEN}+{Fore.RESET} ] Success!!")
		self.pause()


	def search(self): 
		adm_no = self.check_and_input("Please enter the Admission no. of the student: ", "admno")
		students = self.db.get_all_students()
		
		if adm_no not in students.keys(): 
			print(f"{Fore.RESET}[ {Fore.RED}-{Fore.RESET} ] Admission number don't exist!")
			self.pause("\nPress enter to try again!!!")
		else: 
			self._print_data([adm_no])
			self.pause("Press enter to return to main menu....")

	def print_class(self): 
		class_data = self.db.get_group_data("class")["class_based"]
		std = self.check_and_input("Enter standard : ", "std")
		sec = self.check_and_input("Enter section : ", "sec")

		adm_numbers = class_data.get(f"{std} {sec.lower()}")
		self._print_data(adm_numbers)

		self.pause("Press enter to return to main menu....")

	def remove(self): 
		adm_no = self.check_and_input("Please enter the Admission no. of the student: ", "admno")
		students = self.db.get_all_students()
		
		if adm_no not in students.keys(): 
			print(f"{Fore.RESET}[ {Fore.RED}-{Fore.RESET} ] Admission number don't exist!")
			self.pause("\nPress enter to try again!!!")
		else: 
			self.db.remove_student(adm_no)
			print(f"{Fore.RESET}[ {Fore.GREEN}+{Fore.RESET} ] Success!!")
			self.pause()

	def Main(self): 
		while True:
			self.cls()
			
			menu_logo = """
_____________________________________
    ___  ___ _____ _   _ _   _ 
    |  \/  ||  ___| \ | | | | |
    | .  . || |__ |  \| | | | |
    | |\/| ||  __|| . ` | | | |
    | |  | || |___| |\  | |_| |
    \_|  |_/\____/\_| \_/\___/            
_____________________________________

				"""

			print(Fore.CYAN + menu_logo + Fore.YELLOW)

			print(f"Type {Fore.WHITE}1{Fore.YELLOW} to print all student's detail")
			print(f"Type {Fore.WHITE}2{Fore.YELLOW} to insert new student's details")
			print(f"Type {Fore.WHITE}3{Fore.YELLOW} search for a student by admission no.")
			print(f"Type {Fore.WHITE}4{Fore.YELLOW} to see all students of a spcific class")
			print(f"Type {Fore.WHITE}5{Fore.YELLOW} to remove a student from database")
			print("" + Fore.RESET)

			opt = int(input(":"))

			if opt == 1: 
				self.print_all()

			elif opt == 2: 
				self.insert_new()

			elif opt == 3: 
				self.search()
			
			elif opt == 4: 
				self.print_class()
			
			elif opt == 5: 
				self.remove()

			# elif opt == 6: 
			# 	data = self.db._get_data()
			# 	with open("test.json", "w") as f: 
			# 		json.dump(data, f, indent = 2)

if __name__ == "__main__": 
	window = UI()
	window.Main()
