# SwDA-Preprocessing
## This repo refers to [Switchboard Dialog Act Corpus with Penn Treebank links](https://github.com/cgpotts/swda)
### The segmentation of train/valid/test refers to [Ji Young Lee*, Franck Dernoncourt*, "Sequential Short-Text Classification with Recurrent and Convolutional Neural Networks". NAACL 2016. (* indicates equal contribution)](https://arxiv.org/abs/1603.03827)
### The preprocessing rules follow [WS-97 Switchboard DAMSL Coders Manual](https://web.stanford.edu/~jurafsky/ws97/manual.august1.html) to preprocess SwDA dataset
There were 220 tags used in the coding; 130 of these occurred less than 10 times each, so for our initial experiments we clustered the 220 tags into 42 larger classes. We did the clustering by removing the secondary carat-dimensions (^2,^g,^m,^r,^e,^q,^d), with 5 exceptions. The exceptions: we left qy^d (Declarative yes-no Questions) , qw^d (Declarative wh-questions) and b^m (Signal-Understanding-via-Mimic), and we folded the few examples of nn^e into ng, and ny^e into na. Then, we grouped together some tags that had very little training data; those tags that appear in the following list were grouped with other tags on the same line.
### Tags that do not mention in the manual

#### Plus
Plus is the utterance that interrupt by other speakers, see [Nick Webb, Mark Hepple and Yorick Wilks, "Dialogue Act Classification Based on Intra-Utterance Features". AAAI 2005.](https://pdfs.semanticscholar.org/6eef/62288da1c73cb57ed0787b5db12151ae2c29.pdf)

#### Semicolon and Camma
Only take the first tag
e.g. sv;sd -> sv

#### Tag with parentheses
Remove the parentheses
e.g. qh(^q) -> qh^q

### Orginal act_tag -> New act_tag
sd    -> sd
b     -> b
sv    -> sv
qy^d  -> qy^d
na    -> na
sd^r  -> sd
x     -> x
%     -> %
qo    -> qo
ba    -> ba
b^r   -> b
qy    -> qy
ny    -> ny
qr    -> qy
h     -> h
aa    -> aa
fc    -> fc
ny^r  -> ny
sv^t  -> sv
qh    -> qh
aa^r  -> aa
sv^r  -> sv
fc^m  -> fc
o     -> fo
qw    -> qw
nd    -> arp/nd
qw^d  -> qw^d
bk    -> bk
^2    -> ^2
^q    -> ^q
bh    -> bh
ba^r  -> ba
qy^t  -> qy
sd^t  -> sd
qy^g  -> qy
^h    -> ^h
sd^m  -> sd
ba^m  -> ba
sd^e  -> sd
sd(^q) -> sd
ad    -> ad
fe    -> ba
br    -> br
qy^d^r -> qy
b^m   -> b^m
nn    -> nn
sv;sd -> sv
ar    -> ar
ar^r  -> ar
bf    -> bf
qw^t  -> qw
nn^r  -> nn
qrr   -> qrr
sd^c  -> sd
fo    -> fo
ft    -> ft
qy^c  -> qy
sd^e^t -> sd
ad^t  -> ad
ng    -> ng
sv(^q) -> sv
fp    -> fp
bd    -> bd
sv^e  -> sv
t3    -> t3
qy^r  -> qy
no    -> no
^h^t  -> ^h
bf^m  -> bf
ng^r  -> ng
qy^d^t -> qy
na^t  -> na
t1    -> t1
^2^r  -> ^2
cc    -> oo
qy^g^t -> qy
bk^r  -> bk
^g    -> ^g
qo^t  -> qo
fw    -> fo
sd,qy^g -> sd
o^r   -> fo
na^m  -> na
br^m  -> br
fa    -> fa
sv^e^r -> sv
sv^m  -> sv
sd(^q)^t -> sd
sd^2  -> sd
aa^h  -> aa
aa^m  -> aa
co^t  -> oo
aa^t  -> aa
^q^t  -> ^q
h^t   -> h
qw^d^t -> qw
qr^t  -> qy
aa^2  -> aa
qy^2  -> qy
fx    -> sv
aap   -> aap/am
co    -> oo
by    -> fo
qy^m  -> qy
qw^r  -> qw
"     -> sd
fc^r  -> fc
na^r  -> na
bh^r  -> bh
ng^m  -> ng
qy^h  -> qy
qy^d(^q) -> qy
qy(^q) -> qy
ny^m  -> ny
fp^m  -> fp
ny^e  -> na
qr^d  -> qy
am    -> aap/am
bf^g  -> bf
bf^r  -> bf
nn^e  -> ng
qw^h  -> qw
fc^t  -> fc
oo    -> oo
qrr^t -> qrr
bh^m  -> bh
bk^m  -> bk
qy^d^h -> qy
qh^h  -> qh
qh^m  -> qh
qrr^d -> qrr
qh^g  -> qh
ar^m  -> ar
nn^m  -> nn
cc^t  -> oo
arp   -> arp/nd
qo^d  -> qo
no^r  -> no
qw^c  -> qw
bf^2  -> bf
bc    -> fo
qy^d^m -> qy
no^t  -> no
o^t   -> fo
aap^r -> aap/am
b^2   -> b
ny^t  -> ny
sv^2  -> sv
qr(^q) -> qy
b^m^r -> b
sd;qy^d -> sd
sd;no -> sd
b^t   -> b
fp^r  -> fp
qo^r  -> qo
qy^g^r -> qy
fa^t  -> fa
h^r   -> h
^2^g  -> ^2
na^m^t -> na
am^r  -> aap/am
ft^t  -> ft
b^m^t -> b
^h^r  -> ^h
^2^t  -> ^2
^q^r  -> ^q
sd^e^r -> sd
br^r  -> br
sd^e^m -> sd
qw^g  -> qw
co^c  -> oo
sd^e(^q)^r -> sd
qw(^q) -> qw
bc^r  -> fo
cc^r  -> oo
oo^t  -> oo
oo(^q) -> oo
ny^c  -> ny
ny^c^r -> ny
qy^d^c -> qy
ad^r  -> ad
qw^m  -> qw
ad(^q) -> ad
nd^t  -> arp/nd
h^m   -> h
h,sd  -> h
aap^m -> aap/am
aa,ar -> aa
qh(^q) -> qh
ad^c  -> ad
o^c   -> fo
qh^r  -> qh
fo^c  -> fo
bf^t  -> bf
t1^t  -> t1
sv^c  -> sv
qy^c^r -> qy
qw^d^c -> qw
qy^g^c -> qy
qo^d^c -> qo
qh^c  -> qh
ft^m  -> ft
qw^r^t -> qw
b^m^g -> b
sd(^q)^r -> sd
sd,sv -> sd
sd;sv -> sd
bf(^q) -> bf
fa^r  -> fa
bd^r  -> bd
ng^t  -> ng

### Tag statistic
#### Train
INFO:Merge Act Tag:[('sd', 75368), ('b', 33424), ('sv', 27183), ('%', 13820), ('aa', 9932), ('qy', 4425), ('ba', 4263), ('x', 3129), ('ny', 2591), ('fc', 2254), ('qw',1783), ('nn', 1211), ('qy^d', 1141), ('bk', 1139), ('h', 1122), ('bf', 953), ('^q', 944), ('bh', 927), ('na', 794), ('fo', 764), ('ad', 723), ('^2', 694), ('b^m', 606), ('qo', 582), ('qh', 562), ('^h', 499), ('ar', 320), ('ng', 275), ('br', 267), ('no', 256), ('arp/nd', 206), ('fp', 198), ('qrr', 194), ('t3', 110), ('oo', 110), ('aap/am', 95), ('t1', 94), ('bd', 86), ('qw^d', 79), ('^g', 79), ('fa', 62), ('ft', 61)]
INFO:Merge Act Tag:# unique act: 42

#### Valid
INFO:Merge Act Tag:[('sd', 7800), ('b', 3622), ('sv', 2752), ('%', 1407), ('aa', 952), ('qy', 509), ('ba', 441), ('x', 347), ('ny', 334), ('fc', 296), ('qw', 206), ('qy^d', 141), ('bk', 133), ('nn', 128), ('h', 111), ('bh', 96), ('na', 80), ('fo', 79), ('bf', 75), ('qo', 72), ('^2', 71), ('qh', 67), ('^h', 59), ('ad', 57), ('^q', 56), ('b^m', 53), ('no', 33), ('ng', 31), ('qrr', 29), ('ar', 29), ('br', 26), ('fp', 22), ('arp/nd', 17), ('bd', 16), ('fa', 14), ('^g', 13), ('t1', 11), ('oo', 10), ('ft', 7), ('t3', 6), ('qw^d', 5), ('aap/am', 5)]
INFO:Merge Act Tag:# unique act: 42

#### Test
INFO:Merge Act Tag:[('sd', 1497), ('sv', 833), ('b', 765), ('%', 369), ('aa', 213), ('x', 94), ('qy', 90), ('fc', 84), ('ba', 76), ('ny', 73), ('qw', 56), ('qy^d', 38), ('ad', 30), ('bk', 28), ('nn', 26), ('bf', 25), ('h', 23), ('bh', 21), ('b^m', 21), ('^2', 20), ('^q', 18), ('qo', 16), ('fo', 14), ('qh', 12), ('na', 10), ('br', 9),('aap/am', 7), ('ft', 7), ('^h', 7), ('no', 6), ('ng', 6), ('fp', 5), ('qrr', 4), ('ar', 3), ('arp/nd', 3), ('fa', 2), ('bd', 1), ('t1', 1), ('qw^d', 1)]
INFO:Merge Act Tag:# unique act: 39