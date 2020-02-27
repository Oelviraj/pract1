import sys
import rrdtool
import time
tiempo_actual = int(time.time())
tiempo_final = tiempo_actual - 86400
tiempo_inicial = tiempo_actual - 600
while 1:
    ret = rrdtool.graph( "Paquetes_UnicastA1.png",
                     "--start",str(tiempo_inicial),
#                     "--end","N",
                     "--vertical-label=Bytes/s",
                     "--title=Paquetes unicast",
                     "DEF:entrada=Paq_unicast.rrd:Unicast_A1:AVERAGE",
                     "AREA:entrada#00FF00:In Unicast")

    ret = rrdtool.graph("Paquetes_UnicastA2.png",
                        "--start", str(tiempo_inicial),
                        #                     "--end","N",
                        "--vertical-label=Bytes/s",
                        "--title=Paquetes unicast",
                        "DEF:entrada=Paq_unicast.rrd:Unicast_A2:AVERAGE",
                        "LINE1:entrada#00FFFF:In Unicast")


    ret = rrdtool.graph("Paquetes_IPv4A1.png",
                        "--start", str(tiempo_inicial),
#                       "--end","N",
                        "--vertical-label=Bytes/s",
                        "--title=Paquetes recibidos IPv4",
                        "DEF:entrada=Paq_rcvIP.rrd:ReciveIPV4_A1:AVERAGE",
                        "AREA:entrada#00FF00:In IPv4")

    ret = rrdtool.graph("Paquetes_IPv4A2.png",
                        "--start", str(tiempo_inicial),
                        #                       "--end","N",
                        "--vertical-label=Bytes/s",
                        "--title=Paquetes recibidos IPv4",
                        "DEF:entrada=Paq_rcvIP.rrd:ReciveIPV4_A2:AVERAGE",
                        "LINE1:entrada#00FFFF:In IPv4")

    ret = rrdtool.graph("ICMP_echoA1.png",
                        "--start", str(tiempo_inicial),
                        #                       "--end","N",
                        "--vertical-label=Bytes/s",
                        "--title=Mensajes ICMP echo enviados",
                        "DEF:entrada=ICMP_echo.rrd:ICMP_echo_A1:AVERAGE",
                        "AREA:entrada#00FF00:Mensajes echo")

    ret = rrdtool.graph("ICMP_echoA2.png",
                        "--start", str(tiempo_inicial),
                        #                       "--end","N",
                        "--vertical-label=Bytes/s",
                        "--title=Mensajes ICMP echo enviados",
                        "DEF:entrada=ICMP_echo.rrd:ICMP_Echo_A2:AVERAGE",
                        "LINE1:entrada#00FFFF:Mensajes echo")

    ret = rrdtool.graph("Segmentos_recvA1.png",
                        "--start", str(tiempo_inicial),
                        #                       "--end","N",
                        "--vertical-label=Bytes/s",
                        "--title=Segmentos recibidos",
                        "DEF:entrada=Seg_rcv.rrd:Seg_recv_A1:AVERAGE",
                        "AREA:entrada#00FF00:Segmentos recibidos")

    ret = rrdtool.graph("Segmentos_recvA2.png",
                        "--start", str(tiempo_inicial),
                        #                       "--end","N",
                        "--vertical-label=Bytes/s",
                        "--title=Segmentos recibidos",
                        "DEF:entrada=Seg_rcv.rrd:Seg_recv_A2:AVERAGE",
                        "LINE1:entrada#00FFFF:recibidos echo")

    ret = rrdtool.graph("Datagramas_entregadosA1.png",
                        "--start", str(tiempo_inicial),
                        #                       "--end","N",
                        "--vertical-label=Bytes/s",
                        "--title=Datagramas UDP enviados",
                        "DEF:entrada=Data_UDP.rrd:Data_UDP_A1:AVERAGE",
                        "AREA:entrada#00FF00:UDPs enviados")

    ret = rrdtool.graph("Datagramas_entregadosA2.png",
                        "--start", str(tiempo_inicial),
                        #                       "--end","N",
                        "--vertical-label=Bytes/s",
                        "--title=Datagramas UDP enviados",
                        "DEF:entrada=Data_UDP.rrd:Data_UDP_A2:AVERAGE",
                        "LINE1:entrada#00FFFF:UDPs enviados")

    time.sleep(30)