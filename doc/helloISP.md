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

> Parameter

1. img: raw/uint16
2. pattern: rggb/bggr/grbg/gbrg

> Return

img: rgb/uint8

## Gamma

鉴于人眼对于亮度的非线性特性，即对暗光下的亮度变化更为敏感，对原始图像进行gamma矫正可以得到更好的显示效果

![GAC](<Figure_gamma.png>)

一个常见的gamma值为2.2，即

$y=x*1^{(1/2.2)}$

> Parameter

1. img: rgb/uint8

> Return

img: rgb/uint8

## CSC

根据ITU BT.601规范，Y(luminance)可由如下计算公式得到

$Y = 0.299R + 0.587G + 0.114B$

U(Cb)和V(Cr)分别为蓝色和红色与Y的差值

$U = B - Y = -0.299R -0.587G + 0.886B$

$V = R - Y = 0.701R -0.587G -0.114B$

当RGB的取值范围定义为[0,1]时，Y的取值范围同样为[0,1]，但是相应U的取值范围为[-0.886,0.886]，V的取值范围为[-0.701,0.701]，为了将UV的取值范围同样限定在[0,1]，得到新的计算过公式为

$U = (B-Y)/1.772+0.5 = -0.16874R-0.33126G+0.5B+0.5$

$V = (R-Y)/1.402+0.5 = 0.5R-0.41869R-0.08131B+0.5$

> Parameter

1. img: rgb/uint8
2. mode: rgb2yuv

> Return

img: yuv/uint8

## Histeq

直方图均衡适合用在灰度图上，可以增加对比度以显示更多细节。其过程为，先做直方图统计，即统计[0,255]每个值对应像素的个数，然后统计累计个数，除以总的像素个数，并乘上255得到一个映射表，将原图的像素值做映射后便可以得到一个像素分布于[0,255]的新的灰度图

> Parameter

1. img: gray/uint8

> Return

img: gray/uint8