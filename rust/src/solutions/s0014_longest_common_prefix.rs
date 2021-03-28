struct Solution;

impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        if strs.is_empty() {
            return String::from("");
        }
        let first = strs[0].as_bytes();
        let mut tmp: Vec<&[u8]> = Vec::new();
        for s in strs.iter() {
            tmp.push(s.as_bytes());
        }
        for i in 0..first.len() {
            for j in 0..tmp.len() {
                if i >= tmp[j].len() || tmp[j][i] != first[i] {
                    return String::from_utf8(first[0..i].to_vec()).unwrap();
                }
            }
        }
        return String::from_utf8(first.to_vec()).unwrap();
    }
}
