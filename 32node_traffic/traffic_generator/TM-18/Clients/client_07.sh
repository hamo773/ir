 #!/bin/bash 
echo Generating traffic...
        
iperf3 -c 10.0.0.4 -p 7004 -u -b 2896.960k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.6 -p 7006 -u -b 4951.961k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.8 -p 7008 -u -b 4826.311k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.10 -p 7010 -u -b 300.564k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.11 -p 7011 -u -b 4828.429k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.13 -p 7013 -u -b 5937.400k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.14 -p 7014 -u -b 5937.563k -w 256k -t 50000 -i 0 &
sleep 0.4