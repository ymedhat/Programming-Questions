# design an elevator system
# 3 elevators 
# 10 floors
import time

class Elevator:
	floors = range(10)
	
	def __init__(floor, moving=False):
		self.floor = floor
		self.moving = moving

	def change_floor(floor):
		diff_floors = abs(current_floor-floor)
		current_milli_time = lambda: int(round(time.time() * 1000))

		while current_milli_time != (current_milli_time+(diff_floors*1000)):
			self.moving = True

		self.floor=floor
		self.moving = False

class Building(Elevator):
	elev_1 = Elevator(floors[0])
	elev_2 = Elevator(floors[0])
	elev_3 = Elevator(floors[len(floors)/2])

	# takes floor which called the elevator
	def call_elevator(floor):
		elevator = free_elevator(floor)
		elevator.change_floor(floor)
		return_to_origin()

	# returns free elevator, closest to required floor
	def free_elevator(floor):
		el1 = check_elevator(floor, elev_1)
		el2 = check_elevator(floor, elev_2)
		el3 = check_elevator(floor, elev_3)
		el_list = {el1:elev_1, el2:elev_2, el3:elev_3}
		elevator = min(el_list.keys())
		return el_list[elevator]

	# returns the value of the difference between the floor
	# required and the current floor the elevator is at
	def check_elevator(floor, elevator):
		if elevator.moving == False:
			return abs(floor - self.floor)
		return False

	# returns the elevators to original floors
	def return_to_origin():
		elvtr_list = [elev_1, elev_2, elev_3]
		if check_moving(elvtr_list):
			for elvtr in elvtr_list:
				if elvtr is elev_3:
					elvtr.change_floor(floors[len(floors)/2])
				elvtr.change_floor(floors[0])

	# Checks if the elevator arguement is moving
	def check_moving(elevators):
		elvtr_flag = True
		for elvtr in elevators:
			if elvtr.moving:
				elvtr_flag = False
				break
		return elvtr_flag
