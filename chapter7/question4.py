"""
駐車場
- 入れる車の総量を持つ
- 車を受け入れることができる
  - 受け入れ可能な総数を超えていればエラー
- 車を出すことができる
  - 車が駐車中でなければエラー

車
- 所在地を持つ
- 駐車場に停めることができる
- 駐車場から出ることができる
"""


class CarIsAlreadyParkingError(Exception):
    pass


class CarisNotParkingError(Exception):
    pass


class ParkingLotIsFullError(Exception):
    pass


class CarIsNotParkingError(Exception):
    pass


class ParkingLot:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.parking_cars = {}

    @property
    def can_park(self):
        return len(self.cars) > self.capacity

    def exist_parking_car(self, car: "Car"):
        return id(car) in self.parking_cars

    def accept_car(self, car: "Car"):
        if not self.can_park:
            raise ParkingLotIsFullError("This parking lot is full!!!")
        self.parking_cars[id(car)] = True
        return True

    def exit_car(self, car: "Car"):
        if not self.exist_parking_car(car):
            raise CarIsNotParkingError("This car is not paking in the parking lot.")
        self.parking_cars.pop(id(car))


class Car:
    def __init__(self):
        self.parking_lot = None

    @property
    def is_parking(self):
        return bool(self.parking_lot)

    def park(self, parking_lot: ParkingLot):
        if self.parking:
            return CarIsAlreadyParkingError("This car is already parking.")

        try:
            parking_lot.accept_car(self)
        except ParkingLotIsFullError as e:
            raise e

        self.location = parking_lot

    def exit_patking_lot(self):
        if not self.is_parking:
            raise CarIsNotParkingError

        try:
            self.location.exit_car(self)
        except CarIsNotParkingError as e:
            raise e

        self.location = None


class Test