# Nombre: Cristofer Fuentes
# Fecha: 22-04-2025

inventario = {
    "manzanas": 10,
    "bananas": 5,
    "naranjas": 8
}

# Acceder
print("Manzanas:", inventario["manzanas"])

# Agregar
inventario["peras"] = 12

# Eliminar
inventario.pop("bananas")

# Total
total_frutas = sum(inventario.values())
print("Total de frutas:", total_frutas)
