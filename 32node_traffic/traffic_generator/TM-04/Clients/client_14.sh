 #!/bin/bash 
echo Generating traffic...
        
iperf3 -c 10.0.0.1 -p 14001 -u -b 5826.137k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.3 -p 14003 -u -b 85.765k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.6 -p 14006 -u -b 5749.602k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.7 -p 14007 -u -b 6806.882k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.9 -p 14009 -u -b 7118.153k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.10 -p 14010 -u -b 348.978k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.11 -p 14011 -u -b 5606.172k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.12 -p 14012 -u -b 8169.576k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.13 -p 14013 -u -b 6893.772k -w 256k -t 50000 -i 0 &
sleep 0.4