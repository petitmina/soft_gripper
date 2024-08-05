# class SoftGripper:
# 	def __init__(self, max_value, min_value,value):
# 		self.min_value = 0
# 		self.max_value = 360
# 		self.value = 0
# 	def grip(self, value):
# 		self.value = value


class SoftGripper:
    def __init__(self, max_pressure, min_pressure, current_pressure):
        self.max_pressure = max_pressure  # 최대 압력 값
        self.min_pressure = min_pressure  # 최소 압력 값
        self.current_pressure = current_pressure  # 현재 압력 값
        self.gripper_initialized = False
        self.blower_started = False
        self.air_injected = False
        self.object_detected = False

    def initialize_gripper(self):
        self.gripper_initialized = True
        print("Gripper Initialized (그리퍼 초기화)")

    def start_blower(self):
        if self.gripper_initialized:
            self.blower_started = True
            print("Blower Started (송풍기 가동)")
        else:
            print("Initialize Gripper first (그리퍼를 먼저 초기화하세요)")

    def inject_air(self):
        if self.blower_started:
            self.air_injected = True
            print("Air Injected (공기 주입)")
        else:
            print("Start Blower first (송풍기를 먼저 가동하세요)")

    def detect_object(self, method="direct"):
        if self.air_injected:
            if method == "direct":
                print("Object Detected using Direct Detection (직접 탐지)")
            elif method == "vision":
                print("Object Detected using Webcam with Computer Vision (웹캠 및 컴퓨터 비전)")
            else:
                print("Invalid detection method (잘못된 탐지 방법)")
            self.object_detected = True
        else:
            print("Inject Air first (공기를 먼저 주입하세요)")

    def pick_object(self):
        if self.object_detected:
            print("Object Picked (물체 집기)")
        else:
            print("Detect Object first (물체를 먼저 탐지하세요)")

    def end_process(self):
        print("Process Ended or Terminated (종료)")
        # Reset all states
        self.gripper_initialized = False
        self.blower_started = False
        self.air_injected = False
        self.object_detected = False

    def actuate_pressure(self, pressure_change):
        """
        지정 값만큼 공압 액추에이터를 작동시킵니다.
        pressure_change : 작동시킬 압력 변화량
        """
        new_pressure = self.current_pressure + pressure_change
        if self.min_pressure <= new_pressure <= self.max_pressure:
            self.current_pressure = new_pressure
            print(f"Actuator adjusted to {self.current_pressure} units of pressure (공압 액추에이터가 {self.current_pressure} 단위의 압력으로 조정됨)")
        else:
            print(f"Pressure out of range! (압력이 범위를 벗어남) Current Pressure: {self.current_pressure}")

    def reset_to_initial_pressure(self):
        """
        공압 액추에이터를 초기 설정값으로 복원합니다.
        """
        self.current_pressure = self.min_pressure
        print(f"Pressure reset to initial value: {self.current_pressure} units (압력이 초기 설정값으로 복원됨: {self.current_pressure} 단위)")


# Usage example
gripper = SoftGripper()
gripper.initialize_gripper()
gripper.start_blower()
gripper.inject_air()
gripper.detect_object(method="direct")  # or method="vision"
gripper.pick_object()
gripper.end_process()
