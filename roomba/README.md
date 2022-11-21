# Reporte roomba 

## _Instrucciones_
Dado:
- Habitación de MxN espacios.
- Número de agentes.
- Porcentaje de celdas inicialmente sucias.
- Tiempo máximo de ejecución.

Realiza la siguiente simulación:
- Inicializa las celdas sucias (ubicaciones aleatorias).
- Todos los agentes empiezan en la celda [1,1].
En cada paso de tiempo:
- Si la celda está sucia, entonces aspira.
- Si la celda está limpia, el agente elije una dirección aleatoria para moverse (unas de las 8 celdas vecinas) y elije la acción de movimiento (si no puede moverse allí, permanecerá en la misma celda).

## _Información recopilada_
- Tiempo necesario hasta que todas las celdas estén limpias (o se haya llegado al tiempo máximo).
- Porcentaje de celdas limpias después del termino de la simulación.
- Número de movimientos realizados por todos los agentes.

Para cada una de las simulaciones tomaremos un escenario equivalente de porcentaje de 0.5 de "piso sucio" y 10 frames por segundo, variando solamente el numero de agentes/roombas. 

--- 
### Por 4 agentes
|Tiempo              |Celdas limplias al final|movimientos totales|
|           -        |           -            |          -        | 
| Aprox. 20 segundos | 100% limpio, 0% sucio  |     122 steps     |

<p align="center">
<image src="Media/4agents.gif#center" width="30%" height="30%"  />
</p>

---

## Por 5 agentes
|Tiempo              |Celdas limplias al final|movimientos totales|
|           -        |           -            |          -        | 
| Aprox. 18 segundos | 100% limpio, 0% sucio  |     109 steps     |

<p align="center">
<image src="Media/5agents.gif#center" width="30%" height="30%"  />
</p> 

---

## Por 10 agentes
|Tiempo              |Celdas limplias al final|movimientos totales|
|           -        |           -            |          -        | 
| Aprox. 10 segundos | 100% limpio, 0% sucio  |      57 steps     |

<p align="center">
<image src="Media/10.gif#center" width="30%" height="30%"  />
</p>

---
## _Conclusiones_

Para ver las comparaciones se creo un ambiente similar entre todas las simulaciones donde unicamente cambiaba el numero de agentes que limpiaban la zona. 

En las graficas se puede ver como limpian el porcentaje, haciendo que este vaya variando conforme cada movimiento/step, haciendo que el porcentaje de celdas sucias disminuya y por el contrario, la grafica de celdas limpias aumenta. Al final cuando van quedando pocas celdas sucias la velocidad con la que los roombas limpian (encuentran una celda sucia) es menor ya que al tener direcciones aleatorias y nodirigidas, la probabilidad de encontrar esa celda especifica para limpiar disminuye, esto se ve en la ultima grafica donde se va volviendo la grafica mas recta. 

Al final como se esperaba, el agregar mas agentes en la simulacion y bajo las mismas circunstancias, hace que el tiempo y los movimientos de limpieza sea menor. 