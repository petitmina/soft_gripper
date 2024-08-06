# class SoftGripper:
# 	def __init__(self, max_value, min_value,value):
# 		self.min_value = 0
# 		self.max_value = 360
# 		self.value = 0
# 	def grip(self, value):
# 		self.value = value

import time

class SoftGripper:
    def __init__(self, max_pressure, min_pressure, current_pressure, tolerance=3, release_speed=1):
        self.max_pressure = max_pressure  # 최대 압력 값
        self.min_pressure = min_pressure  # 최소 압력 값
        self.current_pressure = current_pressure  # 현재 압력 값
        self.tolerance = tolerance  # 압력 허용 오차
        self.release_speed = release_speed  # 공기 배출 속도 (KPa/s)
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

    def release_object(self):
            """
            물건을 놓을 때 공기를 배출하여 그리퍼를 해제하는 함수
            천천히 공기가 빠지도록 설정
            """
            self.release_pressure_slowly()
            print("Object Released (물건이 놓임)")

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

    def release_pressure_slowly(self):
            """
            조절 밸브를 사용하여 천천히 공기가 빠지도록 설정하는 함수
            """
            while self.current_pressure > self.min_pressure:
                self.current_pressure -= self.release_speed
                if self.current_pressure < self.min_pressure:
                    self.current_pressure = self.min_pressure
                print(f"Releasing pressure slowly: {self.current_pressure} KPa (압력을 천천히 배출 중)")
                time.sleep(1)  # 속도 조절을 위한 대기 시간 (1초에 release_speed만큼 감소)


gripper = SoftGripper(max_pressure=100, min_pressure=0, current_pressure=50, tolerance=4, release_speed=5)
gripper.initialize_gripper()
gripper.start_blower()
gripper.inject_air()
gripper.set_pressure(70)  # 목표 압력을 70 KPa로 설정
# gripper.detect_object(method="direct")  # or method="vision"
gripper.detect_object(method="vision")  # method="direct"로도 가능
gripper.pick_object()
gripper.release_object()  # 물건을 놓을 때 천천히 공기 배출
gripper.reset_to_initial_pressure()  # 초기 설정값으로 복원
gripper.end_process()
