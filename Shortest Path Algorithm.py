# - copper = {
# -     'species': 'guinea pig',
# -     'age': 2
# - }

# To add a new key-value pair after declaring a dictionary (above), you can indicate the key in the same way you would access an existing key, and set the value of the new key by using the assignment operator:
# - copper['food'] = 'hay'
# The same syntax can be used to change the value of an existing key within the dictionary as demonstrated below.
# - copper['species'] = 'Cavia porcellus'

# You can remove a key-value pair from a dictionary by using the "del" keyword. The syntax is the following:
# - del copper['age']


###################################

# Graphs are data structures representing relations between pairs of elements. These elements, called nodes, can be real-life objects, entities, points in space or others. The connections between the nodes are called the edges.
# For example, a graph can be used to represent two points in the space, A and B, connected by a path. A graph like this will be made of two nodes connected by an edge.

my_graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['A', 'C']
}
