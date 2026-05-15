from config.database import get_database
from DTO.cliente_DTO import ClienteDTO, CompraDTO
from bson import ObjectId


class ClienteDAO:

    def __init__(self):
        db = get_database()
        self.coleccion = db["clientes"]

    # ─────────────────────────────────────────
    #  CREATE
    # ─────────────────────────────────────────

    def insertar(self, cliente: ClienteDTO):
        data = cliente.to_dict()
        resultado = self.coleccion.insert_one(data)
        return str(resultado.inserted_id)

    def insertar_muchos(self, clientes: list):
        documentos = [c.to_dict() for c in clientes]
        resultado = self.coleccion.insert_many(documentos)
        return len(resultado.inserted_ids)

    # ─────────────────────────────────────────
    #  READ — básico
    # ─────────────────────────────────────────

    def obtener_todos(self):
        documentos = self.coleccion.find()
        return [ClienteDTO.from_dict(doc) for doc in documentos]

    def obtener_por_id(self, id):
        doc = self.coleccion.find_one({"_id": ObjectId(id)})
        return ClienteDTO.from_dict(doc) if doc else None

    def obtener_por_email(self, email):
        doc = self.coleccion.find_one({"email": email})
        return ClienteDTO.from_dict(doc) if doc else None

    # Búsqueda con operadores de comparación
    # opcion 1 → fecha_registro $gt valor (datetime)
    # opcion 2 → compras.precio  $gt valor (int)
    # opcion 3 → compras.categoria $in valor (list)
    def buscar_por_comparacion(self, opcion, valor):
        if opcion == 1:
            filtro = {"fecha_registro": {"$gt": valor}}
        elif opcion == 2:
            filtro = {"compras.precio": {"$gt": valor}}
        elif opcion == 3:
            filtro = {"compras.categoria": {"$in": valor}}
        else:
            return []

        documentos = self.coleccion.find(filtro)
        return [ClienteDTO.from_dict(doc) for doc in documentos]

    # ─────────────────────────────────────────
    #  READ — avanzado
    # ─────────────────────────────────────────

    # Búsqueda con expresión regular sobre cualquier campo de texto
    def buscar_por_regex(self, campo, patron):
        filtro = {campo: {"$regex": patron, "$options": "i"}}
        documentos = self.coleccion.find(filtro)
        return [ClienteDTO.from_dict(doc) for doc in documentos]

    # Búsqueda por rango de fechas
    # opcion 1 → fecha_registro entre desde y hasta
    # opcion 2 → compras.fecha_compra entre desde y hasta
    def buscar_por_rango_fechas(self, opcion, desde, hasta):
        if opcion == 1:
            filtro = {"fecha_registro": {"$gte": desde, "$lte": hasta}}
        elif opcion == 2:
            filtro = {"compras.fecha_compra": {"$gte": desde, "$lte": hasta}}
        else:
            return []

        documentos = self.coleccion.find(filtro)
        return [ClienteDTO.from_dict(doc) for doc in documentos]

    # Búsqueda dentro de subdocumento o array
    # Ejemplos de campo: "contacto.direccion.ciudad", "contacto.direccion.region", "compras.producto"
    def buscar_en_subdocumento(self, campo, valor):
        filtro = {campo: {"$regex": valor, "$options": "i"}}
        documentos = self.coleccion.find(filtro)
        return [ClienteDTO.from_dict(doc) for doc in documentos]

    # ─────────────────────────────────────────
    #  UPDATE — documento raíz
    # ─────────────────────────────────────────

    def actualizar_campo_raiz(self, email, campo, nuevo_valor):
        resultado = self.coleccion.update_one(
            {"email": email},
            {"$set": {campo: nuevo_valor}}
        )
        return resultado.modified_count > 0

    # ─────────────────────────────────────────
    #  UPDATE — subdocumento y array
    # ─────────────────────────────────────────

    # Actualiza un campo dentro del subdocumento contacto
    # Ejemplos de campo: "contacto.telefono", "contacto.direccion.ciudad"
    def actualizar_contacto(self, email, campo, nuevo_valor):
        resultado = self.coleccion.update_one(
            {"email": email},
            {"$set": {campo: nuevo_valor}}
        )
        return resultado.modified_count > 0

    # Agrega una compra al array usando $push
    def agregar_compra(self, email, compra: CompraDTO):
        resultado = self.coleccion.update_one(
            {"email": email},
            {"$push": {"compras": compra.to_dict()}}
        )
        return resultado.modified_count > 0

    # Elimina una compra del array usando $pull
    def eliminar_compra(self, email, producto):
        resultado = self.coleccion.update_one(
            {"email": email},
            {"$pull": {"compras": {"producto": {"$regex": producto, "$options": "i"}}}}
        )
        return resultado.modified_count > 0

    # ─────────────────────────────────────────
    #  DELETE
    # ─────────────────────────────────────────

    def eliminar(self, email):
        resultado = self.coleccion.delete_one({"email": email})
        return resultado.deleted_count > 0

    # ─────────────────────────────────────────
    #  UTILIDAD
    # ─────────────────────────────────────────

    def contar_documentos(self):
        return self.coleccion.count_documents({})