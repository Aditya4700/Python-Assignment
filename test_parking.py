import ParkingLot
import Vehicle

def test_create_parking_lot():
    parkinglot = ParkingLot.ParkingLot()
    assert parkinglot.create_parking_lot(5) == 5
    assert parkinglot.create_parking_lot(0) == 0

def test_park():
    parkinglot = ParkingLot.ParkingLot()
    assert parkinglot.create_parking_lot(2) == 2
    assert parkinglot.park("1234", "White") == 1
    assert parkinglot.park("9999", "Black") == 2
    assert parkinglot.park("1111", "Red") == -1

def test_leave_slot():
    parkinglot = ParkingLot.ParkingLot()
    assert parkinglot.create_parking_lot(2) == 2
    assert parkinglot.park("1234", "White") == 1
    assert parkinglot.park("9999", "Black") == 2
    assert parkinglot.leave_slot(1) == True
    assert parkinglot.leave_slot(1) == False



def test_check_status():
    parkinglot = ParkingLot.ParkingLot()
    assert parkinglot.create_parking_lot(2) == 2
    assert parkinglot.park("1234", "White") == 1
    assert parkinglot.park("9999", "Black") == 2
    assert parkinglot.check_status() == "Slot No \tRegistration No \tColor\n1\t1234\tWhite\n2\t9999\tBlack"


def test_get_regno_from_color():
    parkinglot = ParkingLot.ParkingLot()
    assert parkinglot.create_parking_lot(3) == 3
    assert parkinglot.park("1234", "White") == 1
    assert parkinglot.park("9999", "Black") == 2
    assert parkinglot.park("7777", "White") == 3
    assert parkinglot.get_regno_from_color("White") == ["1234", "7777"]

def test_get_slotno_from_regno():
    parkinglot = ParkingLot.ParkingLot()
    assert parkinglot.create_parking_lot(3) == 3
    assert parkinglot.park("1234", "White") == 1
    assert parkinglot.park("9999", "Black") == 2
    assert parkinglot.park("7777", "White") == 3
    assert parkinglot.get_slotno_from_regno("1234") == 1
    assert parkinglot.get_slotno_from_regno("8888") == -1

def test_get_slotno_from_color():
    parkinglot = ParkingLot.ParkingLot()
    assert parkinglot.create_parking_lot(3) == 3
    assert parkinglot.park("1234", "White") == 1
    assert parkinglot.park("9999", "Black") == 2
    assert parkinglot.park("9229", "red") == 3
    assert parkinglot.get_slotno_from_color("White")==['1']
    assert parkinglot.get_slotno_from_color("red")==['3']
    