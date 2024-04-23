 #!/bin/bash 
echo Generating traffic...
        
iperf3 -c 10.0.0.4 -p 7004 -u -b 3436.867k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.6 -p 7006 -u -b 5874.860k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.8 -p 7008 -u -b 5725.792k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.10 -p 7010 -u -b 356.580k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.11 -p 7011 -u -b 5728.305k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.13 -p 7013 -u -b 7043.955k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.14 -p 7014 -u -b 7044.148k -w 256k -t 50000 -i 0 &
sleep 0.4