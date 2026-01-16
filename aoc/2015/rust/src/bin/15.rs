use nom::{
    IResult, Parser,
    bytes::complete::tag,
    character::{
        complete::{self, line_ending},
        streaming::alpha1,
    },
    combinator::map,
    multi::separated_list1,
    sequence::{delimited, preceded},
};

advent_of_code::solution!(15);

#[derive(Debug)]
// An iterator over all combinations of an integer vector of length n with the sum all n elements
// adding up to k
pub struct Compositions {
    n: usize,
    k: i32,
    cur: Vec<i32>,
    done: bool,
}

impl Compositions {
    pub fn new(n: usize, k: i32) -> Self {
        let mut cur = vec![0; n];
        cur[n - 1] = k;
        Self {
            n,
            k,
            cur,
            done: false,
        }
    }
}

impl Iterator for Compositions {
    type Item = Vec<i32>;

    fn next(&mut self) -> Option<Self::Item> {
        if self.done {
            return None;
        }
        let result = self.cur.clone();
        for i in (0..self.n - 1).rev() {
            if self.cur[i] < self.k {
                self.cur[i] += 1;

                let used: i32 = self.cur[..=i].iter().sum();
                if used <= self.k {
                    for j in i + 1..self.n - 1 {
                        self.cur[j] = 0;
                    }
                    self.cur[self.n - 1] = self.k - used;
                    return Some(result);
                }
            }
        }
        self.done = true;
        Some(result)
    }
}

#[derive(Debug)]
struct Ingredient<'a> {
    #[allow(dead_code)]
    name: &'a str,
    capacity: i32,
    durability: i32,
    flavor: i32,
    texture: i32,
    calories: i32,
}

fn parser(input: &str) -> IResult<&str, Vec<Ingredient<'_>>> {
    separated_list1(line_ending, ingredient).parse(input)
}

fn ingredient(input: &str) -> IResult<&str, Ingredient<'_>> {
    map(
        (
            alpha1,
            delimited(tag(": capacity "), complete::i32, tag(", ")),
            delimited(tag("durability "), complete::i32, tag(", ")),
            delimited(tag("flavor "), complete::i32, tag(", ")),
            delimited(tag("texture "), complete::i32, tag(", ")),
            preceded(tag("calories "), complete::i32),
        ),
        |(name, capacity, durability, flavor, texture, calories)| Ingredient {
            name,
            capacity,
            durability,
            flavor,
            texture,
            calories,
        },
    )
    .parse(input)
}

fn get_recipe_score(quantities: &[i32], ingredients: &[Ingredient]) -> u64 {
    let n = quantities.len();
    let capacity = 0.max(
        (0..n)
            .map(|i| quantities[i] * ingredients[i].capacity)
            .sum(),
    ) as u64;
    let durability = 0.max(
        (0..n)
            .map(|i| quantities[i] * ingredients[i].durability)
            .sum(),
    ) as u64;
    let flavor = 0.max((0..n).map(|i| quantities[i] * ingredients[i].flavor).sum()) as u64;
    let texture = 0.max((0..n).map(|i| quantities[i] * ingredients[i].texture).sum()) as u64;
    capacity * durability * flavor * texture
}

fn calories(quantities: &[i32], ingredients: &[Ingredient]) -> i32 {
    (0..quantities.len())
        .map(|i| quantities[i] * ingredients[i].calories)
        .sum()
}

const GRAMS: i32 = 100;

pub fn part_one(input: &str) -> Option<u64> {
    let (_, ingredients) = parser.parse(input.trim()).expect("a good parse");
    Compositions::new(ingredients.len(), GRAMS)
        .map(|quantities| get_recipe_score(&quantities, &ingredients))
        .max()
}

pub fn part_two(input: &str) -> Option<u64> {
    let (_, ingredients) = parser.parse(input.trim()).expect("a good parse");
    Compositions::new(ingredients.len(), GRAMS)
        .filter(|quantities| calories(quantities, &ingredients) == 500)
        .map(|quantities| get_recipe_score(&quantities, &ingredients))
        .max()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(62842880));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(57600000));
    }
}
