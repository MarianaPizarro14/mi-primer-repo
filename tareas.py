# tareas.py · Seguimiento de tareas del equipo

tareas_pendientes = [
'Backend: Falta todo',
'Base de datos: Falta Normalización',
]


tareas_completadas = [
    'Frontend: Ya esta terminado', 
    'Diagramas: Completados',
]

print('=== TAREAS PENDIENTES ===')
for t in tareas_pendientes:
    print(f' ☐ {t}')

print('=== TAREAS COMPLETADAS ===')
for t in tareas_completadas:
    print(f' ✓ {t}')