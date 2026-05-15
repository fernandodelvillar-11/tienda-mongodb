from DAO.cliente_DAO import ClienteDAO
from DTO.cliente_DTO import ClienteDTO, ContactoDTO, DireccionDTO, CompraDTO


class ClienteService:

    def __init__(self):
        self.dao = ClienteDAO()

    # ─────────────────────────────────────────
    #  CREATE
    # ─────────────────────────────────────────

    def crear_cliente(self, nombre, email, fecha_registro,
                      telefono, calle, ciudad, region,
                      compras: list = None):

        direccion = DireccionDTO(calle, ciudad, region)
        contacto  = ContactoDTO(telefono, direccion)
        cliente   = ClienteDTO(
            nombre         = nombre,
            email          = email,
            fecha_registro = fecha_registro,
            contacto       = contacto,
            compras        = compras if compras else []
        )
        return self.dao.insertar(cliente)

    def insertar_datos_iniciales(self, clientes: list):
        return self.dao.insertar_muchos(clientes)

    # ─────────────────────────────────────────
    #  READ — básico
    # ─────────────────────────────────────────

    def listar_clientes(self):
        return self.dao.obtener_todos()

    def obtener_cliente(self, id):
        return self.dao.obtener_por_id(id)

    def obtener_por_email(self, email):
        return self.dao.obtener_por_email(email)

    def buscar_por_comparacion(self, opcion, valor):
        return self.dao.buscar_por_comparacion(opcion, valor)

    # ─────────────────────────────────────────
    #  READ — avanzado
    # ─────────────────────────────────────────

    def buscar_por_regex(self, campo, patron):
        return self.dao.buscar_por_regex(campo, patron)

    def buscar_por_rango_fechas(self, opcion, desde, hasta):
        return self.dao.buscar_por_rango_fechas(opcion, desde, hasta)

    def buscar_en_subdocumento(self, campo, valor):
        return self.dao.buscar_en_subdocumento(campo, valor)

    # ─────────────────────────────────────────
    #  UPDATE — documento raíz
    # ─────────────────────────────────────────

    def actualizar_campo_raiz(self, email, campo, nuevo_valor):
        return self.dao.actualizar_campo_raiz(email, campo, nuevo_valor)

    # ─────────────────────────────────────────
    #  UPDATE — subdocumento y array
    # ─────────────────────────────────────────

    def actualizar_contacto(self, email, campo, nuevo_valor):
        return self.dao.actualizar_contacto(email, campo, nuevo_valor)

    def agregar_compra(self, email, producto, categoria,
                       precio, cantidad, fecha_compra):
        compra = CompraDTO(producto, categoria, precio, cantidad, fecha_compra)
        return self.dao.agregar_compra(email, compra)

    def eliminar_compra(self, email, producto):
        return self.dao.eliminar_compra(email, producto)

    # ─────────────────────────────────────────
    #  DELETE
    # ─────────────────────────────────────────

    def eliminar_cliente(self, email):
        return self.dao.eliminar(email)

    # ─────────────────────────────────────────
    #  UTILIDAD
    # ─────────────────────────────────────────

    def contar_clientes(self):
        return self.dao.contar_documentos()