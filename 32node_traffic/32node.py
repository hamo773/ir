﻿from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import Link, Intf, TCLink
import subprocess
import time
import os

def Test_topo():
    net = Mininet(controller=RemoteController,link=TCLink)

    info("*** Add Controller ***\n")
    #net.addController("c0",controller=RemoteController,ip='192.168.72.3')
    net.addController("c0",controller=RemoteController,ip='127.0.0.1')

    info("*** Add Switch ***\n")
    s1 = net.addSwitch("s1")
    s2 = net.addSwitch("s2")
    s3 = net.addSwitch("s3")
    s4 = net.addSwitch("s4")
    s5 = net.addSwitch("s5")
    s6 = net.addSwitch("s6")
    s7 = net.addSwitch("s7")
    s8 = net.addSwitch("s8")
    s9 = net.addSwitch("s9")
    s10 = net.addSwitch("s10")
    s11 = net.addSwitch("s11")
    s12 = net.addSwitch("s12")
    s13 = net.addSwitch("s13")
    s14 = net.addSwitch("s14")
    s15 = net.addSwitch("s15")
    s16 = net.addSwitch("s16")
    s17 = net.addSwitch("s17")
    s18 = net.addSwitch("s18")
    s19 = net.addSwitch("s19")
    s20 = net.addSwitch("s20")
    s21 = net.addSwitch("s21")
    s22 = net.addSwitch("s22")
    s23 = net.addSwitch("s23")
    s24 = net.addSwitch("s24")
    s25 = net.addSwitch("s25")
    s26 = net.addSwitch("s26")
    s27 = net.addSwitch("s27")
    s28 = net.addSwitch("s28")
    s29 = net.addSwitch("s29")
    s30 = net.addSwitch("s30")
    s31 = net.addSwitch("s31")
    s32 = net.addSwitch("s32")
    

    info("*** Add Host ***\n")
    h1 = net.addHost("h1",mac="00:00:00:00:00:01")
    h2 = net.addHost("h2",mac="00:00:00:00:00:02")
    h3 = net.addHost("h3",mac="00:00:00:00:00:03")
    h4 = net.addHost("h4",mac="00:00:00:00:00:04")
    h5 = net.addHost("h5",mac="00:00:00:00:00:05")
    h6 = net.addHost("h6",mac="00:00:00:00:00:06")
    h7 = net.addHost("h7",mac="00:00:00:00:00:07")
    h8 = net.addHost("h8",mac="00:00:00:00:00:08")
    h9 = net.addHost("h9",mac="00:00:00:00:00:09")
    h10 = net.addHost("h10",mac="00:00:00:00:00:10")
    h11 = net.addHost("h11",mac="00:00:00:00:00:11")
    h12 = net.addHost("h12",mac="00:00:00:00:00:12")
    h13 = net.addHost("h13",mac="00:00:00:00:00:13")
    h14 = net.addHost("h14",mac="00:00:00:00:00:14")
    h15 = net.addHost("h15",mac="00:00:00:00:00:15")
    h16 = net.addHost("h16",mac="00:00:00:00:00:16")
    h17 = net.addHost("h17",mac="00:00:00:00:00:17")
    h18 = net.addHost("h18",mac="00:00:00:00:00:18")
    h19 = net.addHost("h19",mac="00:00:00:00:00:19")
    h20 = net.addHost("h20",mac="00:00:00:00:00:20")
    h21 = net.addHost("h21",mac="00:00:00:00:00:21")
    h22 = net.addHost("h22",mac="00:00:00:00:00:22")
    h23 = net.addHost("h23",mac="00:00:00:00:00:23")
    h24 = net.addHost("h24",mac="00:00:00:00:00:24")
    h25 = net.addHost("h25",mac="00:00:00:00:00:25")
    h26 = net.addHost("h26",mac="00:00:00:00:00:26")
    h27 = net.addHost("h27",mac="00:00:00:00:00:27")
    h28 = net.addHost("h28",mac="00:00:00:00:00:28")
    h29 = net.addHost("h29",mac="00:00:00:00:00:29")
    h30 = net.addHost("h30",mac="00:00:00:00:00:30")
    h31 = net.addHost("h31",mac="00:00:00:00:00:31")
    h32 = net.addHost("h32",mac="00:00:00:00:00:32")

    info("*** Add Link ***\n")
    net.addLink(s1,h1)
    net.addLink(s2,h2)
    net.addLink(s3,h3)
    net.addLink(s4,h4)
    net.addLink(s5,h5)
    net.addLink(s6,h6)
    net.addLink(s7,h7)
    net.addLink(s8,h8)
    net.addLink(s9,h9)
    net.addLink(s10,h10)
    net.addLink(s11,h11)
    net.addLink(s12,h12)
    net.addLink(s13,h13)
    net.addLink(s14,h14)
    net.addLink(s15,h15)
    net.addLink(s16,h16)
    net.addLink(s17,h17)
    net.addLink(s18,h18)
    net.addLink(s19,h19)
    net.addLink(s20,h20)
    net.addLink(s21,h21)
    net.addLink(s22,h22)
    net.addLink(s23,h23)
    net.addLink(s24,h24)
    net.addLink(s25,h25)
    net.addLink(s26,h26)
    net.addLink(s27,h27)
    net.addLink(s28,h28)
    net.addLink(s29,h29)
    net.addLink(s30,h30)
    net.addLink(s31,h31)
    net.addLink(s32,h32)


    """net.addLink(s1,s3,bw=100)
    net.addLink(s1,s7,bw=100)
    net.addLink(s1,s8,bw=100)
    net.addLink(s1,s10,bw=100)
    net.addLink(s1,s12,bw=100)
    net.addLink(s1,s30,bw=100)
    net.addLink(s2,s17,bw=100)
    net.addLink(s2,s3,bw=100)
    net.addLink(s2,s4,bw=100)
    net.addLink(s2,s21,bw=100)
    net.addLink(s2,s22,bw=25)
    net.addLink(s2,s31,bw=25)
    net.addLink(s2,s28,bw=100)
    net.addLink(s2,s5,bw=100)
    net.addLink(s3,s32,bw=25)
    net.addLink(s3,s4,bw=25)
    net.addLink(s3,s5,bw=1.55)
    net.addLink(s3,s6,bw=100)
    net.addLink(s3,s7,bw=25)
    net.addLink(s3,s12,bw=1.55)
    net.addLink(s3,s13,bw=100)
    net.addLink(s3,s15,bw=25)
    net.addLink(s3,s20,bw=1.55)
    net.addLink(s3,s27,bw=100)
    net.addLink(s3,s31,bw=100)
    net.addLink(s4,s16,bw=100)
    net.addLink(s4,s17,bw=100)
    net.addLink(s4,s11,bw=100)
    net.addLink(s4,s14,bw=100)
    net.addLink(s4,s16,bw=100)
    net.addLink(s5,s16,bw=25)
    net.addLink(s5,s6,bw=25)
    net.addLink(s5,s9,bw=25)
    net.addLink(s5,s10,bw=25)
    net.addLink(s5,s11,bw=25)
    net.addLink(s5,s15,bw=25)
    net.addLink(s6,s19,bw=1.55)
    net.addLink(s6,s23,bw=1.55)
    net.addLink(s6,s8,bw=1.55)
    net.addLink(s6,s27,bw=1.55)
    net.addLink(s7,s9,bw=100)
    net.addLink(s8,s18,bw=25)
    net.addLink(s10,s29,bw=25)
    net.addLink(s11,s29,bw=100)
    net.addLink(s11,s13,bw=100)
    net.addLink(s13,s14,bw=1.55)
    net.addLink(s13,s22,bw=100)
    net.addLink(s14,s24,bw=100)
    net.addLink(s14,s20,bw=100)
    net.addLink(s14,s21,bw=100)
    net.addLink(s15,s19,bw=25)
    net.addLink(s15,s18,bw=25)
    net.addLink(s15,s26,bw=25)
    net.addLink(s15,s28,bw=25)
    net.addLink(s16,s25,bw=25)
    net.addLink(s16,s23,bw=25)
    net.addLink(s19,s24,bw=25)
    net.addLink(s19,s25,bw=25)
    net.addLink(s20,s26,bw=25)
    net.addLink(s22,s32,bw=25)
    net.addLink(s26,s30,bw=25)"""

    links = set()
    with open('bw_r.txt', 'r') as file:
        for line in file:
            data = line.strip().split(',')
            src, dst,_, bw = map(int, data)  # 只取前三个数字
            link = (src, dst)
            reverse_link = (dst, src)

            # 添加节点
            src_host = ('s{}'.format(src))
            dst_host = ('s{}'.format(dst))

            # 添加链路，确保不重复添加
            if link not in links and reverse_link not in links:
                net.addLink(src_host, dst_host, bw=bw)
                links.add(link)



    info("*** Network Start ***\n")
    net.start()
    return net

