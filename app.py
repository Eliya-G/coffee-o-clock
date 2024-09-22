try:
	import Tkinter
except:
	import tkinter as Tkinter
	
from tkinter import *
from tkinter import messagebox
import math	# Required For Coordinates Calculation
import time	# Required For Time Handling



class main(Tkinter.Tk):
	def __init__(self):
		Tkinter.Tk.__init__(self)
		self.title("Coffee O'Clock")
		self.resizable(width=False, height=False)
		self.x=190	# Center Point x
		self.y=130	# Center Point
		self.length=50	# Stick Length
		self.creating_all_function_trigger()
		self.time_at_opening = time.localtime()
		self.main_time_object = time.localtime()

		self.previous_dd_entry = None
		self.previous_caffeine_amount = None

		# Regular Mode
		self.reg_digital_clock = Label(self, text=self.format_top_time(self.main_time_object),  font=("Arial", 25), bd=2, relief=SUNKEN)
		h24 = int(time.strftime( "%H", self.time_at_opening ))
		main_timedelta = 24 - h24
		self.info_box1 = Label(self, text="The info below asumes you are healthy, and the avarage person.\n It also assumes you are going to drink a cup of coffee right now;\n and it's your first cup (8oz) of coffee today.\n Containing 90mg of caffeine in the cup.", bd=1, relief=SUNKEN, pady=10)
		self.info_box2 = Label(self, text=f"You would have {round(self.coffee_half_life(bedtime=main_timedelta), 1)}mg of caffeine in your blood if you went to bed at 12AM.\nIt's as if you had drank {round(int(self.coffee_half_life(bedtime=main_timedelta) / 90 * 100), 0)}% of a cup of coffee before you went to bed.")
		self.custom_flip_button = Button(self, text="Custom Mode", command=self.regular_or_custom_mode, fg="blue")

		# Custom Mode
		self.custom_digital_clock = Label(self, text=self.format_top_time(self.main_time_object),  font=("Arial", 25), fg="blue", bd=2, relief=SUNKEN)
		self.custom_box_1 =Label(self, text="Enter the amount of caffeine you'll be ingesting right now.\nmg:", bd=1, relief=SUNKEN)
		self.caffeine_entry = Entry(self, width=40)
		self.custom_box_2 = Label(self, text="Select when you'll be going to bed.")
		self.dd_button_clicked = StringVar()
		self.dd_button_clicked.set( "---" )
		self.custom_dropdown = OptionMenu(self , self.dd_button_clicked, *dropdown_dict.keys(),) 
		self.custom_enter_button = Button(self, text="Enter",command=self.custom_enter)
		self.custom_discription = Label(self, text="")
		self.regular_flip_button = Button(self, text="Regular Mode", command=self.regular_or_custom_mode)


	# Creating Trigger For Other Functions
	def creating_all_function_trigger(self):
		self.create_canvas_for_shapes()
		self.creating_background_()
		self.creating_sticks()
		return

	# Creating Background
	def creating_background_(self):
		self.image=Tkinter.PhotoImage(file='images/clock.gif')
		self.canvas.create_image(190,130, image=self.image) # This moves the image.
		return

	# creating Canvas
	def create_canvas_for_shapes(self):
		self.canvas=Tkinter.Canvas(self)
		self.canvas.grid(row=1, column=0)
		# self.canvas.pack(expand='yes',fill='both')
		return

	# Creating Moving Sticks
	def creating_sticks(self):
		self.sticks=[]
		for i in range(3):
			store=self.canvas.create_line(self.x, self.y,self.x+self.length,self.y+self.length,width=2, fill='red')
			self.sticks.append(store)
		return

	# Function Need Regular Update
	def update_class(self, current_time):
		current_time=self.main_time_object
		t = time.strptime(str(current_time.tm_hour), "%H")
		hour = int(time.strftime( "%I", t ))*5
		current_time=(hour,current_time.tm_min,current_time.tm_sec)
		# Changing Stick Coordinates
		for n,i in enumerate(current_time):
			x,y=self.canvas.coords(self.sticks[n])[0:2]
			cr=[x,y]
			cr.append(self.length*math.cos(math.radians(i*6)-math.radians(90))+self.x)
			cr.append(self.length*math.sin(math.radians(i*6)-math.radians(90))+self.y)
			self.canvas.coords(self.sticks[n], tuple(cr))
		return
	  # *-*-*-*-*-*-*-*-*-*-*-*- End of canvas clock *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

	def format_top_time(self, time_object, current_mode=0):
		if current_mode == 0: # The return value is a string
			formated_time = time.strftime("%I:%M %p", time_object)
			return formated_time 
		
		else: # The return value is a tuple
			formated_hour = int(time.strftime("%I", time_object))

			formated_minutes = time.strftime("%M", time_object)
			formated_minutes = int(formated_minutes) / 60

			formated_AMPM = time.strftime("%p", time_object)
			return (formated_hour + formated_minutes, formated_AMPM)

	def coffee_half_life(self, caffeine_amount=90, bedtime=24): # Bedtime is the time delta of when you're going to sleep
		caffeine_amount = caffeine_amount * 0.5 ** (bedtime / 6)
		return caffeine_amount

	def regular_or_custom_mode(self):
		global iternum
		iternum += 1 
		if iternum % 2 == 0: # Custom mode
			self.reg_digital_clock.grid_forget()
			self.info_box1.grid_forget()
			self.info_box2.grid_forget()
			self.custom_flip_button.grid_forget()
			self.custom_digital_clock.grid(row=0, column=0, sticky=W+E)
			self.custom_box_1.grid(row=2,column=0, sticky=W+E)
			self.caffeine_entry.grid(row=3, column=0)
			self.custom_box_2.grid(row=4,column=0)
			self.custom_dropdown.grid(row=5,column=0)
			self.custom_enter_button.grid(row=6, column=0)
			self.regular_flip_button.grid(row=8, column=0)
		else: # Regular mode
			self.custom_digital_clock.grid_forget()
			self.custom_box_1.grid_forget()
			self.caffeine_entry.grid_forget()
			self.custom_box_2.grid_forget()
			self.custom_dropdown.grid_forget()
			self.custom_enter_button.grid_forget()
			self.regular_flip_button.grid_forget()
			self.custom_discription.grid_forget()
			self.reg_digital_clock.grid(row=0, column=0, sticky=W+E)
			self.info_box1.grid(row=2,column=0, sticky=W+E)
			self.info_box2.grid(row=3,column=0)
			self.custom_flip_button.grid(row=8, column=0)
			self.previous_dd_entry = None
			self.previous_caffeine_amount = None
	
	def time_delta(self):
		current_time = self.format_top_time(self.main_time_object, current_mode=1)
		sleep_time = dropdown_dict[self.dd_button_clicked.get()]

		if current_time[1] == "AM" and sleep_time[1] == "AM":
			if current_time[0] < sleep_time[0]:
				time_delta = sleep_time[0] - current_time[0]
				return time_delta
			else:
				time_delta = 24 - current_time[0] + sleep_time[0]
				return time_delta
			
		if current_time[1] == "PM" and sleep_time[1] == "PM":
			if current_time[0] < sleep_time[0]:
				time_delta = sleep_time[0] - current_time[0]
				return time_delta
			else:
				time_delta = 24 - current_time[0] + sleep_time[0]
				return time_delta

		elif current_time[1] == "PM" and sleep_time[1] == "AM":
			time_delta = 12 - current_time[0] + sleep_time[0]
			return time_delta

		elif current_time[1] == "AM" and sleep_time[1] == "PM":
			time_delta = 12 - current_time[0] + sleep_time[0]
			return time_delta

	def custom_enter(self):
		if self.caffeine_entry.get().isdigit() == False:
			messagebox.showerror("Error", "Enter numbers only")
		else:
			if self.caffeine_entry.get() != self.previous_caffeine_amount or dropdown_dict[self.dd_button_clicked.get()] != self.previous_dd_entry:
				self.custom_discription.grid_forget()
				self.previous_caffeine_amount = self.caffeine_entry.get() 
				self.previous_dd_entry = dropdown_dict[self.dd_button_clicked.get()]

				timedelta_var = self.time_delta()
				self.custom_discription = Label(self, text=f"You would have {round(self.coffee_half_life(caffeine_amount=int(self.caffeine_entry.get()), bedtime=timedelta_var), 1)}mg of caffeine in your blood if you went to bed at {str(dropdown_dict[self.dd_button_clicked.get()][0]) + str(dropdown_dict[self.dd_button_clicked.get()][1])}.\nIt is as if you had drank {round(int(self.coffee_half_life(caffeine_amount=int(self.caffeine_entry.get()),bedtime=timedelta_var) / 90 * 100))}% of a cup of coffee before you went to bed.", bd=1, relief=SUNKEN, pady=10)
				self.custom_discription.grid(row=7, column=0)
			else:
				pass

