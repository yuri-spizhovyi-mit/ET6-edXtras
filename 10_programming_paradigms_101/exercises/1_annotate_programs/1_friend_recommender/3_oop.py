#!/usr/bin/env python3


class SocialNetwork:
    def __init__(self):
        self.users = {}
        self.recommendations = {}

    def create_user_database(self):
        self.users = {
            1: {
                "name": "Alice",
                "interests": ["music", "travel", "photography"],
                "friends": [2, 3],
            },
            2: {
                "name": "Bob",
                "interests": ["music", "sports", "coding"],
                "friends": [1, 4],
            },
            3: {
                "name": "Charlie",
                "interests": ["travel", "cooking", "art"],
                "friends": [1, 5],
            },
            4: {
                "name": "David",
                "interests": ["sports", "coding", "gaming"],
                "friends": [2, 5],
            },
            5: {
                "name": "Eve",
                "interests": ["art", "travel", "music"],
                "friends": [3, 4],
            },
        }

    def find_potential_friends(self, user_id, top_n=2):
        user_data = self.users[user_id]
        potential_friends = []

        for other_id, other_data in self.users.items():
            if other_id == user_id or other_id in user_data["friends"]:
                continue

            # Calculate interest similarity
            shared_interests = set(user_data["interests"]) & set(
                other_data["interests"]
            )
            similarity_score = len(shared_interests)

            potential_friends.append(
                {
                    "user_id": other_id,
                    "name": other_data["name"],
                    "similarity_score": similarity_score,
                    "shared_interests": list(shared_interests),
                }
            )

        # Sort potential friends by similarity score
        return sorted(
            potential_friends, key=lambda x: x["similarity_score"], reverse=True
        )[:top_n]

    def generate_recommendations(self):
        for user_id in self.users:
            self.recommendations[user_id] = self.find_potential_friends(user_id)

    def print_recommendations(self):
        print("Friend Recommendations:")
        for user_id, suggested_friends in self.recommendations.items():
            print(f"\n{self.users[user_id]['name']}'s Recommendations:")
            for friend in suggested_friends:
                print(
                    f"- {friend['name']} (Shared Interests: {', '.join(friend['shared_interests'])})"
                )

    def run(self):
        print("\nSimple Social Network Friend Recommender\n")

        self.create_user_database()
        self.generate_recommendations()
        self.print_recommendations()


# Usage
network = SocialNetwork()
network.run()
