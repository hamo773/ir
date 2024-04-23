 #!/bin/bash 
echo Generating traffic...
        
iperf3 -c 10.0.0.1 -p 29001 -u -b 5087.759k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.2 -p 29002 -u -b 4128.777k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.3 -p 29003 -u -b 4035.060k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.4 -p 29004 -u -b 2788.482k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.5 -p 29005 -u -b 1609.462k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.6 -p 29006 -u -b 3670.645k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.8 -p 29008 -u -b 1007.520k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.10 -p 29010 -u -b 4604.382k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.11 -p 29011 -u -b 3050.209k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.13 -p 29013 -u -b 784.230k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.16 -p 29016 -u -b 744.865k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.17 -p 29017 -u -b 4483.801k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.18 -p 29018 -u -b 5415.474k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.20 -p 29020 -u -b 50.547k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.22 -p 29022 -u -b 2530.375k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.24 -p 29024 -u -b 461.076k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.25 -p 29025 -u -b 494.357k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.26 -p 29026 -u -b 932.747k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.27 -p 29027 -u -b 997.173k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.30 -p 29030 -u -b 2456.709k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.31 -p 29031 -u -b 378.627k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.32 -p 29032 -u -b 2709.963k -w 256k -t 80000 -i 0 &
sleep 0.4