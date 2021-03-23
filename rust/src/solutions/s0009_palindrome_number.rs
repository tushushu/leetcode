pub struct Solution;

impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if x <= 0 {
            0;
        }
        let mut z = x as i64;
        let mut y: i64 = 0;
        while z > 0 {
            y = y * 10 + z % 10;
            z /= 10;
        }
        x as i64 == y
    }
}
