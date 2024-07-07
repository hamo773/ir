
使用python 3.8.10
### 安裝mininet
```
git clone https://github.com/mininet/mininet 
```
成功下載下來後會有一個mininet資料夾
```
cd mininet
git tag  # list available versions
git checkout -b 2.3.1b1
cd util 
./install.sh -a
```


安裝完後可以進入terminal確認有無正確安裝
```
sudo mn
```

### 安裝ryu
```
git clone https://github.com/faucetsdn/ryu
```
進入ryu/ryu/topology
```
cd ryu/ryu/topology
```
需對switches.py做出一些修改
```
class PortData(object):
    def __init__(self, is_down, lldp_data):
        super(PortData, self).__init__()
        self.is_down = is_down
        self.lldp_data = lldp_data
        self.timestamp = None
        self.sent = 0
```
在後面在增加一行code
```
class PortData(object):
    def __init__(self, is_down, lldp_data):
        super(PortData, self).__init__()
        self.is_down = is_down
        self.lldp_data = lldp_data
        self.timestamp = None
        self.sent = 0
        self.delay = 0
```
lldp_packet_in_handler
```
@set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
def lldp_packet_in_handler(self, ev):
    if not self.link_discovery:
        return

    msg = ev.msg
    try:
        src_dpid, src_port_no = LLDPPacket.lldp_parse(msg.data)
    except LLDPPacket.LLDPUnknownFormat:
        # This handler can receive all the packets which can be
        # not-LLDP packet. Ignore it silently
        return

    dst_dpid = msg.datapath.id
    if msg.datapath.ofproto.OFP_VERSION == ofproto_v1_0.OFP_VERSION:
        dst_port_no = msg.in_port
    elif msg.datapath.ofproto.OFP_VERSION >= ofproto_v1_2.OFP_VERSION:
        dst_port_no = msg.match['in_port']
    else:
        LOG.error('cannot accept LLDP. unsupported version. %x',
                  msg.datapath.ofproto.OFP_VERSION)

    src = self._get_port(src_dpid, src_port_no)
    if not src or src.dpid == dst_dpid:
        return
```
修改為
```
@set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
def lldp_packet_in_handler(self, ev):
    recv_timestamp = time.time()   #加這一行
    if not self.link_discovery:
        return

    msg = ev.msg
    try:
        src_dpid, src_port_no = LLDPPacket.lldp_parse(msg.data)
    except LLDPPacket.LLDPUnknownFormat:
        # This handler can receive all the packets which can be
        # not-LLDP packet. Ignore it silently
        return

    dst_dpid = msg.datapath.id
    if msg.datapath.ofproto.OFP_VERSION == ofproto_v1_0.OFP_VERSION:
        dst_port_no = msg.in_port
    elif msg.datapath.ofproto.OFP_VERSION >= ofproto_v1_2.OFP_VERSION:
        dst_port_no = msg.match['in_port']
    else:
        LOG.error('cannot accept LLDP. unsupported version. %x',
                  msg.datapath.ofproto.OFP_VERSION)

    #加下面這段
    for port in self.ports.keys():
        if src_dpid == port.dpid and src_port_no == port.port_no:
            send_timestamp = self.ports[port].timestamp
            if send_timestamp:
                self.ports[port].delay = recv_timestamp - send_timestamp
    src = self._get_port(src_dpid, src_port_no)
    if not src or src.dpid == dst_dpid:
        return
```
執行完上述動作後，回到ryu資料夾進行安裝
```
cd ryu
python3 setup.py install
pip3 install .
```
結束ryu controller的安裝 可以在terminal確認有無正確安裝
```
ryu-manager
```
## 安裝ir
```
sudo apt install iperf3
```
```
git clone https://github.com/hamo773/ir
```
```
cd ir
pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/cu118
pip install -r requirements.txt
```
開始訓練前須先生成流量腳本，請參考github上32node_traffic內的readme

進入ir/32node_traffic，執行32node.py，創建mininet拓撲
```
cd ir/32node_traffic
sudo python3 32node.py
```
成功執行後，會有5個選項可以選擇

* CLI
進入mininet command line介面
* TRA
產生training所需要的流量
* GEN
使用TM-XX(00、01.....)資料產生網路流量
*  KILL
結束所有iperf3的process
*  QUIT
結束mininet

開啟第2個terminal，執行controller
```
cd ir/ps_dqn_a/ours_32node/
ryu-manager --observe-link simple_monitor.py
```
當controller成功啟動後，就可以開始在mininet環境傳輸流量，在mininet的terminal中輸入tra。
當訓練流量開始後在第三個terminal執行我們的agent
```
python3 myDRL.py 
```
輸入1讓DRL agent進行轉發路徑的學習
當訓練完成後，可以輸入2進行效能測試模式
