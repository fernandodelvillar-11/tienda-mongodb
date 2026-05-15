from datetime import datetime
from seed import cargar_datos
from service.cliente_service import ClienteService
import re

service = ClienteService()


# ─────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────

def separador():
    print("\n" + "─" * 55)

def pausar():
    input("\nPresiona ENTER para volver al menú...")

def volver():
    print("  0. Volver al menú principal")

def leer_solo_letras(mensaje):
    """Solo acepta letras y espacios. Ej: nombres, ciudades, regiones, categorías."""
    while True:
        valor = input(mensaje).strip()
        if valor == "0":
            return None
        if not valor:
            print("  ⚠️  Este campo no puede estar vacío.")
            continue
        if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]+$", valor):
            print("  ⚠️  Solo se permiten letras y espacios. Intenta de nuevo.")
            continue
        return valor

def leer_texto_libre(mensaje):
    """Acepta letras, números y espacios. Ej: calles, productos."""
    while True:
        valor = input(mensaje).strip()
        if valor == "0":
            return None
        if not valor:
            print("  ⚠️  Este campo no puede estar vacío.")
            continue
        if not re.match(r"^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑüÜ\s\.\,\#\-\'\"]+$", valor):
            print("  ⚠️  Caracteres no permitidos. Intenta de nuevo.")
            continue
        return valor

def leer_email(mensaje):
    """Valida que el email tenga formato correcto (texto@texto.texto)."""
    while True:
        valor = input(mensaje).strip()
        if valor == "0":
            return None
        if not valor:
            print("  ⚠️  El email no puede estar vacío.")
            continue
        if not re.match(r"^[\w\.\-]+@[\w\.\-]+\.[a-zA-Z]{2,}$", valor):
            print("  ⚠️  Formato de email inválido. Ej: usuario@correo.com")
            continue
        return valor

def leer_telefono(mensaje):
    """Solo acepta números y el símbolo + al inicio. Ej: +56912345678."""
    while True:
        valor = input(mensaje).strip()
        if valor == "0":
            return None
        if not valor:
            print("  ⚠️  El teléfono no puede estar vacío.")
            continue
        if not re.match(r"^\+?[0-9]{7,15}$", valor):
            print("  ⚠️  Teléfono inválido. Solo números, puede iniciar con +. Ej: +56912345678")
            continue
        return valor

def leer_fecha(mensaje):
    """Solicita una fecha en formato DD/MM/AAAA y la valida."""
    while True:
        fecha_str = input(mensaje).strip()
        if fecha_str == "0":
            return None
        if not fecha_str:
            print("  ⚠️  La fecha no puede estar vacía.")
            continue
        try:
            return datetime.strptime(fecha_str, "%d/%m/%Y")
        except ValueError:
            print("  ⚠️  Formato inválido. Use DD/MM/AAAA (ej: 25/12/2024).")

def leer_entero(mensaje):
    """Solicita un número entero positivo y lo valida."""
    while True:
        valor_str = input(mensaje).strip()
        if valor_str == "0":
            return None
        if not valor_str:
            print("  ⚠️  Este campo no puede estar vacío.")
            continue
        if not valor_str.isdigit():
            print("  ⚠️  Solo se permiten números enteros positivos.")
            continue
        valor = int(valor_str)
        if valor <= 0:
            print("  ⚠️  El valor debe ser mayor a 0.")
            continue
        return valor

CATEGORIAS = {
    "1": "Tecnología",
    "2": "Muebles",
    "3": "Oficina",
    "4": "Fotografía",
    "5": "Audio",
    "6": "Accesorios",
    "7": "Electrohogar",
    "8": "Ropa y Calzado",
    "9": "Deportes",
}

def leer_categoria():
    """Muestra las categorías disponibles y obliga al usuario a elegir una."""
    print("\n  Categorías disponibles:")
    for numero, nombre in CATEGORIAS.items():
        print(f"    {numero}. {nombre}")
    print("    0. Volver al menú principal")
    while True:
        opcion = input("\n  Selecciona una categoría: ").strip()
        if opcion == "0":
            return None
        if opcion in CATEGORIAS:
            return CATEGORIAS[opcion]
        print(f"  ⚠️  Opción inválida. Elige un número del 1 al {len(CATEGORIAS)}.")

