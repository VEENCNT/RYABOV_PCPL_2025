use std::env;
use std::io;

fn get_coefficient(args: &Vec<String>, index: usize, name: &str) -> f64 {
    match args.get(index) {
        Some(coefficient_string) => {
            match coefficient_string.parse::<f64>() {
                Ok(coefficient) => return coefficient,
                Err(_) => {}
            }
        },
        None => {}
    }

    loop {
        let mut coefficient_string = String::new();

        println!("Введите коэффициент {}: ", name);
        match io::stdin().read_line(&mut coefficient_string) {
            Ok(_) => {},
            Err(error) => println!("Ошибка: {}", error)
        }

        match coefficient_string.trim().parse::<f64>() {
            Ok(coefficient) => return coefficient,
            Err(_) => println!("Введите действительное число!")
        }
    }
}

fn get_roots(a: f64, b: f64, c: f64) -> Vec<f64> {
    let mut roots: Vec<f64> = Vec::new();

    let discriminant: f64 = b * b - 4.0 * a * c;
    
    if discriminant == 0.0 {
        let root = -b / (2.0 * a);

        if root >= 0.0 {
            let squared_root = root.sqrt();

            roots.push(squared_root);
            roots.push(-1.0 * squared_root);
        }
    } else if discriminant > 0.0 {
        let squared_discriminant: f64 = discriminant.sqrt();

        let first_root = (-b - squared_discriminant) / (2.0 * a); 
        let second_root = (-b + squared_discriminant) / (2.0 * a); 

        if first_root >= 0.0 {
            let squared_first_root = first_root.sqrt();
            
            roots.push(squared_first_root);
            roots.push(-1.0 * squared_first_root);
        }

        if second_root >= 0.0 {
            let squared_second_root = second_root.sqrt();
            
            roots.push(squared_second_root);
            roots.push(-1.0 * squared_second_root);
        }
    }

    roots.sort_by(f64::total_cmp);

    roots.dedup();

    return roots;
}

fn main() {
    let args: Vec<_> = env::args().collect();

    let a: f64 = get_coefficient(&args, 1, "A");
    let b: f64 = get_coefficient(&args, 2, "B");
    let c: f64 = get_coefficient(&args, 3, "C");

    let roots = get_roots(a, b, c);

    let roots_amount: usize = roots.len();

    match roots_amount {
        0 => println!("Нет корней"),
        1 => println!("Корень уравнения: {}", roots[0]),
        _ => {
            println!("Корни уравнения: ");

            for i in roots {
                print!("{} ", i);
            }

            println!("");
        }
    }
}
