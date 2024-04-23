 #!/bin/bash 
echo Generating traffic...
        
iperf3 -c 10.0.0.1 -p 30001 -u -b 4536.056k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.4 -p 30004 -u -b 2486.107k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.7 -p 30007 -u -b 466.000k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.8 -p 30008 -u -b 898.267k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.9 -p 30009 -u -b 869.892k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.11 -p 30011 -u -b 2719.452k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.12 -p 30012 -u -b 549.106k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.13 -p 30013 -u -b 699.191k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.16 -p 30016 -u -b 664.094k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.17 -p 30017 -u -b 3997.590k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.19 -p 30019 -u -b 1506.486k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.20 -p 30020 -u -b 45.065k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.21 -p 30021 -u -b 3188.883k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.23 -p 30023 -u -b 1861.502k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.24 -p 30024 -u -b 411.078k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.27 -p 30027 -u -b 889.043k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.28 -p 30028 -u -b 2299.567k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.32 -p 30032 -u -b 2416.101k -w 256k -t 80000 -i 0 &
sleep 0.4