def leer_opcion(mensaje, opciones_validas):
    """Valida que la opción ingresada esté dentro de las permitidas."""
    opciones_validas = [str(o) for o in opciones_validas] + ["0"]
    while True:
        valor = input(mensaje).strip()
        if valor in opciones_validas:
            return valor
        print(f"  ⚠️  Opción inválida. Las opciones disponibles son: {', '.join(opciones_validas)}")

def mostrar_cliente(cliente):
    print(f"\n  Nombre     : {cliente.get_nombre()}")
    print(f"  Email      : {cliente.get_email()}")
    fecha = cliente.get_fecha_registro()
    print(f"  Registro   : {fecha.strftime('%d/%m/%Y') if fecha else '-'}")
    contacto = cliente.get_contacto()
    print(f"  Teléfono   : {contacto.get_telefono()}")
    dir_ = contacto.get_direccion()
    print(f"  Dirección  : {dir_.get_calle()}, {dir_.get_ciudad()}, {dir_.get_region()}")
    compras = cliente.get_compras()
    if compras:
        print(f"  Compras ({len(compras)}):")
        for c in compras:
            print(f"    • {c}")
    else:
        print("  Compras    : Sin compras registradas")

def mostrar_lista(clientes, titulo="Resultados"):
    separador()
    print(f"  {titulo.upper()}")
    separador()
    if not clientes:
        print("  Sin resultados.")
    else:
        print(f"  Total: {len(clientes)} registro(s)")
        for cliente in clientes:
            mostrar_cliente(cliente)
            print()


# ─────────────────────────────────────────
#  1. CREAR CLIENTE
# ─────────────────────────────────────────

def crear_cliente():
    separador()
    print("  CREAR NUEVO CLIENTE")
    print("  (ingresa 0 en cualquier campo para volver al menú)")
    separador()

    nombre = leer_solo_letras("Nombre completo                : ")
    if nombre is None: return

    email = leer_email("Email                          : ")
    if email is None: return

    fecha_registro = leer_fecha("Fecha de registro (DD/MM/AAAA) : ")
    if fecha_registro is None: return

    print("\n-- Contacto --")
    telefono = leer_telefono("Teléfono : ")
    if telefono is None: return

    calle = leer_texto_libre("Calle    : ")
    if calle is None: return

    ciudad = leer_solo_letras("Ciudad   : ")
    if ciudad is None: return

    region = leer_solo_letras("Región   : ")
    if region is None: return

    compras = []
    print("\n-- Compras (ingresa 0 en Producto para terminar) --")
    while True:
        producto = leer_texto_libre("Producto (o 0 para terminar)  : ")
        if producto is None:
            break

        categoria = leer_categoria()
        if categoria is None: break

        precio = leer_entero("Precio      : ")
        if precio is None: break

        cantidad = leer_entero("Cantidad    : ")
        if cantidad is None: break

        fecha_compra = leer_fecha("Fecha compra (DD/MM/AAAA): ")
        if fecha_compra is None: break

        from DTO.cliente_DTO import CompraDTO
        compra = CompraDTO(producto, categoria, precio, cantidad, fecha_compra)
        compras.append(compra)
        print(f"  ✅ Compra '{producto}' agregada.")

    id_nuevo = service.crear_cliente(
        nombre, email, fecha_registro,
        telefono, calle, ciudad, region,
        compras
    )
    print(f"\n✅ Cliente creado correctamente. ID: {id_nuevo}")
    pausar()


# ─────────────────────────────────────────
#  2. LISTAR TODOS
# ─────────────────────────────────────────

def listar_clientes():
    clientes = service.listar_clientes()
    mostrar_lista(clientes, "Listado completo de clientes")
    pausar()


# ─────────────────────────────────────────
#  3. BUSCAR POR OPERADOR DE COMPARACIÓN
# ─────────────────────────────────────────

