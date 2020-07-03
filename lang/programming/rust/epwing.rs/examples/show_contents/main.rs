extern crate epwing;

use epwing::ToPlaintext;
use epwing::subbook::Location;

pub fn main() {
    let book_path = match std::env::args_os().nth(1) {
        Some(path) => path.into(),
        None => panic!("No path given")
    };

    let book = epwing::Book::open(book_path).unwrap();

    println!("Subbooks:");
    for (i, subbook) in book.subbooks().iter().enumerate() {
        println!("  {}: {}", i+1, subbook.title);
    }

    println!("");

    let spine = book.subbooks().first().unwrap();
    println!("Title page ({}) for {}:", spine.index_page, spine.title);

    let mut subbook = book.open_subbook(spine).unwrap();
    let title_text = subbook.read_text(Location::page(spine.index_page as u32)).unwrap();
    println!("{}", title_text.to_plaintext());
}
