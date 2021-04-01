use std::collections::LinkedList;

pub struct Solution;

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack: LinkedList<char> = LinkedList::new();
        for c in s.chars() {
            match c {
                '{' => stack.push_back('}'),
                '[' => stack.push_back(']'),
                '(' => stack.push_back(')'),
                _ => {
                    if let Some(k) = stack.back() {
                        if *k == c {
                            stack.pop_back();
                        } else {
                            return false;
                        }
                    } else {
                        return false;
                    }
                }
            }
        }
        return stack.is_empty();
    }
}
