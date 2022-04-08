# Lazada-VS-Shopee 
Compare a search item based on popularity on both platforms

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
Its common to check on multiple platforms before making an online purchase. I made this for myself for items I have already purchased before (recurring purchases like coffee) as an efficient way to do a quick lookup on both platforms. I ranked the output based on popularity as I find that metric to be what I would use for this use case. On Lazada, popularity is based on ratings while on Shopee, it is based on number of items sold. Selenium was used to webscrape selected elements into resepctive lists. Pandas was used to compile all data and add a ranking system for the final output.
	
## Technologies
Project is created with:
* Webscraping with Selenium via Chrome webdriver
* Pandas for data management and display
* Variable handling
	
## Setup
Install the required modules, then run the project. I'll show my search as follows.
```
Enter item to compare: nescafe coffee 3 in 1
```
Then, wait for the ranked output as follows.
```
                                            Item Name   Price  Source  Rank
0   NESCAFE 25% Less Sugar 3in1 Instant Coffee x32...    6.15  Lazada   1.0
1   (Bundle of 3) Old Town Hazelnut 3 in 1 White C...   20.90  Shopee   1.0
2   NESCAFE Original 3 In 1 Brown Sugar 30s Instan...    6.15  Lazada   2.0
3    Killiney 3-in-1 Premium White Coffee Trio Bundle   27.93  Shopee   2.0
4   Ceo Cafe 4 In 1 3 In 1 Premix Coffee With Gano...   20.99  Shopee   3.0
5   NESCAFE 25% Less Sugar 3in1 32Sachets Instant ...    6.15  Lazada   3.5
6   (2 Pack Bundle) NESCAFE 25% Less Sugar 3in1 32...   12.00  Lazada   3.5
7   G7 ( Original - local packaging )50 sticks 3 i...  100.90  Shopee   4.0
8   NESTLE Nescafe Gold Decaf 100G X 12 (GLASS) - ...   79.90  Lazada   5.0
9   NESCAFE Blend & Brew MILD 3 in 1 Instant Coffe...    3.33  Shopee   5.0
10    Nescafe 3 in 1 Instant Coffee - Original 35x19g    9.90  Shopee   6.0
11  (2 Pack Bundle) NESCAFE Original 3in1 Brown Su...   12.00  Lazada   6.5
12        Nescafe Blend and brew original 3in1 28x19g    7.90  Lazada   6.5
13  Nescafe 3 In 1 Mild Blend & Brew Premix Coffee...   45.90  Shopee   7.0
14  (Bundle of 3) Nescafe Original Low Fat 3 in 1 ...   18.30  Shopee   8.0
15  Nescafe Blend & Brew Original – 3 in 1 Coffee ...   19.90  Shopee   9.0
16  Nescafe 3 in 1 Original 35x19g Special Promo P...   12.55  Shopee  10.0
17  NESCAFE KOPI O 2 IN 1 24 PACK X 15 STICKS X 16...   10.99  Shopee  11.0
18  [Nescafe] Decaf Coffee Decaffeinated Coffee De...    5.90  Shopee  12.0
19  [Mix and Match] Cold Brew Coffee Concentrate b...   28.80  Shopee  13.0
20  Nescafé Blend & Brew Original 3 in 1 Premix Co...   13.39  Shopee  14.0
21  Wholesales 12 Pkt/ 24 Pkt Nescafe 3 in 1 White...    8.50  Shopee  15.0

```
