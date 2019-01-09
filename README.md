# SwDA-Preprocessing
## Reference
#### This repo refers to [Switchboard Dialog Act Corpus with Penn Treebank links](https://github.com/cgpotts/swda)</br>
#### The segmentation of train/valid/test refers to [Ji Young Lee*, Franck Dernoncourt*, "Sequential Short-Text Classification with Recurrent and Convolutional Neural Networks". NAACL 2016. \(* indicates equal contribution\)](https://arxiv.org/abs/1603.03827)</br>
#### The preprocessing rules follow [WS-97 Switchboard DAMSL Coders Manual](https://web.stanford.edu/~jurafsky/ws97/manual.august1.html) to preprocess SwDA dataset</br>
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
sd    -> sd</br>
b     -> b</br>
sv    -> sv</br>
qy^d  -> qy^d</br>
na    -> na</br>
sd^r  -> sd</br>
x     -> x</br>
%     -> %</br>
qo    -> qo</br>
ba    -> ba</br>
b^r   -> b</br>
qy    -> qy</br>
ny    -> ny</br>
qr    -> qy</br>
h     -> h</br>
aa    -> aa</br>
fc    -> fc</br>
ny^r  -> ny</br>
sv^t  -> sv</br>
qh    -> qh</br>
aa^r  -> aa</br>
sv^r  -> sv</br>
fc^m  -> fc</br>
o     -> fo</br>
qw    -> qw</br>
nd    -> arp/nd</br>
qw^d  -> qw^d</br>
bk    -> bk</br>
^2    -> ^2</br>
^q    -> ^q</br>
bh    -> bh</br>
ba^r  -> ba</br>
qy^t  -> qy</br>
sd^t  -> sd</br>
qy^g  -> qy</br>
^h    -> ^h</br>
sd^m  -> sd</br>
ba^m  -> ba</br>
sd^e  -> sd</br>
sd(^q) -> sd</br>
ad    -> ad</br>
fe    -> ba</br>
br    -> br</br>
qy^d^r -> qy</br>
b^m   -> b^m</br>
nn    -> nn</br>
sv;sd -> sv</br>
ar    -> ar</br>
ar^r  -> ar</br>
bf    -> bf</br>
qw^t  -> qw</br>
nn^r  -> nn</br>
qrr   -> qrr</br>
sd^c  -> sd</br>
fo    -> fo</br>
ft    -> ft</br>
qy^c  -> qy</br>
sd^e^t -> sd</br>
ad^t  -> ad</br>
ng    -> ng</br>
sv(^q) -> sv</br>
fp    -> fp</br>
bd    -> bd</br>
sv^e  -> sv</br>
t3    -> t3</br>
qy^r  -> qy</br>
no    -> no</br>
^h^t  -> ^h</br>
bf^m  -> bf</br>
ng^r  -> ng</br>
qy^d^t -> qy</br>
na^t  -> na</br>
t1    -> t1</br>
^2^r  -> ^2</br>
cc    -> oo</br>
qy^g^t -> qy</br>
bk^r  -> bk</br>
^g    -> ^g</br>
qo^t  -> qo</br>
fw    -> fo</br>
sd,qy^g -> sd</br>
o^r   -> fo</br>
na^m  -> na</br>
br^m  -> br</br>
fa    -> fa</br>
sv^e^r -> sv</br>
sv^m  -> sv</br>
sd(^q)^t -> sd</br>
sd^2  -> sd</br>
aa^h  -> aa</br>
aa^m  -> aa</br>
co^t  -> oo</br>
aa^t  -> aa</br>
^q^t  -> ^q</br>
h^t   -> h</br>
qw^d^t -> qw</br>
qr^t  -> qy</br>
aa^2  -> aa</br>
qy^2  -> qy</br>
fx    -> sv</br>
aap   -> aap/am</br>
co    -> oo</br>
by    -> fo</br>
qy^m  -> qy</br>
qw^r  -> qw</br>
"     -> sd</br>
fc^r  -> fc</br>
na^r  -> na</br>
bh^r  -> bh</br>
ng^m  -> ng</br>
qy^h  -> qy</br>
qy^d(^q) -> qy</br>
qy(^q) -> qy</br>
ny^m  -> ny</br>
fp^m  -> fp</br>
ny^e  -> na</br>
qr^d  -> qy</br>
am    -> aap/am</br>
bf^g  -> bf</br>
bf^r  -> bf</br>
nn^e  -> ng</br>
qw^h  -> qw</br>
fc^t  -> fc</br>
oo    -> oo</br>
qrr^t -> qrr</br>
bh^m  -> bh</br>
bk^m  -> bk</br>
qy^d^h -> qy</br>
qh^h  -> qh</br>
qh^m  -> qh</br>
qrr^d -> qrr</br>
qh^g  -> qh</br>
ar^m  -> ar</br>
nn^m  -> nn</br>
cc^t  -> oo</br>
arp   -> arp/nd</br>
qo^d  -> qo</br>
no^r  -> no</br>
qw^c  -> qw</br>
bf^2  -> bf</br>
bc    -> fo</br>
qy^d^m -> qy</br>
no^t  -> no</br>
o^t   -> fo</br>
aap^r -> aap/am</br>
b^2   -> b</br>
ny^t  -> ny</br>
sv^2  -> sv</br>
qr(^q) -> qy</br>
b^m^r -> b</br>
sd;qy^d -> sd</br>
sd;no -> sd</br>
b^t   -> b</br>
fp^r  -> fp</br>
qo^r  -> qo</br>
qy^g^r -> qy</br>
fa^t  -> fa</br>
h^r   -> h</br>
^2^g  -> ^2</br>
na^m^t -> na</br>
am^r  -> aap/am</br>
ft^t  -> ft</br>
b^m^t -> b</br>
^h^r  -> ^h</br>
^2^t  -> ^2</br>
^q^r  -> ^q</br>
sd^e^r -> sd</br>
br^r  -> br</br>
sd^e^m -> sd</br>
qw^g  -> qw</br>
co^c  -> oo</br>
sd^e(^q)^r -> sd</br>
qw(^q) -> qw</br>
bc^r  -> fo</br>
cc^r  -> oo</br>
oo^t  -> oo</br>
oo(^q) -> oo</br>
ny^c  -> ny</br>
ny^c^r -> ny</br>
qy^d^c -> qy</br>
ad^r  -> ad</br>
qw^m  -> qw</br>
ad(^q) -> ad</br>
nd^t  -> arp/nd</br>
h^m   -> h</br>
h,sd  -> h</br>
aap^m -> aap/am</br>
aa,ar -> aa</br>
qh(^q) -> qh</br>
ad^c  -> ad</br>
o^c   -> fo</br>
qh^r  -> qh</br>
fo^c  -> fo</br>
bf^t  -> bf</br>
t1^t  -> t1</br>
sv^c  -> sv</br>
qy^c^r -> qy</br>
qw^d^c -> qw</br>
qy^g^c -> qy</br>
qo^d^c -> qo</br>
qh^c  -> qh</br>
ft^m  -> ft</br>
qw^r^t -> qw</br>
b^m^g -> b</br>
sd(^q)^r -> sd</br>
sd,sv -> sd</br>
sd;sv -> sd</br>
bf(^q) -> bf</br>
fa^r  -> fa</br>
bd^r  -> bd</br>
ng^t  -> ng</br>

