import reflex as rx

class Client(rx.Base):

    id: int
    fecha_ingreso: str 
    nombre: str 
    apellido: str
    documento: int 
    plan: str 
    observaciones: str 
    
    def to_dict(self):
        return {"id": self.id,
                "fecha_ingreso": self.fecha_ingreso,
                "nombre": self.nombre,
                "apellido": self.apellido,
                "documento": self.documento,
                "plan": self.plan,
                "observaciones": self.observaciones}

