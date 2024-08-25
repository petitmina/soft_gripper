class BasePlate:
    def __init__(self, gear_type, input_speed, input_torque):
        self.gear_type = gear_type  # Type of gear, e.g., 'CSGear' or 'MPGear'
        self.input_speed = input_speed  # Input speed for the gear
        self.input_torque = input_torque  # Input torque for the gear

    def calculate_output(self):
        if self.gear_type == 'CSGear':
            output_speed = self.input_speed * 1.5  # Sample calculation
            output_torque = self.input_torque * 0.7  # Sample calculation
        elif self.gear_type == 'MPGear':
            output_speed = self.input_speed * 2.0  # Sample calculation
            output_torque = self.input_torque * 0.5  # Sample calculation
        else:
            output_speed = self.input_speed
            output_torque = self.input_torque
        
        return output_speed, output_torque


class DrivingModule(BasePlate):
    def __init__(self, gear_type, input_speed, input_torque, input_distance, rotation_angle):
        super().__init__(gear_type, input_speed, input_torque)
        self.input_distance = input_distance  # Distance traveled by the module
        self.rotation_angle = rotation_angle  # Rotation angle of the module

    def get_movement(self):
        return f"Speed: {self.input_speed}, Torque: {self.input_torque}, Distance: {self.input_distance}, Rotation: {self.rotation_angle}"


class Actuator(DrivingModule):
    def __init__(self, gear_type, input_speed, input_torque, input_distance, rotation_angle, linear_distance, speed_adjustment):
        super().__init__(gear_type, input_speed, input_torque, input_distance, rotation_angle)
        self.linear_distance = linear_distance  # Linear distance covered by the actuator
        self.speed_adjustment = speed_adjustment  # Speed adjustment of the actuator

    def actuate(self):
        return f"Actuator moves {self.linear_distance} units with speed adjustment: {self.speed_adjustment}"


# Example Usage
base_plate = BasePlate('CSGear', input_speed=100, input_torque=50)
output = base_plate.calculate_output()
print(f"CSGear Output - Speed: {output[0]}, Torque: {output[1]}")

driving_module = DrivingModule('MPGear', input_speed=150, input_torque=35, input_distance=20, rotation_angle=90)
movement = driving_module.get_movement()
print(movement)

actuator = Actuator('CSGear', input_speed=150, input_torque=35, input_distance=20, rotation_angle=90, linear_distance=10, speed_adjustment=1.5)
actuate_result = actuator.actuate()
print(actuate_result)
