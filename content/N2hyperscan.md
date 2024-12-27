Title: CentOS7.5 下正则引擎Hyperscan安装
Date: 2018-07-16 20:20
Modified: 2018-07-16 20:20
Category: 安全
Tags: Hyperscan
Slug: N2
Authors: nJcx
Summary:  Centos7.5 下正则引擎Hyperscan安装~
Status: draft

#### 安装



``` bash


# yum groupinstall development tools

# yum install ragel
 

# git clone https://github.com/intel/hyperscan.git
# mkdir -p hyperscan/build
# cd hyperscan/build
# git checkout v5.1.1

# wget https://dl.bintray.com/boostorg/release/1.71.0/source/boost_1_71_0.tar.bz2

# tar -jxvf boost_1_71_0.tar.bz2 
# cp -r boost_1_71_0/boost ../../include/

# cmake \
    -G "Unix Makefiles" \
    -DCMAKE_INSTALL_PREFIX:PATH=/usr \
    -DBUILD_SHARED_LIBS=ON ../
# make
# make install

# pip install hyperscan(好像不需要上面那一堆，尴尬)

```