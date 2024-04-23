 #!/bin/bash 
echo Generating traffic...
        
iperf3 -c 10.0.0.1 -p 19001 -u -b 3662.847k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.3 -p 19003 -u -b 2904.974k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.4 -p 19004 -u -b 2007.521k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.7 -p 19007 -u -b 376.293k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.8 -p 19008 -u -b 725.347k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.9 -p 19009 -u -b 702.435k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.11 -p 19011 -u -b 2195.947k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.14 -p 19014 -u -b 3871.512k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.15 -p 19015 -u -b 6.630k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.16 -p 19016 -u -b 536.253k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.17 -p 19017 -u -b 3228.038k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.20 -p 19020 -u -b 36.390k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.21 -p 19021 -u -b 2575.010k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.23 -p 19023 -u -b 1503.155k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.24 -p 19024 -u -b 331.944k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.25 -p 19025 -u -b 355.904k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.26 -p 19026 -u -b 671.516k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.27 -p 19027 -u -b 717.898k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.28 -p 19028 -u -b 1856.891k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.29 -p 19029 -u -b 1408.095k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.30 -p 19030 -u -b 1768.667k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.31 -p 19031 -u -b 272.587k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.32 -p 19032 -u -b 1950.992k -w 256k -t 80000 -i 0 &
sleep 0.4