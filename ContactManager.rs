use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use std::fs::{self, File};
use std::io::{self, Write, Read};
use std::path::Path;

// Define the Contact struct with the necessary fields
#[derive(Serialize, Deserialize, Debug)]
struct Contact {
    name: String,
    mobile: Option<String>,
    home: Option<String>,
    email: Option<String>,
    address: Option<String>,
}

impl Contact {
    fn to_dict(&self) -> HashMap<String, Option<String>> {
        let mut map = HashMap::new();
        map.insert("name".to_string(), Some(self.name.clone()));
        map.insert("mobile_number".to_string(), self.mobile.clone());
        map.insert("home_number".to_string(), self.home.clone());
        map.insert("email".to_string(), self.email.clone());
        map.insert("address".to_string(), self.address.clone());
        map
    }
}

// Define the ContactManager struct to manage contacts
struct ContactManager {
    contacts: Vec<Contact>,
}

impl ContactManager {
    fn new() -> Self {
        ContactManager { contacts: Vec::new() }
    }

    fn add_contact(&mut self, contact: Contact) {
        self.contacts.push(contact);
    }

    fn remove_contact(&mut self, name: &str) {
        self.contacts.retain(|contact| contact.name != name);
    }

    fn update_contact(&mut self, name: &str, new_contact: Contact) {
        if let Some(contact) = self.contacts.iter_mut().find(|c| c.name == name) {
            *contact = new_contact;
        }
    }

    fn get_contact(&self, name: &str) -> Option<&Contact> {
        self.contacts.iter().find(|contact| contact.name == name)
    }

    fn list_contacts(&self) -> &Vec<Contact> {
        &self.contacts
    }
}

// Define a struct for handling data operations
struct Data;

impl Data {
    fn save_data(file_path: &str, data: &HashMap<String, Vec<Contact>>) -> io::Result<()> {
        let file = File::create(file_path)?;
        serde_json::to_writer_pretty(file, data).map_err(|e| io::Error::new(io::ErrorKind::Other, e))
    }

    fn load_data(file_path: &str) -> io::Result<HashMap<String, Vec<Contact>>> {
        if Path::new(file_path).exists() {
            let mut file = File::open(file_path)?;
            let mut contents = String::new();
            file.read_to_string(&mut contents)?;
            let data: HashMap<String, Vec<Contact>> = serde_json::from_str(&contents)?;
            Ok(data)
        } else {
            Ok(HashMap::new())
        }
    }

    fn delete_file(file_path: &str) -> io::Result<()> {
        if Path::new(file_path).exists() {
            fs::remove_file(file_path)?;
        }
        Ok(())
    }
}

fn main() {
    let mut contact_manager = ContactManager::new();
    let data_file = "contacts.json";

    // Load existing contacts
    let contacts_data = Data::load_data(data_file).unwrap_or_else(|_| HashMap::new());
    for contact_info in contacts_data.get("contacts").unwrap_or(&vec![]) {
        contact_manager.add_contact(contact_info.clone());
    }

    loop {
        println!("\n1. Add Contact");
        println!("2. Remove Contact");
        println!("3. Update Contact");
        println!("4. List Contacts");
        println!("5. Save and Exit");
        let mut choice = String::new();
        io::stdin().read_line(&mut choice).expect("Failed to read line");

        match choice.trim() {
            "1" => {
                let mut name = String::new();
                let mut mobile = String::new();
                let mut home = String::new();
                let mut email = String::new();
                let mut address = String::new();

                println!("Enter name: ");
                io::stdin().read_line(&mut name).expect("Failed to read line");
                println!("Enter mobile number: ");
                io::stdin().read_line(&mut mobile).expect("Failed to read line");
                println!("Enter home number: ");
                io::stdin().read_line(&mut home).expect("Failed to read line");
                println!("Enter email: ");
                io::stdin().read_line(&mut email).expect("Failed to read line");
                println!("Enter address: ");
                io::stdin().read_line(&mut address).expect("Failed to read line");

                let contact = Contact {
                    name: name.trim().to_string(),
                    mobile: if mobile.trim().is_empty() { None } else { Some(mobile.trim().to_string()) },
                    home: if home.trim().is_empty() { None } else { Some(home.trim().to_string()) },
                    email: if email.trim().is_empty() { None } else { Some(email.trim().to_string()) },
                    address: if address.trim().is_empty() { None } else { Some(address.trim().to_string()) },
                };
                contact_manager.add_contact(contact);
                println!("Contact added.");
            }
            "2" => {
                let mut name = String::new();
                println!("Enter name of contact to remove: ");
                io::stdin().read_line(&mut name).expect("Failed to read line");
                contact_manager.remove_contact(name.trim());
                println!("Contact removed.");
            }
            "3" => {
                let mut name = String::new();
                println!("Enter name of contact to update: ");
                io::stdin().read_line(&mut name).expect("Failed to read line");
                if let Some(contact) = contact_manager.get_contact(name.trim()) {
                    let mut new_mobile = String::new();
                    let mut new_home = String::new();
                    let mut new_email = String::new();
                    let mut new_address = String::new();

                    println!("Enter new mobile number (current: {}): ", contact.mobile.as_deref().unwrap_or("N/A"));
                    io::stdin().read_line(&mut new_mobile).expect("Failed to read line");
                    println!("Enter new home number (current: {}): ", contact.home.as_deref().unwrap_or("N/A"));
                    io::stdin().read_line(&mut new_home).expect("Failed to read line");
                    println!("Enter new email (current: {}): ", contact.email.as_deref().unwrap_or("N/A"));
                    io::stdin().read_line(&mut new_email).expect("Failed to read line");
                    println!("Enter new address (current: {}): ", contact.address.as_deref().unwrap_or("N/A"));
                    io::stdin().read_line(&mut new_address).expect("Failed to read line");

                    let updated_contact = Contact {
                        name: contact.name.clone(),
                        mobile: if new_mobile.trim().is_empty() { contact.mobile.clone() } else { Some(new_mobile.trim().to_string()) },
                        home: if new_home.trim().is_empty() { contact.home.clone() } else { Some(new_home.trim().to_string()) },
                        email: if new_email.trim().is_empty() { contact.email.clone() } else { Some(new_email.trim().to_string()) },
                        address: if new_address.trim().is_empty() { contact.address.clone() } else { Some(new_address.trim().to_string()) },
                    };
                    contact_manager.update_contact(&contact.name, updated_contact);
                    println!("Contact updated.");
                } else {
                    println!("Contact not found.");
                }
            }
            "4" => {
                for contact in contact_manager.list_contacts() {
                    println!(
                        "Name: {}, Mobile: {:?}, Home: {:?}, Email: {:?}, Address: {:?}",
                        contact.name,
                        contact.mobile,
                        contact.home,
                        contact.email,
                        contact.address
                    );
                }
            }
            "5" => {
                // Save contacts to file
                let contacts_data = HashMap::from([("contacts".to_string(), contact_manager.list_contacts().clone())]);
                if let Err(e) = Data::save_data(data_file, &contacts_data) {
                    eprintln!("Error saving data: {}", e);
                } else {
                    println!("Data saved. Exiting...");
                }
                break;
            }
            _ => println!("Invalid choice. Please try again."),
        }
    }
}
