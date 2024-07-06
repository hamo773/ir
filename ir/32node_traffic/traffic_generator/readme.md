## Traffic Generator
```
pyhon3 iperf3_scripts.py 
```
執行成功會依32Nodes_tms_info_24.pkl生成TM資料夾  
產生完TM資料夾後，將這些資料夾放入32nodos中

# Install

若想自己生成 .pkl 需要用到TMGEN套件 https://github.com/progwriter/TMgen  

此套件需要安裝在python2下，先執行pip install --upgrade setuptools  

接著按照github教學安裝tmgen

python package requirement
* numpy
* cython
* matplotlib
* statistics

```
python generate_tms.py
```

