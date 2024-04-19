// 2353. Design a Food Rating System
// 🟠 Medium
//
// https://leetcode.com/problems/design-a-food-rating-system/
//
// Tags: Hash Table - Design - Heap (Priority Queue) - Ordered Set

use std::collections::{BTreeSet, HashMap};

#[derive(Debug)]
struct FoodRatings {
    cf: HashMap<String, BTreeSet<(i32, String)>>,
    fc: HashMap<String, String>,
    fr: HashMap<String, i32>,
}

/// Use a hashmap of cuisines to BTreeSet to be able to both access any element by key and the top
/// element by rating in O(1) To have the BTreeMap sorted by rating we use that, and the food name,
/// as the elements in the BTreeSets.
///
/// Runtime 150 ms Beats 50%
/// Memory 19.73 MB Beats 66.67%
#[allow(dead_code)]
impl FoodRatings {
    /// Time complexity: O(n*log(n)) - We iterate n times, inside the loop we do some O(1) work but
    /// we also insert into the BTreeSets.
    /// Space complexity: O(n) - The three data structures that we use all depend directly in the
    /// size of the input for their size.
    fn new(foods: Vec<String>, cuisines: Vec<String>, ratings: Vec<i32>) -> Self {
        (0..foods.len()).fold(
            Self {
                fc: HashMap::new(),
                cf: HashMap::new(),
                fr: HashMap::new(),
            },
            |mut ob, i| {
                ob.fc.insert(foods[i].clone(), cuisines[i].clone());
                ob.cf
                    .entry(cuisines[i].clone())
                    .and_modify(|s| {
                        s.insert((-ratings[i], foods[i].clone()));
                    })
                    .or_insert(BTreeSet::from([(-ratings[i], foods[i].clone())]));
                ob.fr.insert(foods[i].clone(), ratings[i]);
                ob
            },
        )
    }

    /// Time complexity: O(log(n)) - We delete and insert into one of the BTreeSets.
    fn change_rating(&mut self, food: String, new_rating: i32) {
        let r = -self.fr.get(&food).expect("A valid rating for this food");
        self.cf
            .entry(self.fc.get(&food).unwrap().to_string())
            .and_modify(|s| {
                s.remove(&(r, food.clone()));
                s.insert((-new_rating, food.clone()));
            });
        self.fr.entry(food).and_modify(|e| *e = new_rating);
    }

    /// Time complexity: O(log(n)) - We only access the first element in a BTreeSet
    fn highest_rated(&self, cuisine: String) -> String {
        self.cf
            .get(&cuisine)
            .unwrap()
            // Does not work on LC because an old Rust version.
            //         .first()
            .iter()
            .next()
            .unwrap()
            .1
            .clone()
    }
}

/**
 * Your FoodRatings object will be instantiated and called as such:
 * let obj = FoodRatings::new(foods, cuisines, ratings);
 * obj.change_rating(food, newRating);
 * let ret_2: String = obj.highest_rated(cuisine);
 */

// Tests.
fn main() {
    let fr = (
        vec![
            "tjokfmxg",
            "xmiuwozpmj",
            "uqklk",
            "mnij",
            "iwntdyqxi",
            "cduc",
            "cm",
            "mzwfjk",
        ],
        vec![
            "waxlau", "ldpiabqb", "ldpiabqb", "waxlau", "ldpiabqb", "waxlau", "waxlau", "waxlau",
        ],
        vec![9, 13, 7, 16, 10, 17, 16, 17],
    );
    let mut subject = FoodRatings::new(
        fr.0.into_iter().map(|x| x.to_string()).collect::<Vec<_>>(),
        fr.1.into_iter().map(|x| x.to_string()).collect::<Vec<_>>(),
        fr.2,
    );
    subject.change_rating("tjokfmxg".to_string(), 19);
    assert_eq!(
        subject.highest_rated("waxlau".to_string()),
        "tjokfmxg".to_string()
    );
    subject.change_rating("uqklk".to_string(), 7);
    assert_eq!(
        subject.highest_rated("waxlau".to_string()),
        "tjokfmxg".to_string()
    );
    subject.change_rating("tjokfmxg".to_string(), 14);
    assert_eq!(
        subject.highest_rated("waxlau".to_string()),
        "cduc".to_string()
    );
    assert_eq!(
        subject.highest_rated("waxlau".to_string()),
        "cduc".to_string()
    );
    subject.change_rating("tjokfmxg".to_string(), 4);
    assert_eq!(
        subject.highest_rated("waxlau".to_string()),
        "cduc".to_string()
    );
    subject.change_rating("mnij".to_string(), 18);
    assert_eq!(
        subject.highest_rated("waxlau".to_string()),
        "mnij".to_string()
    );
    println!("\x1b[30;42m✔ All tests passed!\x1b[0m")
}
