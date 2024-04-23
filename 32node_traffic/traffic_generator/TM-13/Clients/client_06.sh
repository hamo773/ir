 #!/bin/bash 
echo Generating traffic...
        
iperf3 -c 10.0.0.2 -p 6002 -u -b 93.045k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.3 -p 6003 -u -b 53.145k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.4 -p 6004 -u -b 2084.257k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.7 -p 6007 -u -b 4217.901k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.9 -p 6009 -u -b 4410.781k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.12 -p 6012 -u -b 5062.298k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.13 -p 6013 -u -b 4271.743k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.14 -p 6014 -u -b 4271.860k -w 256k -t 50000 -i 0 &
sleep 0.4