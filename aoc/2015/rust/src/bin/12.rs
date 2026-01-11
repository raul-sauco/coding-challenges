use serde_json::Value;

advent_of_code::solution!(12);

fn get_numbers(v: &Value) -> i64 {
    match v {
        Value::Number(number) => number.as_i64().unwrap(),
        Value::Array(arr) => arr.iter().map(get_numbers).sum(),
        Value::Object(obj) => obj.values().map(get_numbers).sum(),
        _ => 0,
    }
}

fn no_red(v: &Value) -> i64 {
    match v {
        Value::Number(number) => number.as_i64().unwrap(),
        Value::Array(arr) => arr.iter().map(no_red).sum(),
        Value::Object(obj) => {
            if obj
                .values()
                .any(|v| matches!(v, Value::String(s) if s == "red"))
            {
                0
            } else {
                obj.values().map(get_numbers).sum()
            }
        }
        _ => 0,
    }
}

// Part 1: 156366 (309.9µs @ 1841 samples)
pub fn part_one(input: &str) -> Option<u64> {
    let json: Value = serde_json::from_str(input).expect("valid json");
    Some(get_numbers(&json) as u64)
}

// Part 2: 96852 (327.5µs @ 2949 samples)
pub fn part_two(input: &str) -> Option<u64> {
    let json: Value = serde_json::from_str(input).expect("valid json");
    Some(no_red(&json) as u64)
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case("[]", 0)]
    #[case("{}", 0)]
    #[case("[1,2,3]", 6)]
    #[case("[[[3]]]", 3)]
    #[case(r#"{"a":{"b":4},"c":-1}"#, 3)]
    fn test_part_one(#[case] input: &str, #[case] expected: u64) {
        assert_eq!(part_one(input).expect("a u64"), expected);
    }

    #[rstest]
    #[case("[1,2,3]", 6)]
    #[case(r#"[1,{"c":"red","b":2},3]"#, 4)]
    #[case(r#"{"d":"red","e":[1,2,3,4],"f":5}"#, 0)]
    #[case(r#"[1,"red",5]"#, 6)]
    fn test_part_two(#[case] input: &str, #[case] expected: u64) {
        assert_eq!(part_two(input).expect("a u64"), expected);
    }
}
