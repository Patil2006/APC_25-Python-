# 19. Create two sets:
# Students present in the morning session
# Students present in the afternoon session
# Find:
# Students present in both sessions
# Students present only in the morning
# Students present only in the afternoon
# Students present in at least one session

morning = {"Amit", "Bhakti", "Sneha", "Rahul"}
afternoon = {"Bhakti", "Rahul", "Priya", "Neha"}

both = morning.intersection(afternoon)
only_morning = morning.difference(afternoon)
only_afternoon = afternoon.difference(morning)
at_least_one = morning.union(afternoon)

print("Students present in both sessions:", both)
print("Students present only in the morning:", only_morning)
print("Students present only in the afternoon:", only_afternoon)
print("Students present in at least one session:", at_least_one)