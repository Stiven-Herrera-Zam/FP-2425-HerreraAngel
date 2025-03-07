Ciudad = 2
Semanas = 4
Dias = 7

# Definir la estructura de datos con temperaturas organizadas por ciudad, semana y día
temperaturas = [
        [  # Ciudad 1
            [  # Semana 1
                {"day": "Lunes", "temp": 78}, {"day": "Martes", "temp": 80}, {"day": "Miércoles", "temp": 82},
                {"day": "Jueves", "temp": 79}, {"day": "Viernes", "temp": 85}, {"day": "Sábado", "temp": 88},
                {"day": "Domingo", "temp": 92}
            ],
            [  # Semana 2
                {"day": "Lunes", "temp": 76}, {"day": "Martes", "temp": 79}, {"day": "Miércoles", "temp": 83},
                {"day": "Jueves", "temp": 81}, {"day": "Viernes", "temp": 87}, {"day": "Sábado", "temp": 89},
                {"day": "Domingo", "temp": 93}
            ],
            [  # Semana 3
                {"day": "Lunes", "temp": 77}, {"day": "Martes", "temp": 81}, {"day": "Miércoles", "temp": 85},
                {"day": "Jueves", "temp": 82}, {"day": "Viernes", "temp": 88}, {"day": "Sábado", "temp": 91},
                {"day": "Domingo", "temp": 95}
            ],
            [  # Semana 4
                {"day": "Lunes", "temp": 75}, {"day": "Martes", "temp": 78}, {"day": "Miércoles", "temp": 80},
                {"day": "Jueves", "temp": 79}, {"day": "Viernes", "temp": 84}, {"day": "Sábado", "temp": 87},
                {"day": "Domingo", "temp": 91}
            ]
        ],
        [  # Ciudad 2
            [  # Semana 1
                {"day": "Lunes", "temp": 62}, {"day": "Martes", "temp": 64}, {"day": "Miércoles", "temp": 68},
                {"day": "Jueves", "temp": 70}, {"day": "Viernes", "temp": 73}, {"day": "Sábado", "temp": 75},
                {"day": "Domingo", "temp": 79}
            ],
            [  # Semana 2
                {"day": "Lunes", "temp": 63}, {"day": "Martes", "temp": 66}, {"day": "Miércoles", "temp": 70},
                {"day": "Jueves", "temp": 72}, {"day": "Viernes", "temp": 75}, {"day": "Sábado", "temp": 77},
                {"day": "Domingo", "temp": 81}
            ],
            [  # Semana 3
                {"day": "Lunes", "temp": 61}, {"day": "Martes", "temp": 65}, {"day": "Miércoles", "temp": 68},
                {"day": "Jueves", "temp": 70}, {"day": "Viernes", "temp": 72}, {"day": "Sábado", "temp": 76},
                {"day": "Domingo", "temp": 80}
            ],
            [  # Semana 4
                {"day": "Lunes", "temp": 64}, {"day": "Martes", "temp": 67}, {"day": "Miércoles", "temp": 69},
                {"day": "Jueves", "temp": 71}, {"day": "Viernes", "temp": 74}, {"day": "Sábado", "temp": 77},
                {"day": "Domingo", "temp": 80}
            ]
        ]
    ]

# Recorrer la estructura y calcular los promedios
for i, ciudad in enumerate(temperaturas):
        print(f"\nCiudad {i + 1}:")
        for j, semana in enumerate(ciudad):
            suma = sum(dia['temp'] for dia in semana)  # Sumar temperaturas de la semana
            promedio = suma / len(semana)  # Calcular el promedio
            print(f"  Semana {j + 1}: Promedio de temperatura = {promedio:.2f}°F")