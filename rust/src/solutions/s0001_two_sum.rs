use std::collections::HashMap;

pub struct Solution {}

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map: HashMap<i32, usize> = HashMap::with_capacity(nums.len());
        for (index, num) in nums.iter().enumerate() {
            if let Some(val) = map.get(&num) {
                return vec![*val as i32, index as i32];
            }
            map.insert(target - num, index);
        }
        vec![]
    }
}
