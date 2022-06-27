###################################################

# SET
# Unordered
# Unchangeable
# Duplicates not allowed

###################################################

set1=set([25,97,21])
set2=set([25,7,3])

# difference(): Returns a set containing the difference between two or more sets
set1.difference(set2)
set1-set2

set2.difference(set1)
set2-set1

# symmetric_difference(): Returns a set with the symmetric differences of two sets
set1.symmetric_difference(set2)
set2.symmetric_difference(set1)
# Now outputs are SAME!

# intersection(): Returns a set, that is the intersection of two other sets
set1.intersection(set2)
set2.intersection(set1)
# Outputs are SAME!

#union(): Return a set containing the union of sets
set1.union(set2)

# isdisjoint(): Returns whether two sets have a intersection or not
set1.isdisjoint(set2)