import random

funny_names = ["Bruce Wayne", "Peter Parker", "Tony Stark", "Superman", "Spiderman", "Wolverine", "Deadpool", "Iron Man", "Captain America",
            "Hulk", "Black Widow", "Thor", "Groot", "Aquaman", "Star Lord", "Wanda", "Black Panther", "Doctor Strange", "Ant-Man", "Daredevil",
            "Iron Fist", "Captain Marvel", "Natasha Romanoff", "Vision", "Hawkeye", "Gamora", "Samantha Carter", "Bucky Barnes", "Thor Ragnarok",
            "Steve Rogers", "Scarlet Witch", "Groot", "Winter Soldier"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez",
            "Lopez", "Wilson", "Castillo", "Sanchez", "Jackson", "Lee", "Perez", "Torres", "Martinez", "Robinson", "Walker", "Reynolds",
            "Perez", "Hill", "Flores", "Gomez", "Nguyen", "Chavez", "White", "Adams", "Baker", "Hall", "Ramirez", "Lewis", "Robinson",
            "Johnson", "Mitchell"]
for i in range(20):
    first_name = random.choice(funny_names)
    last_name = random.choice(last_names)
    print("{} {}".format(first_name, last_name))