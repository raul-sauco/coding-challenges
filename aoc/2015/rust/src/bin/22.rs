use std::{cmp::Reverse, collections::BinaryHeap};

use nom::{
    IResult, Parser,
    bytes::complete::tag,
    character::complete::{self, line_ending},
    combinator::map,
};
use rustc_hash::FxHashSet;

advent_of_code::solution!(22);

#[derive(Debug, PartialEq, Eq, PartialOrd, Ord, Hash, Clone, Copy)]
struct State {
    player_hp: i16,
    player_mana: i16,
    boss_hp: i16,
    shield: u8,
    poison: u8,
    recharge: u8,
}

impl State {
    // Apply and decrease the timer for active states, return true if the boss is dead
    fn apply_effects(&mut self) -> bool {
        if self.shield > 0 {
            self.shield -= 1;
        }
        if self.poison > 0 {
            self.poison -= 1;
            self.boss_hp -= 3;
        }
        if self.recharge > 0 {
            self.recharge -= 1;
            self.player_mana += 101;
        }
        self.boss_hp <= 0
    }

    // Returns true if the player can keep playing, still has some hp and has enough mana to cast
    // some spell, We use the result to determine whether to use or discard the next state.
    fn boss_turn(&mut self, damage: i16) -> bool {
        let armor = if self.shield > 0 { 7 } else { 0 };
        self.player_hp -= 1.max(damage - armor);
        // The player has no hp or ability to cast any more spells
        self.player_hp > 0 && self.player_mana >= 53
    }
}

#[derive(Debug)]
struct Boss {
    hp: i16,
    damage: i16,
}

fn parser(input: &str) -> IResult<&str, Boss> {
    map(
        (
            tag("Hit Points: "),
            complete::i16,
            line_ending,
            tag("Damage: "),
            complete::i16,
        ),
        |(_, hp, _, _, damage)| Boss { hp, damage },
    )
    .parse(input)
}

fn play(boss: Boss, hard_mode: bool) -> i16 {
    let initial = State {
        player_hp: 50,
        player_mana: 500,
        boss_hp: boss.hp,
        shield: 0,
        poison: 0,
        recharge: 0,
    };
    let mut pq = BinaryHeap::new();
    let mut seen = FxHashSet::default();
    pq.push((Reverse(0i16), initial));
    seen.insert(initial);
    while let Some((Reverse(mana_spent), mut state)) = pq.pop() {
        // Hard mode deduction
        if hard_mode {
            state.player_hp -= 1;
            if state.player_hp <= 0 {
                continue;
            }
        }

        // Check at the beginning of the turn as well
        if state.apply_effects() {
            return mana_spent;
        }

        // Magic Missile
        if state.player_mana >= 53 {
            let mut next = State {
                boss_hp: state.boss_hp - 4,
                player_mana: state.player_mana - 53,
                ..state
            };
            if next.apply_effects() {
                return 53 + mana_spent;
            }
            if next.boss_turn(boss.damage) && !seen.contains(&next) {
                pq.push((Reverse(53 + mana_spent), next));
                seen.insert(next);
            }
        }

        // Drain
        if state.player_mana >= 73 {
            let mut next = State {
                boss_hp: state.boss_hp - 2,
                player_hp: state.player_hp + 2,
                ..state
            };
            if next.apply_effects() {
                return 73 + mana_spent;
            }
            if next.boss_turn(boss.damage) && !seen.contains(&next) {
                pq.push((Reverse(73 + mana_spent), next));
                seen.insert(next);
            }
        }

        // Shield
        if state.player_mana >= 113 && state.shield == 0 {
            let mut next = State {
                player_mana: state.player_mana - 113,
                shield: 6,
                ..state
            };
            if next.apply_effects() {
                return 113 + mana_spent;
            }
            if next.boss_turn(boss.damage) && !seen.contains(&next) {
                pq.push((Reverse(113 + mana_spent), next));
                seen.insert(next);
            }
        }

        // Poison
        if state.player_mana >= 173 && state.poison == 0 {
            let mut next = State {
                player_mana: state.player_mana - 173,
                poison: 6,
                ..state
            };
            if next.apply_effects() {
                return 173 + mana_spent;
            }
            if next.boss_turn(boss.damage) && !seen.contains(&next) {
                pq.push((Reverse(173 + mana_spent), next));
                seen.insert(next);
            }
        }

        // Recharge
        if state.player_mana >= 229 && state.recharge == 0 {
            let mut next = State {
                player_mana: state.player_mana - 229,
                recharge: 5,
                ..state
            };
            if next.apply_effects() {
                return 229 + mana_spent;
            }
            if next.boss_turn(boss.damage) && !seen.contains(&next) {
                pq.push((Reverse(229 + mana_spent), next));
                seen.insert(next);
            }
        }
    }
    unreachable!("Dijkstra should always find a winning state")
}

// Part 1: 1824 (582.4µs @ 1503 samples)
pub fn part_one(input: &str) -> Option<u64> {
    let (_, boss) = parser.parse(input).expect("a good parse");
    Some(play(boss, false) as u64)
}

// Part 2: 1937 (149.0µs @ 3656 samples)
pub fn part_two(input: &str) -> Option<u64> {
    let (_, boss) = parser.parse(input).expect("a good parse");
    Some(play(boss, true) as u64)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, None);
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, None);
    }
}
