# 🎄 Advent of Code 2015

<img src="./.assets/christmas_ferris.png" width="164" alt="ferris">

Solutions for [Advent of Code](https://adventofcode.com/) in [Rust](https://www.rust-lang.org/).

<!--- advent_readme_stars table --->

<!--- benchmarking table --->

## Benchmarks

|            Day            |  Part 1   |  Part 2   |
| :-----------------------: | :-------: | :-------: |
| [Day 1](./src/bin/01.rs)  |  `4.9µs`  |  `1.4µs`  |
| [Day 2](./src/bin/02.rs)  | `21.0µs`  | `22.2µs`  |
| [Day 3](./src/bin/03.rs)  | `111.3µs` | `122.0µs` |
| [Day 4](./src/bin/04.rs)  | `49.9ms`  | `132.2ms` |
| [Day 5](./src/bin/05.rs)  | `109.1µs` | `856.9µs` |
| [Day 6](./src/bin/06.rs)  |  `5.1ms`  |  `7.2ms`  |
| [Day 7](./src/bin/07.rs)  | `66.5µs`  | `70.1µs`  |
| [Day 8](./src/bin/08.rs)  |  `2.8ms`  |  `2.9ms`  |
| [Day 9](./src/bin/09.rs)  | `59.3µs`  |  `1.4ms`  |
| [Day 10](./src/bin/10.rs) | `11.3ms`  | `161.9ms` |
| [Day 11](./src/bin/11.rs) |  `6.5ms`  | `23.1ms`  |
| [Day 12](./src/bin/12.rs) | `304.4µs` | `314.0µs` |
| [Day 13](./src/bin/13.rs) |  `2.6ms`  | `25.6ms`  |
| [Day 14](./src/bin/14.rs) | `482.0ns` | `17.0µs`  |
| [Day 15](./src/bin/15.rs) |  `3.3ms`  |  `2.7ms`  |
| [Day 16](./src/bin/16.rs) | `78.4µs`  | `82.2µs`  |
| [Day 17](./src/bin/17.rs) | `196.0µs` | `442.5µs` |
| [Day 18](./src/bin/18.rs) |  `7.6ms`  |  `7.8ms`  |
| [Day 19](./src/bin/19.rs) | `59.5µs`  | `57.5µs`  |
| [Day 20](./src/bin/20.rs) |  `7.8ms`  |  `3.6ms`  |
| [Day 21](./src/bin/21.rs) |  `1.2µs`  |  `2.6µs`  |
| [Day 22](./src/bin/22.rs) | `582.4µs` | `149.0µs` |
| [Day 23](./src/bin/23.rs) |    `-`    |    `-`    |
| [Day 24](./src/bin/24.rs) |    `-`    |    `-`    |
| [Day 25](./src/bin/25.rs) |    `-`    |    `-`    |

**Total: 469.03ms**

<!--- benchmarking table --->

## Comments

I found a greedy _O(mn)_ solution where m is the length of the molecule and n
is the number of replacements. The trick is to start with the final molecule
and replace backwards, trying always the longest replacements first, until we
get to the _initial_ **e** molecule.

This works because the replacements form a restricted grammar where **e**
only appears on the left hand side, and all the replacements increase the
molecule size.

> TODO: Have a look at a better solution I found on the thread
>
> No need to simulate at all.
>
> Observation
>
> Given the specific grammar of the replacements in the puzzle, the molecule
> language is almost a context-free grammar, and the minimum number of steps
> can be computed with a formula.
>
> The key facts:
>
> Rn and Ar act like parentheses
>
> Y acts like a comma
>
> Every replacement increases “structure”
>
> Reducing back to e is equivalent to counting structure
>
> The formula
> Let: elements = number of element tokens (capital letter + optional lowercase)
> rn = count of "Rn"
> ar = count of "Ar"
> y = count of "Y"
>
> steps = elements - rn - ar - 2\*y - 1

### Day 20 - Part 1

First idea was binary search but wouldn't work because the number of presents
received does not increment linearly with the number of houses.

Then I tried brute force starting with a vector of 1 million elements, the
plan was to increase the size if needed but it turned out to work and be close
to the minimum size needed.

I also considered using the factors of the number, since these would be the
elves, but didn't look into it after the brute force worked.

### Day 20 - Part 2

Similar just limit each elf to 50 houses.

### Day 22

Hard simulation, lots of details to keep track of, hard to understand what
happens when given the description, I tried a couple of times and didn't get
the right answer, then had a look at this repo and used to fix my solution:

[Maneatingape repo](https://github.com/maneatingape/advent-of-code-rust/blob/main/src/year2015/day22.rs)
