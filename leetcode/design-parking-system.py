# https://leetcode.com/problems/design-parking-system

# Runtime: 153 ms, faster than 74.89% of Python3 online submissions for Design Parking System.
# Memory Usage: 14.4 MB, less than 60.83 % of Python3 online submissions for Design Parking System.
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.spots = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.spots[carType-1] > 0:
            self.spots[carType-1] -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
