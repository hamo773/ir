 #!/bin/bash 
echo Generating traffic...
        
iperf3 -c 10.0.0.1 -p 6001 -u -b 7956.972k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.2 -p 6002 -u -b 6457.177k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.3 -p 6003 -u -b 6310.609k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.5 -p 6005 -u -b 2517.109k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.7 -p 6007 -u -b 817.439k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.8 -p 6008 -u -b 1575.705k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.9 -p 6009 -u -b 1525.931k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.10 -p 6010 -u -b 7200.996k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.12 -p 6012 -u -b 963.220k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.13 -p 6013 -u -b 1226.493k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.14 -p 6014 -u -b 8410.264k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.16 -p 6016 -u -b 1164.927k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.17 -p 6017 -u -b 7012.415k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.18 -p 6018 -u -b 8469.500k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.19 -p 6019 -u -b 2642.619k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.20 -p 6020 -u -b 79.052k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.21 -p 6021 -u -b 5593.814k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.22 -p 6022 -u -b 3957.365k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.25 -p 6025 -u -b 773.147k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.26 -p 6026 -u -b 1458.765k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.27 -p 6027 -u -b 1559.524k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.28 -p 6028 -u -b 4033.811k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.29 -p 6029 -u -b 3058.871k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.30 -p 6030 -u -b 3842.156k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.31 -p 6031 -u -b 592.152k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.32 -p 6032 -u -b 4238.231k -w 256k -t 80000 -i 0 &
sleep 0.4