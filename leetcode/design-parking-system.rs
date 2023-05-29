// 1603. Design Parking System
// 🟢 Easy
//
// https://leetcode.com/problems/design-parking-system/
//
// Tags: Design - Simulation - Counting
struct ParkingSystem {
    availability: [u16; 3],
    occupancy: [u16; 3],
}

/// Keep a record of how many places in total are available and full, when a
/// car tries to park, return true and increase the number of vehicles of the
/// given type by 1 if the parking lot has not reached capacity for the given
/// type. For this problem we could only store the number of available spots,
/// but, if we wanted to update the functionality in the future, for example
/// let cars drive out, it would be useful to know the capacity at any point.
///
/// Time complexity: O(1) - Each call to both the new and add methods takes O(1).
/// Space complexity: O(1) - We store two arrays of 3 u16 each.
///
/// Runtime 12 ms Beats 84.31%
/// Memory 2.6 MB Beats 7.84%
impl ParkingSystem {
    fn new(big: i32, medium: i32, small: i32) -> Self {
        ParkingSystem {
            availability: [big as u16, medium as u16, small as u16],
            occupancy: [0, 0, 0],
        }
    }

    fn add_car(&mut self, car_type: i32) -> bool {
        let index = car_type as usize - 1;
        if self.availability[index] > self.occupancy[index] {
            self.occupancy[index] += 1;
            return true;
        }
        false
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * let obj = ParkingSystem::new(big, medium, small);
 * let ret_1: bool = obj.add_car(carType);
 */

fn main() {
    let mut parking_system = ParkingSystem::new(1, 1, 0);
    assert_eq!(parking_system.add_car(1), true);
    assert_eq!(parking_system.add_car(2), true);
    assert_eq!(parking_system.add_car(3), false);
    assert_eq!(parking_system.add_car(1), false);
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
