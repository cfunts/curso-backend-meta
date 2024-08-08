# Lista de cafés
menu = ['Espresso', 'Latte', 'Cappuccino', 'Caffè Mocha', 'Cortado']

# Función para verificar si el café empieza con 'C'
def starts_with_c(coffee):
    return coffee.startswith('C')

# Usando map para aplicar la función a cada elemento de la lista
map_coffee = map(starts_with_c, menu)
print("Resultados de map:")
for result in map_coffee:
    print(result)  # Imprime True o False si el café empieza con 'C'

# Volver a crear la lista original para usar filter
menu = ['Espresso', 'Latte', 'Cappuccino', 'Caffè Mocha', 'Cortado']

# Usando filter para filtrar los cafés que empiezan con 'C'
filter_coffee = filter(starts_with_c, menu)
print("\nResultados de filter:")
for coffee in filter_coffee:
    print(coffee)  # Imprime solo los cafés que empiezan con 'C'