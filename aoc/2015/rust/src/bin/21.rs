advent_of_code::solution!(21);

#[derive(Debug)]
enum ItemType {
    Weapon,
    Armor,
    Ring,
}

struct Item {
    #[allow(dead_code)]
    it: ItemType,
    cost: u64,
    damage: u64,
    armor: u64,
}

impl Item {
    fn weapon(cost: u64, damage: u64) -> Item {
        Self {
            it: ItemType::Weapon,
            cost,
            damage,
            armor: 0,
        }
    }

    fn armor(cost: u64, armor: u64) -> Item {
        Self {
            it: ItemType::Armor,
            cost,
            damage: 0,
            armor,
        }
    }

    fn ring(cost: u64, damage: u64, armor: u64) -> Item {
        Self {
            it: ItemType::Ring,
            cost,
            damage,
            armor,
        }
    }
}

type Inventory = (Vec<Item>, Vec<Item>, Vec<Item>);

fn get_inventory() -> Inventory {
    (
        vec![
            Item::weapon(8, 4),
            Item::weapon(10, 5),
            Item::weapon(25, 6),
            Item::weapon(40, 7),
            Item::weapon(74, 8),
        ],
        vec![
            Item::armor(0, 0), // Simulate no armor
            Item::armor(13, 1),
            Item::armor(31, 2),
            Item::armor(53, 3),
            Item::armor(75, 4),
            Item::armor(102, 5),
        ],
        vec![
            Item::ring(0, 0, 0),
            Item::ring(0, 0, 0), // Simulate 0-2 rings
            Item::ring(25, 1, 0),
            Item::ring(50, 2, 0),
            Item::ring(100, 3, 0),
            Item::ring(20, 0, 1),
            Item::ring(40, 0, 2),
            Item::ring(80, 0, 3),
        ],
    )
}

// Play a full game. True player wins false enemy wins
fn play(damage: u64, armor: u64) -> bool {
    let (player_hit_points, enemy_hit_points) = (100, 104);
    let player_attack = 1i64.max(damage as i64 - 1) as u64;
    let enemy_attack = 1i64.max(8 - armor as i64) as u64;
    let (mut player_damage, mut enemy_damage) = (0, 0);
    loop {
        // Player attacks
        enemy_damage += player_attack;
        if enemy_damage >= enemy_hit_points {
            return true;
        }
        player_damage += enemy_attack;
        if player_damage >= player_hit_points {
            return false;
        }
    }
}

// Part 1: 78 (1.2µs @ 10000 samples)
pub fn part_one(_input: &str) -> Option<u64> {
    let mut min_gold = u64::MAX;
    let (weapons, armors, rings) = get_inventory();
    let mut gold;
    for weapon in weapons.iter() {
        for armor in armors.iter() {
            for (idx, ring_1) in rings.iter().enumerate() {
                for ring_2 in rings[idx + 1..].iter() {
                    gold = weapon.cost + armor.cost + ring_1.cost + ring_2.cost;
                    if gold >= min_gold {
                        continue;
                    }
                    if play(
                        weapon.damage + ring_1.damage + ring_2.damage,
                        armor.armor + ring_1.armor + ring_2.armor,
                    ) {
                        min_gold = min_gold.min(gold);
                    }
                }
            }
        }
    }
    Some(min_gold)
}

// Part 2: 148 (2.6µs @ 10000 samples)
pub fn part_two(_input: &str) -> Option<u64> {
    let mut max_gold = u64::MIN;
    let (weapons, armors, rings) = get_inventory();
    let mut gold;
    for weapon in weapons.iter() {
        for armor in armors.iter() {
            for (idx, ring_1) in rings.iter().enumerate() {
                for ring_2 in rings[idx + 1..].iter() {
                    gold = weapon.cost + armor.cost + ring_1.cost + ring_2.cost;
                    if gold <= max_gold {
                        continue;
                    }
                    if !play(
                        weapon.damage + ring_1.damage + ring_2.damage,
                        armor.armor + ring_1.armor + ring_2.armor,
                    ) {
                        max_gold = max_gold.max(gold);
                    }
                }
            }
        }
    }
    Some(max_gold)
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case()]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(78));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(148));
    }
}
