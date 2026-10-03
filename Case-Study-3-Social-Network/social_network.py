# Social Network using Adjacency Matrix

users = ["Alice", "Bob", "Charlie", "David"]

n = len(users)

# Create an n x n adjacency matrix
matrix = [[0 for _ in range(n)] for _ in range(n)]


def add_friendship(user1, user2):
    i = users.index(user1)
    j = users.index(user2)

    matrix[i][j] = 1
    matrix[j][i] = 1

    print(f"{user1} and {user2} are now friends.")


def remove_friendship(user1, user2):
    i = users.index(user1)
    j = users.index(user2)

    matrix[i][j] = 0
    matrix[j][i] = 0

    print(f"Friendship between {user1} and {user2} removed.")


def check_friendship(user1, user2):
    i = users.index(user1)
    j = users.index(user2)

    if matrix[i][j] == 1:
        print(f"{user1} and {user2} are friends.")
    else:
        print(f"{user1} and {user2} are not friends.")


def display_matrix():
    print("\n===== FRIENDSHIP MATRIX =====")

    print(f"{'User':<10}", end="")
    for user in users:
        print(f"{user:<10}", end="")
    print()

    for i in range(n):
        print(f"{users[i]:<10}", end="")

        for j in range(n):
            print(f"{matrix[i][j]:<10}", end="")

        print()


def display_friends(user):
    index = users.index(user)

    print(f"\nFriends of {user}:")

    found = False

    for j in range(n):
        if matrix[index][j] == 1:
            print("-", users[j])
            found = True

    if not found:
        print("No friends found.")


# Add friendships
add_friendship("Alice", "Bob")
add_friendship("Alice", "Charlie")
add_friendship("Bob", "David")
add_friendship("Charlie", "David")

# Display current matrix
display_matrix()

# Check friendships
print()
check_friendship("Alice", "Bob")
check_friendship("Alice", "David")

# Display Alice's friends
display_friends("Alice")

# Remove friendship
print()
remove_friendship("Alice", "Bob")

# Display updated matrix
display_matrix()
