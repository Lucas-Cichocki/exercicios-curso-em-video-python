import math

AN = int(input('Diga o angulo: '))

radianos = math.radians(AN)

seno = math.sin(radianos)

cosceno = math.cos(radianos)

tangente = math.tan(radianos)

print(f'O seno de {AN} valor e: {seno}, o cosceno e: {cosceno} e a tangente e: {tangente}')