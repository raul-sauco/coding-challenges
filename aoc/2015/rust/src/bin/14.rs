use nom::{
    IResult, Parser,
    bytes::complete::tag,
    character::complete::{self, alpha1, line_ending},
    combinator::map,
    multi::separated_list1,
};

advent_of_code::solution!(14);

#[derive(Debug)]
struct Deer {
    speed: u64,
    burst: u64,
    rest: u64,
}

#[derive(Debug)]
struct DeerState {
    deer: Deer,
    points: u64,
    time_left_in_lap: u64,
    status: DeerStatus,
    distance: u64,
}

#[derive(Debug)]
enum DeerStatus {
    Running,
    Resting,
}

fn parser(input: &str) -> IResult<&str, Vec<Deer>> {
    separated_list1(line_ending, deer).parse(input)
}

fn deer(input: &str) -> IResult<&str, Deer> {
    map(
        (
            alpha1,
            tag(" can fly "),
            complete::u64,
            tag(" km/s for "),
            complete::u64,
            tag(" seconds, but then must rest for "),
            complete::u64,
            tag(" seconds."),
        ),
        |(_, _, speed, _, burst, _, rest, _)| Deer { speed, burst, rest },
    )
    .parse(input)
}

fn distance_at_time(deer: &Deer, seconds: u64) -> u64 {
    // Duration and distance in a run/rest cycle
    let (cycle_distance, cycle_duration) = (deer.speed * deer.burst, deer.burst + deer.rest);
    let (complete_cycles, remaining) = (seconds / cycle_duration, seconds % cycle_duration);
    complete_cycles * cycle_distance + deer.speed * remaining.min(deer.burst)
}

fn race(mut deers: Vec<DeerState>, duration: u64) -> u64 {
    let mut lead_deer_distance = 0;
    // Init to 1 to avoid matching the first second
    let mut last_lap_lead = 1;
    let mut max_points = u64::MIN;
    for _ in 0..=duration as usize {
        for deer in deers.iter_mut() {
            if deer.distance == last_lap_lead {
                deer.points += 1;
                if deer.points > max_points {
                    max_points = deer.points;
                }
            }
            deer.time_left_in_lap -= 1;
            match deer.status {
                DeerStatus::Running => {
                    // If running, advance distance gained in one second
                    deer.distance += deer.deer.speed;
                    if deer.distance > lead_deer_distance {
                        lead_deer_distance = deer.distance;
                    }
                    if deer.time_left_in_lap == 0 {
                        deer.status = DeerStatus::Resting;
                        deer.time_left_in_lap = deer.deer.rest;
                    }
                }
                DeerStatus::Resting => {
                    if deer.time_left_in_lap == 0 {
                        deer.status = DeerStatus::Running;
                        deer.time_left_in_lap = deer.deer.burst;
                    }
                }
            }
        }
        last_lap_lead = lead_deer_distance;
    }
    max_points
}

// Part 1: 2655 (482.0ns @ 10000 samples)
pub fn part_one(input: &str) -> Option<u64> {
    let (_, deers) = parser.parse(input).expect("a good parse");
    deers.iter().map(|deer| distance_at_time(deer, 2503)).max()
}

// Part 2: 1059 (17.0µs @ 10000 samples)
pub fn part_two(input: &str) -> Option<u64> {
    let (_, deers) = parser.parse(input).expect("a good parse");
    Some(race(
        deers
            .into_iter()
            .map(|deer| DeerState {
                points: 0,
                time_left_in_lap: deer.burst,
                status: DeerStatus::Running,
                distance: 0,
                deer,
            })
            .collect(),
        2503,
    ))
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(2660));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(1564));
    }
}
