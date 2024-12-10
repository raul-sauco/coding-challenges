advent_of_code::solution!(9);

use std::collections::BTreeSet;

use itertools::Itertools;

#[derive(Debug)]
struct FileMetadata {
    length: usize,
    start_idx: usize,
}

struct Disk {
    content: Vec<usize>,
    files: Vec<FileMetadata>,
    empty_blocks: Vec<BTreeSet<usize>>,
}

impl Disk {
    fn from_str(input: &str) -> Self {
        let mut content = Vec::<usize>::new();
        let mut empty_blocks = vec![BTreeSet::new(); 10];
        let mut files = vec![];
        for (id, (file_bytes, empty_bytes)) in input.chars().chain(Some('.')).tuples().enumerate() {
            if let Some(bytes) = file_bytes.to_digit(10) {
                files.push(FileMetadata {
                    length: bytes as usize,
                    start_idx: content.len(),
                });
                for _ in 0..bytes {
                    content.push(id);
                }
            }
            // It will not push the extra '.' character
            if let Some(bytes) = empty_bytes.to_digit(10) {
                if bytes == 0 {
                    continue;
                }
                // Push to the empty blocks of size byte a block starting at the current idx.
                empty_blocks[bytes as usize].insert(content.len());
                for _ in 0..bytes {
                    content.push(usize::MAX);
                }
            }
        }
        Disk {
            content,
            files,
            empty_blocks,
        }
    }

    fn compact(&mut self) {
        let (mut left, mut right) = (0, self.content.len() - 1);
        while left < right {
            while self.content[right] == usize::MAX {
                right -= 1;
            }
            while self.content[left] != usize::MAX {
                left += 1;
            }
            if left >= right {
                break;
            }
            self.content.swap(left, right);
            left += 1;
            right -= 1;
        }
    }

    fn compact_2(&mut self) {
        while let Some(file) = self.files.pop() {
            if let Some((block_start_idx, block_length)) =
                self.get_block(file.length, file.start_idx)
            {
                // The block has been popped
                let (mut read, mut write) = (file.start_idx, block_start_idx);
                for _ in 0..file.length {
                    self.content.swap(read, write);
                    read += 1;
                    write += 1;
                }
                let remaining_empty_bytes = block_length - file.length;
                if remaining_empty_bytes > 0 {
                    self.empty_blocks[remaining_empty_bytes].insert(block_start_idx + file.length);
                }
            }
        }
    }

    /// Get the start index of the furthest left block with at least the given length.
    fn get_block(&mut self, length: usize, file_start_idx: usize) -> Option<(usize, usize)> {
        // Iterate over the lengths that we can use.
        for idx in length..10 {
            if let Some(start_idx) = self.empty_blocks[idx].pop_first() {
                if start_idx + idx < file_start_idx {
                    return Some((start_idx, idx));
                }
            }
        }
        None
    }

    fn get_checksum(&self) -> u64 {
        self.content
            .iter()
            .enumerate()
            .map(|(idx, &x)| if x == usize::MAX { 0 } else { idx * x })
            .sum::<usize>() as _
    }
}

pub fn part_one(input: &str) -> Option<u64> {
    let mut disk = Disk::from_str(input);
    disk.compact();
    Some(disk.get_checksum())
}

// TODO: Complete this part
pub fn part_two(input: &str) -> Option<u64> {
    let mut disk = Disk::from_str(input);
    disk.compact_2();
    Some(disk.get_checksum())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(1928));
    }

    #[test]
    fn test_part_two() {
        assert_eq!(
            part_two(&advent_of_code::template::read_file("examples", DAY)),
            Some(2858)
        );
        assert_eq!(
            part_two(&advent_of_code::template::read_file("inputs", DAY)),
            Some(6389911791746)
        );
    }
}
