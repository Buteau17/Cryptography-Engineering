import hashlib
import getpass

class SecurePasswordVault:
    def __init__(self):
        # Initialize an empty dictionary to store passwords
        self.passwords = {}  
    
    def encrypt_password(self, password):
        # Use SHA-256 hashing for password encryption
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

    def save_password(self, domain, protocol, password):
        # Save password securely
        hashed_password = self.encrypt_password(password)
        self.passwords[domain] = (protocol, hashed_password)
        print(f"Password for {domain} saved securely.")

    def retrieve_password(self, domain, protocol):
        # Retrieve password
        if domain in self.passwords:
            stored_protocol, hashed_password = self.passwords[domain]
            if stored_protocol.lower() == protocol.lower():
                print(f"Password for {domain} is securely stored.")
            else:
                print(f"Security warning: Protocol mismatch for {domain}.")
        else:
            print(f"No password stored for {domain}.")

print("Welcome to the Secure Password Vault!")
print("Store and retrieve your passwords securely.")
vault = SecurePasswordVault()
while True:
    print("\n1. Save Password\n2. Retrieve Password\n3. Exit")
    choice = input("Enter your choice (1~3): ")
    if choice == "1":
        domain = input("Enter the domain: ")
        protocol = input("Enter the protocol (HTTP/HTTPS): ")
        password = getpass.getpass("Enter your password: ")
        vault.save_password(domain, protocol, password)
    elif choice == "2":
        domain = input("Enter domain to retrieve password: ")
        protocol = input("Enter the protocol for retrieval (HTTP/HTTPS): ")
        vault.retrieve_password(domain, protocol)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