def buscar_por_comparacion():
    separador()
    print("  BUSCAR POR OPERADOR DE COMPARACIÓN")
    separador()
    print("  1. Clientes registrados después de una fecha  ($gt)")
    print("  2. Clientes con compras cuyo precio supere un valor ($gt)")
    print("  3. Clientes con compras en categorías específicas ($in)")
    volver()

    opcion = leer_opcion("\n  Elige una opción: ", [1, 2, 3])
    if opcion == "0": return

    if opcion == "1":
        valor = leer_fecha("Fecha desde (DD/MM/AAAA): ")
        if valor is None: return
        titulo = f"Registrados después de {valor.strftime('%d/%m/%Y')}"

    elif opcion == "2":
        valor = leer_entero("Precio mínimo de compra ($): ")
        if valor is None: return
        titulo = f"Clientes con compras mayores a ${valor:,}"

    elif opcion == "3":
        print("  Categorías disponibles: Tecnología, Muebles, Oficina, Fotografía, Audio, Accesorios")
        cats_str = leer_solo_letras("  Ingresa una categoría: ")
        if cats_str is None: return
        valor  = [cats_str.strip()]
        titulo = f"Clientes con compras en: {valor}"

    resultados = service.buscar_por_comparacion(int(opcion), valor)
    mostrar_lista(resultados, titulo)
    pausar()


# ─────────────────────────────────────────
#  4. BUSCAR CON EXPRESIÓN REGULAR
# ─────────────────────────────────────────

def buscar_por_regex():
    separador()
    print("  BUSCAR CON EXPRESIÓN REGULAR ($regex)")
    separador()
    print("  Campos disponibles:")
    print("    1. nombre")
    print("    2. email")
    print("    3. contacto.direccion.ciudad")
    print("    4. contacto.direccion.region")
    volver()

    campos_map = {
        "1": "nombre",
        "2": "email",
        "3": "contacto.direccion.ciudad",
        "4": "contacto.direccion.region"
    }

    opcion = leer_opcion("\n  Elige el campo (1-4): ", [1, 2, 3, 4])
    if opcion == "0": return

    campo  = campos_map[opcion]
    patron = leer_texto_libre("  Patrón de búsqueda: ")
    if patron is None: return

    resultados = service.buscar_por_regex(campo, patron)
    mostrar_lista(resultados, f"Regex '{patron}' en '{campo}'")
    pausar()


# ─────────────────────────────────────────
#  5. BUSCAR POR RANGO DE FECHAS
# ─────────────────────────────────────────

def buscar_por_rango_fechas():
    separador()
    print("  BUSCAR POR RANGO DE FECHAS")
    separador()
    print("  1. Por fecha de registro del cliente")
    print("  2. Por fecha de compra en el historial")
    volver()

    opcion = leer_opcion("\n  Elige una opción: ", [1, 2])
    if opcion == "0": return

    desde = leer_fecha("Fecha desde (DD/MM/AAAA): ")
    if desde is None: return

    hasta = leer_fecha("Fecha hasta (DD/MM/AAAA): ")
    if hasta is None: return

    if desde > hasta:
        print("  ⚠️  La fecha 'desde' no puede ser mayor que la fecha 'hasta'.")
        pausar()
        return

    titulo = (
        f"Clientes {'registrados' if opcion == '1' else 'con compras'} "
        f"entre {desde.strftime('%d/%m/%Y')} y {hasta.strftime('%d/%m/%Y')}"
    )

    resultados = service.buscar_por_rango_fechas(int(opcion), desde, hasta)
    mostrar_lista(resultados, titulo)
    pausar()


# ─────────────────────────────────────────
#  6. BUSCAR EN SUBDOCUMENTO O ARRAY
# ─────────────────────────────────────────

