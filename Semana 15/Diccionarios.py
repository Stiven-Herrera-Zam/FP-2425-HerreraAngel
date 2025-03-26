#DICCIONARIO.

informacion_personal = {"Nombre":"Angel","Edad": 18,"Ciudad":"Coca","Profesion":"Ingeniero"}
print("Diccionario Inicial:", informacion_personal)

#ACCEDER Y MODIFICAR VALORES.

informacion_personal["Ciudad"] = "Tena"
informacion_personal["Profesion"] = "Dentista"
print("Despues de Modificar Valores:", informacion_personal)

#VERIFICAR EXISTENCIA DE CLAVES.

if "Telefono" not in informacion_personal:
    informacion_personal["Telefono"] = "0969078632"
print("Despues de Verificar clave Telefono:", informacion_personal)
#ELIMiNAR UNA CLAVE.

informacion_personal.pop("Edad", None)
print("Despues de Eliminar Edad:", informacion_personal)