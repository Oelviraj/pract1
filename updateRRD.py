import time
import rrdtool
from getSNMP import consultaSNMP

total_paq_unicastA1 = 0
total_paq_recv_IPA1 = 0
total_output_echoA1 = 0
total_InsegsA1 = 0
total_output_datagramsA1 = 0
total_paq_unicastA2 = 0
total_paq_recv_IPA2 = 0
total_output_echoA2 = 0
total_InsegsA2 = 0
total_output_datagramsA2 = 0
j=0
lista = []
f = open("Datos.txt", 'r')
for linea in f.readlines():
    value = linea.rstrip('\n')
    lista.append(value)
    j = j + 1
f.close()
p=0
while 1:
    total_paq_unicastA1 =int(consultaSNMP(lista[p + 2], lista[p], '1.3.6.1.2.1.2.2.1.11.3'))
    total_paq_unicastA2 = int(consultaSNMP(lista[p + 6], lista[p+4], '1.3.6.1.2.1.2.2.1.11.2'))

    valor = "N:" + str(total_paq_unicastA1) + ':' + str(total_paq_unicastA2)
    print (valor)
    rrdtool.update('Paq_unicast.rrd', valor)
    rrdtool.dump('Paq_unicast.rrd', 'Paq_unicast.xml')

    total_paq_recv_IPA1 = int(consultaSNMP(lista[p + 2], lista[p], '1.3.6.1.2.1.4.3.0'))
    total_paq_recv_IPA2 = int(consultaSNMP(lista[p + 6], lista[p+4], '1.3.6.1.2.1.4.3.0'))

    valor = "N:" + str(total_paq_recv_IPA1) + ':' + str(total_paq_recv_IPA2)
    print (valor)
    rrdtool.update('Paq_rcvIP.rrd', valor)
    rrdtool.dump('Paq_rcvIP.rrd', 'Paq_rcvIP.xml')

    total_output_echoA1 = int(consultaSNMP(lista[p + 2], lista[p], '1.3.6.1.2.1.5.21.0'))
    total_output_echoA2 = int(consultaSNMP(lista[p + 6], lista[p+4], '1.3.6.1.2.1.5.21.0'))

    valor = "N:" + str(total_output_echoA1) + ':' + str(total_output_echoA2)
    print (valor)
    rrdtool.update('ICMP_echo.rrd', valor)
    rrdtool.dump('ICMP_echo.rrd', 'ICMP_echo.xml')

    total_InsegsA1 = int(consultaSNMP(lista[p + 2], lista[p], '1.3.6.1.2.1.6.10.0'))
    total_InsegsA2= int(consultaSNMP(lista[p + 6],lista[p+4], '1.3.6.1.2.1.6.10.0'))

    valor = "N:" + str(total_output_datagramsA1) + ':' + str(total_output_datagramsA2)
    print (valor)
    rrdtool.update('Seg_rcv.rrd', valor)
    rrdtool.dump('Seg_rcv.rrd', 'Seg_rcv.xml')

    total_output_datagramsA1 = int(consultaSNMP(lista[p + 2], lista[p], '1.3.6.1.2.1.7.1.0'))
    total_output_datagramsA2 = int(consultaSNMP(lista[p + 6],lista[p+4], '1.3.6.1.2.1.7.1.0'))

    valor = "N:" + str(total_InsegsA1) + ':' + str(total_InsegsA2)
    print (valor)
    rrdtool.update('Data_UDP.rrd', valor)
    rrdtool.dump('Data_UDP.rrd', 'Data_UDP.xml')


    time.sleep(1)

if ret:
    print (rrdtool.error())
    time.sleep(300)