def set_cpu_affinity():
    cpu_list = "0-2"  
    pid = os.getpid()
    subprocess.call(["taskset", "-cp", cpu_list, str(pid)])

def generate(net):

    print("enter TM")
    input_ = input()
    print("################################################")
    for i in range(1,33):
        if i < 10:
            net.get('h'+str(i)).popen('sh 32nodos/TM-'+input_+'/Servers/server_0'+str(i)+'.sh')
            #net.get('h'+str(i)).subprocess.Popen(['sh 23nodos/TM-'+input_+'/Servers/server_0'+str(i)+'.sh'],preexec_fn=set_cpu_affinity)
            #subprocess.Popen(["command_to_execute"], preexec_fn=set_cpu_affinity)
            #print(i)
        else:
            net.get('h'+str(i)).popen('sh 32nodos/TM-'+input_+'/Servers/server_'+str(i)+'.sh')
    time.sleep(10)
    for i in range(1,33):
        if i < 10:
            net.get('h'+str(i)).popen('sh 32nodos/TM-'+input_+'/Clients/client_0'+str(i)+'.sh')
        else:
            net.get('h'+str(i)).popen('sh 32nodos/TM-'+input_+'/Clients/client_'+str(i)+'.sh')


def train(net):
    #tm_list = ['00','01','03','05','07','08','09','10','12','13','15','17','19','21','23']
    #tm_list = ['00','01','02','04','07','08','09','11','13','15','17','19','20','22','23']
    tm_list = ['00','01','03','05','07','09','10','11','12','14','16','18','20','22']
    for tm in tm_list:
        print("################################################")
        print(tm)
        for i in range(1,33):
            #print(i)
            if i < 10:
                net.get('h'+str(i)).popen('sh 32nodos/TM-'+tm+'/Servers/server_0'+str(i)+'.sh')
            else:
                net.get('h'+str(i)).popen('sh 32nodos/TM-'+tm+'/Servers/server_'+str(i)+'.sh')
        time.sleep(10)
        for i in range(1,33):
            if i < 10:
                net.get('h'+str(i)).popen('sh 32nodos/TM-'+tm+'/Clients/client_0'+str(i)+'.sh')
            else:
                net.get('h'+str(i)).popen('sh 32nodos/TM-'+tm+'/Clients/client_'+str(i)+'.sh')
        #time.sleep(720)
        #time.sleep(360)
        time.sleep(2150)
        #time.sleep(1430)
        os.popen("sudo killall -p iperf3")
        time.sleep(2)
        print("next TM")

if __name__ == "__main__":
    setLogLevel("info")
    net = Test_topo()

    #num_links = len(net.links)
    #print(f'Total number of links: {num_links}')

    while 1:
        input_ = input('CLI/TRA/TEST/KILL/QUIT')
        if input_.upper() == 'CLI':
            CLI(net)
        elif input_.upper() == 'TRA':
            train(net)
        elif input_.upper() == 'TEST':
            generate(net)
        elif input_.upper() == 'KILL':
            os.system('sudo killall -9 iperf3')
        elif input_.upper() == 'QUIT':
            net.stop()
            break
