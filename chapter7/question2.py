from typing import List
import unittest
from enum import IntEnum, auto


class CallerBusyError(Exception):
    pass


class Call:
    def __init__(self, call_from: "Caller", call_to: "Caller"):
        self.call_from = call_from

        try:
            self.call_to = self.connect(target=call_to)
        except CallerBusyError as e:
            self.connecting = False
            raise e
        else:
            self.connecting = True

    def connect(self, target: "Caller"):
        return target.answer_the_phone(call=self)

    def send_message(self, speaker: "Caller", message: str):
        print(f"{speaker.name}: {message}")

    def disconnect(self):
        for caller in (self.call_from, self.call_to):
            caller.disconnect()
        self.connecting = False


class Caller:
    def __init__(self, name: str):
        self.name = name
        self.call_in = None

    @property
    def on_the_phone(self):
        return bool(self.call_in)

    def call(self, call_to: "Caller"):
        self.call_in = Call(call_from=self, call_to=call_to)

    def answer_the_phone(self, call: Call):
        if self.on_the_phone:
            raise CallerBusyError()
        self.call_in = call
        return self

    def end_call(self):
        self.call_in.disconnect()

    def disconnect(self):
        self.call_in = None

    def talk(self, message: str):
        self.call_in.send_message(speaker=self, message=message)


class TestCall(unittest.TestCase):
    def test_it(self):
        nancy = Caller("Nancy")
        bob = Caller("Bob")

        nancy.call(call_to=bob)

        nancy.talk("Hi, I'm Nancy.")
        bob.talk("Hi, I'm Bob.")

        assert nancy.on_the_phone is True
        assert bob.on_the_phone is True
        assert nancy.call_in == bob.call_in

        call = nancy.call_in
        assert call.connecting is True
        assert call.call_from == nancy
        assert call.call_to == bob

        nancy.end_call()

        assert call.connecting is False
        assert nancy.on_the_phone is False
        assert bob.on_the_phone is False

    def test_is_busy(self):
        nancy = Caller("Nancy")
        bob = Caller("Bob")

        nancy.call(call_to=bob)

        tom = Caller("Tom")

        with self.assertRaises(CallerBusyError):
            tom.call(call_to=nancy)

        assert tom.call_in is None


class Customer(Caller):
    pass


class CallCenter(Caller):
    def __init__(
        self,
        members: List["CallCenterMember"],
        managers: List["CallCenterManager"],
        directors: List["CallCenterDirector"],
    ):
        self.members = members
        self.managers = managers
        self.directors = directors

    def answer_the_phone(self, call):
        return self.dispatch_call(call)

    def dispatch_call(self, call: Call):
        for staff in (self.members, self.managers, self.directors):
            member = self.get_answerable_staff(staff)
            if member:
                return member.answer_the_phone(call)

        raise CallerBusyError()

    def get_answerable_staff(self, staff: List["CallCenterStaff"]):
        return [staff for staff in staff if not staff.on_the_phone][1]


class CallCenterRole(IntEnum):
    MEMBER = auto()
    MANAGER = auto()
    DIRECTOR = auto()


class CallCenterStaffMixin:
    role: CallCenterRole


class CallCenterStaff(Caller, CallCenterStaffMixin):
    pass


class CallCenterMember(CallCenterStaff):
    role = CallCenterRole.MEMBER


class CallCenterManager(CallCenterStaff):
    role = CallCenterRole.MANAGER


class CallCenterDirector(CallCenterStaff):
    role = CallCenterRole.DIRECTOR


class TestCallCenter(unittest.TestCase):
    def test_it(self):
        member = CallCenterMember("member")
        manager = CallCenterManager("manager")
        director = CallCenterDirector("director")

        call_center = CallCenter(
            members=[member], managers=[manager], directors=[director]
        )

        customers = [Customer(f"customer{n}" for n in range(3))]

        customers[0].call(call_to=call_center)

        call = customers[0].call_in
        assert call.call_from == customers[0]
        assert call.call_to == member

        customers[1].call(call_to=call_center)
        call = customers[1].call_in
        assert call.call_from == customers[1]
        assert call.call_to == manager

        customers[2].call(call_to=call_center)
        call = customers[2].call_in
        assert call.call_from == customers[2]
        assert call.call_to == director


if __name__ == "__main__":
    unittest.main()