def buscar_en_subdocumento():
    separador()
    print("  BUSCAR EN SUBDOCUMENTO O ARRAY")
    separador()
    print("  1. Por ciudad del cliente  (subdocumento contacto.direccion)")
    print("  2. Por región del cliente  (subdocumento contacto.direccion)")
    print("  3. Por producto comprado   (array compras)")
    volver()

    campos = {
        "1": ("contacto.direccion.ciudad", "Ciudad",   leer_solo_letras),
        "2": ("contacto.direccion.region", "Región",   leer_solo_letras),
        "3": ("compras.producto",          "Producto",  leer_texto_libre),
    }

    opcion = leer_opcion("\n  Elige una opción: ", [1, 2, 3])
    if opcion == "0": return

    campo, etiqueta, fn_leer = campos[opcion]
    valor = fn_leer(f"  {etiqueta}: ")
    if valor is None: return

    resultados = service.buscar_en_subdocumento(campo, valor)
    mostrar_lista(resultados, f"Búsqueda en subdocumento/array: '{valor}'")
    pausar()


# ─────────────────────────────────────────
#  7. ACTUALIZAR CAMPO RAÍZ
# ─────────────────────────────────────────

def actualizar_campo_raiz():
    separador()
    print("  ACTUALIZAR CAMPO DEL DOCUMENTO RAÍZ")
    print("  (ingresa 0 en cualquier campo para volver al menú)")
    separador()

    email = leer_email("Email del cliente: ")
    if email is None: return

    cliente = service.obtener_por_email(email)
    if not cliente:
        print("❌ Cliente no encontrado.")
        pausar()
        return

    print("\n  Estado actual:")
    mostrar_cliente(cliente)

    print("\n  Campos modificables:")
    print("    1. nombre")
    print("    2. email")
    volver()

    opcion = leer_opcion("\n  Campo a actualizar: ", [1, 2])
    if opcion == "0": return

    if opcion == "1":
        nuevo_valor = leer_solo_letras("  Nuevo nombre: ")
        campo = "nombre"
    else:
        nuevo_valor = leer_email("  Nuevo email: ")
        campo = "email"

    if nuevo_valor is None: return

    actualizado = service.actualizar_campo_raiz(email, campo, nuevo_valor)

    if actualizado:
        email_busqueda = nuevo_valor if campo == "email" else email
        print(f"\n✅ Campo '{campo}' actualizado. Nuevo estado:")
        mostrar_cliente(service.obtener_por_email(email_busqueda))
    else:
        print("⚠️  No se realizaron cambios.")

    pausar()


# ─────────────────────────────────────────
#  8. ACTUALIZAR SUBDOCUMENTO O ARRAY
# ─────────────────────────────────────────

def actualizar_subdocumento():
    separador()
    print("  ACTUALIZAR SUBDOCUMENTO O ARRAY DE COMPRAS")
    separador()
    print("  1. Actualizar teléfono o dirección  (subdocumento contacto)")
    print("  2. Agregar nueva compra al historial ($push)")
    print("  3. Eliminar una compra del historial ($pull)")
    volver()

    opcion = leer_opcion("\n  Elige una opción: ", [1, 2, 3])
    if opcion == "0": return

    email = leer_email("Email del cliente: ")
    if email is None: return

    cliente = service.obtener_por_email(email)
    if not cliente:
        print("❌ Cliente no encontrado.")
        pausar()
        return

    print("\n  Estado actual:")
    mostrar_cliente(cliente)

    if opcion == "1":
        print("\n  Campos disponibles:")
        print("    1. telefono")
        print("    2. calle")
        print("    3. ciudad")
        print("    4. region")
        volver()

        campos_validos = {
            "1": ("contacto.telefono",         "telefono", leer_telefono),
            "2": ("contacto.direccion.calle",  "calle",    leer_texto_libre),
            "3": ("contacto.direccion.ciudad", "ciudad",   leer_solo_letras),
            "4": ("contacto.direccion.region", "region",   leer_solo_letras),
        }

        sub_opcion = leer_opcion("\n  Campo a modificar: ", [1, 2, 3, 4])
        if sub_opcion == "0": return

        campo_mongo, etiqueta, fn_leer = campos_validos[sub_opcion]
        nuevo_valor = fn_leer(f"  Nuevo valor para '{etiqueta}': ")
        if nuevo_valor is None: return

        actualizado = service.actualizar_contacto(email, campo_mongo, nuevo_valor)
        print(f"\n✅ '{etiqueta}' actualizado." if actualizado else "⚠️  Sin cambios.")

    elif opcion == "2":
        print("\n  -- Nueva compra -- (ingresa 0 en cualquier campo para cancelar)")

        producto = leer_texto_libre("  Producto          : ")
        if producto is None: return

        categoria = leer_categoria()
        if categoria is None: return

        precio = leer_entero("  Precio            : ")
        if precio is None: return

        cantidad = leer_entero("  Cantidad          : ")
        if cantidad is None: return

        fecha_c = leer_fecha("  Fecha (DD/MM/AAAA): ")
        if fecha_c is None: return

        agregado = service.agregar_compra(email, producto, categoria, precio, cantidad, fecha_c)
        print(f"\n✅ Compra '{producto}' agregada." if agregado else "⚠️  Sin cambios.")

    elif opcion == "3":
        producto = leer_texto_libre("\n  Producto a eliminar del historial: ")
        if producto is None: return

        eliminado = service.eliminar_compra(email, producto)
        print(f"\n✅ Compra '{producto}' eliminada." if eliminado else "⚠️  Producto no encontrado.")

    print("\n  Estado actualizado:")
    mostrar_cliente(service.obtener_por_email(email))
    pausar()


