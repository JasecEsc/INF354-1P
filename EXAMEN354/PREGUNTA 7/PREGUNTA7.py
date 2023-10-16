import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo dirigido
familia = nx.DiGraph()

# Agregar nodos para representar a los miembros de la familia
familia.add_node("abuela")
familia.add_node("tio")
familia.add_node("tia")
familia.add_node("padre")
familia.add_node("madre")
familia.add_node("yo")
familia.add_node("hermano1")
familia.add_node("hermano2")
familia.add_node("primo")
familia.add_node("prima")

# Agregar aristas para definir las relaciones familiares
familia.add_edge("abuela", "padre")
familia.add_edge("abuela", "tia")
familia.add_edge("tio", "primo")
familia.add_edge("tia", "prima")
familia.add_edge("tio", "prima")
familia.add_edge("tia", "primo")
familia.add_edge("padre", "yo")
familia.add_edge("madre", "yo")
familia.add_edge("padre", "hermano1")
familia.add_edge("madre", "hermano1")
familia.add_edge("padre", "hermano2")
familia.add_edge("madre", "hermano2")

# Dibujar el grafo
pos = nx.spring_layout(familia, seed=42)
nx.draw(familia, pos, with_labels=True, node_size=800, node_color='lightblue', font_size=10, font_color='black')
plt.title("Árbol Genealógico de la Familia")
#hacer correr con python PREGUNTA7.py
plt.show()

