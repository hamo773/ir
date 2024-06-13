 #!/bin/bash 
echo Generating traffic...
        
iperf3 -c 10.0.0.2 -p 6002 -u -b 129.597k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.3 -p 6003 -u -b 74.022k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.4 -p 6004 -u -b 2903.035k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.7 -p 6007 -u -b 5874.860k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.9 -p 6009 -u -b 6143.510k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.12 -p 6012 -u -b 7050.969k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.13 -p 6013 -u -b 5949.852k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.14 -p 6014 -u -b 5950.015k -w 256k -t 50000 -i 0 &
sleep 0.4