# ─────────────────────────────────────────
#  9. ELIMINAR CLIENTE
# ─────────────────────────────────────────

def eliminar_cliente():
    separador()
    print("  ELIMINAR CLIENTE")
    print("  (ingresa 0 para volver al menú)")
    separador()

    email = leer_email("Email del cliente a eliminar: ")
    if email is None: return

    cliente = service.obtener_por_email(email)
    if not cliente:
        print("❌ Cliente no encontrado.")
        pausar()
        return

    print("\n  ⚠️  Cliente a eliminar:")
    mostrar_cliente(cliente)

    print("\n  ¿Confirmas la eliminación?")
    print("    1. Sí, eliminar")
    print("    2. No, cancelar")

    confirmacion = leer_opcion("  Elige una opción: ", [1, 2])
    if confirmacion in ["0", "2"]:
        print("\n  Operación cancelada.")
        pausar()
        return

    eliminado = service.eliminar_cliente(email)
    print(f"\n✅ Cliente '{cliente.get_nombre()}' eliminado correctamente."
          if eliminado else "⚠️  No se pudo eliminar.")
    pausar()


# ─────────────────────────────────────────
#  MENÚ PRINCIPAL
# ─────────────────────────────────────────

opciones = {
    "1": crear_cliente,
    "2": listar_clientes,
    "3": buscar_por_comparacion,
    "4": buscar_por_regex,
    "5": buscar_por_rango_fechas,
    "6": buscar_en_subdocumento,
    "7": actualizar_campo_raiz,
    "8": actualizar_subdocumento,
    "9": eliminar_cliente,
}

def menu():
    while True:
        print("\n" + "═" * 55)
        print("     SISTEMA DE GESTIÓN DE CLIENTES — TIENDA")
        print("═" * 55)
        print("  1. Crear nuevo cliente")
        print("  2. Listar todos los clientes")
        print("  3. Buscar por operador de comparación")
        print("  4. Buscar con expresión regular ($regex)")
        print("  5. Buscar por rango de fechas")
        print("  6. Buscar en subdocumento o array")
        print("  7. Actualizar campo del documento raíz")
        print("  8. Actualizar subdocumento o array de compras")
        print("  9. Eliminar cliente")
        print("  0. Salir")
        print("═" * 55)

        opcion = leer_opcion("  Selecciona una opción: ", [1, 2, 3, 4, 5, 6, 7, 8, 9])

        if opcion == "0":
            print("\n  👋 Hasta luego.\n")
            break
        else:
            opciones[opcion]()


# ─────────────────────────────────────────
#  ENTRADA
# ─────────────────────────────────────────

if __name__ == "__main__":
    print("\n" + "═" * 55)
    print("     SISTEMA DE GESTIÓN DE CLIENTES — TIENDA")
    print("     Base de Datos No Estructuradas | INACAP")
    print("═" * 55)
    print("\n🔄 Verificando datos iniciales...")
    cargar_datos()
    menu()