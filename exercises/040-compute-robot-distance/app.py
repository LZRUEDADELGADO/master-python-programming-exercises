# Your code here
import math

# Función para calcular la distancia final del robot
def compute_robot_distance(movements):
    # Coordenadas iniciales
    x, y = 0, 0
    
    # Procesa cada movimiento 
    for move in movements:
        direction, steps = move.split()  # Divide en dirección y pasos
        steps = int(steps)  # Convierte los pasos a entero
        
        # Actualiza las coordenadas
        if direction == "UP":
            y += steps
        elif direction == "DOWN":
            y -= steps
        elif direction == "LEFT":
            x -= steps
        elif direction == "RIGHT":
            x += steps
    
    # Calcula la distancia usando Pitágoras
    distance = math.sqrt(x**2 + y**2)
    
    return round(distance)

print(compute_robot_distance(["UP 5", "DOWN 3", "LEFT 3", "RIGHT 2"]))  # Ejemplo de salida: 2

