 #!/bin/bash 
echo Generating traffic...
        
iperf3 -c 10.0.0.1 -p 12001 -u -b 5981.383k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.2 -p 12002 -u -b 154.158k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.3 -p 12003 -u -b 88.051k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.7 -p 12007 -u -b 6988.261k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.8 -p 12008 -u -b 5753.032k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.9 -p 12009 -u -b 7307.826k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.10 -p 12010 -u -b 358.277k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.13 -p 12013 -u -b 7077.467k -w 256k -t 50000 -i 0 &
sleep 0.4