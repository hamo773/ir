 #!/bin/bash 
echo Generating traffic...
        
iperf3 -c 10.0.0.1 -p 15001 -u -b 17.966k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.2 -p 15002 -u -b 14.580k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.3 -p 15003 -u -b 14.249k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.4 -p 15004 -u -b 9.847k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.5 -p 15005 -u -b 5.683k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.6 -p 15006 -u -b 12.962k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.7 -p 15007 -u -b 1.846k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.9 -p 15009 -u -b 3.445k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.10 -p 15010 -u -b 16.259k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.11 -p 15011 -u -b 10.771k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.13 -p 15013 -u -b 2.769k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.14 -p 15014 -u -b 18.990k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.16 -p 15016 -u -b 2.630k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.17 -p 15017 -u -b 15.834k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.18 -p 15018 -u -b 19.124k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.19 -p 15019 -u -b 5.967k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.20 -p 15020 -u -b 0.178k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.21 -p 15021 -u -b 12.631k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.22 -p 15022 -u -b 8.936k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.23 -p 15023 -u -b 7.373k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.24 -p 15024 -u -b 1.628k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.25 -p 15025 -u -b 1.746k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.26 -p 15026 -u -b 3.294k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.28 -p 15028 -u -b 9.108k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.30 -p 15030 -u -b 8.675k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.31 -p 15031 -u -b 1.337k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.32 -p 15032 -u -b 9.570k -w 256k -t 80000 -i 0 &
sleep 0.4