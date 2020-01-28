from graph import Graph
from generate_edges import make_edges
from generate_nodes import make_nodes

'''
handels all of program


'''

def main():
    
    make_edges()        #generates edge file
    make_nodes()        #generates node file
    g = Graph("nodes.txt", "edges.txt") #generates graph
    #add pathfind
    #UI
    #units

main()