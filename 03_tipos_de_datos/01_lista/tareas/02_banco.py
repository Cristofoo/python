# Nombre: Cristofer Fuentes
# Fecha: 22-04-2025

tareas = [
    '🏦 Sacar dinero del banco.',
    '🧺 Hacer la colada.',
    '🌳 Dar un paseo.',
    '💈 Cortarse el cabello.',
    '🍵 Preparar un té.',
    '💻 Terminar el capítulo de Listas.',
    '💖 Llamar a mamá.',
    '📺 Ver Mi Héroe Academia.'
]

# 1
print("Primera tarea:", tareas[0])
# 2
print("Segunda tarea:", tareas[1])
# 3
print("Subconjunto:", tareas[2:5])
# 4 (manejo de error)
try:
    print(tareas[20])
except IndexError:
    print("⚠ Error: Índice fuera de rango.")
# Bonus (sin usar append)
tareas += ["🔓 Nueva tarea secreta"]
print(tareas)
