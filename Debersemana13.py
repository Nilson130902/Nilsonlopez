#Desarrolla una función en Python que calcule la
#temperatura promedio de una ciudad durante un período de tiempo.
temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 12}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 13},
            {"day": "Jueves", "temp": 11},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 13}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 11},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 12},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 11},
            {"day": "Domingo", "temp": 15}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 10},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 11}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "temp": 12},
            {"day": "Martes", "temp": 14},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 10},
            {"day": "Viernes", "temp": 13},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 19}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 13},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 10},
            {"day": "Jueves", "temp": 12},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 11}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 11},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 10},
            {"day": "Viernes", "temp": 12},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 10}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 11},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 10}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"day": "Lunes", "temp": 10},
            {"day": "Martes", "temp": 12},
            {"day": "Miércoles", "temp": 14},
            {"day": "Jueves", "temp": 11},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 12}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 21}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 11},
            {"day": "Martes", "temp": 13},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 12},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 13}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 20}
        ]
    ]
]

def calcular_promedio_semana(suma, dias_semana):
    pro_semana=round(suma / dias_semana,2)
    return pro_semana
def calcular_promedio_ciudad(suma_promedio_sem, n_semana):
    promedio=round(suma_promedio_sem/n_semana,2)
    return promedio

n_ciudad=0
for ciudad in temperaturas:
    n_ciudad +=1
    print(f'Ciudad Nª: {n_ciudad}')
    n_semana=0
    suma_promedio_sem=0
    for semana in ciudad:
        n_semana +=1
        suma = 0
        for dia in semana:
            suma = suma + dia['temp']
        promedio= calcular_promedio_semana(suma,len(semana))

        suma_promedio_sem += promedio
        print(f'El promedio semana nº  {n_semana} es: {promedio}')
    promedio_ciudad = calcular_promedio_ciudad(suma_promedio_sem,len(ciudad))

    print(f'El promedio mensual es: {promedio_ciudad}')