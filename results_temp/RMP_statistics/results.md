(this summary is also saved to results/qwen_ag_news_rmp_alpha0p3_seed42069_shadow_summary.txt)
📊 Experiment Results Summary:
================================================================================

🎯 Overall Performance Metrics:
--------------------------------------------------------------------------------
  Total Rounds: 50
  Initial Clean Accuracy: 0.4560 (45.60%)
  Final Clean Accuracy: 0.9090 (90.90%)
  Accuracy Change: +0.4530 (+45.30%)
  Best Clean Accuracy: 0.9113 (91.13%) [Round 49]
  Worst Clean Accuracy: 0.4560 (45.60%) [Round 1]
  Average Clean Accuracy: 0.8734 (87.34%)
  Std Dev of Clean Accuracy: 0.0707 (7.07%)

  📈 Stability Metrics:
    Final |Δacc| (Stability): 0.0023
    Peak |Δacc|: 0.2450 [Round 1]
    Average |Δacc|: 0.0163
    Std Dev of |Δacc|: 0.0471

  📐 Update Statistics:
    Final Aggregated Update Norm: 0.177836
    Average Update Norm: 0.237190
    Max Update Norm: 1.001267 [Round 1]
    Min Update Norm: 0.164524 [Round 39]

  🔍 Defense Mechanism Detailed Analysis:
    Similarity Statistics (all clients, all rounds):
      Mean Similarity: 0.1380
      Std Dev: 0.1307
      Min: 0.0072
      Max: 0.6315
    Threshold Statistics:
      Mean Threshold: 0.0000
      Min Threshold: 0.0000
      Max Threshold: 0.0000
    Mean Similarity per Round:
      Average: 0.1380
      Std Dev: 0.1162
    Client Acceptance Statistics:
      Total Accepted: 350
      Total Rejected: 0
      Overall Acceptance Rate: 1.0000 (100.00%)

  📐 Euclidean Distance Statistics (all clients, all rounds):
      Mean Distance: 0.322464
      Std Dev: 0.086832
      Min: 0.202564
      Max: 0.808414
    Mean Euclidean Distance per Round:
      Average: 0.322464
      Std Dev: 0.076921
      Min (round): 0.269265 [Round 39]
      Max (round): 0.738351 [Round 1]

📈 Per-Round Summary (All Rounds):
-----------------------------------------------------------------------------------------------
Round   | Clean Acc   | |Δacc|    | Rej Rate    | Update Norm   | Mean Euc Dist  | Threshold  
-----------------------------------------------------------------------------------------------
1       | 0.4560      | 0.2450    | 0.0000      | 1.001267      | 0.738351       | 0.0000     
2       | 0.6867      | 0.2307    | 0.0000      | 0.795785      | 0.554027       | 0.0000     
3       | 0.7763      | 0.0897    | 0.0000      | 0.554145      | 0.454044       | 0.0000     
4       | 0.8037      | 0.0273    | 0.0000      | 0.404244      | 0.392465       | 0.0000     
5       | 0.8267      | 0.0230    | 0.0000      | 0.334329      | 0.375579       | 0.0000     
6       | 0.8340      | 0.0073    | 0.0000      | 0.290050      | 0.358176       | 0.0000     
7       | 0.8487      | 0.0147    | 0.0000      | 0.262581      | 0.349396       | 0.0000     
8       | 0.8573      | 0.0087    | 0.0000      | 0.251116      | 0.348954       | 0.0000     
9       | 0.8763      | 0.0190    | 0.0000      | 0.256382      | 0.352674       | 0.0000     
10      | 0.8763      | 0.0000    | 0.0000      | 0.245039      | 0.344461       | 0.0000     
11      | 0.8880      | 0.0117    | 0.0000      | 0.237554      | 0.343903       | 0.0000     
12      | 0.8857      | 0.0023    | 0.0000      | 0.225857      | 0.332563       | 0.0000     
13      | 0.8897      | 0.0040    | 0.0000      | 0.225451      | 0.330518       | 0.0000     
14      | 0.8843      | 0.0053    | 0.0000      | 0.218055      | 0.326996       | 0.0000     
15      | 0.8863      | 0.0020    | 0.0000      | 0.215146      | 0.322174       | 0.0000     
16      | 0.8867      | 0.0003    | 0.0000      | 0.215947      | 0.324825       | 0.0000     
17      | 0.8890      | 0.0023    | 0.0000      | 0.206341      | 0.315132       | 0.0000     
18      | 0.8877      | 0.0013    | 0.0000      | 0.208365      | 0.321004       | 0.0000     
19      | 0.8877      | 0.0000    | 0.0000      | 0.198278      | 0.313705       | 0.0000     
20      | 0.8897      | 0.0020    | 0.0000      | 0.192209      | 0.309700       | 0.0000     
21      | 0.8837      | 0.0060    | 0.0000      | 0.193143      | 0.305761       | 0.0000     
22      | 0.8880      | 0.0043    | 0.0000      | 0.186525      | 0.300159       | 0.0000     
23      | 0.8923      | 0.0043    | 0.0000      | 0.182953      | 0.297779       | 0.0000     
24      | 0.8850      | 0.0073    | 0.0000      | 0.177525      | 0.292427       | 0.0000     
25      | 0.8957      | 0.0107    | 0.0000      | 0.178011      | 0.288169       | 0.0000     
26      | 0.8937      | 0.0020    | 0.0000      | 0.178653      | 0.290741       | 0.0000     
27      | 0.8937      | 0.0000    | 0.0000      | 0.181401      | 0.289984       | 0.0000     
28      | 0.8927      | 0.0010    | 0.0000      | 0.172298      | 0.282406       | 0.0000     
29      | 0.9000      | 0.0073    | 0.0000      | 0.171184      | 0.282022       | 0.0000     
30      | 0.8967      | 0.0033    | 0.0000      | 0.174723      | 0.285577       | 0.0000     
31      | 0.8960      | 0.0007    | 0.0000      | 0.167175      | 0.280800       | 0.0000     
32      | 0.8980      | 0.0020    | 0.0000      | 0.172909      | 0.282229       | 0.0000     
33      | 0.9040      | 0.0060    | 0.0000      | 0.173943      | 0.284975       | 0.0000     
34      | 0.8993      | 0.0047    | 0.0000      | 0.164584      | 0.270731       | 0.0000     
35      | 0.9000      | 0.0007    | 0.0000      | 0.173460      | 0.281759       | 0.0000     
36      | 0.8963      | 0.0037    | 0.0000      | 0.175164      | 0.283652       | 0.0000     
37      | 0.9013      | 0.0050    | 0.0000      | 0.176552      | 0.284857       | 0.0000     
38      | 0.8973      | 0.0040    | 0.0000      | 0.180366      | 0.293360       | 0.0000     
39      | 0.9023      | 0.0050    | 0.0000      | 0.164524      | 0.269265       | 0.0000     
40      | 0.8987      | 0.0037    | 0.0000      | 0.181100      | 0.287168       | 0.0000     
41      | 0.9077      | 0.0090    | 0.0000      | 0.175553      | 0.282943       | 0.0000     
42      | 0.9023      | 0.0053    | 0.0000      | 0.179655      | 0.289420       | 0.0000     
43      | 0.9003      | 0.0020    | 0.0000      | 0.184150      | 0.294928       | 0.0000     
44      | 0.9007      | 0.0003    | 0.0000      | 0.184057      | 0.293784       | 0.0000     
45      | 0.8993      | 0.0013    | 0.0000      | 0.172592      | 0.277344       | 0.0000     
46      | 0.9010      | 0.0017    | 0.0000      | 0.181171      | 0.292754       | 0.0000     
47      | 0.9057      | 0.0047    | 0.0000      | 0.175203      | 0.282456       | 0.0000     
48      | 0.9030      | 0.0027    | 0.0000      | 0.181488      | 0.290217       | 0.0000     
49      | 0.9113      | 0.0083    | 0.0000      | 0.183486      | 0.290294       | 0.0000     
50      | 0.9090      | 0.0023    | 0.0000      | 0.177836      | 0.286598       | 0.0000     

--------------------------------------------------------------------------------
📐 COSINE SIMILARITY (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A) | Mean | Std
--------------------------------------------------------------------------------
1      | 0.564395       | 0.561311       | 0.529348       | 0.588887       | 0.573488       | 0.592902       | 0.592223       | 0.571794 | 0.021126
2      | 0.631519       | 0.581607       | 0.453262       | 0.602077       | 0.619239       | 0.613016       | 0.613028       | 0.587678 | 0.056713
3      | 0.517212       | 0.446339       | 0.372279       | 0.475227       | 0.506508       | 0.524446       | 0.524388       | 0.480914 | 0.051806
4      | 0.398304       | 0.333872       | 0.304610       | 0.336503       | 0.388169       | 0.433727       | 0.433666       | 0.375550 | 0.047409
5      | 0.295896       | 0.228410       | 0.218384       | 0.231343       | 0.284082       | 0.350172       | 0.350237       | 0.279789 | 0.052033
6      | 0.213526       | 0.148005       | 0.165300       | 0.176510       | 0.226485       | 0.297063       | 0.296836       | 0.217675 | 0.056004
7      | 0.156629       | 0.135489       | 0.108113       | 0.134634       | 0.178102       | 0.259223       | 0.259545       | 0.175962 | 0.056374
8      | 0.121155       | 0.105317       | 0.069976       | 0.117130       | 0.142916       | 0.233520       | 0.234235       | 0.146321 | 0.058967
9      | 0.133596       | 0.121890       | 0.088151       | 0.116656       | 0.155575       | 0.242973       | 0.243795       | 0.157520 | 0.057412
10     | 0.114793       | 0.102969       | 0.060663       | 0.112885       | 0.136981       | 0.229151       | 0.228568       | 0.140859 | 0.059561
11     | 0.108723       | 0.088012       | 0.026164       | 0.086653       | 0.130500       | 0.216148       | 0.216295       | 0.124642 | 0.064966
12     | 0.083119       | 0.081538       | 0.030161       | 0.080266       | 0.125334       | 0.208975       | 0.208539       | 0.116847 | 0.063475
13     | 0.099548       | 0.080285       | 0.035677       | 0.076383       | 0.121081       | 0.210800       | 0.211624       | 0.119342 | 0.062845
14     | 0.085942       | 0.084124       | 0.044930       | 0.070542       | 0.107877       | 0.207084       | 0.205941       | 0.115206 | 0.060337
15     | 0.083849       | 0.075761       | 0.030777       | 0.075908       | 0.105888       | 0.203476       | 0.204123       | 0.111398 | 0.061985
16     | 0.089046       | 0.070584       | 0.037234       | 0.068004       | 0.100076       | 0.202281       | 0.202724       | 0.109993 | 0.061253
17     | 0.086946       | 0.078384       | 0.044406       | 0.056994       | 0.096789       | 0.201405       | 0.202345       | 0.109610 | 0.060592
18     | 0.090812       | 0.069308       | 0.014998       | 0.054850       | 0.078965       | 0.193364       | 0.193333       | 0.099376 | 0.063424
19     | 0.073098       | 0.060058       | 0.021781       | 0.037673       | 0.071727       | 0.185783       | 0.185306       | 0.090775 | 0.062291
20     | 0.073368       | 0.058802       | 0.023520       | 0.015224       | 0.061768       | 0.179014       | 0.179160       | 0.084408 | 0.062919
21     | 0.064583       | 0.068048       | 0.034494       | 0.043472       | 0.070601       | 0.187666       | 0.187849       | 0.093816 | 0.060664
22     | 0.060157       | 0.052683       | 0.037642       | 0.021886       | 0.073738       | 0.181924       | 0.182088       | 0.087160 | 0.061878
23     | 0.052302       | 0.050276       | 0.028694       | 0.022506       | 0.066995       | 0.177724       | 0.177397       | 0.082271 | 0.061827
24     | 0.045114       | 0.063181       | 0.036164       | 0.017860       | 0.060958       | 0.177816       | 0.177649       | 0.082677 | 0.061758
25     | 0.070048       | 0.064985       | 0.030943       | 0.035328       | 0.061478       | 0.186175       | 0.185914       | 0.090696 | 0.061829
26     | 0.058156       | 0.065671       | 0.032560       | 0.028458       | 0.063803       | 0.182200       | 0.182530       | 0.087625 | 0.061414
27     | 0.065952       | 0.052139       | 0.040574       | 0.033064       | 0.076077       | 0.185382       | 0.185403       | 0.091227 | 0.061038
28     | 0.064454       | 0.074449       | 0.036650       | 0.010336       | 0.068860       | 0.183179       | 0.184016       | 0.088849 | 0.063297
29     | 0.052095       | 0.050383       | 0.038632       | 0.020803       | 0.063565       | 0.179245       | 0.179733       | 0.083494 | 0.061936
30     | 0.036763       | 0.066707       | 0.032038       | 0.034469       | 0.063030       | 0.179756       | 0.179594       | 0.084622 | 0.061445
31     | 0.058802       | 0.052268       | 0.023490       | 0.010348       | 0.041473       | 0.172796       | 0.171703       | 0.075840 | 0.062845
32     | 0.054665       | 0.059812       | 0.039476       | 0.023025       | 0.060180       | 0.180381       | 0.180625       | 0.085452 | 0.061324
33     | 0.059922       | 0.059288       | 0.046653       | 0.007226       | 0.062844       | 0.180005       | 0.180410       | 0.085193 | 0.062597
34     | 0.053071       | 0.065731       | 0.026717       | 0.025715       | 0.058604       | 0.180152       | 0.180183       | 0.084311 | 0.062232
35     | 0.057386       | 0.059716       | 0.039652       | 0.026979       | 0.069267       | 0.182902       | 0.183629       | 0.088504 | 0.061294
36     | 0.047151       | 0.069234       | 0.065516       | 0.041401       | 0.066331       | 0.188529       | 0.188778       | 0.095277 | 0.059832
37     | 0.052911       | 0.067648       | 0.041750       | 0.024521       | 0.077742       | 0.185065       | 0.185693       | 0.090761 | 0.061912
38     | 0.057404       | 0.072393       | 0.029297       | 0.019572       | 0.061060       | 0.179980       | 0.180275       | 0.085712 | 0.062074
39     | 0.054356       | 0.064060       | 0.049733       | 0.025020       | 0.069642       | 0.186197       | 0.185582       | 0.090656 | 0.061631
40     | 0.063483       | 0.067361       | 0.055145       | 0.047403       | 0.071204       | 0.191009       | 0.191314       | 0.098131 | 0.059285
41     | 0.073109       | 0.062370       | 0.049062       | 0.023401       | 0.063337       | 0.186219       | 0.186467       | 0.091995 | 0.061420
42     | 0.053483       | 0.062832       | 0.045597       | 0.039025       | 0.064248       | 0.184753       | 0.185322       | 0.090752 | 0.060197
43     | 0.069007       | 0.083662       | 0.059892       | 0.033440       | 0.057340       | 0.189229       | 0.189753       | 0.097475 | 0.059832
44     | 0.060864       | 0.055084       | 0.048215       | 0.023322       | 0.078129       | 0.185277       | 0.185199       | 0.090870 | 0.061570
45     | 0.067015       | 0.066970       | 0.050381       | 0.027580       | 0.075289       | 0.190186       | 0.189852       | 0.095325 | 0.061587
46     | 0.045021       | 0.055713       | 0.045960       | 0.036842       | 0.063240       | 0.180882       | 0.181291       | 0.086993 | 0.060013
47     | 0.061085       | 0.065778       | 0.067234       | 0.039001       | 0.069240       | 0.191690       | 0.191345       | 0.097911 | 0.059936
48     | 0.053221       | 0.045938       | 0.028725       | 0.038323       | 0.074972       | 0.182482       | 0.182376       | 0.086577 | 0.062048
49     | 0.063778       | 0.080561       | 0.080805       | 0.055830       | 0.066225       | 0.197090       | 0.197227       | 0.105931 | 0.058289
50     | 0.053232       | 0.046823       | 0.034016       | 0.034057       | 0.076237       | 0.183473       | 0.183034       | 0.087267 | 0.062117
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
📏 EUCLIDEAN DISTANCE (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A) | Mean | Std
--------------------------------------------------------------------------------
1      | 0.748197       | 0.772142       | 0.808414       | 0.791900       | 0.781588       | 0.558498       | 0.707719       | 0.738351 | 0.079435
2      | 0.539058       | 0.587593       | 0.687017       | 0.577017       | 0.533449       | 0.421615       | 0.532438       | 0.554027 | 0.073667
3      | 0.472324       | 0.457791       | 0.510549       | 0.484660       | 0.475037       | 0.342946       | 0.435001       | 0.454044 | 0.050177
4      | 0.413323       | 0.377083       | 0.401287       | 0.441631       | 0.441646       | 0.296011       | 0.376277       | 0.392465 | 0.046523
5      | 0.412929       | 0.351386       | 0.369217       | 0.429866       | 0.422274       | 0.283070       | 0.360311       | 0.375579 | 0.047718
6      | 0.407238       | 0.338550       | 0.350835       | 0.399998       | 0.396758       | 0.270381       | 0.343471       | 0.358176 | 0.044734
7      | 0.387987       | 0.323725       | 0.343472       | 0.404621       | 0.387316       | 0.263633       | 0.335018       | 0.349396 | 0.045092
8      | 0.376639       | 0.320734       | 0.341335       | 0.400985       | 0.404490       | 0.263568       | 0.334926       | 0.348954 | 0.046136
9      | 0.389607       | 0.322926       | 0.344110       | 0.404425       | 0.403280       | 0.266054       | 0.338316       | 0.352674 | 0.046707
10     | 0.379934       | 0.315274       | 0.334547       | 0.400973       | 0.389743       | 0.259749       | 0.331010       | 0.344461 | 0.045996
11     | 0.385132       | 0.318285       | 0.344774       | 0.393240       | 0.377116       | 0.259028       | 0.329745       | 0.343903 | 0.043586
12     | 0.362111       | 0.303648       | 0.329280       | 0.389864       | 0.373323       | 0.250645       | 0.319071       | 0.332563 | 0.044009
13     | 0.365007       | 0.303988       | 0.328568       | 0.378174       | 0.372148       | 0.249071       | 0.316672       | 0.330518 | 0.042639
14     | 0.370018       | 0.302487       | 0.322298       | 0.369657       | 0.363964       | 0.246342       | 0.314205       | 0.326996 | 0.041967
15     | 0.364187       | 0.301335       | 0.318325       | 0.372824       | 0.346688       | 0.243332       | 0.308526       | 0.322174 | 0.041028
16     | 0.357892       | 0.306673       | 0.318146       | 0.370396       | 0.364279       | 0.244924       | 0.311463       | 0.324825 | 0.040819
17     | 0.350359       | 0.298398       | 0.309801       | 0.358941       | 0.348573       | 0.237583       | 0.302268       | 0.315132 | 0.039218
18     | 0.357581       | 0.305212       | 0.319872       | 0.359893       | 0.354650       | 0.241856       | 0.307965       | 0.321004 | 0.039037
19     | 0.342271       | 0.295312       | 0.316149       | 0.354513       | 0.351035       | 0.236103       | 0.300549       | 0.313705 | 0.038571
20     | 0.348097       | 0.287332       | 0.307734       | 0.346286       | 0.347793       | 0.233554       | 0.297101       | 0.309700 | 0.039143
21     | 0.345093       | 0.290498       | 0.306115       | 0.334632       | 0.340805       | 0.230292       | 0.292890       | 0.305761 | 0.037231
22     | 0.330489       | 0.285262       | 0.297019       | 0.339889       | 0.334441       | 0.226313       | 0.287700       | 0.300159 | 0.036866
23     | 0.333355       | 0.281319       | 0.302185       | 0.335887       | 0.322029       | 0.224207       | 0.285471       | 0.297779 | 0.036175
24     | 0.320917       | 0.284657       | 0.294759       | 0.322141       | 0.324028       | 0.220342       | 0.280145       | 0.292427 | 0.034030
25     | 0.315972       | 0.282292       | 0.294086       | 0.315312       | 0.316733       | 0.216762       | 0.276028       | 0.288169 | 0.033040
26     | 0.321936       | 0.281876       | 0.295135       | 0.326829       | 0.311727       | 0.218935       | 0.278746       | 0.290741 | 0.034046
27     | 0.312058       | 0.278045       | 0.295483       | 0.335030       | 0.312720       | 0.218437       | 0.278116       | 0.289984 | 0.034777
28     | 0.309639       | 0.273015       | 0.288276       | 0.316144       | 0.306714       | 0.212801       | 0.270253       | 0.282406 | 0.032920
29     | 0.307600       | 0.273171       | 0.291005       | 0.314124       | 0.306085       | 0.212230       | 0.269937       | 0.282022 | 0.032601
30     | 0.312785       | 0.273274       | 0.286593       | 0.307209       | 0.330422       | 0.214990       | 0.273768       | 0.285577 | 0.034834
31     | 0.303933       | 0.274648       | 0.298217       | 0.306234       | 0.301925       | 0.211666       | 0.268975       | 0.280800 | 0.031371
32     | 0.305260       | 0.270836       | 0.285040       | 0.306192       | 0.325071       | 0.212623       | 0.270581       | 0.282229 | 0.033930
33     | 0.311618       | 0.274775       | 0.285830       | 0.301599       | 0.333131       | 0.214601       | 0.273270       | 0.284975 | 0.034846
34     | 0.300869       | 0.265726       | 0.276455       | 0.284133       | 0.304939       | 0.203657       | 0.259334       | 0.270731 | 0.031498
35     | 0.300310       | 0.273627       | 0.289165       | 0.320479       | 0.306555       | 0.212101       | 0.270072       | 0.281759 | 0.032881
36     | 0.308743       | 0.277807       | 0.285685       | 0.310810       | 0.316902       | 0.213834       | 0.271780       | 0.283652 | 0.032791
37     | 0.307524       | 0.274809       | 0.292538       | 0.296617       | 0.334466       | 0.214648       | 0.273398       | 0.284857 | 0.034504
38     | 0.324734       | 0.272500       | 0.293131       | 0.325297       | 0.335977       | 0.220983       | 0.280900       | 0.293360 | 0.037128
39     | 0.287522       | 0.273252       | 0.277131       | 0.292633       | 0.293737       | 0.202564       | 0.258013       | 0.269265 | 0.029596
40     | 0.306444       | 0.282978       | 0.282121       | 0.324938       | 0.322213       | 0.216299       | 0.275184       | 0.287168 | 0.034300
41     | 0.310857       | 0.273191       | 0.285517       | 0.305982       | 0.321228       | 0.213006       | 0.270823       | 0.282943 | 0.033627
42     | 0.307522       | 0.282055       | 0.292102       | 0.330674       | 0.318098       | 0.218167       | 0.277321       | 0.289420 | 0.034094
43     | 0.316092       | 0.275074       | 0.290840       | 0.335993       | 0.341169       | 0.222486       | 0.282841       | 0.294928 | 0.037942
44     | 0.315956       | 0.286454       | 0.290884       | 0.317376       | 0.343052       | 0.221262       | 0.281506       | 0.293784 | 0.035753
45     | 0.295686       | 0.276661       | 0.281609       | 0.299724       | 0.313435       | 0.208926       | 0.265363       | 0.277344 | 0.031584
46     | 0.301878       | 0.286749       | 0.289305       | 0.342318       | 0.327461       | 0.220750       | 0.280818       | 0.292754 | 0.036094
47     | 0.319371       | 0.281347       | 0.280942       | 0.307750       | 0.304391       | 0.212643       | 0.270747       | 0.282456 | 0.032729
48     | 0.311113       | 0.286869       | 0.294028       | 0.302752       | 0.340008       | 0.218701       | 0.278045       | 0.290217 | 0.034561
49     | 0.300473       | 0.284566       | 0.285991       | 0.347778       | 0.316081       | 0.218754       | 0.278417       | 0.290294 | 0.036613
50     | 0.314093       | 0.287047       | 0.291809       | 0.298667       | 0.324168       | 0.215815       | 0.274586       | 0.286598 | 0.032722
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
📉 GLOBAL LOSS (Per Round)
--------------------------------------------------------------------------------
Round    | Global Loss    
--------------------------------------------------------------------------------
1        | 1.984382       
2        | 0.981970       
3        | 0.650285       
4        | 0.550737       
5        | 0.518870       
6        | 0.486263       
7        | 0.458532       
8        | 0.456924       
9        | 0.405705       
10       | 0.405310       
11       | 0.384544       
12       | 0.408299       
13       | 0.408592       
14       | 0.430339       
15       | 0.454369       
16       | 0.458663       
17       | 0.455332       
18       | 0.509548       
19       | 0.529315       
20       | 0.541540       
21       | 0.586228       
22       | 0.597276       
23       | 0.609045       
24       | 0.643946       
25       | 0.596709       
26       | 0.656820       
27       | 0.678839       
28       | 0.687015       
29       | 0.637083       
30       | 0.696177       
31       | 0.727422       
32       | 0.708280       
33       | 0.658955       
34       | 0.750789       
35       | 0.765573       
36       | 0.744218       
37       | 0.755798       
38       | 0.802848       
39       | 0.776872       
40       | 0.798169       
41       | 0.772955       
42       | 0.823591       
43       | 0.833587       
44       | 0.799561       
45       | 0.824938       
46       | 0.830569       
47       | 0.768381       
48       | 0.855645       
49       | 0.768106       
50       | 0.829971       
--------------------------------------------------------------------------------

📊 Local Accuracies Analysis:
--------------------------------------------------------------------------------
Client ID    | Initial     | Final       | Change      | Average     | Std Dev     | Best        | Worst      
--------------------------------------------------------------------------------
Client 0      | 0.5924      | 0.8750      |     +0.2826 | 0.8721      | 0.0449      | 0.9022      | 0.5924     
Client 1      | 0.2228      | 0.8533      |     +0.6304 | 0.8311      | 0.1021      | 0.8967      | 0.2228     
Client 2      | 0.3261      | 0.8043      |     +0.4783 | 0.7604      | 0.0978      | 0.8370      | 0.3261     
Client 3      | 0.5924      | 0.7935      |     +0.2011 | 0.7151      | 0.0432      | 0.8043      | 0.5924     
Client 4      | 0.4457      | 0.8315      |     +0.3859 | 0.7499      | 0.0802      | 0.8478      | 0.4457     
Client 5      | 0.2228      | 0.8913      |     +0.6685 | 0.8368      | 0.1153      | 0.8967      | 0.2228     
Client 6      | 0.2228      | 0.8913      |     +0.6685 | 0.8368      | 0.1153      | 0.8967      | 0.2228     

  📈 Cross-Client Statistics:
    Final Accuracy - Mean: 0.8486, Std: 0.0371
    Final Accuracy - Best Client: 0.8913, Worst: 0.7935
    Final Accuracy - Range: 0.0978
    Initial Accuracy - Mean: 0.3750, Std: 0.1565
    Average Accuracy (all rounds) - Mean: 0.8003, Std: 0.0537

⚙️  Complete Experiment Configuration:
================================================================================

📋 Experiment Configuration:
  experiment_name: qwen_ag_news_rmp_alpha0p3_seed42069_shadow
  seed: 42069

👥 Federated Learning Setup:
  num_clients: 7
  num_attackers: 2
  num_benign_clients: None
  num_rounds: 50

🔧 Training Mode Configuration:
  use_lora: True
  lora_r: 8
  lora_alpha: 16
  lora_dropout: 0.1
  lora_target_modules: None
  model_name: Qwen/Qwen2.5-0.5B
  num_labels: 4

📊 Training Hyperparameters:
  client_lr: 0.00005
  server_lr: 1.0
  batch_size: 128
  test_batch_size: 256
  local_epochs: 2
  alpha (FedProx): 0.0

📦 Data Distribution:
  dirichlet_alpha: 0.3
  dataset_size_limit: 20000

🎭 Attack Configuration:
  attack_start_round: 0

📐 Formula 4 Constraint Parameters:
  d_T: N/A  # Distance threshold for constraint (4b)
  gamma: N/A  # Upper bound for constraint (4c)

🔗 Lagrangian Dual Parameters:
  use_lagrangian_dual: True
  lambda_init: N/A
  rho_init: N/A
  lambda_lr: N/A
  rho_lr: N/A

🧠 VGAE Training Parameters:
  dim_reduction_size: 1000
  vgae_epochs: 20
  vgae_lr: 0.01
  vgae_hidden_dim: 64
  vgae_latent_dim: 32
  vgae_dropout: 0

⚡ Attack Optimization Parameters:
  proxy_step: 0.001
  proxy_steps: 100
  gsp_perturbation_scale: N/A
  opt_init_perturbation_scale: N/A
  grad_clip_norm: 1.0
  attacker_claimed_data_size: None

📉 Proxy Loss Estimation Parameters:
  proxy_sample_size: 200
  proxy_max_batches_opt: 1
  proxy_max_batches_eval: 1

🕸️  Graph Construction Parameters:
  graph_threshold: 0.5

🛡️  Defense Mechanism Parameters:
  enable_defense: N/A
  defense_threshold: N/A
  tolerance_factor: N/A
  similarity_alpha: N/A
  defense_high_rejection_threshold: N/A
  defense_threshold_decay: N/A

📈 Visualization:
  generate_plots: N/A
  run_both_experiments: N/A

================================================================================

================================================================================
🔧 CORE SETTINGS OF THIS RUN (from results.json; the keys the overhead analysis depends on)
================================================================================
  GPU: NVIDIA RTX PRO 6000 Blackwell Server Edition
  experiment_name: qwen_ag_news_rmp_alpha0p3_seed42069_shadow
  model_name: Qwen/Qwen2.5-0.5B
  dataset: ag_news
  num_clients: 7
  num_attackers: 2
  num_rounds: 50
  seed: 42069
  data_distribution: non-iid
  dirichlet_alpha: 0.3
  dataset_size_limit: 20000
  local_epochs: 2
  batch_size: 128
  test_batch_size: 256
  max_length: 128
  use_lora: True
  lora_r: 8
  dim_reduction_size: 1000
  vgae_epochs: 20
  vgae_hidden_dim: 64
  vgae_latent_dim: 32
  proxy_step: 0.001
  proxy_steps: 100
  proxy_sample_size: 200
  proxy_max_batches_opt: 1
  early_stop_constraint_stability_steps: 1
  use_lagrangian_dual: True
  use_augmented_lagrangian: True
  lambda_update_mode: alm
  rho_max: 10000.0
  use_cosine_similarity_constraint: True
  use_pairwise_similarity_in_constraint: True
  sim_bound_low: None
  sim_bound_up: None
  dist_bound: None
  server_similarity_mode: pairwise
  attacker_observed_benign: None
  attacker_observed_param_fraction: n/a
  profile_overhead: True
  shadow_defense_enabled: True
  rounds with overhead records: 50 / 50

================================================================================
⏱️  PER-ROUND OVERHEAD (re-printed from results.json)
================================================================================
⏱️  Overhead round 1 (wall-clock s): round 136.72 | broadcast 0.02 | prepare 0.00 | benign train 120.84 [0:30.8 1:11.2 2:10.0 3:34.0 4:34.9] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.18 | observe 0.00 | eval_global 6.92 | eval_local 8.59 (bookkeeping) | unaccounted 0.06
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.04s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 2 (wall-clock s): round 134.62 | broadcast 0.03 | prepare 0.00 | benign train 119.44 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.10 [5:0.0 6:0.1] | aggregate 0.13 | observe 0.00 | eval_global 6.93 | eval_local 7.95 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.04s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.07s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 3 (wall-clock s): round 134.02 | broadcast 0.03 | prepare 0.00 | benign train 119.18 [0:30.3 1:10.9 2:9.7 3:33.7 4:34.6] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.13 | observe 0.00 | eval_global 6.93 | eval_local 7.62 (bookkeeping) | unaccounted 0.05
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 4 (wall-clock s): round 134.21 | broadcast 0.02 | prepare 0.00 | benign train 119.46 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.55 (bookkeeping) | unaccounted 0.06
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 5 (wall-clock s): round 134.25 | broadcast 0.02 | prepare 0.00 | benign train 119.49 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.56 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.06s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 6 (wall-clock s): round 134.25 | broadcast 0.03 | prepare 0.00 | benign train 119.48 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.12 | observe 0.00 | eval_global 6.93 | eval_local 7.56 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.04s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 7 (wall-clock s): round 134.25 | broadcast 0.02 | prepare 0.00 | benign train 119.49 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.56 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 8 (wall-clock s): round 134.15 | broadcast 0.02 | prepare 0.00 | benign train 119.40 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.08 [5:0.0 6:0.1] | aggregate 0.12 | observe 0.00 | eval_global 6.93 | eval_local 7.54 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 9 (wall-clock s): round 134.22 | broadcast 0.02 | prepare 0.00 | benign train 119.44 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.60 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 10 (wall-clock s): round 133.99 | broadcast 0.02 | prepare 0.00 | benign train 119.21 [0:30.2 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.58 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 11 (wall-clock s): round 134.11 | broadcast 0.03 | prepare 0.00 | benign train 119.27 [0:30.3 1:10.9 2:9.7 3:33.8 4:34.6] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.14 | observe 0.00 | eval_global 6.93 | eval_local 7.61 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.06s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 12 (wall-clock s): round 134.02 | broadcast 0.03 | prepare 0.00 | benign train 119.26 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.60 (bookkeeping) | unaccounted 0.01
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 13 (wall-clock s): round 134.12 | broadcast 0.02 | prepare 0.00 | benign train 119.36 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.10 | observe 0.00 | eval_global 6.94 | eval_local 7.60 (bookkeeping) | unaccounted 0.01
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 14 (wall-clock s): round 134.33 | broadcast 0.02 | prepare 0.00 | benign train 119.54 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.59 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.04s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.06s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 15 (wall-clock s): round 134.29 | broadcast 0.03 | prepare 0.00 | benign train 119.51 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.58 (bookkeeping) | unaccounted 0.05
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.04s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 16 (wall-clock s): round 134.05 | broadcast 0.02 | prepare 0.00 | benign train 119.29 [0:30.3 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.09 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.56 (bookkeeping) | unaccounted 0.05
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.04s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 17 (wall-clock s): round 133.96 | broadcast 0.03 | prepare 0.00 | benign train 119.19 [0:30.2 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.56 (bookkeeping) | unaccounted 0.05
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.04s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 18 (wall-clock s): round 133.93 | broadcast 0.03 | prepare 0.00 | benign train 119.17 [0:30.2 1:10.9 2:9.7 3:33.7 4:34.6] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.58 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 19 (wall-clock s): round 134.11 | broadcast 0.03 | prepare 0.00 | benign train 119.33 [0:30.3 1:10.9 2:9.7 3:33.8 4:34.6] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.57 (bookkeeping) | unaccounted 0.05
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.06s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 20 (wall-clock s): round 133.94 | broadcast 0.02 | prepare 0.00 | benign train 119.17 [0:30.2 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.58 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 21 (wall-clock s): round 133.98 | broadcast 0.03 | prepare 0.00 | benign train 119.19 [0:30.2 1:10.9 2:9.7 3:33.7 4:34.6] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.12 | observe 0.00 | eval_global 6.93 | eval_local 7.57 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.06s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 22 (wall-clock s): round 134.26 | broadcast 0.02 | prepare 0.00 | benign train 119.52 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.12 | observe 0.00 | eval_global 6.93 | eval_local 7.54 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.04s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 23 (wall-clock s): round 134.17 | broadcast 0.02 | prepare 0.00 | benign train 119.43 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.56 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 24 (wall-clock s): round 134.06 | broadcast 0.03 | prepare 0.00 | benign train 119.28 [0:30.3 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.56 (bookkeeping) | unaccounted 0.05
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 25 (wall-clock s): round 134.17 | broadcast 0.03 | prepare 0.00 | benign train 119.46 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.53 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 26 (wall-clock s): round 134.06 | broadcast 0.03 | prepare 0.00 | benign train 119.30 [0:30.3 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.10 | observe 0.00 | eval_global 6.93 | eval_local 7.58 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 27 (wall-clock s): round 133.96 | broadcast 0.03 | prepare 0.00 | benign train 119.18 [0:30.2 1:10.9 2:9.7 3:33.7 4:34.6] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.12 | observe 0.00 | eval_global 6.93 | eval_local 7.56 (bookkeeping) | unaccounted 0.06
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.04s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.04s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 28 (wall-clock s): round 134.01 | broadcast 0.02 | prepare 0.00 | benign train 119.20 [0:30.2 1:10.9 2:9.7 3:33.7 4:34.6] | attack 0.08 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.60 (bookkeeping) | unaccounted 0.05
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 29 (wall-clock s): round 134.01 | broadcast 0.02 | prepare 0.00 | benign train 119.23 [0:30.3 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.60 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 30 (wall-clock s): round 133.93 | broadcast 0.03 | prepare 0.00 | benign train 119.18 [0:30.2 1:10.9 2:9.7 3:33.7 4:34.6] | attack 0.08 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.56 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 31 (wall-clock s): round 133.93 | broadcast 0.03 | prepare 0.00 | benign train 119.15 [0:30.2 1:10.9 2:9.7 3:33.7 4:34.6] | attack 0.08 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.58 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 32 (wall-clock s): round 133.99 | broadcast 0.03 | prepare 0.00 | benign train 119.23 [0:30.3 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.10 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.56 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.07s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 33 (wall-clock s): round 133.95 | broadcast 0.02 | prepare 0.00 | benign train 119.18 [0:30.2 1:10.9 2:9.7 3:33.7 4:34.6] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.58 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 34 (wall-clock s): round 133.99 | broadcast 0.03 | prepare 0.00 | benign train 119.21 [0:30.2 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.60 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 35 (wall-clock s): round 133.98 | broadcast 0.02 | prepare 0.00 | benign train 119.20 [0:30.2 1:10.9 2:9.7 3:33.7 4:34.6] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.60 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 36 (wall-clock s): round 134.32 | broadcast 0.02 | prepare 0.00 | benign train 119.53 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.12 | observe 0.00 | eval_global 6.93 | eval_local 7.58 (bookkeeping) | unaccounted 0.05
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.06s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 37 (wall-clock s): round 133.94 | broadcast 0.03 | prepare 0.00 | benign train 119.23 [0:30.2 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.55 (bookkeeping) | unaccounted 0.01
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 38 (wall-clock s): round 133.97 | broadcast 0.03 | prepare 0.00 | benign train 119.20 [0:30.2 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.08 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.58 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 39 (wall-clock s): round 134.23 | broadcast 0.02 | prepare 0.00 | benign train 119.47 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.10 | observe 0.00 | eval_global 6.93 | eval_local 7.56 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 40 (wall-clock s): round 133.93 | broadcast 0.03 | prepare 0.00 | benign train 119.21 [0:30.2 1:10.9 2:9.7 3:33.7 4:34.6] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.57 (bookkeeping) | unaccounted 0.01
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 41 (wall-clock s): round 133.96 | broadcast 0.02 | prepare 0.00 | benign train 119.19 [0:30.2 1:10.9 2:9.7 3:33.7 4:34.6] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.57 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 42 (wall-clock s): round 133.96 | broadcast 0.03 | prepare 0.00 | benign train 119.19 [0:30.2 1:10.9 2:9.7 3:33.7 4:34.6] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.57 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 43 (wall-clock s): round 133.94 | broadcast 0.03 | prepare 0.00 | benign train 119.20 [0:30.2 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.56 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 44 (wall-clock s): round 134.16 | broadcast 0.03 | prepare 0.00 | benign train 119.38 [0:30.2 1:10.9 2:9.7 3:33.8 4:34.7] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.58 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.06s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 45 (wall-clock s): round 134.31 | broadcast 0.03 | prepare 0.00 | benign train 119.52 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.58 (bookkeeping) | unaccounted 0.06
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 46 (wall-clock s): round 134.24 | broadcast 0.03 | prepare 0.00 | benign train 119.48 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.57 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 47 (wall-clock s): round 134.26 | broadcast 0.03 | prepare 0.00 | benign train 119.48 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.12 | observe 0.00 | eval_global 6.93 | eval_local 7.58 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 48 (wall-clock s): round 134.25 | broadcast 0.03 | prepare 0.00 | benign train 119.49 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.58 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.04s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 49 (wall-clock s): round 134.31 | broadcast 0.03 | prepare 0.00 | benign train 119.54 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.57 (bookkeeping) | unaccounted 0.05
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 50 (wall-clock s): round 134.27 | broadcast 0.03 | prepare 0.00 | benign train 119.50 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.07 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.58 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.04s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

================================================================================
🛡️  PER-ROUND SHADOW DEFENSES (re-printed from results.json; computed only, NOT applied)
================================================================================
[shadow] round 1
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=1.361764 krum=3.199984 mkrum=KEEP tm_trim=0.6479 (lo 0.3237 / hi 0.3242) med_prov=0.1087 d_med=0.868109
    [shadow] C1 (B): norm=0.606631 krum=1.950418 mkrum=KEEP tm_trim=0.5257 (lo 0.2632 / hi 0.2625) med_prov=0.1518 d_med=0.657874
    [shadow] C2 (B): norm=0.560976 krum=2.038867 mkrum=KEEP tm_trim=0.5681 (lo 0.2844 / hi 0.2836) med_prov=0.1442 d_med=0.694092
    [shadow] C3 (B): norm=1.518111 krum=3.472590 mkrum=REJECT tm_trim=0.7290 (lo 0.3638 / hi 0.3652) med_prov=0.0797 d_med=0.951056
    [shadow] C4 (B): norm=1.264700 krum=3.289043 mkrum=REJECT tm_trim=0.6094 (lo 0.3057 / hi 0.3038) med_prov=0.1406 d_med=0.788349
    [shadow] C5 (A): norm=1.135799 krum=2.953588 mkrum=KEEP tm_trim=0.4599 (lo 0.2296 / hi 0.2304) med_prov=0.1879 d_med=0.649520
    [shadow] C6 (A): norm=1.135370 krum=2.954827 mkrum=KEEP tm_trim=0.4600 (lo 0.2297 / hi 0.2303) med_prov=0.1872 d_med=0.650600
[shadow] round 2
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=1.088580 krum=1.859704 mkrum=KEEP tm_trim=0.6459 (lo 0.3234 / hi 0.3225) med_prov=0.1124 d_med=0.607232
    [shadow] C1 (B): norm=0.455790 krum=1.174375 mkrum=KEEP tm_trim=0.5249 (lo 0.2625 / hi 0.2624) med_prov=0.1532 d_med=0.519266
    [shadow] C2 (B): norm=0.441318 krum=1.377192 mkrum=KEEP tm_trim=0.6259 (lo 0.3131 / hi 0.3128) med_prov=0.1204 d_med=0.614598
    [shadow] C3 (B): norm=1.121905 krum=1.988635 mkrum=REJECT tm_trim=0.6774 (lo 0.3385 / hi 0.3390) med_prov=0.1031 d_med=0.665772
    [shadow] C4 (B): norm=1.013365 krum=1.915282 mkrum=REJECT tm_trim=0.5932 (lo 0.2970 / hi 0.2963) med_prov=0.1415 d_med=0.574524
    [shadow] C5 (A): norm=0.879329 krum=1.733450 mkrum=KEEP tm_trim=0.4665 (lo 0.2328 / hi 0.2338) med_prov=0.1845 d_med=0.488215
    [shadow] C6 (A): norm=0.878372 krum=1.730442 mkrum=KEEP tm_trim=0.4662 (lo 0.2329 / hi 0.2333) med_prov=0.1848 d_med=0.487784
[shadow] round 3
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.797540 krum=1.400235 mkrum=KEEP tm_trim=0.6482 (lo 0.3236 / hi 0.3246) med_prov=0.1136 d_med=0.512642
    [shadow] C1 (B): norm=0.343250 krum=0.812223 mkrum=KEEP tm_trim=0.5171 (lo 0.2587 / hi 0.2584) med_prov=0.1617 d_med=0.395750
    [shadow] C2 (B): norm=0.389034 krum=0.892518 mkrum=KEEP tm_trim=0.5729 (lo 0.2867 / hi 0.2862) med_prov=0.1408 d_med=0.444619
    [shadow] C3 (B): norm=0.790113 krum=1.445445 mkrum=REJECT tm_trim=0.6543 (lo 0.3274 / hi 0.3269) med_prov=0.1135 d_med=0.542769
    [shadow] C4 (B): norm=0.789663 krum=1.402725 mkrum=REJECT tm_trim=0.6430 (lo 0.3213 / hi 0.3217) med_prov=0.1182 d_med=0.522244
    [shadow] C5 (A): norm=0.655929 krum=1.129692 mkrum=KEEP tm_trim=0.4820 (lo 0.2414 / hi 0.2407) med_prov=0.1761 d_med=0.402297
    [shadow] C6 (A): norm=0.657132 krum=1.132291 mkrum=KEEP tm_trim=0.4824 (lo 0.2410 / hi 0.2414) med_prov=0.1760 d_med=0.403343
[shadow] round 4
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.601862 krum=0.992515 mkrum=KEEP tm_trim=0.6359 (lo 0.3178 / hi 0.3181) med_prov=0.1181 d_med=0.436687
    [shadow] C1 (B): norm=0.313159 krum=0.627507 mkrum=KEEP tm_trim=0.5066 (lo 0.2535 / hi 0.2530) med_prov=0.1687 d_med=0.322626
    [shadow] C2 (B): norm=0.336097 krum=0.656404 mkrum=KEEP tm_trim=0.5424 (lo 0.2714 / hi 0.2710) med_prov=0.1529 d_med=0.344566
    [shadow] C3 (B): norm=0.617252 krum=1.098556 mkrum=REJECT tm_trim=0.6663 (lo 0.3330 / hi 0.3333) med_prov=0.1084 d_med=0.487695
    [shadow] C4 (B): norm=0.644867 krum=1.100318 mkrum=REJECT tm_trim=0.6657 (lo 0.3331 / hi 0.3326) med_prov=0.1084 d_med=0.482213
    [shadow] C5 (A): norm=0.523618 krum=0.824447 mkrum=KEEP tm_trim=0.4916 (lo 0.2455 / hi 0.2460) med_prov=0.1722 d_med=0.351372
    [shadow] C6 (A): norm=0.523692 krum=0.824171 mkrum=KEEP tm_trim=0.4915 (lo 0.2455 / hi 0.2460) med_prov=0.1713 d_med=0.351780
[shadow] round 5
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.551306 krum=0.942830 mkrum=KEEP tm_trim=0.6542 (lo 0.3272 / hi 0.3270) med_prov=0.1111 d_med=0.436075
    [shadow] C1 (B): norm=0.282658 krum=0.578174 mkrum=KEEP tm_trim=0.4945 (lo 0.2471 / hi 0.2474) med_prov=0.1738 d_med=0.300402
    [shadow] C2 (B): norm=0.308478 krum=0.597401 mkrum=KEEP tm_trim=0.5346 (lo 0.2681 / hi 0.2665) med_prov=0.1568 d_med=0.315447
    [shadow] C3 (B): norm=0.552574 krum=1.008450 mkrum=REJECT tm_trim=0.6694 (lo 0.3339 / hi 0.3354) med_prov=0.1059 d_med=0.471294
    [shadow] C4 (B): norm=0.566096 krum=0.982801 mkrum=REJECT tm_trim=0.6565 (lo 0.3284 / hi 0.3281) med_prov=0.1123 d_med=0.457535
    [shadow] C5 (A): norm=0.469648 krum=0.747070 mkrum=KEEP tm_trim=0.4949 (lo 0.2469 / hi 0.2480) med_prov=0.1704 d_med=0.337771
    [shadow] C6 (A): norm=0.470268 krum=0.747947 mkrum=KEEP tm_trim=0.4959 (lo 0.2484 / hi 0.2476) med_prov=0.1697 d_med=0.338446
[shadow] round 6
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C0 (B), C3 (B)
    [shadow] C0 (B): norm=0.514528 krum=0.902211 mkrum=REJECT tm_trim=0.6640 (lo 0.3318 / hi 0.3322) med_prov=0.1085 d_med=0.433331
    [shadow] C1 (B): norm=0.263987 krum=0.539099 mkrum=KEEP tm_trim=0.5067 (lo 0.2534 / hi 0.2533) med_prov=0.1685 d_med=0.291460
    [shadow] C2 (B): norm=0.296837 krum=0.551331 mkrum=KEEP tm_trim=0.5344 (lo 0.2676 / hi 0.2669) med_prov=0.1564 d_med=0.300712
    [shadow] C3 (B): norm=0.496322 krum=0.884287 mkrum=REJECT tm_trim=0.6580 (lo 0.3287 / hi 0.3293) med_prov=0.1101 d_med=0.437400
    [shadow] C4 (B): norm=0.512900 krum=0.875283 mkrum=KEEP tm_trim=0.6476 (lo 0.3235 / hi 0.3241) med_prov=0.1159 d_med=0.428649
    [shadow] C5 (A): norm=0.432340 krum=0.683439 mkrum=KEEP tm_trim=0.4947 (lo 0.2480 / hi 0.2467) med_prov=0.1706 d_med=0.322700
    [shadow] C6 (A): norm=0.431343 krum=0.681850 mkrum=KEEP tm_trim=0.4946 (lo 0.2471 / hi 0.2475) med_prov=0.1700 d_med=0.322310
[shadow] round 7
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.463290 krum=0.812476 mkrum=KEEP tm_trim=0.6474 (lo 0.3234 / hi 0.3240) med_prov=0.1136 d_med=0.407454
    [shadow] C1 (B): norm=0.266272 krum=0.507022 mkrum=KEEP tm_trim=0.4901 (lo 0.2447 / hi 0.2454) med_prov=0.1760 d_med=0.277751
    [shadow] C2 (B): norm=0.278263 krum=0.527452 mkrum=KEEP tm_trim=0.5382 (lo 0.2694 / hi 0.2688) med_prov=0.1562 d_med=0.294630
    [shadow] C3 (B): norm=0.498823 krum=0.896449 mkrum=REJECT tm_trim=0.6816 (lo 0.3406 / hi 0.3409) med_prov=0.1016 d_med=0.448370
    [shadow] C4 (B): norm=0.480349 krum=0.819918 mkrum=REJECT tm_trim=0.6493 (lo 0.3246 / hi 0.3247) med_prov=0.1143 d_med=0.414855
    [shadow] C5 (A): norm=0.410645 krum=0.648341 mkrum=KEEP tm_trim=0.4973 (lo 0.2490 / hi 0.2482) med_prov=0.1692 d_med=0.315113
    [shadow] C6 (A): norm=0.410375 krum=0.647829 mkrum=KEEP tm_trim=0.4961 (lo 0.2481 / hi 0.2479) med_prov=0.1690 d_med=0.314543
[shadow] round 8
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.428726 krum=0.755355 mkrum=KEEP tm_trim=0.6262 (lo 0.3124 / hi 0.3138) med_prov=0.1221 d_med=0.387427
    [shadow] C1 (B): norm=0.260932 krum=0.506555 mkrum=KEEP tm_trim=0.4873 (lo 0.2439 / hi 0.2434) med_prov=0.1774 d_med=0.275183
    [shadow] C2 (B): norm=0.269792 krum=0.527286 mkrum=KEEP tm_trim=0.5405 (lo 0.2703 / hi 0.2701) med_prov=0.1541 d_med=0.292030
    [shadow] C3 (B): norm=0.489746 krum=0.880694 mkrum=REJECT tm_trim=0.6814 (lo 0.3406 / hi 0.3408) med_prov=0.1014 d_med=0.441557
    [shadow] C4 (B): norm=0.499677 krum=0.887229 mkrum=REJECT tm_trim=0.6687 (lo 0.3346 / hi 0.3341) med_prov=0.1075 d_med=0.441774
    [shadow] C5 (A): norm=0.403758 krum=0.645077 mkrum=KEEP tm_trim=0.4985 (lo 0.2496 / hi 0.2489) med_prov=0.1681 d_med=0.315078
    [shadow] C6 (A): norm=0.403853 krum=0.644919 mkrum=KEEP tm_trim=0.4973 (lo 0.2485 / hi 0.2488) med_prov=0.1694 d_med=0.314970
[shadow] round 9
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.451495 krum=0.807713 mkrum=KEEP tm_trim=0.6390 (lo 0.3194 / hi 0.3196) med_prov=0.1173 d_med=0.404391
    [shadow] C1 (B): norm=0.267995 krum=0.518470 mkrum=KEEP tm_trim=0.4880 (lo 0.2437 / hi 0.2443) med_prov=0.1761 d_med=0.277521
    [shadow] C2 (B): norm=0.277869 krum=0.539608 mkrum=KEEP tm_trim=0.5370 (lo 0.2690 / hi 0.2680) med_prov=0.1557 d_med=0.295592
    [shadow] C3 (B): norm=0.489133 krum=0.885021 mkrum=REJECT tm_trim=0.6759 (lo 0.3377 / hi 0.3382) med_prov=0.1038 d_med=0.444194
    [shadow] C4 (B): norm=0.499242 krum=0.883385 mkrum=REJECT tm_trim=0.6656 (lo 0.3331 / hi 0.3325) med_prov=0.1084 d_med=0.437851
    [shadow] C5 (A): norm=0.409892 krum=0.657690 mkrum=KEEP tm_trim=0.4973 (lo 0.2482 / hi 0.2492) med_prov=0.1693 d_med=0.318048
    [shadow] C6 (A): norm=0.410360 krum=0.657904 mkrum=KEEP tm_trim=0.4971 (lo 0.2489 / hi 0.2482) med_prov=0.1693 d_med=0.318308
[shadow] round 10
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.433618 krum=0.761259 mkrum=KEEP tm_trim=0.6401 (lo 0.3202 / hi 0.3198) med_prov=0.1171 d_med=0.393391
    [shadow] C1 (B): norm=0.261002 krum=0.498842 mkrum=KEEP tm_trim=0.4926 (lo 0.2464 / hi 0.2461) med_prov=0.1749 d_med=0.271302
    [shadow] C2 (B): norm=0.262680 krum=0.517519 mkrum=KEEP tm_trim=0.5361 (lo 0.2683 / hi 0.2678) med_prov=0.1560 d_med=0.287117
    [shadow] C3 (B): norm=0.488075 krum=0.864670 mkrum=REJECT tm_trim=0.6805 (lo 0.3396 / hi 0.3410) med_prov=0.1025 d_med=0.441374
    [shadow] C4 (B): norm=0.475667 krum=0.829021 mkrum=REJECT tm_trim=0.6567 (lo 0.3282 / hi 0.3285) med_prov=0.1113 d_med=0.422456
    [shadow] C5 (A): norm=0.397361 krum=0.628521 mkrum=KEEP tm_trim=0.4975 (lo 0.2492 / hi 0.2483) med_prov=0.1687 d_med=0.310803
    [shadow] C6 (A): norm=0.397550 krum=0.628903 mkrum=KEEP tm_trim=0.4965 (lo 0.2480 / hi 0.2484) med_prov=0.1694 d_med=0.311297
[shadow] round 11
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.444449 krum=0.792800 mkrum=KEEP tm_trim=0.6422 (lo 0.3211 / hi 0.3211) med_prov=0.1164 d_med=0.402304
    [shadow] C1 (B): norm=0.270448 krum=0.520438 mkrum=KEEP tm_trim=0.5029 (lo 0.2514 / hi 0.2516) med_prov=0.1707 d_med=0.278829
    [shadow] C2 (B): norm=0.271284 krum=0.546750 mkrum=KEEP tm_trim=0.5476 (lo 0.2740 / hi 0.2736) med_prov=0.1513 d_med=0.300603
    [shadow] C3 (B): norm=0.469403 krum=0.840560 mkrum=REJECT tm_trim=0.6751 (lo 0.3372 / hi 0.3379) med_prov=0.1044 d_med=0.432365
    [shadow] C4 (B): norm=0.457256 krum=0.796295 mkrum=REJECT tm_trim=0.6405 (lo 0.3199 / hi 0.3206) med_prov=0.1178 d_med=0.405638
    [shadow] C5 (A): norm=0.393042 krum=0.634782 mkrum=KEEP tm_trim=0.4956 (lo 0.2481 / hi 0.2475) med_prov=0.1702 d_med=0.309790
    [shadow] C6 (A): norm=0.393176 krum=0.634695 mkrum=KEEP tm_trim=0.4961 (lo 0.2483 / hi 0.2478) med_prov=0.1691 d_med=0.309928
[shadow] round 12
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.401846 krum=0.697551 mkrum=KEEP tm_trim=0.6307 (lo 0.3160 / hi 0.3147) med_prov=0.1207 d_med=0.373368
    [shadow] C1 (B): norm=0.255967 krum=0.480427 mkrum=KEEP tm_trim=0.4883 (lo 0.2437 / hi 0.2446) med_prov=0.1776 d_med=0.264427
    [shadow] C2 (B): norm=0.262574 krum=0.504861 mkrum=KEEP tm_trim=0.5496 (lo 0.2749 / hi 0.2747) med_prov=0.1508 d_med=0.286003
    [shadow] C3 (B): norm=0.465750 krum=0.812527 mkrum=REJECT tm_trim=0.6889 (lo 0.3439 / hi 0.3450) med_prov=0.0993 d_med=0.430296
    [shadow] C4 (B): norm=0.452175 krum=0.761522 mkrum=REJECT tm_trim=0.6493 (lo 0.3248 / hi 0.3245) med_prov=0.1139 d_med=0.402296
    [shadow] C5 (A): norm=0.378515 krum=0.589675 mkrum=KEEP tm_trim=0.4964 (lo 0.2478 / hi 0.2485) med_prov=0.1686 d_med=0.299770
    [shadow] C6 (A): norm=0.378672 krum=0.590504 mkrum=KEEP tm_trim=0.4968 (lo 0.2489 / hi 0.2479) med_prov=0.1690 d_med=0.300074
[shadow] round 13
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.415044 krum=0.705361 mkrum=KEEP tm_trim=0.6362 (lo 0.3183 / hi 0.3178) med_prov=0.1191 d_med=0.377817
    [shadow] C1 (B): norm=0.252355 krum=0.470612 mkrum=KEEP tm_trim=0.4921 (lo 0.2456 / hi 0.2465) med_prov=0.1747 d_med=0.264283
    [shadow] C2 (B): norm=0.262798 krum=0.494667 mkrum=KEEP tm_trim=0.5491 (lo 0.2750 / hi 0.2741) med_prov=0.1509 d_med=0.285935
    [shadow] C3 (B): norm=0.446875 krum=0.775833 mkrum=REJECT tm_trim=0.6738 (lo 0.3368 / hi 0.3370) med_prov=0.1045 d_med=0.414705
    [shadow] C4 (B): norm=0.452574 krum=0.765475 mkrum=REJECT tm_trim=0.6560 (lo 0.3282 / hi 0.3278) med_prov=0.1120 d_med=0.403869
    [shadow] C5 (A): norm=0.376348 krum=0.582773 mkrum=KEEP tm_trim=0.4957 (lo 0.2478 / hi 0.2479) med_prov=0.1697 d_med=0.297811
    [shadow] C6 (A): norm=0.376603 krum=0.582725 mkrum=KEEP tm_trim=0.4971 (lo 0.2483 / hi 0.2489) med_prov=0.1690 d_med=0.297607
[shadow] round 14
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.419454 krum=0.721033 mkrum=KEEP tm_trim=0.6507 (lo 0.3255 / hi 0.3252) med_prov=0.1142 d_med=0.386631
    [shadow] C1 (B): norm=0.258927 krum=0.468625 mkrum=KEEP tm_trim=0.5039 (lo 0.2519 / hi 0.2520) med_prov=0.1690 d_med=0.263945
    [shadow] C2 (B): norm=0.264893 krum=0.486912 mkrum=KEEP tm_trim=0.5423 (lo 0.2716 / hi 0.2707) med_prov=0.1538 d_med=0.281174
    [shadow] C3 (B): norm=0.431572 krum=0.744032 mkrum=REJECT tm_trim=0.6667 (lo 0.3326 / hi 0.3341) med_prov=0.1072 d_med=0.403282
    [shadow] C4 (B): norm=0.435766 krum=0.734349 mkrum=REJECT tm_trim=0.6455 (lo 0.3234 / hi 0.3221) med_prov=0.1164 d_med=0.393902
    [shadow] C5 (A): norm=0.371317 krum=0.571793 mkrum=KEEP tm_trim=0.4954 (lo 0.2477 / hi 0.2476) med_prov=0.1696 d_med=0.294795
    [shadow] C6 (A): norm=0.371422 krum=0.572267 mkrum=KEEP tm_trim=0.4956 (lo 0.2473 / hi 0.2483) med_prov=0.1698 d_med=0.295063
[shadow] round 15
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C0 (B), C3 (B)
    [shadow] C0 (B): norm=0.415358 krum=0.705368 mkrum=REJECT tm_trim=0.6504 (lo 0.3255 / hi 0.3249) med_prov=0.1141 d_med=0.383252
    [shadow] C1 (B): norm=0.256037 krum=0.457026 mkrum=KEEP tm_trim=0.5061 (lo 0.2528 / hi 0.2533) med_prov=0.1685 d_med=0.262771
    [shadow] C2 (B): norm=0.254928 krum=0.472521 mkrum=KEEP tm_trim=0.5430 (lo 0.2721 / hi 0.2709) med_prov=0.1531 d_med=0.276886
    [shadow] C3 (B): norm=0.444135 krum=0.759763 mkrum=REJECT tm_trim=0.6784 (lo 0.3385 / hi 0.3400) med_prov=0.1034 d_med=0.410949
    [shadow] C4 (B): norm=0.408382 krum=0.671241 mkrum=KEEP tm_trim=0.6316 (lo 0.3156 / hi 0.3160) med_prov=0.1212 d_med=0.369583
    [shadow] C5 (A): norm=0.366062 krum=0.557505 mkrum=KEEP tm_trim=0.4960 (lo 0.2481 / hi 0.2479) med_prov=0.1694 d_med=0.291297
    [shadow] C6 (A): norm=0.364909 krum=0.555749 mkrum=KEEP tm_trim=0.4945 (lo 0.2474 / hi 0.2470) med_prov=0.1703 d_med=0.289765
[shadow] round 16
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.407673 krum=0.693490 mkrum=KEEP tm_trim=0.6411 (lo 0.3208 / hi 0.3203) med_prov=0.1168 d_med=0.373419
    [shadow] C1 (B): norm=0.259473 krum=0.465912 mkrum=KEEP tm_trim=0.5080 (lo 0.2542 / hi 0.2538) med_prov=0.1675 d_med=0.267722
    [shadow] C2 (B): norm=0.257000 krum=0.475531 mkrum=KEEP tm_trim=0.5422 (lo 0.2716 / hi 0.2706) med_prov=0.1542 d_med=0.276689
    [shadow] C3 (B): norm=0.434200 krum=0.749464 mkrum=REJECT tm_trim=0.6699 (lo 0.3347 / hi 0.3353) med_prov=0.1062 d_med=0.405246
    [shadow] C4 (B): norm=0.434242 krum=0.727223 mkrum=REJECT tm_trim=0.6497 (lo 0.3250 / hi 0.3246) med_prov=0.1144 d_med=0.394942
    [shadow] C5 (A): norm=0.367943 krum=0.565122 mkrum=KEEP tm_trim=0.4951 (lo 0.2467 / hi 0.2484) med_prov=0.1707 d_med=0.292711
    [shadow] C6 (A): norm=0.367755 krum=0.564251 mkrum=KEEP tm_trim=0.4940 (lo 0.2470 / hi 0.2470) med_prov=0.1701 d_med=0.292226
[shadow] round 17
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.397826 krum=0.661174 mkrum=KEEP tm_trim=0.6393 (lo 0.3195 / hi 0.3198) med_prov=0.1177 d_med=0.366254
    [shadow] C1 (B): norm=0.260417 krum=0.448429 mkrum=KEEP tm_trim=0.5126 (lo 0.2562 / hi 0.2564) med_prov=0.1665 d_med=0.262346
    [shadow] C2 (B): norm=0.257371 krum=0.458296 mkrum=KEEP tm_trim=0.5418 (lo 0.2714 / hi 0.2704) med_prov=0.1540 d_med=0.270111
    [shadow] C3 (B): norm=0.415190 krum=0.703572 mkrum=REJECT tm_trim=0.6692 (lo 0.3343 / hi 0.3349) med_prov=0.1068 d_med=0.393450
    [shadow] C4 (B): norm=0.412825 krum=0.675297 mkrum=REJECT tm_trim=0.6478 (lo 0.3244 / hi 0.3234) med_prov=0.1148 d_med=0.376951
    [shadow] C5 (A): norm=0.356328 krum=0.534026 mkrum=KEEP tm_trim=0.4948 (lo 0.2472 / hi 0.2476) med_prov=0.1701 d_med=0.283950
    [shadow] C6 (A): norm=0.356744 krum=0.533784 mkrum=KEEP tm_trim=0.4945 (lo 0.2470 / hi 0.2475) med_prov=0.1701 d_med=0.283681
[shadow] round 18
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.413490 krum=0.690070 mkrum=KEEP tm_trim=0.6399 (lo 0.3197 / hi 0.3202) med_prov=0.1177 d_med=0.376595
    [shadow] C1 (B): norm=0.264283 krum=0.463644 mkrum=KEEP tm_trim=0.5185 (lo 0.2594 / hi 0.2591) med_prov=0.1633 d_med=0.267296
    [shadow] C2 (B): norm=0.256520 krum=0.477078 mkrum=KEEP tm_trim=0.5477 (lo 0.2743 / hi 0.2734) med_prov=0.1522 d_med=0.280221
    [shadow] C3 (B): norm=0.417636 krum=0.721956 mkrum=REJECT tm_trim=0.6611 (lo 0.3294 / hi 0.3317) med_prov=0.1097 d_med=0.393267
    [shadow] C4 (B): norm=0.414531 krum=0.700049 mkrum=REJECT tm_trim=0.6445 (lo 0.3224 / hi 0.3221) med_prov=0.1163 d_med=0.383322
    [shadow] C5 (A): norm=0.361064 krum=0.555461 mkrum=KEEP tm_trim=0.4940 (lo 0.2473 / hi 0.2468) med_prov=0.1704 d_med=0.288508
    [shadow] C6 (A): norm=0.361530 krum=0.556316 mkrum=KEEP tm_trim=0.4942 (lo 0.2475 / hi 0.2467) med_prov=0.1704 d_med=0.288940
[shadow] round 19
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.385224 krum=0.633468 mkrum=KEEP tm_trim=0.6288 (lo 0.3141 / hi 0.3147) med_prov=0.1217 d_med=0.356651
    [shadow] C1 (B): norm=0.254463 krum=0.444126 mkrum=KEEP tm_trim=0.5083 (lo 0.2539 / hi 0.2544) med_prov=0.1677 d_med=0.259055
    [shadow] C2 (B): norm=0.263181 krum=0.463139 mkrum=KEEP tm_trim=0.5572 (lo 0.2796 / hi 0.2776) med_prov=0.1482 d_med=0.276868
    [shadow] C3 (B): norm=0.406360 krum=0.692688 mkrum=REJECT tm_trim=0.6677 (lo 0.3333 / hi 0.3344) med_prov=0.1066 d_med=0.388295
    [shadow] C4 (B): norm=0.411308 krum=0.686528 mkrum=REJECT tm_trim=0.6495 (lo 0.3254 / hi 0.3241) med_prov=0.1142 d_med=0.381284
    [shadow] C5 (A): norm=0.350914 krum=0.530821 mkrum=KEEP tm_trim=0.4942 (lo 0.2470 / hi 0.2472) med_prov=0.1709 d_med=0.282009
    [shadow] C6 (A): norm=0.350517 krum=0.529757 mkrum=KEEP tm_trim=0.4942 (lo 0.2467 / hi 0.2475) med_prov=0.1708 d_med=0.281945
[shadow] round 20
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.397636 krum=0.649927 mkrum=KEEP tm_trim=0.6455 (lo 0.3227 / hi 0.3228) med_prov=0.1147 d_med=0.365900
    [shadow] C1 (B): norm=0.246951 krum=0.424062 mkrum=KEEP tm_trim=0.5000 (lo 0.2504 / hi 0.2496) med_prov=0.1711 d_med=0.251803
    [shadow] C2 (B): norm=0.256751 krum=0.442205 mkrum=KEEP tm_trim=0.5495 (lo 0.2752 / hi 0.2743) med_prov=0.1515 d_med=0.268732
    [shadow] C3 (B): norm=0.386410 krum=0.656464 mkrum=REJECT tm_trim=0.6632 (lo 0.3311 / hi 0.3321) med_prov=0.1085 d_med=0.376377
    [shadow] C4 (B): norm=0.403084 krum=0.667747 mkrum=REJECT tm_trim=0.6501 (lo 0.3255 / hi 0.3246) med_prov=0.1146 d_med=0.376157
    [shadow] C5 (A): norm=0.345705 krum=0.515079 mkrum=KEEP tm_trim=0.4954 (lo 0.2471 / hi 0.2483) med_prov=0.1699 d_med=0.279282
    [shadow] C6 (A): norm=0.345303 krum=0.513904 mkrum=KEEP tm_trim=0.4963 (lo 0.2481 / hi 0.2482) med_prov=0.1698 d_med=0.278957
[shadow] round 21
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C0 (B), C4 (B)
    [shadow] C0 (B): norm=0.391218 krum=0.642786 mkrum=REJECT tm_trim=0.6471 (lo 0.3240 / hi 0.3231) med_prov=0.1151 d_med=0.365192
    [shadow] C1 (B): norm=0.251843 krum=0.416814 mkrum=KEEP tm_trim=0.5115 (lo 0.2562 / hi 0.2553) med_prov=0.1655 d_med=0.253966
    [shadow] C2 (B): norm=0.256304 krum=0.430429 mkrum=KEEP tm_trim=0.5527 (lo 0.2766 / hi 0.2761) med_prov=0.1499 d_med=0.267089
    [shadow] C3 (B): norm=0.381620 krum=0.628994 mkrum=KEEP tm_trim=0.6503 (lo 0.3250 / hi 0.3253) med_prov=0.1135 d_med=0.364105
    [shadow] C4 (B): norm=0.398544 krum=0.648642 mkrum=REJECT tm_trim=0.6506 (lo 0.3246 / hi 0.3260) med_prov=0.1138 d_med=0.369652
    [shadow] C5 (A): norm=0.342199 krum=0.503470 mkrum=KEEP tm_trim=0.4934 (lo 0.2461 / hi 0.2472) med_prov=0.1712 d_med=0.274747
    [shadow] C6 (A): norm=0.342213 krum=0.503507 mkrum=KEEP tm_trim=0.4944 (lo 0.2475 / hi 0.2469) med_prov=0.1711 d_med=0.274854
[shadow] round 22
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.367298 krum=0.587891 mkrum=KEEP tm_trim=0.6347 (lo 0.3177 / hi 0.3170) med_prov=0.1195 d_med=0.343748
    [shadow] C1 (B): norm=0.246195 krum=0.410888 mkrum=KEEP tm_trim=0.5151 (lo 0.2572 / hi 0.2579) med_prov=0.1649 d_med=0.251362
    [shadow] C2 (B): norm=0.253880 krum=0.420933 mkrum=KEEP tm_trim=0.5501 (lo 0.2750 / hi 0.2751) med_prov=0.1509 d_med=0.260683
    [shadow] C3 (B): norm=0.383407 krum=0.638166 mkrum=REJECT tm_trim=0.6658 (lo 0.3327 / hi 0.3331) med_prov=0.1077 d_med=0.371740
    [shadow] C4 (B): norm=0.392762 krum=0.623506 mkrum=REJECT tm_trim=0.6466 (lo 0.3233 / hi 0.3233) med_prov=0.1156 d_med=0.362619
    [shadow] C5 (A): norm=0.335160 krum=0.485569 mkrum=KEEP tm_trim=0.4939 (lo 0.2470 / hi 0.2470) med_prov=0.1703 d_med=0.270338
    [shadow] C6 (A): norm=0.335268 krum=0.485980 mkrum=KEEP tm_trim=0.4937 (lo 0.2472 / hi 0.2465) med_prov=0.1711 d_med=0.270187
[shadow] round 23
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C0 (B), C3 (B)
    [shadow] C0 (B): norm=0.374875 krum=0.605629 mkrum=REJECT tm_trim=0.6422 (lo 0.3219 / hi 0.3204) med_prov=0.1161 d_med=0.352421
    [shadow] C1 (B): norm=0.242451 krum=0.403954 mkrum=KEEP tm_trim=0.5038 (lo 0.2519 / hi 0.2518) med_prov=0.1694 d_med=0.248408
    [shadow] C2 (B): norm=0.258807 krum=0.421733 mkrum=KEEP tm_trim=0.5644 (lo 0.2826 / hi 0.2818) med_prov=0.1448 d_med=0.264967
    [shadow] C3 (B): norm=0.379146 krum=0.618082 mkrum=REJECT tm_trim=0.6676 (lo 0.3332 / hi 0.3343) med_prov=0.1079 d_med=0.366796
    [shadow] C4 (B): norm=0.373286 krum=0.592201 mkrum=KEEP tm_trim=0.6342 (lo 0.3166 / hi 0.3176) med_prov=0.1203 d_med=0.346810
    [shadow] C5 (A): norm=0.331307 krum=0.480484 mkrum=KEEP tm_trim=0.4933 (lo 0.2463 / hi 0.2470) med_prov=0.1707 d_med=0.267537
    [shadow] C6 (A): norm=0.331404 krum=0.480769 mkrum=KEEP tm_trim=0.4945 (lo 0.2475 / hi 0.2471) med_prov=0.1708 d_med=0.267880
[shadow] round 24
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.355073 krum=0.570869 mkrum=KEEP tm_trim=0.6346 (lo 0.3168 / hi 0.3179) med_prov=0.1192 d_med=0.337463
    [shadow] C1 (B): norm=0.254940 krum=0.398799 mkrum=KEEP tm_trim=0.5257 (lo 0.2639 / hi 0.2618) med_prov=0.1601 d_med=0.251811
    [shadow] C2 (B): norm=0.254706 krum=0.406953 mkrum=KEEP tm_trim=0.5563 (lo 0.2784 / hi 0.2779) med_prov=0.1488 d_med=0.259061
    [shadow] C3 (B): norm=0.359799 krum=0.587051 mkrum=REJECT tm_trim=0.6541 (lo 0.3270 / hi 0.3272) med_prov=0.1121 d_med=0.351315
    [shadow] C4 (B): norm=0.377909 krum=0.598472 mkrum=REJECT tm_trim=0.6478 (lo 0.3234 / hi 0.3244) med_prov=0.1153 d_med=0.352710
    [shadow] C5 (A): norm=0.325110 krum=0.465739 mkrum=KEEP tm_trim=0.4906 (lo 0.2450 / hi 0.2456) med_prov=0.1723 d_med=0.262736
    [shadow] C6 (A): norm=0.324836 krum=0.465608 mkrum=KEEP tm_trim=0.4908 (lo 0.2456 / hi 0.2452) med_prov=0.1722 d_med=0.262360
[shadow] round 25
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.356616 krum=0.552439 mkrum=KEEP tm_trim=0.6320 (lo 0.3162 / hi 0.3158) med_prov=0.1204 d_med=0.331059
    [shadow] C1 (B): norm=0.256621 krum=0.406914 mkrum=KEEP tm_trim=0.5357 (lo 0.2679 / hi 0.2678) med_prov=0.1570 d_med=0.252977
    [shadow] C2 (B): norm=0.255799 krum=0.416518 mkrum=KEEP tm_trim=0.5638 (lo 0.2828 / hi 0.2810) med_prov=0.1445 d_med=0.262987
    [shadow] C3 (B): norm=0.356032 krum=0.562206 mkrum=REJECT tm_trim=0.6474 (lo 0.3230 / hi 0.3243) med_prov=0.1152 d_med=0.343708
    [shadow] C4 (B): norm=0.364991 krum=0.565214 mkrum=REJECT tm_trim=0.6404 (lo 0.3200 / hi 0.3204) med_prov=0.1181 d_med=0.343030
    [shadow] C5 (A): norm=0.321954 krum=0.456928 mkrum=KEEP tm_trim=0.4899 (lo 0.2448 / hi 0.2451) med_prov=0.1732 d_med=0.258506
    [shadow] C6 (A): norm=0.322209 krum=0.457541 mkrum=KEEP tm_trim=0.4909 (lo 0.2453 / hi 0.2456) med_prov=0.1715 d_med=0.258770
[shadow] round 26
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.356116 krum=0.560362 mkrum=KEEP tm_trim=0.6319 (lo 0.3161 / hi 0.3158) med_prov=0.1212 d_med=0.334894
    [shadow] C1 (B): norm=0.253615 krum=0.400993 mkrum=KEEP tm_trim=0.5267 (lo 0.2637 / hi 0.2630) med_prov=0.1596 d_med=0.251072
    [shadow] C2 (B): norm=0.254498 krum=0.411590 mkrum=KEEP tm_trim=0.5632 (lo 0.2821 / hi 0.2811) med_prov=0.1462 d_med=0.261009
    [shadow] C3 (B): norm=0.372433 krum=0.599298 mkrum=REJECT tm_trim=0.6685 (lo 0.3335 / hi 0.3350) med_prov=0.1065 d_med=0.359027
    [shadow] C4 (B): norm=0.361658 krum=0.567319 mkrum=REJECT tm_trim=0.6286 (lo 0.3140 / hi 0.3145) med_prov=0.1220 d_med=0.338521
    [shadow] C5 (A): norm=0.323969 krum=0.461753 mkrum=KEEP tm_trim=0.4906 (lo 0.2447 / hi 0.2459) med_prov=0.1723 d_med=0.260776
    [shadow] C6 (A): norm=0.324369 krum=0.462011 mkrum=KEEP tm_trim=0.4905 (lo 0.2458 / hi 0.2447) med_prov=0.1722 d_med=0.261007
[shadow] round 27
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.346779 krum=0.536999 mkrum=KEEP tm_trim=0.6237 (lo 0.3117 / hi 0.3120) med_prov=0.1230 d_med=0.324700
    [shadow] C1 (B): norm=0.240095 krum=0.391283 mkrum=KEEP tm_trim=0.5145 (lo 0.2569 / hi 0.2577) med_prov=0.1656 d_med=0.246586
    [shadow] C2 (B): norm=0.256115 krum=0.406591 mkrum=KEEP tm_trim=0.5627 (lo 0.2818 / hi 0.2809) med_prov=0.1454 d_med=0.260146
    [shadow] C3 (B): norm=0.386601 krum=0.620189 mkrum=REJECT tm_trim=0.6846 (lo 0.3423 / hi 0.3423) med_prov=0.1009 d_med=0.370759
    [shadow] C4 (B): norm=0.364005 krum=0.558895 mkrum=REJECT tm_trim=0.6336 (lo 0.3163 / hi 0.3173) med_prov=0.1201 d_med=0.336639
    [shadow] C5 (A): norm=0.324154 krum=0.458560 mkrum=KEEP tm_trim=0.4905 (lo 0.2458 / hi 0.2447) med_prov=0.1729 d_med=0.260324
    [shadow] C6 (A): norm=0.324190 krum=0.458254 mkrum=KEEP tm_trim=0.4905 (lo 0.2452 / hi 0.2452) med_prov=0.1721 d_med=0.260460
[shadow] round 28
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.347518 krum=0.529597 mkrum=KEEP tm_trim=0.6355 (lo 0.3169 / hi 0.3186) med_prov=0.1188 d_med=0.325278
    [shadow] C1 (B): norm=0.250601 krum=0.382130 mkrum=KEEP tm_trim=0.5219 (lo 0.2608 / hi 0.2611) med_prov=0.1628 d_med=0.244325
    [shadow] C2 (B): norm=0.252282 krum=0.394618 mkrum=KEEP tm_trim=0.5616 (lo 0.2817 / hi 0.2799) med_prov=0.1456 d_med=0.256544
    [shadow] C3 (B): norm=0.349818 krum=0.552226 mkrum=REJECT tm_trim=0.6678 (lo 0.3337 / hi 0.3341) med_prov=0.1069 d_med=0.344917
    [shadow] C4 (B): norm=0.356030 krum=0.540261 mkrum=REJECT tm_trim=0.6324 (lo 0.3161 / hi 0.3163) med_prov=0.1208 d_med=0.331474
    [shadow] C5 (A): norm=0.315004 krum=0.436841 mkrum=KEEP tm_trim=0.4908 (lo 0.2454 / hi 0.2453) med_prov=0.1721 d_med=0.253482
    [shadow] C6 (A): norm=0.314917 krum=0.436706 mkrum=KEEP tm_trim=0.4899 (lo 0.2453 / hi 0.2446) med_prov=0.1730 d_med=0.253178
[shadow] round 29
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.341681 krum=0.523676 mkrum=KEEP tm_trim=0.6325 (lo 0.3157 / hi 0.3168) med_prov=0.1203 d_med=0.322522
    [shadow] C1 (B): norm=0.242147 krum=0.383575 mkrum=KEEP tm_trim=0.5226 (lo 0.2617 / hi 0.2608) med_prov=0.1616 d_med=0.245108
    [shadow] C2 (B): norm=0.258822 krum=0.398528 mkrum=KEEP tm_trim=0.5731 (lo 0.2868 / hi 0.2863) med_prov=0.1417 d_med=0.259210
    [shadow] C3 (B): norm=0.353397 krum=0.555200 mkrum=REJECT tm_trim=0.6618 (lo 0.3306 / hi 0.3312) med_prov=0.1089 d_med=0.343907
    [shadow] C4 (B): norm=0.353675 krum=0.536088 mkrum=REJECT tm_trim=0.6316 (lo 0.3160 / hi 0.3156) med_prov=0.1217 d_med=0.330534
    [shadow] C5 (A): norm=0.313610 krum=0.436966 mkrum=KEEP tm_trim=0.4898 (lo 0.2445 / hi 0.2454) med_prov=0.1725 d_med=0.252680
    [shadow] C6 (A): norm=0.313746 krum=0.436981 mkrum=KEEP tm_trim=0.4886 (lo 0.2447 / hi 0.2439) med_prov=0.1733 d_med=0.252560
[shadow] round 30
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C0 (B), C4 (B)
    [shadow] C0 (B): norm=0.340081 krum=0.535652 mkrum=REJECT tm_trim=0.6324 (lo 0.3158 / hi 0.3166) med_prov=0.1198 d_med=0.327589
    [shadow] C1 (B): norm=0.246074 krum=0.381499 mkrum=KEEP tm_trim=0.5152 (lo 0.2581 / hi 0.2572) med_prov=0.1651 d_med=0.243055
    [shadow] C2 (B): norm=0.247107 krum=0.391978 mkrum=KEEP tm_trim=0.5532 (lo 0.2768 / hi 0.2764) med_prov=0.1487 d_med=0.254020
    [shadow] C3 (B): norm=0.342694 krum=0.527443 mkrum=KEEP tm_trim=0.6521 (lo 0.3266 / hi 0.3255) med_prov=0.1122 d_med=0.329945
    [shadow] C4 (B): norm=0.389502 krum=0.604302 mkrum=REJECT tm_trim=0.6682 (lo 0.3343 / hi 0.3340) med_prov=0.1079 d_med=0.362161
    [shadow] C5 (A): norm=0.317929 krum=0.442644 mkrum=KEEP tm_trim=0.4892 (lo 0.2442 / hi 0.2450) med_prov=0.1729 d_med=0.256085
    [shadow] C6 (A): norm=0.318264 krum=0.443317 mkrum=KEEP tm_trim=0.4897 (lo 0.2444 / hi 0.2453) med_prov=0.1735 d_med=0.256524
[shadow] round 31
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.341054 krum=0.518243 mkrum=KEEP tm_trim=0.6256 (lo 0.3129 / hi 0.3127) med_prov=0.1222 d_med=0.319604
    [shadow] C1 (B): norm=0.246323 krum=0.382299 mkrum=KEEP tm_trim=0.5211 (lo 0.2602 / hi 0.2609) med_prov=0.1621 d_med=0.246188
    [shadow] C2 (B): norm=0.263031 krum=0.402938 mkrum=KEEP tm_trim=0.5840 (lo 0.2920 / hi 0.2920) med_prov=0.1372 d_med=0.265653
    [shadow] C3 (B): norm=0.344196 krum=0.542272 mkrum=REJECT tm_trim=0.6678 (lo 0.3336 / hi 0.3342) med_prov=0.1066 d_med=0.337063
    [shadow] C4 (B): norm=0.343597 krum=0.533748 mkrum=REJECT tm_trim=0.6301 (lo 0.3154 / hi 0.3147) med_prov=0.1225 d_med=0.327970
    [shadow] C5 (A): norm=0.311115 krum=0.437439 mkrum=KEEP tm_trim=0.4859 (lo 0.2430 / hi 0.2429) med_prov=0.1747 d_med=0.251219
    [shadow] C6 (A): norm=0.310370 krum=0.437148 mkrum=KEEP tm_trim=0.4855 (lo 0.2429 / hi 0.2426) med_prov=0.1748 d_med=0.250936
[shadow] round 32
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.336796 krum=0.512601 mkrum=KEEP tm_trim=0.6325 (lo 0.3159 / hi 0.3166) med_prov=0.1191 d_med=0.317864
    [shadow] C1 (B): norm=0.239325 krum=0.371130 mkrum=KEEP tm_trim=0.5180 (lo 0.2592 / hi 0.2588) med_prov=0.1650 d_med=0.240488
    [shadow] C2 (B): norm=0.248605 krum=0.382501 mkrum=KEEP tm_trim=0.5560 (lo 0.2785 / hi 0.2775) med_prov=0.1475 d_med=0.252081
    [shadow] C3 (B): norm=0.340608 krum=0.531230 mkrum=REJECT tm_trim=0.6523 (lo 0.3262 / hi 0.3261) med_prov=0.1124 d_med=0.331706
    [shadow] C4 (B): norm=0.381532 krum=0.584693 mkrum=REJECT tm_trim=0.6634 (lo 0.3316 / hi 0.3319) med_prov=0.1099 d_med=0.356429
    [shadow] C5 (A): norm=0.314512 krum=0.433342 mkrum=KEEP tm_trim=0.4891 (lo 0.2445 / hi 0.2446) med_prov=0.1729 d_med=0.253256
    [shadow] C6 (A): norm=0.314746 krum=0.433477 mkrum=KEEP tm_trim=0.4887 (lo 0.2442 / hi 0.2445) med_prov=0.1733 d_med=0.253351
[shadow] round 33
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C0 (B), C4 (B)
    [shadow] C0 (B): norm=0.347589 krum=0.533799 mkrum=REJECT tm_trim=0.6369 (lo 0.3186 / hi 0.3183) med_prov=0.1180 d_med=0.326159
    [shadow] C1 (B): norm=0.243418 krum=0.378498 mkrum=KEEP tm_trim=0.5176 (lo 0.2586 / hi 0.2590) med_prov=0.1645 d_med=0.244233
    [shadow] C2 (B): norm=0.251460 krum=0.387272 mkrum=KEEP tm_trim=0.5579 (lo 0.2796 / hi 0.2783) med_prov=0.1468 d_med=0.251868
    [shadow] C3 (B): norm=0.325913 krum=0.521257 mkrum=KEEP tm_trim=0.6416 (lo 0.3203 / hi 0.3212) med_prov=0.1165 d_med=0.324742
    [shadow] C4 (B): norm=0.393288 krum=0.610856 mkrum=REJECT tm_trim=0.6686 (lo 0.3343 / hi 0.3343) med_prov=0.1081 d_med=0.365906
    [shadow] C5 (A): norm=0.317444 krum=0.441621 mkrum=KEEP tm_trim=0.4884 (lo 0.2439 / hi 0.2445) med_prov=0.1732 d_med=0.255872
    [shadow] C6 (A): norm=0.317766 krum=0.441677 mkrum=KEEP tm_trim=0.4889 (lo 0.2447 / hi 0.2443) med_prov=0.1731 d_med=0.255779
[shadow] round 34
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C0 (B), C4 (B)
    [shadow] C0 (B): norm=0.335929 krum=0.498649 mkrum=REJECT tm_trim=0.6369 (lo 0.3186 / hi 0.3183) med_prov=0.1191 d_med=0.317261
    [shadow] C1 (B): norm=0.243322 krum=0.358046 mkrum=KEEP tm_trim=0.5252 (lo 0.2632 / hi 0.2620) med_prov=0.1603 d_med=0.239016
    [shadow] C2 (B): norm=0.240293 krum=0.365633 mkrum=KEEP tm_trim=0.5618 (lo 0.2812 / hi 0.2806) med_prov=0.1461 d_med=0.247968
    [shadow] C3 (B): norm=0.313393 krum=0.468194 mkrum=KEEP tm_trim=0.6492 (lo 0.3240 / hi 0.3252) med_prov=0.1127 d_med=0.305048
    [shadow] C4 (B): norm=0.355595 krum=0.524931 mkrum=REJECT tm_trim=0.6534 (lo 0.3267 / hi 0.3267) med_prov=0.1135 d_med=0.333200
    [shadow] C5 (A): norm=0.301408 krum=0.403604 mkrum=KEEP tm_trim=0.4868 (lo 0.2428 / hi 0.2440) med_prov=0.1742 d_med=0.242271
    [shadow] C6 (A): norm=0.301381 krum=0.403017 mkrum=KEEP tm_trim=0.4867 (lo 0.2436 / hi 0.2431) med_prov=0.1741 d_med=0.242194
[shadow] round 35
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.330656 krum=0.505388 mkrum=KEEP tm_trim=0.6225 (lo 0.3114 / hi 0.3111) med_prov=0.1234 d_med=0.312387
    [shadow] C1 (B): norm=0.243166 krum=0.377172 mkrum=KEEP tm_trim=0.5236 (lo 0.2618 / hi 0.2619) med_prov=0.1617 d_med=0.244067
    [shadow] C2 (B): norm=0.252989 krum=0.389820 mkrum=KEEP tm_trim=0.5633 (lo 0.2824 / hi 0.2808) med_prov=0.1449 d_med=0.256885
    [shadow] C3 (B): norm=0.365003 krum=0.571235 mkrum=REJECT tm_trim=0.6809 (lo 0.3401 / hi 0.3408) med_prov=0.1022 d_med=0.352152
    [shadow] C4 (B): norm=0.357692 krum=0.541564 mkrum=REJECT tm_trim=0.6328 (lo 0.3164 / hi 0.3163) med_prov=0.1208 d_med=0.332757
    [shadow] C5 (A): norm=0.313894 krum=0.434763 mkrum=KEEP tm_trim=0.4881 (lo 0.2436 / hi 0.2445) med_prov=0.1738 d_med=0.252071
    [shadow] C6 (A): norm=0.314519 krum=0.434910 mkrum=KEEP tm_trim=0.4890 (lo 0.2443 / hi 0.2446) med_prov=0.1732 d_med=0.252493
[shadow] round 36
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.337329 krum=0.528801 mkrum=KEEP tm_trim=0.6301 (lo 0.3154 / hi 0.3147) med_prov=0.1207 d_med=0.323511
    [shadow] C1 (B): norm=0.249447 krum=0.381378 mkrum=KEEP tm_trim=0.5268 (lo 0.2639 / hi 0.2629) med_prov=0.1598 d_med=0.247936
    [shadow] C2 (B): norm=0.256414 krum=0.386946 mkrum=KEEP tm_trim=0.5579 (lo 0.2790 / hi 0.2789) med_prov=0.1475 d_med=0.253039
    [shadow] C3 (B): norm=0.352283 krum=0.552228 mkrum=REJECT tm_trim=0.6635 (lo 0.3312 / hi 0.3324) med_prov=0.1082 d_med=0.337600
    [shadow] C4 (B): norm=0.370531 krum=0.571674 mkrum=REJECT tm_trim=0.6479 (lo 0.3234 / hi 0.3245) med_prov=0.1153 d_med=0.345958
    [shadow] C5 (A): norm=0.317357 krum=0.439577 mkrum=KEEP tm_trim=0.4873 (lo 0.2437 / hi 0.2436) med_prov=0.1738 d_med=0.254149
    [shadow] C6 (A): norm=0.317305 krum=0.439742 mkrum=KEEP tm_trim=0.4864 (lo 0.2434 / hi 0.2430) med_prov=0.1747 d_med=0.254105
[shadow] round 37
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C0 (B), C4 (B)
    [shadow] C0 (B): norm=0.338865 krum=0.528210 mkrum=REJECT tm_trim=0.6302 (lo 0.3149 / hi 0.3153) med_prov=0.1208 d_med=0.321578
    [shadow] C1 (B): norm=0.245165 krum=0.382193 mkrum=KEEP tm_trim=0.5197 (lo 0.2601 / hi 0.2595) med_prov=0.1628 d_med=0.244864
    [shadow] C2 (B): norm=0.256932 krum=0.396971 mkrum=KEEP tm_trim=0.5650 (lo 0.2831 / hi 0.2819) med_prov=0.1447 d_med=0.259826
    [shadow] C3 (B): norm=0.323573 krum=0.508224 mkrum=KEEP tm_trim=0.6349 (lo 0.3169 / hi 0.3180) med_prov=0.1183 d_med=0.318394
    [shadow] C4 (B): norm=0.401340 krum=0.620881 mkrum=REJECT tm_trim=0.6739 (lo 0.3368 / hi 0.3371) med_prov=0.1066 d_med=0.368338
    [shadow] C5 (A): norm=0.318245 krum=0.444522 mkrum=KEEP tm_trim=0.4879 (lo 0.2443 / hi 0.2436) med_prov=0.1731 d_med=0.255382
    [shadow] C6 (A): norm=0.319012 krum=0.444999 mkrum=KEEP tm_trim=0.4885 (lo 0.2440 / hi 0.2445) med_prov=0.1737 d_med=0.255772
[shadow] round 38
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.358610 krum=0.561852 mkrum=KEEP tm_trim=0.6393 (lo 0.3202 / hi 0.3191) med_prov=0.1177 d_med=0.336734
    [shadow] C1 (B): norm=0.242347 krum=0.387228 mkrum=KEEP tm_trim=0.5017 (lo 0.2513 / hi 0.2505) med_prov=0.1697 d_med=0.240988
    [shadow] C2 (B): norm=0.249135 krum=0.405006 mkrum=KEEP tm_trim=0.5532 (lo 0.2763 / hi 0.2769) med_prov=0.1490 d_med=0.258231
    [shadow] C3 (B): norm=0.361940 krum=0.582217 mkrum=REJECT tm_trim=0.6637 (lo 0.3314 / hi 0.3323) med_prov=0.1078 d_med=0.352593
    [shadow] C4 (B): norm=0.393769 krum=0.621335 mkrum=REJECT tm_trim=0.6601 (lo 0.3304 / hi 0.3297) med_prov=0.1105 d_med=0.367370
    [shadow] C5 (A): norm=0.327127 krum=0.463059 mkrum=KEEP tm_trim=0.4909 (lo 0.2452 / hi 0.2457) med_prov=0.1722 d_med=0.263819
    [shadow] C6 (A): norm=0.326736 krum=0.462243 mkrum=KEEP tm_trim=0.4910 (lo 0.2453 / hi 0.2458) med_prov=0.1729 d_med=0.263279
[shadow] round 39
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.317928 krum=0.472619 mkrum=KEEP tm_trim=0.6294 (lo 0.3147 / hi 0.3148) med_prov=0.1203 d_med=0.301600
    [shadow] C1 (B): norm=0.250043 krum=0.362031 mkrum=KEEP tm_trim=0.5479 (lo 0.2736 / hi 0.2744) med_prov=0.1511 d_med=0.246132
    [shadow] C2 (B): norm=0.247734 krum=0.364378 mkrum=KEEP tm_trim=0.5622 (lo 0.2814 / hi 0.2807) med_prov=0.1462 d_med=0.248101
    [shadow] C3 (B): norm=0.327490 krum=0.498740 mkrum=REJECT tm_trim=0.6585 (lo 0.3290 / hi 0.3295) med_prov=0.1097 d_med=0.319627
    [shadow] C4 (B): norm=0.344298 krum=0.501064 mkrum=REJECT tm_trim=0.6320 (lo 0.3162 / hi 0.3159) med_prov=0.1216 d_med=0.320113
    [shadow] C5 (A): norm=0.300436 krum=0.402708 mkrum=KEEP tm_trim=0.4845 (lo 0.2424 / hi 0.2421) med_prov=0.1758 d_med=0.240539
    [shadow] C6 (A): norm=0.300354 krum=0.402403 mkrum=KEEP tm_trim=0.4854 (lo 0.2428 / hi 0.2426) med_prov=0.1753 d_med=0.240927
[shadow] round 40
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C2 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.334819 krum=0.511523 mkrum=KEEP tm_trim=0.6283 (lo 0.3140 / hi 0.3143) med_prov=0.1214 d_med=0.316199
    [shadow] C1 (B): norm=0.251709 krum=0.386610 mkrum=KEEP tm_trim=0.5350 (lo 0.2672 / hi 0.2678) med_prov=0.1568 d_med=0.251115
    [shadow] C2 (B): norm=0.242576 krum=0.384608 mkrum=KEEP tm_trim=0.5373 (lo 0.2690 / hi 0.2683) med_prov=0.1552 d_med=0.248711
    [shadow] C3 (B): norm=0.374389 krum=0.593021 mkrum=REJECT tm_trim=0.6619 (lo 0.3304 / hi 0.3315) med_prov=0.1095 d_med=0.356612
    [shadow] C4 (B): norm=0.379703 krum=0.587783 mkrum=REJECT tm_trim=0.6636 (lo 0.3318 / hi 0.3318) med_prov=0.1093 d_med=0.352000
    [shadow] C5 (A): norm=0.321836 krum=0.447321 mkrum=KEEP tm_trim=0.4871 (lo 0.2440 / hi 0.2432) med_prov=0.1733 d_med=0.257523
    [shadow] C6 (A): norm=0.321914 krum=0.447386 mkrum=KEEP tm_trim=0.4868 (lo 0.2436 / hi 0.2432) med_prov=0.1745 d_med=0.257108
[shadow] round 41
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C0 (B), C4 (B)
    [shadow] C0 (B): norm=0.352411 krum=0.533994 mkrum=REJECT tm_trim=0.6448 (lo 0.3224 / hi 0.3224) med_prov=0.1152 d_med=0.325866
    [shadow] C1 (B): norm=0.240231 krum=0.370757 mkrum=KEEP tm_trim=0.5176 (lo 0.2590 / hi 0.2585) med_prov=0.1632 d_med=0.242947
    [shadow] C2 (B): norm=0.249679 krum=0.380757 mkrum=KEEP tm_trim=0.5586 (lo 0.2800 / hi 0.2785) med_prov=0.1474 d_med=0.252093
    [shadow] C3 (B): norm=0.338836 krum=0.529504 mkrum=KEEP tm_trim=0.6538 (lo 0.3266 / hi 0.3273) med_prov=0.1117 d_med=0.331140
    [shadow] C4 (B): norm=0.376214 krum=0.578330 mkrum=REJECT tm_trim=0.6503 (lo 0.3243 / hi 0.3260) med_prov=0.1148 d_med=0.351866
    [shadow] C5 (A): norm=0.315909 krum=0.434339 mkrum=KEEP tm_trim=0.4880 (lo 0.2439 / hi 0.2441) med_prov=0.1737 d_med=0.253417
    [shadow] C6 (A): norm=0.316040 krum=0.434620 mkrum=KEEP tm_trim=0.4870 (lo 0.2438 / hi 0.2432) med_prov=0.1740 d_med=0.253474
[shadow] round 42
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.337049 krum=0.531560 mkrum=KEEP tm_trim=0.6230 (lo 0.3112 / hi 0.3118) med_prov=0.1234 d_med=0.320294
    [shadow] C1 (B): norm=0.248915 krum=0.388509 mkrum=KEEP tm_trim=0.5306 (lo 0.2659 / hi 0.2647) med_prov=0.1578 d_med=0.249896
    [shadow] C2 (B): norm=0.252344 krum=0.396287 mkrum=KEEP tm_trim=0.5586 (lo 0.2794 / hi 0.2792) med_prov=0.1468 d_med=0.256856
    [shadow] C3 (B): norm=0.381346 krum=0.610269 mkrum=REJECT tm_trim=0.6756 (lo 0.3374 / hi 0.3382) med_prov=0.1044 d_med=0.363977
    [shadow] C4 (B): norm=0.370260 krum=0.579939 mkrum=REJECT tm_trim=0.6384 (lo 0.3194 / hi 0.3190) med_prov=0.1195 d_med=0.345616
    [shadow] C5 (A): norm=0.323230 krum=0.456120 mkrum=KEEP tm_trim=0.4870 (lo 0.2431 / hi 0.2440) med_prov=0.1740 d_med=0.259464
    [shadow] C6 (A): norm=0.323139 krum=0.455661 mkrum=KEEP tm_trim=0.4868 (lo 0.2436 / hi 0.2432) med_prov=0.1742 d_med=0.259339
[shadow] round 43
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.349218 krum=0.544970 mkrum=KEEP tm_trim=0.6292 (lo 0.3149 / hi 0.3143) med_prov=0.1207 d_med=0.328012
    [shadow] C1 (B): norm=0.243179 krum=0.382740 mkrum=KEEP tm_trim=0.4997 (lo 0.2501 / hi 0.2496) med_prov=0.1716 d_med=0.240134
    [shadow] C2 (B): norm=0.252012 krum=0.395805 mkrum=KEEP tm_trim=0.5455 (lo 0.2728 / hi 0.2726) med_prov=0.1519 d_med=0.252888
    [shadow] C3 (B): norm=0.381010 krum=0.615575 mkrum=REJECT tm_trim=0.6696 (lo 0.3339 / hi 0.3357) med_prov=0.1065 d_med=0.367717
    [shadow] C4 (B): norm=0.395796 krum=0.634868 mkrum=REJECT tm_trim=0.6726 (lo 0.3361 / hi 0.3365) med_prov=0.1059 d_med=0.372368
    [shadow] C5 (A): norm=0.330504 krum=0.465426 mkrum=KEEP tm_trim=0.4916 (lo 0.2463 / hi 0.2453) med_prov=0.1716 d_med=0.265381
    [shadow] C6 (A): norm=0.330457 krum=0.465211 mkrum=KEEP tm_trim=0.4918 (lo 0.2459 / hi 0.2459) med_prov=0.1718 d_med=0.265035
[shadow] round 44
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.350346 krum=0.554837 mkrum=KEEP tm_trim=0.6295 (lo 0.3148 / hi 0.3147) med_prov=0.1202 d_med=0.330070
    [shadow] C1 (B): norm=0.247674 krum=0.395460 mkrum=KEEP tm_trim=0.5220 (lo 0.2613 / hi 0.2608) med_prov=0.1620 d_med=0.253582
    [shadow] C2 (B): norm=0.249866 krum=0.398404 mkrum=KEEP tm_trim=0.5419 (lo 0.2711 / hi 0.2708) med_prov=0.1540 d_med=0.256111
    [shadow] C3 (B): norm=0.351502 krum=0.572331 mkrum=REJECT tm_trim=0.6665 (lo 0.3322 / hi 0.3343) med_prov=0.1052 d_med=0.342941
    [shadow] C4 (B): norm=0.411733 krum=0.647577 mkrum=REJECT tm_trim=0.6732 (lo 0.3372 / hi 0.3359) med_prov=0.1061 d_med=0.377806
    [shadow] C5 (A): norm=0.328377 krum=0.466968 mkrum=KEEP tm_trim=0.4836 (lo 0.2418 / hi 0.2418) med_prov=0.1761 d_med=0.262979
    [shadow] C6 (A): norm=0.328113 krum=0.466161 mkrum=KEEP tm_trim=0.4833 (lo 0.2416 / hi 0.2417) med_prov=0.1763 d_med=0.262680
[shadow] round 45
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.329567 krum=0.493726 mkrum=KEEP tm_trim=0.6227 (lo 0.3106 / hi 0.3121) med_prov=0.1232 d_med=0.309993
    [shadow] C1 (B): norm=0.250231 krum=0.374339 mkrum=KEEP tm_trim=0.5410 (lo 0.2708 / hi 0.2702) med_prov=0.1531 d_med=0.247535
    [shadow] C2 (B): norm=0.248161 krum=0.377356 mkrum=KEEP tm_trim=0.5595 (lo 0.2803 / hi 0.2792) med_prov=0.1464 d_med=0.250409
    [shadow] C3 (B): norm=0.331888 krum=0.513430 mkrum=REJECT tm_trim=0.6600 (lo 0.3299 / hi 0.3301) med_prov=0.1095 d_med=0.324274
    [shadow] C4 (B): norm=0.372467 krum=0.559319 mkrum=REJECT tm_trim=0.6478 (lo 0.3239 / hi 0.3238) med_prov=0.1164 d_med=0.345163
    [shadow] C5 (A): norm=0.310736 krum=0.423223 mkrum=KEEP tm_trim=0.4840 (lo 0.2420 / hi 0.2420) med_prov=0.1758 d_med=0.248199
    [shadow] C6 (A): norm=0.310151 krum=0.422801 mkrum=KEEP tm_trim=0.4850 (lo 0.2425 / hi 0.2425) med_prov=0.1757 d_med=0.247821
[shadow] round 46
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.324588 krum=0.518641 mkrum=KEEP tm_trim=0.6133 (lo 0.3069 / hi 0.3064) med_prov=0.1268 d_med=0.311640
    [shadow] C1 (B): norm=0.250864 krum=0.395067 mkrum=KEEP tm_trim=0.5347 (lo 0.2674 / hi 0.2673) med_prov=0.1564 d_med=0.252670
    [shadow] C2 (B): norm=0.247677 krum=0.396032 mkrum=KEEP tm_trim=0.5455 (lo 0.2733 / hi 0.2722) med_prov=0.1516 d_med=0.253108
    [shadow] C3 (B): norm=0.395528 krum=0.645877 mkrum=REJECT tm_trim=0.6798 (lo 0.3393 / hi 0.3405) med_prov=0.1030 d_med=0.377425
    [shadow] C4 (B): norm=0.382636 krum=0.604796 mkrum=REJECT tm_trim=0.6493 (lo 0.3247 / hi 0.3246) med_prov=0.1155 d_med=0.356631
    [shadow] C5 (A): norm=0.326395 krum=0.463568 mkrum=KEEP tm_trim=0.4888 (lo 0.2441 / hi 0.2447) med_prov=0.1731 d_med=0.263075
    [shadow] C6 (A): norm=0.326551 krum=0.463305 mkrum=KEEP tm_trim=0.4886 (lo 0.2443 / hi 0.2443) med_prov=0.1737 d_med=0.262901
[shadow] round 47
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C2 (B)
    [shadow] Multi-Krum rejected: C0 (B), C3 (B)
    [shadow] C0 (B): norm=0.359422 krum=0.553657 mkrum=REJECT tm_trim=0.6467 (lo 0.3235 / hi 0.3232) med_prov=0.1154 d_med=0.339217
    [shadow] C1 (B): norm=0.253903 krum=0.387473 mkrum=KEEP tm_trim=0.5430 (lo 0.2716 / hi 0.2715) med_prov=0.1529 d_med=0.252250
    [shadow] C2 (B): norm=0.252225 krum=0.385736 mkrum=KEEP tm_trim=0.5507 (lo 0.2755 / hi 0.2751) med_prov=0.1498 d_med=0.249560
    [shadow] C3 (B): norm=0.346178 krum=0.543742 mkrum=REJECT tm_trim=0.6569 (lo 0.3288 / hi 0.3280) med_prov=0.1105 d_med=0.334491
    [shadow] C4 (B): norm=0.351920 krum=0.533690 mkrum=KEEP tm_trim=0.6330 (lo 0.3163 / hi 0.3166) med_prov=0.1208 d_med=0.329339
    [shadow] C5 (A): norm=0.316747 krum=0.437589 mkrum=KEEP tm_trim=0.4851 (lo 0.2422 / hi 0.2428) med_prov=0.1755 d_med=0.252877
    [shadow] C6 (A): norm=0.316544 krum=0.437171 mkrum=KEEP tm_trim=0.4847 (lo 0.2420 / hi 0.2427) med_prov=0.1750 d_med=0.252966
[shadow] round 48
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C0 (B), C4 (B)
    [shadow] C0 (B): norm=0.342206 krum=0.540115 mkrum=REJECT tm_trim=0.6312 (lo 0.3155 / hi 0.3157) med_prov=0.1203 d_med=0.324191
    [shadow] C1 (B): norm=0.249377 krum=0.400874 mkrum=KEEP tm_trim=0.5354 (lo 0.2671 / hi 0.2684) med_prov=0.1559 d_med=0.255621
    [shadow] C2 (B): norm=0.250785 krum=0.406049 mkrum=KEEP tm_trim=0.5521 (lo 0.2764 / hi 0.2756) med_prov=0.1493 d_med=0.261933
    [shadow] C3 (B): norm=0.337198 krum=0.536603 mkrum=KEEP tm_trim=0.6412 (lo 0.3206 / hi 0.3206) med_prov=0.1155 d_med=0.324910
    [shadow] C4 (B): norm=0.410719 krum=0.648928 mkrum=REJECT tm_trim=0.6739 (lo 0.3370 / hi 0.3368) med_prov=0.1066 d_med=0.376997
    [shadow] C5 (A): norm=0.323856 krum=0.460992 mkrum=KEEP tm_trim=0.4830 (lo 0.2422 / hi 0.2408) med_prov=0.1765 d_med=0.259693
    [shadow] C6 (A): norm=0.323921 krum=0.461559 mkrum=KEEP tm_trim=0.4832 (lo 0.2411 / hi 0.2421) med_prov=0.1758 d_med=0.259486
[shadow] round 49
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C2 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.324341 krum=0.506244 mkrum=KEEP tm_trim=0.6159 (lo 0.3068 / hi 0.3091) med_prov=0.1256 d_med=0.309310
    [shadow] C1 (B): norm=0.255278 krum=0.391703 mkrum=KEEP tm_trim=0.5386 (lo 0.2696 / hi 0.2690) med_prov=0.1533 d_med=0.251135
    [shadow] C2 (B): norm=0.254248 krum=0.391537 mkrum=KEEP tm_trim=0.5434 (lo 0.2718 / hi 0.2716) med_prov=0.1528 d_med=0.249918
    [shadow] C3 (B): norm=0.410480 krum=0.665400 mkrum=REJECT tm_trim=0.6853 (lo 0.3424 / hi 0.3429) med_prov=0.1016 d_med=0.388233
    [shadow] C4 (B): norm=0.361230 krum=0.563849 mkrum=REJECT tm_trim=0.6427 (lo 0.3219 / hi 0.3208) med_prov=0.1172 d_med=0.340633
    [shadow] C5 (A): norm=0.326334 krum=0.455243 mkrum=KEEP tm_trim=0.4873 (lo 0.2440 / hi 0.2433) med_prov=0.1747 d_med=0.260555
    [shadow] C6 (A): norm=0.326729 krum=0.456160 mkrum=KEEP tm_trim=0.4867 (lo 0.2435 / hi 0.2432) med_prov=0.1748 d_med=0.260862
[shadow] round 50
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C0 (B), C4 (B)
    [shadow] C0 (B): norm=0.350329 krum=0.551942 mkrum=REJECT tm_trim=0.6419 (lo 0.3208 / hi 0.3212) med_prov=0.1165 d_med=0.331380
    [shadow] C1 (B): norm=0.252987 krum=0.398700 mkrum=KEEP tm_trim=0.5528 (lo 0.2760 / hi 0.2768) med_prov=0.1473 d_med=0.257129
    [shadow] C2 (B): norm=0.252689 krum=0.401722 mkrum=KEEP tm_trim=0.5539 (lo 0.2776 / hi 0.2763) med_prov=0.1485 d_med=0.262574
    [shadow] C3 (B): norm=0.334631 krum=0.532650 mkrum=KEEP tm_trim=0.6489 (lo 0.3243 / hi 0.3246) med_prov=0.1119 d_med=0.323265
    [shadow] C4 (B): norm=0.385248 krum=0.591701 mkrum=REJECT tm_trim=0.6436 (lo 0.3212 / hi 0.3224) med_prov=0.1191 d_med=0.354907
    [shadow] C5 (A): norm=0.319693 krum=0.452235 mkrum=KEEP tm_trim=0.4794 (lo 0.2402 / hi 0.2391) med_prov=0.1786 d_med=0.255665
    [shadow] C6 (A): norm=0.319722 krum=0.452605 mkrum=KEEP tm_trim=0.4796 (lo 0.2399 / hi 0.2397) med_prov=0.1780 d_med=0.255839

================================================================================
📊 DETAILED EXPERIMENT STATISTICS FOR DATA COLLECTION
================================================================================

--------------------------------------------------------------------------------
1️⃣  GLOBAL ACCURACY (Per Round)
--------------------------------------------------------------------------------
Round    | Clean Accuracy  | Accuracy Change  
--------------------------------------------------------------------------------
1        | 0.456000        |         +0.000000
2        | 0.686667        |         +0.230667
3        | 0.776333        |         +0.089667
4        | 0.803667        |         +0.027333
5        | 0.826667        |         +0.023000
6        | 0.834000        |         +0.007333
7        | 0.848667        |         +0.014667
8        | 0.857333        |         +0.008667
9        | 0.876333        |         +0.019000
10       | 0.876333        |         +0.000000
11       | 0.888000        |         +0.011667
12       | 0.885667        |         -0.002333
13       | 0.889667        |         +0.004000
14       | 0.884333        |         -0.005333
15       | 0.886333        |         +0.002000
16       | 0.886667        |         +0.000333
17       | 0.889000        |         +0.002333
18       | 0.887667        |         -0.001333
19       | 0.887667        |         +0.000000
20       | 0.889667        |         +0.002000
21       | 0.883667        |         -0.006000
22       | 0.888000        |         +0.004333
23       | 0.892333        |         +0.004333
24       | 0.885000        |         -0.007333
25       | 0.895667        |         +0.010667
26       | 0.893667        |         -0.002000
27       | 0.893667        |         +0.000000
28       | 0.892667        |         -0.001000
29       | 0.900000        |         +0.007333
30       | 0.896667        |         -0.003333
31       | 0.896000        |         -0.000667
32       | 0.898000        |         +0.002000
33       | 0.904000        |         +0.006000
34       | 0.899333        |         -0.004667
35       | 0.900000        |         +0.000667
36       | 0.896333        |         -0.003667
37       | 0.901333        |         +0.005000
38       | 0.897333        |         -0.004000
39       | 0.902333        |         +0.005000
40       | 0.898667        |         -0.003667
41       | 0.907667        |         +0.009000
42       | 0.902333        |         -0.005333
43       | 0.900333        |         -0.002000
44       | 0.900667        |         +0.000333
45       | 0.899333        |         -0.001333
46       | 0.901000        |         +0.001667
47       | 0.905667        |         +0.004667
48       | 0.903000        |         -0.002667
49       | 0.911333        |         +0.008333
50       | 0.909000        |         -0.002333
--------------------------------------------------------------------------------
Summary: Initial=0.456000, Final=0.909000, Best=0.911333, Change=+0.453000

--------------------------------------------------------------------------------
2️⃣  COSINE SIMILARITY (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A) | Mean | Std
--------------------------------------------------------------------------------
1      | 0.564395       | 0.561311       | 0.529348       | 0.588887       | 0.573488       | 0.592902       | 0.592223       | 0.571794 | 0.021126
2      | 0.631519       | 0.581607       | 0.453262       | 0.602077       | 0.619239       | 0.613016       | 0.613028       | 0.587678 | 0.056713
3      | 0.517212       | 0.446339       | 0.372279       | 0.475227       | 0.506508       | 0.524446       | 0.524388       | 0.480914 | 0.051806
4      | 0.398304       | 0.333872       | 0.304610       | 0.336503       | 0.388169       | 0.433727       | 0.433666       | 0.375550 | 0.047409
5      | 0.295896       | 0.228410       | 0.218384       | 0.231343       | 0.284082       | 0.350172       | 0.350237       | 0.279789 | 0.052033
6      | 0.213526       | 0.148005       | 0.165300       | 0.176510       | 0.226485       | 0.297063       | 0.296836       | 0.217675 | 0.056004
7      | 0.156629       | 0.135489       | 0.108113       | 0.134634       | 0.178102       | 0.259223       | 0.259545       | 0.175962 | 0.056374
8      | 0.121155       | 0.105317       | 0.069976       | 0.117130       | 0.142916       | 0.233520       | 0.234235       | 0.146321 | 0.058967
9      | 0.133596       | 0.121890       | 0.088151       | 0.116656       | 0.155575       | 0.242973       | 0.243795       | 0.157520 | 0.057412
10     | 0.114793       | 0.102969       | 0.060663       | 0.112885       | 0.136981       | 0.229151       | 0.228568       | 0.140859 | 0.059561
11     | 0.108723       | 0.088012       | 0.026164       | 0.086653       | 0.130500       | 0.216148       | 0.216295       | 0.124642 | 0.064966
12     | 0.083119       | 0.081538       | 0.030161       | 0.080266       | 0.125334       | 0.208975       | 0.208539       | 0.116847 | 0.063475
13     | 0.099548       | 0.080285       | 0.035677       | 0.076383       | 0.121081       | 0.210800       | 0.211624       | 0.119342 | 0.062845
14     | 0.085942       | 0.084124       | 0.044930       | 0.070542       | 0.107877       | 0.207084       | 0.205941       | 0.115206 | 0.060337
15     | 0.083849       | 0.075761       | 0.030777       | 0.075908       | 0.105888       | 0.203476       | 0.204123       | 0.111398 | 0.061985
16     | 0.089046       | 0.070584       | 0.037234       | 0.068004       | 0.100076       | 0.202281       | 0.202724       | 0.109993 | 0.061253
17     | 0.086946       | 0.078384       | 0.044406       | 0.056994       | 0.096789       | 0.201405       | 0.202345       | 0.109610 | 0.060592
18     | 0.090812       | 0.069308       | 0.014998       | 0.054850       | 0.078965       | 0.193364       | 0.193333       | 0.099376 | 0.063424
19     | 0.073098       | 0.060058       | 0.021781       | 0.037673       | 0.071727       | 0.185783       | 0.185306       | 0.090775 | 0.062291
20     | 0.073368       | 0.058802       | 0.023520       | 0.015224       | 0.061768       | 0.179014       | 0.179160       | 0.084408 | 0.062919
21     | 0.064583       | 0.068048       | 0.034494       | 0.043472       | 0.070601       | 0.187666       | 0.187849       | 0.093816 | 0.060664
22     | 0.060157       | 0.052683       | 0.037642       | 0.021886       | 0.073738       | 0.181924       | 0.182088       | 0.087160 | 0.061878
23     | 0.052302       | 0.050276       | 0.028694       | 0.022506       | 0.066995       | 0.177724       | 0.177397       | 0.082271 | 0.061827
24     | 0.045114       | 0.063181       | 0.036164       | 0.017860       | 0.060958       | 0.177816       | 0.177649       | 0.082677 | 0.061758
25     | 0.070048       | 0.064985       | 0.030943       | 0.035328       | 0.061478       | 0.186175       | 0.185914       | 0.090696 | 0.061829
26     | 0.058156       | 0.065671       | 0.032560       | 0.028458       | 0.063803       | 0.182200       | 0.182530       | 0.087625 | 0.061414
27     | 0.065952       | 0.052139       | 0.040574       | 0.033064       | 0.076077       | 0.185382       | 0.185403       | 0.091227 | 0.061038
28     | 0.064454       | 0.074449       | 0.036650       | 0.010336       | 0.068860       | 0.183179       | 0.184016       | 0.088849 | 0.063297
29     | 0.052095       | 0.050383       | 0.038632       | 0.020803       | 0.063565       | 0.179245       | 0.179733       | 0.083494 | 0.061936
30     | 0.036763       | 0.066707       | 0.032038       | 0.034469       | 0.063030       | 0.179756       | 0.179594       | 0.084622 | 0.061445
31     | 0.058802       | 0.052268       | 0.023490       | 0.010348       | 0.041473       | 0.172796       | 0.171703       | 0.075840 | 0.062845
32     | 0.054665       | 0.059812       | 0.039476       | 0.023025       | 0.060180       | 0.180381       | 0.180625       | 0.085452 | 0.061324
33     | 0.059922       | 0.059288       | 0.046653       | 0.007226       | 0.062844       | 0.180005       | 0.180410       | 0.085193 | 0.062597
34     | 0.053071       | 0.065731       | 0.026717       | 0.025715       | 0.058604       | 0.180152       | 0.180183       | 0.084311 | 0.062232
35     | 0.057386       | 0.059716       | 0.039652       | 0.026979       | 0.069267       | 0.182902       | 0.183629       | 0.088504 | 0.061294
36     | 0.047151       | 0.069234       | 0.065516       | 0.041401       | 0.066331       | 0.188529       | 0.188778       | 0.095277 | 0.059832
37     | 0.052911       | 0.067648       | 0.041750       | 0.024521       | 0.077742       | 0.185065       | 0.185693       | 0.090761 | 0.061912
38     | 0.057404       | 0.072393       | 0.029297       | 0.019572       | 0.061060       | 0.179980       | 0.180275       | 0.085712 | 0.062074
39     | 0.054356       | 0.064060       | 0.049733       | 0.025020       | 0.069642       | 0.186197       | 0.185582       | 0.090656 | 0.061631
40     | 0.063483       | 0.067361       | 0.055145       | 0.047403       | 0.071204       | 0.191009       | 0.191314       | 0.098131 | 0.059285
41     | 0.073109       | 0.062370       | 0.049062       | 0.023401       | 0.063337       | 0.186219       | 0.186467       | 0.091995 | 0.061420
42     | 0.053483       | 0.062832       | 0.045597       | 0.039025       | 0.064248       | 0.184753       | 0.185322       | 0.090752 | 0.060197
43     | 0.069007       | 0.083662       | 0.059892       | 0.033440       | 0.057340       | 0.189229       | 0.189753       | 0.097475 | 0.059832
44     | 0.060864       | 0.055084       | 0.048215       | 0.023322       | 0.078129       | 0.185277       | 0.185199       | 0.090870 | 0.061570
45     | 0.067015       | 0.066970       | 0.050381       | 0.027580       | 0.075289       | 0.190186       | 0.189852       | 0.095325 | 0.061587
46     | 0.045021       | 0.055713       | 0.045960       | 0.036842       | 0.063240       | 0.180882       | 0.181291       | 0.086993 | 0.060013
47     | 0.061085       | 0.065778       | 0.067234       | 0.039001       | 0.069240       | 0.191690       | 0.191345       | 0.097911 | 0.059936
48     | 0.053221       | 0.045938       | 0.028725       | 0.038323       | 0.074972       | 0.182482       | 0.182376       | 0.086577 | 0.062048
49     | 0.063778       | 0.080561       | 0.080805       | 0.055830       | 0.066225       | 0.197090       | 0.197227       | 0.105931 | 0.058289
50     | 0.053232       | 0.046823       | 0.034016       | 0.034057       | 0.076237       | 0.183473       | 0.183034       | 0.087267 | 0.062117
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
2b. EUCLIDEAN DISTANCE (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A) | Mean | Std
--------------------------------------------------------------------------------
1      | 0.748197       | 0.772142       | 0.808414       | 0.791900       | 0.781588       | 0.558498       | 0.707719       | 0.738351 | 0.079435
2      | 0.539058       | 0.587593       | 0.687017       | 0.577017       | 0.533449       | 0.421615       | 0.532438       | 0.554027 | 0.073667
3      | 0.472324       | 0.457791       | 0.510549       | 0.484660       | 0.475037       | 0.342946       | 0.435001       | 0.454044 | 0.050177
4      | 0.413323       | 0.377083       | 0.401287       | 0.441631       | 0.441646       | 0.296011       | 0.376277       | 0.392465 | 0.046523
5      | 0.412929       | 0.351386       | 0.369217       | 0.429866       | 0.422274       | 0.283070       | 0.360311       | 0.375579 | 0.047718
6      | 0.407238       | 0.338550       | 0.350835       | 0.399998       | 0.396758       | 0.270381       | 0.343471       | 0.358176 | 0.044734
7      | 0.387987       | 0.323725       | 0.343472       | 0.404621       | 0.387316       | 0.263633       | 0.335018       | 0.349396 | 0.045092
8      | 0.376639       | 0.320734       | 0.341335       | 0.400985       | 0.404490       | 0.263568       | 0.334926       | 0.348954 | 0.046136
9      | 0.389607       | 0.322926       | 0.344110       | 0.404425       | 0.403280       | 0.266054       | 0.338316       | 0.352674 | 0.046707
10     | 0.379934       | 0.315274       | 0.334547       | 0.400973       | 0.389743       | 0.259749       | 0.331010       | 0.344461 | 0.045996
11     | 0.385132       | 0.318285       | 0.344774       | 0.393240       | 0.377116       | 0.259028       | 0.329745       | 0.343903 | 0.043586
12     | 0.362111       | 0.303648       | 0.329280       | 0.389864       | 0.373323       | 0.250645       | 0.319071       | 0.332563 | 0.044009
13     | 0.365007       | 0.303988       | 0.328568       | 0.378174       | 0.372148       | 0.249071       | 0.316672       | 0.330518 | 0.042639
14     | 0.370018       | 0.302487       | 0.322298       | 0.369657       | 0.363964       | 0.246342       | 0.314205       | 0.326996 | 0.041967
15     | 0.364187       | 0.301335       | 0.318325       | 0.372824       | 0.346688       | 0.243332       | 0.308526       | 0.322174 | 0.041028
16     | 0.357892       | 0.306673       | 0.318146       | 0.370396       | 0.364279       | 0.244924       | 0.311463       | 0.324825 | 0.040819
17     | 0.350359       | 0.298398       | 0.309801       | 0.358941       | 0.348573       | 0.237583       | 0.302268       | 0.315132 | 0.039218
18     | 0.357581       | 0.305212       | 0.319872       | 0.359893       | 0.354650       | 0.241856       | 0.307965       | 0.321004 | 0.039037
19     | 0.342271       | 0.295312       | 0.316149       | 0.354513       | 0.351035       | 0.236103       | 0.300549       | 0.313705 | 0.038571
20     | 0.348097       | 0.287332       | 0.307734       | 0.346286       | 0.347793       | 0.233554       | 0.297101       | 0.309700 | 0.039143
21     | 0.345093       | 0.290498       | 0.306115       | 0.334632       | 0.340805       | 0.230292       | 0.292890       | 0.305761 | 0.037231
22     | 0.330489       | 0.285262       | 0.297019       | 0.339889       | 0.334441       | 0.226313       | 0.287700       | 0.300159 | 0.036866
23     | 0.333355       | 0.281319       | 0.302185       | 0.335887       | 0.322029       | 0.224207       | 0.285471       | 0.297779 | 0.036175
24     | 0.320917       | 0.284657       | 0.294759       | 0.322141       | 0.324028       | 0.220342       | 0.280145       | 0.292427 | 0.034030
25     | 0.315972       | 0.282292       | 0.294086       | 0.315312       | 0.316733       | 0.216762       | 0.276028       | 0.288169 | 0.033040
26     | 0.321936       | 0.281876       | 0.295135       | 0.326829       | 0.311727       | 0.218935       | 0.278746       | 0.290741 | 0.034046
27     | 0.312058       | 0.278045       | 0.295483       | 0.335030       | 0.312720       | 0.218437       | 0.278116       | 0.289984 | 0.034777
28     | 0.309639       | 0.273015       | 0.288276       | 0.316144       | 0.306714       | 0.212801       | 0.270253       | 0.282406 | 0.032920
29     | 0.307600       | 0.273171       | 0.291005       | 0.314124       | 0.306085       | 0.212230       | 0.269937       | 0.282022 | 0.032601
30     | 0.312785       | 0.273274       | 0.286593       | 0.307209       | 0.330422       | 0.214990       | 0.273768       | 0.285577 | 0.034834
31     | 0.303933       | 0.274648       | 0.298217       | 0.306234       | 0.301925       | 0.211666       | 0.268975       | 0.280800 | 0.031371
32     | 0.305260       | 0.270836       | 0.285040       | 0.306192       | 0.325071       | 0.212623       | 0.270581       | 0.282229 | 0.033930
33     | 0.311618       | 0.274775       | 0.285830       | 0.301599       | 0.333131       | 0.214601       | 0.273270       | 0.284975 | 0.034846
34     | 0.300869       | 0.265726       | 0.276455       | 0.284133       | 0.304939       | 0.203657       | 0.259334       | 0.270731 | 0.031498
35     | 0.300310       | 0.273627       | 0.289165       | 0.320479       | 0.306555       | 0.212101       | 0.270072       | 0.281759 | 0.032881
36     | 0.308743       | 0.277807       | 0.285685       | 0.310810       | 0.316902       | 0.213834       | 0.271780       | 0.283652 | 0.032791
37     | 0.307524       | 0.274809       | 0.292538       | 0.296617       | 0.334466       | 0.214648       | 0.273398       | 0.284857 | 0.034504
38     | 0.324734       | 0.272500       | 0.293131       | 0.325297       | 0.335977       | 0.220983       | 0.280900       | 0.293360 | 0.037128
39     | 0.287522       | 0.273252       | 0.277131       | 0.292633       | 0.293737       | 0.202564       | 0.258013       | 0.269265 | 0.029596
40     | 0.306444       | 0.282978       | 0.282121       | 0.324938       | 0.322213       | 0.216299       | 0.275184       | 0.287168 | 0.034300
41     | 0.310857       | 0.273191       | 0.285517       | 0.305982       | 0.321228       | 0.213006       | 0.270823       | 0.282943 | 0.033627
42     | 0.307522       | 0.282055       | 0.292102       | 0.330674       | 0.318098       | 0.218167       | 0.277321       | 0.289420 | 0.034094
43     | 0.316092       | 0.275074       | 0.290840       | 0.335993       | 0.341169       | 0.222486       | 0.282841       | 0.294928 | 0.037942
44     | 0.315956       | 0.286454       | 0.290884       | 0.317376       | 0.343052       | 0.221262       | 0.281506       | 0.293784 | 0.035753
45     | 0.295686       | 0.276661       | 0.281609       | 0.299724       | 0.313435       | 0.208926       | 0.265363       | 0.277344 | 0.031584
46     | 0.301878       | 0.286749       | 0.289305       | 0.342318       | 0.327461       | 0.220750       | 0.280818       | 0.292754 | 0.036094
47     | 0.319371       | 0.281347       | 0.280942       | 0.307750       | 0.304391       | 0.212643       | 0.270747       | 0.282456 | 0.032729
48     | 0.311113       | 0.286869       | 0.294028       | 0.302752       | 0.340008       | 0.218701       | 0.278045       | 0.290217 | 0.034561
49     | 0.300473       | 0.284566       | 0.285991       | 0.347778       | 0.316081       | 0.218754       | 0.278417       | 0.290294 | 0.036613
50     | 0.314093       | 0.287047       | 0.291809       | 0.298667       | 0.324168       | 0.215815       | 0.274586       | 0.286598 | 0.032722
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
2c. GLOBAL LOSS (Per Round)
--------------------------------------------------------------------------------
Round    | Global Loss    
--------------------------------------------------------------------------------
1        | 1.984382       
2        | 0.981970       
3        | 0.650285       
4        | 0.550737       
5        | 0.518870       
6        | 0.486263       
7        | 0.458532       
8        | 0.456924       
9        | 0.405705       
10       | 0.405310       
11       | 0.384544       
12       | 0.408299       
13       | 0.408592       
14       | 0.430339       
15       | 0.454369       
16       | 0.458663       
17       | 0.455332       
18       | 0.509548       
19       | 0.529315       
20       | 0.541540       
21       | 0.586228       
22       | 0.597276       
23       | 0.609045       
24       | 0.643946       
25       | 0.596709       
26       | 0.656820       
27       | 0.678839       
28       | 0.687015       
29       | 0.637083       
30       | 0.696177       
31       | 0.727422       
32       | 0.708280       
33       | 0.658955       
34       | 0.750789       
35       | 0.765573       
36       | 0.744218       
37       | 0.755798       
38       | 0.802848       
39       | 0.776872       
40       | 0.798169       
41       | 0.772955       
42       | 0.823591       
43       | 0.833587       
44       | 0.799561       
45       | 0.824938       
46       | 0.830569       
47       | 0.768381       
48       | 0.855645       
49       | 0.768106       
50       | 0.829971       
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
3️⃣  LOCAL ACCURACY (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A) | Mean | Std
--------------------------------------------------------------------------------
1      | 0.592391       | 0.222826       | 0.326087       | 0.592391       | 0.445652       | 0.222826       | 0.222826       | 0.375000 | 0.156467
2      | 0.766304       | 0.559783       | 0.434783       | 0.663043       | 0.527174       | 0.418478       | 0.418478       | 0.541149 | 0.123927
3      | 0.831522       | 0.684783       | 0.581522       | 0.668478       | 0.581522       | 0.657609       | 0.657609       | 0.666149 | 0.077616
4      | 0.864130       | 0.782609       | 0.619565       | 0.668478       | 0.619565       | 0.744565       | 0.744565       | 0.720497 | 0.083433
5      | 0.864130       | 0.809783       | 0.630435       | 0.668478       | 0.630435       | 0.760870       | 0.760870       | 0.732143 | 0.084381
6      | 0.869565       | 0.793478       | 0.668478       | 0.673913       | 0.652174       | 0.777174       | 0.777174       | 0.744565 | 0.075082
7      | 0.869565       | 0.777174       | 0.646739       | 0.673913       | 0.668478       | 0.793478       | 0.793478       | 0.746118 | 0.077282
8      | 0.853261       | 0.847826       | 0.717391       | 0.668478       | 0.684783       | 0.820652       | 0.820652       | 0.773292 | 0.074047
9      | 0.864130       | 0.836957       | 0.695652       | 0.684783       | 0.695652       | 0.831522       | 0.831522       | 0.777174 | 0.074518
10     | 0.875000       | 0.847826       | 0.706522       | 0.679348       | 0.717391       | 0.853261       | 0.853261       | 0.790373 | 0.078428
11     | 0.880435       | 0.815217       | 0.701087       | 0.679348       | 0.739130       | 0.847826       | 0.847826       | 0.787267 | 0.073860
12     | 0.858696       | 0.875000       | 0.766304       | 0.679348       | 0.744565       | 0.864130       | 0.864130       | 0.807453 | 0.071386
13     | 0.875000       | 0.896739       | 0.766304       | 0.684783       | 0.739130       | 0.880435       | 0.880435       | 0.817547 | 0.079177
14     | 0.869565       | 0.847826       | 0.777174       | 0.684783       | 0.722826       | 0.896739       | 0.896739       | 0.813665 | 0.079542
15     | 0.875000       | 0.858696       | 0.793478       | 0.684783       | 0.755435       | 0.885870       | 0.885870       | 0.819876 | 0.072067
16     | 0.875000       | 0.885870       | 0.771739       | 0.684783       | 0.711957       | 0.885870       | 0.885870       | 0.814441 | 0.082904
17     | 0.885870       | 0.875000       | 0.809783       | 0.684783       | 0.760870       | 0.875000       | 0.875000       | 0.823758 | 0.070912
18     | 0.875000       | 0.869565       | 0.793478       | 0.684783       | 0.755435       | 0.880435       | 0.880435       | 0.819876 | 0.071656
19     | 0.885870       | 0.875000       | 0.788043       | 0.673913       | 0.755435       | 0.869565       | 0.869565       | 0.816770 | 0.074388
20     | 0.885870       | 0.885870       | 0.798913       | 0.690217       | 0.793478       | 0.869565       | 0.869565       | 0.827640 | 0.066734
21     | 0.864130       | 0.853261       | 0.798913       | 0.695652       | 0.744565       | 0.885870       | 0.885870       | 0.818323 | 0.068982
22     | 0.880435       | 0.885870       | 0.804348       | 0.711957       | 0.744565       | 0.858696       | 0.858696       | 0.820652 | 0.063910
23     | 0.880435       | 0.847826       | 0.793478       | 0.695652       | 0.788043       | 0.864130       | 0.864130       | 0.819099 | 0.060360
24     | 0.880435       | 0.820652       | 0.793478       | 0.701087       | 0.750000       | 0.858696       | 0.858696       | 0.809006 | 0.060410
25     | 0.880435       | 0.858696       | 0.793478       | 0.739130       | 0.777174       | 0.858696       | 0.858696       | 0.823758 | 0.049458
26     | 0.875000       | 0.847826       | 0.804348       | 0.711957       | 0.771739       | 0.858696       | 0.858696       | 0.818323 | 0.054801
27     | 0.880435       | 0.864130       | 0.815217       | 0.717391       | 0.750000       | 0.864130       | 0.864130       | 0.822205 | 0.059656
28     | 0.880435       | 0.836957       | 0.782609       | 0.701087       | 0.798913       | 0.869565       | 0.869565       | 0.819876 | 0.059565
29     | 0.880435       | 0.891304       | 0.798913       | 0.728261       | 0.771739       | 0.864130       | 0.864130       | 0.828416 | 0.057726
30     | 0.891304       | 0.847826       | 0.815217       | 0.739130       | 0.777174       | 0.875000       | 0.875000       | 0.831522 | 0.052612
31     | 0.885870       | 0.864130       | 0.777174       | 0.706522       | 0.760870       | 0.869565       | 0.869565       | 0.819099 | 0.064809
32     | 0.891304       | 0.853261       | 0.836957       | 0.760870       | 0.793478       | 0.869565       | 0.869565       | 0.839286 | 0.043074
33     | 0.891304       | 0.858696       | 0.820652       | 0.750000       | 0.820652       | 0.875000       | 0.875000       | 0.841615 | 0.045138
34     | 0.896739       | 0.853261       | 0.809783       | 0.739130       | 0.793478       | 0.891304       | 0.891304       | 0.839286 | 0.055944
35     | 0.896739       | 0.880435       | 0.793478       | 0.722826       | 0.826087       | 0.880435       | 0.880435       | 0.840062 | 0.058812
36     | 0.891304       | 0.842391       | 0.809783       | 0.744565       | 0.809783       | 0.875000       | 0.875000       | 0.835404 | 0.047620
37     | 0.891304       | 0.842391       | 0.793478       | 0.750000       | 0.755435       | 0.864130       | 0.864130       | 0.822981 | 0.052359
38     | 0.891304       | 0.875000       | 0.809783       | 0.728261       | 0.771739       | 0.869565       | 0.869565       | 0.830745 | 0.057401
39     | 0.885870       | 0.847826       | 0.826087       | 0.750000       | 0.842391       | 0.869565       | 0.869565       | 0.841615 | 0.041738
40     | 0.885870       | 0.820652       | 0.831522       | 0.782609       | 0.739130       | 0.880435       | 0.880435       | 0.831522 | 0.051804
41     | 0.902174       | 0.880435       | 0.788043       | 0.750000       | 0.815217       | 0.869565       | 0.869565       | 0.839286 | 0.051629
42     | 0.891304       | 0.836957       | 0.804348       | 0.771739       | 0.820652       | 0.885870       | 0.885870       | 0.842391 | 0.043284
43     | 0.880435       | 0.880435       | 0.815217       | 0.739130       | 0.760870       | 0.891304       | 0.891304       | 0.836957 | 0.060380
44     | 0.891304       | 0.875000       | 0.826087       | 0.750000       | 0.788043       | 0.875000       | 0.875000       | 0.840062 | 0.049714
45     | 0.875000       | 0.875000       | 0.820652       | 0.744565       | 0.847826       | 0.880435       | 0.880435       | 0.846273 | 0.046272
46     | 0.885870       | 0.864130       | 0.831522       | 0.766304       | 0.836957       | 0.864130       | 0.864130       | 0.844720 | 0.036267
47     | 0.885870       | 0.858696       | 0.804348       | 0.804348       | 0.842391       | 0.880435       | 0.880435       | 0.850932 | 0.032590
48     | 0.902174       | 0.853261       | 0.820652       | 0.788043       | 0.820652       | 0.880435       | 0.880435       | 0.849379 | 0.038067
49     | 0.896739       | 0.836957       | 0.804348       | 0.798913       | 0.842391       | 0.885870       | 0.885870       | 0.850155 | 0.037186
50     | 0.875000       | 0.853261       | 0.804348       | 0.793478       | 0.831522       | 0.891304       | 0.891304       | 0.848602 | 0.037137
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
4️⃣  SHADOW KRUM SCORE (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A) | Selected | SelIsAtk
--------------------------------------------------------------------------------
1      | 3.199984       | 1.950418       | 2.038867       | 3.472590       | 3.289043       | 2.953588       | 2.954827       | 1        | 0       
2      | 1.859704       | 1.174375       | 1.377192       | 1.988635       | 1.915282       | 1.733450       | 1.730442       | 1        | 0       
3      | 1.400235       | 0.812223       | 0.892518       | 1.445445       | 1.402725       | 1.129692       | 1.132291       | 1        | 0       
4      | 0.992515       | 0.627507       | 0.656404       | 1.098556       | 1.100318       | 0.824447       | 0.824171       | 1        | 0       
5      | 0.942830       | 0.578174       | 0.597401       | 1.008450       | 0.982801       | 0.747070       | 0.747947       | 1        | 0       
6      | 0.902211       | 0.539099       | 0.551331       | 0.884287       | 0.875283       | 0.683439       | 0.681850       | 1        | 0       
7      | 0.812476       | 0.507022       | 0.527452       | 0.896449       | 0.819918       | 0.648341       | 0.647829       | 1        | 0       
8      | 0.755355       | 0.506555       | 0.527286       | 0.880694       | 0.887229       | 0.645077       | 0.644919       | 1        | 0       
9      | 0.807713       | 0.518470       | 0.539608       | 0.885021       | 0.883385       | 0.657690       | 0.657904       | 1        | 0       
10     | 0.761259       | 0.498842       | 0.517519       | 0.864670       | 0.829021       | 0.628521       | 0.628903       | 1        | 0       
11     | 0.792800       | 0.520438       | 0.546750       | 0.840560       | 0.796295       | 0.634782       | 0.634695       | 1        | 0       
12     | 0.697551       | 0.480427       | 0.504861       | 0.812527       | 0.761522       | 0.589675       | 0.590504       | 1        | 0       
13     | 0.705361       | 0.470612       | 0.494667       | 0.775833       | 0.765475       | 0.582773       | 0.582725       | 1        | 0       
14     | 0.721033       | 0.468625       | 0.486912       | 0.744032       | 0.734349       | 0.571793       | 0.572267       | 1        | 0       
15     | 0.705368       | 0.457026       | 0.472521       | 0.759763       | 0.671241       | 0.557505       | 0.555749       | 1        | 0       
16     | 0.693490       | 0.465912       | 0.475531       | 0.749464       | 0.727223       | 0.565122       | 0.564251       | 1        | 0       
17     | 0.661174       | 0.448429       | 0.458296       | 0.703572       | 0.675297       | 0.534026       | 0.533784       | 1        | 0       
18     | 0.690070       | 0.463644       | 0.477078       | 0.721956       | 0.700049       | 0.555461       | 0.556316       | 1        | 0       
19     | 0.633468       | 0.444126       | 0.463139       | 0.692688       | 0.686528       | 0.530821       | 0.529757       | 1        | 0       
20     | 0.649927       | 0.424062       | 0.442205       | 0.656464       | 0.667747       | 0.515079       | 0.513904       | 1        | 0       
21     | 0.642786       | 0.416814       | 0.430429       | 0.628994       | 0.648642       | 0.503470       | 0.503507       | 1        | 0       
22     | 0.587891       | 0.410888       | 0.420933       | 0.638166       | 0.623506       | 0.485569       | 0.485980       | 1        | 0       
23     | 0.605629       | 0.403954       | 0.421733       | 0.618082       | 0.592201       | 0.480484       | 0.480769       | 1        | 0       
24     | 0.570869       | 0.398799       | 0.406953       | 0.587051       | 0.598472       | 0.465739       | 0.465608       | 1        | 0       
25     | 0.552439       | 0.406914       | 0.416518       | 0.562206       | 0.565214       | 0.456928       | 0.457541       | 1        | 0       
26     | 0.560362       | 0.400993       | 0.411590       | 0.599298       | 0.567319       | 0.461753       | 0.462011       | 1        | 0       
27     | 0.536999       | 0.391283       | 0.406591       | 0.620189       | 0.558895       | 0.458560       | 0.458254       | 1        | 0       
28     | 0.529597       | 0.382130       | 0.394618       | 0.552226       | 0.540261       | 0.436841       | 0.436706       | 1        | 0       
29     | 0.523676       | 0.383575       | 0.398528       | 0.555200       | 0.536088       | 0.436966       | 0.436981       | 1        | 0       
30     | 0.535652       | 0.381499       | 0.391978       | 0.527443       | 0.604302       | 0.442644       | 0.443317       | 1        | 0       
31     | 0.518243       | 0.382299       | 0.402938       | 0.542272       | 0.533748       | 0.437439       | 0.437148       | 1        | 0       
32     | 0.512601       | 0.371130       | 0.382501       | 0.531230       | 0.584693       | 0.433342       | 0.433477       | 1        | 0       
33     | 0.533799       | 0.378498       | 0.387272       | 0.521257       | 0.610856       | 0.441621       | 0.441677       | 1        | 0       
34     | 0.498649       | 0.358046       | 0.365633       | 0.468194       | 0.524931       | 0.403604       | 0.403017       | 1        | 0       
35     | 0.505388       | 0.377172       | 0.389820       | 0.571235       | 0.541564       | 0.434763       | 0.434910       | 1        | 0       
36     | 0.528801       | 0.381378       | 0.386946       | 0.552228       | 0.571674       | 0.439577       | 0.439742       | 1        | 0       
37     | 0.528210       | 0.382193       | 0.396971       | 0.508224       | 0.620881       | 0.444522       | 0.444999       | 1        | 0       
38     | 0.561852       | 0.387228       | 0.405006       | 0.582217       | 0.621335       | 0.463059       | 0.462243       | 1        | 0       
39     | 0.472619       | 0.362031       | 0.364378       | 0.498740       | 0.501064       | 0.402708       | 0.402403       | 1        | 0       
40     | 0.511523       | 0.386610       | 0.384608       | 0.593021       | 0.587783       | 0.447321       | 0.447386       | 2        | 0       
41     | 0.533994       | 0.370757       | 0.380757       | 0.529504       | 0.578330       | 0.434339       | 0.434620       | 1        | 0       
42     | 0.531560       | 0.388509       | 0.396287       | 0.610269       | 0.579939       | 0.456120       | 0.455661       | 1        | 0       
43     | 0.544970       | 0.382740       | 0.395805       | 0.615575       | 0.634868       | 0.465426       | 0.465211       | 1        | 0       
44     | 0.554837       | 0.395460       | 0.398404       | 0.572331       | 0.647577       | 0.466968       | 0.466161       | 1        | 0       
45     | 0.493726       | 0.374339       | 0.377356       | 0.513430       | 0.559319       | 0.423223       | 0.422801       | 1        | 0       
46     | 0.518641       | 0.395067       | 0.396032       | 0.645877       | 0.604796       | 0.463568       | 0.463305       | 1        | 0       
47     | 0.553657       | 0.387473       | 0.385736       | 0.543742       | 0.533690       | 0.437589       | 0.437171       | 2        | 0       
48     | 0.540115       | 0.400874       | 0.406049       | 0.536603       | 0.648928       | 0.460992       | 0.461559       | 1        | 0       
49     | 0.506244       | 0.391703       | 0.391537       | 0.665400       | 0.563849       | 0.455243       | 0.456160       | 2        | 0       
50     | 0.551942       | 0.398700       | 0.401722       | 0.532650       | 0.591701       | 0.452235       | 0.452605       | 1        | 0       
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
4b. SHADOW MULTI-KRUM REJECTED (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A)
--------------------------------------------------------------------------------
1      | 0              | 0              | 0              | 1              | 1              | 0              | 0             
2      | 0              | 0              | 0              | 1              | 1              | 0              | 0             
3      | 0              | 0              | 0              | 1              | 1              | 0              | 0             
4      | 0              | 0              | 0              | 1              | 1              | 0              | 0             
5      | 0              | 0              | 0              | 1              | 1              | 0              | 0             
6      | 1              | 0              | 0              | 1              | 0              | 0              | 0             
7      | 0              | 0              | 0              | 1              | 1              | 0              | 0             
8      | 0              | 0              | 0              | 1              | 1              | 0              | 0             
9      | 0              | 0              | 0              | 1              | 1              | 0              | 0             
10     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
11     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
12     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
13     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
14     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
15     | 1              | 0              | 0              | 1              | 0              | 0              | 0             
16     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
17     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
18     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
19     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
20     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
21     | 1              | 0              | 0              | 0              | 1              | 0              | 0             
22     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
23     | 1              | 0              | 0              | 1              | 0              | 0              | 0             
24     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
25     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
26     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
27     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
28     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
29     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
30     | 1              | 0              | 0              | 0              | 1              | 0              | 0             
31     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
32     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
33     | 1              | 0              | 0              | 0              | 1              | 0              | 0             
34     | 1              | 0              | 0              | 0              | 1              | 0              | 0             
35     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
36     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
37     | 1              | 0              | 0              | 0              | 1              | 0              | 0             
38     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
39     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
40     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
41     | 1              | 0              | 0              | 0              | 1              | 0              | 0             
42     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
43     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
44     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
45     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
46     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
47     | 1              | 0              | 0              | 1              | 0              | 0              | 0             
48     | 1              | 0              | 0              | 0              | 1              | 0              | 0             
49     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
50     | 1              | 0              | 0              | 0              | 1              | 0              | 0             
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
4c. SHADOW TRIMMED-MEAN TRIM FRACTION (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A)
--------------------------------------------------------------------------------
1      | 0.647909       | 0.525736       | 0.568077       | 0.728960       | 0.609444       | 0.459918       | 0.459955      
2      | 0.645861       | 0.524887       | 0.625861       | 0.677426       | 0.593216       | 0.466522       | 0.466226      
3      | 0.648185       | 0.517146       | 0.572903       | 0.654298       | 0.643041       | 0.482042       | 0.482385      
4      | 0.635933       | 0.506576       | 0.542449       | 0.666282       | 0.665694       | 0.491579       | 0.491487      
5      | 0.654192       | 0.494529       | 0.534559       | 0.669376       | 0.656467       | 0.494940       | 0.495938      
6      | 0.663954       | 0.506698       | 0.534440       | 0.657983       | 0.647607       | 0.494705       | 0.494613      
7      | 0.647437       | 0.490138       | 0.538208       | 0.681568       | 0.649340       | 0.497252       | 0.496057      
8      | 0.626231       | 0.487308       | 0.540464       | 0.681442       | 0.668748       | 0.498521       | 0.497286      
9      | 0.638994       | 0.487972       | 0.537034       | 0.675946       | 0.665600       | 0.497321       | 0.497133      
10     | 0.640054       | 0.492564       | 0.536142       | 0.680536       | 0.656723       | 0.497518       | 0.496463      
11     | 0.642160       | 0.502936       | 0.547638       | 0.675121       | 0.640487       | 0.495565       | 0.496094      
12     | 0.630693       | 0.488332       | 0.549626       | 0.688871       | 0.649305       | 0.496368       | 0.496805      
13     | 0.636168       | 0.492116       | 0.549136       | 0.673783       | 0.655995       | 0.495654       | 0.497149      
14     | 0.650679       | 0.503889       | 0.542287       | 0.666682       | 0.645505       | 0.495359       | 0.495600      
15     | 0.650364       | 0.506125       | 0.542995       | 0.678437       | 0.631635       | 0.495987       | 0.494458      
16     | 0.641052       | 0.507990       | 0.542200       | 0.669923       | 0.649687       | 0.495111       | 0.494036      
17     | 0.639308       | 0.512642       | 0.541784       | 0.669200       | 0.647794       | 0.494801       | 0.494470      
18     | 0.639922       | 0.518495       | 0.547707       | 0.661134       | 0.644484       | 0.494045       | 0.494213      
19     | 0.628803       | 0.508315       | 0.557193       | 0.667732       | 0.649527       | 0.494225       | 0.494206      
20     | 0.645488       | 0.499989       | 0.549470       | 0.663211       | 0.650102       | 0.495395       | 0.496345      
21     | 0.647134       | 0.511545       | 0.552681       | 0.650312       | 0.650568       | 0.493356       | 0.494403      
22     | 0.634722       | 0.515103       | 0.550065       | 0.665814       | 0.646648       | 0.493942       | 0.493705      
23     | 0.642238       | 0.503769       | 0.564387       | 0.667574       | 0.634189       | 0.493308       | 0.494535      
24     | 0.634628       | 0.525723       | 0.556325       | 0.654136       | 0.647844       | 0.490582       | 0.490761      
25     | 0.631985       | 0.535713       | 0.563759       | 0.647364       | 0.640398       | 0.489891       | 0.490890      
26     | 0.631870       | 0.526728       | 0.563224       | 0.668519       | 0.628585       | 0.490584       | 0.490492      
27     | 0.623690       | 0.514513       | 0.562671       | 0.684563       | 0.633593       | 0.490512       | 0.490457      
28     | 0.635530       | 0.521943       | 0.561619       | 0.667818       | 0.632395       | 0.490763       | 0.489932      
29     | 0.632505       | 0.522562       | 0.573139       | 0.661830       | 0.631560       | 0.489818       | 0.488586      
30     | 0.632401       | 0.515246       | 0.553190       | 0.652096       | 0.668219       | 0.489181       | 0.489667      
31     | 0.625613       | 0.521141       | 0.584003       | 0.667754       | 0.630102       | 0.485892       | 0.485496      
32     | 0.632505       | 0.517953       | 0.555966       | 0.652297       | 0.663442       | 0.489113       | 0.488725      
33     | 0.636911       | 0.517642       | 0.557916       | 0.641579       | 0.668626       | 0.488400       | 0.488926      
34     | 0.636882       | 0.525193       | 0.561804       | 0.649193       | 0.653411       | 0.486790       | 0.486726      
35     | 0.622476       | 0.523630       | 0.563261       | 0.680866       | 0.632756       | 0.488057       | 0.488952      
36     | 0.630123       | 0.526750       | 0.557914       | 0.663549       | 0.647931       | 0.487310       | 0.486423      
37     | 0.630221       | 0.519658       | 0.565014       | 0.634853       | 0.673874       | 0.487903       | 0.488478      
38     | 0.639303       | 0.501743       | 0.553215       | 0.663668       | 0.660114       | 0.490922       | 0.491035      
39     | 0.629416       | 0.547935       | 0.562177       | 0.658524       | 0.632038       | 0.484486       | 0.485424      
40     | 0.628306       | 0.535012       | 0.537296       | 0.661862       | 0.663602       | 0.487148       | 0.486775      
41     | 0.644807       | 0.517569       | 0.558569       | 0.653836       | 0.650251       | 0.488003       | 0.486965      
42     | 0.622974       | 0.530590       | 0.558585       | 0.675574       | 0.638415       | 0.487039       | 0.486824      
43     | 0.629213       | 0.499670       | 0.545486       | 0.669643       | 0.672581       | 0.491608       | 0.491799      
44     | 0.629531       | 0.522045       | 0.541877       | 0.666485       | 0.673162       | 0.483586       | 0.483314      
45     | 0.622695       | 0.540983       | 0.559546       | 0.660024       | 0.647753       | 0.484003       | 0.484997      
46     | 0.613275       | 0.534666       | 0.545498       | 0.679814       | 0.649342       | 0.488790       | 0.488616      
47     | 0.646715       | 0.543039       | 0.550650       | 0.656895       | 0.632953       | 0.485057       | 0.484691      
48     | 0.631186       | 0.535430       | 0.552079       | 0.641221       | 0.673870       | 0.482996       | 0.483218      
49     | 0.615944       | 0.538609       | 0.543419       | 0.685341       | 0.642690       | 0.487269       | 0.486727      
50     | 0.641935       | 0.552815       | 0.553869       | 0.648881       | 0.643597       | 0.479352       | 0.479553      
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
4d. SHADOW MEDIAN PROVIDER FRACTION (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A)
--------------------------------------------------------------------------------
1      | 0.108703       | 0.151791       | 0.144158       | 0.079668       | 0.140619       | 0.187862       | 0.187199      
2      | 0.112411       | 0.153211       | 0.120405       | 0.103123       | 0.141511       | 0.184527       | 0.184812      
3      | 0.113580       | 0.161733       | 0.140846       | 0.113493       | 0.118243       | 0.176102       | 0.176002      
4      | 0.118145       | 0.168748       | 0.152857       | 0.108380       | 0.108406       | 0.172201       | 0.171263      
5      | 0.111098       | 0.173847       | 0.156774       | 0.105856       | 0.112325       | 0.170428       | 0.169672      
6      | 0.108523       | 0.168466       | 0.156405       | 0.110145       | 0.115856       | 0.170632       | 0.169974      
7      | 0.113621       | 0.176044       | 0.156168       | 0.101580       | 0.114331       | 0.169214       | 0.169042      
8      | 0.122055       | 0.177409       | 0.154121       | 0.101425       | 0.107470       | 0.168113       | 0.169407      
9      | 0.117327       | 0.176148       | 0.155664       | 0.103823       | 0.108406       | 0.169307       | 0.169325      
10     | 0.117142       | 0.174921       | 0.155963       | 0.102497       | 0.111347       | 0.168679       | 0.169449      
11     | 0.116425       | 0.170700       | 0.151328       | 0.104439       | 0.117762       | 0.170201       | 0.169145      
12     | 0.120728       | 0.177632       | 0.150806       | 0.099253       | 0.113947       | 0.168589       | 0.169045      
13     | 0.119111       | 0.174715       | 0.150938       | 0.104510       | 0.111983       | 0.169743       | 0.168999      
14     | 0.114237       | 0.169048       | 0.153791       | 0.107189       | 0.116382       | 0.169581       | 0.169773      
15     | 0.114064       | 0.168549       | 0.153077       | 0.103411       | 0.121167       | 0.169433       | 0.170298      
16     | 0.116832       | 0.167535       | 0.154246       | 0.106245       | 0.114379       | 0.170680       | 0.170083      
17     | 0.117709       | 0.166467       | 0.154040       | 0.106829       | 0.114774       | 0.170112       | 0.170068      
18     | 0.117694       | 0.163316       | 0.152174       | 0.109720       | 0.116274       | 0.170394       | 0.170428      
19     | 0.121660       | 0.167652       | 0.148222       | 0.106588       | 0.114185       | 0.170882       | 0.170811      
20     | 0.114668       | 0.171094       | 0.151548       | 0.108474       | 0.114594       | 0.169862       | 0.169760      
21     | 0.115086       | 0.165519       | 0.149874       | 0.113487       | 0.113796       | 0.171170       | 0.171068      
22     | 0.119550       | 0.164864       | 0.150931       | 0.107688       | 0.115568       | 0.170256       | 0.171143      
23     | 0.116097       | 0.169371       | 0.144819       | 0.107933       | 0.120272       | 0.170682       | 0.170826      
24     | 0.119166       | 0.160067       | 0.148840       | 0.112091       | 0.115346       | 0.172317       | 0.172174      
25     | 0.120414       | 0.156992       | 0.144478       | 0.115239       | 0.118119       | 0.173229       | 0.171528      
26     | 0.121175       | 0.159574       | 0.146240       | 0.106465       | 0.122046       | 0.172260       | 0.172240      
27     | 0.123016       | 0.165627       | 0.145362       | 0.100881       | 0.120132       | 0.172855       | 0.172127      
28     | 0.118794       | 0.162826       | 0.145612       | 0.106874       | 0.120812       | 0.172063       | 0.173019      
29     | 0.120317       | 0.161605       | 0.141691       | 0.108860       | 0.121663       | 0.172519       | 0.173345      
30     | 0.119759       | 0.165146       | 0.148661       | 0.112164       | 0.107930       | 0.172883       | 0.173458      
31     | 0.122211       | 0.162072       | 0.137168       | 0.106568       | 0.122516       | 0.174691       | 0.174775      
32     | 0.119077       | 0.164964       | 0.147528       | 0.112389       | 0.109875       | 0.172894       | 0.173273      
33     | 0.118004       | 0.164451       | 0.146794       | 0.116481       | 0.108055       | 0.173152       | 0.173063      
34     | 0.119078       | 0.160303       | 0.146090       | 0.112680       | 0.113545       | 0.174221       | 0.174083      
35     | 0.123417       | 0.161665       | 0.144896       | 0.102200       | 0.120811       | 0.173772       | 0.173238      
36     | 0.120669       | 0.159785       | 0.147519       | 0.108250       | 0.115276       | 0.173845       | 0.174657      
37     | 0.120767       | 0.162793       | 0.144727       | 0.118271       | 0.106614       | 0.173145       | 0.173684      
38     | 0.117684       | 0.169739       | 0.149008       | 0.107849       | 0.110529       | 0.172246       | 0.172944      
39     | 0.120294       | 0.151138       | 0.146192       | 0.109688       | 0.121590       | 0.175837       | 0.175261      
40     | 0.121437       | 0.156802       | 0.155200       | 0.109451       | 0.109286       | 0.173348       | 0.174477      
41     | 0.115154       | 0.163230       | 0.147402       | 0.111699       | 0.114795       | 0.173680       | 0.174040      
42     | 0.123440       | 0.157759       | 0.146765       | 0.104369       | 0.119476       | 0.173984       | 0.174207      
43     | 0.120671       | 0.171583       | 0.151884       | 0.106483       | 0.105920       | 0.171638       | 0.171822      
44     | 0.120233       | 0.162006       | 0.153997       | 0.105211       | 0.106093       | 0.176128       | 0.176332      
45     | 0.123210       | 0.153054       | 0.146356       | 0.109495       | 0.116368       | 0.175811       | 0.175706      
46     | 0.126786       | 0.156385       | 0.151564       | 0.102966       | 0.115506       | 0.173095       | 0.173697      
47     | 0.115410       | 0.152924       | 0.149835       | 0.110451       | 0.120827       | 0.175547       | 0.175007      
48     | 0.120295       | 0.155880       | 0.149311       | 0.115529       | 0.106609       | 0.176533       | 0.175842      
49     | 0.125563       | 0.153323       | 0.152790       | 0.101610       | 0.117246       | 0.174652       | 0.174817      
50     | 0.116547       | 0.147344       | 0.148481       | 0.111923       | 0.119106       | 0.178630       | 0.177969      
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
4e. SHADOW DISTANCE TO COORDINATE MEDIAN (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A)
--------------------------------------------------------------------------------
1      | 0.868109       | 0.657874       | 0.694092       | 0.951056       | 0.788349       | 0.649520       | 0.650600      
2      | 0.607232       | 0.519266       | 0.614598       | 0.665772       | 0.574524       | 0.488215       | 0.487784      
3      | 0.512642       | 0.395750       | 0.444619       | 0.542769       | 0.522244       | 0.402297       | 0.403343      
4      | 0.436687       | 0.322626       | 0.344566       | 0.487695       | 0.482213       | 0.351372       | 0.351780      
5      | 0.436075       | 0.300402       | 0.315447       | 0.471294       | 0.457535       | 0.337771       | 0.338446      
6      | 0.433331       | 0.291460       | 0.300712       | 0.437400       | 0.428649       | 0.322700       | 0.322310      
7      | 0.407454       | 0.277751       | 0.294630       | 0.448370       | 0.414855       | 0.315113       | 0.314543      
8      | 0.387427       | 0.275183       | 0.292030       | 0.441557       | 0.441774       | 0.315078       | 0.314970      
9      | 0.404391       | 0.277521       | 0.295592       | 0.444194       | 0.437851       | 0.318048       | 0.318308      
10     | 0.393391       | 0.271302       | 0.287117       | 0.441374       | 0.422456       | 0.310803       | 0.311297      
11     | 0.402304       | 0.278829       | 0.300603       | 0.432365       | 0.405638       | 0.309790       | 0.309928      
12     | 0.373368       | 0.264427       | 0.286003       | 0.430296       | 0.402296       | 0.299770       | 0.300074      
13     | 0.377817       | 0.264283       | 0.285935       | 0.414705       | 0.403869       | 0.297811       | 0.297607      
14     | 0.386631       | 0.263945       | 0.281174       | 0.403282       | 0.393902       | 0.294795       | 0.295063      
15     | 0.383252       | 0.262771       | 0.276886       | 0.410949       | 0.369583       | 0.291297       | 0.289765      
16     | 0.373419       | 0.267722       | 0.276689       | 0.405246       | 0.394942       | 0.292711       | 0.292226      
17     | 0.366254       | 0.262346       | 0.270111       | 0.393450       | 0.376951       | 0.283950       | 0.283681      
18     | 0.376595       | 0.267296       | 0.280221       | 0.393267       | 0.383322       | 0.288508       | 0.288940      
19     | 0.356651       | 0.259055       | 0.276868       | 0.388295       | 0.381284       | 0.282009       | 0.281945      
20     | 0.365900       | 0.251803       | 0.268732       | 0.376377       | 0.376157       | 0.279282       | 0.278957      
21     | 0.365192       | 0.253966       | 0.267089       | 0.364105       | 0.369652       | 0.274747       | 0.274854      
22     | 0.343748       | 0.251362       | 0.260683       | 0.371740       | 0.362619       | 0.270338       | 0.270187      
23     | 0.352421       | 0.248408       | 0.264967       | 0.366796       | 0.346810       | 0.267537       | 0.267880      
24     | 0.337463       | 0.251811       | 0.259061       | 0.351315       | 0.352710       | 0.262736       | 0.262360      
25     | 0.331059       | 0.252977       | 0.262987       | 0.343708       | 0.343030       | 0.258506       | 0.258770      
26     | 0.334894       | 0.251072       | 0.261009       | 0.359027       | 0.338521       | 0.260776       | 0.261007      
27     | 0.324700       | 0.246586       | 0.260146       | 0.370759       | 0.336639       | 0.260324       | 0.260460      
28     | 0.325278       | 0.244325       | 0.256544       | 0.344917       | 0.331474       | 0.253482       | 0.253178      
29     | 0.322522       | 0.245108       | 0.259210       | 0.343907       | 0.330534       | 0.252680       | 0.252560      
30     | 0.327589       | 0.243055       | 0.254020       | 0.329945       | 0.362161       | 0.256085       | 0.256524      
31     | 0.319604       | 0.246188       | 0.265653       | 0.337063       | 0.327970       | 0.251219       | 0.250936      
32     | 0.317864       | 0.240488       | 0.252081       | 0.331706       | 0.356429       | 0.253256       | 0.253351      
33     | 0.326159       | 0.244233       | 0.251868       | 0.324742       | 0.365906       | 0.255872       | 0.255779      
34     | 0.317261       | 0.239016       | 0.247968       | 0.305048       | 0.333200       | 0.242271       | 0.242194      
35     | 0.312387       | 0.244067       | 0.256885       | 0.352152       | 0.332757       | 0.252071       | 0.252493      
36     | 0.323511       | 0.247936       | 0.253039       | 0.337600       | 0.345958       | 0.254149       | 0.254105      
37     | 0.321578       | 0.244864       | 0.259826       | 0.318394       | 0.368338       | 0.255382       | 0.255772      
38     | 0.336734       | 0.240988       | 0.258231       | 0.352593       | 0.367370       | 0.263819       | 0.263279      
39     | 0.301600       | 0.246132       | 0.248101       | 0.319627       | 0.320113       | 0.240539       | 0.240927      
40     | 0.316199       | 0.251115       | 0.248711       | 0.356612       | 0.352000       | 0.257523       | 0.257108      
41     | 0.325866       | 0.242947       | 0.252093       | 0.331140       | 0.351866       | 0.253417       | 0.253474      
42     | 0.320294       | 0.249896       | 0.256856       | 0.363977       | 0.345616       | 0.259464       | 0.259339      
43     | 0.328012       | 0.240134       | 0.252888       | 0.367717       | 0.372368       | 0.265381       | 0.265035      
44     | 0.330070       | 0.253582       | 0.256111       | 0.342941       | 0.377806       | 0.262979       | 0.262680      
45     | 0.309993       | 0.247535       | 0.250409       | 0.324274       | 0.345163       | 0.248199       | 0.247821      
46     | 0.311640       | 0.252670       | 0.253108       | 0.377425       | 0.356631       | 0.263075       | 0.262901      
47     | 0.339217       | 0.252250       | 0.249560       | 0.334491       | 0.329339       | 0.252877       | 0.252966      
48     | 0.324191       | 0.255621       | 0.261933       | 0.324910       | 0.376997       | 0.259693       | 0.259486      
49     | 0.309310       | 0.251135       | 0.249918       | 0.388233       | 0.340633       | 0.260555       | 0.260862      
50     | 0.331380       | 0.257129       | 0.262574       | 0.323265       | 0.354907       | 0.255665       | 0.255839      
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
4f. UPDATE NORM (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A)
--------------------------------------------------------------------------------
1      | 1.361764       | 0.606631       | 0.560976       | 1.518111       | 1.264700       | 1.135799       | 1.135370      
2      | 1.088580       | 0.455790       | 0.441318       | 1.121905       | 1.013365       | 0.879329       | 0.878372      
3      | 0.797540       | 0.343250       | 0.389034       | 0.790113       | 0.789663       | 0.655929       | 0.657132      
4      | 0.601862       | 0.313159       | 0.336097       | 0.617252       | 0.644867       | 0.523618       | 0.523692      
5      | 0.551306       | 0.282658       | 0.308478       | 0.552574       | 0.566096       | 0.469648       | 0.470268      
6      | 0.514528       | 0.263987       | 0.296837       | 0.496322       | 0.512900       | 0.432340       | 0.431343      
7      | 0.463290       | 0.266272       | 0.278263       | 0.498823       | 0.480349       | 0.410645       | 0.410375      
8      | 0.428726       | 0.260932       | 0.269792       | 0.489746       | 0.499677       | 0.403758       | 0.403853      
9      | 0.451495       | 0.267995       | 0.277869       | 0.489133       | 0.499242       | 0.409892       | 0.410360      
10     | 0.433618       | 0.261002       | 0.262680       | 0.488075       | 0.475667       | 0.397361       | 0.397550      
11     | 0.444449       | 0.270448       | 0.271284       | 0.469403       | 0.457256       | 0.393042       | 0.393176      
12     | 0.401846       | 0.255967       | 0.262574       | 0.465750       | 0.452175       | 0.378515       | 0.378672      
13     | 0.415044       | 0.252355       | 0.262798       | 0.446875       | 0.452574       | 0.376348       | 0.376603      
14     | 0.419454       | 0.258927       | 0.264893       | 0.431572       | 0.435766       | 0.371317       | 0.371422      
15     | 0.415358       | 0.256037       | 0.254928       | 0.444135       | 0.408382       | 0.366062       | 0.364909      
16     | 0.407673       | 0.259473       | 0.257000       | 0.434200       | 0.434242       | 0.367943       | 0.367755      
17     | 0.397826       | 0.260417       | 0.257371       | 0.415190       | 0.412825       | 0.356328       | 0.356744      
18     | 0.413490       | 0.264283       | 0.256520       | 0.417636       | 0.414531       | 0.361064       | 0.361530      
19     | 0.385224       | 0.254463       | 0.263181       | 0.406360       | 0.411308       | 0.350914       | 0.350517      
20     | 0.397636       | 0.246951       | 0.256751       | 0.386410       | 0.403084       | 0.345705       | 0.345303      
21     | 0.391218       | 0.251843       | 0.256304       | 0.381620       | 0.398544       | 0.342199       | 0.342213      
22     | 0.367298       | 0.246195       | 0.253880       | 0.383407       | 0.392762       | 0.335160       | 0.335268      
23     | 0.374875       | 0.242451       | 0.258807       | 0.379146       | 0.373286       | 0.331307       | 0.331404      
24     | 0.355073       | 0.254940       | 0.254706       | 0.359799       | 0.377909       | 0.325110       | 0.324836      
25     | 0.356616       | 0.256621       | 0.255799       | 0.356032       | 0.364991       | 0.321954       | 0.322209      
26     | 0.356116       | 0.253615       | 0.254498       | 0.372433       | 0.361658       | 0.323969       | 0.324369      
27     | 0.346779       | 0.240095       | 0.256115       | 0.386601       | 0.364005       | 0.324154       | 0.324190      
28     | 0.347518       | 0.250601       | 0.252282       | 0.349818       | 0.356030       | 0.315004       | 0.314917      
29     | 0.341681       | 0.242147       | 0.258822       | 0.353397       | 0.353675       | 0.313610       | 0.313746      
30     | 0.340081       | 0.246074       | 0.247107       | 0.342694       | 0.389502       | 0.317929       | 0.318264      
31     | 0.341054       | 0.246323       | 0.263031       | 0.344196       | 0.343597       | 0.311115       | 0.310370      
32     | 0.336796       | 0.239325       | 0.248605       | 0.340608       | 0.381532       | 0.314512       | 0.314746      
33     | 0.347589       | 0.243418       | 0.251460       | 0.325913       | 0.393288       | 0.317444       | 0.317766      
34     | 0.335929       | 0.243322       | 0.240293       | 0.313393       | 0.355595       | 0.301408       | 0.301381      
35     | 0.330656       | 0.243166       | 0.252989       | 0.365003       | 0.357692       | 0.313894       | 0.314519      
36     | 0.337329       | 0.249447       | 0.256414       | 0.352283       | 0.370531       | 0.317357       | 0.317305      
37     | 0.338865       | 0.245165       | 0.256932       | 0.323573       | 0.401340       | 0.318245       | 0.319012      
38     | 0.358610       | 0.242347       | 0.249135       | 0.361940       | 0.393769       | 0.327127       | 0.326736      
39     | 0.317928       | 0.250043       | 0.247734       | 0.327490       | 0.344298       | 0.300436       | 0.300354      
40     | 0.334819       | 0.251709       | 0.242576       | 0.374389       | 0.379703       | 0.321836       | 0.321914      
41     | 0.352411       | 0.240231       | 0.249679       | 0.338836       | 0.376214       | 0.315909       | 0.316040      
42     | 0.337049       | 0.248915       | 0.252344       | 0.381346       | 0.370260       | 0.323230       | 0.323139      
43     | 0.349218       | 0.243179       | 0.252012       | 0.381010       | 0.395796       | 0.330504       | 0.330457      
44     | 0.350346       | 0.247674       | 0.249866       | 0.351502       | 0.411733       | 0.328377       | 0.328113      
45     | 0.329567       | 0.250231       | 0.248161       | 0.331888       | 0.372467       | 0.310736       | 0.310151      
46     | 0.324588       | 0.250864       | 0.247677       | 0.395528       | 0.382636       | 0.326395       | 0.326551      
47     | 0.359422       | 0.253903       | 0.252225       | 0.346178       | 0.351920       | 0.316747       | 0.316544      
48     | 0.342206       | 0.249377       | 0.250785       | 0.337198       | 0.410719       | 0.323856       | 0.323921      
49     | 0.324341       | 0.255278       | 0.254248       | 0.410480       | 0.361230       | 0.326334       | 0.326729      
50     | 0.350329       | 0.252987       | 0.252689       | 0.334631       | 0.385248       | 0.319693       | 0.319722      
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
4g. PAIRWISE SQUARED DISTANCE (Per Round, Upper Triangle)
--------------------------------------------------------------------------------
Round | d(0,1) | d(0,2) | d(0,3) | d(0,4) | d(0,5) | d(0,6) | d(1,2) | d(1,3) | d(1,4) | d(1,5) | d(1,6) | d(2,3) | d(2,4) | d(2,5) | d(2,6) | d(3,4) | d(3,5) | d(3,6) | d(4,5) | d(4,6) | d(5,6)
--------------------------------------------------------------------------------
1      | 1.554941       | 1.543046       | 0.901672       | 1.749678       | 1.147506       | 1.150807       | 0.127025       | 1.842158       | 1.025643       | 0.911646       | 0.911747       | 1.956156       | 1.144003       | 0.955352       | 0.956491       | 1.731028       | 1.283658       | 1.287261       | 1.132116       | 1.131283       | 1.086590      
2      | 0.836455       | 0.990923       | 0.601168       | 0.709069       | 0.628448       | 0.630088       | 0.143047       | 0.901063       | 0.706506       | 0.516492       | 0.514836       | 1.158607       | 0.801673       | 0.617833       | 0.616312       | 0.804884       | 0.693478       | 0.693989       | 0.605065       | 0.603711       | 0.611894      
3      | 0.527641       | 0.570962       | 0.528121       | 0.560041       | 0.436281       | 0.436312       | 0.133487       | 0.523155       | 0.511820       | 0.338576       | 0.340160       | 0.646945       | 0.545620       | 0.379007       | 0.380024       | 0.609069       | 0.460963       | 0.461326       | 0.445032       | 0.445874       | 0.412108      
4      | 0.347092       | 0.357160       | 0.438275       | 0.473999       | 0.322663       | 0.322761       | 0.128692       | 0.376522       | 0.393906       | 0.249547       | 0.249268       | 0.448330       | 0.384011       | 0.263855       | 0.263858       | 0.539632       | 0.360662       | 0.361373       | 0.357998       | 0.358309       | 0.311045      
5      | 0.323766       | 0.330304       | 0.440866       | 0.453951       | 0.309524       | 0.309539       | 0.126517       | 0.338819       | 0.340607       | 0.225508       | 0.226149       | 0.389260       | 0.331485       | 0.235323       | 0.235561       | 0.505005       | 0.334862       | 0.334769       | 0.325187       | 0.326129       | 0.286238      
6      | 0.320752       | 0.314080       | 0.407788       | 0.425242       | 0.293962       | 0.294169       | 0.123340       | 0.293951       | 0.303000       | 0.208202       | 0.207557       | 0.339832       | 0.293187       | 0.214467       | 0.213523       | 0.433750       | 0.295588       | 0.294748       | 0.291101       | 0.290994       | 0.260770      
7      | 0.273272       | 0.282800       | 0.390964       | 0.400792       | 0.269705       | 0.269498       | 0.117469       | 0.305143       | 0.278198       | 0.194951       | 0.194603       | 0.354210       | 0.268974       | 0.205073       | 0.204910       | 0.430456       | 0.295945       | 0.295360       | 0.275562       | 0.275382       | 0.248317      
8      | 0.243990       | 0.254175       | 0.374760       | 0.413241       | 0.257374       | 0.257190       | 0.119944       | 0.296796       | 0.305975       | 0.193257       | 0.193354       | 0.342168       | 0.301666       | 0.203799       | 0.203543       | 0.443822       | 0.292515       | 0.291383       | 0.292609       | 0.292954       | 0.248021      
9      | 0.266214       | 0.270815       | 0.396378       | 0.421502       | 0.271284       | 0.270685       | 0.124045       | 0.291986       | 0.304430       | 0.197200       | 0.197225       | 0.348792       | 0.296212       | 0.207687       | 0.207876       | 0.445875       | 0.296203       | 0.296832       | 0.293759       | 0.293414       | 0.252803      
10     | 0.251673       | 0.252435       | 0.388508       | 0.395294       | 0.257150       | 0.257792       | 0.121481       | 0.287484       | 0.282137       | 0.188587       | 0.188774       | 0.338324       | 0.276831       | 0.197921       | 0.198117       | 0.426960       | 0.288439       | 0.288747       | 0.275881       | 0.276310       | 0.242012      
11     | 0.269075       | 0.268375       | 0.388022       | 0.386951       | 0.262344       | 0.262081       | 0.139255       | 0.277777       | 0.267453       | 0.190420       | 0.190763       | 0.341966       | 0.269150       | 0.203963       | 0.203533       | 0.400025       | 0.280956       | 0.281827       | 0.264528       | 0.264315       | 0.240399      
12     | 0.227826       | 0.233867       | 0.359400       | 0.360093       | 0.236188       | 0.235858       | 0.127599       | 0.269573       | 0.257605       | 0.176128       | 0.176699       | 0.329150       | 0.253157       | 0.188502       | 0.188760       | 0.400197       | 0.271417       | 0.271537       | 0.254015       | 0.254350       | 0.225045      
13     | 0.231118       | 0.242887       | 0.352702       | 0.362996       | 0.236837       | 0.237406       | 0.121818       | 0.256737       | 0.263870       | 0.174473       | 0.174321       | 0.308366       | 0.259350       | 0.186373       | 0.186476       | 0.380727       | 0.259820       | 0.259276       | 0.253379       | 0.252747       | 0.221928      
14     | 0.240222       | 0.249460       | 0.351693       | 0.359453       | 0.240203       | 0.240608       | 0.123765       | 0.244400       | 0.253349       | 0.172327       | 0.172533       | 0.289639       | 0.245651       | 0.181439       | 0.181708       | 0.362693       | 0.249629       | 0.250002       | 0.243830       | 0.244868       | 0.218027      
15     | 0.238179       | 0.247125       | 0.348989       | 0.334219       | 0.234301       | 0.232889       | 0.119333       | 0.257823       | 0.227405       | 0.169365       | 0.168328       | 0.296885       | 0.218998       | 0.176953       | 0.176235       | 0.350205       | 0.251274       | 0.250667       | 0.226419       | 0.225825       | 0.211187      
16     | 0.232601       | 0.238485       | 0.334820       | 0.344300       | 0.230398       | 0.230490       | 0.120563       | 0.251107       | 0.258585       | 0.172939       | 0.172410       | 0.288898       | 0.241601       | 0.177655       | 0.177314       | 0.370681       | 0.249315       | 0.249042       | 0.242778       | 0.242843       | 0.214528      
17     | 0.223621       | 0.225536       | 0.323315       | 0.321126       | 0.218716       | 0.218837       | 0.121295       | 0.235347       | 0.237610       | 0.163655       | 0.163480       | 0.271064       | 0.224516       | 0.168534       | 0.168467       | 0.340275       | 0.234119       | 0.234106       | 0.225335       | 0.225446       | 0.201837      
18     | 0.233132       | 0.249424       | 0.324250       | 0.336238       | 0.228484       | 0.228455       | 0.124031       | 0.244740       | 0.246738       | 0.169675       | 0.169937       | 0.276044       | 0.233957       | 0.176227       | 0.176820       | 0.347124       | 0.238611       | 0.238605       | 0.232832       | 0.233261       | 0.209559      
19     | 0.210030       | 0.225653       | 0.306623       | 0.318110       | 0.211542       | 0.211896       | 0.122679       | 0.232595       | 0.240195       | 0.160831       | 0.160616       | 0.271775       | 0.233786       | 0.170655       | 0.169805       | 0.339541       | 0.229660       | 0.230433       | 0.226421       | 0.226321       | 0.199335      
20     | 0.219940       | 0.227556       | 0.303280       | 0.322727       | 0.215038       | 0.214949       | 0.113846       | 0.215362       | 0.226506       | 0.155338       | 0.154877       | 0.254572       | 0.225167       | 0.164536       | 0.163823       | 0.329826       | 0.220524       | 0.220578       | 0.221185       | 0.221395       | 0.195205      
21     | 0.221066       | 0.229721       | 0.289046       | 0.314910       | 0.211032       | 0.210688       | 0.109776       | 0.209578       | 0.228075       | 0.153501       | 0.153536       | 0.243363       | 0.220553       | 0.160325       | 0.160327       | 0.307838       | 0.209975       | 0.209442       | 0.213744       | 0.214345       | 0.189643      
22     | 0.195910       | 0.204090       | 0.287367       | 0.291688       | 0.195927       | 0.196054       | 0.113096       | 0.216585       | 0.219094       | 0.148773       | 0.149019       | 0.241604       | 0.210512       | 0.153836       | 0.154001       | 0.308763       | 0.210857       | 0.210725       | 0.206764       | 0.206229       | 0.182960      
23     | 0.209508       | 0.215613       | 0.287505       | 0.279261       | 0.198040       | 0.198081       | 0.112328       | 0.205331       | 0.201292       | 0.145801       | 0.145825       | 0.244853       | 0.201822       | 0.154571       | 0.154833       | 0.294430       | 0.206376       | 0.206374       | 0.195278       | 0.195631       | 0.180112      
24     | 0.199395       | 0.198359       | 0.260537       | 0.273322       | 0.186428       | 0.186083       | 0.110750       | 0.200607       | 0.209619       | 0.144077       | 0.143972       | 0.223248       | 0.208059       | 0.148115       | 0.148089       | 0.283083       | 0.193358       | 0.193086       | 0.195109       | 0.195304       | 0.173547      
25     | 0.191877       | 0.196571       | 0.249661       | 0.266100       | 0.180283       | 0.180279       | 0.122919       | 0.189222       | 0.205166       | 0.141864       | 0.142132       | 0.222435       | 0.191529       | 0.146627       | 0.146972       | 0.270665       | 0.186418       | 0.186566       | 0.186770       | 0.186915       | 0.168438      
26     | 0.191023       | 0.191161       | 0.275767       | 0.263957       | 0.184660       | 0.184678       | 0.116065       | 0.205245       | 0.199426       | 0.142552       | 0.142376       | 0.235994       | 0.196329       | 0.147546       | 0.147979       | 0.268083       | 0.196767       | 0.197285       | 0.185546       | 0.185443       | 0.171655      
27     | 0.180765       | 0.187168       | 0.268321       | 0.254013       | 0.178015       | 0.178219       | 0.111485       | 0.214052       | 0.193906       | 0.139937       | 0.139860       | 0.248503       | 0.189593       | 0.147667       | 0.147439       | 0.285130       | 0.202812       | 0.203325       | 0.184737       | 0.184565       | 0.170955      
28     | 0.187485       | 0.182476       | 0.250077       | 0.246865       | 0.173659       | 0.173462       | 0.113367       | 0.184441       | 0.187484       | 0.134431       | 0.134332       | 0.220482       | 0.186632       | 0.140643       | 0.140607       | 0.264170       | 0.184190       | 0.183595       | 0.177010       | 0.176619       | 0.161766      
29     | 0.179873       | 0.189321       | 0.243274       | 0.247960       | 0.171806       | 0.171997       | 0.115310       | 0.189520       | 0.187021       | 0.134049       | 0.134215       | 0.219871       | 0.184518       | 0.141684       | 0.141534       | 0.261271       | 0.183023       | 0.182658       | 0.175838       | 0.175733       | 0.161233      
30     | 0.186502       | 0.182113       | 0.237384       | 0.277389       | 0.176901       | 0.176638       | 0.109441       | 0.171067       | 0.213772       | 0.135759       | 0.136298       | 0.203614       | 0.211693       | 0.141201       | 0.141336       | 0.279432       | 0.177770       | 0.178607       | 0.196472       | 0.196136       | 0.165683      
31     | 0.180104       | 0.187647       | 0.231277       | 0.244938       | 0.169108       | 0.169031       | 0.115141       | 0.186183       | 0.187036       | 0.133652       | 0.133506       | 0.227640       | 0.188542       | 0.143970       | 0.143826       | 0.245130       | 0.178265       | 0.177824       | 0.173303       | 0.173410       | 0.159816      
32     | 0.172589       | 0.180113       | 0.228513       | 0.268144       | 0.169958       | 0.170054       | 0.105165       | 0.177612       | 0.208168       | 0.132923       | 0.133042       | 0.203589       | 0.203900       | 0.138660       | 0.138676       | 0.272931       | 0.176749       | 0.176870       | 0.190413       | 0.190380       | 0.161759      
33     | 0.186595       | 0.182569       | 0.226183       | 0.284114       | 0.175733       | 0.175498       | 0.106326       | 0.172112       | 0.215230       | 0.136073       | 0.136099       | 0.197636       | 0.214843       | 0.140458       | 0.140488       | 0.276475       | 0.174473       | 0.174672       | 0.197790       | 0.198223       | 0.165090      
34     | 0.176689       | 0.174852       | 0.210990       | 0.248832       | 0.161709       | 0.162088       | 0.107133       | 0.155628       | 0.187077       | 0.125490       | 0.125423       | 0.181005       | 0.183814       | 0.129510       | 0.128989       | 0.233231       | 0.156135       | 0.156431       | 0.170555       | 0.170562       | 0.148605      
35     | 0.172188       | 0.175667       | 0.245958       | 0.238123       | 0.166500       | 0.166700       | 0.109560       | 0.196194       | 0.190902       | 0.133733       | 0.133878       | 0.227744       | 0.187887       | 0.140129       | 0.140131       | 0.267605       | 0.187409       | 0.187632       | 0.176691       | 0.176987       | 0.160901      
36     | 0.182969       | 0.182435       | 0.240473       | 0.259603       | 0.173194       | 0.173172       | 0.107936       | 0.190424       | 0.200924       | 0.136707       | 0.136735       | 0.206261       | 0.200587       | 0.139436       | 0.139573       | 0.266437       | 0.181278       | 0.180526       | 0.185513       | 0.185574       | 0.163434      
37     | 0.181341       | 0.186178       | 0.218050       | 0.280692       | 0.173008       | 0.173861       | 0.109919       | 0.166163       | 0.221563       | 0.136097       | 0.136177       | 0.197901       | 0.222400       | 0.143327       | 0.143724       | 0.273282       | 0.170812       | 0.171249       | 0.199959       | 0.199359       | 0.165098      
38     | 0.186551       | 0.191066       | 0.267723       | 0.293421       | 0.187631       | 0.187670       | 0.108122       | 0.191218       | 0.212952       | 0.139752       | 0.139354       | 0.222628       | 0.220045       | 0.148651       | 0.148233       | 0.296631       | 0.195753       | 0.195247       | 0.204189       | 0.204194       | 0.174656      
39     | 0.169572       | 0.166128       | 0.209614       | 0.220802       | 0.153255       | 0.153236       | 0.107477       | 0.174949       | 0.184201       | 0.127496       | 0.127059       | 0.192185       | 0.175949       | 0.128384       | 0.128516       | 0.232254       | 0.161809       | 0.161982       | 0.162167       | 0.162949       | 0.146828      
40     | 0.179687       | 0.167585       | 0.254791       | 0.258959       | 0.172346       | 0.171592       | 0.105735       | 0.207093       | 0.210217       | 0.140485       | 0.140390       | 0.218854       | 0.204883       | 0.139356       | 0.139517       | 0.284045       | 0.193017       | 0.192911       | 0.191118       | 0.191781       | 0.167479      
41     | 0.186482       | 0.185111       | 0.235372       | 0.266517       | 0.174681       | 0.174202       | 0.103273       | 0.176299       | 0.204502       | 0.133672       | 0.133811       | 0.204434       | 0.201885       | 0.138671       | 0.138813       | 0.268002       | 0.176574       | 0.176631       | 0.188178       | 0.188267       | 0.161996      
42     | 0.182473       | 0.181591       | 0.259378       | 0.252333       | 0.175157       | 0.174812       | 0.106536       | 0.212496       | 0.203279       | 0.140941       | 0.141032       | 0.234732       | 0.201713       | 0.145150       | 0.144601       | 0.287628       | 0.198692       | 0.199081       | 0.189330       | 0.188896       | 0.170029      
43     | 0.179128       | 0.184494       | 0.264318       | 0.287349       | 0.182986       | 0.182856       | 0.101035       | 0.205836       | 0.219610       | 0.140839       | 0.140866       | 0.235541       | 0.217551       | 0.147506       | 0.147263       | 0.318414       | 0.205081       | 0.204658       | 0.208688       | 0.208629       | 0.177081      
44     | 0.190452       | 0.188779       | 0.245020       | 0.290945       | 0.183066       | 0.182992       | 0.105300       | 0.192535       | 0.237704       | 0.145367       | 0.144793       | 0.213553       | 0.225894       | 0.146668       | 0.146436       | 0.299814       | 0.189767       | 0.190028       | 0.210695       | 0.210988       | 0.174933      
45     | 0.176304       | 0.169870       | 0.220598       | 0.242845       | 0.161882       | 0.161974       | 0.108551       | 0.174802       | 0.204533       | 0.133023       | 0.132765       | 0.195193       | 0.198295       | 0.134485       | 0.134320       | 0.256943       | 0.169516       | 0.169112       | 0.180717       | 0.180307       | 0.155715      
46     | 0.177362       | 0.172476       | 0.263513       | 0.251343       | 0.173160       | 0.173006       | 0.105196       | 0.228041       | 0.213192       | 0.145018       | 0.144853       | 0.239625       | 0.209424       | 0.145390       | 0.145446       | 0.313803       | 0.209038       | 0.208798       | 0.197439       | 0.197933       | 0.174163      
47     | 0.200622       | 0.192610       | 0.252321       | 0.256316       | 0.180590       | 0.180457       | 0.111356       | 0.187865       | 0.189969       | 0.138297       | 0.137820       | 0.199399       | 0.182347       | 0.137161       | 0.137220       | 0.249987       | 0.177777       | 0.178100       | 0.175554       | 0.175789       | 0.162132      
48     | 0.184678       | 0.188945       | 0.230088       | 0.285719       | 0.177783       | 0.177654       | 0.113023       | 0.181104       | 0.240111       | 0.143786       | 0.144065       | 0.197723       | 0.233449       | 0.146369       | 0.146657       | 0.280003       | 0.177762       | 0.177737       | 0.207911       | 0.207568       | 0.170837      
49     | 0.173783       | 0.165836       | 0.269449       | 0.242677       | 0.169973       | 0.170435       | 0.106122       | 0.238684       | 0.196094       | 0.142673       | 0.142907       | 0.252738       | 0.189985       | 0.142597       | 0.142818       | 0.306052       | 0.213392       | 0.213325       | 0.186968       | 0.186896       | 0.171145      
50     | 0.197723       | 0.194108       | 0.225306       | 0.278475       | 0.178646       | 0.179188       | 0.114262       | 0.183401       | 0.215581       | 0.142169       | 0.142270       | 0.203310       | 0.207143       | 0.143596       | 0.143865       | 0.260208       | 0.174784       | 0.174464       | 0.192303       | 0.192256       | 0.166470      
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
4h. PAIRWISE COSINE (Per Round, Upper Triangle)
--------------------------------------------------------------------------------
Round | c(0,1) | c(0,2) | c(0,3) | c(0,4) | c(0,5) | c(0,6) | c(1,2) | c(1,3) | c(1,4) | c(1,5) | c(1,6) | c(2,3) | c(2,4) | c(2,5) | c(2,6) | c(3,4) | c(3,5) | c(3,6) | c(4,5) | c(4,6) | c(5,6)
--------------------------------------------------------------------------------
1      | 0.403994       | 0.409766       | 0.787847       | 0.494773       | 0.645562       | 0.644426       | 0.816432       | 0.450911       | 0.613809       | 0.541649       | 0.541074       | 0.389379       | 0.542777       | 0.509600       | 0.508136       | 0.565934       | 0.670162       | 0.669089       | 0.611726       | 0.611907       | 0.578709      
2      | 0.560609       | 0.404708       | 0.754347       | 0.681189       | 0.694621       | 0.693640       | 0.644954       | 0.552812       | 0.571747       | 0.579461       | 0.580058       | 0.297739       | 0.469576       | 0.451157       | 0.451440       | 0.651214       | 0.678361       | 0.677993       | 0.670584       | 0.671132       | 0.603906      
3      | 0.413242       | 0.348825       | 0.581015       | 0.555438       | 0.602190       | 0.602562       | 0.508044       | 0.403657       | 0.423489       | 0.465233       | 0.464370       | 0.209322       | 0.373203       | 0.396952       | 0.397327       | 0.511917       | 0.572662       | 0.572787       | 0.587682       | 0.587317       | 0.521965      
4      | 0.300343       | 0.291770       | 0.410458       | 0.391758       | 0.497799       | 0.497697       | 0.391155       | 0.265260       | 0.297157       | 0.374143       | 0.375175       | 0.109979       | 0.334059       | 0.350268       | 0.350429       | 0.323112       | 0.455627       | 0.454579       | 0.491671       | 0.491256       | 0.432853      
5      | 0.192738       | 0.202259       | 0.276416       | 0.273087       | 0.415165       | 0.415712       | 0.278341       | 0.148591       | 0.186722       | 0.282328       | 0.281742       | 0.032964       | 0.240914       | 0.277500       | 0.278325       | 0.193090       | 0.368088       | 0.368906       | 0.405944       | 0.404733       | 0.352002      
6      | 0.050344       | 0.126928       | 0.202232       | 0.194326       | 0.354458       | 0.352871       | 0.219893       | 0.084238       | 0.109884       | 0.212064       | 0.211607       | -0.018272      | 0.190455       | 0.235962       | 0.236833       | 0.148594       | 0.320788       | 0.321479       | 0.358264       | 0.357388       | 0.300846      
7      | 0.049717       | 0.035944       | 0.156859       | 0.100165       | 0.298466       | 0.298625       | 0.208271       | 0.054896       | 0.091623       | 0.203856       | 0.204570       | -0.100704      | 0.146606       | 0.179347       | 0.179213       | 0.102467       | 0.296601       | 0.297686       | 0.313823       | 0.313928       | 0.263244      
8      | 0.035316       | 0.010456       | 0.116444       | 0.047244       | 0.258388       | 0.259080       | 0.148657       | 0.043594       | 0.045205       | 0.179637       | 0.179495       | -0.111746      | 0.077142       | 0.146928       | 0.148421       | 0.093388       | 0.279055       | 0.282044       | 0.297629       | 0.296891       | 0.239481      
9      | 0.039073       | 0.040828       | 0.105781       | 0.070073       | 0.271739       | 0.274083       | 0.167775       | 0.072802       | 0.062165       | 0.194058       | 0.195468       | -0.118938      | 0.109003       | 0.164784       | 0.165454       | 0.087265       | 0.276975       | 0.276050       | 0.301753       | 0.303189       | 0.248531      
10     | 0.019762       | 0.020148       | 0.089149       | 0.046034       | 0.257608       | 0.256060       | 0.114073       | 0.074010       | 0.049313       | 0.180458       | 0.180201       | -0.121314      | 0.073747       | 0.138801       | 0.138521       | 0.080801       | 0.277601       | 0.277065       | 0.286430       | 0.285559       | 0.234007      
11     | 0.006663       | 0.011426       | 0.071548       | 0.048388       | 0.256674       | 0.257640       | 0.050992       | 0.061855       | 0.059730       | 0.175005       | 0.173825       | -0.188595      | 0.054528       | 0.113082       | 0.115551       | 0.068484       | 0.254391       | 0.252231       | 0.275541       | 0.276330       | 0.222193      
12     | -0.004022      | -0.016308      | 0.050771       | 0.016097       | 0.225396       | 0.226778       | 0.051067       | 0.053976       | 0.053467       | 0.168572       | 0.166172       | -0.176961      | 0.085284       | 0.119317       | 0.118568       | 0.050307       | 0.251805       | 0.251696       | 0.273797       | 0.273053       | 0.214964      
13     | 0.023041       | -0.007164      | 0.051915       | 0.037502       | 0.246684       | 0.245309       | 0.082391       | 0.029457       | 0.020300       | 0.162409       | 0.164109       | -0.168626      | 0.061112       | 0.122992       | 0.123354       | 0.058825       | 0.242352       | 0.244375       | 0.273255       | 0.275489       | 0.217104      
14     | 0.012719       | -0.015076      | 0.029012       | 0.017453       | 0.236331       | 0.235213       | 0.098024       | 0.039814       | 0.015892       | 0.169503       | 0.168794       | -0.145277      | 0.062415       | 0.135251       | 0.134244       | 0.035768       | 0.232462       | 0.231476       | 0.259385       | 0.256346       | 0.209572      
15     | -0.000476      | -0.045398      | 0.056350       | 0.014972       | 0.237506       | 0.240137       | 0.085877       | 0.021934       | 0.023554       | 0.161063       | 0.162615       | -0.152979      | 0.061316       | 0.118075       | 0.117773       | 0.038118       | 0.245989       | 0.246036       | 0.248708       | 0.248661       | 0.209518      
16     | 0.004358       | -0.029775      | 0.056232       | 0.029553       | 0.237275       | 0.236631       | 0.096070       | 0.021076       | -0.011948      | 0.155909       | 0.158037       | -0.153779      | 0.058308       | 0.125720       | 0.126859       | 0.017012       | 0.233469       | 0.234011       | 0.254019       | 0.253512       | 0.207296      
17     | 0.011879       | -0.005037      | 0.022200       | 0.023029       | 0.234629       | 0.234975       | 0.095206       | 0.022441       | 0.002936       | 0.167752       | 0.170093       | -0.151798      | 0.057169       | 0.134535       | 0.136358       | 0.007386       | 0.220472       | 0.221261       | 0.244936       | 0.245280       | 0.206106      
18     | 0.035177       | -0.059622      | 0.061221       | 0.019172       | 0.244008       | 0.244917       | 0.085682       | -0.002146      | -0.023079      | 0.160015       | 0.160199       | -0.167186      | 0.017312       | 0.107660       | 0.106140       | -0.002508      | 0.219432       | 0.220284       | 0.231751       | 0.231143       | 0.197317      
19     | 0.015908       | -0.039412      | 0.022049       | -0.001699      | 0.221916       | 0.219828       | 0.084641       | -0.013132      | -0.029949      | 0.151533       | 0.151347       | -0.174773      | 0.021491       | 0.117756       | 0.120986       | -0.015672      | 0.205512       | 0.202053       | 0.228274       | 0.227916       | 0.189708      
20     | -0.004282      | -0.017243      | 0.013497       | -0.006662      | 0.227661       | 0.227238       | 0.102984       | -0.026540      | -0.015293      | 0.147350       | 0.148596       | -0.198260      | 0.015609       | 0.117720       | 0.120310       | -0.057902      | 0.180793       | 0.179757       | 0.218179       | 0.216679       | 0.182380      
21     | -0.023290      | -0.054740      | 0.032284       | -0.009687      | 0.220809       | 0.222122       | 0.149814       | -0.002701      | -0.028961      | 0.156789       | 0.156636       | -0.163774      | 0.019463       | 0.128081       | 0.128122       | -0.011070      | 0.202010       | 0.204080       | 0.228018       | 0.225843       | 0.190291      
22     | -0.002156      | -0.025345      | -0.019379      | -0.008728      | 0.208422       | 0.208129       | 0.095766       | -0.047525      | -0.021825      | 0.146471       | 0.145368       | -0.154864      | 0.041143       | 0.134869       | 0.134282       | -0.024905      | 0.188627       | 0.189361       | 0.227256       | 0.229490       | 0.185899      
23     | -0.056081      | -0.041749      | -0.011334      | 0.002189       | 0.210376       | 0.210412       | 0.107056       | -0.015215      | -0.017498      | 0.141592       | 0.141800       | -0.173863      | 0.023297       | 0.129305       | 0.128118       | -0.040050      | 0.187644       | 0.187852       | 0.217630       | 0.216403       | 0.179800      
24     | -0.045981      | -0.040949      | -0.019591      | -0.016508      | 0.196412       | 0.197300       | 0.147223       | -0.033565      | -0.009395      | 0.160553       | 0.160251       | -0.157776      | -0.001914      | 0.135602       | 0.134797       | -0.039764      | 0.178651       | 0.179202       | 0.217332       | 0.215998       | 0.178344      
25     | 0.006293       | -0.021724      | 0.016827       | -0.021922      | 0.220129       | 0.220686       | 0.063740       | 0.018557       | -0.032529      | 0.167305       | 0.166546       | -0.166039      | 0.038148       | 0.136368       | 0.135163       | -0.041122      | 0.191910       | 0.191834       | 0.213189       | 0.213103       | 0.188150      
26     | 0.000641       | 0.002354       | -0.038611      | -0.024623      | 0.204193       | 0.204985       | 0.100901       | -0.011742      | -0.023488      | 0.162637       | 0.165080       | -0.171542      | -0.004144      | 0.134506       | 0.133288       | 0.005273       | 0.194339       | 0.193028       | 0.214258       | 0.215539       | 0.183265      
27     | -0.017200      | -0.007417      | 0.005200       | -0.004981      | 0.210471       | 0.209642       | 0.095582       | -0.037419      | -0.021516      | 0.146379       | 0.147008       | -0.168911      | 0.045598       | 0.138545       | 0.140044       | -0.011263      | 0.206374       | 0.204399       | 0.223910       | 0.224711       | 0.186610      
28     | -0.022482      | 0.011057       | -0.028528      | 0.002670       | 0.211648       | 0.212360       | 0.103446       | 0.004176       | 0.011619       | 0.174804       | 0.175130       | -0.195256      | 0.020994       | 0.139868       | 0.139790       | -0.060381      | 0.169751       | 0.172251       | 0.218348       | 0.219910       | 0.184652      
29     | -0.027146      | -0.031581      | -0.006784      | -0.025355      | 0.202009       | 0.201429       | 0.082284       | -0.035029      | -0.019270      | 0.151024       | 0.150432       | -0.153026      | 0.041279       | 0.145725       | 0.147113       | -0.045187      | 0.181446       | 0.183398       | 0.214580       | 0.215343       | 0.180682      
30     | -0.061506      | -0.032105      | -0.018404      | -0.037832      | 0.184211       | 0.186216       | 0.100102       | 0.041061       | -0.007865      | 0.165354       | 0.163099       | -0.148282      | 0.005612       | 0.133270       | 0.133629       | -0.038514      | 0.187004       | 0.183947       | 0.227400       | 0.229377       | 0.181296      
31     | -0.018516      | -0.011950      | 0.014958       | -0.045061      | 0.207356       | 0.206027       | 0.113592       | -0.041502      | -0.049041      | 0.155388       | 0.153685       | -0.220830      | -0.007179      | 0.134468       | 0.132837       | -0.036361      | 0.172757       | 0.173068       | 0.194343       | 0.192137       | 0.172466      
32     | -0.011668      | -0.029123      | 0.004066       | -0.035587      | 0.200103       | 0.200197       | 0.116951       | -0.026507      | -0.029159      | 0.154590       | 0.154662       | -0.152171      | 0.018296       | 0.141090       | 0.141817       | -0.043672      | 0.178223       | 0.178211       | 0.225313       | 0.225892       | 0.182970      
33     | -0.038561      | 0.008477       | 0.003771       | -0.031532      | 0.207801       | 0.209576       | 0.131995       | -0.041855      | -0.006802      | 0.154977       | 0.155972       | -0.171954      | 0.015494       | 0.147483       | 0.148424       | -0.060777      | 0.157155       | 0.157019       | 0.230915       | 0.229766       | 0.181699      
34     | -0.028352      | -0.026402      | 0.000348       | -0.039914      | 0.207340       | 0.205408       | 0.083921       | 0.011754       | -0.008226      | 0.167466       | 0.167824       | -0.166321      | 0.002195       | 0.131708       | 0.135202       | -0.038443      | 0.174299       | 0.172657       | 0.218049       | 0.217960       | 0.182048      
35     | -0.023167      | -0.013927      | -0.014076      | -0.003575      | 0.199262       | 0.199796       | 0.110319       | -0.021620      | -0.022008      | 0.156732       | 0.158040       | -0.165223      | 0.022438       | 0.141063       | 0.143240       | -0.024640      | 0.193538       | 0.193893       | 0.221698       | 0.221689       | 0.185116      
36     | -0.041320      | -0.016740      | -0.010849      | -0.034080      | 0.192956       | 0.192938       | 0.156626       | -0.023311      | -0.007612      | 0.165687       | 0.165332       | -0.090831      | 0.012915       | 0.166072       | 0.165053       | -0.019309      | 0.194730       | 0.197979       | 0.223217       | 0.222857       | 0.188508      
37     | -0.038555      | -0.030637      | 0.006746       | -0.017606      | 0.199840       | 0.197675       | 0.128600       | -0.008556      | -0.001948      | 0.162064       | 0.164285       | -0.163511      | 0.022732       | 0.146555       | 0.146764       | -0.028911      | 0.170760       | 0.170600       | 0.244259       | 0.247924       | 0.186910      
38     | 0.004500       | -0.002221      | -0.031287      | -0.034584      | 0.204514       | 0.203501       | 0.104991       | -0.008466      | 0.004371       | 0.163933       | 0.165030       | -0.163912      | -0.014901      | 0.125337       | 0.126487       | -0.037108      | 0.178465       | 0.179738       | 0.224660       | 0.223920       | 0.182972      
39     | -0.037568      | -0.023347      | -0.006178      | -0.005401      | 0.199367       | 0.199263       | 0.132516       | -0.031616      | -0.018230      | 0.168313       | 0.170943       | -0.145220      | 0.023241       | 0.156189       | 0.155017       | -0.028662      | 0.181437       | 0.180358       | 0.225433       | 0.221473       | 0.186441      
40     | -0.025069      | 0.020702       | -0.010053      | -0.010543      | 0.201090       | 0.204770       | 0.134838       | -0.018937      | -0.014048      | 0.163260       | 0.164120       | -0.109255      | -0.010128      | 0.147728       | 0.146984       | 0.001044       | 0.210510       | 0.211109       | 0.231730       | 0.229167       | 0.191735      
41     | -0.027034      | 0.008083       | 0.015207       | -0.002966      | 0.221469       | 0.223897       | 0.139859       | -0.023208      | -0.029065      | 0.157050       | 0.156617       | -0.161260      | 0.010603       | 0.148763       | 0.148326       | -0.045715      | 0.177666       | 0.177715       | 0.223642       | 0.223523       | 0.188726      
42     | -0.041195      | -0.025345      | -0.001364      | -0.006565      | 0.196999       | 0.198366       | 0.152046       | -0.026928      | -0.022936      | 0.158445       | 0.157562       | -0.133170      | -0.005048      | 0.141026       | 0.144073       | -0.018100      | 0.207733       | 0.205978       | 0.218253       | 0.219886       | 0.186066      
43     | 0.011546       | 0.005506       | 0.010535       | -0.031624      | 0.208808       | 0.209270       | 0.176323       | -0.008263      | -0.019840      | 0.171271       | 0.170934       | -0.139879      | 0.013104       | 0.151502       | 0.152796       | -0.055010      | 0.195836       | 0.197422       | 0.218636       | 0.218774       | 0.189323      
44     | -0.036687      | -0.020584      | 0.005181       | 0.004580       | 0.206479       | 0.206213       | 0.149278       | -0.043872      | -0.033525      | 0.146360       | 0.148949       | -0.156936      | 0.029466       | 0.143797       | 0.144270       | -0.023274      | 0.180286       | 0.178546       | 0.246528       | 0.244999       | 0.188213      
45     | -0.030768      | 0.002010       | -0.008386      | 0.018335       | 0.211364       | 0.209534       | 0.125996       | -0.012263      | -0.017092      | 0.168154       | 0.167792       | -0.142423      | 0.010931       | 0.153389       | 0.152387       | -0.032608      | 0.180310       | 0.180849       | 0.235759       | 0.236408       | 0.192145      
46     | -0.055708      | -0.035913      | -0.006673      | 0.001708       | 0.182792       | 0.183917       | 0.153549       | -0.043671      | -0.020047      | 0.149298       | 0.150855       | -0.111465      | -0.008810      | 0.139089       | 0.139309       | -0.036179      | 0.208907       | 0.210131       | 0.222219       | 0.220546       | 0.182987      
47     | -0.038197      | 0.001056       | -0.013254      | -0.012984      | 0.214869       | 0.215023       | 0.130609       | -0.020250      | -0.009261      | 0.164745       | 0.167020       | -0.091298      | 0.028831       | 0.167638       | 0.166570       | -0.025858      | 0.193302       | 0.191366       | 0.218103       | 0.216611       | 0.191483      
48     | -0.031547      | -0.052127      | 0.003118       | 0.000270       | 0.199442       | 0.200172       | 0.096411       | -0.030997      | -0.045070      | 0.144166       | 0.142667       | -0.124918      | -0.009057      | 0.131789       | 0.130250       | 0.008629       | 0.186918       | 0.187189       | 0.246831       | 0.248230       | 0.185749      
49     | -0.020651      | 0.024275       | 0.015930       | -0.029842      | 0.197077       | 0.195878       | 0.182475       | -0.023968      | -0.002389      | 0.173983       | 0.173919       | -0.093916      | 0.028008       | 0.171988       | 0.172003       | -0.023843      | 0.229922       | 0.230856       | 0.212137       | 0.213278       | 0.197432      
50     | -0.062004      | -0.042507      | 0.040103       | -0.027151      | 0.206653       | 0.204295       | 0.106312       | -0.043829      | -0.016225      | 0.148604       | 0.148080       | -0.162495      | 0.026322       | 0.139015       | 0.137451       | 0.000721       | 0.184137       | 0.185704       | 0.236756       | 0.237000       | 0.185671      
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
🛡️  SHADOW DEFENSE SUMMARY (computed only, NOT applied)
  Parameters: n=7, f=2, k=3, m=5, beta=2, rounds=50
  Krum        : attacker selection rate = 0.0000   (chance = A/n = 0.2857)   [rounds where the selected update is malicious]
  Multi-Krum  : DR = 0.0000  FPR = 0.4000  ER = 1.0000   (chance DR = FPR = (n-m)/n = 0.2857)
  Trimmed Mean: DR = 0.4896  FPR = 0.6042  ER = 0.5104   (chance = 2*beta/n = 0.5714)   [DR/FPR = mean trim fraction over attacker/benign submissions]
  Median      : attacker provider rate = 0.1729  attacker total influence = 0.3458  benign provider rate = 0.1308   (chance per client = 1/n = 0.1429)   [no rejection step: DR/FPR n/a]
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
💾 SAVING DATA TO CSV FILES FOR EASY COLLECTION
--------------------------------------------------------------------------------
✅ Global Accuracy saved to: results/qwen_ag_news_rmp_alpha0p3_seed42069_shadow_global_accuracy.csv
✅ Cosine Similarity saved to: results/qwen_ag_news_rmp_alpha0p3_seed42069_shadow_cosine_similarity.csv
✅ Local Accuracy saved to: results/qwen_ag_news_rmp_alpha0p3_seed42069_shadow_local_accuracy.csv

================================================================================
✅ All statistics printed and saved to CSV files!
   You can now easily collect data from multiple runs and compare them.
================================================================================

======================================================================================================================
⏱️  PER-ROUND OVERHEAD SUMMARY (wall-clock seconds)  --  GPU: NVIDIA RTX PRO 6000 Blackwell Server Edition
======================================================================================================================
Attacker columns are summed over all attackers of the round; GRL = select+graph+vgae+spectral+expand;
optimize = the K-step manipulation loop; diag = logging-only forwards; eval_local = per-client test-set
evaluation kept for the local-accuracy figure (experiment bookkeeping, not part of the FL protocol).
----------------------------------------------------------------------------------------------------------------------------------------
     round      GRL    setup  optimize  steps  finalize    diag    attack   att_GB  train_ben aggregate  eval_glob   eval_loc      round
----------------------------------------------------------------------------------------------------------------------------------------
         1    0.000     0.00      0.00      0      0.00    0.00      0.09        -     120.84      0.18       6.92       8.59     136.72
         2    0.000     0.00      0.00      0      0.00    0.00      0.10        -     119.44      0.13       6.93       7.95     134.62
         3    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.18      0.13       6.93       7.62     134.02
         4    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.46      0.11       6.93       7.55     134.21
         5    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.49      0.11       6.93       7.56     134.25
         6    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.48      0.12       6.93       7.56     134.25
         7    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.49      0.11       6.93       7.56     134.25
         8    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.40      0.12       6.93       7.54     134.15
         9    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.44      0.11       6.93       7.60     134.22
        10    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.21      0.11       6.94       7.58     133.99
        11    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.27      0.14       6.93       7.61     134.11
        12    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.26      0.11       6.94       7.60     134.02
        13    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.36      0.10       6.94       7.60     134.12
        14    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.54      0.11       6.93       7.59     134.33
        15    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.51      0.11       6.93       7.58     134.29
        16    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.29      0.11       6.93       7.56     134.05
        17    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.19      0.11       6.93       7.56     133.96
        18    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.17      0.11       6.93       7.58     133.93
        19    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.33      0.11       6.93       7.57     134.11
        20    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.17      0.11       6.93       7.58     133.94
        21    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.19      0.12       6.93       7.57     133.98
        22    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.52      0.12       6.93       7.54     134.26
        23    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.43      0.11       6.93       7.56     134.17
        24    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.28      0.11       6.93       7.56     134.06
        25    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.46      0.11       6.93       7.53     134.17
        26    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.30      0.10       6.93       7.58     134.06
        27    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.18      0.12       6.93       7.56     133.96
        28    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.20      0.11       6.93       7.60     134.01
        29    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.23      0.11       6.93       7.60     134.01
        30    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.18      0.11       6.93       7.56     133.93
        31    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.15      0.11       6.93       7.58     133.93
        32    0.000     0.00      0.00      0      0.00    0.00      0.10        -     119.23      0.11       6.93       7.56     133.99
        33    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.18      0.11       6.93       7.58     133.95
        34    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.21      0.11       6.93       7.60     133.99
        35    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.20      0.11       6.93       7.60     133.98
        36    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.53      0.12       6.93       7.58     134.32
        37    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.23      0.11       6.93       7.55     133.94
        38    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.20      0.11       6.93       7.58     133.97
        39    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.47      0.10       6.93       7.56     134.23
        40    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.21      0.11       6.94       7.57     133.93
        41    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.19      0.11       6.93       7.57     133.96
        42    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.19      0.11       6.93       7.57     133.96
        43    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.20      0.11       6.93       7.56     133.94
        44    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.38      0.11       6.93       7.58     134.16
        45    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.52      0.11       6.93       7.58     134.31
        46    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.48      0.11       6.93       7.57     134.24
        47    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.48      0.12       6.93       7.58     134.26
        48    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.49      0.11       6.93       7.58     134.25
        49    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.54      0.11       6.93       7.57     134.31
        50    0.000     0.00      0.00      0      0.00    0.00      0.07        -     119.50      0.11       6.93       7.58     134.27
----------------------------------------------------------------------------------------------------------------------------------------
 mean r>=2    0.000     0.00      0.00    0.0      0.00    0.00      0.08        -     119.33      0.11       6.93       7.58     134.11
  std r>=2    0.000     0.00      0.00    0.0      0.00    0.00      0.01        -       0.14      0.01       0.00       0.06       0.15
  mean all    0.000     0.00      0.00    0.0      0.00    0.00      0.09        -     119.36      0.11       6.93       7.60     134.16
   sum all    0.000     0.00      0.00    0.0      0.00    0.00      4.25        -    5968.10      5.65     346.55     380.07    6708.05
----------------------------------------------------------------------------------------------------------------------------------------

Wall-clock totals (s): setup_and_initial_eval_sec 29.0, rounds_sec 6726.7, experiment_sec 6755.7, rounds_completed 50.0
Overhead per round saved to: results/qwen_ag_news_rmp_alpha0p3_seed42069_shadow_overhead_rounds.csv
Overhead per attacker-round saved to: results/qwen_ag_news_rmp_alpha0p3_seed42069_shadow_overhead_attackers.csv
Summary saved to: results/qwen_ag_news_rmp_alpha0p3_seed42069_shadow_summary.txt (226 KB)


🚀 Starting AugMP experiment...
============================================================
Using configuration from main.py
Full log file: results/qwen_ag_news_rmp_alpha0p3_seed42069_shadow_log.txt
============================================================
Running Gaussian Attack (Random Model Poisoning Baseline)...

==================================================
Setting up Experiment: qwen_ag_news_rmp_alpha0p3_seed42069_shadow
==================================================
tokenizer_config.json: 
 7.23k/? [00:00<00:00, 1.97MB/s]
vocab.json: 
 2.78M/? [00:00<00:00, 51.2MB/s]
merges.txt: 
 1.67M/? [00:00<00:00, 186MB/s]
tokenizer.json: 
 7.03M/? [00:00<00:00, 318MB/s]
Loading AG News dataset...
  ✅ Found local AG News CSVs under data/AG News Datasets/. Loading...
  📊 Full AG News Dataset: Train=120000, Test=7600
  ⚠️  WARNING: Using limited dataset size (20000) for faster experimentation
     This may affect results reproducibility. For paper reproduction, use full dataset.
  ✅ Dataset ready! Train: 20000, Test: 3000
  ⚠️  Note: Using subset of full dataset (Train: 20000/120000, Test: 3000/7600)

Partitioning data (Non-IID distribution)...
  Non-IID distribution (Dirichlet alpha=0.3)
    Client 0 (BENIGN): 3184 samples (Label 0: 4.8%, Label 1: 23.1%, Label 2: 13.0%, Label 3: 59.1%)
    Client 1 (BENIGN): 1127 samples (Label 0: 81.7%, Label 1: 5.3%, Label 2: 9.8%, Label 3: 3.2%)
    Client 2 (BENIGN): 991 samples (Label 0: 51.3%, Label 1: 0.3%, Label 2: 46.0%, Label 3: 2.4%)
    Client 3 (BENIGN): 3560 samples (Label 0: 26.3%, Label 1: 33.0%, Label 2: 0.0%, Label 3: 40.7%)
    Client 4 (BENIGN): 3650 samples (Label 0: 65.0%, Label 1: 0.0%, Label 2: 7.8%, Label 3: 27.2%)
    Client 5 (ATTACKER): 5473 samples (Label 0: 0.4%, Label 1: 49.6%, Label 2: 47.8%, Label 3: 2.3%)
    Client 6 (ATTACKER): 2015 samples (Label 0: 2.6%, Label 1: 19.8%, Label 2: 52.9%, Label 3: 24.7%)

  [Note] Attackers are assigned only data *quantities* (sizes) following the non-IID distribution, for experimental setup. In reality, attackers do NOT perform local training and do NOT use these local data (dataset-free). They also do NOT access other local agents' data.
Initializing global model (Qwen/Qwen2.5-0.5B) with LoRA...
config.json: 100%
 681/681 [00:00<00:00, 227kB/s]
model.safetensors: 100%
 988M/988M [00:07<00:00, 83.5MB/s]
Some weights of Qwen2ForSequenceClassification were not initialized from the model checkpoint at Qwen/Qwen2.5-0.5B and are newly initialized: ['score.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
  Loaded model: Qwen2ForSequenceClassification (from Qwen/Qwen2.5-0.5B) with LoRA
  Trainable params: 1,084,928 (0.22% of 495,121,280 total)

Creating federated learning clients...
  Client 0: BENIGN (3184 samples)
  Client 1: BENIGN (1127 samples)
  Client 2: BENIGN (991 samples)
  Client 3: BENIGN (3560 samples)
  Client 4: BENIGN (3650 samples)
  Client 5: ATTACKER (Gaussian Attack, USENIX Security '20)
    Claimed data size D'_j(t): 5473 (matches assigned data)
    Lagrangian Dual enabled: λ_dist(1)=0.1
  Client 6: ATTACKER (Gaussian Attack, USENIX Security '20)
    Claimed data size D'_j(t): 2015 (matches assigned data)
    Lagrangian Dual enabled: λ_dist(1)=0.1

Evaluating initial model...
Initial Performance - Clean Accuracy: 0.2110

==================================================
Starting Federated Learning Rounds
==================================================

============================================================
Round 1/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.8633, effective_std_norm=0.7369, attack_norm=1.1358, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.8633, effective_std_norm=0.7369, attack_norm=1.1354, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 1.001267
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.572, Std Dev: 0.021
    Client 0 (Benign): 0.564
    Client 1 (Benign): 0.561
    Client 2 (Benign): 0.529
    Client 3 (Benign): 0.589
    Client 4 (Benign): 0.573
    Client 5 (Attacker): 0.593
    Client 6 (Attacker): 0.592
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.738351, Std Dev: 0.079435
    Client 0 (Benign): 0.748197
    Client 1 (Benign): 0.772142
    Client 2 (Benign): 0.808414
    Client 3 (Benign): 0.791900
    Client 4 (Benign): 0.781588
    Client 5 (Attacker): 0.558498
    Client 6 (Attacker): 0.707719
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=1.361764 krum=3.199984 mkrum=KEEP tm_trim=0.6479 (lo 0.3237 / hi 0.3242) med_prov=0.1087 d_med=0.868109
    [shadow] C1 (B): norm=0.606631 krum=1.950418 mkrum=KEEP tm_trim=0.5257 (lo 0.2632 / hi 0.2625) med_prov=0.1518 d_med=0.657874
    [shadow] C2 (B): norm=0.560976 krum=2.038867 mkrum=KEEP tm_trim=0.5681 (lo 0.2844 / hi 0.2836) med_prov=0.1442 d_med=0.694092
    [shadow] C3 (B): norm=1.518111 krum=3.472590 mkrum=REJECT tm_trim=0.7290 (lo 0.3638 / hi 0.3652) med_prov=0.0797 d_med=0.951056
    [shadow] C4 (B): norm=1.264700 krum=3.289043 mkrum=REJECT tm_trim=0.6094 (lo 0.3057 / hi 0.3038) med_prov=0.1406 d_med=0.788349
    [shadow] C5 (A): norm=1.135799 krum=2.953588 mkrum=KEEP tm_trim=0.4599 (lo 0.2296 / hi 0.2304) med_prov=0.1879 d_med=0.649520
    [shadow] C6 (A): norm=1.135370 krum=2.954827 mkrum=KEEP tm_trim=0.4600 (lo 0.2297 / hi 0.2303) med_prov=0.1872 d_med=0.650600

⏱️  Overhead round 1 (wall-clock s): round 136.72 | broadcast 0.02 | prepare 0.00 | benign train 120.84 [0:30.8 1:11.2 2:10.0 3:34.0 4:34.9] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.18 | observe 0.00 | eval_global 6.92 | eval_local 8.59 (bookkeeping) | unaccounted 0.06
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.04s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 1 Results:
  Clean Accuracy: 0.4560
  ΔClean vs prev: +0.2450
  ΔClean vs best: +0.0000
  Global Loss: 1.9844

============================================================
Round 2/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.6845, effective_std_norm=0.5533, attack_norm=0.8793, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.6845, effective_std_norm=0.5533, attack_norm=0.8784, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.795785
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.588, Std Dev: 0.057
    Client 0 (Benign): 0.632
    Client 1 (Benign): 0.582
    Client 2 (Benign): 0.453
    Client 3 (Benign): 0.602
    Client 4 (Benign): 0.619
    Client 5 (Attacker): 0.613
    Client 6 (Attacker): 0.613
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.554027, Std Dev: 0.073667
    Client 0 (Benign): 0.539058
    Client 1 (Benign): 0.587593
    Client 2 (Benign): 0.687017
    Client 3 (Benign): 0.577017
    Client 4 (Benign): 0.533449
    Client 5 (Attacker): 0.421615
    Client 6 (Attacker): 0.532438
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=1.088580 krum=1.859704 mkrum=KEEP tm_trim=0.6459 (lo 0.3234 / hi 0.3225) med_prov=0.1124 d_med=0.607232
    [shadow] C1 (B): norm=0.455790 krum=1.174375 mkrum=KEEP tm_trim=0.5249 (lo 0.2625 / hi 0.2624) med_prov=0.1532 d_med=0.519266
    [shadow] C2 (B): norm=0.441318 krum=1.377192 mkrum=KEEP tm_trim=0.6259 (lo 0.3131 / hi 0.3128) med_prov=0.1204 d_med=0.614598
    [shadow] C3 (B): norm=1.121905 krum=1.988635 mkrum=REJECT tm_trim=0.6774 (lo 0.3385 / hi 0.3390) med_prov=0.1031 d_med=0.665772
    [shadow] C4 (B): norm=1.013365 krum=1.915282 mkrum=REJECT tm_trim=0.5932 (lo 0.2970 / hi 0.2963) med_prov=0.1415 d_med=0.574524
    [shadow] C5 (A): norm=0.879329 krum=1.733450 mkrum=KEEP tm_trim=0.4665 (lo 0.2328 / hi 0.2338) med_prov=0.1845 d_med=0.488215
    [shadow] C6 (A): norm=0.878372 krum=1.730442 mkrum=KEEP tm_trim=0.4662 (lo 0.2329 / hi 0.2333) med_prov=0.1848 d_med=0.487784

⏱️  Overhead round 2 (wall-clock s): round 134.62 | broadcast 0.03 | prepare 0.00 | benign train 119.44 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.10 [5:0.0 6:0.1] | aggregate 0.13 | observe 0.00 | eval_global 6.93 | eval_local 7.95 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.04s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.07s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 2 Results:
  Clean Accuracy: 0.6867
  ΔClean vs prev: +0.2307
  ΔClean vs best: +0.0000
  Global Loss: 0.9820

============================================================
Round 3/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.4736, effective_std_norm=0.4542, attack_norm=0.6559, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.4736, effective_std_norm=0.4542, attack_norm=0.6571, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.554145
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.481, Std Dev: 0.052
    Client 0 (Benign): 0.517
    Client 1 (Benign): 0.446
    Client 2 (Benign): 0.372
    Client 3 (Benign): 0.475
    Client 4 (Benign): 0.507
    Client 5 (Attacker): 0.524
    Client 6 (Attacker): 0.524
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.454044, Std Dev: 0.050177
    Client 0 (Benign): 0.472324
    Client 1 (Benign): 0.457791
    Client 2 (Benign): 0.510549
    Client 3 (Benign): 0.484660
    Client 4 (Benign): 0.475037
    Client 5 (Attacker): 0.342946
    Client 6 (Attacker): 0.435001
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.797540 krum=1.400235 mkrum=KEEP tm_trim=0.6482 (lo 0.3236 / hi 0.3246) med_prov=0.1136 d_med=0.512642
    [shadow] C1 (B): norm=0.343250 krum=0.812223 mkrum=KEEP tm_trim=0.5171 (lo 0.2587 / hi 0.2584) med_prov=0.1617 d_med=0.395750
    [shadow] C2 (B): norm=0.389034 krum=0.892518 mkrum=KEEP tm_trim=0.5729 (lo 0.2867 / hi 0.2862) med_prov=0.1408 d_med=0.444619
    [shadow] C3 (B): norm=0.790113 krum=1.445445 mkrum=REJECT tm_trim=0.6543 (lo 0.3274 / hi 0.3269) med_prov=0.1135 d_med=0.542769
    [shadow] C4 (B): norm=0.789663 krum=1.402725 mkrum=REJECT tm_trim=0.6430 (lo 0.3213 / hi 0.3217) med_prov=0.1182 d_med=0.522244
    [shadow] C5 (A): norm=0.655929 krum=1.129692 mkrum=KEEP tm_trim=0.4820 (lo 0.2414 / hi 0.2407) med_prov=0.1761 d_med=0.402297
    [shadow] C6 (A): norm=0.657132 krum=1.132291 mkrum=KEEP tm_trim=0.4824 (lo 0.2410 / hi 0.2414) med_prov=0.1760 d_med=0.403343

⏱️  Overhead round 3 (wall-clock s): round 134.02 | broadcast 0.03 | prepare 0.00 | benign train 119.18 [0:30.3 1:10.9 2:9.7 3:33.7 4:34.6] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.13 | observe 0.00 | eval_global 6.93 | eval_local 7.62 (bookkeeping) | unaccounted 0.05
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 3 Results:
  Clean Accuracy: 0.7763
  ΔClean vs prev: +0.0897
  ΔClean vs best: +0.0000
  Global Loss: 0.6503

============================================================
Round 4/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.3443, effective_std_norm=0.3943, attack_norm=0.5236, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.3443, effective_std_norm=0.3943, attack_norm=0.5237, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.404244
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.376, Std Dev: 0.047
    Client 0 (Benign): 0.398
    Client 1 (Benign): 0.334
    Client 2 (Benign): 0.305
    Client 3 (Benign): 0.337
    Client 4 (Benign): 0.388
    Client 5 (Attacker): 0.434
    Client 6 (Attacker): 0.434
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.392465, Std Dev: 0.046523
    Client 0 (Benign): 0.413323
    Client 1 (Benign): 0.377083
    Client 2 (Benign): 0.401287
    Client 3 (Benign): 0.441631
    Client 4 (Benign): 0.441646
    Client 5 (Attacker): 0.296011
    Client 6 (Attacker): 0.376277
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.601862 krum=0.992515 mkrum=KEEP tm_trim=0.6359 (lo 0.3178 / hi 0.3181) med_prov=0.1181 d_med=0.436687
    [shadow] C1 (B): norm=0.313159 krum=0.627507 mkrum=KEEP tm_trim=0.5066 (lo 0.2535 / hi 0.2530) med_prov=0.1687 d_med=0.322626
    [shadow] C2 (B): norm=0.336097 krum=0.656404 mkrum=KEEP tm_trim=0.5424 (lo 0.2714 / hi 0.2710) med_prov=0.1529 d_med=0.344566
    [shadow] C3 (B): norm=0.617252 krum=1.098556 mkrum=REJECT tm_trim=0.6663 (lo 0.3330 / hi 0.3333) med_prov=0.1084 d_med=0.487695
    [shadow] C4 (B): norm=0.644867 krum=1.100318 mkrum=REJECT tm_trim=0.6657 (lo 0.3331 / hi 0.3326) med_prov=0.1084 d_med=0.482213
    [shadow] C5 (A): norm=0.523618 krum=0.824447 mkrum=KEEP tm_trim=0.4916 (lo 0.2455 / hi 0.2460) med_prov=0.1722 d_med=0.351372
    [shadow] C6 (A): norm=0.523692 krum=0.824171 mkrum=KEEP tm_trim=0.4915 (lo 0.2455 / hi 0.2460) med_prov=0.1713 d_med=0.351780

⏱️  Overhead round 4 (wall-clock s): round 134.21 | broadcast 0.02 | prepare 0.00 | benign train 119.46 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.55 (bookkeeping) | unaccounted 0.06
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 4 Results:
  Clean Accuracy: 0.8037
  ΔClean vs prev: +0.0273
  ΔClean vs best: +0.0000
  Global Loss: 0.5507

============================================================
Round 5/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.2788, effective_std_norm=0.3784, attack_norm=0.4696, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.2788, effective_std_norm=0.3784, attack_norm=0.4703, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.334329
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.280, Std Dev: 0.052
    Client 0 (Benign): 0.296
    Client 1 (Benign): 0.228
    Client 2 (Benign): 0.218
    Client 3 (Benign): 0.231
    Client 4 (Benign): 0.284
    Client 5 (Attacker): 0.350
    Client 6 (Attacker): 0.350
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.375579, Std Dev: 0.047718
    Client 0 (Benign): 0.412929
    Client 1 (Benign): 0.351386
    Client 2 (Benign): 0.369217
    Client 3 (Benign): 0.429866
    Client 4 (Benign): 0.422274
    Client 5 (Attacker): 0.283070
    Client 6 (Attacker): 0.360311
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.551306 krum=0.942830 mkrum=KEEP tm_trim=0.6542 (lo 0.3272 / hi 0.3270) med_prov=0.1111 d_med=0.436075
    [shadow] C1 (B): norm=0.282658 krum=0.578174 mkrum=KEEP tm_trim=0.4945 (lo 0.2471 / hi 0.2474) med_prov=0.1738 d_med=0.300402
    [shadow] C2 (B): norm=0.308478 krum=0.597401 mkrum=KEEP tm_trim=0.5346 (lo 0.2681 / hi 0.2665) med_prov=0.1568 d_med=0.315447
    [shadow] C3 (B): norm=0.552574 krum=1.008450 mkrum=REJECT tm_trim=0.6694 (lo 0.3339 / hi 0.3354) med_prov=0.1059 d_med=0.471294
    [shadow] C4 (B): norm=0.566096 krum=0.982801 mkrum=REJECT tm_trim=0.6565 (lo 0.3284 / hi 0.3281) med_prov=0.1123 d_med=0.457535
    [shadow] C5 (A): norm=0.469648 krum=0.747070 mkrum=KEEP tm_trim=0.4949 (lo 0.2469 / hi 0.2480) med_prov=0.1704 d_med=0.337771
    [shadow] C6 (A): norm=0.470268 krum=0.747947 mkrum=KEEP tm_trim=0.4959 (lo 0.2484 / hi 0.2476) med_prov=0.1697 d_med=0.338446

⏱️  Overhead round 5 (wall-clock s): round 134.25 | broadcast 0.02 | prepare 0.00 | benign train 119.49 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.56 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.06s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 5 Results:
  Clean Accuracy: 0.8267
  ΔClean vs prev: +0.0230
  ΔClean vs best: +0.0000
  Global Loss: 0.5189

============================================================
Round 6/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.2370, effective_std_norm=0.3608, attack_norm=0.4323, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.2370, effective_std_norm=0.3608, attack_norm=0.4313, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.290050
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.218, Std Dev: 0.056
    Client 0 (Benign): 0.214
    Client 1 (Benign): 0.148
    Client 2 (Benign): 0.165
    Client 3 (Benign): 0.177
    Client 4 (Benign): 0.226
    Client 5 (Attacker): 0.297
    Client 6 (Attacker): 0.297
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.358176, Std Dev: 0.044734
    Client 0 (Benign): 0.407238
    Client 1 (Benign): 0.338550
    Client 2 (Benign): 0.350835
    Client 3 (Benign): 0.399998
    Client 4 (Benign): 0.396758
    Client 5 (Attacker): 0.270381
    Client 6 (Attacker): 0.343471
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C0 (B), C3 (B)
    [shadow] C0 (B): norm=0.514528 krum=0.902211 mkrum=REJECT tm_trim=0.6640 (lo 0.3318 / hi 0.3322) med_prov=0.1085 d_med=0.433331
    [shadow] C1 (B): norm=0.263987 krum=0.539099 mkrum=KEEP tm_trim=0.5067 (lo 0.2534 / hi 0.2533) med_prov=0.1685 d_med=0.291460
    [shadow] C2 (B): norm=0.296837 krum=0.551331 mkrum=KEEP tm_trim=0.5344 (lo 0.2676 / hi 0.2669) med_prov=0.1564 d_med=0.300712
    [shadow] C3 (B): norm=0.496322 krum=0.884287 mkrum=REJECT tm_trim=0.6580 (lo 0.3287 / hi 0.3293) med_prov=0.1101 d_med=0.437400
    [shadow] C4 (B): norm=0.512900 krum=0.875283 mkrum=KEEP tm_trim=0.6476 (lo 0.3235 / hi 0.3241) med_prov=0.1159 d_med=0.428649
    [shadow] C5 (A): norm=0.432340 krum=0.683439 mkrum=KEEP tm_trim=0.4947 (lo 0.2480 / hi 0.2467) med_prov=0.1706 d_med=0.322700
    [shadow] C6 (A): norm=0.431343 krum=0.681850 mkrum=KEEP tm_trim=0.4946 (lo 0.2471 / hi 0.2475) med_prov=0.1700 d_med=0.322310

⏱️  Overhead round 6 (wall-clock s): round 134.25 | broadcast 0.03 | prepare 0.00 | benign train 119.48 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.12 | observe 0.00 | eval_global 6.93 | eval_local 7.56 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.04s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 6 Results:
  Clean Accuracy: 0.8340
  ΔClean vs prev: +0.0073
  ΔClean vs best: +0.0000
  Global Loss: 0.4863

============================================================
Round 7/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.2107, effective_std_norm=0.3523, attack_norm=0.4106, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.2107, effective_std_norm=0.3523, attack_norm=0.4104, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.262581
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.176, Std Dev: 0.056
    Client 0 (Benign): 0.157
    Client 1 (Benign): 0.135
    Client 2 (Benign): 0.108
    Client 3 (Benign): 0.135
    Client 4 (Benign): 0.178
    Client 5 (Attacker): 0.259
    Client 6 (Attacker): 0.260
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.349396, Std Dev: 0.045092
    Client 0 (Benign): 0.387987
    Client 1 (Benign): 0.323725
    Client 2 (Benign): 0.343472
    Client 3 (Benign): 0.404621
    Client 4 (Benign): 0.387316
    Client 5 (Attacker): 0.263633
    Client 6 (Attacker): 0.335018
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.463290 krum=0.812476 mkrum=KEEP tm_trim=0.6474 (lo 0.3234 / hi 0.3240) med_prov=0.1136 d_med=0.407454
    [shadow] C1 (B): norm=0.266272 krum=0.507022 mkrum=KEEP tm_trim=0.4901 (lo 0.2447 / hi 0.2454) med_prov=0.1760 d_med=0.277751
    [shadow] C2 (B): norm=0.278263 krum=0.527452 mkrum=KEEP tm_trim=0.5382 (lo 0.2694 / hi 0.2688) med_prov=0.1562 d_med=0.294630
    [shadow] C3 (B): norm=0.498823 krum=0.896449 mkrum=REJECT tm_trim=0.6816 (lo 0.3406 / hi 0.3409) med_prov=0.1016 d_med=0.448370
    [shadow] C4 (B): norm=0.480349 krum=0.819918 mkrum=REJECT tm_trim=0.6493 (lo 0.3246 / hi 0.3247) med_prov=0.1143 d_med=0.414855
    [shadow] C5 (A): norm=0.410645 krum=0.648341 mkrum=KEEP tm_trim=0.4973 (lo 0.2490 / hi 0.2482) med_prov=0.1692 d_med=0.315113
    [shadow] C6 (A): norm=0.410375 krum=0.647829 mkrum=KEEP tm_trim=0.4961 (lo 0.2481 / hi 0.2479) med_prov=0.1690 d_med=0.314543

⏱️  Overhead round 7 (wall-clock s): round 134.25 | broadcast 0.02 | prepare 0.00 | benign train 119.49 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.56 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 7 Results:
  Clean Accuracy: 0.8487
  ΔClean vs prev: +0.0147
  ΔClean vs best: +0.0000
  Global Loss: 0.4585

============================================================
Round 8/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1974, effective_std_norm=0.3519, attack_norm=0.4038, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1974, effective_std_norm=0.3519, attack_norm=0.4039, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.251116
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.146, Std Dev: 0.059
    Client 0 (Benign): 0.121
    Client 1 (Benign): 0.105
    Client 2 (Benign): 0.070
    Client 3 (Benign): 0.117
    Client 4 (Benign): 0.143
    Client 5 (Attacker): 0.234
    Client 6 (Attacker): 0.234
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.348954, Std Dev: 0.046136
    Client 0 (Benign): 0.376639
    Client 1 (Benign): 0.320734
    Client 2 (Benign): 0.341335
    Client 3 (Benign): 0.400985
    Client 4 (Benign): 0.404490
    Client 5 (Attacker): 0.263568
    Client 6 (Attacker): 0.334926
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.428726 krum=0.755355 mkrum=KEEP tm_trim=0.6262 (lo 0.3124 / hi 0.3138) med_prov=0.1221 d_med=0.387427
    [shadow] C1 (B): norm=0.260932 krum=0.506555 mkrum=KEEP tm_trim=0.4873 (lo 0.2439 / hi 0.2434) med_prov=0.1774 d_med=0.275183
    [shadow] C2 (B): norm=0.269792 krum=0.527286 mkrum=KEEP tm_trim=0.5405 (lo 0.2703 / hi 0.2701) med_prov=0.1541 d_med=0.292030
    [shadow] C3 (B): norm=0.489746 krum=0.880694 mkrum=REJECT tm_trim=0.6814 (lo 0.3406 / hi 0.3408) med_prov=0.1014 d_med=0.441557
    [shadow] C4 (B): norm=0.499677 krum=0.887229 mkrum=REJECT tm_trim=0.6687 (lo 0.3346 / hi 0.3341) med_prov=0.1075 d_med=0.441774
    [shadow] C5 (A): norm=0.403758 krum=0.645077 mkrum=KEEP tm_trim=0.4985 (lo 0.2496 / hi 0.2489) med_prov=0.1681 d_med=0.315078
    [shadow] C6 (A): norm=0.403853 krum=0.644919 mkrum=KEEP tm_trim=0.4973 (lo 0.2485 / hi 0.2488) med_prov=0.1694 d_med=0.314970

⏱️  Overhead round 8 (wall-clock s): round 134.15 | broadcast 0.02 | prepare 0.00 | benign train 119.40 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.08 [5:0.0 6:0.1] | aggregate 0.12 | observe 0.00 | eval_global 6.93 | eval_local 7.54 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 8 Results:
  Clean Accuracy: 0.8573
  ΔClean vs prev: +0.0087
  ΔClean vs best: +0.0000
  Global Loss: 0.4569

============================================================
Round 9/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.2040, effective_std_norm=0.3559, attack_norm=0.4099, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.2040, effective_std_norm=0.3559, attack_norm=0.4104, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.256382
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.158, Std Dev: 0.057
    Client 0 (Benign): 0.134
    Client 1 (Benign): 0.122
    Client 2 (Benign): 0.088
    Client 3 (Benign): 0.117
    Client 4 (Benign): 0.156
    Client 5 (Attacker): 0.243
    Client 6 (Attacker): 0.244
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.352674, Std Dev: 0.046707
    Client 0 (Benign): 0.389607
    Client 1 (Benign): 0.322926
    Client 2 (Benign): 0.344110
    Client 3 (Benign): 0.404425
    Client 4 (Benign): 0.403280
    Client 5 (Attacker): 0.266054
    Client 6 (Attacker): 0.338316
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.451495 krum=0.807713 mkrum=KEEP tm_trim=0.6390 (lo 0.3194 / hi 0.3196) med_prov=0.1173 d_med=0.404391
    [shadow] C1 (B): norm=0.267995 krum=0.518470 mkrum=KEEP tm_trim=0.4880 (lo 0.2437 / hi 0.2443) med_prov=0.1761 d_med=0.277521
    [shadow] C2 (B): norm=0.277869 krum=0.539608 mkrum=KEEP tm_trim=0.5370 (lo 0.2690 / hi 0.2680) med_prov=0.1557 d_med=0.295592
    [shadow] C3 (B): norm=0.489133 krum=0.885021 mkrum=REJECT tm_trim=0.6759 (lo 0.3377 / hi 0.3382) med_prov=0.1038 d_med=0.444194
    [shadow] C4 (B): norm=0.499242 krum=0.883385 mkrum=REJECT tm_trim=0.6656 (lo 0.3331 / hi 0.3325) med_prov=0.1084 d_med=0.437851
    [shadow] C5 (A): norm=0.409892 krum=0.657690 mkrum=KEEP tm_trim=0.4973 (lo 0.2482 / hi 0.2492) med_prov=0.1693 d_med=0.318048
    [shadow] C6 (A): norm=0.410360 krum=0.657904 mkrum=KEEP tm_trim=0.4971 (lo 0.2489 / hi 0.2482) med_prov=0.1693 d_med=0.318308

⏱️  Overhead round 9 (wall-clock s): round 134.22 | broadcast 0.02 | prepare 0.00 | benign train 119.44 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.60 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 9 Results:
  Clean Accuracy: 0.8763
  ΔClean vs prev: +0.0190
  ΔClean vs best: +0.0000
  Global Loss: 0.4057

============================================================
Round 10/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1926, effective_std_norm=0.3476, attack_norm=0.3974, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1926, effective_std_norm=0.3476, attack_norm=0.3976, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.245039
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.141, Std Dev: 0.060
    Client 0 (Benign): 0.115
    Client 1 (Benign): 0.103
    Client 2 (Benign): 0.061
    Client 3 (Benign): 0.113
    Client 4 (Benign): 0.137
    Client 5 (Attacker): 0.229
    Client 6 (Attacker): 0.229
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.344461, Std Dev: 0.045996
    Client 0 (Benign): 0.379934
    Client 1 (Benign): 0.315274
    Client 2 (Benign): 0.334547
    Client 3 (Benign): 0.400973
    Client 4 (Benign): 0.389743
    Client 5 (Attacker): 0.259749
    Client 6 (Attacker): 0.331010
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.433618 krum=0.761259 mkrum=KEEP tm_trim=0.6401 (lo 0.3202 / hi 0.3198) med_prov=0.1171 d_med=0.393391
    [shadow] C1 (B): norm=0.261002 krum=0.498842 mkrum=KEEP tm_trim=0.4926 (lo 0.2464 / hi 0.2461) med_prov=0.1749 d_med=0.271302
    [shadow] C2 (B): norm=0.262680 krum=0.517519 mkrum=KEEP tm_trim=0.5361 (lo 0.2683 / hi 0.2678) med_prov=0.1560 d_med=0.287117
    [shadow] C3 (B): norm=0.488075 krum=0.864670 mkrum=REJECT tm_trim=0.6805 (lo 0.3396 / hi 0.3410) med_prov=0.1025 d_med=0.441374
    [shadow] C4 (B): norm=0.475667 krum=0.829021 mkrum=REJECT tm_trim=0.6567 (lo 0.3282 / hi 0.3285) med_prov=0.1113 d_med=0.422456
    [shadow] C5 (A): norm=0.397361 krum=0.628521 mkrum=KEEP tm_trim=0.4975 (lo 0.2492 / hi 0.2483) med_prov=0.1687 d_med=0.310803
    [shadow] C6 (A): norm=0.397550 krum=0.628903 mkrum=KEEP tm_trim=0.4965 (lo 0.2480 / hi 0.2484) med_prov=0.1694 d_med=0.311297

⏱️  Overhead round 10 (wall-clock s): round 133.99 | broadcast 0.02 | prepare 0.00 | benign train 119.21 [0:30.2 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.58 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 10 Results:
  Clean Accuracy: 0.8763
  ΔClean vs prev: +0.0000
  ΔClean vs best: +0.0000
  Global Loss: 0.4053

============================================================
Round 11/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1855, effective_std_norm=0.3469, attack_norm=0.3930, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1855, effective_std_norm=0.3469, attack_norm=0.3932, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.237554
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.125, Std Dev: 0.065
    Client 0 (Benign): 0.109
    Client 1 (Benign): 0.088
    Client 2 (Benign): 0.026
    Client 3 (Benign): 0.087
    Client 4 (Benign): 0.131
    Client 5 (Attacker): 0.216
    Client 6 (Attacker): 0.216
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.343903, Std Dev: 0.043586
    Client 0 (Benign): 0.385132
    Client 1 (Benign): 0.318285
    Client 2 (Benign): 0.344774
    Client 3 (Benign): 0.393240
    Client 4 (Benign): 0.377116
    Client 5 (Attacker): 0.259028
    Client 6 (Attacker): 0.329745
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.444449 krum=0.792800 mkrum=KEEP tm_trim=0.6422 (lo 0.3211 / hi 0.3211) med_prov=0.1164 d_med=0.402304
    [shadow] C1 (B): norm=0.270448 krum=0.520438 mkrum=KEEP tm_trim=0.5029 (lo 0.2514 / hi 0.2516) med_prov=0.1707 d_med=0.278829
    [shadow] C2 (B): norm=0.271284 krum=0.546750 mkrum=KEEP tm_trim=0.5476 (lo 0.2740 / hi 0.2736) med_prov=0.1513 d_med=0.300603
    [shadow] C3 (B): norm=0.469403 krum=0.840560 mkrum=REJECT tm_trim=0.6751 (lo 0.3372 / hi 0.3379) med_prov=0.1044 d_med=0.432365
    [shadow] C4 (B): norm=0.457256 krum=0.796295 mkrum=REJECT tm_trim=0.6405 (lo 0.3199 / hi 0.3206) med_prov=0.1178 d_med=0.405638
    [shadow] C5 (A): norm=0.393042 krum=0.634782 mkrum=KEEP tm_trim=0.4956 (lo 0.2481 / hi 0.2475) med_prov=0.1702 d_med=0.309790
    [shadow] C6 (A): norm=0.393176 krum=0.634695 mkrum=KEEP tm_trim=0.4961 (lo 0.2483 / hi 0.2478) med_prov=0.1691 d_med=0.309928

⏱️  Overhead round 11 (wall-clock s): round 134.11 | broadcast 0.03 | prepare 0.00 | benign train 119.27 [0:30.3 1:10.9 2:9.7 3:33.8 4:34.6] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.14 | observe 0.00 | eval_global 6.93 | eval_local 7.61 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.06s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 11 Results:
  Clean Accuracy: 0.8880
  ΔClean vs prev: +0.0117
  ΔClean vs best: +0.0000
  Global Loss: 0.3845

============================================================
Round 12/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1753, effective_std_norm=0.3358, attack_norm=0.3785, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1753, effective_std_norm=0.3358, attack_norm=0.3787, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.225857
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.117, Std Dev: 0.063
    Client 0 (Benign): 0.083
    Client 1 (Benign): 0.082
    Client 2 (Benign): 0.030
    Client 3 (Benign): 0.080
    Client 4 (Benign): 0.125
    Client 5 (Attacker): 0.209
    Client 6 (Attacker): 0.209
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.332563, Std Dev: 0.044009
    Client 0 (Benign): 0.362111
    Client 1 (Benign): 0.303648
    Client 2 (Benign): 0.329280
    Client 3 (Benign): 0.389864
    Client 4 (Benign): 0.373323
    Client 5 (Attacker): 0.250645
    Client 6 (Attacker): 0.319071
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.401846 krum=0.697551 mkrum=KEEP tm_trim=0.6307 (lo 0.3160 / hi 0.3147) med_prov=0.1207 d_med=0.373368
    [shadow] C1 (B): norm=0.255967 krum=0.480427 mkrum=KEEP tm_trim=0.4883 (lo 0.2437 / hi 0.2446) med_prov=0.1776 d_med=0.264427
    [shadow] C2 (B): norm=0.262574 krum=0.504861 mkrum=KEEP tm_trim=0.5496 (lo 0.2749 / hi 0.2747) med_prov=0.1508 d_med=0.286003
    [shadow] C3 (B): norm=0.465750 krum=0.812527 mkrum=REJECT tm_trim=0.6889 (lo 0.3439 / hi 0.3450) med_prov=0.0993 d_med=0.430296
    [shadow] C4 (B): norm=0.452175 krum=0.761522 mkrum=REJECT tm_trim=0.6493 (lo 0.3248 / hi 0.3245) med_prov=0.1139 d_med=0.402296
    [shadow] C5 (A): norm=0.378515 krum=0.589675 mkrum=KEEP tm_trim=0.4964 (lo 0.2478 / hi 0.2485) med_prov=0.1686 d_med=0.299770
    [shadow] C6 (A): norm=0.378672 krum=0.590504 mkrum=KEEP tm_trim=0.4968 (lo 0.2489 / hi 0.2479) med_prov=0.1690 d_med=0.300074

⏱️  Overhead round 12 (wall-clock s): round 134.02 | broadcast 0.03 | prepare 0.00 | benign train 119.26 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.60 (bookkeeping) | unaccounted 0.01
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 12 Results:
  Clean Accuracy: 0.8857
  ΔClean vs prev: -0.0023
  ΔClean vs best: -0.0023
  Global Loss: 0.4083

============================================================
Round 13/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1752, effective_std_norm=0.3335, attack_norm=0.3763, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1752, effective_std_norm=0.3335, attack_norm=0.3766, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.225451
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.119, Std Dev: 0.063
    Client 0 (Benign): 0.100
    Client 1 (Benign): 0.080
    Client 2 (Benign): 0.036
    Client 3 (Benign): 0.076
    Client 4 (Benign): 0.121
    Client 5 (Attacker): 0.211
    Client 6 (Attacker): 0.212
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.330518, Std Dev: 0.042639
    Client 0 (Benign): 0.365007
    Client 1 (Benign): 0.303988
    Client 2 (Benign): 0.328568
    Client 3 (Benign): 0.378174
    Client 4 (Benign): 0.372148
    Client 5 (Attacker): 0.249071
    Client 6 (Attacker): 0.316672
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.415044 krum=0.705361 mkrum=KEEP tm_trim=0.6362 (lo 0.3183 / hi 0.3178) med_prov=0.1191 d_med=0.377817
    [shadow] C1 (B): norm=0.252355 krum=0.470612 mkrum=KEEP tm_trim=0.4921 (lo 0.2456 / hi 0.2465) med_prov=0.1747 d_med=0.264283
    [shadow] C2 (B): norm=0.262798 krum=0.494667 mkrum=KEEP tm_trim=0.5491 (lo 0.2750 / hi 0.2741) med_prov=0.1509 d_med=0.285935
    [shadow] C3 (B): norm=0.446875 krum=0.775833 mkrum=REJECT tm_trim=0.6738 (lo 0.3368 / hi 0.3370) med_prov=0.1045 d_med=0.414705
    [shadow] C4 (B): norm=0.452574 krum=0.765475 mkrum=REJECT tm_trim=0.6560 (lo 0.3282 / hi 0.3278) med_prov=0.1120 d_med=0.403869
    [shadow] C5 (A): norm=0.376348 krum=0.582773 mkrum=KEEP tm_trim=0.4957 (lo 0.2478 / hi 0.2479) med_prov=0.1697 d_med=0.297811
    [shadow] C6 (A): norm=0.376603 krum=0.582725 mkrum=KEEP tm_trim=0.4971 (lo 0.2483 / hi 0.2489) med_prov=0.1690 d_med=0.297607

⏱️  Overhead round 13 (wall-clock s): round 134.12 | broadcast 0.02 | prepare 0.00 | benign train 119.36 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.10 | observe 0.00 | eval_global 6.94 | eval_local 7.60 (bookkeeping) | unaccounted 0.01
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 13 Results:
  Clean Accuracy: 0.8897
  ΔClean vs prev: +0.0040
  ΔClean vs best: +0.0000
  Global Loss: 0.4086

============================================================
Round 14/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1704, effective_std_norm=0.3299, attack_norm=0.3713, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1704, effective_std_norm=0.3299, attack_norm=0.3714, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.218055
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.115, Std Dev: 0.060
    Client 0 (Benign): 0.086
    Client 1 (Benign): 0.084
    Client 2 (Benign): 0.045
    Client 3 (Benign): 0.071
    Client 4 (Benign): 0.108
    Client 5 (Attacker): 0.207
    Client 6 (Attacker): 0.206
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.326996, Std Dev: 0.041967
    Client 0 (Benign): 0.370018
    Client 1 (Benign): 0.302487
    Client 2 (Benign): 0.322298
    Client 3 (Benign): 0.369657
    Client 4 (Benign): 0.363964
    Client 5 (Attacker): 0.246342
    Client 6 (Attacker): 0.314205
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.419454 krum=0.721033 mkrum=KEEP tm_trim=0.6507 (lo 0.3255 / hi 0.3252) med_prov=0.1142 d_med=0.386631
    [shadow] C1 (B): norm=0.258927 krum=0.468625 mkrum=KEEP tm_trim=0.5039 (lo 0.2519 / hi 0.2520) med_prov=0.1690 d_med=0.263945
    [shadow] C2 (B): norm=0.264893 krum=0.486912 mkrum=KEEP tm_trim=0.5423 (lo 0.2716 / hi 0.2707) med_prov=0.1538 d_med=0.281174
    [shadow] C3 (B): norm=0.431572 krum=0.744032 mkrum=REJECT tm_trim=0.6667 (lo 0.3326 / hi 0.3341) med_prov=0.1072 d_med=0.403282
    [shadow] C4 (B): norm=0.435766 krum=0.734349 mkrum=REJECT tm_trim=0.6455 (lo 0.3234 / hi 0.3221) med_prov=0.1164 d_med=0.393902
    [shadow] C5 (A): norm=0.371317 krum=0.571793 mkrum=KEEP tm_trim=0.4954 (lo 0.2477 / hi 0.2476) med_prov=0.1696 d_med=0.294795
    [shadow] C6 (A): norm=0.371422 krum=0.572267 mkrum=KEEP tm_trim=0.4956 (lo 0.2473 / hi 0.2483) med_prov=0.1698 d_med=0.295063

⏱️  Overhead round 14 (wall-clock s): round 134.33 | broadcast 0.02 | prepare 0.00 | benign train 119.54 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.59 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.04s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.06s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 14 Results:
  Clean Accuracy: 0.8843
  ΔClean vs prev: -0.0053
  ΔClean vs best: -0.0053
  Global Loss: 0.4303

============================================================
Round 15/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1669, effective_std_norm=0.3249, attack_norm=0.3661, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1669, effective_std_norm=0.3249, attack_norm=0.3649, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.215146
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.111, Std Dev: 0.062
    Client 0 (Benign): 0.084
    Client 1 (Benign): 0.076
    Client 2 (Benign): 0.031
    Client 3 (Benign): 0.076
    Client 4 (Benign): 0.106
    Client 5 (Attacker): 0.203
    Client 6 (Attacker): 0.204
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.322174, Std Dev: 0.041028
    Client 0 (Benign): 0.364187
    Client 1 (Benign): 0.301335
    Client 2 (Benign): 0.318325
    Client 3 (Benign): 0.372824
    Client 4 (Benign): 0.346688
    Client 5 (Attacker): 0.243332
    Client 6 (Attacker): 0.308526
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C0 (B), C3 (B)
    [shadow] C0 (B): norm=0.415358 krum=0.705368 mkrum=REJECT tm_trim=0.6504 (lo 0.3255 / hi 0.3249) med_prov=0.1141 d_med=0.383252
    [shadow] C1 (B): norm=0.256037 krum=0.457026 mkrum=KEEP tm_trim=0.5061 (lo 0.2528 / hi 0.2533) med_prov=0.1685 d_med=0.262771
    [shadow] C2 (B): norm=0.254928 krum=0.472521 mkrum=KEEP tm_trim=0.5430 (lo 0.2721 / hi 0.2709) med_prov=0.1531 d_med=0.276886
    [shadow] C3 (B): norm=0.444135 krum=0.759763 mkrum=REJECT tm_trim=0.6784 (lo 0.3385 / hi 0.3400) med_prov=0.1034 d_med=0.410949
    [shadow] C4 (B): norm=0.408382 krum=0.671241 mkrum=KEEP tm_trim=0.6316 (lo 0.3156 / hi 0.3160) med_prov=0.1212 d_med=0.369583
    [shadow] C5 (A): norm=0.366062 krum=0.557505 mkrum=KEEP tm_trim=0.4960 (lo 0.2481 / hi 0.2479) med_prov=0.1694 d_med=0.291297
    [shadow] C6 (A): norm=0.364909 krum=0.555749 mkrum=KEEP tm_trim=0.4945 (lo 0.2474 / hi 0.2470) med_prov=0.1703 d_med=0.289765

⏱️  Overhead round 15 (wall-clock s): round 134.29 | broadcast 0.03 | prepare 0.00 | benign train 119.51 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.58 (bookkeeping) | unaccounted 0.05
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.04s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 15 Results:
  Clean Accuracy: 0.8863
  ΔClean vs prev: +0.0020
  ΔClean vs best: -0.0033
  Global Loss: 0.4544

============================================================
Round 16/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1675, effective_std_norm=0.3275, attack_norm=0.3679, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1675, effective_std_norm=0.3275, attack_norm=0.3678, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.215947
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.110, Std Dev: 0.061
    Client 0 (Benign): 0.089
    Client 1 (Benign): 0.071
    Client 2 (Benign): 0.037
    Client 3 (Benign): 0.068
    Client 4 (Benign): 0.100
    Client 5 (Attacker): 0.202
    Client 6 (Attacker): 0.203
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.324825, Std Dev: 0.040819
    Client 0 (Benign): 0.357892
    Client 1 (Benign): 0.306673
    Client 2 (Benign): 0.318146
    Client 3 (Benign): 0.370396
    Client 4 (Benign): 0.364279
    Client 5 (Attacker): 0.244924
    Client 6 (Attacker): 0.311463
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.407673 krum=0.693490 mkrum=KEEP tm_trim=0.6411 (lo 0.3208 / hi 0.3203) med_prov=0.1168 d_med=0.373419
    [shadow] C1 (B): norm=0.259473 krum=0.465912 mkrum=KEEP tm_trim=0.5080 (lo 0.2542 / hi 0.2538) med_prov=0.1675 d_med=0.267722
    [shadow] C2 (B): norm=0.257000 krum=0.475531 mkrum=KEEP tm_trim=0.5422 (lo 0.2716 / hi 0.2706) med_prov=0.1542 d_med=0.276689
    [shadow] C3 (B): norm=0.434200 krum=0.749464 mkrum=REJECT tm_trim=0.6699 (lo 0.3347 / hi 0.3353) med_prov=0.1062 d_med=0.405246
    [shadow] C4 (B): norm=0.434242 krum=0.727223 mkrum=REJECT tm_trim=0.6497 (lo 0.3250 / hi 0.3246) med_prov=0.1144 d_med=0.394942
    [shadow] C5 (A): norm=0.367943 krum=0.565122 mkrum=KEEP tm_trim=0.4951 (lo 0.2467 / hi 0.2484) med_prov=0.1707 d_med=0.292711
    [shadow] C6 (A): norm=0.367755 krum=0.564251 mkrum=KEEP tm_trim=0.4940 (lo 0.2470 / hi 0.2470) med_prov=0.1701 d_med=0.292226

⏱️  Overhead round 16 (wall-clock s): round 134.05 | broadcast 0.02 | prepare 0.00 | benign train 119.29 [0:30.3 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.09 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.56 (bookkeeping) | unaccounted 0.05
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.04s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 16 Results:
  Clean Accuracy: 0.8867
  ΔClean vs prev: +0.0003
  ΔClean vs best: -0.0030
  Global Loss: 0.4587

============================================================
Round 17/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1615, effective_std_norm=0.3177, attack_norm=0.3563, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1615, effective_std_norm=0.3177, attack_norm=0.3567, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.206341
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.110, Std Dev: 0.061
    Client 0 (Benign): 0.087
    Client 1 (Benign): 0.078
    Client 2 (Benign): 0.044
    Client 3 (Benign): 0.057
    Client 4 (Benign): 0.097
    Client 5 (Attacker): 0.201
    Client 6 (Attacker): 0.202
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.315132, Std Dev: 0.039218
    Client 0 (Benign): 0.350359
    Client 1 (Benign): 0.298398
    Client 2 (Benign): 0.309801
    Client 3 (Benign): 0.358941
    Client 4 (Benign): 0.348573
    Client 5 (Attacker): 0.237583
    Client 6 (Attacker): 0.302268
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.397826 krum=0.661174 mkrum=KEEP tm_trim=0.6393 (lo 0.3195 / hi 0.3198) med_prov=0.1177 d_med=0.366254
    [shadow] C1 (B): norm=0.260417 krum=0.448429 mkrum=KEEP tm_trim=0.5126 (lo 0.2562 / hi 0.2564) med_prov=0.1665 d_med=0.262346
    [shadow] C2 (B): norm=0.257371 krum=0.458296 mkrum=KEEP tm_trim=0.5418 (lo 0.2714 / hi 0.2704) med_prov=0.1540 d_med=0.270111
    [shadow] C3 (B): norm=0.415190 krum=0.703572 mkrum=REJECT tm_trim=0.6692 (lo 0.3343 / hi 0.3349) med_prov=0.1068 d_med=0.393450
    [shadow] C4 (B): norm=0.412825 krum=0.675297 mkrum=REJECT tm_trim=0.6478 (lo 0.3244 / hi 0.3234) med_prov=0.1148 d_med=0.376951
    [shadow] C5 (A): norm=0.356328 krum=0.534026 mkrum=KEEP tm_trim=0.4948 (lo 0.2472 / hi 0.2476) med_prov=0.1701 d_med=0.283950
    [shadow] C6 (A): norm=0.356744 krum=0.533784 mkrum=KEEP tm_trim=0.4945 (lo 0.2470 / hi 0.2475) med_prov=0.1701 d_med=0.283681

⏱️  Overhead round 17 (wall-clock s): round 133.96 | broadcast 0.03 | prepare 0.00 | benign train 119.19 [0:30.2 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.56 (bookkeeping) | unaccounted 0.05
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.04s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 17 Results:
  Clean Accuracy: 0.8890
  ΔClean vs prev: +0.0023
  ΔClean vs best: -0.0007
  Global Loss: 0.4553

============================================================
Round 18/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1611, effective_std_norm=0.3235, attack_norm=0.3611, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1611, effective_std_norm=0.3235, attack_norm=0.3615, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.208365
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.099, Std Dev: 0.063
    Client 0 (Benign): 0.091
    Client 1 (Benign): 0.069
    Client 2 (Benign): 0.015
    Client 3 (Benign): 0.055
    Client 4 (Benign): 0.079
    Client 5 (Attacker): 0.193
    Client 6 (Attacker): 0.193
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.321004, Std Dev: 0.039037
    Client 0 (Benign): 0.357581
    Client 1 (Benign): 0.305212
    Client 2 (Benign): 0.319872
    Client 3 (Benign): 0.359893
    Client 4 (Benign): 0.354650
    Client 5 (Attacker): 0.241856
    Client 6 (Attacker): 0.307965
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.413490 krum=0.690070 mkrum=KEEP tm_trim=0.6399 (lo 0.3197 / hi 0.3202) med_prov=0.1177 d_med=0.376595
    [shadow] C1 (B): norm=0.264283 krum=0.463644 mkrum=KEEP tm_trim=0.5185 (lo 0.2594 / hi 0.2591) med_prov=0.1633 d_med=0.267296
    [shadow] C2 (B): norm=0.256520 krum=0.477078 mkrum=KEEP tm_trim=0.5477 (lo 0.2743 / hi 0.2734) med_prov=0.1522 d_med=0.280221
    [shadow] C3 (B): norm=0.417636 krum=0.721956 mkrum=REJECT tm_trim=0.6611 (lo 0.3294 / hi 0.3317) med_prov=0.1097 d_med=0.393267
    [shadow] C4 (B): norm=0.414531 krum=0.700049 mkrum=REJECT tm_trim=0.6445 (lo 0.3224 / hi 0.3221) med_prov=0.1163 d_med=0.383322
    [shadow] C5 (A): norm=0.361064 krum=0.555461 mkrum=KEEP tm_trim=0.4940 (lo 0.2473 / hi 0.2468) med_prov=0.1704 d_med=0.288508
    [shadow] C6 (A): norm=0.361530 krum=0.556316 mkrum=KEEP tm_trim=0.4942 (lo 0.2475 / hi 0.2467) med_prov=0.1704 d_med=0.288940

⏱️  Overhead round 18 (wall-clock s): round 133.93 | broadcast 0.03 | prepare 0.00 | benign train 119.17 [0:30.2 1:10.9 2:9.7 3:33.7 4:34.6] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.58 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 18 Results:
  Clean Accuracy: 0.8877
  ΔClean vs prev: -0.0013
  ΔClean vs best: -0.0020
  Global Loss: 0.5095

============================================================
Round 19/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1527, effective_std_norm=0.3163, attack_norm=0.3509, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1527, effective_std_norm=0.3163, attack_norm=0.3505, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.198278
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.091, Std Dev: 0.062
    Client 0 (Benign): 0.073
    Client 1 (Benign): 0.060
    Client 2 (Benign): 0.022
    Client 3 (Benign): 0.038
    Client 4 (Benign): 0.072
    Client 5 (Attacker): 0.186
    Client 6 (Attacker): 0.185
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.313705, Std Dev: 0.038571
    Client 0 (Benign): 0.342271
    Client 1 (Benign): 0.295312
    Client 2 (Benign): 0.316149
    Client 3 (Benign): 0.354513
    Client 4 (Benign): 0.351035
    Client 5 (Attacker): 0.236103
    Client 6 (Attacker): 0.300549
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.385224 krum=0.633468 mkrum=KEEP tm_trim=0.6288 (lo 0.3141 / hi 0.3147) med_prov=0.1217 d_med=0.356651
    [shadow] C1 (B): norm=0.254463 krum=0.444126 mkrum=KEEP tm_trim=0.5083 (lo 0.2539 / hi 0.2544) med_prov=0.1677 d_med=0.259055
    [shadow] C2 (B): norm=0.263181 krum=0.463139 mkrum=KEEP tm_trim=0.5572 (lo 0.2796 / hi 0.2776) med_prov=0.1482 d_med=0.276868
    [shadow] C3 (B): norm=0.406360 krum=0.692688 mkrum=REJECT tm_trim=0.6677 (lo 0.3333 / hi 0.3344) med_prov=0.1066 d_med=0.388295
    [shadow] C4 (B): norm=0.411308 krum=0.686528 mkrum=REJECT tm_trim=0.6495 (lo 0.3254 / hi 0.3241) med_prov=0.1142 d_med=0.381284
    [shadow] C5 (A): norm=0.350914 krum=0.530821 mkrum=KEEP tm_trim=0.4942 (lo 0.2470 / hi 0.2472) med_prov=0.1709 d_med=0.282009
    [shadow] C6 (A): norm=0.350517 krum=0.529757 mkrum=KEEP tm_trim=0.4942 (lo 0.2467 / hi 0.2475) med_prov=0.1708 d_med=0.281945

⏱️  Overhead round 19 (wall-clock s): round 134.11 | broadcast 0.03 | prepare 0.00 | benign train 119.33 [0:30.3 1:10.9 2:9.7 3:33.8 4:34.6] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.57 (bookkeeping) | unaccounted 0.05
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.06s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 19 Results:
  Clean Accuracy: 0.8877
  ΔClean vs prev: +0.0000
  ΔClean vs best: -0.0020
  Global Loss: 0.5293

============================================================
Round 20/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1477, effective_std_norm=0.3123, attack_norm=0.3457, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1477, effective_std_norm=0.3123, attack_norm=0.3453, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.192209
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.084, Std Dev: 0.063
    Client 0 (Benign): 0.073
    Client 1 (Benign): 0.059
    Client 2 (Benign): 0.024
    Client 3 (Benign): 0.015
    Client 4 (Benign): 0.062
    Client 5 (Attacker): 0.179
    Client 6 (Attacker): 0.179
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.309700, Std Dev: 0.039143
    Client 0 (Benign): 0.348097
    Client 1 (Benign): 0.287332
    Client 2 (Benign): 0.307734
    Client 3 (Benign): 0.346286
    Client 4 (Benign): 0.347793
    Client 5 (Attacker): 0.233554
    Client 6 (Attacker): 0.297101
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.397636 krum=0.649927 mkrum=KEEP tm_trim=0.6455 (lo 0.3227 / hi 0.3228) med_prov=0.1147 d_med=0.365900
    [shadow] C1 (B): norm=0.246951 krum=0.424062 mkrum=KEEP tm_trim=0.5000 (lo 0.2504 / hi 0.2496) med_prov=0.1711 d_med=0.251803
    [shadow] C2 (B): norm=0.256751 krum=0.442205 mkrum=KEEP tm_trim=0.5495 (lo 0.2752 / hi 0.2743) med_prov=0.1515 d_med=0.268732
    [shadow] C3 (B): norm=0.386410 krum=0.656464 mkrum=REJECT tm_trim=0.6632 (lo 0.3311 / hi 0.3321) med_prov=0.1085 d_med=0.376377
    [shadow] C4 (B): norm=0.403084 krum=0.667747 mkrum=REJECT tm_trim=0.6501 (lo 0.3255 / hi 0.3246) med_prov=0.1146 d_med=0.376157
    [shadow] C5 (A): norm=0.345705 krum=0.515079 mkrum=KEEP tm_trim=0.4954 (lo 0.2471 / hi 0.2483) med_prov=0.1699 d_med=0.279282
    [shadow] C6 (A): norm=0.345303 krum=0.513904 mkrum=KEEP tm_trim=0.4963 (lo 0.2481 / hi 0.2482) med_prov=0.1698 d_med=0.278957

⏱️  Overhead round 20 (wall-clock s): round 133.94 | broadcast 0.02 | prepare 0.00 | benign train 119.17 [0:30.2 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.58 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 20 Results:
  Clean Accuracy: 0.8897
  ΔClean vs prev: +0.0020
  ΔClean vs best: +0.0000
  Global Loss: 0.5415

============================================================
Round 21/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1496, effective_std_norm=0.3082, attack_norm=0.3422, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1496, effective_std_norm=0.3082, attack_norm=0.3422, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.193143
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.094, Std Dev: 0.061
    Client 0 (Benign): 0.065
    Client 1 (Benign): 0.068
    Client 2 (Benign): 0.034
    Client 3 (Benign): 0.043
    Client 4 (Benign): 0.071
    Client 5 (Attacker): 0.188
    Client 6 (Attacker): 0.188
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.305761, Std Dev: 0.037231
    Client 0 (Benign): 0.345093
    Client 1 (Benign): 0.290498
    Client 2 (Benign): 0.306115
    Client 3 (Benign): 0.334632
    Client 4 (Benign): 0.340805
    Client 5 (Attacker): 0.230292
    Client 6 (Attacker): 0.292890
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C0 (B), C4 (B)
    [shadow] C0 (B): norm=0.391218 krum=0.642786 mkrum=REJECT tm_trim=0.6471 (lo 0.3240 / hi 0.3231) med_prov=0.1151 d_med=0.365192
    [shadow] C1 (B): norm=0.251843 krum=0.416814 mkrum=KEEP tm_trim=0.5115 (lo 0.2562 / hi 0.2553) med_prov=0.1655 d_med=0.253966
    [shadow] C2 (B): norm=0.256304 krum=0.430429 mkrum=KEEP tm_trim=0.5527 (lo 0.2766 / hi 0.2761) med_prov=0.1499 d_med=0.267089
    [shadow] C3 (B): norm=0.381620 krum=0.628994 mkrum=KEEP tm_trim=0.6503 (lo 0.3250 / hi 0.3253) med_prov=0.1135 d_med=0.364105
    [shadow] C4 (B): norm=0.398544 krum=0.648642 mkrum=REJECT tm_trim=0.6506 (lo 0.3246 / hi 0.3260) med_prov=0.1138 d_med=0.369652
    [shadow] C5 (A): norm=0.342199 krum=0.503470 mkrum=KEEP tm_trim=0.4934 (lo 0.2461 / hi 0.2472) med_prov=0.1712 d_med=0.274747
    [shadow] C6 (A): norm=0.342213 krum=0.503507 mkrum=KEEP tm_trim=0.4944 (lo 0.2475 / hi 0.2469) med_prov=0.1711 d_med=0.274854

⏱️  Overhead round 21 (wall-clock s): round 133.98 | broadcast 0.03 | prepare 0.00 | benign train 119.19 [0:30.2 1:10.9 2:9.7 3:33.7 4:34.6] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.12 | observe 0.00 | eval_global 6.93 | eval_local 7.57 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.06s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 21 Results:
  Clean Accuracy: 0.8837
  ΔClean vs prev: -0.0060
  ΔClean vs best: -0.0060
  Global Loss: 0.5862

============================================================
Round 22/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1439, effective_std_norm=0.3026, attack_norm=0.3352, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1439, effective_std_norm=0.3026, attack_norm=0.3353, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.186525
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.087, Std Dev: 0.062
    Client 0 (Benign): 0.060
    Client 1 (Benign): 0.053
    Client 2 (Benign): 0.038
    Client 3 (Benign): 0.022
    Client 4 (Benign): 0.074
    Client 5 (Attacker): 0.182
    Client 6 (Attacker): 0.182
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.300159, Std Dev: 0.036866
    Client 0 (Benign): 0.330489
    Client 1 (Benign): 0.285262
    Client 2 (Benign): 0.297019
    Client 3 (Benign): 0.339889
    Client 4 (Benign): 0.334441
    Client 5 (Attacker): 0.226313
    Client 6 (Attacker): 0.287700
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.367298 krum=0.587891 mkrum=KEEP tm_trim=0.6347 (lo 0.3177 / hi 0.3170) med_prov=0.1195 d_med=0.343748
    [shadow] C1 (B): norm=0.246195 krum=0.410888 mkrum=KEEP tm_trim=0.5151 (lo 0.2572 / hi 0.2579) med_prov=0.1649 d_med=0.251362
    [shadow] C2 (B): norm=0.253880 krum=0.420933 mkrum=KEEP tm_trim=0.5501 (lo 0.2750 / hi 0.2751) med_prov=0.1509 d_med=0.260683
    [shadow] C3 (B): norm=0.383407 krum=0.638166 mkrum=REJECT tm_trim=0.6658 (lo 0.3327 / hi 0.3331) med_prov=0.1077 d_med=0.371740
    [shadow] C4 (B): norm=0.392762 krum=0.623506 mkrum=REJECT tm_trim=0.6466 (lo 0.3233 / hi 0.3233) med_prov=0.1156 d_med=0.362619
    [shadow] C5 (A): norm=0.335160 krum=0.485569 mkrum=KEEP tm_trim=0.4939 (lo 0.2470 / hi 0.2470) med_prov=0.1703 d_med=0.270338
    [shadow] C6 (A): norm=0.335268 krum=0.485980 mkrum=KEEP tm_trim=0.4937 (lo 0.2472 / hi 0.2465) med_prov=0.1711 d_med=0.270187

⏱️  Overhead round 22 (wall-clock s): round 134.26 | broadcast 0.02 | prepare 0.00 | benign train 119.52 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.12 | observe 0.00 | eval_global 6.93 | eval_local 7.54 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.04s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 22 Results:
  Clean Accuracy: 0.8880
  ΔClean vs prev: +0.0043
  ΔClean vs best: -0.0017
  Global Loss: 0.5973

============================================================
Round 23/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1407, effective_std_norm=0.3001, attack_norm=0.3313, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1407, effective_std_norm=0.3001, attack_norm=0.3314, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.182953
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.082, Std Dev: 0.062
    Client 0 (Benign): 0.052
    Client 1 (Benign): 0.050
    Client 2 (Benign): 0.029
    Client 3 (Benign): 0.023
    Client 4 (Benign): 0.067
    Client 5 (Attacker): 0.178
    Client 6 (Attacker): 0.177
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.297779, Std Dev: 0.036175
    Client 0 (Benign): 0.333355
    Client 1 (Benign): 0.281319
    Client 2 (Benign): 0.302185
    Client 3 (Benign): 0.335887
    Client 4 (Benign): 0.322029
    Client 5 (Attacker): 0.224207
    Client 6 (Attacker): 0.285471
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C0 (B), C3 (B)
    [shadow] C0 (B): norm=0.374875 krum=0.605629 mkrum=REJECT tm_trim=0.6422 (lo 0.3219 / hi 0.3204) med_prov=0.1161 d_med=0.352421
    [shadow] C1 (B): norm=0.242451 krum=0.403954 mkrum=KEEP tm_trim=0.5038 (lo 0.2519 / hi 0.2518) med_prov=0.1694 d_med=0.248408
    [shadow] C2 (B): norm=0.258807 krum=0.421733 mkrum=KEEP tm_trim=0.5644 (lo 0.2826 / hi 0.2818) med_prov=0.1448 d_med=0.264967
    [shadow] C3 (B): norm=0.379146 krum=0.618082 mkrum=REJECT tm_trim=0.6676 (lo 0.3332 / hi 0.3343) med_prov=0.1079 d_med=0.366796
    [shadow] C4 (B): norm=0.373286 krum=0.592201 mkrum=KEEP tm_trim=0.6342 (lo 0.3166 / hi 0.3176) med_prov=0.1203 d_med=0.346810
    [shadow] C5 (A): norm=0.331307 krum=0.480484 mkrum=KEEP tm_trim=0.4933 (lo 0.2463 / hi 0.2470) med_prov=0.1707 d_med=0.267537
    [shadow] C6 (A): norm=0.331404 krum=0.480769 mkrum=KEEP tm_trim=0.4945 (lo 0.2475 / hi 0.2471) med_prov=0.1708 d_med=0.267880

⏱️  Overhead round 23 (wall-clock s): round 134.17 | broadcast 0.02 | prepare 0.00 | benign train 119.43 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.56 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 23 Results:
  Clean Accuracy: 0.8923
  ΔClean vs prev: +0.0043
  ΔClean vs best: +0.0000
  Global Loss: 0.6090

============================================================
Round 24/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1377, effective_std_norm=0.2944, attack_norm=0.3251, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1377, effective_std_norm=0.2944, attack_norm=0.3248, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.177525
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.083, Std Dev: 0.062
    Client 0 (Benign): 0.045
    Client 1 (Benign): 0.063
    Client 2 (Benign): 0.036
    Client 3 (Benign): 0.018
    Client 4 (Benign): 0.061
    Client 5 (Attacker): 0.178
    Client 6 (Attacker): 0.178
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.292427, Std Dev: 0.034030
    Client 0 (Benign): 0.320917
    Client 1 (Benign): 0.284657
    Client 2 (Benign): 0.294759
    Client 3 (Benign): 0.322141
    Client 4 (Benign): 0.324028
    Client 5 (Attacker): 0.220342
    Client 6 (Attacker): 0.280145
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.355073 krum=0.570869 mkrum=KEEP tm_trim=0.6346 (lo 0.3168 / hi 0.3179) med_prov=0.1192 d_med=0.337463
    [shadow] C1 (B): norm=0.254940 krum=0.398799 mkrum=KEEP tm_trim=0.5257 (lo 0.2639 / hi 0.2618) med_prov=0.1601 d_med=0.251811
    [shadow] C2 (B): norm=0.254706 krum=0.406953 mkrum=KEEP tm_trim=0.5563 (lo 0.2784 / hi 0.2779) med_prov=0.1488 d_med=0.259061
    [shadow] C3 (B): norm=0.359799 krum=0.587051 mkrum=REJECT tm_trim=0.6541 (lo 0.3270 / hi 0.3272) med_prov=0.1121 d_med=0.351315
    [shadow] C4 (B): norm=0.377909 krum=0.598472 mkrum=REJECT tm_trim=0.6478 (lo 0.3234 / hi 0.3244) med_prov=0.1153 d_med=0.352710
    [shadow] C5 (A): norm=0.325110 krum=0.465739 mkrum=KEEP tm_trim=0.4906 (lo 0.2450 / hi 0.2456) med_prov=0.1723 d_med=0.262736
    [shadow] C6 (A): norm=0.324836 krum=0.465608 mkrum=KEEP tm_trim=0.4908 (lo 0.2456 / hi 0.2452) med_prov=0.1722 d_med=0.262360

⏱️  Overhead round 24 (wall-clock s): round 134.06 | broadcast 0.03 | prepare 0.00 | benign train 119.28 [0:30.3 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.56 (bookkeeping) | unaccounted 0.05
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 24 Results:
  Clean Accuracy: 0.8850
  ΔClean vs prev: -0.0073
  ΔClean vs best: -0.0073
  Global Loss: 0.6439

============================================================
Round 25/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1394, effective_std_norm=0.2903, attack_norm=0.3220, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1394, effective_std_norm=0.2903, attack_norm=0.3222, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.178011
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.091, Std Dev: 0.062
    Client 0 (Benign): 0.070
    Client 1 (Benign): 0.065
    Client 2 (Benign): 0.031
    Client 3 (Benign): 0.035
    Client 4 (Benign): 0.061
    Client 5 (Attacker): 0.186
    Client 6 (Attacker): 0.186
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.288169, Std Dev: 0.033040
    Client 0 (Benign): 0.315972
    Client 1 (Benign): 0.282292
    Client 2 (Benign): 0.294086
    Client 3 (Benign): 0.315312
    Client 4 (Benign): 0.316733
    Client 5 (Attacker): 0.216762
    Client 6 (Attacker): 0.276028
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.356616 krum=0.552439 mkrum=KEEP tm_trim=0.6320 (lo 0.3162 / hi 0.3158) med_prov=0.1204 d_med=0.331059
    [shadow] C1 (B): norm=0.256621 krum=0.406914 mkrum=KEEP tm_trim=0.5357 (lo 0.2679 / hi 0.2678) med_prov=0.1570 d_med=0.252977
    [shadow] C2 (B): norm=0.255799 krum=0.416518 mkrum=KEEP tm_trim=0.5638 (lo 0.2828 / hi 0.2810) med_prov=0.1445 d_med=0.262987
    [shadow] C3 (B): norm=0.356032 krum=0.562206 mkrum=REJECT tm_trim=0.6474 (lo 0.3230 / hi 0.3243) med_prov=0.1152 d_med=0.343708
    [shadow] C4 (B): norm=0.364991 krum=0.565214 mkrum=REJECT tm_trim=0.6404 (lo 0.3200 / hi 0.3204) med_prov=0.1181 d_med=0.343030
    [shadow] C5 (A): norm=0.321954 krum=0.456928 mkrum=KEEP tm_trim=0.4899 (lo 0.2448 / hi 0.2451) med_prov=0.1732 d_med=0.258506
    [shadow] C6 (A): norm=0.322209 krum=0.457541 mkrum=KEEP tm_trim=0.4909 (lo 0.2453 / hi 0.2456) med_prov=0.1715 d_med=0.258770

⏱️  Overhead round 25 (wall-clock s): round 134.17 | broadcast 0.03 | prepare 0.00 | benign train 119.46 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.53 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 25 Results:
  Clean Accuracy: 0.8957
  ΔClean vs prev: +0.0107
  ΔClean vs best: +0.0000
  Global Loss: 0.5967

============================================================
Round 26/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1391, effective_std_norm=0.2928, attack_norm=0.3240, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1391, effective_std_norm=0.2928, attack_norm=0.3244, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.178653
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.088, Std Dev: 0.061
    Client 0 (Benign): 0.058
    Client 1 (Benign): 0.066
    Client 2 (Benign): 0.033
    Client 3 (Benign): 0.028
    Client 4 (Benign): 0.064
    Client 5 (Attacker): 0.182
    Client 6 (Attacker): 0.183
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.290741, Std Dev: 0.034046
    Client 0 (Benign): 0.321936
    Client 1 (Benign): 0.281876
    Client 2 (Benign): 0.295135
    Client 3 (Benign): 0.326829
    Client 4 (Benign): 0.311727
    Client 5 (Attacker): 0.218935
    Client 6 (Attacker): 0.278746
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.356116 krum=0.560362 mkrum=KEEP tm_trim=0.6319 (lo 0.3161 / hi 0.3158) med_prov=0.1212 d_med=0.334894
    [shadow] C1 (B): norm=0.253615 krum=0.400993 mkrum=KEEP tm_trim=0.5267 (lo 0.2637 / hi 0.2630) med_prov=0.1596 d_med=0.251072
    [shadow] C2 (B): norm=0.254498 krum=0.411590 mkrum=KEEP tm_trim=0.5632 (lo 0.2821 / hi 0.2811) med_prov=0.1462 d_med=0.261009
    [shadow] C3 (B): norm=0.372433 krum=0.599298 mkrum=REJECT tm_trim=0.6685 (lo 0.3335 / hi 0.3350) med_prov=0.1065 d_med=0.359027
    [shadow] C4 (B): norm=0.361658 krum=0.567319 mkrum=REJECT tm_trim=0.6286 (lo 0.3140 / hi 0.3145) med_prov=0.1220 d_med=0.338521
    [shadow] C5 (A): norm=0.323969 krum=0.461753 mkrum=KEEP tm_trim=0.4906 (lo 0.2447 / hi 0.2459) med_prov=0.1723 d_med=0.260776
    [shadow] C6 (A): norm=0.324369 krum=0.462011 mkrum=KEEP tm_trim=0.4905 (lo 0.2458 / hi 0.2447) med_prov=0.1722 d_med=0.261007

⏱️  Overhead round 26 (wall-clock s): round 134.06 | broadcast 0.03 | prepare 0.00 | benign train 119.30 [0:30.3 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.10 | observe 0.00 | eval_global 6.93 | eval_local 7.58 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 26 Results:
  Clean Accuracy: 0.8937
  ΔClean vs prev: -0.0020
  ΔClean vs best: -0.0020
  Global Loss: 0.6568

============================================================
Round 27/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1406, effective_std_norm=0.2921, attack_norm=0.3242, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1406, effective_std_norm=0.2921, attack_norm=0.3242, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.181401
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.091, Std Dev: 0.061
    Client 0 (Benign): 0.066
    Client 1 (Benign): 0.052
    Client 2 (Benign): 0.041
    Client 3 (Benign): 0.033
    Client 4 (Benign): 0.076
    Client 5 (Attacker): 0.185
    Client 6 (Attacker): 0.185
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.289984, Std Dev: 0.034777
    Client 0 (Benign): 0.312058
    Client 1 (Benign): 0.278045
    Client 2 (Benign): 0.295483
    Client 3 (Benign): 0.335030
    Client 4 (Benign): 0.312720
    Client 5 (Attacker): 0.218437
    Client 6 (Attacker): 0.278116
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.346779 krum=0.536999 mkrum=KEEP tm_trim=0.6237 (lo 0.3117 / hi 0.3120) med_prov=0.1230 d_med=0.324700
    [shadow] C1 (B): norm=0.240095 krum=0.391283 mkrum=KEEP tm_trim=0.5145 (lo 0.2569 / hi 0.2577) med_prov=0.1656 d_med=0.246586
    [shadow] C2 (B): norm=0.256115 krum=0.406591 mkrum=KEEP tm_trim=0.5627 (lo 0.2818 / hi 0.2809) med_prov=0.1454 d_med=0.260146
    [shadow] C3 (B): norm=0.386601 krum=0.620189 mkrum=REJECT tm_trim=0.6846 (lo 0.3423 / hi 0.3423) med_prov=0.1009 d_med=0.370759
    [shadow] C4 (B): norm=0.364005 krum=0.558895 mkrum=REJECT tm_trim=0.6336 (lo 0.3163 / hi 0.3173) med_prov=0.1201 d_med=0.336639
    [shadow] C5 (A): norm=0.324154 krum=0.458560 mkrum=KEEP tm_trim=0.4905 (lo 0.2458 / hi 0.2447) med_prov=0.1729 d_med=0.260324
    [shadow] C6 (A): norm=0.324190 krum=0.458254 mkrum=KEEP tm_trim=0.4905 (lo 0.2452 / hi 0.2452) med_prov=0.1721 d_med=0.260460

⏱️  Overhead round 27 (wall-clock s): round 133.96 | broadcast 0.03 | prepare 0.00 | benign train 119.18 [0:30.2 1:10.9 2:9.7 3:33.7 4:34.6] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.12 | observe 0.00 | eval_global 6.93 | eval_local 7.56 (bookkeeping) | unaccounted 0.06
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.04s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.04s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 27 Results:
  Clean Accuracy: 0.8937
  ΔClean vs prev: +0.0000
  ΔClean vs best: -0.0020
  Global Loss: 0.6788

============================================================
Round 28/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1354, effective_std_norm=0.2845, attack_norm=0.3150, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1354, effective_std_norm=0.2845, attack_norm=0.3149, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.172298
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.089, Std Dev: 0.063
    Client 0 (Benign): 0.064
    Client 1 (Benign): 0.074
    Client 2 (Benign): 0.037
    Client 3 (Benign): 0.010
    Client 4 (Benign): 0.069
    Client 5 (Attacker): 0.183
    Client 6 (Attacker): 0.184
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.282406, Std Dev: 0.032920
    Client 0 (Benign): 0.309639
    Client 1 (Benign): 0.273015
    Client 2 (Benign): 0.288276
    Client 3 (Benign): 0.316144
    Client 4 (Benign): 0.306714
    Client 5 (Attacker): 0.212801
    Client 6 (Attacker): 0.270253
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.347518 krum=0.529597 mkrum=KEEP tm_trim=0.6355 (lo 0.3169 / hi 0.3186) med_prov=0.1188 d_med=0.325278
    [shadow] C1 (B): norm=0.250601 krum=0.382130 mkrum=KEEP tm_trim=0.5219 (lo 0.2608 / hi 0.2611) med_prov=0.1628 d_med=0.244325
    [shadow] C2 (B): norm=0.252282 krum=0.394618 mkrum=KEEP tm_trim=0.5616 (lo 0.2817 / hi 0.2799) med_prov=0.1456 d_med=0.256544
    [shadow] C3 (B): norm=0.349818 krum=0.552226 mkrum=REJECT tm_trim=0.6678 (lo 0.3337 / hi 0.3341) med_prov=0.1069 d_med=0.344917
    [shadow] C4 (B): norm=0.356030 krum=0.540261 mkrum=REJECT tm_trim=0.6324 (lo 0.3161 / hi 0.3163) med_prov=0.1208 d_med=0.331474
    [shadow] C5 (A): norm=0.315004 krum=0.436841 mkrum=KEEP tm_trim=0.4908 (lo 0.2454 / hi 0.2453) med_prov=0.1721 d_med=0.253482
    [shadow] C6 (A): norm=0.314917 krum=0.436706 mkrum=KEEP tm_trim=0.4899 (lo 0.2453 / hi 0.2446) med_prov=0.1730 d_med=0.253178

⏱️  Overhead round 28 (wall-clock s): round 134.01 | broadcast 0.02 | prepare 0.00 | benign train 119.20 [0:30.2 1:10.9 2:9.7 3:33.7 4:34.6] | attack 0.08 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.60 (bookkeeping) | unaccounted 0.05
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 28 Results:
  Clean Accuracy: 0.8927
  ΔClean vs prev: -0.0010
  ΔClean vs best: -0.0030
  Global Loss: 0.6870

============================================================
Round 29/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1332, effective_std_norm=0.2841, attack_norm=0.3136, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1332, effective_std_norm=0.2841, attack_norm=0.3137, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.171184
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.083, Std Dev: 0.062
    Client 0 (Benign): 0.052
    Client 1 (Benign): 0.050
    Client 2 (Benign): 0.039
    Client 3 (Benign): 0.021
    Client 4 (Benign): 0.064
    Client 5 (Attacker): 0.179
    Client 6 (Attacker): 0.180
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.282022, Std Dev: 0.032601
    Client 0 (Benign): 0.307600
    Client 1 (Benign): 0.273171
    Client 2 (Benign): 0.291005
    Client 3 (Benign): 0.314124
    Client 4 (Benign): 0.306085
    Client 5 (Attacker): 0.212230
    Client 6 (Attacker): 0.269937
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.341681 krum=0.523676 mkrum=KEEP tm_trim=0.6325 (lo 0.3157 / hi 0.3168) med_prov=0.1203 d_med=0.322522
    [shadow] C1 (B): norm=0.242147 krum=0.383575 mkrum=KEEP tm_trim=0.5226 (lo 0.2617 / hi 0.2608) med_prov=0.1616 d_med=0.245108
    [shadow] C2 (B): norm=0.258822 krum=0.398528 mkrum=KEEP tm_trim=0.5731 (lo 0.2868 / hi 0.2863) med_prov=0.1417 d_med=0.259210
    [shadow] C3 (B): norm=0.353397 krum=0.555200 mkrum=REJECT tm_trim=0.6618 (lo 0.3306 / hi 0.3312) med_prov=0.1089 d_med=0.343907
    [shadow] C4 (B): norm=0.353675 krum=0.536088 mkrum=REJECT tm_trim=0.6316 (lo 0.3160 / hi 0.3156) med_prov=0.1217 d_med=0.330534
    [shadow] C5 (A): norm=0.313610 krum=0.436966 mkrum=KEEP tm_trim=0.4898 (lo 0.2445 / hi 0.2454) med_prov=0.1725 d_med=0.252680
    [shadow] C6 (A): norm=0.313746 krum=0.436981 mkrum=KEEP tm_trim=0.4886 (lo 0.2447 / hi 0.2439) med_prov=0.1733 d_med=0.252560

⏱️  Overhead round 29 (wall-clock s): round 134.01 | broadcast 0.02 | prepare 0.00 | benign train 119.23 [0:30.3 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.60 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 29 Results:
  Clean Accuracy: 0.9000
  ΔClean vs prev: +0.0073
  ΔClean vs best: +0.0000
  Global Loss: 0.6371

============================================================
Round 30/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1356, effective_std_norm=0.2879, attack_norm=0.3179, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1356, effective_std_norm=0.2879, attack_norm=0.3183, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.174723
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.085, Std Dev: 0.061
    Client 0 (Benign): 0.037
    Client 1 (Benign): 0.067
    Client 2 (Benign): 0.032
    Client 3 (Benign): 0.034
    Client 4 (Benign): 0.063
    Client 5 (Attacker): 0.180
    Client 6 (Attacker): 0.180
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.285577, Std Dev: 0.034834
    Client 0 (Benign): 0.312785
    Client 1 (Benign): 0.273274
    Client 2 (Benign): 0.286593
    Client 3 (Benign): 0.307209
    Client 4 (Benign): 0.330422
    Client 5 (Attacker): 0.214990
    Client 6 (Attacker): 0.273768
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C0 (B), C4 (B)
    [shadow] C0 (B): norm=0.340081 krum=0.535652 mkrum=REJECT tm_trim=0.6324 (lo 0.3158 / hi 0.3166) med_prov=0.1198 d_med=0.327589
    [shadow] C1 (B): norm=0.246074 krum=0.381499 mkrum=KEEP tm_trim=0.5152 (lo 0.2581 / hi 0.2572) med_prov=0.1651 d_med=0.243055
    [shadow] C2 (B): norm=0.247107 krum=0.391978 mkrum=KEEP tm_trim=0.5532 (lo 0.2768 / hi 0.2764) med_prov=0.1487 d_med=0.254020
    [shadow] C3 (B): norm=0.342694 krum=0.527443 mkrum=KEEP tm_trim=0.6521 (lo 0.3266 / hi 0.3255) med_prov=0.1122 d_med=0.329945
    [shadow] C4 (B): norm=0.389502 krum=0.604302 mkrum=REJECT tm_trim=0.6682 (lo 0.3343 / hi 0.3340) med_prov=0.1079 d_med=0.362161
    [shadow] C5 (A): norm=0.317929 krum=0.442644 mkrum=KEEP tm_trim=0.4892 (lo 0.2442 / hi 0.2450) med_prov=0.1729 d_med=0.256085
    [shadow] C6 (A): norm=0.318264 krum=0.443317 mkrum=KEEP tm_trim=0.4897 (lo 0.2444 / hi 0.2453) med_prov=0.1735 d_med=0.256524

⏱️  Overhead round 30 (wall-clock s): round 133.93 | broadcast 0.03 | prepare 0.00 | benign train 119.18 [0:30.2 1:10.9 2:9.7 3:33.7 4:34.6] | attack 0.08 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.56 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 30 Results:
  Clean Accuracy: 0.8967
  ΔClean vs prev: -0.0033
  ΔClean vs best: -0.0033
  Global Loss: 0.6962

============================================================
Round 31/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1296, effective_std_norm=0.2824, attack_norm=0.3111, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1296, effective_std_norm=0.2824, attack_norm=0.3104, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.167175
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.076, Std Dev: 0.063
    Client 0 (Benign): 0.059
    Client 1 (Benign): 0.052
    Client 2 (Benign): 0.023
    Client 3 (Benign): 0.010
    Client 4 (Benign): 0.041
    Client 5 (Attacker): 0.173
    Client 6 (Attacker): 0.172
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.280800, Std Dev: 0.031371
    Client 0 (Benign): 0.303933
    Client 1 (Benign): 0.274648
    Client 2 (Benign): 0.298217
    Client 3 (Benign): 0.306234
    Client 4 (Benign): 0.301925
    Client 5 (Attacker): 0.211666
    Client 6 (Attacker): 0.268975
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.341054 krum=0.518243 mkrum=KEEP tm_trim=0.6256 (lo 0.3129 / hi 0.3127) med_prov=0.1222 d_med=0.319604
    [shadow] C1 (B): norm=0.246323 krum=0.382299 mkrum=KEEP tm_trim=0.5211 (lo 0.2602 / hi 0.2609) med_prov=0.1621 d_med=0.246188
    [shadow] C2 (B): norm=0.263031 krum=0.402938 mkrum=KEEP tm_trim=0.5840 (lo 0.2920 / hi 0.2920) med_prov=0.1372 d_med=0.265653
    [shadow] C3 (B): norm=0.344196 krum=0.542272 mkrum=REJECT tm_trim=0.6678 (lo 0.3336 / hi 0.3342) med_prov=0.1066 d_med=0.337063
    [shadow] C4 (B): norm=0.343597 krum=0.533748 mkrum=REJECT tm_trim=0.6301 (lo 0.3154 / hi 0.3147) med_prov=0.1225 d_med=0.327970
    [shadow] C5 (A): norm=0.311115 krum=0.437439 mkrum=KEEP tm_trim=0.4859 (lo 0.2430 / hi 0.2429) med_prov=0.1747 d_med=0.251219
    [shadow] C6 (A): norm=0.310370 krum=0.437148 mkrum=KEEP tm_trim=0.4855 (lo 0.2429 / hi 0.2426) med_prov=0.1748 d_med=0.250936

⏱️  Overhead round 31 (wall-clock s): round 133.93 | broadcast 0.03 | prepare 0.00 | benign train 119.15 [0:30.2 1:10.9 2:9.7 3:33.7 4:34.6] | attack 0.08 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.58 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 31 Results:
  Clean Accuracy: 0.8960
  ΔClean vs prev: -0.0007
  ΔClean vs best: -0.0040
  Global Loss: 0.7274

============================================================
Round 32/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1341, effective_std_norm=0.2843, attack_norm=0.3145, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1341, effective_std_norm=0.2843, attack_norm=0.3147, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.172909
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.085, Std Dev: 0.061
    Client 0 (Benign): 0.055
    Client 1 (Benign): 0.060
    Client 2 (Benign): 0.039
    Client 3 (Benign): 0.023
    Client 4 (Benign): 0.060
    Client 5 (Attacker): 0.180
    Client 6 (Attacker): 0.181
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.282229, Std Dev: 0.033930
    Client 0 (Benign): 0.305260
    Client 1 (Benign): 0.270836
    Client 2 (Benign): 0.285040
    Client 3 (Benign): 0.306192
    Client 4 (Benign): 0.325071
    Client 5 (Attacker): 0.212623
    Client 6 (Attacker): 0.270581
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.336796 krum=0.512601 mkrum=KEEP tm_trim=0.6325 (lo 0.3159 / hi 0.3166) med_prov=0.1191 d_med=0.317864
    [shadow] C1 (B): norm=0.239325 krum=0.371130 mkrum=KEEP tm_trim=0.5180 (lo 0.2592 / hi 0.2588) med_prov=0.1650 d_med=0.240488
    [shadow] C2 (B): norm=0.248605 krum=0.382501 mkrum=KEEP tm_trim=0.5560 (lo 0.2785 / hi 0.2775) med_prov=0.1475 d_med=0.252081
    [shadow] C3 (B): norm=0.340608 krum=0.531230 mkrum=REJECT tm_trim=0.6523 (lo 0.3262 / hi 0.3261) med_prov=0.1124 d_med=0.331706
    [shadow] C4 (B): norm=0.381532 krum=0.584693 mkrum=REJECT tm_trim=0.6634 (lo 0.3316 / hi 0.3319) med_prov=0.1099 d_med=0.356429
    [shadow] C5 (A): norm=0.314512 krum=0.433342 mkrum=KEEP tm_trim=0.4891 (lo 0.2445 / hi 0.2446) med_prov=0.1729 d_med=0.253256
    [shadow] C6 (A): norm=0.314746 krum=0.433477 mkrum=KEEP tm_trim=0.4887 (lo 0.2442 / hi 0.2445) med_prov=0.1733 d_med=0.253351

⏱️  Overhead round 32 (wall-clock s): round 133.99 | broadcast 0.03 | prepare 0.00 | benign train 119.23 [0:30.3 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.10 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.56 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.07s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 32 Results:
  Clean Accuracy: 0.8980
  ΔClean vs prev: +0.0020
  ΔClean vs best: -0.0020
  Global Loss: 0.7083

============================================================
Round 33/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1355, effective_std_norm=0.2872, attack_norm=0.3174, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1355, effective_std_norm=0.2872, attack_norm=0.3178, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.173943
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.085, Std Dev: 0.063
    Client 0 (Benign): 0.060
    Client 1 (Benign): 0.059
    Client 2 (Benign): 0.047
    Client 3 (Benign): 0.007
    Client 4 (Benign): 0.063
    Client 5 (Attacker): 0.180
    Client 6 (Attacker): 0.180
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.284975, Std Dev: 0.034846
    Client 0 (Benign): 0.311618
    Client 1 (Benign): 0.274775
    Client 2 (Benign): 0.285830
    Client 3 (Benign): 0.301599
    Client 4 (Benign): 0.333131
    Client 5 (Attacker): 0.214601
    Client 6 (Attacker): 0.273270
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C0 (B), C4 (B)
    [shadow] C0 (B): norm=0.347589 krum=0.533799 mkrum=REJECT tm_trim=0.6369 (lo 0.3186 / hi 0.3183) med_prov=0.1180 d_med=0.326159
    [shadow] C1 (B): norm=0.243418 krum=0.378498 mkrum=KEEP tm_trim=0.5176 (lo 0.2586 / hi 0.2590) med_prov=0.1645 d_med=0.244233
    [shadow] C2 (B): norm=0.251460 krum=0.387272 mkrum=KEEP tm_trim=0.5579 (lo 0.2796 / hi 0.2783) med_prov=0.1468 d_med=0.251868
    [shadow] C3 (B): norm=0.325913 krum=0.521257 mkrum=KEEP tm_trim=0.6416 (lo 0.3203 / hi 0.3212) med_prov=0.1165 d_med=0.324742
    [shadow] C4 (B): norm=0.393288 krum=0.610856 mkrum=REJECT tm_trim=0.6686 (lo 0.3343 / hi 0.3343) med_prov=0.1081 d_med=0.365906
    [shadow] C5 (A): norm=0.317444 krum=0.441621 mkrum=KEEP tm_trim=0.4884 (lo 0.2439 / hi 0.2445) med_prov=0.1732 d_med=0.255872
    [shadow] C6 (A): norm=0.317766 krum=0.441677 mkrum=KEEP tm_trim=0.4889 (lo 0.2447 / hi 0.2443) med_prov=0.1731 d_med=0.255779

⏱️  Overhead round 33 (wall-clock s): round 133.95 | broadcast 0.02 | prepare 0.00 | benign train 119.18 [0:30.2 1:10.9 2:9.7 3:33.7 4:34.6] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.58 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 33 Results:
  Clean Accuracy: 0.9040
  ΔClean vs prev: +0.0060
  ΔClean vs best: +0.0000
  Global Loss: 0.6590

============================================================
Round 34/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1285, effective_std_norm=0.2727, attack_norm=0.3014, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1285, effective_std_norm=0.2727, attack_norm=0.3014, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.164584
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.084, Std Dev: 0.062
    Client 0 (Benign): 0.053
    Client 1 (Benign): 0.066
    Client 2 (Benign): 0.027
    Client 3 (Benign): 0.026
    Client 4 (Benign): 0.059
    Client 5 (Attacker): 0.180
    Client 6 (Attacker): 0.180
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.270731, Std Dev: 0.031498
    Client 0 (Benign): 0.300869
    Client 1 (Benign): 0.265726
    Client 2 (Benign): 0.276455
    Client 3 (Benign): 0.284133
    Client 4 (Benign): 0.304939
    Client 5 (Attacker): 0.203657
    Client 6 (Attacker): 0.259334
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C0 (B), C4 (B)
    [shadow] C0 (B): norm=0.335929 krum=0.498649 mkrum=REJECT tm_trim=0.6369 (lo 0.3186 / hi 0.3183) med_prov=0.1191 d_med=0.317261
    [shadow] C1 (B): norm=0.243322 krum=0.358046 mkrum=KEEP tm_trim=0.5252 (lo 0.2632 / hi 0.2620) med_prov=0.1603 d_med=0.239016
    [shadow] C2 (B): norm=0.240293 krum=0.365633 mkrum=KEEP tm_trim=0.5618 (lo 0.2812 / hi 0.2806) med_prov=0.1461 d_med=0.247968
    [shadow] C3 (B): norm=0.313393 krum=0.468194 mkrum=KEEP tm_trim=0.6492 (lo 0.3240 / hi 0.3252) med_prov=0.1127 d_med=0.305048
    [shadow] C4 (B): norm=0.355595 krum=0.524931 mkrum=REJECT tm_trim=0.6534 (lo 0.3267 / hi 0.3267) med_prov=0.1135 d_med=0.333200
    [shadow] C5 (A): norm=0.301408 krum=0.403604 mkrum=KEEP tm_trim=0.4868 (lo 0.2428 / hi 0.2440) med_prov=0.1742 d_med=0.242271
    [shadow] C6 (A): norm=0.301381 krum=0.403017 mkrum=KEEP tm_trim=0.4867 (lo 0.2436 / hi 0.2431) med_prov=0.1741 d_med=0.242194

⏱️  Overhead round 34 (wall-clock s): round 133.99 | broadcast 0.03 | prepare 0.00 | benign train 119.21 [0:30.2 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.60 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 34 Results:
  Clean Accuracy: 0.8993
  ΔClean vs prev: -0.0047
  ΔClean vs best: -0.0047
  Global Loss: 0.7508

============================================================
Round 35/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1351, effective_std_norm=0.2837, attack_norm=0.3139, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1351, effective_std_norm=0.2837, attack_norm=0.3145, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.173460
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.089, Std Dev: 0.061
    Client 0 (Benign): 0.057
    Client 1 (Benign): 0.060
    Client 2 (Benign): 0.040
    Client 3 (Benign): 0.027
    Client 4 (Benign): 0.069
    Client 5 (Attacker): 0.183
    Client 6 (Attacker): 0.184
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.281759, Std Dev: 0.032881
    Client 0 (Benign): 0.300310
    Client 1 (Benign): 0.273627
    Client 2 (Benign): 0.289165
    Client 3 (Benign): 0.320479
    Client 4 (Benign): 0.306555
    Client 5 (Attacker): 0.212101
    Client 6 (Attacker): 0.270072
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.330656 krum=0.505388 mkrum=KEEP tm_trim=0.6225 (lo 0.3114 / hi 0.3111) med_prov=0.1234 d_med=0.312387
    [shadow] C1 (B): norm=0.243166 krum=0.377172 mkrum=KEEP tm_trim=0.5236 (lo 0.2618 / hi 0.2619) med_prov=0.1617 d_med=0.244067
    [shadow] C2 (B): norm=0.252989 krum=0.389820 mkrum=KEEP tm_trim=0.5633 (lo 0.2824 / hi 0.2808) med_prov=0.1449 d_med=0.256885
    [shadow] C3 (B): norm=0.365003 krum=0.571235 mkrum=REJECT tm_trim=0.6809 (lo 0.3401 / hi 0.3408) med_prov=0.1022 d_med=0.352152
    [shadow] C4 (B): norm=0.357692 krum=0.541564 mkrum=REJECT tm_trim=0.6328 (lo 0.3164 / hi 0.3163) med_prov=0.1208 d_med=0.332757
    [shadow] C5 (A): norm=0.313894 krum=0.434763 mkrum=KEEP tm_trim=0.4881 (lo 0.2436 / hi 0.2445) med_prov=0.1738 d_med=0.252071
    [shadow] C6 (A): norm=0.314519 krum=0.434910 mkrum=KEEP tm_trim=0.4890 (lo 0.2443 / hi 0.2446) med_prov=0.1732 d_med=0.252493

⏱️  Overhead round 35 (wall-clock s): round 133.98 | broadcast 0.02 | prepare 0.00 | benign train 119.20 [0:30.2 1:10.9 2:9.7 3:33.7 4:34.6] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.60 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 35 Results:
  Clean Accuracy: 0.9000
  ΔClean vs prev: +0.0007
  ΔClean vs best: -0.0040
  Global Loss: 0.7656

============================================================
Round 36/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1382, effective_std_norm=0.2855, attack_norm=0.3174, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1382, effective_std_norm=0.2855, attack_norm=0.3173, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.175164
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.095, Std Dev: 0.060
    Client 0 (Benign): 0.047
    Client 1 (Benign): 0.069
    Client 2 (Benign): 0.066
    Client 3 (Benign): 0.041
    Client 4 (Benign): 0.066
    Client 5 (Attacker): 0.189
    Client 6 (Attacker): 0.189
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.283652, Std Dev: 0.032791
    Client 0 (Benign): 0.308743
    Client 1 (Benign): 0.277807
    Client 2 (Benign): 0.285685
    Client 3 (Benign): 0.310810
    Client 4 (Benign): 0.316902
    Client 5 (Attacker): 0.213834
    Client 6 (Attacker): 0.271780
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.337329 krum=0.528801 mkrum=KEEP tm_trim=0.6301 (lo 0.3154 / hi 0.3147) med_prov=0.1207 d_med=0.323511
    [shadow] C1 (B): norm=0.249447 krum=0.381378 mkrum=KEEP tm_trim=0.5268 (lo 0.2639 / hi 0.2629) med_prov=0.1598 d_med=0.247936
    [shadow] C2 (B): norm=0.256414 krum=0.386946 mkrum=KEEP tm_trim=0.5579 (lo 0.2790 / hi 0.2789) med_prov=0.1475 d_med=0.253039
    [shadow] C3 (B): norm=0.352283 krum=0.552228 mkrum=REJECT tm_trim=0.6635 (lo 0.3312 / hi 0.3324) med_prov=0.1082 d_med=0.337600
    [shadow] C4 (B): norm=0.370531 krum=0.571674 mkrum=REJECT tm_trim=0.6479 (lo 0.3234 / hi 0.3245) med_prov=0.1153 d_med=0.345958
    [shadow] C5 (A): norm=0.317357 krum=0.439577 mkrum=KEEP tm_trim=0.4873 (lo 0.2437 / hi 0.2436) med_prov=0.1738 d_med=0.254149
    [shadow] C6 (A): norm=0.317305 krum=0.439742 mkrum=KEEP tm_trim=0.4864 (lo 0.2434 / hi 0.2430) med_prov=0.1747 d_med=0.254105

⏱️  Overhead round 36 (wall-clock s): round 134.32 | broadcast 0.02 | prepare 0.00 | benign train 119.53 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.12 | observe 0.00 | eval_global 6.93 | eval_local 7.58 (bookkeeping) | unaccounted 0.05
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.06s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 36 Results:
  Clean Accuracy: 0.8963
  ΔClean vs prev: -0.0037
  ΔClean vs best: -0.0077
  Global Loss: 0.7442

============================================================
Round 37/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1380, effective_std_norm=0.2869, attack_norm=0.3182, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1380, effective_std_norm=0.2869, attack_norm=0.3190, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.176552
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.091, Std Dev: 0.062
    Client 0 (Benign): 0.053
    Client 1 (Benign): 0.068
    Client 2 (Benign): 0.042
    Client 3 (Benign): 0.025
    Client 4 (Benign): 0.078
    Client 5 (Attacker): 0.185
    Client 6 (Attacker): 0.186
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.284857, Std Dev: 0.034504
    Client 0 (Benign): 0.307524
    Client 1 (Benign): 0.274809
    Client 2 (Benign): 0.292538
    Client 3 (Benign): 0.296617
    Client 4 (Benign): 0.334466
    Client 5 (Attacker): 0.214648
    Client 6 (Attacker): 0.273398
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C0 (B), C4 (B)
    [shadow] C0 (B): norm=0.338865 krum=0.528210 mkrum=REJECT tm_trim=0.6302 (lo 0.3149 / hi 0.3153) med_prov=0.1208 d_med=0.321578
    [shadow] C1 (B): norm=0.245165 krum=0.382193 mkrum=KEEP tm_trim=0.5197 (lo 0.2601 / hi 0.2595) med_prov=0.1628 d_med=0.244864
    [shadow] C2 (B): norm=0.256932 krum=0.396971 mkrum=KEEP tm_trim=0.5650 (lo 0.2831 / hi 0.2819) med_prov=0.1447 d_med=0.259826
    [shadow] C3 (B): norm=0.323573 krum=0.508224 mkrum=KEEP tm_trim=0.6349 (lo 0.3169 / hi 0.3180) med_prov=0.1183 d_med=0.318394
    [shadow] C4 (B): norm=0.401340 krum=0.620881 mkrum=REJECT tm_trim=0.6739 (lo 0.3368 / hi 0.3371) med_prov=0.1066 d_med=0.368338
    [shadow] C5 (A): norm=0.318245 krum=0.444522 mkrum=KEEP tm_trim=0.4879 (lo 0.2443 / hi 0.2436) med_prov=0.1731 d_med=0.255382
    [shadow] C6 (A): norm=0.319012 krum=0.444999 mkrum=KEEP tm_trim=0.4885 (lo 0.2440 / hi 0.2445) med_prov=0.1737 d_med=0.255772

⏱️  Overhead round 37 (wall-clock s): round 133.94 | broadcast 0.03 | prepare 0.00 | benign train 119.23 [0:30.2 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.55 (bookkeeping) | unaccounted 0.01
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 37 Results:
  Clean Accuracy: 0.9013
  ΔClean vs prev: +0.0050
  ΔClean vs best: -0.0027
  Global Loss: 0.7558

============================================================
Round 38/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1396, effective_std_norm=0.2960, attack_norm=0.3271, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1396, effective_std_norm=0.2960, attack_norm=0.3267, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.180366
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.086, Std Dev: 0.062
    Client 0 (Benign): 0.057
    Client 1 (Benign): 0.072
    Client 2 (Benign): 0.029
    Client 3 (Benign): 0.020
    Client 4 (Benign): 0.061
    Client 5 (Attacker): 0.180
    Client 6 (Attacker): 0.180
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.293360, Std Dev: 0.037128
    Client 0 (Benign): 0.324734
    Client 1 (Benign): 0.272500
    Client 2 (Benign): 0.293131
    Client 3 (Benign): 0.325297
    Client 4 (Benign): 0.335977
    Client 5 (Attacker): 0.220983
    Client 6 (Attacker): 0.280900
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.358610 krum=0.561852 mkrum=KEEP tm_trim=0.6393 (lo 0.3202 / hi 0.3191) med_prov=0.1177 d_med=0.336734
    [shadow] C1 (B): norm=0.242347 krum=0.387228 mkrum=KEEP tm_trim=0.5017 (lo 0.2513 / hi 0.2505) med_prov=0.1697 d_med=0.240988
    [shadow] C2 (B): norm=0.249135 krum=0.405006 mkrum=KEEP tm_trim=0.5532 (lo 0.2763 / hi 0.2769) med_prov=0.1490 d_med=0.258231
    [shadow] C3 (B): norm=0.361940 krum=0.582217 mkrum=REJECT tm_trim=0.6637 (lo 0.3314 / hi 0.3323) med_prov=0.1078 d_med=0.352593
    [shadow] C4 (B): norm=0.393769 krum=0.621335 mkrum=REJECT tm_trim=0.6601 (lo 0.3304 / hi 0.3297) med_prov=0.1105 d_med=0.367370
    [shadow] C5 (A): norm=0.327127 krum=0.463059 mkrum=KEEP tm_trim=0.4909 (lo 0.2452 / hi 0.2457) med_prov=0.1722 d_med=0.263819
    [shadow] C6 (A): norm=0.326736 krum=0.462243 mkrum=KEEP tm_trim=0.4910 (lo 0.2453 / hi 0.2458) med_prov=0.1729 d_med=0.263279

⏱️  Overhead round 38 (wall-clock s): round 133.97 | broadcast 0.03 | prepare 0.00 | benign train 119.20 [0:30.2 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.08 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.58 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 38 Results:
  Clean Accuracy: 0.8973
  ΔClean vs prev: -0.0040
  ΔClean vs best: -0.0067
  Global Loss: 0.8028

============================================================
Round 39/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1297, effective_std_norm=0.2708, attack_norm=0.3004, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1297, effective_std_norm=0.2708, attack_norm=0.3004, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.164524
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.091, Std Dev: 0.062
    Client 0 (Benign): 0.054
    Client 1 (Benign): 0.064
    Client 2 (Benign): 0.050
    Client 3 (Benign): 0.025
    Client 4 (Benign): 0.070
    Client 5 (Attacker): 0.186
    Client 6 (Attacker): 0.186
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.269265, Std Dev: 0.029596
    Client 0 (Benign): 0.287522
    Client 1 (Benign): 0.273252
    Client 2 (Benign): 0.277131
    Client 3 (Benign): 0.292633
    Client 4 (Benign): 0.293737
    Client 5 (Attacker): 0.202564
    Client 6 (Attacker): 0.258013
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.317928 krum=0.472619 mkrum=KEEP tm_trim=0.6294 (lo 0.3147 / hi 0.3148) med_prov=0.1203 d_med=0.301600
    [shadow] C1 (B): norm=0.250043 krum=0.362031 mkrum=KEEP tm_trim=0.5479 (lo 0.2736 / hi 0.2744) med_prov=0.1511 d_med=0.246132
    [shadow] C2 (B): norm=0.247734 krum=0.364378 mkrum=KEEP tm_trim=0.5622 (lo 0.2814 / hi 0.2807) med_prov=0.1462 d_med=0.248101
    [shadow] C3 (B): norm=0.327490 krum=0.498740 mkrum=REJECT tm_trim=0.6585 (lo 0.3290 / hi 0.3295) med_prov=0.1097 d_med=0.319627
    [shadow] C4 (B): norm=0.344298 krum=0.501064 mkrum=REJECT tm_trim=0.6320 (lo 0.3162 / hi 0.3159) med_prov=0.1216 d_med=0.320113
    [shadow] C5 (A): norm=0.300436 krum=0.402708 mkrum=KEEP tm_trim=0.4845 (lo 0.2424 / hi 0.2421) med_prov=0.1758 d_med=0.240539
    [shadow] C6 (A): norm=0.300354 krum=0.402403 mkrum=KEEP tm_trim=0.4854 (lo 0.2428 / hi 0.2426) med_prov=0.1753 d_med=0.240927

⏱️  Overhead round 39 (wall-clock s): round 134.23 | broadcast 0.02 | prepare 0.00 | benign train 119.47 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.10 | observe 0.00 | eval_global 6.93 | eval_local 7.56 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 39 Results:
  Clean Accuracy: 0.9023
  ΔClean vs prev: +0.0050
  ΔClean vs best: -0.0017
  Global Loss: 0.7769

============================================================
Round 40/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1416, effective_std_norm=0.2893, attack_norm=0.3218, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1416, effective_std_norm=0.2893, attack_norm=0.3219, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.181100
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.098, Std Dev: 0.059
    Client 0 (Benign): 0.063
    Client 1 (Benign): 0.067
    Client 2 (Benign): 0.055
    Client 3 (Benign): 0.047
    Client 4 (Benign): 0.071
    Client 5 (Attacker): 0.191
    Client 6 (Attacker): 0.191
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.287168, Std Dev: 0.034300
    Client 0 (Benign): 0.306444
    Client 1 (Benign): 0.282978
    Client 2 (Benign): 0.282121
    Client 3 (Benign): 0.324938
    Client 4 (Benign): 0.322213
    Client 5 (Attacker): 0.216299
    Client 6 (Attacker): 0.275184
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C2 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.334819 krum=0.511523 mkrum=KEEP tm_trim=0.6283 (lo 0.3140 / hi 0.3143) med_prov=0.1214 d_med=0.316199
    [shadow] C1 (B): norm=0.251709 krum=0.386610 mkrum=KEEP tm_trim=0.5350 (lo 0.2672 / hi 0.2678) med_prov=0.1568 d_med=0.251115
    [shadow] C2 (B): norm=0.242576 krum=0.384608 mkrum=KEEP tm_trim=0.5373 (lo 0.2690 / hi 0.2683) med_prov=0.1552 d_med=0.248711
    [shadow] C3 (B): norm=0.374389 krum=0.593021 mkrum=REJECT tm_trim=0.6619 (lo 0.3304 / hi 0.3315) med_prov=0.1095 d_med=0.356612
    [shadow] C4 (B): norm=0.379703 krum=0.587783 mkrum=REJECT tm_trim=0.6636 (lo 0.3318 / hi 0.3318) med_prov=0.1093 d_med=0.352000
    [shadow] C5 (A): norm=0.321836 krum=0.447321 mkrum=KEEP tm_trim=0.4871 (lo 0.2440 / hi 0.2432) med_prov=0.1733 d_med=0.257523
    [shadow] C6 (A): norm=0.321914 krum=0.447386 mkrum=KEEP tm_trim=0.4868 (lo 0.2436 / hi 0.2432) med_prov=0.1745 d_med=0.257108

⏱️  Overhead round 40 (wall-clock s): round 133.93 | broadcast 0.03 | prepare 0.00 | benign train 119.21 [0:30.2 1:10.9 2:9.7 3:33.7 4:34.6] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.57 (bookkeeping) | unaccounted 0.01
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 40 Results:
  Clean Accuracy: 0.8987
  ΔClean vs prev: -0.0037
  ΔClean vs best: -0.0053
  Global Loss: 0.7982

============================================================
Round 41/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1373, effective_std_norm=0.2851, attack_norm=0.3159, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1373, effective_std_norm=0.2851, attack_norm=0.3160, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.175553
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.092, Std Dev: 0.061
    Client 0 (Benign): 0.073
    Client 1 (Benign): 0.062
    Client 2 (Benign): 0.049
    Client 3 (Benign): 0.023
    Client 4 (Benign): 0.063
    Client 5 (Attacker): 0.186
    Client 6 (Attacker): 0.186
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.282943, Std Dev: 0.033627
    Client 0 (Benign): 0.310857
    Client 1 (Benign): 0.273191
    Client 2 (Benign): 0.285517
    Client 3 (Benign): 0.305982
    Client 4 (Benign): 0.321228
    Client 5 (Attacker): 0.213006
    Client 6 (Attacker): 0.270823
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C0 (B), C4 (B)
    [shadow] C0 (B): norm=0.352411 krum=0.533994 mkrum=REJECT tm_trim=0.6448 (lo 0.3224 / hi 0.3224) med_prov=0.1152 d_med=0.325866
    [shadow] C1 (B): norm=0.240231 krum=0.370757 mkrum=KEEP tm_trim=0.5176 (lo 0.2590 / hi 0.2585) med_prov=0.1632 d_med=0.242947
    [shadow] C2 (B): norm=0.249679 krum=0.380757 mkrum=KEEP tm_trim=0.5586 (lo 0.2800 / hi 0.2785) med_prov=0.1474 d_med=0.252093
    [shadow] C3 (B): norm=0.338836 krum=0.529504 mkrum=KEEP tm_trim=0.6538 (lo 0.3266 / hi 0.3273) med_prov=0.1117 d_med=0.331140
    [shadow] C4 (B): norm=0.376214 krum=0.578330 mkrum=REJECT tm_trim=0.6503 (lo 0.3243 / hi 0.3260) med_prov=0.1148 d_med=0.351866
    [shadow] C5 (A): norm=0.315909 krum=0.434339 mkrum=KEEP tm_trim=0.4880 (lo 0.2439 / hi 0.2441) med_prov=0.1737 d_med=0.253417
    [shadow] C6 (A): norm=0.316040 krum=0.434620 mkrum=KEEP tm_trim=0.4870 (lo 0.2438 / hi 0.2432) med_prov=0.1740 d_med=0.253474

⏱️  Overhead round 41 (wall-clock s): round 133.96 | broadcast 0.02 | prepare 0.00 | benign train 119.19 [0:30.2 1:10.9 2:9.7 3:33.7 4:34.6] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.57 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 41 Results:
  Clean Accuracy: 0.9077
  ΔClean vs prev: +0.0090
  ΔClean vs best: +0.0000
  Global Loss: 0.7730

============================================================
Round 42/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1395, effective_std_norm=0.2914, attack_norm=0.3232, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1395, effective_std_norm=0.2914, attack_norm=0.3231, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.179655
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.091, Std Dev: 0.060
    Client 0 (Benign): 0.053
    Client 1 (Benign): 0.063
    Client 2 (Benign): 0.046
    Client 3 (Benign): 0.039
    Client 4 (Benign): 0.064
    Client 5 (Attacker): 0.185
    Client 6 (Attacker): 0.185
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.289420, Std Dev: 0.034094
    Client 0 (Benign): 0.307522
    Client 1 (Benign): 0.282055
    Client 2 (Benign): 0.292102
    Client 3 (Benign): 0.330674
    Client 4 (Benign): 0.318098
    Client 5 (Attacker): 0.218167
    Client 6 (Attacker): 0.277321
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.337049 krum=0.531560 mkrum=KEEP tm_trim=0.6230 (lo 0.3112 / hi 0.3118) med_prov=0.1234 d_med=0.320294
    [shadow] C1 (B): norm=0.248915 krum=0.388509 mkrum=KEEP tm_trim=0.5306 (lo 0.2659 / hi 0.2647) med_prov=0.1578 d_med=0.249896
    [shadow] C2 (B): norm=0.252344 krum=0.396287 mkrum=KEEP tm_trim=0.5586 (lo 0.2794 / hi 0.2792) med_prov=0.1468 d_med=0.256856
    [shadow] C3 (B): norm=0.381346 krum=0.610269 mkrum=REJECT tm_trim=0.6756 (lo 0.3374 / hi 0.3382) med_prov=0.1044 d_med=0.363977
    [shadow] C4 (B): norm=0.370260 krum=0.579939 mkrum=REJECT tm_trim=0.6384 (lo 0.3194 / hi 0.3190) med_prov=0.1195 d_med=0.345616
    [shadow] C5 (A): norm=0.323230 krum=0.456120 mkrum=KEEP tm_trim=0.4870 (lo 0.2431 / hi 0.2440) med_prov=0.1740 d_med=0.259464
    [shadow] C6 (A): norm=0.323139 krum=0.455661 mkrum=KEEP tm_trim=0.4868 (lo 0.2436 / hi 0.2432) med_prov=0.1742 d_med=0.259339

⏱️  Overhead round 42 (wall-clock s): round 133.96 | broadcast 0.03 | prepare 0.00 | benign train 119.19 [0:30.2 1:10.9 2:9.7 3:33.7 4:34.6] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.57 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 42 Results:
  Clean Accuracy: 0.9023
  ΔClean vs prev: -0.0053
  ΔClean vs best: -0.0053
  Global Loss: 0.8236

============================================================
Round 43/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1441, effective_std_norm=0.2975, attack_norm=0.3305, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1441, effective_std_norm=0.2975, attack_norm=0.3305, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.184150
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.097, Std Dev: 0.060
    Client 0 (Benign): 0.069
    Client 1 (Benign): 0.084
    Client 2 (Benign): 0.060
    Client 3 (Benign): 0.033
    Client 4 (Benign): 0.057
    Client 5 (Attacker): 0.189
    Client 6 (Attacker): 0.190
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.294928, Std Dev: 0.037942
    Client 0 (Benign): 0.316092
    Client 1 (Benign): 0.275074
    Client 2 (Benign): 0.290840
    Client 3 (Benign): 0.335993
    Client 4 (Benign): 0.341169
    Client 5 (Attacker): 0.222486
    Client 6 (Attacker): 0.282841
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.349218 krum=0.544970 mkrum=KEEP tm_trim=0.6292 (lo 0.3149 / hi 0.3143) med_prov=0.1207 d_med=0.328012
    [shadow] C1 (B): norm=0.243179 krum=0.382740 mkrum=KEEP tm_trim=0.4997 (lo 0.2501 / hi 0.2496) med_prov=0.1716 d_med=0.240134
    [shadow] C2 (B): norm=0.252012 krum=0.395805 mkrum=KEEP tm_trim=0.5455 (lo 0.2728 / hi 0.2726) med_prov=0.1519 d_med=0.252888
    [shadow] C3 (B): norm=0.381010 krum=0.615575 mkrum=REJECT tm_trim=0.6696 (lo 0.3339 / hi 0.3357) med_prov=0.1065 d_med=0.367717
    [shadow] C4 (B): norm=0.395796 krum=0.634868 mkrum=REJECT tm_trim=0.6726 (lo 0.3361 / hi 0.3365) med_prov=0.1059 d_med=0.372368
    [shadow] C5 (A): norm=0.330504 krum=0.465426 mkrum=KEEP tm_trim=0.4916 (lo 0.2463 / hi 0.2453) med_prov=0.1716 d_med=0.265381
    [shadow] C6 (A): norm=0.330457 krum=0.465211 mkrum=KEEP tm_trim=0.4918 (lo 0.2459 / hi 0.2459) med_prov=0.1718 d_med=0.265035

⏱️  Overhead round 43 (wall-clock s): round 133.94 | broadcast 0.03 | prepare 0.00 | benign train 119.20 [0:30.2 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.56 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 43 Results:
  Clean Accuracy: 0.9003
  ΔClean vs prev: -0.0020
  ΔClean vs best: -0.0073
  Global Loss: 0.8336

============================================================
Round 44/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1425, effective_std_norm=0.2960, attack_norm=0.3284, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1425, effective_std_norm=0.2960, attack_norm=0.3281, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.184057
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.091, Std Dev: 0.062
    Client 0 (Benign): 0.061
    Client 1 (Benign): 0.055
    Client 2 (Benign): 0.048
    Client 3 (Benign): 0.023
    Client 4 (Benign): 0.078
    Client 5 (Attacker): 0.185
    Client 6 (Attacker): 0.185
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.293784, Std Dev: 0.035753
    Client 0 (Benign): 0.315956
    Client 1 (Benign): 0.286454
    Client 2 (Benign): 0.290884
    Client 3 (Benign): 0.317376
    Client 4 (Benign): 0.343052
    Client 5 (Attacker): 0.221262
    Client 6 (Attacker): 0.281506
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.350346 krum=0.554837 mkrum=KEEP tm_trim=0.6295 (lo 0.3148 / hi 0.3147) med_prov=0.1202 d_med=0.330070
    [shadow] C1 (B): norm=0.247674 krum=0.395460 mkrum=KEEP tm_trim=0.5220 (lo 0.2613 / hi 0.2608) med_prov=0.1620 d_med=0.253582
    [shadow] C2 (B): norm=0.249866 krum=0.398404 mkrum=KEEP tm_trim=0.5419 (lo 0.2711 / hi 0.2708) med_prov=0.1540 d_med=0.256111
    [shadow] C3 (B): norm=0.351502 krum=0.572331 mkrum=REJECT tm_trim=0.6665 (lo 0.3322 / hi 0.3343) med_prov=0.1052 d_med=0.342941
    [shadow] C4 (B): norm=0.411733 krum=0.647577 mkrum=REJECT tm_trim=0.6732 (lo 0.3372 / hi 0.3359) med_prov=0.1061 d_med=0.377806
    [shadow] C5 (A): norm=0.328377 krum=0.466968 mkrum=KEEP tm_trim=0.4836 (lo 0.2418 / hi 0.2418) med_prov=0.1761 d_med=0.262979
    [shadow] C6 (A): norm=0.328113 krum=0.466161 mkrum=KEEP tm_trim=0.4833 (lo 0.2416 / hi 0.2417) med_prov=0.1763 d_med=0.262680

⏱️  Overhead round 44 (wall-clock s): round 134.16 | broadcast 0.03 | prepare 0.00 | benign train 119.38 [0:30.2 1:10.9 2:9.7 3:33.8 4:34.7] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.58 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.06s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 44 Results:
  Clean Accuracy: 0.9007
  ΔClean vs prev: +0.0003
  ΔClean vs best: -0.0070
  Global Loss: 0.7996

============================================================
Round 45/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1357, effective_std_norm=0.2791, attack_norm=0.3107, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1357, effective_std_norm=0.2791, attack_norm=0.3102, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.172592
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.095, Std Dev: 0.062
    Client 0 (Benign): 0.067
    Client 1 (Benign): 0.067
    Client 2 (Benign): 0.050
    Client 3 (Benign): 0.028
    Client 4 (Benign): 0.075
    Client 5 (Attacker): 0.190
    Client 6 (Attacker): 0.190
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.277344, Std Dev: 0.031584
    Client 0 (Benign): 0.295686
    Client 1 (Benign): 0.276661
    Client 2 (Benign): 0.281609
    Client 3 (Benign): 0.299724
    Client 4 (Benign): 0.313435
    Client 5 (Attacker): 0.208926
    Client 6 (Attacker): 0.265363
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.329567 krum=0.493726 mkrum=KEEP tm_trim=0.6227 (lo 0.3106 / hi 0.3121) med_prov=0.1232 d_med=0.309993
    [shadow] C1 (B): norm=0.250231 krum=0.374339 mkrum=KEEP tm_trim=0.5410 (lo 0.2708 / hi 0.2702) med_prov=0.1531 d_med=0.247535
    [shadow] C2 (B): norm=0.248161 krum=0.377356 mkrum=KEEP tm_trim=0.5595 (lo 0.2803 / hi 0.2792) med_prov=0.1464 d_med=0.250409
    [shadow] C3 (B): norm=0.331888 krum=0.513430 mkrum=REJECT tm_trim=0.6600 (lo 0.3299 / hi 0.3301) med_prov=0.1095 d_med=0.324274
    [shadow] C4 (B): norm=0.372467 krum=0.559319 mkrum=REJECT tm_trim=0.6478 (lo 0.3239 / hi 0.3238) med_prov=0.1164 d_med=0.345163
    [shadow] C5 (A): norm=0.310736 krum=0.423223 mkrum=KEEP tm_trim=0.4840 (lo 0.2420 / hi 0.2420) med_prov=0.1758 d_med=0.248199
    [shadow] C6 (A): norm=0.310151 krum=0.422801 mkrum=KEEP tm_trim=0.4850 (lo 0.2425 / hi 0.2425) med_prov=0.1757 d_med=0.247821

⏱️  Overhead round 45 (wall-clock s): round 134.31 | broadcast 0.03 | prepare 0.00 | benign train 119.52 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.58 (bookkeeping) | unaccounted 0.06
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 45 Results:
  Clean Accuracy: 0.8993
  ΔClean vs prev: -0.0013
  ΔClean vs best: -0.0083
  Global Loss: 0.8249

============================================================
Round 46/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1398, effective_std_norm=0.2949, attack_norm=0.3264, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1398, effective_std_norm=0.2949, attack_norm=0.3266, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.181171
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.087, Std Dev: 0.060
    Client 0 (Benign): 0.045
    Client 1 (Benign): 0.056
    Client 2 (Benign): 0.046
    Client 3 (Benign): 0.037
    Client 4 (Benign): 0.063
    Client 5 (Attacker): 0.181
    Client 6 (Attacker): 0.181
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.292754, Std Dev: 0.036094
    Client 0 (Benign): 0.301878
    Client 1 (Benign): 0.286749
    Client 2 (Benign): 0.289305
    Client 3 (Benign): 0.342318
    Client 4 (Benign): 0.327461
    Client 5 (Attacker): 0.220750
    Client 6 (Attacker): 0.280818
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.324588 krum=0.518641 mkrum=KEEP tm_trim=0.6133 (lo 0.3069 / hi 0.3064) med_prov=0.1268 d_med=0.311640
    [shadow] C1 (B): norm=0.250864 krum=0.395067 mkrum=KEEP tm_trim=0.5347 (lo 0.2674 / hi 0.2673) med_prov=0.1564 d_med=0.252670
    [shadow] C2 (B): norm=0.247677 krum=0.396032 mkrum=KEEP tm_trim=0.5455 (lo 0.2733 / hi 0.2722) med_prov=0.1516 d_med=0.253108
    [shadow] C3 (B): norm=0.395528 krum=0.645877 mkrum=REJECT tm_trim=0.6798 (lo 0.3393 / hi 0.3405) med_prov=0.1030 d_med=0.377425
    [shadow] C4 (B): norm=0.382636 krum=0.604796 mkrum=REJECT tm_trim=0.6493 (lo 0.3247 / hi 0.3246) med_prov=0.1155 d_med=0.356631
    [shadow] C5 (A): norm=0.326395 krum=0.463568 mkrum=KEEP tm_trim=0.4888 (lo 0.2441 / hi 0.2447) med_prov=0.1731 d_med=0.263075
    [shadow] C6 (A): norm=0.326551 krum=0.463305 mkrum=KEEP tm_trim=0.4886 (lo 0.2443 / hi 0.2443) med_prov=0.1737 d_med=0.262901

⏱️  Overhead round 46 (wall-clock s): round 134.24 | broadcast 0.03 | prepare 0.00 | benign train 119.48 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.57 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 46 Results:
  Clean Accuracy: 0.9010
  ΔClean vs prev: +0.0017
  ΔClean vs best: -0.0067
  Global Loss: 0.8306

============================================================
Round 47/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1388, effective_std_norm=0.2844, attack_norm=0.3167, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1388, effective_std_norm=0.2844, attack_norm=0.3165, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.175203
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.098, Std Dev: 0.060
    Client 0 (Benign): 0.061
    Client 1 (Benign): 0.066
    Client 2 (Benign): 0.067
    Client 3 (Benign): 0.039
    Client 4 (Benign): 0.069
    Client 5 (Attacker): 0.192
    Client 6 (Attacker): 0.191
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.282456, Std Dev: 0.032729
    Client 0 (Benign): 0.319371
    Client 1 (Benign): 0.281347
    Client 2 (Benign): 0.280942
    Client 3 (Benign): 0.307750
    Client 4 (Benign): 0.304391
    Client 5 (Attacker): 0.212643
    Client 6 (Attacker): 0.270747
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C2 (B)
    [shadow] Multi-Krum rejected: C0 (B), C3 (B)
    [shadow] C0 (B): norm=0.359422 krum=0.553657 mkrum=REJECT tm_trim=0.6467 (lo 0.3235 / hi 0.3232) med_prov=0.1154 d_med=0.339217
    [shadow] C1 (B): norm=0.253903 krum=0.387473 mkrum=KEEP tm_trim=0.5430 (lo 0.2716 / hi 0.2715) med_prov=0.1529 d_med=0.252250
    [shadow] C2 (B): norm=0.252225 krum=0.385736 mkrum=KEEP tm_trim=0.5507 (lo 0.2755 / hi 0.2751) med_prov=0.1498 d_med=0.249560
    [shadow] C3 (B): norm=0.346178 krum=0.543742 mkrum=REJECT tm_trim=0.6569 (lo 0.3288 / hi 0.3280) med_prov=0.1105 d_med=0.334491
    [shadow] C4 (B): norm=0.351920 krum=0.533690 mkrum=KEEP tm_trim=0.6330 (lo 0.3163 / hi 0.3166) med_prov=0.1208 d_med=0.329339
    [shadow] C5 (A): norm=0.316747 krum=0.437589 mkrum=KEEP tm_trim=0.4851 (lo 0.2422 / hi 0.2428) med_prov=0.1755 d_med=0.252877
    [shadow] C6 (A): norm=0.316544 krum=0.437171 mkrum=KEEP tm_trim=0.4847 (lo 0.2420 / hi 0.2427) med_prov=0.1750 d_med=0.252966

⏱️  Overhead round 47 (wall-clock s): round 134.26 | broadcast 0.03 | prepare 0.00 | benign train 119.48 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.12 | observe 0.00 | eval_global 6.93 | eval_local 7.58 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 47 Results:
  Clean Accuracy: 0.9057
  ΔClean vs prev: +0.0047
  ΔClean vs best: -0.0020
  Global Loss: 0.7684

============================================================
Round 48/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1397, effective_std_norm=0.2922, attack_norm=0.3239, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1397, effective_std_norm=0.2922, attack_norm=0.3239, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.181488
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.087, Std Dev: 0.062
    Client 0 (Benign): 0.053
    Client 1 (Benign): 0.046
    Client 2 (Benign): 0.029
    Client 3 (Benign): 0.038
    Client 4 (Benign): 0.075
    Client 5 (Attacker): 0.182
    Client 6 (Attacker): 0.182
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.290217, Std Dev: 0.034561
    Client 0 (Benign): 0.311113
    Client 1 (Benign): 0.286869
    Client 2 (Benign): 0.294028
    Client 3 (Benign): 0.302752
    Client 4 (Benign): 0.340008
    Client 5 (Attacker): 0.218701
    Client 6 (Attacker): 0.278045
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C0 (B), C4 (B)
    [shadow] C0 (B): norm=0.342206 krum=0.540115 mkrum=REJECT tm_trim=0.6312 (lo 0.3155 / hi 0.3157) med_prov=0.1203 d_med=0.324191
    [shadow] C1 (B): norm=0.249377 krum=0.400874 mkrum=KEEP tm_trim=0.5354 (lo 0.2671 / hi 0.2684) med_prov=0.1559 d_med=0.255621
    [shadow] C2 (B): norm=0.250785 krum=0.406049 mkrum=KEEP tm_trim=0.5521 (lo 0.2764 / hi 0.2756) med_prov=0.1493 d_med=0.261933
    [shadow] C3 (B): norm=0.337198 krum=0.536603 mkrum=KEEP tm_trim=0.6412 (lo 0.3206 / hi 0.3206) med_prov=0.1155 d_med=0.324910
    [shadow] C4 (B): norm=0.410719 krum=0.648928 mkrum=REJECT tm_trim=0.6739 (lo 0.3370 / hi 0.3368) med_prov=0.1066 d_med=0.376997
    [shadow] C5 (A): norm=0.323856 krum=0.460992 mkrum=KEEP tm_trim=0.4830 (lo 0.2422 / hi 0.2408) med_prov=0.1765 d_med=0.259693
    [shadow] C6 (A): norm=0.323921 krum=0.461559 mkrum=KEEP tm_trim=0.4832 (lo 0.2411 / hi 0.2421) med_prov=0.1758 d_med=0.259486

⏱️  Overhead round 48 (wall-clock s): round 134.25 | broadcast 0.03 | prepare 0.00 | benign train 119.49 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.08 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.58 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.04s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 48 Results:
  Clean Accuracy: 0.9030
  ΔClean vs prev: -0.0027
  ΔClean vs best: -0.0047
  Global Loss: 0.8556

============================================================
Round 49/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1454, effective_std_norm=0.2927, attack_norm=0.3263, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1454, effective_std_norm=0.2927, attack_norm=0.3267, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.183486
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.106, Std Dev: 0.058
    Client 0 (Benign): 0.064
    Client 1 (Benign): 0.081
    Client 2 (Benign): 0.081
    Client 3 (Benign): 0.056
    Client 4 (Benign): 0.066
    Client 5 (Attacker): 0.197
    Client 6 (Attacker): 0.197
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.290294, Std Dev: 0.036613
    Client 0 (Benign): 0.300473
    Client 1 (Benign): 0.284566
    Client 2 (Benign): 0.285991
    Client 3 (Benign): 0.347778
    Client 4 (Benign): 0.316081
    Client 5 (Attacker): 0.218754
    Client 6 (Attacker): 0.278417
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C2 (B)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.324341 krum=0.506244 mkrum=KEEP tm_trim=0.6159 (lo 0.3068 / hi 0.3091) med_prov=0.1256 d_med=0.309310
    [shadow] C1 (B): norm=0.255278 krum=0.391703 mkrum=KEEP tm_trim=0.5386 (lo 0.2696 / hi 0.2690) med_prov=0.1533 d_med=0.251135
    [shadow] C2 (B): norm=0.254248 krum=0.391537 mkrum=KEEP tm_trim=0.5434 (lo 0.2718 / hi 0.2716) med_prov=0.1528 d_med=0.249918
    [shadow] C3 (B): norm=0.410480 krum=0.665400 mkrum=REJECT tm_trim=0.6853 (lo 0.3424 / hi 0.3429) med_prov=0.1016 d_med=0.388233
    [shadow] C4 (B): norm=0.361230 krum=0.563849 mkrum=REJECT tm_trim=0.6427 (lo 0.3219 / hi 0.3208) med_prov=0.1172 d_med=0.340633
    [shadow] C5 (A): norm=0.326334 krum=0.455243 mkrum=KEEP tm_trim=0.4873 (lo 0.2440 / hi 0.2433) med_prov=0.1747 d_med=0.260555
    [shadow] C6 (A): norm=0.326729 krum=0.456160 mkrum=KEEP tm_trim=0.4867 (lo 0.2435 / hi 0.2432) med_prov=0.1748 d_med=0.260862

⏱️  Overhead round 49 (wall-clock s): round 134.31 | broadcast 0.03 | prepare 0.00 | benign train 119.54 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.09 [5:0.0 6:0.1] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.57 (bookkeeping) | unaccounted 0.05
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.05s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 49 Results:
  Clean Accuracy: 0.9113
  ΔClean vs prev: +0.0083
  ΔClean vs best: +0.0000
  Global Loss: 0.7681

============================================================
Round 50/50
Current Parameters: server_lr=1.00
============================================================
📡 Broadcasting the global model...

🔧 Phase 1: Client Preparation

💪 Phase 2: Local Training
  ✓ Client 0 completed training
  ✓ Client 1 completed training
  ✓ Client 2 completed training
  ✓ Client 3 completed training
  ✓ Client 4 completed training
  ✓ Client 5 completed training
  ✓ Client 6 completed training

🎭 Phase 3: Attacker Camouflage
  Captured 5 benign updates for camouflage.
  ⚠️ Triggering camouflage logic for Client 5
    [Gaussian Attacker 5] Generated attack (LoRA): mean_norm=0.1379, effective_std_norm=0.2884, attack_norm=0.3197, num_benign=5
  ⚠️ Triggering camouflage logic for Client 6
    [Gaussian Attacker 6] Generated attack (LoRA): mean_norm=0.1379, effective_std_norm=0.2884, attack_norm=0.3197, num_benign=5

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.177836
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.087, Std Dev: 0.062
    Client 0 (Benign): 0.053
    Client 1 (Benign): 0.047
    Client 2 (Benign): 0.034
    Client 3 (Benign): 0.034
    Client 4 (Benign): 0.076
    Client 5 (Attacker): 0.183
    Client 6 (Attacker): 0.183
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.286598, Std Dev: 0.032722
    Client 0 (Benign): 0.314093
    Client 1 (Benign): 0.287047
    Client 2 (Benign): 0.291809
    Client 3 (Benign): 0.298667
    Client 4 (Benign): 0.324168
    Client 5 (Attacker): 0.215815
    Client 6 (Attacker): 0.274586
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C1 (B)
    [shadow] Multi-Krum rejected: C0 (B), C4 (B)
    [shadow] C0 (B): norm=0.350329 krum=0.551942 mkrum=REJECT tm_trim=0.6419 (lo 0.3208 / hi 0.3212) med_prov=0.1165 d_med=0.331380
    [shadow] C1 (B): norm=0.252987 krum=0.398700 mkrum=KEEP tm_trim=0.5528 (lo 0.2760 / hi 0.2768) med_prov=0.1473 d_med=0.257129
    [shadow] C2 (B): norm=0.252689 krum=0.401722 mkrum=KEEP tm_trim=0.5539 (lo 0.2776 / hi 0.2763) med_prov=0.1485 d_med=0.262574
    [shadow] C3 (B): norm=0.334631 krum=0.532650 mkrum=KEEP tm_trim=0.6489 (lo 0.3243 / hi 0.3246) med_prov=0.1119 d_med=0.323265
    [shadow] C4 (B): norm=0.385248 krum=0.591701 mkrum=REJECT tm_trim=0.6436 (lo 0.3212 / hi 0.3224) med_prov=0.1191 d_med=0.354907
    [shadow] C5 (A): norm=0.319693 krum=0.452235 mkrum=KEEP tm_trim=0.4794 (lo 0.2402 / hi 0.2391) med_prov=0.1786 d_med=0.255665
    [shadow] C6 (A): norm=0.319722 krum=0.452605 mkrum=KEEP tm_trim=0.4796 (lo 0.2399 / hi 0.2397) med_prov=0.1780 d_med=0.255839

⏱️  Overhead round 50 (wall-clock s): round 134.27 | broadcast 0.03 | prepare 0.00 | benign train 119.50 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.07 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.58 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.04s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 50 Results:
  Clean Accuracy: 0.9090
  ΔClean vs prev: -0.0023
  ΔClean vs best: -0.0023
  Global Loss: 0.8300

Results saved to: results/qwen_ag_news_rmp_alpha0p3_seed42069_shadow_results.json

================================================================================
📊 DETAILED EXPERIMENT STATISTICS FOR DATA COLLECTION
================================================================================

--------------------------------------------------------------------------------
1️⃣  GLOBAL ACCURACY (Per Round)
--------------------------------------------------------------------------------
Round    | Clean Accuracy  | Accuracy Change  
--------------------------------------------------------------------------------
1        | 0.456000        |         +0.000000
2        | 0.686667        |         +0.230667
3        | 0.776333        |         +0.089667
4        | 0.803667        |         +0.027333
5        | 0.826667        |         +0.023000
6        | 0.834000        |         +0.007333
7        | 0.848667        |         +0.014667
8        | 0.857333        |         +0.008667
9        | 0.876333        |         +0.019000
10       | 0.876333        |         +0.000000
11       | 0.888000        |         +0.011667
12       | 0.885667        |         -0.002333
13       | 0.889667        |         +0.004000
14       | 0.884333        |         -0.005333
15       | 0.886333        |         +0.002000
16       | 0.886667        |         +0.000333
17       | 0.889000        |         +0.002333
18       | 0.887667        |         -0.001333
19       | 0.887667        |         +0.000000
20       | 0.889667        |         +0.002000
21       | 0.883667        |         -0.006000
22       | 0.888000        |         +0.004333
23       | 0.892333        |         +0.004333
24       | 0.885000        |         -0.007333
25       | 0.895667        |         +0.010667
26       | 0.893667        |         -0.002000
27       | 0.893667        |         +0.000000
28       | 0.892667        |         -0.001000
29       | 0.900000        |         +0.007333
30       | 0.896667        |         -0.003333
31       | 0.896000        |         -0.000667
32       | 0.898000        |         +0.002000
33       | 0.904000        |         +0.006000
34       | 0.899333        |         -0.004667
35       | 0.900000        |         +0.000667
36       | 0.896333        |         -0.003667
37       | 0.901333        |         +0.005000
38       | 0.897333        |         -0.004000
39       | 0.902333        |         +0.005000
40       | 0.898667        |         -0.003667
41       | 0.907667        |         +0.009000
42       | 0.902333        |         -0.005333
43       | 0.900333        |         -0.002000
44       | 0.900667        |         +0.000333
45       | 0.899333        |         -0.001333
46       | 0.901000        |         +0.001667
47       | 0.905667        |         +0.004667
48       | 0.903000        |         -0.002667
49       | 0.911333        |         +0.008333
50       | 0.909000        |         -0.002333
--------------------------------------------------------------------------------
Summary: Initial=0.456000, Final=0.909000, Best=0.911333, Change=+0.453000

--------------------------------------------------------------------------------
2️⃣  COSINE SIMILARITY (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A) | Mean | Std
--------------------------------------------------------------------------------
1      | 0.564395       | 0.561311       | 0.529348       | 0.588887       | 0.573488       | 0.592902       | 0.592223       | 0.571794 | 0.021126
2      | 0.631519       | 0.581607       | 0.453262       | 0.602077       | 0.619239       | 0.613016       | 0.613028       | 0.587678 | 0.056713
3      | 0.517212       | 0.446339       | 0.372279       | 0.475227       | 0.506508       | 0.524446       | 0.524388       | 0.480914 | 0.051806
4      | 0.398304       | 0.333872       | 0.304610       | 0.336503       | 0.388169       | 0.433727       | 0.433666       | 0.375550 | 0.047409
5      | 0.295896       | 0.228410       | 0.218384       | 0.231343       | 0.284082       | 0.350172       | 0.350237       | 0.279789 | 0.052033
6      | 0.213526       | 0.148005       | 0.165300       | 0.176510       | 0.226485       | 0.297063       | 0.296836       | 0.217675 | 0.056004
7      | 0.156629       | 0.135489       | 0.108113       | 0.134634       | 0.178102       | 0.259223       | 0.259545       | 0.175962 | 0.056374
8      | 0.121155       | 0.105317       | 0.069976       | 0.117130       | 0.142916       | 0.233520       | 0.234235       | 0.146321 | 0.058967
9      | 0.133596       | 0.121890       | 0.088151       | 0.116656       | 0.155575       | 0.242973       | 0.243795       | 0.157520 | 0.057412
10     | 0.114793       | 0.102969       | 0.060663       | 0.112885       | 0.136981       | 0.229151       | 0.228568       | 0.140859 | 0.059561
11     | 0.108723       | 0.088012       | 0.026164       | 0.086653       | 0.130500       | 0.216148       | 0.216295       | 0.124642 | 0.064966
12     | 0.083119       | 0.081538       | 0.030161       | 0.080266       | 0.125334       | 0.208975       | 0.208539       | 0.116847 | 0.063475
13     | 0.099548       | 0.080285       | 0.035677       | 0.076383       | 0.121081       | 0.210800       | 0.211624       | 0.119342 | 0.062845
14     | 0.085942       | 0.084124       | 0.044930       | 0.070542       | 0.107877       | 0.207084       | 0.205941       | 0.115206 | 0.060337
15     | 0.083849       | 0.075761       | 0.030777       | 0.075908       | 0.105888       | 0.203476       | 0.204123       | 0.111398 | 0.061985
16     | 0.089046       | 0.070584       | 0.037234       | 0.068004       | 0.100076       | 0.202281       | 0.202724       | 0.109993 | 0.061253
17     | 0.086946       | 0.078384       | 0.044406       | 0.056994       | 0.096789       | 0.201405       | 0.202345       | 0.109610 | 0.060592
18     | 0.090812       | 0.069308       | 0.014998       | 0.054850       | 0.078965       | 0.193364       | 0.193333       | 0.099376 | 0.063424
19     | 0.073098       | 0.060058       | 0.021781       | 0.037673       | 0.071727       | 0.185783       | 0.185306       | 0.090775 | 0.062291
20     | 0.073368       | 0.058802       | 0.023520       | 0.015224       | 0.061768       | 0.179014       | 0.179160       | 0.084408 | 0.062919
21     | 0.064583       | 0.068048       | 0.034494       | 0.043472       | 0.070601       | 0.187666       | 0.187849       | 0.093816 | 0.060664
22     | 0.060157       | 0.052683       | 0.037642       | 0.021886       | 0.073738       | 0.181924       | 0.182088       | 0.087160 | 0.061878
23     | 0.052302       | 0.050276       | 0.028694       | 0.022506       | 0.066995       | 0.177724       | 0.177397       | 0.082271 | 0.061827
24     | 0.045114       | 0.063181       | 0.036164       | 0.017860       | 0.060958       | 0.177816       | 0.177649       | 0.082677 | 0.061758
25     | 0.070048       | 0.064985       | 0.030943       | 0.035328       | 0.061478       | 0.186175       | 0.185914       | 0.090696 | 0.061829
26     | 0.058156       | 0.065671       | 0.032560       | 0.028458       | 0.063803       | 0.182200       | 0.182530       | 0.087625 | 0.061414
27     | 0.065952       | 0.052139       | 0.040574       | 0.033064       | 0.076077       | 0.185382       | 0.185403       | 0.091227 | 0.061038
28     | 0.064454       | 0.074449       | 0.036650       | 0.010336       | 0.068860       | 0.183179       | 0.184016       | 0.088849 | 0.063297
29     | 0.052095       | 0.050383       | 0.038632       | 0.020803       | 0.063565       | 0.179245       | 0.179733       | 0.083494 | 0.061936
30     | 0.036763       | 0.066707       | 0.032038       | 0.034469       | 0.063030       | 0.179756       | 0.179594       | 0.084622 | 0.061445
31     | 0.058802       | 0.052268       | 0.023490       | 0.010348       | 0.041473       | 0.172796       | 0.171703       | 0.075840 | 0.062845
32     | 0.054665       | 0.059812       | 0.039476       | 0.023025       | 0.060180       | 0.180381       | 0.180625       | 0.085452 | 0.061324
33     | 0.059922       | 0.059288       | 0.046653       | 0.007226       | 0.062844       | 0.180005       | 0.180410       | 0.085193 | 0.062597
34     | 0.053071       | 0.065731       | 0.026717       | 0.025715       | 0.058604       | 0.180152       | 0.180183       | 0.084311 | 0.062232
35     | 0.057386       | 0.059716       | 0.039652       | 0.026979       | 0.069267       | 0.182902       | 0.183629       | 0.088504 | 0.061294
36     | 0.047151       | 0.069234       | 0.065516       | 0.041401       | 0.066331       | 0.188529       | 0.188778       | 0.095277 | 0.059832
37     | 0.052911       | 0.067648       | 0.041750       | 0.024521       | 0.077742       | 0.185065       | 0.185693       | 0.090761 | 0.061912
38     | 0.057404       | 0.072393       | 0.029297       | 0.019572       | 0.061060       | 0.179980       | 0.180275       | 0.085712 | 0.062074
39     | 0.054356       | 0.064060       | 0.049733       | 0.025020       | 0.069642       | 0.186197       | 0.185582       | 0.090656 | 0.061631
40     | 0.063483       | 0.067361       | 0.055145       | 0.047403       | 0.071204       | 0.191009       | 0.191314       | 0.098131 | 0.059285
41     | 0.073109       | 0.062370       | 0.049062       | 0.023401       | 0.063337       | 0.186219       | 0.186467       | 0.091995 | 0.061420
42     | 0.053483       | 0.062832       | 0.045597       | 0.039025       | 0.064248       | 0.184753       | 0.185322       | 0.090752 | 0.060197
43     | 0.069007       | 0.083662       | 0.059892       | 0.033440       | 0.057340       | 0.189229       | 0.189753       | 0.097475 | 0.059832
44     | 0.060864       | 0.055084       | 0.048215       | 0.023322       | 0.078129       | 0.185277       | 0.185199       | 0.090870 | 0.061570
45     | 0.067015       | 0.066970       | 0.050381       | 0.027580       | 0.075289       | 0.190186       | 0.189852       | 0.095325 | 0.061587
46     | 0.045021       | 0.055713       | 0.045960       | 0.036842       | 0.063240       | 0.180882       | 0.181291       | 0.086993 | 0.060013
47     | 0.061085       | 0.065778       | 0.067234       | 0.039001       | 0.069240       | 0.191690       | 0.191345       | 0.097911 | 0.059936
48     | 0.053221       | 0.045938       | 0.028725       | 0.038323       | 0.074972       | 0.182482       | 0.182376       | 0.086577 | 0.062048
49     | 0.063778       | 0.080561       | 0.080805       | 0.055830       | 0.066225       | 0.197090       | 0.197227       | 0.105931 | 0.058289
50     | 0.053232       | 0.046823       | 0.034016       | 0.034057       | 0.076237       | 0.183473       | 0.183034       | 0.087267 | 0.062117
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
2b. EUCLIDEAN DISTANCE (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A) | Mean | Std
--------------------------------------------------------------------------------
1      | 0.748197       | 0.772142       | 0.808414       | 0.791900       | 0.781588       | 0.558498       | 0.707719       | 0.738351 | 0.079435
2      | 0.539058       | 0.587593       | 0.687017       | 0.577017       | 0.533449       | 0.421615       | 0.532438       | 0.554027 | 0.073667
3      | 0.472324       | 0.457791       | 0.510549       | 0.484660       | 0.475037       | 0.342946       | 0.435001       | 0.454044 | 0.050177
4      | 0.413323       | 0.377083       | 0.401287       | 0.441631       | 0.441646       | 0.296011       | 0.376277       | 0.392465 | 0.046523
5      | 0.412929       | 0.351386       | 0.369217       | 0.429866       | 0.422274       | 0.283070       | 0.360311       | 0.375579 | 0.047718
6      | 0.407238       | 0.338550       | 0.350835       | 0.399998       | 0.396758       | 0.270381       | 0.343471       | 0.358176 | 0.044734
7      | 0.387987       | 0.323725       | 0.343472       | 0.404621       | 0.387316       | 0.263633       | 0.335018       | 0.349396 | 0.045092
8      | 0.376639       | 0.320734       | 0.341335       | 0.400985       | 0.404490       | 0.263568       | 0.334926       | 0.348954 | 0.046136
9      | 0.389607       | 0.322926       | 0.344110       | 0.404425       | 0.403280       | 0.266054       | 0.338316       | 0.352674 | 0.046707
10     | 0.379934       | 0.315274       | 0.334547       | 0.400973       | 0.389743       | 0.259749       | 0.331010       | 0.344461 | 0.045996
11     | 0.385132       | 0.318285       | 0.344774       | 0.393240       | 0.377116       | 0.259028       | 0.329745       | 0.343903 | 0.043586
12     | 0.362111       | 0.303648       | 0.329280       | 0.389864       | 0.373323       | 0.250645       | 0.319071       | 0.332563 | 0.044009
13     | 0.365007       | 0.303988       | 0.328568       | 0.378174       | 0.372148       | 0.249071       | 0.316672       | 0.330518 | 0.042639
14     | 0.370018       | 0.302487       | 0.322298       | 0.369657       | 0.363964       | 0.246342       | 0.314205       | 0.326996 | 0.041967
15     | 0.364187       | 0.301335       | 0.318325       | 0.372824       | 0.346688       | 0.243332       | 0.308526       | 0.322174 | 0.041028
16     | 0.357892       | 0.306673       | 0.318146       | 0.370396       | 0.364279       | 0.244924       | 0.311463       | 0.324825 | 0.040819
17     | 0.350359       | 0.298398       | 0.309801       | 0.358941       | 0.348573       | 0.237583       | 0.302268       | 0.315132 | 0.039218
18     | 0.357581       | 0.305212       | 0.319872       | 0.359893       | 0.354650       | 0.241856       | 0.307965       | 0.321004 | 0.039037
19     | 0.342271       | 0.295312       | 0.316149       | 0.354513       | 0.351035       | 0.236103       | 0.300549       | 0.313705 | 0.038571
20     | 0.348097       | 0.287332       | 0.307734       | 0.346286       | 0.347793       | 0.233554       | 0.297101       | 0.309700 | 0.039143
21     | 0.345093       | 0.290498       | 0.306115       | 0.334632       | 0.340805       | 0.230292       | 0.292890       | 0.305761 | 0.037231
22     | 0.330489       | 0.285262       | 0.297019       | 0.339889       | 0.334441       | 0.226313       | 0.287700       | 0.300159 | 0.036866
23     | 0.333355       | 0.281319       | 0.302185       | 0.335887       | 0.322029       | 0.224207       | 0.285471       | 0.297779 | 0.036175
24     | 0.320917       | 0.284657       | 0.294759       | 0.322141       | 0.324028       | 0.220342       | 0.280145       | 0.292427 | 0.034030
25     | 0.315972       | 0.282292       | 0.294086       | 0.315312       | 0.316733       | 0.216762       | 0.276028       | 0.288169 | 0.033040
26     | 0.321936       | 0.281876       | 0.295135       | 0.326829       | 0.311727       | 0.218935       | 0.278746       | 0.290741 | 0.034046
27     | 0.312058       | 0.278045       | 0.295483       | 0.335030       | 0.312720       | 0.218437       | 0.278116       | 0.289984 | 0.034777
28     | 0.309639       | 0.273015       | 0.288276       | 0.316144       | 0.306714       | 0.212801       | 0.270253       | 0.282406 | 0.032920
29     | 0.307600       | 0.273171       | 0.291005       | 0.314124       | 0.306085       | 0.212230       | 0.269937       | 0.282022 | 0.032601
30     | 0.312785       | 0.273274       | 0.286593       | 0.307209       | 0.330422       | 0.214990       | 0.273768       | 0.285577 | 0.034834
31     | 0.303933       | 0.274648       | 0.298217       | 0.306234       | 0.301925       | 0.211666       | 0.268975       | 0.280800 | 0.031371
32     | 0.305260       | 0.270836       | 0.285040       | 0.306192       | 0.325071       | 0.212623       | 0.270581       | 0.282229 | 0.033930
33     | 0.311618       | 0.274775       | 0.285830       | 0.301599       | 0.333131       | 0.214601       | 0.273270       | 0.284975 | 0.034846
34     | 0.300869       | 0.265726       | 0.276455       | 0.284133       | 0.304939       | 0.203657       | 0.259334       | 0.270731 | 0.031498
35     | 0.300310       | 0.273627       | 0.289165       | 0.320479       | 0.306555       | 0.212101       | 0.270072       | 0.281759 | 0.032881
36     | 0.308743       | 0.277807       | 0.285685       | 0.310810       | 0.316902       | 0.213834       | 0.271780       | 0.283652 | 0.032791
37     | 0.307524       | 0.274809       | 0.292538       | 0.296617       | 0.334466       | 0.214648       | 0.273398       | 0.284857 | 0.034504
38     | 0.324734       | 0.272500       | 0.293131       | 0.325297       | 0.335977       | 0.220983       | 0.280900       | 0.293360 | 0.037128
39     | 0.287522       | 0.273252       | 0.277131       | 0.292633       | 0.293737       | 0.202564       | 0.258013       | 0.269265 | 0.029596
40     | 0.306444       | 0.282978       | 0.282121       | 0.324938       | 0.322213       | 0.216299       | 0.275184       | 0.287168 | 0.034300
41     | 0.310857       | 0.273191       | 0.285517       | 0.305982       | 0.321228       | 0.213006       | 0.270823       | 0.282943 | 0.033627
42     | 0.307522       | 0.282055       | 0.292102       | 0.330674       | 0.318098       | 0.218167       | 0.277321       | 0.289420 | 0.034094
43     | 0.316092       | 0.275074       | 0.290840       | 0.335993       | 0.341169       | 0.222486       | 0.282841       | 0.294928 | 0.037942
44     | 0.315956       | 0.286454       | 0.290884       | 0.317376       | 0.343052       | 0.221262       | 0.281506       | 0.293784 | 0.035753
45     | 0.295686       | 0.276661       | 0.281609       | 0.299724       | 0.313435       | 0.208926       | 0.265363       | 0.277344 | 0.031584
46     | 0.301878       | 0.286749       | 0.289305       | 0.342318       | 0.327461       | 0.220750       | 0.280818       | 0.292754 | 0.036094
47     | 0.319371       | 0.281347       | 0.280942       | 0.307750       | 0.304391       | 0.212643       | 0.270747       | 0.282456 | 0.032729
48     | 0.311113       | 0.286869       | 0.294028       | 0.302752       | 0.340008       | 0.218701       | 0.278045       | 0.290217 | 0.034561
49     | 0.300473       | 0.284566       | 0.285991       | 0.347778       | 0.316081       | 0.218754       | 0.278417       | 0.290294 | 0.036613
50     | 0.314093       | 0.287047       | 0.291809       | 0.298667       | 0.324168       | 0.215815       | 0.274586       | 0.286598 | 0.032722
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
2c. GLOBAL LOSS (Per Round)
--------------------------------------------------------------------------------
Round    | Global Loss    
--------------------------------------------------------------------------------
1        | 1.984382       
2        | 0.981970       
3        | 0.650285       
4        | 0.550737       
5        | 0.518870       
6        | 0.486263       
7        | 0.458532       
8        | 0.456924       
9        | 0.405705       
10       | 0.405310       
11       | 0.384544       
12       | 0.408299       
13       | 0.408592       
14       | 0.430339       
15       | 0.454369       
16       | 0.458663       
17       | 0.455332       
18       | 0.509548       
19       | 0.529315       
20       | 0.541540       
21       | 0.586228       
22       | 0.597276       
23       | 0.609045       
24       | 0.643946       
25       | 0.596709       
26       | 0.656820       
27       | 0.678839       
28       | 0.687015       
29       | 0.637083       
30       | 0.696177       
31       | 0.727422       
32       | 0.708280       
33       | 0.658955       
34       | 0.750789       
35       | 0.765573       
36       | 0.744218       
37       | 0.755798       
38       | 0.802848       
39       | 0.776872       
40       | 0.798169       
41       | 0.772955       
42       | 0.823591       
43       | 0.833587       
44       | 0.799561       
45       | 0.824938       
46       | 0.830569       
47       | 0.768381       
48       | 0.855645       
49       | 0.768106       
50       | 0.829971       
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
3️⃣  LOCAL ACCURACY (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A) | Mean | Std
--------------------------------------------------------------------------------
1      | 0.592391       | 0.222826       | 0.326087       | 0.592391       | 0.445652       | 0.222826       | 0.222826       | 0.375000 | 0.156467
2      | 0.766304       | 0.559783       | 0.434783       | 0.663043       | 0.527174       | 0.418478       | 0.418478       | 0.541149 | 0.123927
3      | 0.831522       | 0.684783       | 0.581522       | 0.668478       | 0.581522       | 0.657609       | 0.657609       | 0.666149 | 0.077616
4      | 0.864130       | 0.782609       | 0.619565       | 0.668478       | 0.619565       | 0.744565       | 0.744565       | 0.720497 | 0.083433
5      | 0.864130       | 0.809783       | 0.630435       | 0.668478       | 0.630435       | 0.760870       | 0.760870       | 0.732143 | 0.084381
6      | 0.869565       | 0.793478       | 0.668478       | 0.673913       | 0.652174       | 0.777174       | 0.777174       | 0.744565 | 0.075082
7      | 0.869565       | 0.777174       | 0.646739       | 0.673913       | 0.668478       | 0.793478       | 0.793478       | 0.746118 | 0.077282
8      | 0.853261       | 0.847826       | 0.717391       | 0.668478       | 0.684783       | 0.820652       | 0.820652       | 0.773292 | 0.074047
9      | 0.864130       | 0.836957       | 0.695652       | 0.684783       | 0.695652       | 0.831522       | 0.831522       | 0.777174 | 0.074518
10     | 0.875000       | 0.847826       | 0.706522       | 0.679348       | 0.717391       | 0.853261       | 0.853261       | 0.790373 | 0.078428
11     | 0.880435       | 0.815217       | 0.701087       | 0.679348       | 0.739130       | 0.847826       | 0.847826       | 0.787267 | 0.073860
12     | 0.858696       | 0.875000       | 0.766304       | 0.679348       | 0.744565       | 0.864130       | 0.864130       | 0.807453 | 0.071386
13     | 0.875000       | 0.896739       | 0.766304       | 0.684783       | 0.739130       | 0.880435       | 0.880435       | 0.817547 | 0.079177
14     | 0.869565       | 0.847826       | 0.777174       | 0.684783       | 0.722826       | 0.896739       | 0.896739       | 0.813665 | 0.079542
15     | 0.875000       | 0.858696       | 0.793478       | 0.684783       | 0.755435       | 0.885870       | 0.885870       | 0.819876 | 0.072067
16     | 0.875000       | 0.885870       | 0.771739       | 0.684783       | 0.711957       | 0.885870       | 0.885870       | 0.814441 | 0.082904
17     | 0.885870       | 0.875000       | 0.809783       | 0.684783       | 0.760870       | 0.875000       | 0.875000       | 0.823758 | 0.070912
18     | 0.875000       | 0.869565       | 0.793478       | 0.684783       | 0.755435       | 0.880435       | 0.880435       | 0.819876 | 0.071656
19     | 0.885870       | 0.875000       | 0.788043       | 0.673913       | 0.755435       | 0.869565       | 0.869565       | 0.816770 | 0.074388
20     | 0.885870       | 0.885870       | 0.798913       | 0.690217       | 0.793478       | 0.869565       | 0.869565       | 0.827640 | 0.066734
21     | 0.864130       | 0.853261       | 0.798913       | 0.695652       | 0.744565       | 0.885870       | 0.885870       | 0.818323 | 0.068982
22     | 0.880435       | 0.885870       | 0.804348       | 0.711957       | 0.744565       | 0.858696       | 0.858696       | 0.820652 | 0.063910
23     | 0.880435       | 0.847826       | 0.793478       | 0.695652       | 0.788043       | 0.864130       | 0.864130       | 0.819099 | 0.060360
24     | 0.880435       | 0.820652       | 0.793478       | 0.701087       | 0.750000       | 0.858696       | 0.858696       | 0.809006 | 0.060410
25     | 0.880435       | 0.858696       | 0.793478       | 0.739130       | 0.777174       | 0.858696       | 0.858696       | 0.823758 | 0.049458
26     | 0.875000       | 0.847826       | 0.804348       | 0.711957       | 0.771739       | 0.858696       | 0.858696       | 0.818323 | 0.054801
27     | 0.880435       | 0.864130       | 0.815217       | 0.717391       | 0.750000       | 0.864130       | 0.864130       | 0.822205 | 0.059656
28     | 0.880435       | 0.836957       | 0.782609       | 0.701087       | 0.798913       | 0.869565       | 0.869565       | 0.819876 | 0.059565
29     | 0.880435       | 0.891304       | 0.798913       | 0.728261       | 0.771739       | 0.864130       | 0.864130       | 0.828416 | 0.057726
30     | 0.891304       | 0.847826       | 0.815217       | 0.739130       | 0.777174       | 0.875000       | 0.875000       | 0.831522 | 0.052612
31     | 0.885870       | 0.864130       | 0.777174       | 0.706522       | 0.760870       | 0.869565       | 0.869565       | 0.819099 | 0.064809
32     | 0.891304       | 0.853261       | 0.836957       | 0.760870       | 0.793478       | 0.869565       | 0.869565       | 0.839286 | 0.043074
33     | 0.891304       | 0.858696       | 0.820652       | 0.750000       | 0.820652       | 0.875000       | 0.875000       | 0.841615 | 0.045138
34     | 0.896739       | 0.853261       | 0.809783       | 0.739130       | 0.793478       | 0.891304       | 0.891304       | 0.839286 | 0.055944
35     | 0.896739       | 0.880435       | 0.793478       | 0.722826       | 0.826087       | 0.880435       | 0.880435       | 0.840062 | 0.058812
36     | 0.891304       | 0.842391       | 0.809783       | 0.744565       | 0.809783       | 0.875000       | 0.875000       | 0.835404 | 0.047620
37     | 0.891304       | 0.842391       | 0.793478       | 0.750000       | 0.755435       | 0.864130       | 0.864130       | 0.822981 | 0.052359
38     | 0.891304       | 0.875000       | 0.809783       | 0.728261       | 0.771739       | 0.869565       | 0.869565       | 0.830745 | 0.057401
39     | 0.885870       | 0.847826       | 0.826087       | 0.750000       | 0.842391       | 0.869565       | 0.869565       | 0.841615 | 0.041738
40     | 0.885870       | 0.820652       | 0.831522       | 0.782609       | 0.739130       | 0.880435       | 0.880435       | 0.831522 | 0.051804
41     | 0.902174       | 0.880435       | 0.788043       | 0.750000       | 0.815217       | 0.869565       | 0.869565       | 0.839286 | 0.051629
42     | 0.891304       | 0.836957       | 0.804348       | 0.771739       | 0.820652       | 0.885870       | 0.885870       | 0.842391 | 0.043284
43     | 0.880435       | 0.880435       | 0.815217       | 0.739130       | 0.760870       | 0.891304       | 0.891304       | 0.836957 | 0.060380
44     | 0.891304       | 0.875000       | 0.826087       | 0.750000       | 0.788043       | 0.875000       | 0.875000       | 0.840062 | 0.049714
45     | 0.875000       | 0.875000       | 0.820652       | 0.744565       | 0.847826       | 0.880435       | 0.880435       | 0.846273 | 0.046272
46     | 0.885870       | 0.864130       | 0.831522       | 0.766304       | 0.836957       | 0.864130       | 0.864130       | 0.844720 | 0.036267
47     | 0.885870       | 0.858696       | 0.804348       | 0.804348       | 0.842391       | 0.880435       | 0.880435       | 0.850932 | 0.032590
48     | 0.902174       | 0.853261       | 0.820652       | 0.788043       | 0.820652       | 0.880435       | 0.880435       | 0.849379 | 0.038067
49     | 0.896739       | 0.836957       | 0.804348       | 0.798913       | 0.842391       | 0.885870       | 0.885870       | 0.850155 | 0.037186
50     | 0.875000       | 0.853261       | 0.804348       | 0.793478       | 0.831522       | 0.891304       | 0.891304       | 0.848602 | 0.037137
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
4️⃣  SHADOW KRUM SCORE (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A) | Selected | SelIsAtk
--------------------------------------------------------------------------------
1      | 3.199984       | 1.950418       | 2.038867       | 3.472590       | 3.289043       | 2.953588       | 2.954827       | 1        | 0       
2      | 1.859704       | 1.174375       | 1.377192       | 1.988635       | 1.915282       | 1.733450       | 1.730442       | 1        | 0       
3      | 1.400235       | 0.812223       | 0.892518       | 1.445445       | 1.402725       | 1.129692       | 1.132291       | 1        | 0       
4      | 0.992515       | 0.627507       | 0.656404       | 1.098556       | 1.100318       | 0.824447       | 0.824171       | 1        | 0       
5      | 0.942830       | 0.578174       | 0.597401       | 1.008450       | 0.982801       | 0.747070       | 0.747947       | 1        | 0       
6      | 0.902211       | 0.539099       | 0.551331       | 0.884287       | 0.875283       | 0.683439       | 0.681850       | 1        | 0       
7      | 0.812476       | 0.507022       | 0.527452       | 0.896449       | 0.819918       | 0.648341       | 0.647829       | 1        | 0       
8      | 0.755355       | 0.506555       | 0.527286       | 0.880694       | 0.887229       | 0.645077       | 0.644919       | 1        | 0       
9      | 0.807713       | 0.518470       | 0.539608       | 0.885021       | 0.883385       | 0.657690       | 0.657904       | 1        | 0       
10     | 0.761259       | 0.498842       | 0.517519       | 0.864670       | 0.829021       | 0.628521       | 0.628903       | 1        | 0       
11     | 0.792800       | 0.520438       | 0.546750       | 0.840560       | 0.796295       | 0.634782       | 0.634695       | 1        | 0       
12     | 0.697551       | 0.480427       | 0.504861       | 0.812527       | 0.761522       | 0.589675       | 0.590504       | 1        | 0       
13     | 0.705361       | 0.470612       | 0.494667       | 0.775833       | 0.765475       | 0.582773       | 0.582725       | 1        | 0       
14     | 0.721033       | 0.468625       | 0.486912       | 0.744032       | 0.734349       | 0.571793       | 0.572267       | 1        | 0       
15     | 0.705368       | 0.457026       | 0.472521       | 0.759763       | 0.671241       | 0.557505       | 0.555749       | 1        | 0       
16     | 0.693490       | 0.465912       | 0.475531       | 0.749464       | 0.727223       | 0.565122       | 0.564251       | 1        | 0       
17     | 0.661174       | 0.448429       | 0.458296       | 0.703572       | 0.675297       | 0.534026       | 0.533784       | 1        | 0       
18     | 0.690070       | 0.463644       | 0.477078       | 0.721956       | 0.700049       | 0.555461       | 0.556316       | 1        | 0       
19     | 0.633468       | 0.444126       | 0.463139       | 0.692688       | 0.686528       | 0.530821       | 0.529757       | 1        | 0       
20     | 0.649927       | 0.424062       | 0.442205       | 0.656464       | 0.667747       | 0.515079       | 0.513904       | 1        | 0       
21     | 0.642786       | 0.416814       | 0.430429       | 0.628994       | 0.648642       | 0.503470       | 0.503507       | 1        | 0       
22     | 0.587891       | 0.410888       | 0.420933       | 0.638166       | 0.623506       | 0.485569       | 0.485980       | 1        | 0       
23     | 0.605629       | 0.403954       | 0.421733       | 0.618082       | 0.592201       | 0.480484       | 0.480769       | 1        | 0       
24     | 0.570869       | 0.398799       | 0.406953       | 0.587051       | 0.598472       | 0.465739       | 0.465608       | 1        | 0       
25     | 0.552439       | 0.406914       | 0.416518       | 0.562206       | 0.565214       | 0.456928       | 0.457541       | 1        | 0       
26     | 0.560362       | 0.400993       | 0.411590       | 0.599298       | 0.567319       | 0.461753       | 0.462011       | 1        | 0       
27     | 0.536999       | 0.391283       | 0.406591       | 0.620189       | 0.558895       | 0.458560       | 0.458254       | 1        | 0       
28     | 0.529597       | 0.382130       | 0.394618       | 0.552226       | 0.540261       | 0.436841       | 0.436706       | 1        | 0       
29     | 0.523676       | 0.383575       | 0.398528       | 0.555200       | 0.536088       | 0.436966       | 0.436981       | 1        | 0       
30     | 0.535652       | 0.381499       | 0.391978       | 0.527443       | 0.604302       | 0.442644       | 0.443317       | 1        | 0       
31     | 0.518243       | 0.382299       | 0.402938       | 0.542272       | 0.533748       | 0.437439       | 0.437148       | 1        | 0       
32     | 0.512601       | 0.371130       | 0.382501       | 0.531230       | 0.584693       | 0.433342       | 0.433477       | 1        | 0       
33     | 0.533799       | 0.378498       | 0.387272       | 0.521257       | 0.610856       | 0.441621       | 0.441677       | 1        | 0       
34     | 0.498649       | 0.358046       | 0.365633       | 0.468194       | 0.524931       | 0.403604       | 0.403017       | 1        | 0       
35     | 0.505388       | 0.377172       | 0.389820       | 0.571235       | 0.541564       | 0.434763       | 0.434910       | 1        | 0       
36     | 0.528801       | 0.381378       | 0.386946       | 0.552228       | 0.571674       | 0.439577       | 0.439742       | 1        | 0       
37     | 0.528210       | 0.382193       | 0.396971       | 0.508224       | 0.620881       | 0.444522       | 0.444999       | 1        | 0       
38     | 0.561852       | 0.387228       | 0.405006       | 0.582217       | 0.621335       | 0.463059       | 0.462243       | 1        | 0       
39     | 0.472619       | 0.362031       | 0.364378       | 0.498740       | 0.501064       | 0.402708       | 0.402403       | 1        | 0       
40     | 0.511523       | 0.386610       | 0.384608       | 0.593021       | 0.587783       | 0.447321       | 0.447386       | 2        | 0       
41     | 0.533994       | 0.370757       | 0.380757       | 0.529504       | 0.578330       | 0.434339       | 0.434620       | 1        | 0       
42     | 0.531560       | 0.388509       | 0.396287       | 0.610269       | 0.579939       | 0.456120       | 0.455661       | 1        | 0       
43     | 0.544970       | 0.382740       | 0.395805       | 0.615575       | 0.634868       | 0.465426       | 0.465211       | 1        | 0       
44     | 0.554837       | 0.395460       | 0.398404       | 0.572331       | 0.647577       | 0.466968       | 0.466161       | 1        | 0       
45     | 0.493726       | 0.374339       | 0.377356       | 0.513430       | 0.559319       | 0.423223       | 0.422801       | 1        | 0       
46     | 0.518641       | 0.395067       | 0.396032       | 0.645877       | 0.604796       | 0.463568       | 0.463305       | 1        | 0       
47     | 0.553657       | 0.387473       | 0.385736       | 0.543742       | 0.533690       | 0.437589       | 0.437171       | 2        | 0       
48     | 0.540115       | 0.400874       | 0.406049       | 0.536603       | 0.648928       | 0.460992       | 0.461559       | 1        | 0       
49     | 0.506244       | 0.391703       | 0.391537       | 0.665400       | 0.563849       | 0.455243       | 0.456160       | 2        | 0       
50     | 0.551942       | 0.398700       | 0.401722       | 0.532650       | 0.591701       | 0.452235       | 0.452605       | 1        | 0       
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
4b. SHADOW MULTI-KRUM REJECTED (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A)
--------------------------------------------------------------------------------
1      | 0              | 0              | 0              | 1              | 1              | 0              | 0             
2      | 0              | 0              | 0              | 1              | 1              | 0              | 0             
3      | 0              | 0              | 0              | 1              | 1              | 0              | 0             
4      | 0              | 0              | 0              | 1              | 1              | 0              | 0             
5      | 0              | 0              | 0              | 1              | 1              | 0              | 0             
6      | 1              | 0              | 0              | 1              | 0              | 0              | 0             
7      | 0              | 0              | 0              | 1              | 1              | 0              | 0             
8      | 0              | 0              | 0              | 1              | 1              | 0              | 0             
9      | 0              | 0              | 0              | 1              | 1              | 0              | 0             
10     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
11     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
12     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
13     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
14     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
15     | 1              | 0              | 0              | 1              | 0              | 0              | 0             
16     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
17     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
18     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
19     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
20     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
21     | 1              | 0              | 0              | 0              | 1              | 0              | 0             
22     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
23     | 1              | 0              | 0              | 1              | 0              | 0              | 0             
24     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
25     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
26     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
27     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
28     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
29     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
30     | 1              | 0              | 0              | 0              | 1              | 0              | 0             
31     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
32     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
33     | 1              | 0              | 0              | 0              | 1              | 0              | 0             
34     | 1              | 0              | 0              | 0              | 1              | 0              | 0             
35     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
36     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
37     | 1              | 0              | 0              | 0              | 1              | 0              | 0             
38     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
39     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
40     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
41     | 1              | 0              | 0              | 0              | 1              | 0              | 0             
42     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
43     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
44     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
45     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
46     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
47     | 1              | 0              | 0              | 1              | 0              | 0              | 0             
48     | 1              | 0              | 0              | 0              | 1              | 0              | 0             
49     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
50     | 1              | 0              | 0              | 0              | 1              | 0              | 0             
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
4c. SHADOW TRIMMED-MEAN TRIM FRACTION (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A)
--------------------------------------------------------------------------------
1      | 0.647909       | 0.525736       | 0.568077       | 0.728960       | 0.609444       | 0.459918       | 0.459955      
2      | 0.645861       | 0.524887       | 0.625861       | 0.677426       | 0.593216       | 0.466522       | 0.466226      
3      | 0.648185       | 0.517146       | 0.572903       | 0.654298       | 0.643041       | 0.482042       | 0.482385      
4      | 0.635933       | 0.506576       | 0.542449       | 0.666282       | 0.665694       | 0.491579       | 0.491487      
5      | 0.654192       | 0.494529       | 0.534559       | 0.669376       | 0.656467       | 0.494940       | 0.495938      
6      | 0.663954       | 0.506698       | 0.534440       | 0.657983       | 0.647607       | 0.494705       | 0.494613      
7      | 0.647437       | 0.490138       | 0.538208       | 0.681568       | 0.649340       | 0.497252       | 0.496057      
8      | 0.626231       | 0.487308       | 0.540464       | 0.681442       | 0.668748       | 0.498521       | 0.497286      
9      | 0.638994       | 0.487972       | 0.537034       | 0.675946       | 0.665600       | 0.497321       | 0.497133      
10     | 0.640054       | 0.492564       | 0.536142       | 0.680536       | 0.656723       | 0.497518       | 0.496463      
11     | 0.642160       | 0.502936       | 0.547638       | 0.675121       | 0.640487       | 0.495565       | 0.496094      
12     | 0.630693       | 0.488332       | 0.549626       | 0.688871       | 0.649305       | 0.496368       | 0.496805      
13     | 0.636168       | 0.492116       | 0.549136       | 0.673783       | 0.655995       | 0.495654       | 0.497149      
14     | 0.650679       | 0.503889       | 0.542287       | 0.666682       | 0.645505       | 0.495359       | 0.495600      
15     | 0.650364       | 0.506125       | 0.542995       | 0.678437       | 0.631635       | 0.495987       | 0.494458      
16     | 0.641052       | 0.507990       | 0.542200       | 0.669923       | 0.649687       | 0.495111       | 0.494036      
17     | 0.639308       | 0.512642       | 0.541784       | 0.669200       | 0.647794       | 0.494801       | 0.494470      
18     | 0.639922       | 0.518495       | 0.547707       | 0.661134       | 0.644484       | 0.494045       | 0.494213      
19     | 0.628803       | 0.508315       | 0.557193       | 0.667732       | 0.649527       | 0.494225       | 0.494206      
20     | 0.645488       | 0.499989       | 0.549470       | 0.663211       | 0.650102       | 0.495395       | 0.496345      
21     | 0.647134       | 0.511545       | 0.552681       | 0.650312       | 0.650568       | 0.493356       | 0.494403      
22     | 0.634722       | 0.515103       | 0.550065       | 0.665814       | 0.646648       | 0.493942       | 0.493705      
23     | 0.642238       | 0.503769       | 0.564387       | 0.667574       | 0.634189       | 0.493308       | 0.494535      
24     | 0.634628       | 0.525723       | 0.556325       | 0.654136       | 0.647844       | 0.490582       | 0.490761      
25     | 0.631985       | 0.535713       | 0.563759       | 0.647364       | 0.640398       | 0.489891       | 0.490890      
26     | 0.631870       | 0.526728       | 0.563224       | 0.668519       | 0.628585       | 0.490584       | 0.490492      
27     | 0.623690       | 0.514513       | 0.562671       | 0.684563       | 0.633593       | 0.490512       | 0.490457      
28     | 0.635530       | 0.521943       | 0.561619       | 0.667818       | 0.632395       | 0.490763       | 0.489932      
29     | 0.632505       | 0.522562       | 0.573139       | 0.661830       | 0.631560       | 0.489818       | 0.488586      
30     | 0.632401       | 0.515246       | 0.553190       | 0.652096       | 0.668219       | 0.489181       | 0.489667      
31     | 0.625613       | 0.521141       | 0.584003       | 0.667754       | 0.630102       | 0.485892       | 0.485496      
32     | 0.632505       | 0.517953       | 0.555966       | 0.652297       | 0.663442       | 0.489113       | 0.488725      
33     | 0.636911       | 0.517642       | 0.557916       | 0.641579       | 0.668626       | 0.488400       | 0.488926      
34     | 0.636882       | 0.525193       | 0.561804       | 0.649193       | 0.653411       | 0.486790       | 0.486726      
35     | 0.622476       | 0.523630       | 0.563261       | 0.680866       | 0.632756       | 0.488057       | 0.488952      
36     | 0.630123       | 0.526750       | 0.557914       | 0.663549       | 0.647931       | 0.487310       | 0.486423      
37     | 0.630221       | 0.519658       | 0.565014       | 0.634853       | 0.673874       | 0.487903       | 0.488478      
38     | 0.639303       | 0.501743       | 0.553215       | 0.663668       | 0.660114       | 0.490922       | 0.491035      
39     | 0.629416       | 0.547935       | 0.562177       | 0.658524       | 0.632038       | 0.484486       | 0.485424      
40     | 0.628306       | 0.535012       | 0.537296       | 0.661862       | 0.663602       | 0.487148       | 0.486775      
41     | 0.644807       | 0.517569       | 0.558569       | 0.653836       | 0.650251       | 0.488003       | 0.486965      
42     | 0.622974       | 0.530590       | 0.558585       | 0.675574       | 0.638415       | 0.487039       | 0.486824      
43     | 0.629213       | 0.499670       | 0.545486       | 0.669643       | 0.672581       | 0.491608       | 0.491799      
44     | 0.629531       | 0.522045       | 0.541877       | 0.666485       | 0.673162       | 0.483586       | 0.483314      
45     | 0.622695       | 0.540983       | 0.559546       | 0.660024       | 0.647753       | 0.484003       | 0.484997      
46     | 0.613275       | 0.534666       | 0.545498       | 0.679814       | 0.649342       | 0.488790       | 0.488616      
47     | 0.646715       | 0.543039       | 0.550650       | 0.656895       | 0.632953       | 0.485057       | 0.484691      
48     | 0.631186       | 0.535430       | 0.552079       | 0.641221       | 0.673870       | 0.482996       | 0.483218      
49     | 0.615944       | 0.538609       | 0.543419       | 0.685341       | 0.642690       | 0.487269       | 0.486727      
50     | 0.641935       | 0.552815       | 0.553869       | 0.648881       | 0.643597       | 0.479352       | 0.479553      
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
4d. SHADOW MEDIAN PROVIDER FRACTION (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A)
--------------------------------------------------------------------------------
1      | 0.108703       | 0.151791       | 0.144158       | 0.079668       | 0.140619       | 0.187862       | 0.187199      
2      | 0.112411       | 0.153211       | 0.120405       | 0.103123       | 0.141511       | 0.184527       | 0.184812      
3      | 0.113580       | 0.161733       | 0.140846       | 0.113493       | 0.118243       | 0.176102       | 0.176002      
4      | 0.118145       | 0.168748       | 0.152857       | 0.108380       | 0.108406       | 0.172201       | 0.171263      
5      | 0.111098       | 0.173847       | 0.156774       | 0.105856       | 0.112325       | 0.170428       | 0.169672      
6      | 0.108523       | 0.168466       | 0.156405       | 0.110145       | 0.115856       | 0.170632       | 0.169974      
7      | 0.113621       | 0.176044       | 0.156168       | 0.101580       | 0.114331       | 0.169214       | 0.169042      
8      | 0.122055       | 0.177409       | 0.154121       | 0.101425       | 0.107470       | 0.168113       | 0.169407      
9      | 0.117327       | 0.176148       | 0.155664       | 0.103823       | 0.108406       | 0.169307       | 0.169325      
10     | 0.117142       | 0.174921       | 0.155963       | 0.102497       | 0.111347       | 0.168679       | 0.169449      
11     | 0.116425       | 0.170700       | 0.151328       | 0.104439       | 0.117762       | 0.170201       | 0.169145      
12     | 0.120728       | 0.177632       | 0.150806       | 0.099253       | 0.113947       | 0.168589       | 0.169045      
13     | 0.119111       | 0.174715       | 0.150938       | 0.104510       | 0.111983       | 0.169743       | 0.168999      
14     | 0.114237       | 0.169048       | 0.153791       | 0.107189       | 0.116382       | 0.169581       | 0.169773      
15     | 0.114064       | 0.168549       | 0.153077       | 0.103411       | 0.121167       | 0.169433       | 0.170298      
16     | 0.116832       | 0.167535       | 0.154246       | 0.106245       | 0.114379       | 0.170680       | 0.170083      
17     | 0.117709       | 0.166467       | 0.154040       | 0.106829       | 0.114774       | 0.170112       | 0.170068      
18     | 0.117694       | 0.163316       | 0.152174       | 0.109720       | 0.116274       | 0.170394       | 0.170428      
19     | 0.121660       | 0.167652       | 0.148222       | 0.106588       | 0.114185       | 0.170882       | 0.170811      
20     | 0.114668       | 0.171094       | 0.151548       | 0.108474       | 0.114594       | 0.169862       | 0.169760      
21     | 0.115086       | 0.165519       | 0.149874       | 0.113487       | 0.113796       | 0.171170       | 0.171068      
22     | 0.119550       | 0.164864       | 0.150931       | 0.107688       | 0.115568       | 0.170256       | 0.171143      
23     | 0.116097       | 0.169371       | 0.144819       | 0.107933       | 0.120272       | 0.170682       | 0.170826      
24     | 0.119166       | 0.160067       | 0.148840       | 0.112091       | 0.115346       | 0.172317       | 0.172174      
25     | 0.120414       | 0.156992       | 0.144478       | 0.115239       | 0.118119       | 0.173229       | 0.171528      
26     | 0.121175       | 0.159574       | 0.146240       | 0.106465       | 0.122046       | 0.172260       | 0.172240      
27     | 0.123016       | 0.165627       | 0.145362       | 0.100881       | 0.120132       | 0.172855       | 0.172127      
28     | 0.118794       | 0.162826       | 0.145612       | 0.106874       | 0.120812       | 0.172063       | 0.173019      
29     | 0.120317       | 0.161605       | 0.141691       | 0.108860       | 0.121663       | 0.172519       | 0.173345      
30     | 0.119759       | 0.165146       | 0.148661       | 0.112164       | 0.107930       | 0.172883       | 0.173458      
31     | 0.122211       | 0.162072       | 0.137168       | 0.106568       | 0.122516       | 0.174691       | 0.174775      
32     | 0.119077       | 0.164964       | 0.147528       | 0.112389       | 0.109875       | 0.172894       | 0.173273      
33     | 0.118004       | 0.164451       | 0.146794       | 0.116481       | 0.108055       | 0.173152       | 0.173063      
34     | 0.119078       | 0.160303       | 0.146090       | 0.112680       | 0.113545       | 0.174221       | 0.174083      
35     | 0.123417       | 0.161665       | 0.144896       | 0.102200       | 0.120811       | 0.173772       | 0.173238      
36     | 0.120669       | 0.159785       | 0.147519       | 0.108250       | 0.115276       | 0.173845       | 0.174657      
37     | 0.120767       | 0.162793       | 0.144727       | 0.118271       | 0.106614       | 0.173145       | 0.173684      
38     | 0.117684       | 0.169739       | 0.149008       | 0.107849       | 0.110529       | 0.172246       | 0.172944      
39     | 0.120294       | 0.151138       | 0.146192       | 0.109688       | 0.121590       | 0.175837       | 0.175261      
40     | 0.121437       | 0.156802       | 0.155200       | 0.109451       | 0.109286       | 0.173348       | 0.174477      
41     | 0.115154       | 0.163230       | 0.147402       | 0.111699       | 0.114795       | 0.173680       | 0.174040      
42     | 0.123440       | 0.157759       | 0.146765       | 0.104369       | 0.119476       | 0.173984       | 0.174207      
43     | 0.120671       | 0.171583       | 0.151884       | 0.106483       | 0.105920       | 0.171638       | 0.171822      
44     | 0.120233       | 0.162006       | 0.153997       | 0.105211       | 0.106093       | 0.176128       | 0.176332      
45     | 0.123210       | 0.153054       | 0.146356       | 0.109495       | 0.116368       | 0.175811       | 0.175706      
46     | 0.126786       | 0.156385       | 0.151564       | 0.102966       | 0.115506       | 0.173095       | 0.173697      
47     | 0.115410       | 0.152924       | 0.149835       | 0.110451       | 0.120827       | 0.175547       | 0.175007      
48     | 0.120295       | 0.155880       | 0.149311       | 0.115529       | 0.106609       | 0.176533       | 0.175842      
49     | 0.125563       | 0.153323       | 0.152790       | 0.101610       | 0.117246       | 0.174652       | 0.174817      
50     | 0.116547       | 0.147344       | 0.148481       | 0.111923       | 0.119106       | 0.178630       | 0.177969      
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
4e. SHADOW DISTANCE TO COORDINATE MEDIAN (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A)
--------------------------------------------------------------------------------
1      | 0.868109       | 0.657874       | 0.694092       | 0.951056       | 0.788349       | 0.649520       | 0.650600      
2      | 0.607232       | 0.519266       | 0.614598       | 0.665772       | 0.574524       | 0.488215       | 0.487784      
3      | 0.512642       | 0.395750       | 0.444619       | 0.542769       | 0.522244       | 0.402297       | 0.403343      
4      | 0.436687       | 0.322626       | 0.344566       | 0.487695       | 0.482213       | 0.351372       | 0.351780      
5      | 0.436075       | 0.300402       | 0.315447       | 0.471294       | 0.457535       | 0.337771       | 0.338446      
6      | 0.433331       | 0.291460       | 0.300712       | 0.437400       | 0.428649       | 0.322700       | 0.322310      
7      | 0.407454       | 0.277751       | 0.294630       | 0.448370       | 0.414855       | 0.315113       | 0.314543      
8      | 0.387427       | 0.275183       | 0.292030       | 0.441557       | 0.441774       | 0.315078       | 0.314970      
9      | 0.404391       | 0.277521       | 0.295592       | 0.444194       | 0.437851       | 0.318048       | 0.318308      
10     | 0.393391       | 0.271302       | 0.287117       | 0.441374       | 0.422456       | 0.310803       | 0.311297      
11     | 0.402304       | 0.278829       | 0.300603       | 0.432365       | 0.405638       | 0.309790       | 0.309928      
12     | 0.373368       | 0.264427       | 0.286003       | 0.430296       | 0.402296       | 0.299770       | 0.300074      
13     | 0.377817       | 0.264283       | 0.285935       | 0.414705       | 0.403869       | 0.297811       | 0.297607      
14     | 0.386631       | 0.263945       | 0.281174       | 0.403282       | 0.393902       | 0.294795       | 0.295063      
15     | 0.383252       | 0.262771       | 0.276886       | 0.410949       | 0.369583       | 0.291297       | 0.289765      
16     | 0.373419       | 0.267722       | 0.276689       | 0.405246       | 0.394942       | 0.292711       | 0.292226      
17     | 0.366254       | 0.262346       | 0.270111       | 0.393450       | 0.376951       | 0.283950       | 0.283681      
18     | 0.376595       | 0.267296       | 0.280221       | 0.393267       | 0.383322       | 0.288508       | 0.288940      
19     | 0.356651       | 0.259055       | 0.276868       | 0.388295       | 0.381284       | 0.282009       | 0.281945      
20     | 0.365900       | 0.251803       | 0.268732       | 0.376377       | 0.376157       | 0.279282       | 0.278957      
21     | 0.365192       | 0.253966       | 0.267089       | 0.364105       | 0.369652       | 0.274747       | 0.274854      
22     | 0.343748       | 0.251362       | 0.260683       | 0.371740       | 0.362619       | 0.270338       | 0.270187      
23     | 0.352421       | 0.248408       | 0.264967       | 0.366796       | 0.346810       | 0.267537       | 0.267880      
24     | 0.337463       | 0.251811       | 0.259061       | 0.351315       | 0.352710       | 0.262736       | 0.262360      
25     | 0.331059       | 0.252977       | 0.262987       | 0.343708       | 0.343030       | 0.258506       | 0.258770      
26     | 0.334894       | 0.251072       | 0.261009       | 0.359027       | 0.338521       | 0.260776       | 0.261007      
27     | 0.324700       | 0.246586       | 0.260146       | 0.370759       | 0.336639       | 0.260324       | 0.260460      
28     | 0.325278       | 0.244325       | 0.256544       | 0.344917       | 0.331474       | 0.253482       | 0.253178      
29     | 0.322522       | 0.245108       | 0.259210       | 0.343907       | 0.330534       | 0.252680       | 0.252560      
30     | 0.327589       | 0.243055       | 0.254020       | 0.329945       | 0.362161       | 0.256085       | 0.256524      
31     | 0.319604       | 0.246188       | 0.265653       | 0.337063       | 0.327970       | 0.251219       | 0.250936      
32     | 0.317864       | 0.240488       | 0.252081       | 0.331706       | 0.356429       | 0.253256       | 0.253351      
33     | 0.326159       | 0.244233       | 0.251868       | 0.324742       | 0.365906       | 0.255872       | 0.255779      
34     | 0.317261       | 0.239016       | 0.247968       | 0.305048       | 0.333200       | 0.242271       | 0.242194      
35     | 0.312387       | 0.244067       | 0.256885       | 0.352152       | 0.332757       | 0.252071       | 0.252493      
36     | 0.323511       | 0.247936       | 0.253039       | 0.337600       | 0.345958       | 0.254149       | 0.254105      
37     | 0.321578       | 0.244864       | 0.259826       | 0.318394       | 0.368338       | 0.255382       | 0.255772      
38     | 0.336734       | 0.240988       | 0.258231       | 0.352593       | 0.367370       | 0.263819       | 0.263279      
39     | 0.301600       | 0.246132       | 0.248101       | 0.319627       | 0.320113       | 0.240539       | 0.240927      
40     | 0.316199       | 0.251115       | 0.248711       | 0.356612       | 0.352000       | 0.257523       | 0.257108      
41     | 0.325866       | 0.242947       | 0.252093       | 0.331140       | 0.351866       | 0.253417       | 0.253474      
42     | 0.320294       | 0.249896       | 0.256856       | 0.363977       | 0.345616       | 0.259464       | 0.259339      
43     | 0.328012       | 0.240134       | 0.252888       | 0.367717       | 0.372368       | 0.265381       | 0.265035      
44     | 0.330070       | 0.253582       | 0.256111       | 0.342941       | 0.377806       | 0.262979       | 0.262680      
45     | 0.309993       | 0.247535       | 0.250409       | 0.324274       | 0.345163       | 0.248199       | 0.247821      
46     | 0.311640       | 0.252670       | 0.253108       | 0.377425       | 0.356631       | 0.263075       | 0.262901      
47     | 0.339217       | 0.252250       | 0.249560       | 0.334491       | 0.329339       | 0.252877       | 0.252966      
48     | 0.324191       | 0.255621       | 0.261933       | 0.324910       | 0.376997       | 0.259693       | 0.259486      
49     | 0.309310       | 0.251135       | 0.249918       | 0.388233       | 0.340633       | 0.260555       | 0.260862      
50     | 0.331380       | 0.257129       | 0.262574       | 0.323265       | 0.354907       | 0.255665       | 0.255839      
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
4f. UPDATE NORM (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A)
--------------------------------------------------------------------------------
1      | 1.361764       | 0.606631       | 0.560976       | 1.518111       | 1.264700       | 1.135799       | 1.135370      
2      | 1.088580       | 0.455790       | 0.441318       | 1.121905       | 1.013365       | 0.879329       | 0.878372      
3      | 0.797540       | 0.343250       | 0.389034       | 0.790113       | 0.789663       | 0.655929       | 0.657132      
4      | 0.601862       | 0.313159       | 0.336097       | 0.617252       | 0.644867       | 0.523618       | 0.523692      
5      | 0.551306       | 0.282658       | 0.308478       | 0.552574       | 0.566096       | 0.469648       | 0.470268      
6      | 0.514528       | 0.263987       | 0.296837       | 0.496322       | 0.512900       | 0.432340       | 0.431343      
7      | 0.463290       | 0.266272       | 0.278263       | 0.498823       | 0.480349       | 0.410645       | 0.410375      
8      | 0.428726       | 0.260932       | 0.269792       | 0.489746       | 0.499677       | 0.403758       | 0.403853      
9      | 0.451495       | 0.267995       | 0.277869       | 0.489133       | 0.499242       | 0.409892       | 0.410360      
10     | 0.433618       | 0.261002       | 0.262680       | 0.488075       | 0.475667       | 0.397361       | 0.397550      
11     | 0.444449       | 0.270448       | 0.271284       | 0.469403       | 0.457256       | 0.393042       | 0.393176      
12     | 0.401846       | 0.255967       | 0.262574       | 0.465750       | 0.452175       | 0.378515       | 0.378672      
13     | 0.415044       | 0.252355       | 0.262798       | 0.446875       | 0.452574       | 0.376348       | 0.376603      
14     | 0.419454       | 0.258927       | 0.264893       | 0.431572       | 0.435766       | 0.371317       | 0.371422      
15     | 0.415358       | 0.256037       | 0.254928       | 0.444135       | 0.408382       | 0.366062       | 0.364909      
16     | 0.407673       | 0.259473       | 0.257000       | 0.434200       | 0.434242       | 0.367943       | 0.367755      
17     | 0.397826       | 0.260417       | 0.257371       | 0.415190       | 0.412825       | 0.356328       | 0.356744      
18     | 0.413490       | 0.264283       | 0.256520       | 0.417636       | 0.414531       | 0.361064       | 0.361530      
19     | 0.385224       | 0.254463       | 0.263181       | 0.406360       | 0.411308       | 0.350914       | 0.350517      
20     | 0.397636       | 0.246951       | 0.256751       | 0.386410       | 0.403084       | 0.345705       | 0.345303      
21     | 0.391218       | 0.251843       | 0.256304       | 0.381620       | 0.398544       | 0.342199       | 0.342213      
22     | 0.367298       | 0.246195       | 0.253880       | 0.383407       | 0.392762       | 0.335160       | 0.335268      
23     | 0.374875       | 0.242451       | 0.258807       | 0.379146       | 0.373286       | 0.331307       | 0.331404      
24     | 0.355073       | 0.254940       | 0.254706       | 0.359799       | 0.377909       | 0.325110       | 0.324836      
25     | 0.356616       | 0.256621       | 0.255799       | 0.356032       | 0.364991       | 0.321954       | 0.322209      
26     | 0.356116       | 0.253615       | 0.254498       | 0.372433       | 0.361658       | 0.323969       | 0.324369      
27     | 0.346779       | 0.240095       | 0.256115       | 0.386601       | 0.364005       | 0.324154       | 0.324190      
28     | 0.347518       | 0.250601       | 0.252282       | 0.349818       | 0.356030       | 0.315004       | 0.314917      
29     | 0.341681       | 0.242147       | 0.258822       | 0.353397       | 0.353675       | 0.313610       | 0.313746      
30     | 0.340081       | 0.246074       | 0.247107       | 0.342694       | 0.389502       | 0.317929       | 0.318264      
31     | 0.341054       | 0.246323       | 0.263031       | 0.344196       | 0.343597       | 0.311115       | 0.310370      
32     | 0.336796       | 0.239325       | 0.248605       | 0.340608       | 0.381532       | 0.314512       | 0.314746      
33     | 0.347589       | 0.243418       | 0.251460       | 0.325913       | 0.393288       | 0.317444       | 0.317766      
34     | 0.335929       | 0.243322       | 0.240293       | 0.313393       | 0.355595       | 0.301408       | 0.301381      
35     | 0.330656       | 0.243166       | 0.252989       | 0.365003       | 0.357692       | 0.313894       | 0.314519      
36     | 0.337329       | 0.249447       | 0.256414       | 0.352283       | 0.370531       | 0.317357       | 0.317305      
37     | 0.338865       | 0.245165       | 0.256932       | 0.323573       | 0.401340       | 0.318245       | 0.319012      
38     | 0.358610       | 0.242347       | 0.249135       | 0.361940       | 0.393769       | 0.327127       | 0.326736      
39     | 0.317928       | 0.250043       | 0.247734       | 0.327490       | 0.344298       | 0.300436       | 0.300354      
40     | 0.334819       | 0.251709       | 0.242576       | 0.374389       | 0.379703       | 0.321836       | 0.321914      
41     | 0.352411       | 0.240231       | 0.249679       | 0.338836       | 0.376214       | 0.315909       | 0.316040      
42     | 0.337049       | 0.248915       | 0.252344       | 0.381346       | 0.370260       | 0.323230       | 0.323139      
43     | 0.349218       | 0.243179       | 0.252012       | 0.381010       | 0.395796       | 0.330504       | 0.330457      
44     | 0.350346       | 0.247674       | 0.249866       | 0.351502       | 0.411733       | 0.328377       | 0.328113      
45     | 0.329567       | 0.250231       | 0.248161       | 0.331888       | 0.372467       | 0.310736       | 0.310151      
46     | 0.324588       | 0.250864       | 0.247677       | 0.395528       | 0.382636       | 0.326395       | 0.326551      
47     | 0.359422       | 0.253903       | 0.252225       | 0.346178       | 0.351920       | 0.316747       | 0.316544      
48     | 0.342206       | 0.249377       | 0.250785       | 0.337198       | 0.410719       | 0.323856       | 0.323921      
49     | 0.324341       | 0.255278       | 0.254248       | 0.410480       | 0.361230       | 0.326334       | 0.326729      
50     | 0.350329       | 0.252987       | 0.252689       | 0.334631       | 0.385248       | 0.319693       | 0.319722      
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
4g. PAIRWISE SQUARED DISTANCE (Per Round, Upper Triangle)
--------------------------------------------------------------------------------
Round | d(0,1) | d(0,2) | d(0,3) | d(0,4) | d(0,5) | d(0,6) | d(1,2) | d(1,3) | d(1,4) | d(1,5) | d(1,6) | d(2,3) | d(2,4) | d(2,5) | d(2,6) | d(3,4) | d(3,5) | d(3,6) | d(4,5) | d(4,6) | d(5,6)
--------------------------------------------------------------------------------
1      | 1.554941       | 1.543046       | 0.901672       | 1.749678       | 1.147506       | 1.150807       | 0.127025       | 1.842158       | 1.025643       | 0.911646       | 0.911747       | 1.956156       | 1.144003       | 0.955352       | 0.956491       | 1.731028       | 1.283658       | 1.287261       | 1.132116       | 1.131283       | 1.086590      
2      | 0.836455       | 0.990923       | 0.601168       | 0.709069       | 0.628448       | 0.630088       | 0.143047       | 0.901063       | 0.706506       | 0.516492       | 0.514836       | 1.158607       | 0.801673       | 0.617833       | 0.616312       | 0.804884       | 0.693478       | 0.693989       | 0.605065       | 0.603711       | 0.611894      
3      | 0.527641       | 0.570962       | 0.528121       | 0.560041       | 0.436281       | 0.436312       | 0.133487       | 0.523155       | 0.511820       | 0.338576       | 0.340160       | 0.646945       | 0.545620       | 0.379007       | 0.380024       | 0.609069       | 0.460963       | 0.461326       | 0.445032       | 0.445874       | 0.412108      
4      | 0.347092       | 0.357160       | 0.438275       | 0.473999       | 0.322663       | 0.322761       | 0.128692       | 0.376522       | 0.393906       | 0.249547       | 0.249268       | 0.448330       | 0.384011       | 0.263855       | 0.263858       | 0.539632       | 0.360662       | 0.361373       | 0.357998       | 0.358309       | 0.311045      
5      | 0.323766       | 0.330304       | 0.440866       | 0.453951       | 0.309524       | 0.309539       | 0.126517       | 0.338819       | 0.340607       | 0.225508       | 0.226149       | 0.389260       | 0.331485       | 0.235323       | 0.235561       | 0.505005       | 0.334862       | 0.334769       | 0.325187       | 0.326129       | 0.286238      
6      | 0.320752       | 0.314080       | 0.407788       | 0.425242       | 0.293962       | 0.294169       | 0.123340       | 0.293951       | 0.303000       | 0.208202       | 0.207557       | 0.339832       | 0.293187       | 0.214467       | 0.213523       | 0.433750       | 0.295588       | 0.294748       | 0.291101       | 0.290994       | 0.260770      
7      | 0.273272       | 0.282800       | 0.390964       | 0.400792       | 0.269705       | 0.269498       | 0.117469       | 0.305143       | 0.278198       | 0.194951       | 0.194603       | 0.354210       | 0.268974       | 0.205073       | 0.204910       | 0.430456       | 0.295945       | 0.295360       | 0.275562       | 0.275382       | 0.248317      
8      | 0.243990       | 0.254175       | 0.374760       | 0.413241       | 0.257374       | 0.257190       | 0.119944       | 0.296796       | 0.305975       | 0.193257       | 0.193354       | 0.342168       | 0.301666       | 0.203799       | 0.203543       | 0.443822       | 0.292515       | 0.291383       | 0.292609       | 0.292954       | 0.248021      
9      | 0.266214       | 0.270815       | 0.396378       | 0.421502       | 0.271284       | 0.270685       | 0.124045       | 0.291986       | 0.304430       | 0.197200       | 0.197225       | 0.348792       | 0.296212       | 0.207687       | 0.207876       | 0.445875       | 0.296203       | 0.296832       | 0.293759       | 0.293414       | 0.252803      
10     | 0.251673       | 0.252435       | 0.388508       | 0.395294       | 0.257150       | 0.257792       | 0.121481       | 0.287484       | 0.282137       | 0.188587       | 0.188774       | 0.338324       | 0.276831       | 0.197921       | 0.198117       | 0.426960       | 0.288439       | 0.288747       | 0.275881       | 0.276310       | 0.242012      
11     | 0.269075       | 0.268375       | 0.388022       | 0.386951       | 0.262344       | 0.262081       | 0.139255       | 0.277777       | 0.267453       | 0.190420       | 0.190763       | 0.341966       | 0.269150       | 0.203963       | 0.203533       | 0.400025       | 0.280956       | 0.281827       | 0.264528       | 0.264315       | 0.240399      
12     | 0.227826       | 0.233867       | 0.359400       | 0.360093       | 0.236188       | 0.235858       | 0.127599       | 0.269573       | 0.257605       | 0.176128       | 0.176699       | 0.329150       | 0.253157       | 0.188502       | 0.188760       | 0.400197       | 0.271417       | 0.271537       | 0.254015       | 0.254350       | 0.225045      
13     | 0.231118       | 0.242887       | 0.352702       | 0.362996       | 0.236837       | 0.237406       | 0.121818       | 0.256737       | 0.263870       | 0.174473       | 0.174321       | 0.308366       | 0.259350       | 0.186373       | 0.186476       | 0.380727       | 0.259820       | 0.259276       | 0.253379       | 0.252747       | 0.221928      
14     | 0.240222       | 0.249460       | 0.351693       | 0.359453       | 0.240203       | 0.240608       | 0.123765       | 0.244400       | 0.253349       | 0.172327       | 0.172533       | 0.289639       | 0.245651       | 0.181439       | 0.181708       | 0.362693       | 0.249629       | 0.250002       | 0.243830       | 0.244868       | 0.218027      
15     | 0.238179       | 0.247125       | 0.348989       | 0.334219       | 0.234301       | 0.232889       | 0.119333       | 0.257823       | 0.227405       | 0.169365       | 0.168328       | 0.296885       | 0.218998       | 0.176953       | 0.176235       | 0.350205       | 0.251274       | 0.250667       | 0.226419       | 0.225825       | 0.211187      
16     | 0.232601       | 0.238485       | 0.334820       | 0.344300       | 0.230398       | 0.230490       | 0.120563       | 0.251107       | 0.258585       | 0.172939       | 0.172410       | 0.288898       | 0.241601       | 0.177655       | 0.177314       | 0.370681       | 0.249315       | 0.249042       | 0.242778       | 0.242843       | 0.214528      
17     | 0.223621       | 0.225536       | 0.323315       | 0.321126       | 0.218716       | 0.218837       | 0.121295       | 0.235347       | 0.237610       | 0.163655       | 0.163480       | 0.271064       | 0.224516       | 0.168534       | 0.168467       | 0.340275       | 0.234119       | 0.234106       | 0.225335       | 0.225446       | 0.201837      
18     | 0.233132       | 0.249424       | 0.324250       | 0.336238       | 0.228484       | 0.228455       | 0.124031       | 0.244740       | 0.246738       | 0.169675       | 0.169937       | 0.276044       | 0.233957       | 0.176227       | 0.176820       | 0.347124       | 0.238611       | 0.238605       | 0.232832       | 0.233261       | 0.209559      
19     | 0.210030       | 0.225653       | 0.306623       | 0.318110       | 0.211542       | 0.211896       | 0.122679       | 0.232595       | 0.240195       | 0.160831       | 0.160616       | 0.271775       | 0.233786       | 0.170655       | 0.169805       | 0.339541       | 0.229660       | 0.230433       | 0.226421       | 0.226321       | 0.199335      
20     | 0.219940       | 0.227556       | 0.303280       | 0.322727       | 0.215038       | 0.214949       | 0.113846       | 0.215362       | 0.226506       | 0.155338       | 0.154877       | 0.254572       | 0.225167       | 0.164536       | 0.163823       | 0.329826       | 0.220524       | 0.220578       | 0.221185       | 0.221395       | 0.195205      
21     | 0.221066       | 0.229721       | 0.289046       | 0.314910       | 0.211032       | 0.210688       | 0.109776       | 0.209578       | 0.228075       | 0.153501       | 0.153536       | 0.243363       | 0.220553       | 0.160325       | 0.160327       | 0.307838       | 0.209975       | 0.209442       | 0.213744       | 0.214345       | 0.189643      
22     | 0.195910       | 0.204090       | 0.287367       | 0.291688       | 0.195927       | 0.196054       | 0.113096       | 0.216585       | 0.219094       | 0.148773       | 0.149019       | 0.241604       | 0.210512       | 0.153836       | 0.154001       | 0.308763       | 0.210857       | 0.210725       | 0.206764       | 0.206229       | 0.182960      
23     | 0.209508       | 0.215613       | 0.287505       | 0.279261       | 0.198040       | 0.198081       | 0.112328       | 0.205331       | 0.201292       | 0.145801       | 0.145825       | 0.244853       | 0.201822       | 0.154571       | 0.154833       | 0.294430       | 0.206376       | 0.206374       | 0.195278       | 0.195631       | 0.180112      
24     | 0.199395       | 0.198359       | 0.260537       | 0.273322       | 0.186428       | 0.186083       | 0.110750       | 0.200607       | 0.209619       | 0.144077       | 0.143972       | 0.223248       | 0.208059       | 0.148115       | 0.148089       | 0.283083       | 0.193358       | 0.193086       | 0.195109       | 0.195304       | 0.173547      
25     | 0.191877       | 0.196571       | 0.249661       | 0.266100       | 0.180283       | 0.180279       | 0.122919       | 0.189222       | 0.205166       | 0.141864       | 0.142132       | 0.222435       | 0.191529       | 0.146627       | 0.146972       | 0.270665       | 0.186418       | 0.186566       | 0.186770       | 0.186915       | 0.168438      
26     | 0.191023       | 0.191161       | 0.275767       | 0.263957       | 0.184660       | 0.184678       | 0.116065       | 0.205245       | 0.199426       | 0.142552       | 0.142376       | 0.235994       | 0.196329       | 0.147546       | 0.147979       | 0.268083       | 0.196767       | 0.197285       | 0.185546       | 0.185443       | 0.171655      
27     | 0.180765       | 0.187168       | 0.268321       | 0.254013       | 0.178015       | 0.178219       | 0.111485       | 0.214052       | 0.193906       | 0.139937       | 0.139860       | 0.248503       | 0.189593       | 0.147667       | 0.147439       | 0.285130       | 0.202812       | 0.203325       | 0.184737       | 0.184565       | 0.170955      
28     | 0.187485       | 0.182476       | 0.250077       | 0.246865       | 0.173659       | 0.173462       | 0.113367       | 0.184441       | 0.187484       | 0.134431       | 0.134332       | 0.220482       | 0.186632       | 0.140643       | 0.140607       | 0.264170       | 0.184190       | 0.183595       | 0.177010       | 0.176619       | 0.161766      
29     | 0.179873       | 0.189321       | 0.243274       | 0.247960       | 0.171806       | 0.171997       | 0.115310       | 0.189520       | 0.187021       | 0.134049       | 0.134215       | 0.219871       | 0.184518       | 0.141684       | 0.141534       | 0.261271       | 0.183023       | 0.182658       | 0.175838       | 0.175733       | 0.161233      
30     | 0.186502       | 0.182113       | 0.237384       | 0.277389       | 0.176901       | 0.176638       | 0.109441       | 0.171067       | 0.213772       | 0.135759       | 0.136298       | 0.203614       | 0.211693       | 0.141201       | 0.141336       | 0.279432       | 0.177770       | 0.178607       | 0.196472       | 0.196136       | 0.165683      
31     | 0.180104       | 0.187647       | 0.231277       | 0.244938       | 0.169108       | 0.169031       | 0.115141       | 0.186183       | 0.187036       | 0.133652       | 0.133506       | 0.227640       | 0.188542       | 0.143970       | 0.143826       | 0.245130       | 0.178265       | 0.177824       | 0.173303       | 0.173410       | 0.159816      
32     | 0.172589       | 0.180113       | 0.228513       | 0.268144       | 0.169958       | 0.170054       | 0.105165       | 0.177612       | 0.208168       | 0.132923       | 0.133042       | 0.203589       | 0.203900       | 0.138660       | 0.138676       | 0.272931       | 0.176749       | 0.176870       | 0.190413       | 0.190380       | 0.161759      
33     | 0.186595       | 0.182569       | 0.226183       | 0.284114       | 0.175733       | 0.175498       | 0.106326       | 0.172112       | 0.215230       | 0.136073       | 0.136099       | 0.197636       | 0.214843       | 0.140458       | 0.140488       | 0.276475       | 0.174473       | 0.174672       | 0.197790       | 0.198223       | 0.165090      
34     | 0.176689       | 0.174852       | 0.210990       | 0.248832       | 0.161709       | 0.162088       | 0.107133       | 0.155628       | 0.187077       | 0.125490       | 0.125423       | 0.181005       | 0.183814       | 0.129510       | 0.128989       | 0.233231       | 0.156135       | 0.156431       | 0.170555       | 0.170562       | 0.148605      
35     | 0.172188       | 0.175667       | 0.245958       | 0.238123       | 0.166500       | 0.166700       | 0.109560       | 0.196194       | 0.190902       | 0.133733       | 0.133878       | 0.227744       | 0.187887       | 0.140129       | 0.140131       | 0.267605       | 0.187409       | 0.187632       | 0.176691       | 0.176987       | 0.160901      
36     | 0.182969       | 0.182435       | 0.240473       | 0.259603       | 0.173194       | 0.173172       | 0.107936       | 0.190424       | 0.200924       | 0.136707       | 0.136735       | 0.206261       | 0.200587       | 0.139436       | 0.139573       | 0.266437       | 0.181278       | 0.180526       | 0.185513       | 0.185574       | 0.163434      
37     | 0.181341       | 0.186178       | 0.218050       | 0.280692       | 0.173008       | 0.173861       | 0.109919       | 0.166163       | 0.221563       | 0.136097       | 0.136177       | 0.197901       | 0.222400       | 0.143327       | 0.143724       | 0.273282       | 0.170812       | 0.171249       | 0.199959       | 0.199359       | 0.165098      
38     | 0.186551       | 0.191066       | 0.267723       | 0.293421       | 0.187631       | 0.187670       | 0.108122       | 0.191218       | 0.212952       | 0.139752       | 0.139354       | 0.222628       | 0.220045       | 0.148651       | 0.148233       | 0.296631       | 0.195753       | 0.195247       | 0.204189       | 0.204194       | 0.174656      
39     | 0.169572       | 0.166128       | 0.209614       | 0.220802       | 0.153255       | 0.153236       | 0.107477       | 0.174949       | 0.184201       | 0.127496       | 0.127059       | 0.192185       | 0.175949       | 0.128384       | 0.128516       | 0.232254       | 0.161809       | 0.161982       | 0.162167       | 0.162949       | 0.146828      
40     | 0.179687       | 0.167585       | 0.254791       | 0.258959       | 0.172346       | 0.171592       | 0.105735       | 0.207093       | 0.210217       | 0.140485       | 0.140390       | 0.218854       | 0.204883       | 0.139356       | 0.139517       | 0.284045       | 0.193017       | 0.192911       | 0.191118       | 0.191781       | 0.167479      
41     | 0.186482       | 0.185111       | 0.235372       | 0.266517       | 0.174681       | 0.174202       | 0.103273       | 0.176299       | 0.204502       | 0.133672       | 0.133811       | 0.204434       | 0.201885       | 0.138671       | 0.138813       | 0.268002       | 0.176574       | 0.176631       | 0.188178       | 0.188267       | 0.161996      
42     | 0.182473       | 0.181591       | 0.259378       | 0.252333       | 0.175157       | 0.174812       | 0.106536       | 0.212496       | 0.203279       | 0.140941       | 0.141032       | 0.234732       | 0.201713       | 0.145150       | 0.144601       | 0.287628       | 0.198692       | 0.199081       | 0.189330       | 0.188896       | 0.170029      
43     | 0.179128       | 0.184494       | 0.264318       | 0.287349       | 0.182986       | 0.182856       | 0.101035       | 0.205836       | 0.219610       | 0.140839       | 0.140866       | 0.235541       | 0.217551       | 0.147506       | 0.147263       | 0.318414       | 0.205081       | 0.204658       | 0.208688       | 0.208629       | 0.177081      
44     | 0.190452       | 0.188779       | 0.245020       | 0.290945       | 0.183066       | 0.182992       | 0.105300       | 0.192535       | 0.237704       | 0.145367       | 0.144793       | 0.213553       | 0.225894       | 0.146668       | 0.146436       | 0.299814       | 0.189767       | 0.190028       | 0.210695       | 0.210988       | 0.174933      
45     | 0.176304       | 0.169870       | 0.220598       | 0.242845       | 0.161882       | 0.161974       | 0.108551       | 0.174802       | 0.204533       | 0.133023       | 0.132765       | 0.195193       | 0.198295       | 0.134485       | 0.134320       | 0.256943       | 0.169516       | 0.169112       | 0.180717       | 0.180307       | 0.155715      
46     | 0.177362       | 0.172476       | 0.263513       | 0.251343       | 0.173160       | 0.173006       | 0.105196       | 0.228041       | 0.213192       | 0.145018       | 0.144853       | 0.239625       | 0.209424       | 0.145390       | 0.145446       | 0.313803       | 0.209038       | 0.208798       | 0.197439       | 0.197933       | 0.174163      
47     | 0.200622       | 0.192610       | 0.252321       | 0.256316       | 0.180590       | 0.180457       | 0.111356       | 0.187865       | 0.189969       | 0.138297       | 0.137820       | 0.199399       | 0.182347       | 0.137161       | 0.137220       | 0.249987       | 0.177777       | 0.178100       | 0.175554       | 0.175789       | 0.162132      
48     | 0.184678       | 0.188945       | 0.230088       | 0.285719       | 0.177783       | 0.177654       | 0.113023       | 0.181104       | 0.240111       | 0.143786       | 0.144065       | 0.197723       | 0.233449       | 0.146369       | 0.146657       | 0.280003       | 0.177762       | 0.177737       | 0.207911       | 0.207568       | 0.170837      
49     | 0.173783       | 0.165836       | 0.269449       | 0.242677       | 0.169973       | 0.170435       | 0.106122       | 0.238684       | 0.196094       | 0.142673       | 0.142907       | 0.252738       | 0.189985       | 0.142597       | 0.142818       | 0.306052       | 0.213392       | 0.213325       | 0.186968       | 0.186896       | 0.171145      
50     | 0.197723       | 0.194108       | 0.225306       | 0.278475       | 0.178646       | 0.179188       | 0.114262       | 0.183401       | 0.215581       | 0.142169       | 0.142270       | 0.203310       | 0.207143       | 0.143596       | 0.143865       | 0.260208       | 0.174784       | 0.174464       | 0.192303       | 0.192256       | 0.166470      
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
4h. PAIRWISE COSINE (Per Round, Upper Triangle)
--------------------------------------------------------------------------------
Round | c(0,1) | c(0,2) | c(0,3) | c(0,4) | c(0,5) | c(0,6) | c(1,2) | c(1,3) | c(1,4) | c(1,5) | c(1,6) | c(2,3) | c(2,4) | c(2,5) | c(2,6) | c(3,4) | c(3,5) | c(3,6) | c(4,5) | c(4,6) | c(5,6)
--------------------------------------------------------------------------------
1      | 0.403994       | 0.409766       | 0.787847       | 0.494773       | 0.645562       | 0.644426       | 0.816432       | 0.450911       | 0.613809       | 0.541649       | 0.541074       | 0.389379       | 0.542777       | 0.509600       | 0.508136       | 0.565934       | 0.670162       | 0.669089       | 0.611726       | 0.611907       | 0.578709      
2      | 0.560609       | 0.404708       | 0.754347       | 0.681189       | 0.694621       | 0.693640       | 0.644954       | 0.552812       | 0.571747       | 0.579461       | 0.580058       | 0.297739       | 0.469576       | 0.451157       | 0.451440       | 0.651214       | 0.678361       | 0.677993       | 0.670584       | 0.671132       | 0.603906      
3      | 0.413242       | 0.348825       | 0.581015       | 0.555438       | 0.602190       | 0.602562       | 0.508044       | 0.403657       | 0.423489       | 0.465233       | 0.464370       | 0.209322       | 0.373203       | 0.396952       | 0.397327       | 0.511917       | 0.572662       | 0.572787       | 0.587682       | 0.587317       | 0.521965      
4      | 0.300343       | 0.291770       | 0.410458       | 0.391758       | 0.497799       | 0.497697       | 0.391155       | 0.265260       | 0.297157       | 0.374143       | 0.375175       | 0.109979       | 0.334059       | 0.350268       | 0.350429       | 0.323112       | 0.455627       | 0.454579       | 0.491671       | 0.491256       | 0.432853      
5      | 0.192738       | 0.202259       | 0.276416       | 0.273087       | 0.415165       | 0.415712       | 0.278341       | 0.148591       | 0.186722       | 0.282328       | 0.281742       | 0.032964       | 0.240914       | 0.277500       | 0.278325       | 0.193090       | 0.368088       | 0.368906       | 0.405944       | 0.404733       | 0.352002      
6      | 0.050344       | 0.126928       | 0.202232       | 0.194326       | 0.354458       | 0.352871       | 0.219893       | 0.084238       | 0.109884       | 0.212064       | 0.211607       | -0.018272      | 0.190455       | 0.235962       | 0.236833       | 0.148594       | 0.320788       | 0.321479       | 0.358264       | 0.357388       | 0.300846      
7      | 0.049717       | 0.035944       | 0.156859       | 0.100165       | 0.298466       | 0.298625       | 0.208271       | 0.054896       | 0.091623       | 0.203856       | 0.204570       | -0.100704      | 0.146606       | 0.179347       | 0.179213       | 0.102467       | 0.296601       | 0.297686       | 0.313823       | 0.313928       | 0.263244      
8      | 0.035316       | 0.010456       | 0.116444       | 0.047244       | 0.258388       | 0.259080       | 0.148657       | 0.043594       | 0.045205       | 0.179637       | 0.179495       | -0.111746      | 0.077142       | 0.146928       | 0.148421       | 0.093388       | 0.279055       | 0.282044       | 0.297629       | 0.296891       | 0.239481      
9      | 0.039073       | 0.040828       | 0.105781       | 0.070073       | 0.271739       | 0.274083       | 0.167775       | 0.072802       | 0.062165       | 0.194058       | 0.195468       | -0.118938      | 0.109003       | 0.164784       | 0.165454       | 0.087265       | 0.276975       | 0.276050       | 0.301753       | 0.303189       | 0.248531      
10     | 0.019762       | 0.020148       | 0.089149       | 0.046034       | 0.257608       | 0.256060       | 0.114073       | 0.074010       | 0.049313       | 0.180458       | 0.180201       | -0.121314      | 0.073747       | 0.138801       | 0.138521       | 0.080801       | 0.277601       | 0.277065       | 0.286430       | 0.285559       | 0.234007      
11     | 0.006663       | 0.011426       | 0.071548       | 0.048388       | 0.256674       | 0.257640       | 0.050992       | 0.061855       | 0.059730       | 0.175005       | 0.173825       | -0.188595      | 0.054528       | 0.113082       | 0.115551       | 0.068484       | 0.254391       | 0.252231       | 0.275541       | 0.276330       | 0.222193      
12     | -0.004022      | -0.016308      | 0.050771       | 0.016097       | 0.225396       | 0.226778       | 0.051067       | 0.053976       | 0.053467       | 0.168572       | 0.166172       | -0.176961      | 0.085284       | 0.119317       | 0.118568       | 0.050307       | 0.251805       | 0.251696       | 0.273797       | 0.273053       | 0.214964      
13     | 0.023041       | -0.007164      | 0.051915       | 0.037502       | 0.246684       | 0.245309       | 0.082391       | 0.029457       | 0.020300       | 0.162409       | 0.164109       | -0.168626      | 0.061112       | 0.122992       | 0.123354       | 0.058825       | 0.242352       | 0.244375       | 0.273255       | 0.275489       | 0.217104      
14     | 0.012719       | -0.015076      | 0.029012       | 0.017453       | 0.236331       | 0.235213       | 0.098024       | 0.039814       | 0.015892       | 0.169503       | 0.168794       | -0.145277      | 0.062415       | 0.135251       | 0.134244       | 0.035768       | 0.232462       | 0.231476       | 0.259385       | 0.256346       | 0.209572      
15     | -0.000476      | -0.045398      | 0.056350       | 0.014972       | 0.237506       | 0.240137       | 0.085877       | 0.021934       | 0.023554       | 0.161063       | 0.162615       | -0.152979      | 0.061316       | 0.118075       | 0.117773       | 0.038118       | 0.245989       | 0.246036       | 0.248708       | 0.248661       | 0.209518      
16     | 0.004358       | -0.029775      | 0.056232       | 0.029553       | 0.237275       | 0.236631       | 0.096070       | 0.021076       | -0.011948      | 0.155909       | 0.158037       | -0.153779      | 0.058308       | 0.125720       | 0.126859       | 0.017012       | 0.233469       | 0.234011       | 0.254019       | 0.253512       | 0.207296      
17     | 0.011879       | -0.005037      | 0.022200       | 0.023029       | 0.234629       | 0.234975       | 0.095206       | 0.022441       | 0.002936       | 0.167752       | 0.170093       | -0.151798      | 0.057169       | 0.134535       | 0.136358       | 0.007386       | 0.220472       | 0.221261       | 0.244936       | 0.245280       | 0.206106      
18     | 0.035177       | -0.059622      | 0.061221       | 0.019172       | 0.244008       | 0.244917       | 0.085682       | -0.002146      | -0.023079      | 0.160015       | 0.160199       | -0.167186      | 0.017312       | 0.107660       | 0.106140       | -0.002508      | 0.219432       | 0.220284       | 0.231751       | 0.231143       | 0.197317      
19     | 0.015908       | -0.039412      | 0.022049       | -0.001699      | 0.221916       | 0.219828       | 0.084641       | -0.013132      | -0.029949      | 0.151533       | 0.151347       | -0.174773      | 0.021491       | 0.117756       | 0.120986       | -0.015672      | 0.205512       | 0.202053       | 0.228274       | 0.227916       | 0.189708      
20     | -0.004282      | -0.017243      | 0.013497       | -0.006662      | 0.227661       | 0.227238       | 0.102984       | -0.026540      | -0.015293      | 0.147350       | 0.148596       | -0.198260      | 0.015609       | 0.117720       | 0.120310       | -0.057902      | 0.180793       | 0.179757       | 0.218179       | 0.216679       | 0.182380      
21     | -0.023290      | -0.054740      | 0.032284       | -0.009687      | 0.220809       | 0.222122       | 0.149814       | -0.002701      | -0.028961      | 0.156789       | 0.156636       | -0.163774      | 0.019463       | 0.128081       | 0.128122       | -0.011070      | 0.202010       | 0.204080       | 0.228018       | 0.225843       | 0.190291      
22     | -0.002156      | -0.025345      | -0.019379      | -0.008728      | 0.208422       | 0.208129       | 0.095766       | -0.047525      | -0.021825      | 0.146471       | 0.145368       | -0.154864      | 0.041143       | 0.134869       | 0.134282       | -0.024905      | 0.188627       | 0.189361       | 0.227256       | 0.229490       | 0.185899      
23     | -0.056081      | -0.041749      | -0.011334      | 0.002189       | 0.210376       | 0.210412       | 0.107056       | -0.015215      | -0.017498      | 0.141592       | 0.141800       | -0.173863      | 0.023297       | 0.129305       | 0.128118       | -0.040050      | 0.187644       | 0.187852       | 0.217630       | 0.216403       | 0.179800      
24     | -0.045981      | -0.040949      | -0.019591      | -0.016508      | 0.196412       | 0.197300       | 0.147223       | -0.033565      | -0.009395      | 0.160553       | 0.160251       | -0.157776      | -0.001914      | 0.135602       | 0.134797       | -0.039764      | 0.178651       | 0.179202       | 0.217332       | 0.215998       | 0.178344      
25     | 0.006293       | -0.021724      | 0.016827       | -0.021922      | 0.220129       | 0.220686       | 0.063740       | 0.018557       | -0.032529      | 0.167305       | 0.166546       | -0.166039      | 0.038148       | 0.136368       | 0.135163       | -0.041122      | 0.191910       | 0.191834       | 0.213189       | 0.213103       | 0.188150      
26     | 0.000641       | 0.002354       | -0.038611      | -0.024623      | 0.204193       | 0.204985       | 0.100901       | -0.011742      | -0.023488      | 0.162637       | 0.165080       | -0.171542      | -0.004144      | 0.134506       | 0.133288       | 0.005273       | 0.194339       | 0.193028       | 0.214258       | 0.215539       | 0.183265      
27     | -0.017200      | -0.007417      | 0.005200       | -0.004981      | 0.210471       | 0.209642       | 0.095582       | -0.037419      | -0.021516      | 0.146379       | 0.147008       | -0.168911      | 0.045598       | 0.138545       | 0.140044       | -0.011263      | 0.206374       | 0.204399       | 0.223910       | 0.224711       | 0.186610      
28     | -0.022482      | 0.011057       | -0.028528      | 0.002670       | 0.211648       | 0.212360       | 0.103446       | 0.004176       | 0.011619       | 0.174804       | 0.175130       | -0.195256      | 0.020994       | 0.139868       | 0.139790       | -0.060381      | 0.169751       | 0.172251       | 0.218348       | 0.219910       | 0.184652      
29     | -0.027146      | -0.031581      | -0.006784      | -0.025355      | 0.202009       | 0.201429       | 0.082284       | -0.035029      | -0.019270      | 0.151024       | 0.150432       | -0.153026      | 0.041279       | 0.145725       | 0.147113       | -0.045187      | 0.181446       | 0.183398       | 0.214580       | 0.215343       | 0.180682      
30     | -0.061506      | -0.032105      | -0.018404      | -0.037832      | 0.184211       | 0.186216       | 0.100102       | 0.041061       | -0.007865      | 0.165354       | 0.163099       | -0.148282      | 0.005612       | 0.133270       | 0.133629       | -0.038514      | 0.187004       | 0.183947       | 0.227400       | 0.229377       | 0.181296      
31     | -0.018516      | -0.011950      | 0.014958       | -0.045061      | 0.207356       | 0.206027       | 0.113592       | -0.041502      | -0.049041      | 0.155388       | 0.153685       | -0.220830      | -0.007179      | 0.134468       | 0.132837       | -0.036361      | 0.172757       | 0.173068       | 0.194343       | 0.192137       | 0.172466      
32     | -0.011668      | -0.029123      | 0.004066       | -0.035587      | 0.200103       | 0.200197       | 0.116951       | -0.026507      | -0.029159      | 0.154590       | 0.154662       | -0.152171      | 0.018296       | 0.141090       | 0.141817       | -0.043672      | 0.178223       | 0.178211       | 0.225313       | 0.225892       | 0.182970      
33     | -0.038561      | 0.008477       | 0.003771       | -0.031532      | 0.207801       | 0.209576       | 0.131995       | -0.041855      | -0.006802      | 0.154977       | 0.155972       | -0.171954      | 0.015494       | 0.147483       | 0.148424       | -0.060777      | 0.157155       | 0.157019       | 0.230915       | 0.229766       | 0.181699      
34     | -0.028352      | -0.026402      | 0.000348       | -0.039914      | 0.207340       | 0.205408       | 0.083921       | 0.011754       | -0.008226      | 0.167466       | 0.167824       | -0.166321      | 0.002195       | 0.131708       | 0.135202       | -0.038443      | 0.174299       | 0.172657       | 0.218049       | 0.217960       | 0.182048      
35     | -0.023167      | -0.013927      | -0.014076      | -0.003575      | 0.199262       | 0.199796       | 0.110319       | -0.021620      | -0.022008      | 0.156732       | 0.158040       | -0.165223      | 0.022438       | 0.141063       | 0.143240       | -0.024640      | 0.193538       | 0.193893       | 0.221698       | 0.221689       | 0.185116      
36     | -0.041320      | -0.016740      | -0.010849      | -0.034080      | 0.192956       | 0.192938       | 0.156626       | -0.023311      | -0.007612      | 0.165687       | 0.165332       | -0.090831      | 0.012915       | 0.166072       | 0.165053       | -0.019309      | 0.194730       | 0.197979       | 0.223217       | 0.222857       | 0.188508      
37     | -0.038555      | -0.030637      | 0.006746       | -0.017606      | 0.199840       | 0.197675       | 0.128600       | -0.008556      | -0.001948      | 0.162064       | 0.164285       | -0.163511      | 0.022732       | 0.146555       | 0.146764       | -0.028911      | 0.170760       | 0.170600       | 0.244259       | 0.247924       | 0.186910      
38     | 0.004500       | -0.002221      | -0.031287      | -0.034584      | 0.204514       | 0.203501       | 0.104991       | -0.008466      | 0.004371       | 0.163933       | 0.165030       | -0.163912      | -0.014901      | 0.125337       | 0.126487       | -0.037108      | 0.178465       | 0.179738       | 0.224660       | 0.223920       | 0.182972      
39     | -0.037568      | -0.023347      | -0.006178      | -0.005401      | 0.199367       | 0.199263       | 0.132516       | -0.031616      | -0.018230      | 0.168313       | 0.170943       | -0.145220      | 0.023241       | 0.156189       | 0.155017       | -0.028662      | 0.181437       | 0.180358       | 0.225433       | 0.221473       | 0.186441      
40     | -0.025069      | 0.020702       | -0.010053      | -0.010543      | 0.201090       | 0.204770       | 0.134838       | -0.018937      | -0.014048      | 0.163260       | 0.164120       | -0.109255      | -0.010128      | 0.147728       | 0.146984       | 0.001044       | 0.210510       | 0.211109       | 0.231730       | 0.229167       | 0.191735      
41     | -0.027034      | 0.008083       | 0.015207       | -0.002966      | 0.221469       | 0.223897       | 0.139859       | -0.023208      | -0.029065      | 0.157050       | 0.156617       | -0.161260      | 0.010603       | 0.148763       | 0.148326       | -0.045715      | 0.177666       | 0.177715       | 0.223642       | 0.223523       | 0.188726      
42     | -0.041195      | -0.025345      | -0.001364      | -0.006565      | 0.196999       | 0.198366       | 0.152046       | -0.026928      | -0.022936      | 0.158445       | 0.157562       | -0.133170      | -0.005048      | 0.141026       | 0.144073       | -0.018100      | 0.207733       | 0.205978       | 0.218253       | 0.219886       | 0.186066      
43     | 0.011546       | 0.005506       | 0.010535       | -0.031624      | 0.208808       | 0.209270       | 0.176323       | -0.008263      | -0.019840      | 0.171271       | 0.170934       | -0.139879      | 0.013104       | 0.151502       | 0.152796       | -0.055010      | 0.195836       | 0.197422       | 0.218636       | 0.218774       | 0.189323      
44     | -0.036687      | -0.020584      | 0.005181       | 0.004580       | 0.206479       | 0.206213       | 0.149278       | -0.043872      | -0.033525      | 0.146360       | 0.148949       | -0.156936      | 0.029466       | 0.143797       | 0.144270       | -0.023274      | 0.180286       | 0.178546       | 0.246528       | 0.244999       | 0.188213      
45     | -0.030768      | 0.002010       | -0.008386      | 0.018335       | 0.211364       | 0.209534       | 0.125996       | -0.012263      | -0.017092      | 0.168154       | 0.167792       | -0.142423      | 0.010931       | 0.153389       | 0.152387       | -0.032608      | 0.180310       | 0.180849       | 0.235759       | 0.236408       | 0.192145      
46     | -0.055708      | -0.035913      | -0.006673      | 0.001708       | 0.182792       | 0.183917       | 0.153549       | -0.043671      | -0.020047      | 0.149298       | 0.150855       | -0.111465      | -0.008810      | 0.139089       | 0.139309       | -0.036179      | 0.208907       | 0.210131       | 0.222219       | 0.220546       | 0.182987      
47     | -0.038197      | 0.001056       | -0.013254      | -0.012984      | 0.214869       | 0.215023       | 0.130609       | -0.020250      | -0.009261      | 0.164745       | 0.167020       | -0.091298      | 0.028831       | 0.167638       | 0.166570       | -0.025858      | 0.193302       | 0.191366       | 0.218103       | 0.216611       | 0.191483      
48     | -0.031547      | -0.052127      | 0.003118       | 0.000270       | 0.199442       | 0.200172       | 0.096411       | -0.030997      | -0.045070      | 0.144166       | 0.142667       | -0.124918      | -0.009057      | 0.131789       | 0.130250       | 0.008629       | 0.186918       | 0.187189       | 0.246831       | 0.248230       | 0.185749      
49     | -0.020651      | 0.024275       | 0.015930       | -0.029842      | 0.197077       | 0.195878       | 0.182475       | -0.023968      | -0.002389      | 0.173983       | 0.173919       | -0.093916      | 0.028008       | 0.171988       | 0.172003       | -0.023843      | 0.229922       | 0.230856       | 0.212137       | 0.213278       | 0.197432      
50     | -0.062004      | -0.042507      | 0.040103       | -0.027151      | 0.206653       | 0.204295       | 0.106312       | -0.043829      | -0.016225      | 0.148604       | 0.148080       | -0.162495      | 0.026322       | 0.139015       | 0.137451       | 0.000721       | 0.184137       | 0.185704       | 0.236756       | 0.237000       | 0.185671      
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
🛡️  SHADOW DEFENSE SUMMARY (computed only, NOT applied)
  Parameters: n=7, f=2, k=3, m=5, beta=2, rounds=50
  Krum        : attacker selection rate = 0.0000   (chance = A/n = 0.2857)   [rounds where the selected update is malicious]
  Multi-Krum  : DR = 0.0000  FPR = 0.4000  ER = 1.0000   (chance DR = FPR = (n-m)/n = 0.2857)
  Trimmed Mean: DR = 0.4896  FPR = 0.6042  ER = 0.5104   (chance = 2*beta/n = 0.5714)   [DR/FPR = mean trim fraction over attacker/benign submissions]
  Median      : attacker provider rate = 0.1729  attacker total influence = 0.3458  benign provider rate = 0.1308   (chance per client = 1/n = 0.1429)   [no rejection step: DR/FPR n/a]
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
💾 SAVING DATA TO CSV FILES FOR EASY COLLECTION
--------------------------------------------------------------------------------
✅ Global Accuracy saved to: results/qwen_ag_news_rmp_alpha0p3_seed42069_shadow_global_accuracy.csv
✅ Cosine Similarity saved to: results/qwen_ag_news_rmp_alpha0p3_seed42069_shadow_cosine_similarity.csv
✅ Local Accuracy saved to: results/qwen_ag_news_rmp_alpha0p3_seed42069_shadow_local_accuracy.csv

================================================================================
✅ All statistics printed and saved to CSV files!
   You can now easily collect data from multiple runs and compare them.
================================================================================

======================================================================================================================
⏱️  PER-ROUND OVERHEAD SUMMARY (wall-clock seconds)  --  GPU: NVIDIA RTX PRO 6000 Blackwell Server Edition
======================================================================================================================
Attacker columns are summed over all attackers of the round; GRL = select+graph+vgae+spectral+expand;
optimize = the K-step manipulation loop; diag = logging-only forwards; eval_local = per-client test-set
evaluation kept for the local-accuracy figure (experiment bookkeeping, not part of the FL protocol).
----------------------------------------------------------------------------------------------------------------------------------------
     round      GRL    setup  optimize  steps  finalize    diag    attack   att_GB  train_ben aggregate  eval_glob   eval_loc      round
----------------------------------------------------------------------------------------------------------------------------------------
         1    0.000     0.00      0.00      0      0.00    0.00      0.09        -     120.84      0.18       6.92       8.59     136.72
         2    0.000     0.00      0.00      0      0.00    0.00      0.10        -     119.44      0.13       6.93       7.95     134.62
         3    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.18      0.13       6.93       7.62     134.02
         4    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.46      0.11       6.93       7.55     134.21
         5    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.49      0.11       6.93       7.56     134.25
         6    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.48      0.12       6.93       7.56     134.25
         7    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.49      0.11       6.93       7.56     134.25
         8    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.40      0.12       6.93       7.54     134.15
         9    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.44      0.11       6.93       7.60     134.22
        10    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.21      0.11       6.94       7.58     133.99
        11    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.27      0.14       6.93       7.61     134.11
        12    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.26      0.11       6.94       7.60     134.02
        13    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.36      0.10       6.94       7.60     134.12
        14    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.54      0.11       6.93       7.59     134.33
        15    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.51      0.11       6.93       7.58     134.29
        16    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.29      0.11       6.93       7.56     134.05
        17    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.19      0.11       6.93       7.56     133.96
        18    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.17      0.11       6.93       7.58     133.93
        19    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.33      0.11       6.93       7.57     134.11
        20    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.17      0.11       6.93       7.58     133.94
        21    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.19      0.12       6.93       7.57     133.98
        22    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.52      0.12       6.93       7.54     134.26
        23    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.43      0.11       6.93       7.56     134.17
        24    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.28      0.11       6.93       7.56     134.06
        25    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.46      0.11       6.93       7.53     134.17
        26    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.30      0.10       6.93       7.58     134.06
        27    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.18      0.12       6.93       7.56     133.96
        28    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.20      0.11       6.93       7.60     134.01
        29    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.23      0.11       6.93       7.60     134.01
        30    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.18      0.11       6.93       7.56     133.93
        31    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.15      0.11       6.93       7.58     133.93
        32    0.000     0.00      0.00      0      0.00    0.00      0.10        -     119.23      0.11       6.93       7.56     133.99
        33    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.18      0.11       6.93       7.58     133.95
        34    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.21      0.11       6.93       7.60     133.99
        35    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.20      0.11       6.93       7.60     133.98
        36    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.53      0.12       6.93       7.58     134.32
        37    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.23      0.11       6.93       7.55     133.94
        38    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.20      0.11       6.93       7.58     133.97
        39    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.47      0.10       6.93       7.56     134.23
        40    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.21      0.11       6.94       7.57     133.93
        41    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.19      0.11       6.93       7.57     133.96
        42    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.19      0.11       6.93       7.57     133.96
        43    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.20      0.11       6.93       7.56     133.94
        44    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.38      0.11       6.93       7.58     134.16
        45    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.52      0.11       6.93       7.58     134.31
        46    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.48      0.11       6.93       7.57     134.24
        47    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.48      0.12       6.93       7.58     134.26
        48    0.000     0.00      0.00      0      0.00    0.00      0.08        -     119.49      0.11       6.93       7.58     134.25
        49    0.000     0.00      0.00      0      0.00    0.00      0.09        -     119.54      0.11       6.93       7.57     134.31
        50    0.000     0.00      0.00      0      0.00    0.00      0.07        -     119.50      0.11       6.93       7.58     134.27
----------------------------------------------------------------------------------------------------------------------------------------
 mean r>=2    0.000     0.00      0.00    0.0      0.00    0.00      0.08        -     119.33      0.11       6.93       7.58     134.11
  std r>=2    0.000     0.00      0.00    0.0      0.00    0.00      0.01        -       0.14      0.01       0.00       0.06       0.15
  mean all    0.000     0.00      0.00    0.0      0.00    0.00      0.09        -     119.36      0.11       6.93       7.60     134.16
   sum all    0.000     0.00      0.00    0.0      0.00    0.00      4.25        -    5968.10      5.65     346.55     380.07    6708.05
----------------------------------------------------------------------------------------------------------------------------------------

Wall-clock totals (s): setup_and_initial_eval_sec 29.0, rounds_sec 6726.7, experiment_sec 6755.7, rounds_completed 50.0
Overhead per round saved to: results/qwen_ag_news_rmp_alpha0p3_seed42069_shadow_overhead_rounds.csv
Overhead per attacker-round saved to: results/qwen_ag_news_rmp_alpha0p3_seed42069_shadow_overhead_attackers.csv

============================================================
Generating Visualization Plots
============================================================

============================================================
Generating Visualization Figures
============================================================

📊 Generating Figure 1: Global Accuracy Stability...
  ✅ Saved Figure 3 to: results/qwen_ag_news_rmp_alpha0p3_seed42069_shadow_figure1.png
📊 Generating Figure 2: Cosine Similarity...
  ✅ Saved Figure 4 to: results/qwen_ag_news_rmp_alpha0p3_seed42069_shadow_figure2.png
📊 Generating Figure 3: Local accuracy by client...
  ✅ Saved Figure 6 to: results/qwen_ag_news_rmp_alpha0p3_seed42069_shadow_figure3.png
📊 Generating Figure 4: Euclidean Distance...
  ✅ Saved Figure 4 to: results/qwen_ag_news_rmp_alpha0p3_seed42069_shadow_figure4.png
📊 Generating Figure 5: Global Loss...
  ✅ Saved Global Loss figure to: results/qwen_ag_news_rmp_alpha0p3_seed42069_shadow_figure5.png

✅ All available figures generated successfully!
   Output directory: results

⏱️  Total wall-clock incl. figures/checkpoint/downstream: 6757.6s (FL rounds 6726.7s, setup+initial eval 29.0s)

==================================================
Experiment Summary
==================================================
Total Rounds: 50
Final Clean Accuracy: 0.9090
Best Clean Accuracy: 0.9113
Accuracy Change: +0.4530

✅ Experiment completed successfully!
Full log saved to: results/qwen_ag_news_rmp_alpha0p3_seed42069_shadow_log.txt (1965 KB)