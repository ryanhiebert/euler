fn main() {
    let mut sum = 0;
    let (mut i, mut j) = (1, 1);
    while j < 4000000 {
        let k = i + j;
        i = j;
        j = k;
        if i % 2 == 0 {
            sum += i;
        }
    }
    println!("{}", sum);
}
