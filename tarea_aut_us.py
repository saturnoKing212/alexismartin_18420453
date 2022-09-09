#alexis martin hernandez silva 18420453
import bcrypt

def validarus(us, passs):
    regist = passus()
    alum= estudiantes()
    valida = {}
    for r in regist:
        if r[0] == us:
            for est in alum:
                if est[0]==us:
                    ban = bcrypt.checkpw(passs.encode('utf-8'), r[2].encode('utf-8'))
                    valida["Ban"] = ban
                    valida["Us"] = est[1]
                    if ban:
                        valida["Msj"] = "autententificate"
                    else:
                        valida["Msj"] = "incorrecto"
                    return valida
    valida["Ban"] = False
    valida["Us"] = ""
    valida["Msj"] = "No hay coincidencias"
    return valida

print(validarus("18420453", "1GVF3xLk0F"))
