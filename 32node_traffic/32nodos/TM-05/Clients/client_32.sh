 #!/bin/bash 
echo Generating traffic...
        
iperf3 -c 10.0.0.1 -p 32001 -u -b 5307.747k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.2 -p 32002 -u -b 4307.300k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.3 -p 32003 -u -b 4209.530k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.4 -p 32004 -u -b 2909.052k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.5 -p 32005 -u -b 1679.053k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.6 -p 32006 -u -b 3829.358k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.7 -p 32007 -u -b 545.277k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.8 -p 32008 -u -b 1051.084k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.9 -p 32009 -u -b 1017.882k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.10 -p 32010 -u -b 4803.469k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.12 -p 32012 -u -b 642.522k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.13 -p 32013 -u -b 818.139k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.14 -p 32014 -u -b 5610.118k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.15 -p 32015 -u -b 9.607k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.16 -p 32016 -u -b 777.072k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.18 -p 32018 -u -b 5649.632k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.20 -p 32020 -u -b 52.732k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.22 -p 32022 -u -b 2639.785k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.23 -p 32023 -u -b 2178.188k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.26 -p 32026 -u -b 973.078k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.29 -p 32029 -u -b 2040.438k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.31 -p 32031 -u -b 394.999k -w 256k -t 80000 -i 0 &
sleep 0.4