### Tag statistic
#### Train
INFO:Merge Act Tag:[('sd', 75368), ('b', 33424), ('sv', 27183), ('%', 13820), ('aa', 9932), ('qy', 4425), ('ba', 4263), ('x', 3129), ('ny', 2591), ('fc', 2254), ('qw',1783), ('nn', 1211), ('qy^d', 1141), ('bk', 1139), ('h', 1122), ('bf', 953), ('^q', 944), ('bh', 927), ('na', 794), ('fo', 764), ('ad', 723), ('^2', 694), ('b^m', 606), ('qo', 582), ('qh', 562), ('^h', 499), ('ar', 320), ('ng', 275), ('br', 267), ('no', 256), ('arp/nd', 206), ('fp', 198), ('qrr', 194), ('t3', 110), ('oo', 110), ('aap/am', 95), ('t1', 94), ('bd', 86), ('qw^d', 79), ('^g', 79), ('fa', 62), ('ft', 61)]</br>
INFO:Merge Act Tag:# unique act: 42

#### Valid
INFO:Merge Act Tag:[('sd', 7800), ('b', 3622), ('sv', 2752), ('%', 1407), ('aa', 952), ('qy', 509), ('ba', 441), ('x', 347), ('ny', 334), ('fc', 296), ('qw', 206), ('qy^d', 141), ('bk', 133), ('nn', 128), ('h', 111), ('bh', 96), ('na', 80), ('fo', 79), ('bf', 75), ('qo', 72), ('^2', 71), ('qh', 67), ('^h', 59), ('ad', 57), ('^q', 56), ('b^m', 53), ('no', 33), ('ng', 31), ('qrr', 29), ('ar', 29), ('br', 26), ('fp', 22), ('arp/nd', 17), ('bd', 16), ('fa', 14), ('^g', 13), ('t1', 11), ('oo', 10), ('ft', 7), ('t3', 6), ('qw^d', 5), ('aap/am', 5)]</br>
INFO:Merge Act Tag:# unique act: 42

#### Test
INFO:Merge Act Tag:[('sd', 1497), ('sv', 833), ('b', 765), ('%', 369), ('aa', 213), ('x', 94), ('qy', 90), ('fc', 84), ('ba', 76), ('ny', 73), ('qw', 56), ('qy^d', 38), ('ad', 30), ('bk', 28), ('nn', 26), ('bf', 25), ('h', 23), ('bh', 21), ('b^m', 21), ('^2', 20), ('^q', 18), ('qo', 16), ('fo', 14), ('qh', 12), ('na', 10), ('br', 9),('aap/am', 7), ('ft', 7), ('^h', 7), ('no', 6), ('ng', 6), ('fp', 5), ('qrr', 4), ('ar', 3), ('arp/nd', 3), ('fa', 2), ('bd', 1), ('t1', 1), ('qw^d', 1)]</br>
INFO:Merge Act Tag:# unique act: 39
