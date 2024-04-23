 #!/bin/bash 
echo Generating traffic...
        
iperf3 -c 10.0.0.1 -p 13001 -u -b 5825.978k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.3 -p 13003 -u -b 85.763k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.4 -p 13004 -u -b 3363.498k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.5 -p 13005 -u -b 3793.733k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.7 -p 13007 -u -b 6806.696k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.8 -p 13008 -u -b 5603.560k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.9 -p 13009 -u -b 7117.958k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.11 -p 13011 -u -b 5606.019k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.14 -p 13014 -u -b 6893.772k -w 256k -t 50000 -i 0 &
sleep 0.4