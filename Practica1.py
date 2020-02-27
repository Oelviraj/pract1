# coding=utf-8
import os
import time
import threading
import rrdtool
from getSNMP import consultaSNMP
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from getSNMP_2 import consultaSNMP2


def worker(num,comunidad,host):     # Los worker son los hilos
    namedb1 = "Multicast_recibidos_" + str(num)
    namedb2 = "IP_recibidos_" + str(num)
    namedb3 = "ICMP_enviados_" + str(num)
    namedb4 = "TCP_enviados_" + str(num)
    namedb5 = "UDP_recibidos_" + str(num)

    total_multicast = 0
    total_IP = 0
    total_ICMP = 0
    total_TCP = 0
    total_UDP = 0

    #SE CREAN LAS BASES DE DATOS

    ret = rrdtool.create(str(namedb1 + ".rrd"), "--start", 'N', "--step", '60', "DS:Multicast:COUNTER:600:U:U", "RRA:AVERAGE:0.5:6:700")
    if ret:
        print (rrdtool.error())

    ret = rrdtool.create(str(namedb2 + ".rrd"), "--start", 'N', "--step", '60', "DS:recibidosIP:COUNTER:600:U:U", "RRA:AVERAGE:0.5:6:700")
    if ret:
        print (rrdtool.error())

    ret = rrdtool.create(str(namedb3 + ".rrd"), "--start", 'N', "--step", '60',  "DS:enviadosICMP:COUNTER:600:U:U", "RRA:AVERAGE:0.5:6:700")
    if ret:
        print (rrdtool.error())

    ret = rrdtool.create(str(namedb4 + ".rrd"), "--start", 'N', "--step", '60', "DS:enviadosTCP:COUNTER:600:U:U", "RRA:AVERAGE:0.5:6:700")
    if ret:
        print (rrdtool.error())

    ret = rrdtool.create(str(namedb5 + ".rrd"), "--start", 'N', "--step", '60', "DS:enviadosUDP:COUNTER:600:U:U", "RRA:AVERAGE:0.5:6:700")
    if ret:
        print (rrdtool.error())

    while 1:
        total_multicast = int(consultaSNMP(comunidad, host, '1.3.6.1.2.1.2.2.1.18.2'))   #Paquetes multicast que ha enviado una interfaz
        valor = "N:" + str(total_multicast)
        #print (valor)
        rrdtool.update(str(namedb1 + ".rrd"), valor)
        rrdtool.dump(str(namedb1 + ".rrd"), str(namedb1 + ".xml"))


        total_IP = int(consultaSNMP(comunidad, host, '1.3.6.1.2.1.4.27.0')) #Paquetes Ipv4 que los protocolos locales de usuarios de IPv4 suministraron a IPv4 en las
                                                                            #solicitudes de transmisión.
        valor = "N:" + str(total_IP)
        #print (valor)
        rrdtool.update(str(namedb2 + ".rrd"), valor)
        rrdtool.dump(str(namedb2 + ".rrd"), str(namedb2 + ".xml"))


        total_ICMP = int(consultaSNMP(comunidad, host, '1.3.6.1.2.1.5.1.0')) #Mensajes ICMP que ha recibido el agente.
        valor = "N:" + str(total_ICMP)
        #print (valor)
        rrdtool.update(str(namedb3 + ".rrd"), valor)
        rrdtool.dump(str(namedb3 + ".rrd"), str(namedb3 + ".xml"))


        total_TCP = int(consultaSNMP(comunidad, host, '1.3.6.1.2.1.6.12.0')) # Segmentos retransmitidos; es decir, el número de segmentos TCP transmitidos que contienen
                                                                            #  uno o más octetos transmitidos previamente
        valor = "N:" + str(total_TCP)
        #print (valor)
        rrdtool.update(str(namedb4 + ".rrd"), valor)
        rrdtool.dump(str(namedb4 + ".rrd"), str(namedb4 + ".xml"))


        total_UDP = int(consultaSNMP(comunidad, host, '1.3.6.1.2.1.7.1.0')) #3) Datagramas enviados por el dispositivo.
        valor = "N:" + str(total_UDP)
        #print (valor)
        rrdtool.update(str(namedb5 + ".rrd"), valor)
        rrdtool.dump(str(namedb5 + ".rrd"), str(namedb5 + ".xml"))

        time.sleep(1)

    if ret:
        print (rrdtool.error())
        time.sleep(300)

    #print('Worker: %s' % num)
num_agentes = 0
resp = 'Y'
while resp != 'N':

    estatus_monitoreo = 0
    k = 0
    j = 0
    l = 0
    listaleida = []


    print("Ingrese un valor")

    print ("1: Comenzar el monitoreo")
    print ("2: Agregar un agente")
    print ("3: ELiminar un agente")
    print ("4: Generar reporte PDF\n")

    numero = int(input("Seleccione una opcion: "))

    f = open("Datos.txt", 'r')
    for linea in f.readlines():
        value = linea.rstrip('\n')
        listaleida.append(value)
        j = j + 1
    f.close()

    numdisp = int(j / 4)

    if numero == 1:
        os.system("clear")
        print ("Comenzando monitoreo\n")

        if numdisp != 0:
            print (" Dispositivos en monitoreo: ", numdisp)
            for k in range(numdisp):
                try:
                    name = str(consultaSNMP(listaleida[p + 2], listaleida[p], '1.3.6.1.2.1.1.1.0'))

                    if name == 'Hardware:':
                        name = "Windows"
                        _OID = '1.3.6.1.2.1.2.2.1.8.3' #OID para la interfaz en el mio es el 3
                    else: #Cuando name == Linux
                        _OID = '1.3.6.1.2.1.2.2.1.8.3' # En caso de Linux como es nuestra compu es wlan0, hay que buscar que numero tiene

                    print ("\nAgente " + str(k + 1) + " : " + name)

                    OperStatus = consultaSNMP(listaleida[p + 2], listaleida[p], _OID)

                    if OperStatus == '1':
                        status = 'up'
                    elif OperStatus == '2':
                        status = 'down'
                    elif OperStatus == '3':
                        status = 'testing'

                    print ("      Estatus del Monitoreo: ", status)

                    num_puertos = consultaSNMP(listaleida[p + 2], listaleida[p], '1.3.6.1.2.1.2.1.0')
                    print ("      Numero de puertos disponibles: ", num_puertos)

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
                    print ("\n   >Agente " + str(k + 1) + "   Status: down")
                p = p + 4

        else:
            print ("No hay Datos en el Registro! D:")
            time.sleep(1)

    elif numero == 2:
        os.system("clear")
        print ("Agregar un agente:\n")
        print (" Ingrese los siguientes datos\n")
        host    = str(input(" Dir IP"))
        version = int(input("Version SNMP"))
        namecom = str(input("Comunidad"))
        puerto  = int(input("Puerto"))

        lista = [host, version, namecom, puerto]

        f = open('Datos.txt', 'a')
        for i in lista:
            f.write(str(i))
            f.write("\n")
        f.close()

        num_agentes += 1

        threads = []
        t = threading.Thread(target=worker, args=(num_agentes,namecom,host))
        threads.append(t)
        t.start()



    elif numero == 3:
        os.system("clear")
        print ("Último agente eliminado!\n")

    elif numero == 4:
        os.system("clear")
        print ("Generando el reporte PDF con la información obtenida:\n")

    resp = str(input("\n Quieres volver al inicio? (Y/N)"))
    resp = resp.upper()
    os.system("clear")
