 #!/bin/bash 
echo Generating traffic...
        
iperf3 -c 10.0.0.4 -p 7004 -u -b 2317.568k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.6 -p 7006 -u -b 3961.569k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.8 -p 7008 -u -b 3861.049k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.10 -p 7010 -u -b 240.451k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.11 -p 7011 -u -b 3862.743k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.13 -p 7013 -u -b 4749.920k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.14 -p 7014 -u -b 4750.050k -w 256k -t 50000 -i 0 &
sleep 0.4