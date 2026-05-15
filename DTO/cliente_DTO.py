from datetime import datetime


# ─────────────────────────────────────────
#  DireccionDTO  (parte del subdocumento contacto)
# ─────────────────────────────────────────

class DireccionDTO:
    def __init__(self, calle=None, ciudad=None, region=None):
        self.__calle  = calle
        self.__ciudad = ciudad
        self.__region = region

    # GETTERS
    def get_calle(self):
        return self.__calle

    def get_ciudad(self):
        return self.__ciudad

    def get_region(self):
        return self.__region

    # SETTERS
    def set_calle(self, calle):
        self.__calle = calle

    def set_ciudad(self, ciudad):
        self.__ciudad = ciudad

    def set_region(self, region):
        self.__region = region

    def to_dict(self):
        return {
            "calle" : self.__calle,
            "ciudad": self.__ciudad,
            "region": self.__region
        }

    @staticmethod
    def from_dict(data: dict):
        return DireccionDTO(
            calle  = data.get("calle"),
            ciudad = data.get("ciudad"),
            region = data.get("region")
        )

    def __str__(self):
        return f"{self.__calle}, {self.__ciudad}, {self.__region}"


# ─────────────────────────────────────────
#  ContactoDTO  (subdocumento del cliente)
# ─────────────────────────────────────────

class ContactoDTO:
    def __init__(self, telefono=None, direccion: DireccionDTO = None):
        self.__telefono  = telefono
        self.__direccion = direccion

    # GETTERS
    def get_telefono(self):
        return self.__telefono

    def get_direccion(self):
        return self.__direccion

    # SETTERS
    def set_telefono(self, telefono):
        self.__telefono = telefono

    def set_direccion(self, direccion: DireccionDTO):
        self.__direccion = direccion

    def to_dict(self):
        return {
            "telefono" : self.__telefono,
            "direccion": self.__direccion.to_dict() if self.__direccion else {}
        }

    @staticmethod
    def from_dict(data: dict):
        return ContactoDTO(
            telefono  = data.get("telefono"),
            direccion = DireccionDTO.from_dict(data.get("direccion", {}))
        )

    def __str__(self):
        return f"Tel: {self.__telefono} | Dir: {self.__direccion}"


# ─────────────────────────────────────────
#  CompraDTO  (elemento del array de compras)
# ─────────────────────────────────────────

class CompraDTO:
    def __init__(self, producto=None, categoria=None,
                 precio=0, cantidad=1, fecha_compra=None):
        self.__producto     = producto
        self.__categoria    = categoria
        self.__precio       = precio
        self.__cantidad     = cantidad
        self.__fecha_compra = fecha_compra

    # GETTERS
    def get_producto(self):
        return self.__producto

    def get_categoria(self):
        return self.__categoria

    def get_precio(self):
        return self.__precio

    def get_cantidad(self):
        return self.__cantidad

    def get_fecha_compra(self):
        return self.__fecha_compra

    # SETTERS
    def set_producto(self, producto):
        self.__producto = producto

    def set_categoria(self, categoria):
        self.__categoria = categoria

    def set_precio(self, precio):
        self.__precio = precio

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_fecha_compra(self, fecha_compra):
        self.__fecha_compra = fecha_compra

    def to_dict(self):
        return {
            "producto"    : self.__producto,
            "categoria"   : self.__categoria,
            "precio"      : self.__precio,
            "cantidad"    : self.__cantidad,
            "fecha_compra": self.__fecha_compra
        }

    @staticmethod
    def from_dict(data: dict):
        return CompraDTO(
            producto     = data.get("producto"),
            categoria    = data.get("categoria"),
            precio       = data.get("precio", 0),
            cantidad     = data.get("cantidad", 1),
            fecha_compra = data.get("fecha_compra")
        )

    def __str__(self):
        fecha = self.__fecha_compra.strftime("%d/%m/%Y") if self.__fecha_compra else "-"
        return (f"{self.__producto} | {self.__categoria} | "
                f"${self.__precio:,} x{self.__cantidad} | {fecha}")


# ─────────────────────────────────────────
#  ClienteDTO  (documento principal)
# ─────────────────────────────────────────

class ClienteDTO:
    def __init__(self, id=None, nombre=None, email=None,
                 fecha_registro=None, contacto: ContactoDTO = None,
                 compras: list = None):
        self.__id             = id
        self.__nombre         = nombre
        self.__email          = email
        self.__fecha_registro = fecha_registro
        self.__contacto       = contacto
        self.__compras        = compras if compras is not None else []

    # GETTERS
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_email(self):
        return self.__email

    def get_fecha_registro(self):
        return self.__fecha_registro

    def get_contacto(self):
        return self.__contacto

    def get_compras(self):
        return self.__compras

    # SETTERS
    def set_id(self, id):
        self.__id = id

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_email(self, email):
        self.__email = email

    def set_fecha_registro(self, fecha_registro):
        self.__fecha_registro = fecha_registro

    def set_contacto(self, contacto: ContactoDTO):
        self.__contacto = contacto

    def set_compras(self, compras: list):
        self.__compras = compras

    def to_dict(self):
        return {
            "nombre"         : self.__nombre,
            "email"          : self.__email,
            "fecha_registro" : self.__fecha_registro,
            "contacto"       : self.__contacto.to_dict() if self.__contacto else {},
            "compras"        : [c.to_dict() for c in self.__compras]
        }

    @staticmethod
    def from_dict(data: dict):
        compras = [CompraDTO.from_dict(c) for c in data.get("compras", [])]
        return ClienteDTO(
            id             = str(data.get("_id", "")),
            nombre         = data.get("nombre"),
            email          = data.get("email"),
            fecha_registro = data.get("fecha_registro"),
            contacto       = ContactoDTO.from_dict(data.get("contacto", {})),
            compras        = compras
        )

    def __str__(self):
        fecha = self.__fecha_registro.strftime("%d/%m/%Y") if self.__fecha_registro else "-"
        return f"{self.__nombre} | {self.__email} | Registro: {fecha}"