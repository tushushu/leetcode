pub struct Solution {}

impl Solution {
    pub fn reverse(x: i32) -> i32 {
        let mut x: i32 = x;
        let mut result: i32 = 0;
        while x != 0 {
            if let Some(k) = result.checked_mul(10) {
                result = k;
            } else {
                return 0;
            }
            if let Some(k) = result.checked_add(x % 10) {
                result = k;
            } else {
                return 0;
            };
            x /= 10;
        }
        result
    }
}
