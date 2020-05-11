Title: 使用Masscan、Nmap、ELK做内网资产收集
Date: 2018-07-16 03:20
Modified: 2018-07-16 03:20
Category: 安全
Tags: Nmap
Slug: O2
Authors: nJcx
Summary: 使用Masscan、Nmap、ELK做内网资产收集~

#### 安装


安装masscan

```bash

# yum install git gcc make libpcap-devel

#git clone https://github.com/robertdavidgraham/masscan
# cd masscan
# make

# cp bin/masscan  /bin

```

安装最新nmap 7.8

```bash

wget https://nmap.org/dist/nmap-7.80-1.x86_64.rpm

rpm -ivh nmap-7.80-1.x86_64.rpm

```

安装es 和 kibana

```bash
docker run -d --name es -p 127.0.0.1:9201:9200 -p 9300:9300 -e ES_JAVA_OPTS="-Xms2G -Xmx2G" -e "discovery.type=single-node"  docker.elastic.co/elasticsearch/elasticsearch-oss:7.1.1   

docker run --name kibana -d -p 5601:5601 -e ELASTICSEARCH_HOSTS=http://127.0.0.1:9201   docker.elastic.co/kibana/kibana-oss:7.1.1   

```

大致逻辑就是，
1，使用 Masscan 做主机存活扫描
2，然后使用Nmap扫描上面存活的主机，导出xml
3，格式化xml，写入es，然后kibana做可视化

上代码

```python

from elasticsearch import Elasticsearch
from settings import es_ip, es_port, ip_list
from utils import Logger
import xmltodict
import os
import threading
import time
import json

logger = Logger.get_logger(__name__, path=os.getcwd())
es = Elasticsearch([{'host': es_ip, 'port': es_port}])


def xml_to_json(path):
    try:
        with open(path, 'r') as load_f:
            temp_ = xmltodict.parse(load_f).get("nmaprun")
            return {key: temp_[key]
                    for key in temp_
                    if key not in ["verbose", 'scaninfo', 'taskbegin', 'taskend', "debugging"]}

    except Exception as e:
        logger.error(str(e)+path)
        return {}


def json_to_es(index, json_):
    try:
        es.index(index=index, doc_type="vuln", body=json_)
    except Exception as e:
        try:
            es.index(index=index + '_', doc_type="vuln", body=json.dumps(json_))
        except Exception as e:
            try:
                es.index(index=index + '__', doc_type="vuln", body=json.dumps(json_))
            except Exception as e:
                logger.error(str(e))
                pass


def masscan_scan(ip):
    try:
        if ip:
            if not os.path.exists('tmp'):
                os.makedirs('tmp')
            os.system('masscan --ping {0} --rate 1000 -oL tmp/{1}.txt'.format(ip, ip.split('/')[0]))
    except Exception as e:
        logger.error(str(e))


def nmap_scan(ip):
    try:
        if ip:
            if not os.path.exists('report'):
                os.makedirs('report')
            os.system('nmap -sV -Pn -A -T5 --script=nmap-vulners/vulners.nse -oX report/{0}.xml {1}'.format(ip, ip))
    except Exception as e:
        logger.error(str(e))


def masscan_scan_worker():

    t_obj = []
    for i in range(len(ip_list)):
        t = threading.Thread(target=masscan_scan, args=(ip_list[i],))
        t_obj.append(t)
        t.start()
    for t in t_obj:
        t.join()
    if not os.path.exists('alive_host'):
        os.makedirs('alive_host')
    cmd = """ awk '{print $4}' tmp/*.txt | tr -s '\n' > alive_host/host.txt """
    os.system(cmd)
    os.system("""rm -f tmp/*.txt""")


def read_txt(path):
    lines = []
    try:
        with open(path, 'r') as file_to_read:
            while True:
                line = file_to_read.readline()
                if not line:
                    break
                line = line.strip('\n')
                lines.append(line)
    except Exception as e:
        logger.error(str(e))
    return lines


def nmap_scan_worker():
    lst = read_txt('alive_host/host.txt')
    tmp_ = [lst[i:i+5] for i in range(0, len(lst), 5)]
    print tmp_
    if tmp_:
        for list_ in tmp_:
            t_obj = []
            for i in range(len(list_)):
                t = threading.Thread(target=nmap_scan, args=(list_[i],))
                t_obj.append(t)
                t.start()
            for t in t_obj:
                t.join()


def nmap_to_es(index):
        if os.path.exists('report'):
            files = os.listdir('report')
        for file in files:
                json_to_es(index, xml_to_json('report'+'/'+file))
        os.system("""rm -f report/*.xml""")


if __name__ == '__main__':

    while True:
        now = time.strftime('%Y-%m-%d')
        masscan_scan_worker()
        nmap_scan_worker()
        es.indices.delete('nmap-*')
        nmap_to_es('nmap-' + now)

```


完整代码

```bash
https://github.com/njcx/nmap_to_es.git
```


![icmp](../images/kibana.png)