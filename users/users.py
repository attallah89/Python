class User:
    def __init__(self, first_name, last_name, email, age, is_rewards_member=False, gold_card_points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")

    def enroll(self):
        if self.is_rewards_member:
            print("User  already a member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True

    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print("Insufficient points to spend.")
            return False
        else:
            self.gold_card_points -= amount
            return True


# Create a user instance and call the display_info method to test
user1 = User("John", "Doe", "john.doe@example.com", 30)
user1.display_info()

# Test the enroll method
user1.enroll()

# Create two more instances of the User class
user2 = User("Jane", "Smith", "jane.smith@example.com", 25)
user3 = User("Alice", "Johnson", "alice.johnson@example.com", 28)

# User1 spends 50 points
user1.spend_points(50)

# User2 enrolls
user2.enroll()

# User2 tries to spend 80 points
user2.spend_points(80)


user1.display_info()
user2.display_info()
user3.display_info()


user1.enroll()

user3.spend_points(40)