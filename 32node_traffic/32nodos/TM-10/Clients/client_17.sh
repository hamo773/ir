 #!/bin/bash 
echo Generating traffic...
        
iperf3 -c 10.0.0.3 -p 17003 -u -b 9250.315k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.4 -p 17004 -u -b 6392.554k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.5 -p 17005 -u -b 3689.668k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.6 -p 17006 -u -b 8414.899k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.8 -p 17008 -u -b 2309.725k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.9 -p 17009 -u -b 2236.764k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.10 -p 17010 -u -b 10555.476k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.11 -p 17011 -u -b 6992.559k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.12 -p 17012 -u -b 1411.922k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.13 -p 17013 -u -b 1797.837k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.14 -p 17014 -u -b 12328.063k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.15 -p 17015 -u -b 21.112k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.18 -p 17018 -u -b 12414.894k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.19 -p 17019 -u -b 3873.645k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.21 -p 17021 -u -b 8199.611k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.22 -p 17022 -u -b 5800.847k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.24 -p 17024 -u -b 1057.009k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.25 -p 17025 -u -b 1133.306k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.26 -p 17026 -u -b 2138.309k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.29 -p 17029 -u -b 4483.801k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.31 -p 17031 -u -b 867.998k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.32 -p 17032 -u -b 6212.549k -w 256k -t 80000 -i 0 &
sleep 0.4