def handler():
    global run
    run = False
			
dropdown_dict = { 
    "1AM":(1,"AM"), 
    "2AM":(2,"AM"), 
    "3AM":(3,"AM"), 
    "4AM":(4,"AM"), 
    "5AM":(5,"AM"), 
    "6AM":(6,"AM"), 
    "7AM":(7,"AM"), 
    "8AM":(8,"AM"), 
    "9AM":(9,"AM"), 
    "10AM":(10,"AM"), 
    "11AM":(11,"AM"), 
    "12PM":(12,"AM"), 
    "1PM":(1,"PM"), 
    "2PM":(2,"PM"), 
    "3PM":(3,"PM"), 
    "4PM":(4,"PM"), 
    "5PM":(5,"PM"), 
    "6PM":(6,"PM"), 
    "7PM":(7,"PM"), 
    "8PM":(8,"PM"), 
    "9PM":(9,"PM"), 
    "10PM":(10,"PM"), 
    "11PM":(11,"PM"), 
    "12AM":(12,"PM"), 
} 
		
# Main Function Trigger
root=main()
iternum = 0
root.regular_or_custom_mode()

root.protocol("WM_DELETE_WINDOW", handler)
run = True

# Main loop
while run:
	root.main_time_object = time.localtime()
	root.update()
	root.update_idletasks()
	root.update_class(root.main_time_object)
	time.sleep(0.1)

root.destroy()
