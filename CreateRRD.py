#!/usr/bin/env python

import rrdtool
ret = rrdtool.create("Paq_unicast.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:Unicast_A1:COUNTER:600:U:U",
                     "DS:Unicast_A2:COUNTER:600:U:U",
                     "RRA:AVERAGE:0.5:6:700")
if ret:
    print (rrdtool.error())

import rrdtool
ret = rrdtool.create("Paq_rcvIP.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:ReciveIPV4_A1:COUNTER:600:U:U",
                     "DS:ReciveIPV4_A2:COUNTER:600:U:U",
                     "RRA:AVERAGE:0.5:6:700")
if ret:
    print (rrdtool.error())

import rrdtool
ret = rrdtool.create("ICMP_echo.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:ICMP_echo_A1:COUNTER:600:U:U",
                     "DS:ICMP_Echo_A2:COUNTER:600:U:U",
                     "RRA:AVERAGE:0.5:6:700")
if ret:
    print (rrdtool.error())

import rrdtool
ret = rrdtool.create("Seg_rcv.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:Seg_recv_A1:COUNTER:600:U:U",
                     "DS:Seg_recv_A2:COUNTER:600:U:U",
                     "RRA:AVERAGE:0.5:6:700")
if ret:
    print (rrdtool.error())

import rrdtool
ret = rrdtool.create("Data_UDP.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:Data_UDP_A1:COUNTER:600:U:U",
                     "DS:Data_UDP_A2:COUNTER:600:U:U",
                     "RRA:AVERAGE:0.5:6:700")
if ret:
    print (rrdtool.error())