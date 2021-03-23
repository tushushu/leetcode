struct Solution;

impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let mut num = 0;
        let mut res = 0;
        let mut last = 0;
        for c in s.chars() {
            num = match c {
                'I' => 1,
                'V' => 5,
                'X' => 10,
                'L' => 50,
                'C' => 100,
                'D' => 500,
                'M' => 1000,
                _ => 0,
            };
            if last < num {
                res -= last;
            } else {
                res += last;
            }
            last = num;
        }
        res += num;
        res
    }
}
