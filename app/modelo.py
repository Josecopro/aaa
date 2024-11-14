from abc import  ABC, abstractmethod
from  dataclasses import dataclass, field
from errores import DestinoInalcanzableError
from datos import distancias


@dataclass
class Transporte(ABC):
    id_transporte: str
    capacidad_maxima: int
    ubicacion_actual: str 

    def GetValidPlaces(self):
        ValidPlaces = []
        for Places in  distancias:
            if Places[0] not in ValidPlaces:
                ValidPlaces.append(Places[0])
            if  Places[1] not in ValidPlaces:
                ValidPlaces.append(Places[1])
        print(ValidPlaces)


    @abstractmethod
    def estimar_tiempo_entrega(self, distancia_total: float) -> float:
        pass


    def calcular_ruta(self, destinos: list[str]) -> dict:
        Places = []
        Places.append(self.ubicacion_actual)
        for Place in destinos:
            Places.append(Place)

        for i in range(destinos):
            if Places[i] not in destinos:
                raise  DestinoInalcanzableError()

        for i in Places: 
            CurrentCheck = (Places(i),  Places(i+1))
            CurrentDistance =  distancias(CurrentCheck)
            TotalDistance += CurrentDistance

        return {
            "ruta": Places,
            "distancia_total": TotalDistance
        }

    def generar_reporte(self, ruta: dict, archivo: str):
        ruta = self.calcular_ruta()
        with  open(archivo, "w") as archivo:
            a =  f"Reporte de Transporte\n----------------------\nID del Transporte: {self.id_transporte}\nCapacidad Máxima: {self.capacidad_maxima} kg\n Ubicación Actual: {self.ubicacion_actual} \n Ruta Calculada: {ruta['ruta']} Distancia Total: {ruta['TotalDistance']} km "
            archivo.write(a)

@dataclass
class Camion(Transporte):
    velocidad_promedio: int
    peajes: int

    def estimar_tiempo_entrega(self, distancia_total: float) -> float:
        tiempo_estimado = distancia_total / self.Velocidad_promedio
        tiempo_estimado += (10/60) * self.peajes


@dataclass
class Avion(Transporte):
    velocidad_promedio: int
    horas_descanso: int

    def estimar_tiempo_entrega(self, distancia_total: float) -> float:

        tiempo_estimado = distancia_total / self.Velocidad_promedio
        CheckRest = tiempo_estimado // 5
        tiempo_estimado += (CheckRest * self.horas_descanso) + tiempo_estimado

