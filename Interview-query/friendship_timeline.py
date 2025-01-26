from collections import defaultdict

def friendship_timeline(friends_added, friends_removed):
    # Normalize user_ids so that [1, 2] and [2, 1] are treated as the same pair
    def normalize(user_ids):
        return tuple(sorted(user_ids))

    # Store the start dates of friendships by normalized user_ids
    active_friendships = defaultdict(list)

    # Process friends_added to build a timeline of friendship starts
    for entry in friends_added:
        normalized_pair = normalize(entry['user_ids'])
        active_friendships[normalized_pair].append(entry['created_at'])

    friendships = []

    # Process friends_removed to match start and end dates
    for entry in friends_removed:
        normalized_pair = normalize(entry['user_ids'])
        if normalized_pair in active_friendships and active_friendships[normalized_pair]:
            # Take the earliest start date for the friendship
            start_date = active_friendships[normalized_pair].pop(0)
            friendships.append({
                'user_ids': list(normalized_pair),
                'start_date': start_date,
                'end_date': entry['created_at']
            })

    return friendships

friends_added = [
    {'user_ids': [1, 2], 'created_at': '2020-01-01'},
    {'user_ids': [3, 2], 'created_at': '2020-01-02'},
    {'user_ids': [2, 1], 'created_at': '2020-02-02'},
    {'user_ids': [4, 1], 'created_at': '2020-02-02'}]

friends_removed = [
    {'user_ids': [2, 1], 'created_at': '2020-01-03'},
    {'user_ids': [2, 3], 'created_at': '2020-01-05'},
    {'user_ids': [1, 2], 'created_at': '2020-02-05'}]

friendships = friendship_timeline(friends_added, friends_removed)
for friendship in friendships:
    print(friendship)