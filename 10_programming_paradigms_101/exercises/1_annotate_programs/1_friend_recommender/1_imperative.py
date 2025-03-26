#!/usr/bin/env python3

print("\nSimple Social Network Friend Recommender\n")

# User data structure: {user_id: {name, interests, friends}}
users = {}

# Hardcoded initial user data
users = {
    1: {'name': 'Alice', 'interests': ['music', 'travel', 'photography'], 'friends': [2, 3]},
    2: {'name': 'Bob', 'interests': ['music', 'sports', 'coding'], 'friends': [1, 4]},
    3: {'name': 'Charlie', 'interests': ['travel', 'cooking', 'art'], 'friends': [1, 5]},
    4: {'name': 'David', 'interests': ['sports', 'coding', 'gaming'], 'friends': [2, 5]},
    5: {'name': 'Eve', 'interests': ['art', 'travel', 'music'], 'friends': [3, 4]}
}

# Recommend friends based on shared interests
recommendations = {}

for user_id, user_data in users.items():
    potential_friends = []
    
    # Find users with shared interests
    for other_id, other_data in users.items():
        if other_id == user_id or other_id in user_data['friends']:
            continue
        
        # Calculate interest similarity
        shared_interests = set(user_data['interests']) & set(other_data['interests'])
        similarity_score = len(shared_interests)
        
        potential_friends.append({
            'user_id': other_id,
            'name': other_data['name'],
            'similarity_score': similarity_score,
            'shared_interests': list(shared_interests)
        })
    
    # Sort potential friends by similarity score
    potential_friends.sort(key=lambda x: x['similarity_score'], reverse=True)
    recommendations[user_id] = potential_friends[:2]

# Print recommendations
print("Friend Recommendations:")
for user_id, suggested_friends in recommendations.items():
    print(f"\n{users[user_id]['name']}'s Recommendations:")
    for friend in suggested_friends:
        print(f"- {friend['name']} (Shared Interests: {', '.join(friend['shared_interests'])})")
