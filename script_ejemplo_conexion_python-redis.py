import redis

# Configura la conexión
redis_host = "localhost" # Cambia esto por la IP o el hostname del contenedor si no está en localhost
redis_port = 6379 # Puerto por defecto
redis_db = 0 # BBDD a usar dentro de redis (Por defecto de 0 a 15)

# Crear conexion
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db, decode_responses=True)

# Prueba la conexión
ping_response = redis_client.ping()
print(f"Conexión exitosa: {ping_response}")

# Prueba crear clave y recuperar su valor
redis_client.set("Nombre", "Manuel")  # Establecemos un valor
value = redis_client.get("Nombre")  # Obtenemos el valor
print(f"Valor de 'Nombre': {value}")