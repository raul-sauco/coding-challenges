// 1396. Design Underground System
// 🟠 Medium
//
// https://leetcode.com/problems/design-underground-system/
//
// Tags: Hash Table - Design - String

use std::collections::HashMap;

struct UndergroundSystem {
    travelers: HashMap<i32, (String, i32)>,
    times: HashMap<(String, String), (f64, usize)>,
}

/// Use two hashmaps, one to store travelers in transit information, it will
/// save an entry when a traveler starts a trip with the traveler's id as the
/// key and the station and time as the value. When a traveler checks out, it
/// will use all the data to compute the travel time and insert it into the
/// times hashmap under the (start_st, end_st) key, if the key already exists
/// in the hashmap, it will update the values. When we need to get the average,
/// we access the times hashmap and use the total traveled time and number of
/// trips to get and return it.
///
/// Time complexity: O(1) - Each call to any of the methods is processed in
/// constant time.
/// Space complexity: O(n) - We could have as many entries in the travelers
/// hashmap as calls to the check_in method, but most likely that number will
/// remain low, as entries are removed by calls to the checkout method. The
/// number of entries in the times hashmap could be equal to the number of
/// total trips, if every combination of in_station and out_station was unique.
///
/// Runtime 34 ms Beats 92.86%
/// Memory 17.1 MB Beats 100%
impl UndergroundSystem {
    fn new() -> Self {
        UndergroundSystem {
            travelers: HashMap::new(),
            times: HashMap::new(),
        }
    }

    fn check_in(&mut self, id: i32, station_name: String, t: i32) {
        self.travelers.insert(id, (station_name, t));
    }

    fn check_out(&mut self, id: i32, station_name: String, t: i32) {
        match self.travelers.remove(&id) {
            Some((in_st, in_tm)) => {
                let travel_time = (t - in_tm) as f64;
                let src_station = in_st.to_owned();
                self.times
                    .entry((src_station, station_name))
                    .and_modify(|(total_travel_time, count)| {
                        *total_travel_time += travel_time;
                        *count += 1;
                    })
                    .or_insert((travel_time, 1));
            }
            None => unreachable!(),
        }
    }

    fn get_average_time(&self, start_station: String, end_station: String) -> f64 {
        match self.times.get(&(start_station, end_station)) {
            Some(e) => e.0 / e.1 as f64,
            None => unreachable!(),
        }
    }
}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * let obj = UndergroundSystem::new();
 * obj.check_in(id, stationName, t);
 * obj.check_out(id, stationName, t);
 * let ret_3: f64 = obj.get_average_time(startStation, endStation);
 */

/**
 * Your MyHashSet object will be instantiated and called as such:
 * let obj = MyHashSet::new();
 * obj.add(key);
 * obj.remove(key);
 * let ret_3: bool = obj.contains(key);
 */
fn main() {
    let mut us = UndergroundSystem::new();
    us.check_in(10, String::from("Leyton"), 3);
    us.check_out(10, String::from("Paradise"), 8);
    assert_eq!(
        us.get_average_time(String::from("Leyton"), String::from("Paradise")),
        5.0
    );
    us.check_in(5, String::from("Leyton"), 10);
    us.check_out(5, String::from("Paradise"), 16);
    assert_eq!(
        us.get_average_time(String::from("Leyton"), String::from("Paradise")),
        5.5
    );
    us.check_in(2, String::from("Leyton"), 21);
    us.check_out(2, String::from("Paradise"), 30);
    assert!(
        us.get_average_time(String::from("Leyton"), String::from("Paradise")) - (20.0 / 3.0)
            < 0.00001
    );
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
