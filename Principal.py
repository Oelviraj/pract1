# coding=utf-8
import os
import time
from getSNMP import consultaSNMP
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from getSNMP_2 import consultaSNMP2

resp = 'Y'
while resp != 'N':

    estatus_monitoreo = 0
    k = 0
    j = 0
    l = 0
    listaleida = []

    print("**************************************************************")
    print("*                         Práctica 1                         *")
    print("*           Adquisición de información usando SNMP           *")
    print("*               González Ledesma Carla Daniela               *")
    print("**************************************************************\n")

    print "    1.- Inicio"
    print "    2.- Agregar Agente"
    print "    3.- Eliminar Agente"
    print "    4.- Generar Reporte\n"

    numero = input("Seleccione una opcion: ")

    f = open("Datos.txt", 'r')
    for linea in f.readlines():
        value = linea.rstrip('\n')
        listaleida.append(value)
        j = j + 1
    f.close()

    numdisp = j / 4

    if numero == 1:
        os.system ("clear")
        print "\n****************************************************"
        print "*                    = Inicio =                    *"
        print "****************************************************\n"

        if numdisp != 0:
            print " Dispositivos en monitoreo: ", numdisp
            # Ahora ya sabiendo el numero de dispositivos que hay, obtendremos su informacion
            p = 0
            for k in range(2):
                try:
                    name = str(consultaSNMP(listaleida[p + 2], listaleida[p], '1.3.6.1.2.1.1.1.0'))
                    if name == 'Hardware:':
                        name = "Windows"
                    print ("\n   >Agente " + str(k + 1) + " : " + name)

                    if name == 'Windows':
                        _OID = '1.3.6.1.2.1.2.2.1.8.3'
                    else:
                        _OID = '1.3.6.1.2.1.2.2.1.8.2'

                    OperStatus = consultaSNMP(listaleida[p + 2], listaleida[p], _OID)

                    if OperStatus == '1':
                        status = 'up'
                    elif OperStatus == '2':
                        status = 'down'
                    elif OperStatus == '3':
                        status = 'testing'

                    print "    Estatus del Monitoreo: ", status
                    num_puertos = consultaSNMP(listaleida[p + 2], listaleida[p], '1.3.6.1.2.1.2.1.0')
                    print "    Numero de puertos disponibles: ", num_puertos

                    for puertosh in range(int(num_puertos)):
                        num = puertosh + 1
                        _OID = "1.3.6.1.2.1.2.2.1.8." + str(num)
                        OperStatus = consultaSNMP(listaleida[p + 2], listaleida[p], _OID)

                        if OperStatus == '1':
                            status = 'up'
                        elif OperStatus == '2':
                            status = 'down'
                        elif OperStatus == '3':
                            status = 'testing'

                        print ("        Puerto " + str(num) + " : " + status)
                except:
                    print ("\n   >Agente "+str(k+1)+"   Status: down")
                p = p + 4

        else :
            print ("No hay Datos en el Registro! D:")
            time.sleep(1)
            print ("Presione [Y] para regresar al Menú")



    elif numero == 2:
        os.system ("clear")
        print "\n ****************************************"
        print " *          = Agregar Agente =          *"
        print " ****************************************\n"
        print " Ingrese los siguientes datos\n"
        host = raw_input("  > Host o direccion IP: ")
        version = input("  > Version SNMP: ")
        namecom = raw_input("  > Nombre de la Comunidad: ")
        puerto = input("  > Puerto: ")

        lista = [host, version, namecom, puerto]

        time.sleep(2)
        print "\n Los datos se agregaron exitosamente! :D\n"

        f = open('Datos.txt', 'a')
        for i in lista:
            f.write(str(i))
            f.write("\n")
        f.close()

    elif numero == 3:
        os.system ("clear")
        print "\n *****************************************"
        print " *          = Eliminar Agente =          *"
        print " *****************************************\n"

        print " Agentes registrados: "

        for i in range(numdisp):
            print "\n  >Agente ", i + 1
            for k in range(4):
                print "    ", listaleida[l]
                l = l + 1

        delete_agente = input("\n Seleccione el numero de Agente que quiere eliminar: ")
        delete = (delete_agente - 1) * 4
        m = 0
        for m in range(4):
            listaleida.pop(delete)
        # print listaleida

        f = open('Datos.txt', 'w')
        for i in listaleida:
            f.write(str(i))
            f.write("\n")
        f.close()
        time.sleep(2)
        print "\n Agente eliminado Exitosamente! :D\n"
    elif numero == 4:
        os.system("clear")
        print "\n *****************************************"
        print " *       = Generacion de Reporte =       *"
        print " *****************************************\n"
        numero = input("Seleccione el Agente: ")
        p = (numero-1)*4

        name = str(consultaSNMP(listaleida[p + 2], listaleida[p], '1.3.6.1.2.1.1.1.0'))
        if name == 'Hardware:':
            urlImg = "/home/scarlett/Documentos/wn-logo.jpg"
        else :
            urlImg = "/home/scarlett/Documentos/ub-logo.png"

        doc = SimpleDocTemplate("Reporte.pdf", pagesize=letter,
                                rightMargin=50, leftMargin=50,
                                topMargin=20, bottomMargin=18)

        Story = []
        logotipo = urlImg

        nombreAgente = str(consultaSNMP2(listaleida[p + 2], listaleida[p], '1.3.6.1.2.1.1.1.0'))
        numeroPuertos = str(consultaSNMP(listaleida[p + 2], listaleida[p], '1.3.6.1.2.1.2.1.0'))
        MILISEG = int(consultaSNMP(listaleida[p + 2], listaleida[p], '1.3.6.1.2.1.1.3.0')) / 1000
        SEG = MILISEG / 60
        ultimoReinicio = str(SEG)
        comunidad = listaleida[p + 2]
        ip = listaleida[p]

        imagen = Image(logotipo, 1 * inch, 1 * inch)
        Story.append(imagen)

        Story.append(Spacer(1, 8))

        estilos = getSampleStyleSheet()
        estilos.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

        name = nombreAgente.split()
        Agente = " "
        q = 0
        for desde in name:
            if (q > 1):
                Agente = Agente + " " + desde
            q = q + 1

        texto = ' %s' % Agente
        Story.append(Paragraph(texto, estilos["Justify"]))

        Story.append(Spacer(1, 2))

        texto = ">> Número de puertos: %s" % numeroPuertos
        Story.append(Paragraph(texto, estilos["Normal"]))

        Story.append(Spacer(1, 2))

        texto = ">> Tiempo de Actividad desde el último reinicio: %s" % ultimoReinicio + " minutos"
        Story.append(Paragraph(texto, estilos["Justify"]))

        Story.append(Spacer(1, 2))

        texto = ">> Comunidad: %s" % comunidad
        Story.append(Paragraph(texto, estilos["Normal"]))

        Story.append(Spacer(1, 2))

        texto = ">> Dirección IP: %s" % ip
        Story.append(Paragraph(texto, estilos["Normal"]))

        Story.append(Spacer(1, 12))

        texto = 'Paquetes unicast que ha recibido la interfaz'
        Story.append(Paragraph(texto, estilos["Normal"]))
        Story.append(Spacer(1, 4))

        if(numero == 1):
            unicastimg = '/home/scarlett/Documentos/P1_Final/venv/Paquetes_UnicastA1.png'
            IPv4img = '/home/scarlett/Documentos/P1_Final/venv/Paquetes_IPv4A1.png'
            ICMP_echoimg = '/home/scarlett/Documentos/P1_Final/venv/ICMP_echoA1.png'
            Seg_recvimg =  '/home/scarlett/Documentos/P1_Final/venv/Segmentos_recvA1.png'
            Datagramasimg = '/home/scarlett/Documentos/P1_Final/venv/Datagramas_entregadosA1.png'
        elif numero ==2:
            unicastimg = '/home/scarlett/Documentos/P1_Final/venv/Paquetes_UnicastA2.png'
            IPv4img = '/home/scarlett/Documentos/P1_Final/venv/Paquetes_IPv4A2.png'
            ICMP_echoimg = '/home/scarlett/Documentos/P1_Final/venv/ICMP_echoA2.png'
            Seg_recvimg = '/home/scarlett/Documentos/P1_Final/venv/Segmentos_recvA2.png'
            Datagramasimg = '/home/scarlett/Documentos/P1_Final/venv/Datagramas_entregadosA2.png'

        img = Image(unicastimg, 497/2, 173/2)
        Story.append(img)

        Story.append(Spacer(1, 8))

        texto = 'Paquetes recibidos a protocolos IPv4, incluyendo los que tienen errores'
        Story.append(Paragraph(texto, estilos["Normal"]))
        Story.append(Spacer(1, 4))

        img = Image(IPv4img, 497/2, 173/2)
        Story.append(img)

        Story.append(Spacer(1, 8))

        texto = 'Mensajes ICMP echo que ha enviado el agente'

        Story.append(Paragraph(texto, estilos["Normal"]))
        Story.append(Spacer(1, 4))

        img = Image(ICMP_echoimg, 497/2, 173/2)
        Story.append(img)

        Story.append(Spacer(1, 8))
        texto = 'Segmentos recibidos, incluyendo los que se han recibido con errores'
        Story.append(Paragraph(texto, estilos["Normal"]))
        Story.append(Spacer(1, 4))

        img = Image(Seg_recvimg, 497/2, 173/2)
        Story.append(img)

        Story.append(Spacer(1, 8))
        texto = 'Datagramas entregados a usuarios UDP'
        Story.append(Paragraph(texto, estilos["Normal"]))
        Story.append(Spacer(1, 4))

        img = Image(Datagramasimg, 497/2, 173/2)
        Story.append(img)

        Story.append(Spacer(1, 8))

        doc.build(Story)

        print ("\n Su reporte ha sido generado exitosamente! :D ")

    resp = raw_input("\n\n                   ¿Regresar al Menú?[Y/N] ")
    resp = resp.upper()
    os.system("clear")