from rdflib import Graph, Literal, RDF, URIRef


g = Graph()

hyderabad = URIRef('http://example.org/Hyderabad')
charminar = URIRef('http://example.org/Charminar')
has_place = URIRef('http://example.org/hasPlace')


g.add((hyderabad, has_place, charminar))

print('Knowledge Graph Triples:')
for s, p, o in g:
    print(s, p, o)
