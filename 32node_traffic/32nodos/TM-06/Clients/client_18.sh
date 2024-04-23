 #!/bin/bash 
echo Generating traffic...
        
iperf3 -c 10.0.0.1 -p 18001 -u -b 11739.293k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.2 -p 18002 -u -b 9526.576k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.3 -p 18003 -u -b 9310.337k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.7 -p 18007 -u -b 1206.006k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.8 -p 18008 -u -b 2324.712k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.10 -p 18010 -u -b 10623.967k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.11 -p 18011 -u -b 7037.931k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.12 -p 18012 -u -b 1421.084k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.13 -p 18013 -u -b 1809.502k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.14 -p 18014 -u -b 12408.056k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.15 -p 18015 -u -b 21.249k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.17 -p 18017 -u -b 10345.745k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.19 -p 18019 -u -b 3898.780k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.20 -p 18020 -u -b 116.629k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.21 -p 18021 -u -b 8252.815k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.24 -p 18024 -u -b 1063.868k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.26 -p 18026 -u -b 2152.184k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.29 -p 18029 -u -b 4512.895k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.30 -p 18030 -u -b 5668.513k -w 256k -t 80000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.32 -p 18032 -u -b 6252.860k -w 256k -t 80000 -i 0 &
sleep 0.4