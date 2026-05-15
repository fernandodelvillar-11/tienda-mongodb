from datetime import datetime
from service.cliente_service import ClienteService
from DTO.cliente_DTO import ClienteDTO, ContactoDTO, DireccionDTO, CompraDTO


def cargar_datos():
    service = ClienteService()

    clientes = [
        ClienteDTO(
            nombre="Carlos Ramírez", email="carlos.ramirez@email.com",
            fecha_registro=datetime(2023, 3, 15),
            contacto=ContactoDTO(
                telefono="+56912345678",
                direccion=DireccionDTO("Av. Providencia 1234", "Santiago", "Metropolitana")
            ),
            compras=[
                CompraDTO("Laptop Lenovo",     "Tecnología", 599990, 1, datetime(2023, 4, 10)),
                CompraDTO("Mouse Inalámbrico", "Tecnología",  19990, 2, datetime(2023, 6, 22)),
            ]
        ),
        ClienteDTO(
            nombre="Ana López", email="ana.lopez@email.com",
            fecha_registro=datetime(2023, 5, 20),
            contacto=ContactoDTO(
                telefono="+56923456789",
                direccion=DireccionDTO("Calle Los Aromos 456", "Viña del Mar", "Valparaíso")
            ),
            compras=[
                CompraDTO("Teclado Mecánico", "Tecnología",  89990, 1, datetime(2023, 7,  5)),
                CompraDTO("Silla Gamer",      "Muebles",    249990, 1, datetime(2023, 9, 14)),
            ]
        ),
        ClienteDTO(
            nombre="Pedro Soto", email="pedro.soto@email.com",
            fecha_registro=datetime(2023, 1, 8),
            contacto=ContactoDTO(
                telefono="+56934567890",
                direccion=DireccionDTO("Pasaje Rosas 789", "Concepción", "Biobío")
            ),
            compras=[
                CompraDTO('Monitor 24"',         "Tecnología", 189990, 1, datetime(2023, 2, 28)),
                CompraDTO("Audífonos Bluetooth", "Tecnología",  49990, 1, datetime(2023, 8,  3)),
            ]
        ),
        ClienteDTO(
            nombre="María González", email="maria.gonzalez@email.com",
            fecha_registro=datetime(2022, 11, 30),
            contacto=ContactoDTO(
                telefono="+56945678901",
                direccion=DireccionDTO("Av. Libertad 321", "Temuco", "La Araucanía")
            ),
            compras=[
                CompraDTO("Tablet Samsung", "Tecnología", 299990, 1, datetime(2022, 12, 18)),
                CompraDTO("Funda Tablet",   "Accesorios",  14990, 1, datetime(2022, 12, 18)),
                CompraDTO("Smartwatch",     "Tecnología", 149990, 1, datetime(2023,  5,  7)),
            ]
        ),
        ClienteDTO(
            nombre="Juan Herrera", email="juan.herrera@email.com",
            fecha_registro=datetime(2024, 2, 14),
            contacto=ContactoDTO(
                telefono="+56956789012",
                direccion=DireccionDTO("Calle O'Higgins 654", "Rancagua", "O'Higgins")
            ),
            compras=[
                CompraDTO("Impresora HP",   "Oficina", 79990, 1, datetime(2024, 3, 1)),
                CompraDTO("Resma de Papel", "Oficina",  4990, 5, datetime(2024, 3, 1)),
            ]
        ),
        ClienteDTO(
            nombre="Valentina Torres", email="valentina.torres@email.com",
            fecha_registro=datetime(2024, 6, 1),
            contacto=ContactoDTO(
                telefono="+56967890123",
                direccion=DireccionDTO("Av. Colón 987", "Antofagasta", "Antofagasta")
            ),
            compras=[
                CompraDTO("Cámara Sony", "Fotografía", 499990, 1, datetime(2024, 6, 15)),
                CompraDTO("Trípode",     "Fotografía",  34990, 1, datetime(2024, 7, 20)),
            ]
        ),
        ClienteDTO(
            nombre="Diego Morales", email="diego.morales@email.com",
            fecha_registro=datetime(2023, 9, 10),
            contacto=ContactoDTO(
                telefono="+56978901234",
                direccion=DireccionDTO("Calle Maipú 111", "Iquique", "Tarapacá")
            ),
            compras=[
                CompraDTO("Parlante JBL", "Audio",      99990, 1, datetime(2023, 10,  5)),
                CompraDTO("Cable USB-C",  "Accesorios",  9990, 3, datetime(2023, 11, 11)),
            ]
        ),
        ClienteDTO(
            nombre="Sofía Castillo", email="sofia.castillo@email.com",
            fecha_registro=datetime(2024, 1, 25),
            contacto=ContactoDTO(
                telefono="+56989012345",
                direccion=DireccionDTO("Av. Prat 500", "Puerto Montt", "Los Lagos")
            ),
            compras=[
                CompraDTO("Notebook Dell",  "Tecnología", 699990, 1, datetime(2024, 2, 10)),
                CompraDTO("Mochila Laptop", "Accesorios",  29990, 1, datetime(2024, 2, 10)),
                CompraDTO("Hub USB",        "Tecnología",  24990, 1, datetime(2024, 4, 18)),
            ]
        ),
    ]

    insertados = 0
    for cliente in clientes:
        # Verifica por email si el cliente ya existe antes de insertar
        if not service.obtener_por_email(cliente.get_email()):
            service.insertar_datos_iniciales([cliente])
            insertados += 1

    if insertados > 0:
        print(f"✅ Se insertaron {insertados} cliente(s) nuevos en la base de datos.")
    else:
        print("✅ Todos los clientes iniciales ya existen. No se insertaron duplicados.")