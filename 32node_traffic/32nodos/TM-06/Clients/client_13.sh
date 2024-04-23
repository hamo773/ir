 #!/bin/bash 
echo Generating traffic...
        
iperf3 -c 10.0.0.2 -p 13002 -u -b 1379.571k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.3 -p 13003 -u -b 1348.257k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.4 -p 13004 -u -b 931.731k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.5 -p 13005 -u -b 537.778k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.6 -p 13006 -u -b 1226.493k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.7 -p 13007 -u -b 174.645k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.8 -p 13008 -u -b 336.648k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.10 -p 13010 -u -b 1538.487k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.11 -p 13011 -u -b 1019.183k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.12 -p 13012 -u -b 205.791k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.14 -p 13014 -u -b 1796.846k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.15 -p 13015 -u -b 3.077k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.16 -p 13016 -u -b 248.886k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.17 -p 13017 -u -b 1498.197k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.18 -p 13018 -u -b 1809.502k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.19 -p 13019 -u -b 564.594k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.22 -p 13022 -u -b 845.488k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.23 -p 13023 -u -b 697.645k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.24 -p 13024 -u -b 154.062k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.26 -p 13026 -u -b 311.664k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.27 -p 13027 -u -b 333.191k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.30 -p 13030 -u -b 820.874k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.31 -p 13031 -u -b 126.513k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.32 -p 13032 -u -b 905.495k -w 256k -t 80000 -i 0 &
sleep 0.4