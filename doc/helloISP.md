# hello ISP

## Overall

使用Python实现一些简单的ISP pipeline处理过程，后续可以考虑使用RTL实现
算法实现力求简答，以理解原理为目标

## DPC

如下图，将bayer格式的RGB分量拆分出来看，并将G拆分为Gr和Gb，则R/Gr/Gb/B四周点的相对位置关系一致，采用当前点与四周不相邻的8个点做差，如果差值均大于预设阈值，则判定为坏点

![DPC](<helloISP-DPC.png>)

纠错可以通过配置选择2种模式：简单均值与方向均值

> Parameter

1. img: raw/uint16
2. thres: threshold
3. mode: 0 - simple mode; 1 - direction mode

> Return

img: raw/uint16

## Demosaicing

Bayer存在4种格式，需要分别处理。对于每个点，取以它为中心的3x3的矩阵来计算

![DMS](<helloISP-DMS.png>)

## CSC

## Histeq