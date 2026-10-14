# Case Study 3: social network using an undirected graph and adjacency matrix

class SocialNetwork:
    def __init__(self, users):
        self.users = list(users)
        self.matrix = [[0 for _ in self.users] for _ in self.users]

    def _index(self, user):
        if user not in self.users:
            raise ValueError(f"Unknown user: {user}")
        return self.users.index(user)

    def add_friendship(self, user1, user2):
        i, j = self._index(user1), self._index(user2)
        if i == j:
            print("A user cannot be their own friend in this demo.")
            return
        self.matrix[i][j] = self.matrix[j][i] = 1

    def remove_friendship(self, user1, user2):
        i, j = self._index(user1), self._index(user2)
        self.matrix[i][j] = self.matrix[j][i] = 0

    def are_friends(self, user1, user2):
        return self.matrix[self._index(user1)][self._index(user2)] == 1

    def display(self):
        print("     " + " ".join(f"{user:>7}" for user in self.users))
        for user, row in zip(self.users, self.matrix):
            print(f"{user:>5} " + " ".join(f"{value:>7}" for value in row))


if __name__ == "__main__":
    network = SocialNetwork(["Asha", "Rahul", "Meera", "Karan"])
    network.add_friendship("Asha", "Rahul")
    network.add_friendship("Asha", "Meera")
    network.add_friendship("Rahul", "Karan")

    print("SOCIAL NETWORK FRIENDSHIP MANAGER")
    print("\nFriendship matrix (1 = friends, 0 = not friends):")
    network.display()
    print("\nAre Asha and Rahul friends?", network.are_friends("Asha", "Rahul"))
    print("Are Meera and Karan friends?", network.are_friends("Meera", "Karan"))

    network.remove_friendship("Asha", "Rahul")
    print("\nAfter removing friendship between Asha and Rahul:")
    print("Are Asha and Rahul friends?", network.are_friends("Asha", "Rahul"))
