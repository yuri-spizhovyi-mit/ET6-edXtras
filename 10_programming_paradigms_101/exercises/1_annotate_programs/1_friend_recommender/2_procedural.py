#!/usr/bin/env python3

def create_user_database():
    return {
        1: {'name': 'Alice', 'interests': ['music', 'travel', 'photography'], 'friends': [2, 3]},
        2: {'name': 'Bob', 'interests': ['music', 'sports', 'coding'], 'friends': [1, 4]},
        3: {'name': 'Charlie', 'interests': ['travel', 'cooking', 'art'], 'friends': [1, 5]},
        4: {'name': 'David', 'interests': ['sports', 'coding', 'gaming'], 'friends': [2, 5]},
        5: {'name': 'Eve', 'interests': ['art', 'travel', 'music'], 'friends': [3, 4]}
    }

def find_potential_friends(users, user_id):
    user_data = users[user_id]
    potential_friends = []
    
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
    return sorted(potential_friends, key=lambda x: x['similarity_score'], reverse=True)

def generate_recommendations(users, top_n=2):
    recommendations = {}
    
    for user_id in users:
        potential_friends = find_potential_friends(users, user_id)
        recommendations[user_id] = potential_friends[:top_n]
    
    return recommendations

def print_recommendations(users, recommendations):
    print("Friend Recommendations:")
    for user_id, suggested_friends in recommendations.items():
        print(f"\n{users[user_id]['name']}'s Recommendations:")
        for friend in suggested_friends:
            print(f"- {friend['name']} (Shared Interests: {', '.join(friend['shared_interests'])})")

def main():
    print("\nSimple Social Network Friend Recommender\n")
    
    users = create_user_database()
    recommendations = generate_recommendations(users)
    print_recommendations(users, recommendations)

main()
