nombre_proyecto = 'Uy, era para hoy' 
descripcion = 'Aplicación diseñada para estudiantes expertos en procrastinar. El sistema detecta tareas olvidadas, calcula el nivel de peligro acádemico y genera excusas "semi profesionales" automaticamente ' 
tecnologias = ['Vue.js', 'Bootrstrap'] 
integrantes = ['Mariana', 'Jahela', ''] 
funcionalidades = ['Gestión de tareas', 'Calendario inteligente', 'Alertas y recordatorios automáticos de próximas entregas', 'Notificaciones'] 

def mostrar_info():
    print(f'Proyecto: {nombre_proyecto}')
    print(f'Descripción: {descripcion}')
    print(f'Equipo: {", ".join(integrantes)}')
    print(f'Tecnologías: {", ".join(tecnologias)}')
    print('Funcionalidades:')
    for f in funcionalidades:
        print(f' - {f}')

mostrar_info()