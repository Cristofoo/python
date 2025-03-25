# Cristofer fuentes
#programador de left for dead 2
#24-03-2025

tareas = ["🏦Sacar dinero del banco", 
          "🪣hacer la colada", 
          "🎄dar un paseo", 
          "💈cortarse el cabello",
          "🍵preparar el té",
          "💻Terminar el capítulo de Listas",
          "💖llamar a mamá",
          "📺Ver mi héroe academía"]


print(f"desafio uno: {tareas[0]}")
print(f"desafio dos: {tareas[1]}")
subconjunto = tareas[2:5]
print(f"desafio tres: {subconjunto}")

try:
    tarea_inexistente = tareas[100]
except IndexError as e:
    print(f"desafio cuatro: Error detectado -> {e}")

tareas += ["💻 cambiar a cientifico humanista.com"]
print(f"Bonus: {tareas}")