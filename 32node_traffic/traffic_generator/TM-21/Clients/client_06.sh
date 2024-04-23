 #!/bin/bash 
echo Generating traffic...
        
iperf3 -c 10.0.0.2 -p 6002 -u -b 102.839k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.3 -p 6003 -u -b 58.739k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.4 -p 6004 -u -b 2303.648k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.7 -p 6007 -u -b 4661.882k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.9 -p 6009 -u -b 4875.064k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.12 -p 6012 -u -b 5595.161k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.13 -p 6013 -u -b 4721.391k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.14 -p 6014 -u -b 4721.520k -w 256k -t 50000 -i 0 &
sleep 0.4