(this summary is also saved to results/qwen_ag_news_alie_alpha0p3_seed42069_shadow_summary.txt)
📊 Experiment Results Summary:
================================================================================

🎯 Overall Performance Metrics:
--------------------------------------------------------------------------------
  Total Rounds: 50
  Initial Clean Accuracy: 0.4567 (45.67%)
  Final Clean Accuracy: 0.9130 (91.30%)
  Accuracy Change: +0.4563 (+45.63%)
  Best Clean Accuracy: 0.9130 (91.30%) [Round 50]
  Worst Clean Accuracy: 0.4567 (45.67%) [Round 1]
  Average Clean Accuracy: 0.8744 (87.44%)
  Std Dev of Clean Accuracy: 0.0706 (7.06%)

  📈 Stability Metrics:
    Final |Δacc| (Stability): 0.0030
    Peak |Δacc|: 0.2457 [Round 1]
    Average |Δacc|: 0.0165
    Std Dev of |Δacc|: 0.0475

  📐 Update Statistics:
    Final Aggregated Update Norm: 0.162599
    Average Update Norm: 0.219006
    Max Update Norm: 0.980240 [Round 1]
    Min Update Norm: 0.150899 [Round 30]

  🔍 Defense Mechanism Detailed Analysis:
    Similarity Statistics (all clients, all rounds):
      Mean Similarity: 0.2672
      Std Dev: 0.1947
      Min: 0.0504
      Max: 0.8127
    Threshold Statistics:
      Mean Threshold: 0.0000
      Min Threshold: 0.0000
      Max Threshold: 0.0000
    Mean Similarity per Round:
      Average: 0.2672
      Std Dev: 0.1097
    Client Acceptance Statistics:
      Total Accepted: 350
      Total Rejected: 0
      Overall Acceptance Rate: 1.0000 (100.00%)

  📐 Euclidean Distance Statistics (all clients, all rounds):
      Mean Distance: 0.255717
      Std Dev: 0.136075
      Min: 0.060048
      Max: 0.782136
    Mean Euclidean Distance per Round:
      Average: 0.255717
      Std Dev: 0.061902
      Min (round): 0.218768 [Round 41]
      Max (round): 0.590680 [Round 1]

📈 Per-Round Summary (All Rounds):
-----------------------------------------------------------------------------------------------
Round   | Clean Acc   | |Δacc|    | Rej Rate    | Update Norm   | Mean Euc Dist  | Threshold  
-----------------------------------------------------------------------------------------------
1       | 0.4567      | 0.2457    | 0.0000      | 0.980240      | 0.590680       | 0.0000     
2       | 0.6940      | 0.2373    | 0.0000      | 0.783093      | 0.444878       | 0.0000     
3       | 0.7750      | 0.0810    | 0.0000      | 0.539807      | 0.362341       | 0.0000     
4       | 0.8080      | 0.0330    | 0.0000      | 0.390323      | 0.311801       | 0.0000     
5       | 0.8237      | 0.0157    | 0.0000      | 0.318115      | 0.297555       | 0.0000     
6       | 0.8343      | 0.0107    | 0.0000      | 0.272651      | 0.283368       | 0.0000     
7       | 0.8480      | 0.0137    | 0.0000      | 0.244039      | 0.276475       | 0.0000     
8       | 0.8580      | 0.0100    | 0.0000      | 0.231735      | 0.275706       | 0.0000     
9       | 0.8770      | 0.0190    | 0.0000      | 0.236953      | 0.279179       | 0.0000     
10      | 0.8770      | 0.0000    | 0.0000      | 0.225568      | 0.272031       | 0.0000     
11      | 0.8883      | 0.0113    | 0.0000      | 0.217608      | 0.271781       | 0.0000     
12      | 0.8853      | 0.0030    | 0.0000      | 0.206104      | 0.262715       | 0.0000     
13      | 0.8890      | 0.0037    | 0.0000      | 0.205086      | 0.260730       | 0.0000     
14      | 0.8857      | 0.0033    | 0.0000      | 0.197401      | 0.258088       | 0.0000     
15      | 0.8863      | 0.0007    | 0.0000      | 0.194476      | 0.254249       | 0.0000     
16      | 0.8880      | 0.0017    | 0.0000      | 0.195198      | 0.256451       | 0.0000     
17      | 0.8893      | 0.0013    | 0.0000      | 0.186655      | 0.249157       | 0.0000     
18      | 0.8863      | 0.0030    | 0.0000      | 0.188816      | 0.253199       | 0.0000     
19      | 0.8880      | 0.0017    | 0.0000      | 0.177976      | 0.247522       | 0.0000     
20      | 0.8900      | 0.0020    | 0.0000      | 0.172279      | 0.244215       | 0.0000     
21      | 0.8830      | 0.0070    | 0.0000      | 0.171774      | 0.241067       | 0.0000     
22      | 0.8847      | 0.0017    | 0.0000      | 0.168247      | 0.237874       | 0.0000     
23      | 0.8913      | 0.0067    | 0.0000      | 0.163124      | 0.235214       | 0.0000     
24      | 0.8837      | 0.0077    | 0.0000      | 0.156230      | 0.230019       | 0.0000     
25      | 0.9003      | 0.0167    | 0.0000      | 0.157863      | 0.227859       | 0.0000     
26      | 0.8953      | 0.0050    | 0.0000      | 0.159176      | 0.228935       | 0.0000     
27      | 0.8947      | 0.0007    | 0.0000      | 0.155508      | 0.224382       | 0.0000     
28      | 0.8997      | 0.0050    | 0.0000      | 0.157480      | 0.226765       | 0.0000     
29      | 0.9020      | 0.0023    | 0.0000      | 0.151999      | 0.222029       | 0.0000     
30      | 0.8943      | 0.0077    | 0.0000      | 0.150899      | 0.221632       | 0.0000     
31      | 0.8937      | 0.0007    | 0.0000      | 0.152572      | 0.225859       | 0.0000     
32      | 0.8980      | 0.0043    | 0.0000      | 0.154035      | 0.219236       | 0.0000     
33      | 0.8957      | 0.0023    | 0.0000      | 0.156667      | 0.225877       | 0.0000     
34      | 0.8980      | 0.0023    | 0.0000      | 0.156015      | 0.225425       | 0.0000     
35      | 0.9020      | 0.0040    | 0.0000      | 0.157987      | 0.227359       | 0.0000     
36      | 0.9017      | 0.0003    | 0.0000      | 0.157360      | 0.228650       | 0.0000     
37      | 0.9027      | 0.0010    | 0.0000      | 0.157053      | 0.225649       | 0.0000     
38      | 0.8997      | 0.0030    | 0.0000      | 0.163636      | 0.235153       | 0.0000     
39      | 0.9063      | 0.0067    | 0.0000      | 0.157425      | 0.222033       | 0.0000     
40      | 0.9003      | 0.0060    | 0.0000      | 0.163718      | 0.227106       | 0.0000     
41      | 0.9053      | 0.0050    | 0.0000      | 0.152760      | 0.218768       | 0.0000     
42      | 0.9013      | 0.0040    | 0.0000      | 0.158798      | 0.226130       | 0.0000     
43      | 0.9083      | 0.0070    | 0.0000      | 0.160845      | 0.224480       | 0.0000     
44      | 0.9040      | 0.0043    | 0.0000      | 0.154665      | 0.222148       | 0.0000     
45      | 0.9050      | 0.0010    | 0.0000      | 0.166110      | 0.230707       | 0.0000     
46      | 0.9063      | 0.0013    | 0.0000      | 0.164262      | 0.230878       | 0.0000     
47      | 0.9020      | 0.0043    | 0.0000      | 0.155807      | 0.223949       | 0.0000     
48      | 0.9080      | 0.0060    | 0.0000      | 0.169406      | 0.237154       | 0.0000     
49      | 0.9100      | 0.0020    | 0.0000      | 0.172176      | 0.237181       | 0.0000     
50      | 0.9130      | 0.0030    | 0.0000      | 0.162599      | 0.224230       | 0.0000     

--------------------------------------------------------------------------------
📐 COSINE SIMILARITY (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A) | Mean | Std
--------------------------------------------------------------------------------
1      | 0.625569       | 0.612901       | 0.578039       | 0.652474       | 0.631754       | 0.804432       | 0.804432       | 0.672800 | 0.085815
2      | 0.692583       | 0.632574       | 0.493357       | 0.660443       | 0.677867       | 0.812746       | 0.812746       | 0.683188 | 0.101982
3      | 0.586602       | 0.500550       | 0.419542       | 0.540418       | 0.575656       | 0.755497       | 0.755497       | 0.590538 | 0.116195
4      | 0.475413       | 0.392811       | 0.360430       | 0.406714       | 0.465359       | 0.695353       | 0.695353       | 0.498776 | 0.129720
5      | 0.377631       | 0.282641       | 0.275377       | 0.303400       | 0.366260       | 0.631304       | 0.631304       | 0.409702 | 0.144725
6      | 0.297294       | 0.194032       | 0.221528       | 0.250833       | 0.311662       | 0.585779       | 0.585779       | 0.349558 | 0.154039
7      | 0.235443       | 0.187983       | 0.157804       | 0.212344       | 0.261498       | 0.553011       | 0.553011       | 0.308728 | 0.157479
8      | 0.196649       | 0.156034       | 0.114952       | 0.198283       | 0.229144       | 0.528095       | 0.528095       | 0.278750 | 0.161206
9      | 0.208029       | 0.173731       | 0.133834       | 0.193505       | 0.240002       | 0.536928       | 0.536928       | 0.288994 | 0.159632
10     | 0.188755       | 0.157232       | 0.102613       | 0.194487       | 0.221722       | 0.523731       | 0.523731       | 0.273182 | 0.162154
11     | 0.187813       | 0.139140       | 0.061164       | 0.164773       | 0.213969       | 0.509702       | 0.509702       | 0.255181 | 0.166939
12     | 0.154652       | 0.131256       | 0.068086       | 0.160038       | 0.210743       | 0.502312       | 0.502312       | 0.247057 | 0.166124
13     | 0.175157       | 0.131318       | 0.076819       | 0.152396       | 0.204454       | 0.504793       | 0.504793       | 0.249961 | 0.165235
14     | 0.163184       | 0.134224       | 0.084741       | 0.143020       | 0.186402       | 0.500720       | 0.500720       | 0.244716 | 0.164433
15     | 0.159219       | 0.125936       | 0.069683       | 0.153164       | 0.182969       | 0.496976       | 0.496976       | 0.240703 | 0.165360
16     | 0.164115       | 0.117835       | 0.078245       | 0.143109       | 0.178979       | 0.495710       | 0.495710       | 0.239100 | 0.165066
17     | 0.159827       | 0.130833       | 0.084791       | 0.129141       | 0.177396       | 0.496468       | 0.496468       | 0.239275 | 0.164834
18     | 0.174841       | 0.125210       | 0.050409       | 0.127778       | 0.158877       | 0.488789       | 0.488789       | 0.230670 | 0.167214
19     | 0.150588       | 0.111285       | 0.065974       | 0.109875       | 0.151323       | 0.481280       | 0.481280       | 0.221658 | 0.166356
20     | 0.158614       | 0.107287       | 0.066654       | 0.077143       | 0.142229       | 0.474335       | 0.474335       | 0.214371 | 0.167159
21     | 0.136819       | 0.121219       | 0.077692       | 0.107669       | 0.146748       | 0.480996       | 0.480996       | 0.221734 | 0.165240
22     | 0.135561       | 0.097370       | 0.080646       | 0.092160       | 0.156886       | 0.476531       | 0.476531       | 0.216526 | 0.166238
23     | 0.130574       | 0.099617       | 0.069986       | 0.088857       | 0.142883       | 0.471651       | 0.471651       | 0.210746 | 0.166560
24     | 0.110596       | 0.115755       | 0.085320       | 0.076836       | 0.139244       | 0.471413       | 0.471413       | 0.210083 | 0.166356
25     | 0.150830       | 0.121828       | 0.071615       | 0.090671       | 0.131678       | 0.479154       | 0.479154       | 0.217847 | 0.167014
26     | 0.129621       | 0.124380       | 0.074418       | 0.092842       | 0.150531       | 0.479567       | 0.479567       | 0.218704 | 0.166579
27     | 0.147829       | 0.103110       | 0.092895       | 0.082842       | 0.136528       | 0.477732       | 0.477732       | 0.216953 | 0.166302
28     | 0.142270       | 0.120520       | 0.103282       | 0.080570       | 0.143913       | 0.482636       | 0.482636       | 0.222261 | 0.165922
29     | 0.123526       | 0.106848       | 0.078865       | 0.092463       | 0.141760       | 0.475068       | 0.475068       | 0.213371 | 0.166574
30     | 0.108040       | 0.118995       | 0.090220       | 0.082695       | 0.142984       | 0.474652       | 0.474652       | 0.213177 | 0.166362
31     | 0.116987       | 0.115286       | 0.075505       | 0.097074       | 0.121866       | 0.472142       | 0.472142       | 0.210143 | 0.166334
32     | 0.153713       | 0.110199       | 0.094358       | 0.104488       | 0.132890       | 0.483902       | 0.483902       | 0.223350 | 0.165778
33     | 0.123578       | 0.098196       | 0.068524       | 0.107915       | 0.139594       | 0.473622       | 0.473622       | 0.212150 | 0.166615
34     | 0.130422       | 0.120527       | 0.103092       | 0.098456       | 0.129496       | 0.480901       | 0.480901       | 0.220542 | 0.165049
35     | 0.113795       | 0.118480       | 0.097568       | 0.091165       | 0.154121       | 0.479540       | 0.479540       | 0.219172 | 0.165715
36     | 0.112290       | 0.117324       | 0.092982       | 0.082461       | 0.148867       | 0.475903       | 0.475903       | 0.215104 | 0.166072
37     | 0.105270       | 0.118828       | 0.105012       | 0.111451       | 0.143438       | 0.481164       | 0.481164       | 0.220904 | 0.165043
38     | 0.123463       | 0.106126       | 0.073090       | 0.087437       | 0.142831       | 0.470470       | 0.470470       | 0.210555 | 0.165721
39     | 0.140856       | 0.126434       | 0.098917       | 0.120110       | 0.138337       | 0.488532       | 0.488532       | 0.228817 | 0.164751
40     | 0.128928       | 0.109309       | 0.105586       | 0.119824       | 0.165908       | 0.488699       | 0.488699       | 0.229565 | 0.164905
41     | 0.128918       | 0.120380       | 0.101093       | 0.080855       | 0.164985       | 0.484366       | 0.484366       | 0.223566 | 0.166663
42     | 0.124298       | 0.113530       | 0.100609       | 0.087815       | 0.160798       | 0.481307       | 0.481307       | 0.221380 | 0.165735
43     | 0.143859       | 0.125984       | 0.112164       | 0.110992       | 0.148723       | 0.490529       | 0.490529       | 0.231826 | 0.164152
44     | 0.134878       | 0.117893       | 0.107949       | 0.087923       | 0.144901       | 0.483070       | 0.483070       | 0.222812 | 0.165472
45     | 0.139670       | 0.135188       | 0.108590       | 0.116966       | 0.153037       | 0.492354       | 0.492354       | 0.234023 | 0.163941
46     | 0.142531       | 0.116701       | 0.089873       | 0.115527       | 0.137235       | 0.483390       | 0.483390       | 0.224093 | 0.164751
47     | 0.142931       | 0.102254       | 0.080089       | 0.084058       | 0.149542       | 0.477744       | 0.477744       | 0.216337 | 0.167158
48     | 0.126991       | 0.108823       | 0.090461       | 0.114506       | 0.154654       | 0.482127       | 0.482127       | 0.222813 | 0.164992
49     | 0.123657       | 0.129306       | 0.127969       | 0.129183       | 0.155872       | 0.492337       | 0.492337       | 0.235809 | 0.162535
50     | 0.169343       | 0.139028       | 0.108531       | 0.114644       | 0.146919       | 0.497573       | 0.497573       | 0.239087 | 0.164548
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
📏 EUCLIDEAN DISTANCE (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A) | Mean | Std
--------------------------------------------------------------------------------
1      | 0.720415       | 0.744663       | 0.782136       | 0.765626       | 0.754365       | 0.183776       | 0.183776       | 0.590680 | 0.257942
2      | 0.517642       | 0.569055       | 0.671576       | 0.556356       | 0.511131       | 0.144193       | 0.144193       | 0.444878 | 0.196304
3      | 0.455659       | 0.440125       | 0.494431       | 0.468007       | 0.457744       | 0.110210       | 0.110210       | 0.362341 | 0.160184
4      | 0.399283       | 0.361289       | 0.386764       | 0.428457       | 0.427823       | 0.089495       | 0.089495       | 0.311801 | 0.142243
5      | 0.399735       | 0.336334       | 0.353872       | 0.417490       | 0.409264       | 0.083096       | 0.083096       | 0.297555 | 0.138340
6      | 0.394263       | 0.324395       | 0.335986       | 0.387440       | 0.384010       | 0.078742       | 0.078742       | 0.283368 | 0.131721
7      | 0.376062       | 0.309030       | 0.328706       | 0.393514       | 0.374779       | 0.076616       | 0.076616       | 0.276475 | 0.129259
8      | 0.363905       | 0.305584       | 0.326198       | 0.389500       | 0.392110       | 0.076321       | 0.076321       | 0.275706 | 0.129410
9      | 0.377685       | 0.307842       | 0.329316       | 0.393501       | 0.392082       | 0.076913       | 0.076913       | 0.279179 | 0.131300
10     | 0.368306       | 0.299995       | 0.319701       | 0.389153       | 0.377816       | 0.074624       | 0.074624       | 0.272031 | 0.128269
11     | 0.373735       | 0.303441       | 0.329962       | 0.382691       | 0.363946       | 0.074346       | 0.074346       | 0.271781 | 0.127357
12     | 0.349837       | 0.289650       | 0.315070       | 0.378873       | 0.362059       | 0.071757       | 0.071757       | 0.262715 | 0.123837
13     | 0.353814       | 0.289407       | 0.313516       | 0.365434       | 0.359713       | 0.071613       | 0.071613       | 0.260730 | 0.122220
14     | 0.359381       | 0.288636       | 0.308222       | 0.358118       | 0.351685       | 0.070288       | 0.070288       | 0.258088 | 0.121309
15     | 0.352384       | 0.287426       | 0.304802       | 0.362158       | 0.333905       | 0.069533       | 0.069533       | 0.254249 | 0.119234
16     | 0.345407       | 0.292622       | 0.304199       | 0.360335       | 0.352238       | 0.070177       | 0.070177       | 0.256451 | 0.120038
17     | 0.340681       | 0.285484       | 0.297195       | 0.348256       | 0.336597       | 0.067944       | 0.067944       | 0.249157 | 0.116586
18     | 0.347136       | 0.290131       | 0.305268       | 0.348864       | 0.342321       | 0.069337       | 0.069337       | 0.253199 | 0.118083
19     | 0.332348       | 0.283064       | 0.302168       | 0.339599       | 0.339986       | 0.067744       | 0.067744       | 0.247522 | 0.115334
20     | 0.338133       | 0.276230       | 0.292541       | 0.331252       | 0.338269       | 0.066539       | 0.066539       | 0.244215 | 0.114480
21     | 0.332612       | 0.276806       | 0.291781       | 0.324215       | 0.329396       | 0.066330       | 0.066330       | 0.241067 | 0.112130
22     | 0.322564       | 0.275114       | 0.286000       | 0.329002       | 0.321982       | 0.065227       | 0.065227       | 0.237874 | 0.110755
23     | 0.321716       | 0.269914       | 0.291446       | 0.320890       | 0.313146       | 0.064692       | 0.064692       | 0.235214 | 0.109164
24     | 0.309609       | 0.271550       | 0.279473       | 0.306505       | 0.316419       | 0.063288       | 0.063288       | 0.230019 | 0.106515
25     | 0.306356       | 0.270064       | 0.283755       | 0.303646       | 0.306876       | 0.062158       | 0.062158       | 0.227859 | 0.105538
26     | 0.308421       | 0.270482       | 0.285321       | 0.315206       | 0.297118       | 0.062998       | 0.062998       | 0.228935 | 0.105820
27     | 0.304893       | 0.262246       | 0.277272       | 0.305062       | 0.298204       | 0.061497       | 0.061497       | 0.224382 | 0.104016
28     | 0.305362       | 0.266981       | 0.276609       | 0.311010       | 0.303377       | 0.062008       | 0.062008       | 0.226765 | 0.105245
29     | 0.293559       | 0.260654       | 0.279231       | 0.307555       | 0.292166       | 0.060519       | 0.060519       | 0.222029 | 0.103016
30     | 0.301442       | 0.262096       | 0.272194       | 0.282792       | 0.311587       | 0.060657       | 0.060657       | 0.221632 | 0.102971
31     | 0.301101       | 0.265874       | 0.286020       | 0.307204       | 0.296363       | 0.062224       | 0.062224       | 0.225859 | 0.104213
32     | 0.291572       | 0.259757       | 0.272309       | 0.292711       | 0.298208       | 0.060048       | 0.060048       | 0.219236 | 0.101424
33     | 0.300703       | 0.269082       | 0.282901       | 0.304959       | 0.298109       | 0.062692       | 0.062692       | 0.225877 | 0.103818
34     | 0.303817       | 0.261388       | 0.274292       | 0.301088       | 0.314639       | 0.061375       | 0.061375       | 0.225425 | 0.105109
35     | 0.293349       | 0.265775       | 0.278164       | 0.314651       | 0.314998       | 0.062288       | 0.062288       | 0.227359 | 0.105701
36     | 0.311028       | 0.266117       | 0.280142       | 0.298809       | 0.318866       | 0.062792       | 0.062792       | 0.228650 | 0.106181
37     | 0.287661       | 0.263505       | 0.280463       | 0.303882       | 0.319426       | 0.062301       | 0.062301       | 0.225649 | 0.104583
38     | 0.304105       | 0.264802       | 0.281379       | 0.328591       | 0.338773       | 0.064209       | 0.064209       | 0.235153 | 0.110636
39     | 0.294882       | 0.259497       | 0.278260       | 0.305371       | 0.293994       | 0.061114       | 0.061114       | 0.222033 | 0.102668
40     | 0.304086       | 0.267025       | 0.272583       | 0.315165       | 0.306926       | 0.061981       | 0.061981       | 0.227106 | 0.105726
41     | 0.292299       | 0.262253       | 0.273327       | 0.285407       | 0.297468       | 0.060312       | 0.060312       | 0.218768 | 0.100801
42     | 0.297975       | 0.266401       | 0.272361       | 0.311858       | 0.309992       | 0.062160       | 0.062160       | 0.226130 | 0.104932
43     | 0.299126       | 0.262520       | 0.271292       | 0.299265       | 0.316072       | 0.061543       | 0.061543       | 0.224480 | 0.104396
44     | 0.298943       | 0.264046       | 0.271016       | 0.295448       | 0.303586       | 0.060998       | 0.060998       | 0.222148 | 0.102807
45     | 0.314299       | 0.266472       | 0.279598       | 0.318661       | 0.309623       | 0.063147       | 0.063147       | 0.230707 | 0.107420
46     | 0.299396       | 0.271483       | 0.278399       | 0.325625       | 0.314102       | 0.063572       | 0.063572       | 0.230878 | 0.107230
47     | 0.311126       | 0.270975       | 0.277763       | 0.282620       | 0.301931       | 0.061614       | 0.061614       | 0.223949 | 0.103466
48     | 0.313780       | 0.277664       | 0.289550       | 0.298216       | 0.349912       | 0.065476       | 0.065476       | 0.237154 | 0.110613
49     | 0.299553       | 0.272171       | 0.282906       | 0.360767       | 0.314089       | 0.065389       | 0.065389       | 0.237181 | 0.111751
50     | 0.313066       | 0.263016       | 0.275397       | 0.296098       | 0.299870       | 0.061080       | 0.061080       | 0.224230 | 0.104291
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
📉 GLOBAL LOSS (Per Round)
--------------------------------------------------------------------------------
Round    | Global Loss    
--------------------------------------------------------------------------------
1        | 1.991154       
2        | 0.966186       
3        | 0.660474       
4        | 0.547519       
5        | 0.525599       
6        | 0.489649       
7        | 0.461563       
8        | 0.453002       
9        | 0.405915       
10       | 0.404065       
11       | 0.381145       
12       | 0.410645       
13       | 0.399374       
14       | 0.431015       
15       | 0.447248       
16       | 0.449755       
17       | 0.459933       
18       | 0.511479       
19       | 0.518287       
20       | 0.533837       
21       | 0.587086       
22       | 0.603987       
23       | 0.606484       
24       | 0.648768       
25       | 0.584001       
26       | 0.660172       
27       | 0.654098       
28       | 0.643877       
29       | 0.632248       
30       | 0.695093       
31       | 0.741947       
32       | 0.701255       
33       | 0.765545       
34       | 0.730146       
35       | 0.734020       
36       | 0.737638       
37       | 0.770239       
38       | 0.799902       
39       | 0.761986       
40       | 0.790760       
41       | 0.758204       
42       | 0.795020       
43       | 0.772579       
44       | 0.791023       
45       | 0.804658       
46       | 0.790038       
47       | 0.860566       
48       | 0.850122       
49       | 0.784418       
50       | 0.765824       
--------------------------------------------------------------------------------

📊 Local Accuracies Analysis:
--------------------------------------------------------------------------------
Client ID    | Initial     | Final       | Change      | Average     | Std Dev     | Best        | Worst      
--------------------------------------------------------------------------------
Client 0      | 0.5924      | 0.8859      |     +0.2935 | 0.8738      | 0.0451      | 0.9022      | 0.5924     
Client 1      | 0.2228      | 0.8641      |     +0.6413 | 0.8317      | 0.1020      | 0.8967      | 0.2228     
Client 2      | 0.3261      | 0.8098      |     +0.4837 | 0.7599      | 0.0972      | 0.8424      | 0.3261     
Client 3      | 0.5924      | 0.8207      |     +0.2283 | 0.7163      | 0.0449      | 0.8207      | 0.5924     
Client 4      | 0.4457      | 0.8478      |     +0.4022 | 0.7498      | 0.0791      | 0.8533      | 0.4457     
Client 5      | 0.2228      | 0.8859      |     +0.6630 | 0.8424      | 0.1163      | 0.9022      | 0.2228     
Client 6      | 0.2228      | 0.8859      |     +0.6630 | 0.8424      | 0.1163      | 0.9022      | 0.2228     

  📈 Cross-Client Statistics:
    Final Accuracy - Mean: 0.8571, Std: 0.0297
    Final Accuracy - Best Client: 0.8859, Worst: 0.8098
    Final Accuracy - Range: 0.0761
    Initial Accuracy - Mean: 0.3750, Std: 0.1565
    Average Accuracy (all rounds) - Mean: 0.8023, Std: 0.0550

⚙️  Complete Experiment Configuration:
================================================================================

📋 Experiment Configuration:
  experiment_name: qwen_ag_news_alie_alpha0p3_seed42069_shadow
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
  experiment_name: qwen_ag_news_alie_alpha0p3_seed42069_shadow
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
⏱️  Overhead round 1 (wall-clock s): round 136.58 | broadcast 0.03 | prepare 0.00 | benign train 120.82 [0:30.8 1:11.2 2:9.9 3:34.0 4:34.9] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.17 | observe 0.00 | eval_global 6.92 | eval_local 8.59 (bookkeeping) | unaccounted 0.01
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 2 (wall-clock s): round 134.47 | broadcast 0.02 | prepare 0.00 | benign train 119.31 [0:30.3 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 8.01 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 3 (wall-clock s): round 134.36 | broadcast 0.02 | prepare 0.00 | benign train 119.55 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.62 (bookkeeping) | unaccounted 0.06
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 4 (wall-clock s): round 134.29 | broadcast 0.02 | prepare 0.00 | benign train 119.55 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.05 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.59 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 5 (wall-clock s): round 134.33 | broadcast 0.02 | prepare 0.00 | benign train 119.55 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.05 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.62 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 6 (wall-clock s): round 134.22 | broadcast 0.02 | prepare 0.00 | benign train 119.46 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.05 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.58 (bookkeeping) | unaccounted 0.07
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 7 (wall-clock s): round 134.27 | broadcast 0.03 | prepare 0.00 | benign train 119.56 [0:30.3 1:11.0 2:9.7 3:33.9 4:34.7] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.57 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 8 (wall-clock s): round 134.22 | broadcast 0.02 | prepare 0.00 | benign train 119.51 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.05 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.56 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.04s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 9 (wall-clock s): round 134.21 | broadcast 0.03 | prepare 0.00 | benign train 119.50 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.03 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.58 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 10 (wall-clock s): round 134.24 | broadcast 0.03 | prepare 0.00 | benign train 119.51 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.57 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 11 (wall-clock s): round 134.29 | broadcast 0.02 | prepare 0.00 | benign train 119.53 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.05 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.59 (bookkeeping) | unaccounted 0.05
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 12 (wall-clock s): round 134.24 | broadcast 0.03 | prepare 0.00 | benign train 119.52 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.05 [5:0.0 6:0.0] | aggregate 0.10 | observe 0.00 | eval_global 6.93 | eval_local 7.55 (bookkeeping) | unaccounted 0.05
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 13 (wall-clock s): round 134.09 | broadcast 0.03 | prepare 0.00 | benign train 119.41 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.54 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 14 (wall-clock s): round 134.03 | broadcast 0.02 | prepare 0.00 | benign train 119.30 [0:30.2 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.60 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 15 (wall-clock s): round 134.04 | broadcast 0.03 | prepare 0.00 | benign train 119.36 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.03 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.54 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.01s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 16 (wall-clock s): round 134.12 | broadcast 0.03 | prepare 0.00 | benign train 119.38 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.59 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 17 (wall-clock s): round 133.98 | broadcast 0.03 | prepare 0.00 | benign train 119.24 [0:30.2 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.03 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.60 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 18 (wall-clock s): round 133.98 | broadcast 0.03 | prepare 0.00 | benign train 119.20 [0:30.2 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.05 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.62 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 19 (wall-clock s): round 133.99 | broadcast 0.03 | prepare 0.00 | benign train 119.24 [0:30.2 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.59 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 20 (wall-clock s): round 133.97 | broadcast 0.03 | prepare 0.00 | benign train 119.26 [0:30.3 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.57 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 21 (wall-clock s): round 133.98 | broadcast 0.03 | prepare 0.00 | benign train 119.20 [0:30.2 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.05 [5:0.0 6:0.0] | aggregate 0.10 | observe 0.00 | eval_global 6.94 | eval_local 7.61 (bookkeeping) | unaccounted 0.05
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 22 (wall-clock s): round 133.90 | broadcast 0.02 | prepare 0.00 | benign train 119.21 [0:30.2 1:10.9 2:9.7 3:33.7 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.55 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 23 (wall-clock s): round 134.12 | broadcast 0.02 | prepare 0.00 | benign train 119.31 [0:30.3 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.15 | observe 0.00 | eval_global 6.93 | eval_local 7.63 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 24 (wall-clock s): round 133.93 | broadcast 0.03 | prepare 0.00 | benign train 119.22 [0:30.2 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.56 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 25 (wall-clock s): round 134.00 | broadcast 0.03 | prepare 0.00 | benign train 119.21 [0:30.2 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.05 [5:0.0 6:0.0] | aggregate 0.12 | observe 0.00 | eval_global 6.93 | eval_local 7.59 (bookkeeping) | unaccounted 0.06
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 26 (wall-clock s): round 133.99 | broadcast 0.03 | prepare 0.00 | benign train 119.21 [0:30.2 1:10.9 2:9.7 3:33.7 4:34.6] | attack 0.05 [5:0.0 6:0.0] | aggregate 0.14 | observe 0.00 | eval_global 6.93 | eval_local 7.57 (bookkeeping) | unaccounted 0.06
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 27 (wall-clock s): round 133.93 | broadcast 0.03 | prepare 0.00 | benign train 119.20 [0:30.2 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.58 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 28 (wall-clock s): round 134.00 | broadcast 0.03 | prepare 0.00 | benign train 119.25 [0:30.2 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.05 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.60 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 29 (wall-clock s): round 134.26 | broadcast 0.02 | prepare 0.00 | benign train 119.53 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.03 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.59 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 30 (wall-clock s): round 134.25 | broadcast 0.03 | prepare 0.00 | benign train 119.52 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.05 [5:0.0 6:0.0] | aggregate 0.12 | observe 0.00 | eval_global 6.93 | eval_local 7.56 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 31 (wall-clock s): round 134.08 | broadcast 0.02 | prepare 0.00 | benign train 119.29 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.64 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 32 (wall-clock s): round 133.98 | broadcast 0.03 | prepare 0.00 | benign train 119.23 [0:30.2 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.59 (bookkeeping) | unaccounted 0.05
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 33 (wall-clock s): round 134.00 | broadcast 0.03 | prepare 0.00 | benign train 119.23 [0:30.2 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.62 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 34 (wall-clock s): round 134.01 | broadcast 0.03 | prepare 0.00 | benign train 119.23 [0:30.2 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.61 (bookkeeping) | unaccounted 0.06
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 35 (wall-clock s): round 134.19 | broadcast 0.03 | prepare 0.00 | benign train 119.43 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.05 [5:0.0 6:0.0] | aggregate 0.10 | observe 0.00 | eval_global 6.94 | eval_local 7.59 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.04s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 36 (wall-clock s): round 134.04 | broadcast 0.03 | prepare 0.00 | benign train 119.28 [0:30.3 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.59 (bookkeeping) | unaccounted 0.05
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 37 (wall-clock s): round 134.09 | broadcast 0.02 | prepare 0.00 | benign train 119.33 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.61 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 38 (wall-clock s): round 134.01 | broadcast 0.03 | prepare 0.00 | benign train 119.28 [0:30.3 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.58 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 39 (wall-clock s): round 134.07 | broadcast 0.03 | prepare 0.00 | benign train 119.31 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.05 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.60 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.01s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 40 (wall-clock s): round 134.07 | broadcast 0.03 | prepare 0.00 | benign train 119.30 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.62 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 41 (wall-clock s): round 134.20 | broadcast 0.03 | prepare 0.00 | benign train 119.37 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.05 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.65 (bookkeeping) | unaccounted 0.05
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 42 (wall-clock s): round 134.10 | broadcast 0.03 | prepare 0.00 | benign train 119.31 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.12 | observe 0.00 | eval_global 6.94 | eval_local 7.62 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 43 (wall-clock s): round 134.09 | broadcast 0.03 | prepare 0.00 | benign train 119.32 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.62 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 44 (wall-clock s): round 134.05 | broadcast 0.03 | prepare 0.00 | benign train 119.30 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.60 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 45 (wall-clock s): round 134.08 | broadcast 0.03 | prepare 0.00 | benign train 119.33 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.60 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 46 (wall-clock s): round 134.06 | broadcast 0.03 | prepare 0.00 | benign train 119.34 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.56 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 47 (wall-clock s): round 134.09 | broadcast 0.03 | prepare 0.00 | benign train 119.34 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.60 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 48 (wall-clock s): round 134.01 | broadcast 0.03 | prepare 0.00 | benign train 119.28 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.58 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 49 (wall-clock s): round 134.09 | broadcast 0.03 | prepare 0.00 | benign train 119.33 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.03 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.62 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)
⏱️  Overhead round 50 (wall-clock s): round 134.19 | broadcast 0.02 | prepare 0.00 | benign train 119.45 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.13 | observe 0.00 | eval_global 6.94 | eval_local 7.58 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

================================================================================
🛡️  PER-ROUND SHADOW DEFENSES (re-printed from results.json; computed only, NOT applied)
================================================================================
[shadow] round 1
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=1.361764 krum=2.184508 mkrum=KEEP tm_trim=0.8067 (lo 0.4136 / hi 0.3930) med_prov=0.0247 d_med=0.802971
    [shadow] C1 (B): norm=0.606631 krum=0.931724 mkrum=KEEP tm_trim=0.7250 (lo 0.3788 / hi 0.3462) med_prov=0.0363 d_med=0.626460
    [shadow] C2 (B): norm=0.560976 krum=1.019077 mkrum=KEEP tm_trim=0.7328 (lo 0.3829 / hi 0.3499) med_prov=0.0362 d_med=0.660390
    [shadow] C3 (B): norm=1.518111 krum=2.456323 mkrum=REJECT tm_trim=0.8650 (lo 0.4426 / hi 0.4223) med_prov=0.0251 d_med=0.883313
    [shadow] C4 (B): norm=1.264700 krum=2.270075 mkrum=REJECT tm_trim=0.7272 (lo 0.3741 / hi 0.3531) med_prov=0.0210 d_med=0.790884
    [shadow] C5 (A): norm=0.883457 krum=0.848375 mkrum=KEEP tm_trim=0.0453 (lo 0.0000 / hi 0.0453) med_prov=0.1983 d_med=0.062792
    [shadow] C6 (A): norm=0.883457 krum=0.848375 mkrum=KEEP tm_trim=0.0981 (lo 0.0079 / hi 0.0902) med_prov=0.6584 d_med=0.062792
[shadow] round 2
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=1.091374 krum=1.288623 mkrum=KEEP tm_trim=0.7998 (lo 0.4114 / hi 0.3884) med_prov=0.0253 d_med=0.585321
    [shadow] C1 (B): norm=0.456474 krum=0.605912 mkrum=KEEP tm_trim=0.7279 (lo 0.3801 / hi 0.3478) med_prov=0.0357 d_med=0.474936
    [shadow] C2 (B): norm=0.444832 krum=0.809440 mkrum=KEEP tm_trim=0.7860 (lo 0.4069 / hi 0.3791) med_prov=0.0308 d_med=0.571752
    [shadow] C3 (B): norm=1.121806 krum=1.417320 mkrum=REJECT tm_trim=0.8141 (lo 0.4171 / hi 0.3970) med_prov=0.0224 d_med=0.642030
    [shadow] C4 (B): norm=1.015485 krum=1.345907 mkrum=REJECT tm_trim=0.7334 (lo 0.3780 / hi 0.3555) med_prov=0.0245 d_med=0.565322
    [shadow] C5 (A): norm=0.700432 krum=0.550280 mkrum=KEEP tm_trim=0.0365 (lo 0.0000 / hi 0.0365) med_prov=0.1800 d_med=0.048019
    [shadow] C6 (A): norm=0.700432 krum=0.550280 mkrum=KEEP tm_trim=0.1022 (lo 0.0066 / hi 0.0956) med_prov=0.6812 d_med=0.048019
[shadow] round 3
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.797187 krum=1.014705 mkrum=KEEP tm_trim=0.7992 (lo 0.4120 / hi 0.3872) med_prov=0.0281 d_med=0.494028
    [shadow] C1 (B): norm=0.343377 krum=0.425802 mkrum=KEEP tm_trim=0.7095 (lo 0.3739 / hi 0.3356) med_prov=0.0412 d_med=0.375456
    [shadow] C2 (B): norm=0.389968 krum=0.505683 mkrum=KEEP tm_trim=0.7489 (lo 0.3907 / hi 0.3583) med_prov=0.0355 d_med=0.424716
    [shadow] C3 (B): norm=0.788796 krum=1.058199 mkrum=REJECT tm_trim=0.7977 (lo 0.4108 / hi 0.3869) med_prov=0.0263 d_med=0.521085
    [shadow] C4 (B): norm=0.790543 krum=1.016121 mkrum=REJECT tm_trim=0.7869 (lo 0.4054 / hi 0.3815) med_prov=0.0266 d_med=0.504037
    [shadow] C5 (A): norm=0.487816 krum=0.332236 mkrum=KEEP tm_trim=0.0447 (lo 0.0000 / hi 0.0447) med_prov=0.1482 d_med=0.044370
    [shadow] C6 (A): norm=0.487816 krum=0.332236 mkrum=KEEP tm_trim=0.1130 (lo 0.0071 / hi 0.1059) med_prov=0.6940 d_med=0.044370
[shadow] round 4
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.603022 krum=0.703833 mkrum=KEEP tm_trim=0.7920 (lo 0.4101 / hi 0.3819) med_prov=0.0312 d_med=0.420827
    [shadow] C1 (B): norm=0.313136 krum=0.336292 mkrum=KEEP tm_trim=0.6961 (lo 0.3681 / hi 0.3281) med_prov=0.0434 d_med=0.315501
    [shadow] C2 (B): norm=0.337406 krum=0.365413 mkrum=KEEP tm_trim=0.7260 (lo 0.3816 / hi 0.3444) med_prov=0.0399 d_med=0.337370
    [shadow] C3 (B): norm=0.618022 krum=0.808883 mkrum=REJECT tm_trim=0.8100 (lo 0.4171 / hi 0.3929) med_prov=0.0270 d_med=0.467654
    [shadow] C4 (B): norm=0.645800 krum=0.809631 mkrum=REJECT tm_trim=0.8072 (lo 0.4158 / hi 0.3914) med_prov=0.0271 d_med=0.463342
    [shadow] C5 (A): norm=0.359636 krum=0.222397 mkrum=KEEP tm_trim=0.0495 (lo 0.0000 / hi 0.0495) med_prov=0.1361 d_med=0.041059
    [shadow] C6 (A): norm=0.359636 krum=0.222397 mkrum=KEEP tm_trim=0.1192 (lo 0.0073 / hi 0.1119) med_prov=0.6952 d_med=0.041059
[shadow] round 5
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.551211 krum=0.676074 mkrum=KEEP tm_trim=0.8051 (lo 0.4167 / hi 0.3884) med_prov=0.0314 d_med=0.419009
    [shadow] C1 (B): norm=0.282117 krum=0.310843 mkrum=KEEP tm_trim=0.6863 (lo 0.3639 / hi 0.3224) med_prov=0.0458 d_med=0.296709
    [shadow] C2 (B): norm=0.308799 krum=0.328953 mkrum=KEEP tm_trim=0.7175 (lo 0.3786 / hi 0.3389) med_prov=0.0415 d_med=0.311045
    [shadow] C3 (B): norm=0.552944 krum=0.742761 mkrum=REJECT tm_trim=0.8136 (lo 0.4189 / hi 0.3947) med_prov=0.0282 d_med=0.451984
    [shadow] C4 (B): norm=0.567312 krum=0.715778 mkrum=REJECT tm_trim=0.8014 (lo 0.4143 / hi 0.3871) med_prov=0.0292 d_med=0.439985
    [shadow] C5 (A): norm=0.295336 krum=0.193683 mkrum=KEEP tm_trim=0.0479 (lo 0.0000 / hi 0.0479) med_prov=0.1357 d_med=0.040861
    [shadow] C6 (A): norm=0.295336 krum=0.193683 mkrum=KEEP tm_trim=0.1282 (lo 0.0076 / hi 0.1206) med_prov=0.6882 d_med=0.040861
[shadow] round 6
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C0 (B), C3 (B)
    [shadow] C0 (B): norm=0.514162 krum=0.655433 mkrum=REJECT tm_trim=0.8094 (lo 0.4179 / hi 0.3915) med_prov=0.0293 d_med=0.415118
    [shadow] C1 (B): norm=0.263286 krum=0.296330 mkrum=KEEP tm_trim=0.6971 (lo 0.3686 / hi 0.3284) med_prov=0.0440 d_med=0.287707
    [shadow] C2 (B): norm=0.296725 krum=0.307016 mkrum=KEEP tm_trim=0.7182 (lo 0.3784 / hi 0.3398) med_prov=0.0410 d_med=0.296404
    [shadow] C3 (B): norm=0.496099 krum=0.640505 mkrum=REJECT tm_trim=0.8064 (lo 0.4160 / hi 0.3904) med_prov=0.0294 d_med=0.418549
    [shadow] C4 (B): norm=0.513919 krum=0.631644 mkrum=KEEP tm_trim=0.7955 (lo 0.4116 / hi 0.3839) med_prov=0.0299 d_med=0.412418
    [shadow] C5 (A): norm=0.254237 krum=0.178631 mkrum=KEEP tm_trim=0.0444 (lo 0.0000 / hi 0.0444) med_prov=0.1376 d_med=0.038867
    [shadow] C6 (A): norm=0.254237 krum=0.178631 mkrum=KEEP tm_trim=0.1291 (lo 0.0075 / hi 0.1216) med_prov=0.6888 d_med=0.038867
[shadow] round 7
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.463592 krum=0.581261 mkrum=KEEP tm_trim=0.8004 (lo 0.4141 / hi 0.3863) med_prov=0.0312 d_med=0.392347
    [shadow] C1 (B): norm=0.265800 krum=0.274788 mkrum=KEEP tm_trim=0.6814 (lo 0.3616 / hi 0.3199) med_prov=0.0458 d_med=0.274098
    [shadow] C2 (B): norm=0.278044 krum=0.293797 mkrum=KEEP tm_trim=0.7198 (lo 0.3790 / hi 0.3407) med_prov=0.0414 d_med=0.290408
    [shadow] C3 (B): norm=0.499538 krum=0.666942 mkrum=REJECT tm_trim=0.8248 (lo 0.4249 / hi 0.3999) med_prov=0.0273 d_med=0.428606
    [shadow] C4 (B): norm=0.480436 krum=0.587458 mkrum=REJECT tm_trim=0.7975 (lo 0.4129 / hi 0.3847) med_prov=0.0304 d_med=0.399617
    [shadow] C5 (A): norm=0.229000 krum=0.167118 mkrum=KEEP tm_trim=0.0437 (lo 0.0000 / hi 0.0437) med_prov=0.1381 d_med=0.038156
    [shadow] C6 (A): norm=0.229000 krum=0.167118 mkrum=KEEP tm_trim=0.1324 (lo 0.0076 / hi 0.1247) med_prov=0.6858 d_med=0.038156
[shadow] round 8
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.428943 krum=0.526360 mkrum=KEEP tm_trim=0.7841 (lo 0.4069 / hi 0.3772) med_prov=0.0341 d_med=0.374415
    [shadow] C1 (B): norm=0.260282 krum=0.274086 mkrum=KEEP tm_trim=0.6790 (lo 0.3609 / hi 0.3181) med_prov=0.0468 d_med=0.271149
    [shadow] C2 (B): norm=0.269350 krum=0.293744 mkrum=KEEP tm_trim=0.7241 (lo 0.3812 / hi 0.3429) med_prov=0.0414 d_med=0.288053
    [shadow] C3 (B): norm=0.490549 krum=0.649673 mkrum=REJECT tm_trim=0.8242 (lo 0.4249 / hi 0.3993) med_prov=0.0278 d_med=0.422899
    [shadow] C4 (B): norm=0.498908 krum=0.652371 mkrum=REJECT tm_trim=0.8102 (lo 0.4183 / hi 0.3919) med_prov=0.0284 d_med=0.422601
    [shadow] C5 (A): norm=0.216824 krum=0.164520 mkrum=KEEP tm_trim=0.0519 (lo 0.0000 / hi 0.0519) med_prov=0.1320 d_med=0.039100
    [shadow] C6 (A): norm=0.216824 krum=0.164520 mkrum=KEEP tm_trim=0.1266 (lo 0.0079 / hi 0.1187) med_prov=0.6895 d_med=0.039100
[shadow] round 9
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.451479 krum=0.572358 mkrum=KEEP tm_trim=0.7933 (lo 0.4113 / hi 0.3821) med_prov=0.0325 d_med=0.390644
    [shadow] C1 (B): norm=0.267130 krum=0.281374 mkrum=KEEP tm_trim=0.6797 (lo 0.3609 / hi 0.3188) med_prov=0.0465 d_med=0.273810
    [shadow] C2 (B): norm=0.277108 krum=0.302016 mkrum=KEEP tm_trim=0.7198 (lo 0.3792 / hi 0.3406) med_prov=0.0418 d_med=0.291487
    [shadow] C3 (B): norm=0.490293 krum=0.650648 mkrum=REJECT tm_trim=0.8194 (lo 0.4225 / hi 0.3970) med_prov=0.0286 d_med=0.426133
    [shadow] C4 (B): norm=0.500580 krum=0.648775 mkrum=REJECT tm_trim=0.8097 (lo 0.4183 / hi 0.3914) med_prov=0.0286 d_med=0.421369
    [shadow] C5 (A): norm=0.222939 krum=0.168031 mkrum=KEEP tm_trim=0.0495 (lo 0.0000 / hi 0.0495) med_prov=0.1331 d_med=0.039176
    [shadow] C6 (A): norm=0.222939 krum=0.168031 mkrum=KEEP tm_trim=0.1285 (lo 0.0078 / hi 0.1207) med_prov=0.6889 d_med=0.039176
[shadow] round 10
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.433835 krum=0.541796 mkrum=KEEP tm_trim=0.7951 (lo 0.4126 / hi 0.3825) med_prov=0.0319 d_med=0.380093
    [shadow] C1 (B): norm=0.261136 krum=0.271844 mkrum=KEEP tm_trim=0.6832 (lo 0.3631 / hi 0.3200) med_prov=0.0464 d_med=0.267685
    [shadow] C2 (B): norm=0.262002 krum=0.289956 mkrum=KEEP tm_trim=0.7192 (lo 0.3789 / hi 0.3403) med_prov=0.0419 d_med=0.283515
    [shadow] C3 (B): norm=0.487770 krum=0.636775 mkrum=REJECT tm_trim=0.8218 (lo 0.4229 / hi 0.3989) med_prov=0.0276 d_med=0.421578
    [shadow] C4 (B): norm=0.475989 krum=0.602493 mkrum=REJECT tm_trim=0.8031 (lo 0.4148 / hi 0.3882) med_prov=0.0299 d_med=0.405509
    [shadow] C5 (A): norm=0.211839 krum=0.159750 mkrum=KEEP tm_trim=0.0473 (lo 0.0000 / hi 0.0473) med_prov=0.1343 d_med=0.038333
    [shadow] C6 (A): norm=0.211839 krum=0.159750 mkrum=KEEP tm_trim=0.1304 (lo 0.0076 / hi 0.1228) med_prov=0.6880 d_med=0.038333
[shadow] round 11
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.445382 krum=0.568345 mkrum=KEEP tm_trim=0.7945 (lo 0.4116 / hi 0.3829) med_prov=0.0309 d_med=0.388086
    [shadow] C1 (B): norm=0.269372 krum=0.294657 mkrum=KEEP tm_trim=0.6930 (lo 0.3671 / hi 0.3259) med_prov=0.0454 d_med=0.273351
    [shadow] C2 (B): norm=0.269707 krum=0.319746 mkrum=KEEP tm_trim=0.7278 (lo 0.3825 / hi 0.3453) med_prov=0.0395 d_med=0.294991
    [shadow] C3 (B): norm=0.471219 krum=0.618543 mkrum=REJECT tm_trim=0.8193 (lo 0.4214 / hi 0.3979) med_prov=0.0274 d_med=0.414951
    [shadow] C4 (B): norm=0.455817 krum=0.568990 mkrum=REJECT tm_trim=0.7911 (lo 0.4098 / hi 0.3813) med_prov=0.0310 d_med=0.389539
    [shadow] C5 (A): norm=0.205244 krum=0.168677 mkrum=KEEP tm_trim=0.0420 (lo 0.0000 / hi 0.0420) med_prov=0.1390 d_med=0.037355
    [shadow] C6 (A): norm=0.205244 krum=0.168677 mkrum=KEEP tm_trim=0.1322 (lo 0.0076 / hi 0.1246) med_prov=0.6867 d_med=0.037355
[shadow] round 12
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.402023 krum=0.489839 mkrum=KEEP tm_trim=0.7864 (lo 0.4088 / hi 0.3776) med_prov=0.0330 d_med=0.360741
    [shadow] C1 (B): norm=0.255221 krum=0.269086 mkrum=KEEP tm_trim=0.6795 (lo 0.3606 / hi 0.3189) med_prov=0.0463 d_med=0.260545
    [shadow] C2 (B): norm=0.261483 krum=0.292302 mkrum=KEEP tm_trim=0.7295 (lo 0.3832 / hi 0.3464) med_prov=0.0406 d_med=0.281461
    [shadow] C3 (B): norm=0.465900 krum=0.601013 mkrum=REJECT tm_trim=0.8273 (lo 0.4255 / hi 0.4018) med_prov=0.0268 d_med=0.410859
    [shadow] C4 (B): norm=0.452643 krum=0.551053 mkrum=REJECT tm_trim=0.7997 (lo 0.4145 / hi 0.3852) med_prov=0.0308 d_med=0.387249
    [shadow] C5 (A): norm=0.194720 krum=0.153861 mkrum=KEEP tm_trim=0.0443 (lo 0.0000 / hi 0.0443) med_prov=0.1357 d_med=0.036248
    [shadow] C6 (A): norm=0.194720 krum=0.153861 mkrum=KEEP tm_trim=0.1333 (lo 0.0075 / hi 0.1258) med_prov=0.6867 d_med=0.036248
[shadow] round 13
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.415517 krum=0.499881 mkrum=KEEP tm_trim=0.7901 (lo 0.4094 / hi 0.3806) med_prov=0.0314 d_med=0.365782
    [shadow] C1 (B): norm=0.252444 krum=0.261718 mkrum=KEEP tm_trim=0.6840 (lo 0.3630 / hi 0.3210) med_prov=0.0473 d_med=0.259277
    [shadow] C2 (B): norm=0.261641 krum=0.283835 mkrum=KEEP tm_trim=0.7291 (lo 0.3835 / hi 0.3456) med_prov=0.0401 d_med=0.279415
    [shadow] C3 (B): norm=0.445034 krum=0.563508 mkrum=REJECT tm_trim=0.8164 (lo 0.4205 / hi 0.3959) med_prov=0.0281 d_med=0.395752
    [shadow] C4 (B): norm=0.450793 krum=0.554436 mkrum=REJECT tm_trim=0.8037 (lo 0.4160 / hi 0.3877) med_prov=0.0299 d_med=0.386857
    [shadow] C5 (A): norm=0.193899 krum=0.151913 mkrum=KEEP tm_trim=0.0460 (lo 0.0000 / hi 0.0460) med_prov=0.1342 d_med=0.035987
    [shadow] C6 (A): norm=0.193899 krum=0.151913 mkrum=KEEP tm_trim=0.1307 (lo 0.0076 / hi 0.1231) med_prov=0.6891 d_med=0.035987
[shadow] round 14
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.421650 krum=0.519948 mkrum=KEEP tm_trim=0.8002 (lo 0.4137 / hi 0.3865) med_prov=0.0297 d_med=0.373680
    [shadow] C1 (B): norm=0.258474 krum=0.265080 mkrum=KEEP tm_trim=0.6955 (lo 0.3682 / hi 0.3273) med_prov=0.0446 d_med=0.259825
    [shadow] C2 (B): norm=0.263441 krum=0.282703 mkrum=KEEP tm_trim=0.7243 (lo 0.3809 / hi 0.3434) med_prov=0.0407 d_med=0.276074
    [shadow] C3 (B): norm=0.430674 krum=0.539103 mkrum=REJECT tm_trim=0.8121 (lo 0.4184 / hi 0.3937) med_prov=0.0287 d_med=0.386006
    [shadow] C4 (B): norm=0.433328 krum=0.526848 mkrum=REJECT tm_trim=0.7932 (lo 0.4113 / hi 0.3820) med_prov=0.0311 d_med=0.377365
    [shadow] C5 (A): norm=0.189118 krum=0.150099 mkrum=KEEP tm_trim=0.0433 (lo 0.0000 / hi 0.0433) med_prov=0.1363 d_med=0.035316
    [shadow] C6 (A): norm=0.189118 krum=0.150099 mkrum=KEEP tm_trim=0.1313 (lo 0.0075 / hi 0.1238) med_prov=0.6890 d_med=0.035316
[shadow] round 15
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C0 (B), C3 (B)
    [shadow] C0 (B): norm=0.414647 krum=0.507486 mkrum=REJECT tm_trim=0.7993 (lo 0.4138 / hi 0.3854) med_prov=0.0302 d_med=0.367621
    [shadow] C1 (B): norm=0.255707 krum=0.258672 mkrum=KEEP tm_trim=0.6945 (lo 0.3676 / hi 0.3269) med_prov=0.0447 d_med=0.258361
    [shadow] C2 (B): norm=0.255188 krum=0.274037 mkrum=KEEP tm_trim=0.7258 (lo 0.3816 / hi 0.3442) med_prov=0.0402 d_med=0.272398
    [shadow] C3 (B): norm=0.444097 krum=0.562336 mkrum=REJECT tm_trim=0.8202 (lo 0.4220 / hi 0.3982) med_prov=0.0271 d_med=0.393288
    [shadow] C4 (B): norm=0.406159 krum=0.470246 mkrum=KEEP tm_trim=0.7857 (lo 0.4074 / hi 0.3783) med_prov=0.0324 d_med=0.355400
    [shadow] C5 (A): norm=0.185328 krum=0.147165 mkrum=KEEP tm_trim=0.0392 (lo 0.0000 / hi 0.0392) med_prov=0.1417 d_med=0.034896
    [shadow] C6 (A): norm=0.185328 krum=0.147165 mkrum=KEEP tm_trim=0.1354 (lo 0.0076 / hi 0.1279) med_prov=0.6837 d_med=0.034896
[shadow] round 16
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.406120 krum=0.490013 mkrum=KEEP tm_trim=0.7930 (lo 0.4107 / hi 0.3822) med_prov=0.0312 d_med=0.359100
    [shadow] C1 (B): norm=0.258584 krum=0.265137 mkrum=KEEP tm_trim=0.6979 (lo 0.3696 / hi 0.3284) med_prov=0.0438 d_med=0.262937
    [shadow] C2 (B): norm=0.257160 krum=0.275102 mkrum=KEEP tm_trim=0.7240 (lo 0.3809 / hi 0.3431) med_prov=0.0402 d_med=0.271842
    [shadow] C3 (B): norm=0.435622 krum=0.551064 mkrum=REJECT tm_trim=0.8151 (lo 0.4192 / hi 0.3958) med_prov=0.0277 d_med=0.389242
    [shadow] C4 (B): norm=0.431928 krum=0.522142 mkrum=REJECT tm_trim=0.7970 (lo 0.4122 / hi 0.3848) med_prov=0.0301 d_med=0.377835
    [shadow] C5 (A): norm=0.186187 krum=0.149275 mkrum=KEEP tm_trim=0.0447 (lo 0.0000 / hi 0.0447) med_prov=0.1357 d_med=0.034928
    [shadow] C6 (A): norm=0.186187 krum=0.149275 mkrum=KEEP tm_trim=0.1283 (lo 0.0074 / hi 0.1210) med_prov=0.6913 d_med=0.034928
[shadow] round 17
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.398392 krum=0.474981 mkrum=KEEP tm_trim=0.7925 (lo 0.4100 / hi 0.3825) med_prov=0.0312 d_med=0.353957
    [shadow] C1 (B): norm=0.260254 krum=0.259788 mkrum=KEEP tm_trim=0.7007 (lo 0.3704 / hi 0.3303) med_prov=0.0436 d_med=0.257736
    [shadow] C2 (B): norm=0.256499 krum=0.269414 mkrum=KEEP tm_trim=0.7245 (lo 0.3804 / hi 0.3441) med_prov=0.0391 d_med=0.266488
    [shadow] C3 (B): norm=0.415696 krum=0.514510 mkrum=REJECT tm_trim=0.8130 (lo 0.4189 / hi 0.3942) med_prov=0.0281 d_med=0.376255
    [shadow] C4 (B): norm=0.412376 krum=0.484210 mkrum=REJECT tm_trim=0.7971 (lo 0.4128 / hi 0.3843) med_prov=0.0302 d_med=0.361238
    [shadow] C5 (A): norm=0.180095 krum=0.143241 mkrum=KEEP tm_trim=0.0427 (lo 0.0000 / hi 0.0427) med_prov=0.1370 d_med=0.033875
    [shadow] C6 (A): norm=0.180095 krum=0.143241 mkrum=KEEP tm_trim=0.1294 (lo 0.0075 / hi 0.1219) med_prov=0.6908 d_med=0.033875
[shadow] round 18
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.415528 krum=0.496672 mkrum=KEEP tm_trim=0.7940 (lo 0.4108 / hi 0.3832) med_prov=0.0308 d_med=0.363057
    [shadow] C1 (B): norm=0.262547 krum=0.263673 mkrum=KEEP tm_trim=0.7045 (lo 0.3723 / hi 0.3322) med_prov=0.0424 d_med=0.260903
    [shadow] C2 (B): norm=0.253551 krum=0.277108 mkrum=KEEP tm_trim=0.7269 (lo 0.3822 / hi 0.3448) med_prov=0.0391 d_med=0.273319
    [shadow] C3 (B): norm=0.417644 krum=0.525367 mkrum=REJECT tm_trim=0.8095 (lo 0.4167 / hi 0.3928) med_prov=0.0287 d_med=0.376890
    [shadow] C4 (B): norm=0.413286 krum=0.499111 mkrum=REJECT tm_trim=0.7936 (lo 0.4108 / hi 0.3828) med_prov=0.0305 d_med=0.366816
    [shadow] C5 (A): norm=0.181034 krum=0.148762 mkrum=KEEP tm_trim=0.0424 (lo 0.0000 / hi 0.0424) med_prov=0.1377 d_med=0.034172
    [shadow] C6 (A): norm=0.181034 krum=0.148762 mkrum=KEEP tm_trim=0.1291 (lo 0.0073 / hi 0.1218) med_prov=0.6908 d_med=0.034172
[shadow] round 19
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.386919 krum=0.449825 mkrum=KEEP tm_trim=0.7861 (lo 0.4071 / hi 0.3790) med_prov=0.0323 d_med=0.345091
    [shadow] C1 (B): norm=0.255716 krum=0.259890 mkrum=KEEP tm_trim=0.6999 (lo 0.3698 / hi 0.3301) med_prov=0.0431 d_med=0.255483
    [shadow] C2 (B): norm=0.262829 krum=0.276963 mkrum=KEEP tm_trim=0.7338 (lo 0.3855 / hi 0.3483) med_prov=0.0386 d_med=0.271433
    [shadow] C3 (B): norm=0.400868 krum=0.495158 mkrum=REJECT tm_trim=0.8094 (lo 0.4173 / hi 0.3921) med_prov=0.0285 d_med=0.366812
    [shadow] C4 (B): norm=0.411824 krum=0.500078 mkrum=REJECT tm_trim=0.7986 (lo 0.4129 / hi 0.3856) med_prov=0.0299 d_med=0.366166
    [shadow] C5 (A): norm=0.172541 krum=0.144501 mkrum=KEEP tm_trim=0.0445 (lo 0.0000 / hi 0.0445) med_prov=0.1352 d_med=0.033577
    [shadow] C6 (A): norm=0.172541 krum=0.144501 mkrum=KEEP tm_trim=0.1278 (lo 0.0074 / hi 0.1204) med_prov=0.6926 d_med=0.033577
[shadow] round 20
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C0 (B), C4 (B)
    [shadow] C0 (B): norm=0.400221 krum=0.471425 mkrum=REJECT tm_trim=0.7994 (lo 0.4128 / hi 0.3866) med_prov=0.0305 d_med=0.353022
    [shadow] C1 (B): norm=0.248239 krum=0.242927 mkrum=KEEP tm_trim=0.6954 (lo 0.3682 / hi 0.3271) med_prov=0.0435 d_med=0.249196
    [shadow] C2 (B): norm=0.253634 krum=0.256536 mkrum=KEEP tm_trim=0.7255 (lo 0.3814 / hi 0.3442) med_prov=0.0401 d_med=0.262106
    [shadow] C3 (B): norm=0.380045 krum=0.464214 mkrum=KEEP tm_trim=0.8069 (lo 0.4169 / hi 0.3900) med_prov=0.0295 d_med=0.356059
    [shadow] C4 (B): norm=0.406028 krum=0.487230 mkrum=REJECT tm_trim=0.7999 (lo 0.4135 / hi 0.3865) med_prov=0.0292 d_med=0.363185
    [shadow] C5 (A): norm=0.167779 krum=0.136379 mkrum=KEEP tm_trim=0.0458 (lo 0.0000 / hi 0.0458) med_prov=0.1357 d_med=0.033035
    [shadow] C6 (A): norm=0.167779 krum=0.136379 mkrum=KEEP tm_trim=0.1270 (lo 0.0072 / hi 0.1198) med_prov=0.6915 d_med=0.033035
[shadow] round 21
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C0 (B), C4 (B)
    [shadow] C0 (B): norm=0.387237 krum=0.458566 mkrum=REJECT tm_trim=0.7958 (lo 0.4124 / hi 0.3834) med_prov=0.0304 d_med=0.348095
    [shadow] C1 (B): norm=0.251315 krum=0.237236 mkrum=KEEP tm_trim=0.7020 (lo 0.3709 / hi 0.3311) med_prov=0.0426 d_med=0.248451
    [shadow] C2 (B): norm=0.254182 krum=0.249789 mkrum=KEEP tm_trim=0.7303 (lo 0.3832 / hi 0.3472) med_prov=0.0393 d_med=0.260580
    [shadow] C3 (B): norm=0.381355 krum=0.453151 mkrum=KEEP tm_trim=0.8025 (lo 0.4146 / hi 0.3880) med_prov=0.0297 d_med=0.349725
    [shadow] C4 (B): norm=0.397396 krum=0.468377 mkrum=REJECT tm_trim=0.7984 (lo 0.4118 / hi 0.3865) med_prov=0.0290 d_med=0.354615
    [shadow] C5 (A): norm=0.167267 krum=0.135072 mkrum=KEEP tm_trim=0.0450 (lo 0.0000 / hi 0.0450) med_prov=0.1369 d_med=0.032516
    [shadow] C6 (A): norm=0.167267 krum=0.135072 mkrum=KEEP tm_trim=0.1260 (lo 0.0072 / hi 0.1187) med_prov=0.6922 d_med=0.032516
[shadow] round 22
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.371051 krum=0.422685 mkrum=KEEP tm_trim=0.7889 (lo 0.4089 / hi 0.3799) med_prov=0.0305 d_med=0.334395
    [shadow] C1 (B): norm=0.245628 krum=0.239458 mkrum=KEEP tm_trim=0.7059 (lo 0.3723 / hi 0.3335) med_prov=0.0420 d_med=0.247958
    [shadow] C2 (B): norm=0.252349 krum=0.248279 mkrum=KEEP tm_trim=0.7294 (lo 0.3823 / hi 0.3471) med_prov=0.0391 d_med=0.256438
    [shadow] C3 (B): norm=0.385050 krum=0.469763 mkrum=REJECT tm_trim=0.8129 (lo 0.4191 / hi 0.3938) med_prov=0.0277 d_med=0.355974
    [shadow] C4 (B): norm=0.392274 krum=0.450589 mkrum=REJECT tm_trim=0.7933 (lo 0.4101 / hi 0.3832) med_prov=0.0303 d_med=0.346970
    [shadow] C5 (A): norm=0.163624 krum=0.132338 mkrum=KEEP tm_trim=0.0424 (lo 0.0000 / hi 0.0424) med_prov=0.1374 d_med=0.032015
    [shadow] C6 (A): norm=0.163624 krum=0.132338 mkrum=KEEP tm_trim=0.1272 (lo 0.0071 / hi 0.1201) med_prov=0.6930 d_med=0.032015
[shadow] round 23
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C0 (B), C3 (B)
    [shadow] C0 (B): norm=0.374431 krum=0.434951 mkrum=REJECT tm_trim=0.7929 (lo 0.4110 / hi 0.3819) med_prov=0.0304 d_med=0.337170
    [shadow] C1 (B): norm=0.242663 krum=0.234268 mkrum=KEEP tm_trim=0.6979 (lo 0.3692 / hi 0.3287) med_prov=0.0443 d_med=0.243539
    [shadow] C2 (B): norm=0.258014 krum=0.252453 mkrum=KEEP tm_trim=0.7400 (lo 0.3876 / hi 0.3525) med_prov=0.0373 d_med=0.261148
    [shadow] C3 (B): norm=0.373368 krum=0.440780 mkrum=REJECT tm_trim=0.8082 (lo 0.4166 / hi 0.3916) med_prov=0.0282 d_med=0.346330
    [shadow] C4 (B): norm=0.376839 krum=0.431426 mkrum=KEEP tm_trim=0.7903 (lo 0.4085 / hi 0.3818) med_prov=0.0305 d_med=0.336844
    [shadow] C5 (A): norm=0.159521 krum=0.132405 mkrum=KEEP tm_trim=0.0418 (lo 0.0000 / hi 0.0418) med_prov=0.1390 d_med=0.031330
    [shadow] C6 (A): norm=0.159521 krum=0.132405 mkrum=KEEP tm_trim=0.1287 (lo 0.0071 / hi 0.1217) med_prov=0.6904 d_med=0.031330
[shadow] round 24
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.351754 krum=0.400435 mkrum=KEEP tm_trim=0.7882 (lo 0.4076 / hi 0.3806) med_prov=0.0302 d_med=0.322643
    [shadow] C1 (B): norm=0.252748 krum=0.233284 mkrum=KEEP tm_trim=0.7131 (lo 0.3755 / hi 0.3376) med_prov=0.0402 d_med=0.245403
    [shadow] C2 (B): norm=0.251172 krum=0.238893 mkrum=KEEP tm_trim=0.7313 (lo 0.3831 / hi 0.3482) med_prov=0.0373 d_med=0.250804
    [shadow] C3 (B): norm=0.351709 krum=0.411778 mkrum=REJECT tm_trim=0.8017 (lo 0.4144 / hi 0.3873) med_prov=0.0290 d_med=0.330210
    [shadow] C4 (B): norm=0.382886 krum=0.443667 mkrum=REJECT tm_trim=0.8013 (lo 0.4127 / hi 0.3886) med_prov=0.0276 d_med=0.342428
    [shadow] C5 (A): norm=0.154976 krum=0.127571 mkrum=KEEP tm_trim=0.0451 (lo 0.0000 / hi 0.0451) med_prov=0.1372 d_med=0.029866
    [shadow] C6 (A): norm=0.154976 krum=0.127571 mkrum=KEEP tm_trim=0.1192 (lo 0.0067 / hi 0.1125) med_prov=0.6985 d_med=0.029866
[shadow] round 25
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.360498 krum=0.399229 mkrum=KEEP tm_trim=0.7872 (lo 0.4072 / hi 0.3800) med_prov=0.0303 d_med=0.320679
    [shadow] C1 (B): norm=0.255429 krum=0.245981 mkrum=KEEP tm_trim=0.7132 (lo 0.3754 / hi 0.3378) med_prov=0.0404 d_med=0.246214
    [shadow] C2 (B): norm=0.254976 krum=0.256989 mkrum=KEEP tm_trim=0.7423 (lo 0.3889 / hi 0.3534) med_prov=0.0367 d_med=0.257044
    [shadow] C3 (B): norm=0.351271 krum=0.400290 mkrum=REJECT tm_trim=0.7969 (lo 0.4115 / hi 0.3854) med_prov=0.0295 d_med=0.327470
    [shadow] C4 (B): norm=0.364720 krum=0.408299 mkrum=REJECT tm_trim=0.7942 (lo 0.4102 / hi 0.3840) med_prov=0.0292 d_med=0.329867
    [shadow] C5 (A): norm=0.156593 krum=0.130730 mkrum=KEEP tm_trim=0.0418 (lo 0.0000 / hi 0.0418) med_prov=0.1391 d_med=0.029728
    [shadow] C6 (A): norm=0.156593 krum=0.130730 mkrum=KEEP tm_trim=0.1243 (lo 0.0067 / hi 0.1176) med_prov=0.6948 d_med=0.029728
[shadow] round 26
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.352675 krum=0.394964 mkrum=KEEP tm_trim=0.7838 (lo 0.4058 / hi 0.3780) med_prov=0.0300 d_med=0.320274
    [shadow] C1 (B): norm=0.254643 krum=0.241423 mkrum=KEEP tm_trim=0.7145 (lo 0.3761 / hi 0.3384) med_prov=0.0397 d_med=0.245696
    [shadow] C2 (B): norm=0.254859 krum=0.253267 mkrum=KEEP tm_trim=0.7432 (lo 0.3886 / hi 0.3547) med_prov=0.0357 d_med=0.257334
    [shadow] C3 (B): norm=0.371203 krum=0.440536 mkrum=REJECT tm_trim=0.8164 (lo 0.4196 / hi 0.3967) med_prov=0.0263 d_med=0.342842
    [shadow] C4 (B): norm=0.358582 krum=0.395459 mkrum=REJECT tm_trim=0.7790 (lo 0.4034 / hi 0.3756) med_prov=0.0313 d_med=0.319859
    [shadow] C5 (A): norm=0.157214 krum=0.130580 mkrum=KEEP tm_trim=0.0362 (lo 0.0000 / hi 0.0362) med_prov=0.1417 d_med=0.029063
    [shadow] C6 (A): norm=0.157214 krum=0.130580 mkrum=KEEP tm_trim=0.1269 (lo 0.0064 / hi 0.1205) med_prov=0.6952 d_med=0.029063
[shadow] round 27
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.356829 krum=0.387698 mkrum=KEEP tm_trim=0.7906 (lo 0.4083 / hi 0.3823) med_prov=0.0297 d_med=0.318295
    [shadow] C1 (B): norm=0.239063 krum=0.225092 mkrum=KEEP tm_trim=0.7035 (lo 0.3705 / hi 0.3330) med_prov=0.0404 d_med=0.238021
    [shadow] C2 (B): norm=0.252763 krum=0.237052 mkrum=KEEP tm_trim=0.7382 (lo 0.3866 / hi 0.3516) med_prov=0.0365 d_med=0.250004
    [shadow] C3 (B): norm=0.353702 krum=0.406541 mkrum=REJECT tm_trim=0.8181 (lo 0.4213 / hi 0.3968) med_prov=0.0261 d_med=0.329869
    [shadow] C4 (B): norm=0.355882 krum=0.389583 mkrum=REJECT tm_trim=0.7874 (lo 0.4067 / hi 0.3808) med_prov=0.0295 d_med=0.320559
    [shadow] C5 (A): norm=0.153649 krum=0.123060 mkrum=KEEP tm_trim=0.0391 (lo 0.0000 / hi 0.0391) med_prov=0.1421 d_med=0.028540
    [shadow] C6 (A): norm=0.153649 krum=0.123060 mkrum=KEEP tm_trim=0.1231 (lo 0.0066 / hi 0.1165) med_prov=0.6957 d_med=0.028540
[shadow] round 28
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.354515 krum=0.387837 mkrum=KEEP tm_trim=0.7917 (lo 0.4092 / hi 0.3825) med_prov=0.0303 d_med=0.318172
    [shadow] C1 (B): norm=0.249544 krum=0.233835 mkrum=KEEP tm_trim=0.7132 (lo 0.3750 / hi 0.3382) med_prov=0.0405 d_med=0.242524
    [shadow] C2 (B): norm=0.253737 krum=0.240812 mkrum=KEEP tm_trim=0.7347 (lo 0.3852 / hi 0.3494) med_prov=0.0372 d_med=0.249554
    [shadow] C3 (B): norm=0.357009 krum=0.414983 mkrum=REJECT tm_trim=0.8086 (lo 0.4164 / hi 0.3921) med_prov=0.0276 d_med=0.334904
    [shadow] C4 (B): norm=0.365174 krum=0.408798 mkrum=REJECT tm_trim=0.7864 (lo 0.4073 / hi 0.3791) med_prov=0.0299 d_med=0.327320
    [shadow] C5 (A): norm=0.156557 krum=0.125248 mkrum=KEEP tm_trim=0.0403 (lo 0.0000 / hi 0.0403) med_prov=0.1403 d_med=0.029522
    [shadow] C6 (A): norm=0.156557 krum=0.125248 mkrum=KEEP tm_trim=0.1251 (lo 0.0068 / hi 0.1183) med_prov=0.6942 d_med=0.029522
[shadow] round 29
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.335702 krum=0.361694 mkrum=KEEP tm_trim=0.7854 (lo 0.4058 / hi 0.3796) med_prov=0.0298 d_med=0.305684
    [shadow] C1 (B): norm=0.243218 krum=0.234892 mkrum=KEEP tm_trim=0.7115 (lo 0.3749 / hi 0.3367) med_prov=0.0402 d_med=0.238416
    [shadow] C2 (B): norm=0.255319 krum=0.249686 mkrum=KEEP tm_trim=0.7481 (lo 0.3906 / hi 0.3575) med_prov=0.0353 d_med=0.253373
    [shadow] C3 (B): norm=0.359721 krum=0.410680 mkrum=REJECT tm_trim=0.8108 (lo 0.4170 / hi 0.3938) med_prov=0.0265 d_med=0.332875
    [shadow] C4 (B): norm=0.349098 krum=0.375935 mkrum=REJECT tm_trim=0.7825 (lo 0.4054 / hi 0.3771) med_prov=0.0299 d_med=0.313382
    [shadow] C5 (A): norm=0.150889 krum=0.124651 mkrum=KEEP tm_trim=0.0371 (lo 0.0000 / hi 0.0371) med_prov=0.1433 d_med=0.028193
    [shadow] C6 (A): norm=0.150889 krum=0.124651 mkrum=KEEP tm_trim=0.1245 (lo 0.0064 / hi 0.1181) med_prov=0.6950 d_med=0.028193
[shadow] round 30
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C0 (B), C4 (B)
    [shadow] C0 (B): norm=0.341978 krum=0.380321 mkrum=REJECT tm_trim=0.7895 (lo 0.4077 / hi 0.3818) med_prov=0.0292 d_med=0.314698
    [shadow] C1 (B): norm=0.246791 krum=0.226806 mkrum=KEEP tm_trim=0.7116 (lo 0.3747 / hi 0.3369) med_prov=0.0393 d_med=0.238558
    [shadow] C2 (B): norm=0.249078 krum=0.234005 mkrum=KEEP tm_trim=0.7393 (lo 0.3869 / hi 0.3523) med_prov=0.0368 d_med=0.245816
    [shadow] C3 (B): norm=0.321612 krum=0.346986 mkrum=KEEP tm_trim=0.7955 (lo 0.4107 / hi 0.3848) med_prov=0.0297 d_med=0.302894
    [shadow] C4 (B): norm=0.378112 krum=0.425639 mkrum=REJECT tm_trim=0.8031 (lo 0.4135 / hi 0.3896) med_prov=0.0260 d_med=0.337474
    [shadow] C5 (A): norm=0.150528 krum=0.121115 mkrum=KEEP tm_trim=0.0463 (lo 0.0000 / hi 0.0463) med_prov=0.1374 d_med=0.028146
    [shadow] C6 (A): norm=0.150528 krum=0.121115 mkrum=KEEP tm_trim=0.1147 (lo 0.0066 / hi 0.1082) med_prov=0.7016 d_med=0.028146
[shadow] round 31
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.341704 krum=0.378337 mkrum=KEEP tm_trim=0.7865 (lo 0.4063 / hi 0.3802) med_prov=0.0294 d_med=0.312676
    [shadow] C1 (B): norm=0.249864 krum=0.238177 mkrum=KEEP tm_trim=0.7055 (lo 0.3712 / hi 0.3343) med_prov=0.0401 d_med=0.242177
    [shadow] C2 (B): norm=0.259815 krum=0.254529 mkrum=KEEP tm_trim=0.7493 (lo 0.3909 / hi 0.3584) med_prov=0.0344 d_med=0.258290
    [shadow] C3 (B): norm=0.361935 krum=0.416289 mkrum=REJECT tm_trim=0.8126 (lo 0.4184 / hi 0.3942) med_prov=0.0268 d_med=0.333502
    [shadow] C4 (B): norm=0.352023 krum=0.396221 mkrum=REJECT tm_trim=0.7861 (lo 0.4068 / hi 0.3793) med_prov=0.0293 d_med=0.320016
    [shadow] C5 (A): norm=0.151938 krum=0.129008 mkrum=KEEP tm_trim=0.0376 (lo 0.0000 / hi 0.0376) med_prov=0.1415 d_med=0.028412
    [shadow] C6 (A): norm=0.151938 krum=0.129008 mkrum=KEEP tm_trim=0.1224 (lo 0.0064 / hi 0.1160) med_prov=0.6986 d_med=0.028412
[shadow] round 32
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.342180 krum=0.363114 mkrum=KEEP tm_trim=0.7885 (lo 0.4078 / hi 0.3807) med_prov=0.0294 d_med=0.304317
    [shadow] C1 (B): norm=0.240175 krum=0.224523 mkrum=KEEP tm_trim=0.7138 (lo 0.3753 / hi 0.3385) med_prov=0.0399 d_med=0.236628
    [shadow] C2 (B): norm=0.248929 krum=0.233974 mkrum=KEEP tm_trim=0.7380 (lo 0.3863 / hi 0.3517) med_prov=0.0363 d_med=0.246382
    [shadow] C3 (B): norm=0.341691 krum=0.375446 mkrum=REJECT tm_trim=0.8072 (lo 0.4153 / hi 0.3919) med_prov=0.0273 d_med=0.315107
    [shadow] C4 (B): norm=0.356110 krum=0.393824 mkrum=REJECT tm_trim=0.7916 (lo 0.4086 / hi 0.3830) med_prov=0.0278 d_med=0.321891
    [shadow] C5 (A): norm=0.152282 krum=0.120146 mkrum=KEEP tm_trim=0.0430 (lo 0.0000 / hi 0.0430) med_prov=0.1394 d_med=0.027740
    [shadow] C6 (A): norm=0.152282 krum=0.120146 mkrum=KEEP tm_trim=0.1178 (lo 0.0066 / hi 0.1112) med_prov=0.6998 d_med=0.027740
[shadow] round 33
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.347377 krum=0.390120 mkrum=KEEP tm_trim=0.7892 (lo 0.4083 / hi 0.3809) med_prov=0.0293 d_med=0.315322
    [shadow] C1 (B): norm=0.245355 krum=0.231717 mkrum=KEEP tm_trim=0.7158 (lo 0.3753 / hi 0.3406) med_prov=0.0386 d_med=0.243378
    [shadow] C2 (B): norm=0.251176 krum=0.242698 mkrum=KEEP tm_trim=0.7451 (lo 0.3887 / hi 0.3564) med_prov=0.0354 d_med=0.254068
    [shadow] C3 (B): norm=0.361998 krum=0.413956 mkrum=REJECT tm_trim=0.8083 (lo 0.4168 / hi 0.3916) med_prov=0.0270 d_med=0.330860
    [shadow] C4 (B): norm=0.357950 krum=0.397454 mkrum=REJECT tm_trim=0.7821 (lo 0.4044 / hi 0.3777) med_prov=0.0290 d_med=0.321263
    [shadow] C5 (A): norm=0.153250 krum=0.127672 mkrum=KEEP tm_trim=0.0379 (lo 0.0000 / hi 0.0379) med_prov=0.1437 d_med=0.028331
    [shadow] C6 (A): norm=0.153250 krum=0.127672 mkrum=KEEP tm_trim=0.1215 (lo 0.0065 / hi 0.1150) med_prov=0.6969 d_med=0.028331
[shadow] round 34
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.347892 krum=0.381757 mkrum=KEEP tm_trim=0.7909 (lo 0.4091 / hi 0.3818) med_prov=0.0297 d_med=0.315450
    [shadow] C1 (B): norm=0.243753 krum=0.227178 mkrum=KEEP tm_trim=0.7032 (lo 0.3709 / hi 0.3323) med_prov=0.0406 d_med=0.238087
    [shadow] C2 (B): norm=0.252275 krum=0.236810 mkrum=KEEP tm_trim=0.7354 (lo 0.3851 / hi 0.3503) med_prov=0.0375 d_med=0.247886
    [shadow] C3 (B): norm=0.349767 krum=0.390787 mkrum=REJECT tm_trim=0.8057 (lo 0.4147 / hi 0.3910) med_prov=0.0281 d_med=0.323666
    [shadow] C4 (B): norm=0.375037 krum=0.428064 mkrum=REJECT tm_trim=0.8021 (lo 0.4137 / hi 0.3884) med_prov=0.0267 d_med=0.339122
    [shadow] C5 (A): norm=0.155169 krum=0.122018 mkrum=KEEP tm_trim=0.0456 (lo 0.0000 / hi 0.0456) med_prov=0.1341 d_med=0.028511
    [shadow] C6 (A): norm=0.155169 krum=0.122018 mkrum=KEEP tm_trim=0.1170 (lo 0.0065 / hi 0.1106) med_prov=0.7032 d_med=0.028511
[shadow] round 35
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.328335 krum=0.359105 mkrum=KEEP tm_trim=0.7796 (lo 0.4047 / hi 0.3748) med_prov=0.0312 d_med=0.303235
    [shadow] C1 (B): norm=0.247130 krum=0.231983 mkrum=KEEP tm_trim=0.7091 (lo 0.3730 / hi 0.3361) med_prov=0.0402 d_med=0.241224
    [shadow] C2 (B): norm=0.253913 krum=0.241562 mkrum=KEEP tm_trim=0.7364 (lo 0.3861 / hi 0.3503) med_prov=0.0370 d_med=0.251014
    [shadow] C3 (B): norm=0.365549 krum=0.422752 mkrum=REJECT tm_trim=0.8130 (lo 0.4179 / hi 0.3951) med_prov=0.0260 d_med=0.339190
    [shadow] C4 (B): norm=0.384197 krum=0.434129 mkrum=REJECT tm_trim=0.7998 (lo 0.4115 / hi 0.3883) med_prov=0.0277 d_med=0.340408
    [shadow] C5 (A): norm=0.156219 krum=0.125207 mkrum=KEEP tm_trim=0.0438 (lo 0.0000 / hi 0.0438) med_prov=0.1378 d_med=0.029042
    [shadow] C6 (A): norm=0.156219 krum=0.125207 mkrum=KEEP tm_trim=0.1183 (lo 0.0068 / hi 0.1116) med_prov=0.7001 d_med=0.029042
[shadow] round 36
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C0 (B), C4 (B)
    [shadow] C0 (B): norm=0.353882 krum=0.402865 mkrum=REJECT tm_trim=0.7957 (lo 0.4112 / hi 0.3845) med_prov=0.0284 d_med=0.324652
    [shadow] C1 (B): norm=0.246705 krum=0.229207 mkrum=KEEP tm_trim=0.7052 (lo 0.3708 / hi 0.3344) med_prov=0.0389 d_med=0.241289
    [shadow] C2 (B): norm=0.254377 krum=0.240102 mkrum=KEEP tm_trim=0.7306 (lo 0.3819 / hi 0.3487) med_prov=0.0370 d_med=0.252235
    [shadow] C3 (B): norm=0.340330 krum=0.389596 mkrum=KEEP tm_trim=0.8145 (lo 0.4191 / hi 0.3954) med_prov=0.0265 d_med=0.319251
    [shadow] C4 (B): norm=0.389510 krum=0.447335 mkrum=REJECT tm_trim=0.7971 (lo 0.4104 / hi 0.3867) med_prov=0.0261 d_med=0.346144
    [shadow] C5 (A): norm=0.155819 krum=0.125772 mkrum=KEEP tm_trim=0.0437 (lo 0.0000 / hi 0.0437) med_prov=0.1417 d_med=0.028976
    [shadow] C6 (A): norm=0.155819 krum=0.125772 mkrum=KEEP tm_trim=0.1132 (lo 0.0065 / hi 0.1067) med_prov=0.7014 d_med=0.028976
[shadow] round 37
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.320529 krum=0.349751 mkrum=KEEP tm_trim=0.7872 (lo 0.4072 / hi 0.3800) med_prov=0.0298 d_med=0.298525
    [shadow] C1 (B): norm=0.243812 krum=0.226789 mkrum=KEEP tm_trim=0.7098 (lo 0.3734 / hi 0.3363) med_prov=0.0392 d_med=0.238784
    [shadow] C2 (B): norm=0.258532 krum=0.240357 mkrum=KEEP tm_trim=0.7399 (lo 0.3867 / hi 0.3532) med_prov=0.0362 d_med=0.252474
    [shadow] C3 (B): norm=0.356701 krum=0.399933 mkrum=REJECT tm_trim=0.8010 (lo 0.4126 / hi 0.3884) med_prov=0.0272 d_med=0.326941
    [shadow] C4 (B): norm=0.387901 krum=0.450574 mkrum=REJECT tm_trim=0.8042 (lo 0.4139 / hi 0.3903) med_prov=0.0255 d_med=0.346163
    [shadow] C5 (A): norm=0.155361 krum=0.124553 mkrum=KEEP tm_trim=0.0459 (lo 0.0000 / hi 0.0459) med_prov=0.1378 d_med=0.028261
    [shadow] C6 (A): norm=0.155361 krum=0.124553 mkrum=KEEP tm_trim=0.1120 (lo 0.0062 / hi 0.1058) med_prov=0.7043 d_med=0.028261
[shadow] round 38
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.341189 krum=0.372183 mkrum=KEEP tm_trim=0.7785 (lo 0.4041 / hi 0.3745) med_prov=0.0324 d_med=0.311804
    [shadow] C1 (B): norm=0.239408 krum=0.227758 mkrum=KEEP tm_trim=0.6911 (lo 0.3656 / hi 0.3254) med_prov=0.0440 d_med=0.239556
    [shadow] C2 (B): norm=0.247136 krum=0.240872 mkrum=KEEP tm_trim=0.7286 (lo 0.3828 / hi 0.3458) med_prov=0.0395 d_med=0.252778
    [shadow] C3 (B): norm=0.380658 krum=0.453135 mkrum=REJECT tm_trim=0.8190 (lo 0.4216 / hi 0.3974) med_prov=0.0265 d_med=0.352837
    [shadow] C4 (B): norm=0.412000 krum=0.494258 mkrum=REJECT tm_trim=0.8144 (lo 0.4189 / hi 0.3954) med_prov=0.0260 d_med=0.366455
    [shadow] C5 (A): norm=0.159495 krum=0.125973 mkrum=KEEP tm_trim=0.0499 (lo 0.0000 / hi 0.0499) med_prov=0.1323 d_med=0.030935
    [shadow] C6 (A): norm=0.159495 krum=0.125973 mkrum=KEEP tm_trim=0.1185 (lo 0.0070 / hi 0.1116) med_prov=0.6993 d_med=0.030935
[shadow] round 39
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.341253 krum=0.364413 mkrum=KEEP tm_trim=0.7941 (lo 0.4098 / hi 0.3843) med_prov=0.0293 d_med=0.307302
    [shadow] C1 (B): norm=0.241519 krum=0.223025 mkrum=KEEP tm_trim=0.7075 (lo 0.3719 / hi 0.3356) med_prov=0.0406 d_med=0.235504
    [shadow] C2 (B): norm=0.254275 krum=0.238224 mkrum=KEEP tm_trim=0.7417 (lo 0.3882 / hi 0.3535) med_prov=0.0364 d_med=0.251202
    [shadow] C3 (B): norm=0.364136 krum=0.410542 mkrum=REJECT tm_trim=0.8112 (lo 0.4173 / hi 0.3939) med_prov=0.0265 d_med=0.331060
    [shadow] C4 (B): norm=0.349882 krum=0.382180 mkrum=REJECT tm_trim=0.7829 (lo 0.4062 / hi 0.3767) med_prov=0.0296 d_med=0.316071
    [shadow] C5 (A): norm=0.155528 krum=0.122188 mkrum=KEEP tm_trim=0.0386 (lo 0.0000 / hi 0.0386) med_prov=0.1410 d_med=0.027976
    [shadow] C6 (A): norm=0.155528 krum=0.122188 mkrum=KEEP tm_trim=0.1239 (lo 0.0065 / hi 0.1174) med_prov=0.6965 d_med=0.027976
[shadow] round 40
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.347237 krum=0.383425 mkrum=KEEP tm_trim=0.7914 (lo 0.4091 / hi 0.3823) med_prov=0.0290 d_med=0.316249
    [shadow] C1 (B): norm=0.243317 krum=0.230756 mkrum=KEEP tm_trim=0.7088 (lo 0.3723 / hi 0.3365) med_prov=0.0390 d_med=0.242598
    [shadow] C2 (B): norm=0.247119 krum=0.234374 mkrum=KEEP tm_trim=0.7277 (lo 0.3817 / hi 0.3460) med_prov=0.0380 d_med=0.246159
    [shadow] C3 (B): norm=0.374046 krum=0.429311 mkrum=REJECT tm_trim=0.8130 (lo 0.4193 / hi 0.3938) med_prov=0.0264 d_med=0.340179
    [shadow] C4 (B): norm=0.373645 krum=0.405474 mkrum=REJECT tm_trim=0.7994 (lo 0.4114 / hi 0.3881) med_prov=0.0272 d_med=0.329330
    [shadow] C5 (A): norm=0.160093 krum=0.123340 mkrum=KEEP tm_trim=0.0402 (lo 0.0000 / hi 0.0402) med_prov=0.1408 d_med=0.028485
    [shadow] C6 (A): norm=0.160093 krum=0.123340 mkrum=KEEP tm_trim=0.1194 (lo 0.0062 / hi 0.1132) med_prov=0.6997 d_med=0.028485
[shadow] round 41
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C0 (B), C4 (B)
    [shadow] C0 (B): norm=0.336531 krum=0.365976 mkrum=REJECT tm_trim=0.8025 (lo 0.4141 / hi 0.3884) med_prov=0.0280 d_med=0.305275
    [shadow] C1 (B): norm=0.245874 krum=0.225565 mkrum=KEEP tm_trim=0.7129 (lo 0.3734 / hi 0.3395) med_prov=0.0383 d_med=0.238483
    [shadow] C2 (B): norm=0.251968 krum=0.233777 mkrum=KEEP tm_trim=0.7450 (lo 0.3895 / hi 0.3555) med_prov=0.0350 d_med=0.246726
    [shadow] C3 (B): norm=0.326615 krum=0.362363 mkrum=KEEP tm_trim=0.7975 (lo 0.4113 / hi 0.3862) med_prov=0.0286 d_med=0.307993
    [shadow] C4 (B): norm=0.365157 krum=0.395266 mkrum=REJECT tm_trim=0.7839 (lo 0.4053 / hi 0.3786) med_prov=0.0282 d_med=0.322089
    [shadow] C5 (A): norm=0.151746 krum=0.121159 mkrum=KEEP tm_trim=0.0409 (lo 0.0000 / hi 0.0409) med_prov=0.1415 d_med=0.027293
    [shadow] C6 (A): norm=0.151746 krum=0.121159 mkrum=KEEP tm_trim=0.1172 (lo 0.0064 / hi 0.1109) med_prov=0.7004 d_med=0.027293
[shadow] round 42
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.339203 krum=0.367654 mkrum=KEEP tm_trim=0.7897 (lo 0.4074 / hi 0.3823) med_prov=0.0296 d_med=0.309452
    [shadow] C1 (B): norm=0.244873 krum=0.224679 mkrum=KEEP tm_trim=0.7134 (lo 0.3752 / hi 0.3381) med_prov=0.0392 d_med=0.241411
    [shadow] C2 (B): norm=0.245954 krum=0.228350 mkrum=KEEP tm_trim=0.7282 (lo 0.3817 / hi 0.3465) med_prov=0.0375 d_med=0.245040
    [shadow] C3 (B): norm=0.361422 krum=0.421262 mkrum=REJECT tm_trim=0.8211 (lo 0.4221 / hi 0.3991) med_prov=0.0245 d_med=0.335697
    [shadow] C4 (B): norm=0.379286 krum=0.423238 mkrum=REJECT tm_trim=0.7890 (lo 0.4073 / hi 0.3817) med_prov=0.0278 d_med=0.334843
    [shadow] C5 (A): norm=0.156111 krum=0.122047 mkrum=KEEP tm_trim=0.0406 (lo 0.0000 / hi 0.0406) med_prov=0.1436 d_med=0.028120
    [shadow] C6 (A): norm=0.156111 krum=0.122047 mkrum=KEEP tm_trim=0.1179 (lo 0.0063 / hi 0.1117) med_prov=0.6978 d_med=0.028120
[shadow] round 43
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.346987 krum=0.374812 mkrum=KEEP tm_trim=0.7890 (lo 0.4083 / hi 0.3807) med_prov=0.0296 d_med=0.311832
    [shadow] C1 (B): norm=0.242400 krum=0.219880 mkrum=KEEP tm_trim=0.7085 (lo 0.3720 / hi 0.3365) med_prov=0.0391 d_med=0.238034
    [shadow] C2 (B): norm=0.246985 krum=0.226010 mkrum=KEEP tm_trim=0.7305 (lo 0.3826 / hi 0.3479) med_prov=0.0362 d_med=0.244093
    [shadow] C3 (B): norm=0.348449 krum=0.386251 mkrum=REJECT tm_trim=0.8095 (lo 0.4162 / hi 0.3932) med_prov=0.0265 d_med=0.320804
    [shadow] C4 (B): norm=0.382880 krum=0.436000 mkrum=REJECT tm_trim=0.8060 (lo 0.4146 / hi 0.3915) med_prov=0.0251 d_med=0.341544
    [shadow] C5 (A): norm=0.158210 krum=0.120036 mkrum=KEEP tm_trim=0.0451 (lo 0.0000 / hi 0.0451) med_prov=0.1398 d_med=0.028141
    [shadow] C6 (A): norm=0.158210 krum=0.120036 mkrum=KEEP tm_trim=0.1114 (lo 0.0063 / hi 0.1051) med_prov=0.7037 d_med=0.028141
[shadow] round 44
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.345032 krum=0.375629 mkrum=KEEP tm_trim=0.7852 (lo 0.4050 / hi 0.3802) med_prov=0.0284 d_med=0.311755
    [shadow] C1 (B): norm=0.245268 krum=0.224189 mkrum=KEEP tm_trim=0.7124 (lo 0.3737 / hi 0.3388) med_prov=0.0375 d_med=0.239844
    [shadow] C2 (B): norm=0.249430 krum=0.229158 mkrum=KEEP tm_trim=0.7318 (lo 0.3833 / hi 0.3485) med_prov=0.0359 d_med=0.244779
    [shadow] C3 (B): norm=0.339767 krum=0.382475 mkrum=REJECT tm_trim=0.8154 (lo 0.4184 / hi 0.3970) med_prov=0.0248 d_med=0.317624
    [shadow] C4 (B): norm=0.367727 krum=0.407567 mkrum=REJECT tm_trim=0.8029 (lo 0.4134 / hi 0.3895) med_prov=0.0258 d_med=0.328270
    [shadow] C5 (A): norm=0.153459 krum=0.120802 mkrum=KEEP tm_trim=0.0403 (lo 0.0000 / hi 0.0403) med_prov=0.1419 d_med=0.027150
    [shadow] C6 (A): norm=0.153459 krum=0.120802 mkrum=KEEP tm_trim=0.1121 (lo 0.0062 / hi 0.1059) med_prov=0.7057 d_med=0.027150
[shadow] round 45
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.364013 krum=0.411999 mkrum=KEEP tm_trim=0.8102 (lo 0.4163 / hi 0.3939) med_prov=0.0261 d_med=0.327599
    [shadow] C1 (B): norm=0.247056 krum=0.227046 mkrum=KEEP tm_trim=0.7025 (lo 0.3700 / hi 0.3326) med_prov=0.0394 d_med=0.241528
    [shadow] C2 (B): norm=0.252741 krum=0.237284 mkrum=KEEP tm_trim=0.7268 (lo 0.3810 / hi 0.3457) med_prov=0.0371 d_med=0.252072
    [shadow] C3 (B): norm=0.375481 krum=0.435935 mkrum=REJECT tm_trim=0.8240 (lo 0.4231 / hi 0.4009) med_prov=0.0239 d_med=0.342747
    [shadow] C4 (B): norm=0.373629 krum=0.420220 mkrum=REJECT tm_trim=0.7815 (lo 0.4034 / hi 0.3781) med_prov=0.0285 d_med=0.333239
    [shadow] C5 (A): norm=0.163324 krum=0.125624 mkrum=KEEP tm_trim=0.0369 (lo 0.0000 / hi 0.0369) med_prov=0.1460 d_med=0.028308
    [shadow] C6 (A): norm=0.163324 krum=0.125624 mkrum=KEEP tm_trim=0.1181 (lo 0.0062 / hi 0.1119) med_prov=0.6990 d_med=0.028308
[shadow] round 46
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.344072 krum=0.373422 mkrum=KEEP tm_trim=0.7813 (lo 0.4047 / hi 0.3766) med_prov=0.0320 d_med=0.309904
    [shadow] C1 (B): norm=0.248819 krum=0.231887 mkrum=KEEP tm_trim=0.7106 (lo 0.3742 / hi 0.3363) med_prov=0.0403 d_med=0.245002
    [shadow] C2 (B): norm=0.246710 krum=0.236641 mkrum=KEEP tm_trim=0.7286 (lo 0.3822 / hi 0.3464) med_prov=0.0378 d_med=0.249831
    [shadow] C3 (B): norm=0.387972 krum=0.466240 mkrum=REJECT tm_trim=0.8164 (lo 0.4191 / hi 0.3973) med_prov=0.0261 d_med=0.352804
    [shadow] C4 (B): norm=0.376291 krum=0.433059 mkrum=REJECT tm_trim=0.7989 (lo 0.4129 / hi 0.3859) med_prov=0.0281 d_med=0.338345
    [shadow] C5 (A): norm=0.160579 krum=0.126875 mkrum=KEEP tm_trim=0.0425 (lo 0.0000 / hi 0.0425) med_prov=0.1404 d_med=0.030063
    [shadow] C6 (A): norm=0.160579 krum=0.126875 mkrum=KEEP tm_trim=0.1218 (lo 0.0069 / hi 0.1149) med_prov=0.6953 d_med=0.030063
[shadow] round 47
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C0 (B), C4 (B)
    [shadow] C0 (B): norm=0.367236 krum=0.417316 mkrum=REJECT tm_trim=0.7956 (lo 0.4095 / hi 0.3861) med_prov=0.0268 d_med=0.327975
    [shadow] C1 (B): norm=0.250520 krum=0.238617 mkrum=KEEP tm_trim=0.7220 (lo 0.3772 / hi 0.3448) med_prov=0.0361 d_med=0.246685
    [shadow] C2 (B): norm=0.250683 krum=0.243314 mkrum=KEEP tm_trim=0.7388 (lo 0.3859 / hi 0.3529) med_prov=0.0346 d_med=0.251416
    [shadow] C3 (B): norm=0.322225 krum=0.359477 mkrum=KEEP tm_trim=0.8073 (lo 0.4163 / hi 0.3910) med_prov=0.0268 d_med=0.303137
    [shadow] C4 (B): norm=0.366163 krum=0.406250 mkrum=REJECT tm_trim=0.7850 (lo 0.4050 / hi 0.3800) med_prov=0.0269 d_med=0.326136
    [shadow] C5 (A): norm=0.153776 krum=0.127328 mkrum=KEEP tm_trim=0.0376 (lo 0.0000 / hi 0.0376) med_prov=0.1467 d_med=0.027124
    [shadow] C6 (A): norm=0.153776 krum=0.127328 mkrum=KEEP tm_trim=0.1137 (lo 0.0061 / hi 0.1077) med_prov=0.7020 d_med=0.027124
[shadow] round 48
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C0 (B), C4 (B)
    [shadow] C0 (B): norm=0.356317 krum=0.406665 mkrum=REJECT tm_trim=0.7900 (lo 0.4087 / hi 0.3813) med_prov=0.0289 d_med=0.324599
    [shadow] C1 (B): norm=0.251913 krum=0.247615 mkrum=KEEP tm_trim=0.7147 (lo 0.3741 / hi 0.3406) med_prov=0.0380 d_med=0.250927
    [shadow] C2 (B): norm=0.259547 krum=0.257220 mkrum=KEEP tm_trim=0.7352 (lo 0.3846 / hi 0.3506) med_prov=0.0362 d_med=0.260567
    [shadow] C3 (B): norm=0.344009 krum=0.384349 mkrum=KEEP tm_trim=0.7848 (lo 0.4060 / hi 0.3787) med_prov=0.0310 d_med=0.317493
    [shadow] C4 (B): norm=0.433281 krum=0.545942 mkrum=REJECT tm_trim=0.8181 (lo 0.4201 / hi 0.3980) med_prov=0.0232 d_med=0.382691
    [shadow] C5 (A): norm=0.165066 krum=0.135240 mkrum=KEEP tm_trim=0.0527 (lo 0.0000 / hi 0.0527) med_prov=0.1321 d_med=0.030057
    [shadow] C6 (A): norm=0.165066 krum=0.135240 mkrum=KEEP tm_trim=0.1045 (lo 0.0065 / hi 0.0980) med_prov=0.7107 d_med=0.030057
[shadow] round 49
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.333481 krum=0.368952 mkrum=KEEP tm_trim=0.7863 (lo 0.4085 / hi 0.3778) med_prov=0.0330 d_med=0.308042
    [shadow] C1 (B): norm=0.246783 krum=0.229449 mkrum=KEEP tm_trim=0.6966 (lo 0.3672 / hi 0.3293) med_prov=0.0422 d_med=0.244641
    [shadow] C2 (B): norm=0.257313 krum=0.237741 mkrum=KEEP tm_trim=0.7271 (lo 0.3814 / hi 0.3457) med_prov=0.0379 d_med=0.252356
    [shadow] C3 (B): norm=0.438017 krum=0.563266 mkrum=REJECT tm_trim=0.8298 (lo 0.4260 / hi 0.4038) med_prov=0.0236 d_med=0.393948
    [shadow] C4 (B): norm=0.375121 krum=0.422356 mkrum=REJECT tm_trim=0.7939 (lo 0.4097 / hi 0.3842) med_prov=0.0296 d_med=0.334315
    [shadow] C5 (A): norm=0.168220 krum=0.128724 mkrum=KEEP tm_trim=0.0386 (lo 0.0000 / hi 0.0386) med_prov=0.1451 d_med=0.032094
    [shadow] C6 (A): norm=0.168220 krum=0.128724 mkrum=KEEP tm_trim=0.1277 (lo 0.0072 / hi 0.1204) med_prov=0.6886 d_med=0.032094
[shadow] round 50
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C0 (B), C4 (B)
    [shadow] C0 (B): norm=0.371051 krum=0.407795 mkrum=REJECT tm_trim=0.8010 (lo 0.4135 / hi 0.3875) med_prov=0.0272 d_med=0.326952
    [shadow] C1 (B): norm=0.247981 krum=0.229866 mkrum=KEEP tm_trim=0.7193 (lo 0.3770 / hi 0.3422) med_prov=0.0382 d_med=0.239673
    [shadow] C2 (B): norm=0.251748 krum=0.239314 mkrum=KEEP tm_trim=0.7386 (lo 0.3870 / hi 0.3515) med_prov=0.0360 d_med=0.249487
    [shadow] C3 (B): norm=0.346542 krum=0.385570 mkrum=KEEP tm_trim=0.8007 (lo 0.4118 / hi 0.3889) med_prov=0.0279 d_med=0.318788
    [shadow] C4 (B): norm=0.359060 krum=0.396566 mkrum=REJECT tm_trim=0.7826 (lo 0.4043 / hi 0.3783) med_prov=0.0285 d_med=0.322732
    [shadow] C5 (A): norm=0.160829 krum=0.123305 mkrum=KEEP tm_trim=0.0381 (lo 0.0000 / hi 0.0381) med_prov=0.1422 d_med=0.027849
    [shadow] C6 (A): norm=0.160829 krum=0.123305 mkrum=KEEP tm_trim=0.1197 (lo 0.0063 / hi 0.1134) med_prov=0.7000 d_med=0.027849

================================================================================
📊 DETAILED EXPERIMENT STATISTICS FOR DATA COLLECTION
================================================================================

--------------------------------------------------------------------------------
1️⃣  GLOBAL ACCURACY (Per Round)
--------------------------------------------------------------------------------
Round    | Clean Accuracy  | Accuracy Change  
--------------------------------------------------------------------------------
1        | 0.456667        |         +0.000000
2        | 0.694000        |         +0.237333
3        | 0.775000        |         +0.081000
4        | 0.808000        |         +0.033000
5        | 0.823667        |         +0.015667
6        | 0.834333        |         +0.010667
7        | 0.848000        |         +0.013667
8        | 0.858000        |         +0.010000
9        | 0.877000        |         +0.019000
10       | 0.877000        |         +0.000000
11       | 0.888333        |         +0.011333
12       | 0.885333        |         -0.003000
13       | 0.889000        |         +0.003667
14       | 0.885667        |         -0.003333
15       | 0.886333        |         +0.000667
16       | 0.888000        |         +0.001667
17       | 0.889333        |         +0.001333
18       | 0.886333        |         -0.003000
19       | 0.888000        |         +0.001667
20       | 0.890000        |         +0.002000
21       | 0.883000        |         -0.007000
22       | 0.884667        |         +0.001667
23       | 0.891333        |         +0.006667
24       | 0.883667        |         -0.007667
25       | 0.900333        |         +0.016667
26       | 0.895333        |         -0.005000
27       | 0.894667        |         -0.000667
28       | 0.899667        |         +0.005000
29       | 0.902000        |         +0.002333
30       | 0.894333        |         -0.007667
31       | 0.893667        |         -0.000667
32       | 0.898000        |         +0.004333
33       | 0.895667        |         -0.002333
34       | 0.898000        |         +0.002333
35       | 0.902000        |         +0.004000
36       | 0.901667        |         -0.000333
37       | 0.902667        |         +0.001000
38       | 0.899667        |         -0.003000
39       | 0.906333        |         +0.006667
40       | 0.900333        |         -0.006000
41       | 0.905333        |         +0.005000
42       | 0.901333        |         -0.004000
43       | 0.908333        |         +0.007000
44       | 0.904000        |         -0.004333
45       | 0.905000        |         +0.001000
46       | 0.906333        |         +0.001333
47       | 0.902000        |         -0.004333
48       | 0.908000        |         +0.006000
49       | 0.910000        |         +0.002000
50       | 0.913000        |         +0.003000
--------------------------------------------------------------------------------
Summary: Initial=0.456667, Final=0.913000, Best=0.913000, Change=+0.456333

--------------------------------------------------------------------------------
2️⃣  COSINE SIMILARITY (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A) | Mean | Std
--------------------------------------------------------------------------------
1      | 0.625569       | 0.612901       | 0.578039       | 0.652474       | 0.631754       | 0.804432       | 0.804432       | 0.672800 | 0.085815
2      | 0.692583       | 0.632574       | 0.493357       | 0.660443       | 0.677867       | 0.812746       | 0.812746       | 0.683188 | 0.101982
3      | 0.586602       | 0.500550       | 0.419542       | 0.540418       | 0.575656       | 0.755497       | 0.755497       | 0.590538 | 0.116195
4      | 0.475413       | 0.392811       | 0.360430       | 0.406714       | 0.465359       | 0.695353       | 0.695353       | 0.498776 | 0.129720
5      | 0.377631       | 0.282641       | 0.275377       | 0.303400       | 0.366260       | 0.631304       | 0.631304       | 0.409702 | 0.144725
6      | 0.297294       | 0.194032       | 0.221528       | 0.250833       | 0.311662       | 0.585779       | 0.585779       | 0.349558 | 0.154039
7      | 0.235443       | 0.187983       | 0.157804       | 0.212344       | 0.261498       | 0.553011       | 0.553011       | 0.308728 | 0.157479
8      | 0.196649       | 0.156034       | 0.114952       | 0.198283       | 0.229144       | 0.528095       | 0.528095       | 0.278750 | 0.161206
9      | 0.208029       | 0.173731       | 0.133834       | 0.193505       | 0.240002       | 0.536928       | 0.536928       | 0.288994 | 0.159632
10     | 0.188755       | 0.157232       | 0.102613       | 0.194487       | 0.221722       | 0.523731       | 0.523731       | 0.273182 | 0.162154
11     | 0.187813       | 0.139140       | 0.061164       | 0.164773       | 0.213969       | 0.509702       | 0.509702       | 0.255181 | 0.166939
12     | 0.154652       | 0.131256       | 0.068086       | 0.160038       | 0.210743       | 0.502312       | 0.502312       | 0.247057 | 0.166124
13     | 0.175157       | 0.131318       | 0.076819       | 0.152396       | 0.204454       | 0.504793       | 0.504793       | 0.249961 | 0.165235
14     | 0.163184       | 0.134224       | 0.084741       | 0.143020       | 0.186402       | 0.500720       | 0.500720       | 0.244716 | 0.164433
15     | 0.159219       | 0.125936       | 0.069683       | 0.153164       | 0.182969       | 0.496976       | 0.496976       | 0.240703 | 0.165360
16     | 0.164115       | 0.117835       | 0.078245       | 0.143109       | 0.178979       | 0.495710       | 0.495710       | 0.239100 | 0.165066
17     | 0.159827       | 0.130833       | 0.084791       | 0.129141       | 0.177396       | 0.496468       | 0.496468       | 0.239275 | 0.164834
18     | 0.174841       | 0.125210       | 0.050409       | 0.127778       | 0.158877       | 0.488789       | 0.488789       | 0.230670 | 0.167214
19     | 0.150588       | 0.111285       | 0.065974       | 0.109875       | 0.151323       | 0.481280       | 0.481280       | 0.221658 | 0.166356
20     | 0.158614       | 0.107287       | 0.066654       | 0.077143       | 0.142229       | 0.474335       | 0.474335       | 0.214371 | 0.167159
21     | 0.136819       | 0.121219       | 0.077692       | 0.107669       | 0.146748       | 0.480996       | 0.480996       | 0.221734 | 0.165240
22     | 0.135561       | 0.097370       | 0.080646       | 0.092160       | 0.156886       | 0.476531       | 0.476531       | 0.216526 | 0.166238
23     | 0.130574       | 0.099617       | 0.069986       | 0.088857       | 0.142883       | 0.471651       | 0.471651       | 0.210746 | 0.166560
24     | 0.110596       | 0.115755       | 0.085320       | 0.076836       | 0.139244       | 0.471413       | 0.471413       | 0.210083 | 0.166356
25     | 0.150830       | 0.121828       | 0.071615       | 0.090671       | 0.131678       | 0.479154       | 0.479154       | 0.217847 | 0.167014
26     | 0.129621       | 0.124380       | 0.074418       | 0.092842       | 0.150531       | 0.479567       | 0.479567       | 0.218704 | 0.166579
27     | 0.147829       | 0.103110       | 0.092895       | 0.082842       | 0.136528       | 0.477732       | 0.477732       | 0.216953 | 0.166302
28     | 0.142270       | 0.120520       | 0.103282       | 0.080570       | 0.143913       | 0.482636       | 0.482636       | 0.222261 | 0.165922
29     | 0.123526       | 0.106848       | 0.078865       | 0.092463       | 0.141760       | 0.475068       | 0.475068       | 0.213371 | 0.166574
30     | 0.108040       | 0.118995       | 0.090220       | 0.082695       | 0.142984       | 0.474652       | 0.474652       | 0.213177 | 0.166362
31     | 0.116987       | 0.115286       | 0.075505       | 0.097074       | 0.121866       | 0.472142       | 0.472142       | 0.210143 | 0.166334
32     | 0.153713       | 0.110199       | 0.094358       | 0.104488       | 0.132890       | 0.483902       | 0.483902       | 0.223350 | 0.165778
33     | 0.123578       | 0.098196       | 0.068524       | 0.107915       | 0.139594       | 0.473622       | 0.473622       | 0.212150 | 0.166615
34     | 0.130422       | 0.120527       | 0.103092       | 0.098456       | 0.129496       | 0.480901       | 0.480901       | 0.220542 | 0.165049
35     | 0.113795       | 0.118480       | 0.097568       | 0.091165       | 0.154121       | 0.479540       | 0.479540       | 0.219172 | 0.165715
36     | 0.112290       | 0.117324       | 0.092982       | 0.082461       | 0.148867       | 0.475903       | 0.475903       | 0.215104 | 0.166072
37     | 0.105270       | 0.118828       | 0.105012       | 0.111451       | 0.143438       | 0.481164       | 0.481164       | 0.220904 | 0.165043
38     | 0.123463       | 0.106126       | 0.073090       | 0.087437       | 0.142831       | 0.470470       | 0.470470       | 0.210555 | 0.165721
39     | 0.140856       | 0.126434       | 0.098917       | 0.120110       | 0.138337       | 0.488532       | 0.488532       | 0.228817 | 0.164751
40     | 0.128928       | 0.109309       | 0.105586       | 0.119824       | 0.165908       | 0.488699       | 0.488699       | 0.229565 | 0.164905
41     | 0.128918       | 0.120380       | 0.101093       | 0.080855       | 0.164985       | 0.484366       | 0.484366       | 0.223566 | 0.166663
42     | 0.124298       | 0.113530       | 0.100609       | 0.087815       | 0.160798       | 0.481307       | 0.481307       | 0.221380 | 0.165735
43     | 0.143859       | 0.125984       | 0.112164       | 0.110992       | 0.148723       | 0.490529       | 0.490529       | 0.231826 | 0.164152
44     | 0.134878       | 0.117893       | 0.107949       | 0.087923       | 0.144901       | 0.483070       | 0.483070       | 0.222812 | 0.165472
45     | 0.139670       | 0.135188       | 0.108590       | 0.116966       | 0.153037       | 0.492354       | 0.492354       | 0.234023 | 0.163941
46     | 0.142531       | 0.116701       | 0.089873       | 0.115527       | 0.137235       | 0.483390       | 0.483390       | 0.224093 | 0.164751
47     | 0.142931       | 0.102254       | 0.080089       | 0.084058       | 0.149542       | 0.477744       | 0.477744       | 0.216337 | 0.167158
48     | 0.126991       | 0.108823       | 0.090461       | 0.114506       | 0.154654       | 0.482127       | 0.482127       | 0.222813 | 0.164992
49     | 0.123657       | 0.129306       | 0.127969       | 0.129183       | 0.155872       | 0.492337       | 0.492337       | 0.235809 | 0.162535
50     | 0.169343       | 0.139028       | 0.108531       | 0.114644       | 0.146919       | 0.497573       | 0.497573       | 0.239087 | 0.164548
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
2b. EUCLIDEAN DISTANCE (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A) | Mean | Std
--------------------------------------------------------------------------------
1      | 0.720415       | 0.744663       | 0.782136       | 0.765626       | 0.754365       | 0.183776       | 0.183776       | 0.590680 | 0.257942
2      | 0.517642       | 0.569055       | 0.671576       | 0.556356       | 0.511131       | 0.144193       | 0.144193       | 0.444878 | 0.196304
3      | 0.455659       | 0.440125       | 0.494431       | 0.468007       | 0.457744       | 0.110210       | 0.110210       | 0.362341 | 0.160184
4      | 0.399283       | 0.361289       | 0.386764       | 0.428457       | 0.427823       | 0.089495       | 0.089495       | 0.311801 | 0.142243
5      | 0.399735       | 0.336334       | 0.353872       | 0.417490       | 0.409264       | 0.083096       | 0.083096       | 0.297555 | 0.138340
6      | 0.394263       | 0.324395       | 0.335986       | 0.387440       | 0.384010       | 0.078742       | 0.078742       | 0.283368 | 0.131721
7      | 0.376062       | 0.309030       | 0.328706       | 0.393514       | 0.374779       | 0.076616       | 0.076616       | 0.276475 | 0.129259
8      | 0.363905       | 0.305584       | 0.326198       | 0.389500       | 0.392110       | 0.076321       | 0.076321       | 0.275706 | 0.129410
9      | 0.377685       | 0.307842       | 0.329316       | 0.393501       | 0.392082       | 0.076913       | 0.076913       | 0.279179 | 0.131300
10     | 0.368306       | 0.299995       | 0.319701       | 0.389153       | 0.377816       | 0.074624       | 0.074624       | 0.272031 | 0.128269
11     | 0.373735       | 0.303441       | 0.329962       | 0.382691       | 0.363946       | 0.074346       | 0.074346       | 0.271781 | 0.127357
12     | 0.349837       | 0.289650       | 0.315070       | 0.378873       | 0.362059       | 0.071757       | 0.071757       | 0.262715 | 0.123837
13     | 0.353814       | 0.289407       | 0.313516       | 0.365434       | 0.359713       | 0.071613       | 0.071613       | 0.260730 | 0.122220
14     | 0.359381       | 0.288636       | 0.308222       | 0.358118       | 0.351685       | 0.070288       | 0.070288       | 0.258088 | 0.121309
15     | 0.352384       | 0.287426       | 0.304802       | 0.362158       | 0.333905       | 0.069533       | 0.069533       | 0.254249 | 0.119234
16     | 0.345407       | 0.292622       | 0.304199       | 0.360335       | 0.352238       | 0.070177       | 0.070177       | 0.256451 | 0.120038
17     | 0.340681       | 0.285484       | 0.297195       | 0.348256       | 0.336597       | 0.067944       | 0.067944       | 0.249157 | 0.116586
18     | 0.347136       | 0.290131       | 0.305268       | 0.348864       | 0.342321       | 0.069337       | 0.069337       | 0.253199 | 0.118083
19     | 0.332348       | 0.283064       | 0.302168       | 0.339599       | 0.339986       | 0.067744       | 0.067744       | 0.247522 | 0.115334
20     | 0.338133       | 0.276230       | 0.292541       | 0.331252       | 0.338269       | 0.066539       | 0.066539       | 0.244215 | 0.114480
21     | 0.332612       | 0.276806       | 0.291781       | 0.324215       | 0.329396       | 0.066330       | 0.066330       | 0.241067 | 0.112130
22     | 0.322564       | 0.275114       | 0.286000       | 0.329002       | 0.321982       | 0.065227       | 0.065227       | 0.237874 | 0.110755
23     | 0.321716       | 0.269914       | 0.291446       | 0.320890       | 0.313146       | 0.064692       | 0.064692       | 0.235214 | 0.109164
24     | 0.309609       | 0.271550       | 0.279473       | 0.306505       | 0.316419       | 0.063288       | 0.063288       | 0.230019 | 0.106515
25     | 0.306356       | 0.270064       | 0.283755       | 0.303646       | 0.306876       | 0.062158       | 0.062158       | 0.227859 | 0.105538
26     | 0.308421       | 0.270482       | 0.285321       | 0.315206       | 0.297118       | 0.062998       | 0.062998       | 0.228935 | 0.105820
27     | 0.304893       | 0.262246       | 0.277272       | 0.305062       | 0.298204       | 0.061497       | 0.061497       | 0.224382 | 0.104016
28     | 0.305362       | 0.266981       | 0.276609       | 0.311010       | 0.303377       | 0.062008       | 0.062008       | 0.226765 | 0.105245
29     | 0.293559       | 0.260654       | 0.279231       | 0.307555       | 0.292166       | 0.060519       | 0.060519       | 0.222029 | 0.103016
30     | 0.301442       | 0.262096       | 0.272194       | 0.282792       | 0.311587       | 0.060657       | 0.060657       | 0.221632 | 0.102971
31     | 0.301101       | 0.265874       | 0.286020       | 0.307204       | 0.296363       | 0.062224       | 0.062224       | 0.225859 | 0.104213
32     | 0.291572       | 0.259757       | 0.272309       | 0.292711       | 0.298208       | 0.060048       | 0.060048       | 0.219236 | 0.101424
33     | 0.300703       | 0.269082       | 0.282901       | 0.304959       | 0.298109       | 0.062692       | 0.062692       | 0.225877 | 0.103818
34     | 0.303817       | 0.261388       | 0.274292       | 0.301088       | 0.314639       | 0.061375       | 0.061375       | 0.225425 | 0.105109
35     | 0.293349       | 0.265775       | 0.278164       | 0.314651       | 0.314998       | 0.062288       | 0.062288       | 0.227359 | 0.105701
36     | 0.311028       | 0.266117       | 0.280142       | 0.298809       | 0.318866       | 0.062792       | 0.062792       | 0.228650 | 0.106181
37     | 0.287661       | 0.263505       | 0.280463       | 0.303882       | 0.319426       | 0.062301       | 0.062301       | 0.225649 | 0.104583
38     | 0.304105       | 0.264802       | 0.281379       | 0.328591       | 0.338773       | 0.064209       | 0.064209       | 0.235153 | 0.110636
39     | 0.294882       | 0.259497       | 0.278260       | 0.305371       | 0.293994       | 0.061114       | 0.061114       | 0.222033 | 0.102668
40     | 0.304086       | 0.267025       | 0.272583       | 0.315165       | 0.306926       | 0.061981       | 0.061981       | 0.227106 | 0.105726
41     | 0.292299       | 0.262253       | 0.273327       | 0.285407       | 0.297468       | 0.060312       | 0.060312       | 0.218768 | 0.100801
42     | 0.297975       | 0.266401       | 0.272361       | 0.311858       | 0.309992       | 0.062160       | 0.062160       | 0.226130 | 0.104932
43     | 0.299126       | 0.262520       | 0.271292       | 0.299265       | 0.316072       | 0.061543       | 0.061543       | 0.224480 | 0.104396
44     | 0.298943       | 0.264046       | 0.271016       | 0.295448       | 0.303586       | 0.060998       | 0.060998       | 0.222148 | 0.102807
45     | 0.314299       | 0.266472       | 0.279598       | 0.318661       | 0.309623       | 0.063147       | 0.063147       | 0.230707 | 0.107420
46     | 0.299396       | 0.271483       | 0.278399       | 0.325625       | 0.314102       | 0.063572       | 0.063572       | 0.230878 | 0.107230
47     | 0.311126       | 0.270975       | 0.277763       | 0.282620       | 0.301931       | 0.061614       | 0.061614       | 0.223949 | 0.103466
48     | 0.313780       | 0.277664       | 0.289550       | 0.298216       | 0.349912       | 0.065476       | 0.065476       | 0.237154 | 0.110613
49     | 0.299553       | 0.272171       | 0.282906       | 0.360767       | 0.314089       | 0.065389       | 0.065389       | 0.237181 | 0.111751
50     | 0.313066       | 0.263016       | 0.275397       | 0.296098       | 0.299870       | 0.061080       | 0.061080       | 0.224230 | 0.104291
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
2c. GLOBAL LOSS (Per Round)
--------------------------------------------------------------------------------
Round    | Global Loss    
--------------------------------------------------------------------------------
1        | 1.991154       
2        | 0.966186       
3        | 0.660474       
4        | 0.547519       
5        | 0.525599       
6        | 0.489649       
7        | 0.461563       
8        | 0.453002       
9        | 0.405915       
10       | 0.404065       
11       | 0.381145       
12       | 0.410645       
13       | 0.399374       
14       | 0.431015       
15       | 0.447248       
16       | 0.449755       
17       | 0.459933       
18       | 0.511479       
19       | 0.518287       
20       | 0.533837       
21       | 0.587086       
22       | 0.603987       
23       | 0.606484       
24       | 0.648768       
25       | 0.584001       
26       | 0.660172       
27       | 0.654098       
28       | 0.643877       
29       | 0.632248       
30       | 0.695093       
31       | 0.741947       
32       | 0.701255       
33       | 0.765545       
34       | 0.730146       
35       | 0.734020       
36       | 0.737638       
37       | 0.770239       
38       | 0.799902       
39       | 0.761986       
40       | 0.790760       
41       | 0.758204       
42       | 0.795020       
43       | 0.772579       
44       | 0.791023       
45       | 0.804658       
46       | 0.790038       
47       | 0.860566       
48       | 0.850122       
49       | 0.784418       
50       | 0.765824       
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
3️⃣  LOCAL ACCURACY (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A) | Mean | Std
--------------------------------------------------------------------------------
1      | 0.592391       | 0.222826       | 0.326087       | 0.592391       | 0.445652       | 0.222826       | 0.222826       | 0.375000 | 0.156467
2      | 0.766304       | 0.559783       | 0.440217       | 0.663043       | 0.527174       | 0.418478       | 0.418478       | 0.541925 | 0.123274
3      | 0.836957       | 0.701087       | 0.581522       | 0.668478       | 0.581522       | 0.663043       | 0.663043       | 0.670807 | 0.079814
4      | 0.864130       | 0.782609       | 0.619565       | 0.668478       | 0.619565       | 0.755435       | 0.755435       | 0.723602 | 0.084467
5      | 0.869565       | 0.804348       | 0.630435       | 0.668478       | 0.630435       | 0.771739       | 0.771739       | 0.735248 | 0.086114
6      | 0.869565       | 0.788043       | 0.663043       | 0.673913       | 0.657609       | 0.777174       | 0.777174       | 0.743789 | 0.074486
7      | 0.869565       | 0.777174       | 0.646739       | 0.673913       | 0.673913       | 0.798913       | 0.798913       | 0.748447 | 0.077500
8      | 0.853261       | 0.853261       | 0.722826       | 0.668478       | 0.684783       | 0.815217       | 0.815217       | 0.773292 | 0.073360
9      | 0.864130       | 0.826087       | 0.695652       | 0.684783       | 0.695652       | 0.836957       | 0.836957       | 0.777174 | 0.074575
10     | 0.875000       | 0.842391       | 0.706522       | 0.679348       | 0.717391       | 0.858696       | 0.858696       | 0.791149 | 0.079177
11     | 0.885870       | 0.815217       | 0.701087       | 0.679348       | 0.739130       | 0.847826       | 0.847826       | 0.788043 | 0.074857
12     | 0.858696       | 0.875000       | 0.766304       | 0.679348       | 0.744565       | 0.869565       | 0.869565       | 0.809006 | 0.072650
13     | 0.880435       | 0.880435       | 0.771739       | 0.684783       | 0.750000       | 0.880435       | 0.880435       | 0.818323 | 0.075690
14     | 0.869565       | 0.842391       | 0.793478       | 0.684783       | 0.717391       | 0.896739       | 0.896739       | 0.814441 | 0.079314
15     | 0.869565       | 0.858696       | 0.788043       | 0.684783       | 0.750000       | 0.885870       | 0.885870       | 0.817547 | 0.072501
16     | 0.880435       | 0.885870       | 0.760870       | 0.684783       | 0.711957       | 0.880435       | 0.880435       | 0.812112 | 0.083078
17     | 0.885870       | 0.875000       | 0.804348       | 0.690217       | 0.750000       | 0.885870       | 0.885870       | 0.825311 | 0.073516
18     | 0.885870       | 0.869565       | 0.804348       | 0.684783       | 0.744565       | 0.885870       | 0.885870       | 0.822981 | 0.075242
19     | 0.891304       | 0.869565       | 0.782609       | 0.673913       | 0.744565       | 0.880435       | 0.880435       | 0.817547 | 0.078589
20     | 0.891304       | 0.891304       | 0.804348       | 0.679348       | 0.793478       | 0.869565       | 0.869565       | 0.828416 | 0.071031
21     | 0.869565       | 0.858696       | 0.793478       | 0.690217       | 0.755435       | 0.880435       | 0.880435       | 0.818323 | 0.068614
22     | 0.880435       | 0.896739       | 0.809783       | 0.711957       | 0.739130       | 0.864130       | 0.864130       | 0.823758 | 0.067247
23     | 0.891304       | 0.847826       | 0.777174       | 0.695652       | 0.798913       | 0.864130       | 0.864130       | 0.819876 | 0.062672
24     | 0.875000       | 0.847826       | 0.798913       | 0.684783       | 0.760870       | 0.891304       | 0.891304       | 0.821429 | 0.071891
25     | 0.880435       | 0.864130       | 0.788043       | 0.739130       | 0.782609       | 0.869565       | 0.869565       | 0.827640 | 0.052186
26     | 0.880435       | 0.858696       | 0.798913       | 0.684783       | 0.777174       | 0.880435       | 0.880435       | 0.822981 | 0.068614
27     | 0.875000       | 0.875000       | 0.804348       | 0.717391       | 0.766304       | 0.880435       | 0.880435       | 0.828416 | 0.061546
28     | 0.902174       | 0.815217       | 0.804348       | 0.744565       | 0.820652       | 0.885870       | 0.885870       | 0.836957 | 0.052612
29     | 0.880435       | 0.858696       | 0.798913       | 0.739130       | 0.798913       | 0.880435       | 0.880435       | 0.833851 | 0.051465
30     | 0.885870       | 0.831522       | 0.826087       | 0.733696       | 0.750000       | 0.880435       | 0.880435       | 0.826863 | 0.058349
31     | 0.896739       | 0.847826       | 0.782609       | 0.722826       | 0.739130       | 0.864130       | 0.864130       | 0.816770 | 0.063094
32     | 0.902174       | 0.853261       | 0.842391       | 0.744565       | 0.771739       | 0.880435       | 0.880435       | 0.839286 | 0.054878
33     | 0.896739       | 0.847826       | 0.809783       | 0.722826       | 0.793478       | 0.864130       | 0.864130       | 0.828416 | 0.053869
34     | 0.891304       | 0.847826       | 0.820652       | 0.733696       | 0.798913       | 0.875000       | 0.875000       | 0.834627 | 0.051136
35     | 0.885870       | 0.842391       | 0.809783       | 0.739130       | 0.820652       | 0.864130       | 0.864130       | 0.832298 | 0.045231
36     | 0.885870       | 0.836957       | 0.788043       | 0.744565       | 0.793478       | 0.885870       | 0.885870       | 0.831522 | 0.053170
37     | 0.891304       | 0.836957       | 0.798913       | 0.766304       | 0.804348       | 0.880435       | 0.880435       | 0.836957 | 0.045098
38     | 0.891304       | 0.875000       | 0.804348       | 0.766304       | 0.782609       | 0.885870       | 0.885870       | 0.841615 | 0.050770
39     | 0.896739       | 0.885870       | 0.815217       | 0.760870       | 0.831522       | 0.875000       | 0.875000       | 0.848602 | 0.045044
40     | 0.891304       | 0.864130       | 0.826087       | 0.760870       | 0.760870       | 0.885870       | 0.885870       | 0.839286 | 0.053633
41     | 0.885870       | 0.875000       | 0.782609       | 0.766304       | 0.853261       | 0.891304       | 0.891304       | 0.849379 | 0.049104
42     | 0.891304       | 0.836957       | 0.804348       | 0.744565       | 0.788043       | 0.885870       | 0.885870       | 0.833851 | 0.053000
43     | 0.885870       | 0.842391       | 0.836957       | 0.760870       | 0.820652       | 0.880435       | 0.880435       | 0.843944 | 0.041259
44     | 0.896739       | 0.885870       | 0.815217       | 0.755435       | 0.798913       | 0.902174       | 0.902174       | 0.850932 | 0.055641
45     | 0.896739       | 0.875000       | 0.820652       | 0.777174       | 0.831522       | 0.891304       | 0.891304       | 0.854814 | 0.042369
46     | 0.885870       | 0.896739       | 0.804348       | 0.766304       | 0.804348       | 0.885870       | 0.885870       | 0.847050 | 0.049507
47     | 0.875000       | 0.858696       | 0.798913       | 0.755435       | 0.831522       | 0.885870       | 0.885870       | 0.841615 | 0.045788
48     | 0.891304       | 0.853261       | 0.815217       | 0.798913       | 0.782609       | 0.880435       | 0.880435       | 0.843168 | 0.040715
49     | 0.885870       | 0.885870       | 0.798913       | 0.798913       | 0.804348       | 0.891304       | 0.891304       | 0.850932 | 0.043561
50     | 0.885870       | 0.864130       | 0.809783       | 0.820652       | 0.847826       | 0.885870       | 0.885870       | 0.857143 | 0.029727
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
4️⃣  SHADOW KRUM SCORE (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A) | Selected | SelIsAtk
--------------------------------------------------------------------------------
1      | 2.184508       | 0.931724       | 1.019077       | 2.456323       | 2.270075       | 0.848375       | 0.848375       | 5        | 1       
2      | 1.288623       | 0.605912       | 0.809440       | 1.417320       | 1.345907       | 0.550280       | 0.550280       | 5        | 1       
3      | 1.014705       | 0.425802       | 0.505683       | 1.058199       | 1.016121       | 0.332236       | 0.332236       | 5        | 1       
4      | 0.703833       | 0.336292       | 0.365413       | 0.808883       | 0.809631       | 0.222397       | 0.222397       | 5        | 1       
5      | 0.676074       | 0.310843       | 0.328953       | 0.742761       | 0.715778       | 0.193683       | 0.193683       | 5        | 1       
6      | 0.655433       | 0.296330       | 0.307016       | 0.640505       | 0.631644       | 0.178631       | 0.178631       | 5        | 1       
7      | 0.581261       | 0.274788       | 0.293797       | 0.666942       | 0.587458       | 0.167118       | 0.167118       | 5        | 1       
8      | 0.526360       | 0.274086       | 0.293744       | 0.649673       | 0.652371       | 0.164520       | 0.164520       | 5        | 1       
9      | 0.572358       | 0.281374       | 0.302016       | 0.650648       | 0.648775       | 0.168031       | 0.168031       | 5        | 1       
10     | 0.541796       | 0.271844       | 0.289956       | 0.636775       | 0.602493       | 0.159750       | 0.159750       | 5        | 1       
11     | 0.568345       | 0.294657       | 0.319746       | 0.618543       | 0.568990       | 0.168677       | 0.168677       | 5        | 1       
12     | 0.489839       | 0.269086       | 0.292302       | 0.601013       | 0.551053       | 0.153861       | 0.153861       | 5        | 1       
13     | 0.499881       | 0.261718       | 0.283835       | 0.563508       | 0.554436       | 0.151913       | 0.151913       | 5        | 1       
14     | 0.519948       | 0.265080       | 0.282703       | 0.539103       | 0.526848       | 0.150099       | 0.150099       | 5        | 1       
15     | 0.507486       | 0.258672       | 0.274037       | 0.562336       | 0.470246       | 0.147165       | 0.147165       | 5        | 1       
16     | 0.490013       | 0.265137       | 0.275102       | 0.551064       | 0.522142       | 0.149275       | 0.149275       | 5        | 1       
17     | 0.474981       | 0.259788       | 0.269414       | 0.514510       | 0.484210       | 0.143241       | 0.143241       | 5        | 1       
18     | 0.496672       | 0.263673       | 0.277108       | 0.525367       | 0.499111       | 0.148762       | 0.148762       | 5        | 1       
19     | 0.449825       | 0.259890       | 0.276963       | 0.495158       | 0.500078       | 0.144501       | 0.144501       | 5        | 1       
20     | 0.471425       | 0.242927       | 0.256536       | 0.464214       | 0.487230       | 0.136379       | 0.136379       | 5        | 1       
21     | 0.458566       | 0.237236       | 0.249789       | 0.453151       | 0.468377       | 0.135072       | 0.135072       | 5        | 1       
22     | 0.422685       | 0.239458       | 0.248279       | 0.469763       | 0.450589       | 0.132338       | 0.132338       | 5        | 1       
23     | 0.434951       | 0.234268       | 0.252453       | 0.440780       | 0.431426       | 0.132405       | 0.132405       | 5        | 1       
24     | 0.400435       | 0.233284       | 0.238893       | 0.411778       | 0.443667       | 0.127571       | 0.127571       | 5        | 1       
25     | 0.399229       | 0.245981       | 0.256989       | 0.400290       | 0.408299       | 0.130730       | 0.130730       | 5        | 1       
26     | 0.394964       | 0.241423       | 0.253267       | 0.440536       | 0.395459       | 0.130580       | 0.130580       | 5        | 1       
27     | 0.387698       | 0.225092       | 0.237052       | 0.406541       | 0.389583       | 0.123060       | 0.123060       | 5        | 1       
28     | 0.387837       | 0.233835       | 0.240812       | 0.414983       | 0.408798       | 0.125248       | 0.125248       | 5        | 1       
29     | 0.361694       | 0.234892       | 0.249686       | 0.410680       | 0.375935       | 0.124651       | 0.124651       | 5        | 1       
30     | 0.380321       | 0.226806       | 0.234005       | 0.346986       | 0.425639       | 0.121115       | 0.121115       | 5        | 1       
31     | 0.378337       | 0.238177       | 0.254529       | 0.416289       | 0.396221       | 0.129008       | 0.129008       | 5        | 1       
32     | 0.363114       | 0.224523       | 0.233974       | 0.375446       | 0.393824       | 0.120146       | 0.120146       | 5        | 1       
33     | 0.390120       | 0.231717       | 0.242698       | 0.413956       | 0.397454       | 0.127672       | 0.127672       | 5        | 1       
34     | 0.381757       | 0.227178       | 0.236810       | 0.390787       | 0.428064       | 0.122018       | 0.122018       | 5        | 1       
35     | 0.359105       | 0.231983       | 0.241562       | 0.422752       | 0.434129       | 0.125207       | 0.125207       | 5        | 1       
36     | 0.402865       | 0.229207       | 0.240102       | 0.389596       | 0.447335       | 0.125772       | 0.125772       | 5        | 1       
37     | 0.349751       | 0.226789       | 0.240357       | 0.399933       | 0.450574       | 0.124553       | 0.124553       | 5        | 1       
38     | 0.372183       | 0.227758       | 0.240872       | 0.453135       | 0.494258       | 0.125973       | 0.125973       | 5        | 1       
39     | 0.364413       | 0.223025       | 0.238224       | 0.410542       | 0.382180       | 0.122188       | 0.122188       | 5        | 1       
40     | 0.383425       | 0.230756       | 0.234374       | 0.429311       | 0.405474       | 0.123340       | 0.123340       | 5        | 1       
41     | 0.365976       | 0.225565       | 0.233777       | 0.362363       | 0.395266       | 0.121159       | 0.121159       | 5        | 1       
42     | 0.367654       | 0.224679       | 0.228350       | 0.421262       | 0.423238       | 0.122047       | 0.122047       | 5        | 1       
43     | 0.374812       | 0.219880       | 0.226010       | 0.386251       | 0.436000       | 0.120036       | 0.120036       | 5        | 1       
44     | 0.375629       | 0.224189       | 0.229158       | 0.382475       | 0.407567       | 0.120802       | 0.120802       | 5        | 1       
45     | 0.411999       | 0.227046       | 0.237284       | 0.435935       | 0.420220       | 0.125624       | 0.125624       | 5        | 1       
46     | 0.373422       | 0.231887       | 0.236641       | 0.466240       | 0.433059       | 0.126875       | 0.126875       | 5        | 1       
47     | 0.417316       | 0.238617       | 0.243314       | 0.359477       | 0.406250       | 0.127328       | 0.127328       | 5        | 1       
48     | 0.406665       | 0.247615       | 0.257220       | 0.384349       | 0.545942       | 0.135240       | 0.135240       | 5        | 1       
49     | 0.368952       | 0.229449       | 0.237741       | 0.563266       | 0.422356       | 0.128724       | 0.128724       | 5        | 1       
50     | 0.407795       | 0.229866       | 0.239314       | 0.385570       | 0.396566       | 0.123305       | 0.123305       | 5        | 1       
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
20     | 1              | 0              | 0              | 0              | 1              | 0              | 0             
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
33     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
34     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
35     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
36     | 1              | 0              | 0              | 0              | 1              | 0              | 0             
37     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
38     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
39     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
40     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
41     | 1              | 0              | 0              | 0              | 1              | 0              | 0             
42     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
43     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
44     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
45     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
46     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
47     | 1              | 0              | 0              | 0              | 1              | 0              | 0             
48     | 1              | 0              | 0              | 0              | 1              | 0              | 0             
49     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
50     | 1              | 0              | 0              | 0              | 1              | 0              | 0             
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
4c. SHADOW TRIMMED-MEAN TRIM FRACTION (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A)
--------------------------------------------------------------------------------
1      | 0.806651       | 0.724999       | 0.732848       | 0.864952       | 0.727239       | 0.045257       | 0.098054      
2      | 0.799816       | 0.727909       | 0.786033       | 0.814082       | 0.733449       | 0.036509       | 0.102202      
3      | 0.799211       | 0.709514       | 0.748941       | 0.797702       | 0.786916       | 0.044698       | 0.113019      
4      | 0.791988       | 0.696141       | 0.725959       | 0.810024       | 0.807241       | 0.049460       | 0.119187      
5      | 0.805135       | 0.686328       | 0.717455       | 0.813563       | 0.801389       | 0.047935       | 0.128196      
6      | 0.809357       | 0.697090       | 0.718158       | 0.806412       | 0.795454       | 0.044429       | 0.129100      
7      | 0.800402       | 0.681440       | 0.719760       | 0.824799       | 0.797537       | 0.043696       | 0.132366      
8      | 0.784063       | 0.679005       | 0.724077       | 0.824152       | 0.810178       | 0.051893       | 0.126632      
9      | 0.793321       | 0.679687       | 0.719784       | 0.819438       | 0.809735       | 0.049492       | 0.128544      
10     | 0.795139       | 0.683181       | 0.719163       | 0.821769       | 0.803055       | 0.047290       | 0.130403      
11     | 0.794535       | 0.693020       | 0.727830       | 0.819328       | 0.791054       | 0.042037       | 0.132196      
12     | 0.786411       | 0.679527       | 0.729528       | 0.827262       | 0.799699       | 0.044294       | 0.133279      
13     | 0.790083       | 0.684026       | 0.729072       | 0.816411       | 0.803724       | 0.046010       | 0.130674      
14     | 0.800223       | 0.695490       | 0.724287       | 0.812127       | 0.793204       | 0.043340       | 0.131329      
15     | 0.799294       | 0.694468       | 0.725754       | 0.820153       | 0.785732       | 0.039162       | 0.135437      
16     | 0.792969       | 0.697938       | 0.724006       | 0.815067       | 0.796998       | 0.044683       | 0.128339      
17     | 0.792537       | 0.700727       | 0.724483       | 0.813009       | 0.797092       | 0.042732       | 0.129421      
18     | 0.793995       | 0.704527       | 0.726941       | 0.809479       | 0.793598       | 0.042376       | 0.129084      
19     | 0.786132       | 0.699876       | 0.733769       | 0.809365       | 0.798570       | 0.044482       | 0.127806      
20     | 0.799439       | 0.695356       | 0.725534       | 0.806901       | 0.799942       | 0.045785       | 0.127043      
21     | 0.795797       | 0.702037       | 0.730338       | 0.802542       | 0.798351       | 0.044982       | 0.125954      
22     | 0.788885       | 0.705863       | 0.729440       | 0.812913       | 0.793296       | 0.042391       | 0.127213      
23     | 0.792936       | 0.697916       | 0.740036       | 0.808219       | 0.790311       | 0.041834       | 0.128748      
24     | 0.788219       | 0.713114       | 0.731308       | 0.801731       | 0.801329       | 0.045096       | 0.119203      
25     | 0.787174       | 0.713236       | 0.742314       | 0.796941       | 0.794216       | 0.041835       | 0.124284      
26     | 0.783807       | 0.714484       | 0.743224       | 0.816360       | 0.779005       | 0.036199       | 0.126922      
27     | 0.790600       | 0.703493       | 0.738192       | 0.818084       | 0.787426       | 0.039056       | 0.123149      
28     | 0.791684       | 0.713210       | 0.734668       | 0.808576       | 0.786384       | 0.040334       | 0.125144      
29     | 0.785424       | 0.711535       | 0.748091       | 0.810783       | 0.782492       | 0.037127       | 0.124547      
30     | 0.789462       | 0.711609       | 0.739255       | 0.795526       | 0.803133       | 0.046278       | 0.114739      
31     | 0.786494       | 0.705498       | 0.749273       | 0.812622       | 0.786139       | 0.037602       | 0.122372      
32     | 0.788544       | 0.713833       | 0.737978       | 0.807232       | 0.791604       | 0.042965       | 0.117845      
33     | 0.789180       | 0.715839       | 0.745130       | 0.808339       | 0.782127       | 0.037857       | 0.121528      
34     | 0.790938       | 0.703206       | 0.735400       | 0.805673       | 0.802117       | 0.045620       | 0.117046      
35     | 0.779565       | 0.709064       | 0.736416       | 0.812970       | 0.799831       | 0.043839       | 0.118316      
36     | 0.795683       | 0.705211       | 0.730594       | 0.814514       | 0.797093       | 0.043714       | 0.113191      
37     | 0.787224       | 0.709756       | 0.739882       | 0.801007       | 0.804234       | 0.045882       | 0.112015      
38     | 0.778547       | 0.691061       | 0.728643       | 0.818998       | 0.814356       | 0.049879       | 0.118517      
39     | 0.794147       | 0.707535       | 0.741738       | 0.811226       | 0.782853       | 0.038562       | 0.123939      
40     | 0.791440       | 0.708802       | 0.727705       | 0.813035       | 0.799448       | 0.040192       | 0.119378      
41     | 0.802498       | 0.712905       | 0.745045       | 0.797452       | 0.783930       | 0.040935       | 0.117235      
42     | 0.789719       | 0.713381       | 0.728233       | 0.821140       | 0.788988       | 0.040590       | 0.117950      
43     | 0.789015       | 0.708522       | 0.730461       | 0.809463       | 0.806031       | 0.045121       | 0.111386      
44     | 0.785187       | 0.712439       | 0.731786       | 0.815372       | 0.802856       | 0.040253       | 0.112107      
45     | 0.810191       | 0.702546       | 0.726777       | 0.824010       | 0.781456       | 0.036875       | 0.118143      
46     | 0.781322       | 0.710561       | 0.728579       | 0.816408       | 0.798854       | 0.042503       | 0.121772      
47     | 0.795598       | 0.721979       | 0.738771       | 0.807314       | 0.785026       | 0.037567       | 0.113745      
48     | 0.789961       | 0.714701       | 0.735160       | 0.784783       | 0.818146       | 0.052714       | 0.104534      
49     | 0.786321       | 0.696564       | 0.727101       | 0.829791       | 0.793926       | 0.038637       | 0.127660      
50     | 0.801046       | 0.719266       | 0.738576       | 0.800708       | 0.782588       | 0.038129       | 0.119686      
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
4d. SHADOW MEDIAN PROVIDER FRACTION (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A)
--------------------------------------------------------------------------------
1      | 0.024745       | 0.036342       | 0.036166       | 0.025066       | 0.020992       | 0.198299       | 0.658390      
2      | 0.025337       | 0.035718       | 0.030787       | 0.022378       | 0.024491       | 0.180043       | 0.681245      
3      | 0.028111       | 0.041208       | 0.035521       | 0.026257       | 0.026619       | 0.148236       | 0.694048      
4      | 0.031218       | 0.043416       | 0.039922       | 0.027027       | 0.027065       | 0.136131       | 0.695222      
5      | 0.031408       | 0.045759       | 0.041486       | 0.028239       | 0.029240       | 0.135675       | 0.688194      
6      | 0.029299       | 0.043965       | 0.040972       | 0.029383       | 0.029910       | 0.137649       | 0.688823      
7      | 0.031240       | 0.045780       | 0.041390       | 0.027264       | 0.030389       | 0.138111       | 0.685827      
8      | 0.034125       | 0.046805       | 0.041415       | 0.027794       | 0.028387       | 0.131958       | 0.689517      
9      | 0.032545       | 0.046492       | 0.041826       | 0.028593       | 0.028580       | 0.133059       | 0.688906      
10     | 0.031941       | 0.046399       | 0.041917       | 0.027559       | 0.029877       | 0.134273       | 0.688034      
11     | 0.030903       | 0.045365       | 0.039500       | 0.027425       | 0.031040       | 0.139039       | 0.686729      
12     | 0.032987       | 0.046319       | 0.040639       | 0.026809       | 0.030820       | 0.135702       | 0.686725      
13     | 0.031367       | 0.047262       | 0.040077       | 0.028120       | 0.029857       | 0.134190       | 0.689127      
14     | 0.029657       | 0.044551       | 0.040651       | 0.028699       | 0.031112       | 0.136307       | 0.689024      
15     | 0.030241       | 0.044665       | 0.040248       | 0.027069       | 0.032376       | 0.141684       | 0.683717      
16     | 0.031184       | 0.043805       | 0.040241       | 0.027701       | 0.030091       | 0.135717       | 0.691261      
17     | 0.031188       | 0.043562       | 0.039110       | 0.028095       | 0.030196       | 0.137034       | 0.690814      
18     | 0.030825       | 0.042353       | 0.039079       | 0.028661       | 0.030542       | 0.137712       | 0.690827      
19     | 0.032287       | 0.043074       | 0.038551       | 0.028497       | 0.029879       | 0.135156       | 0.692557      
20     | 0.030478       | 0.043460       | 0.040113       | 0.029538       | 0.029239       | 0.135715       | 0.691457      
21     | 0.030361       | 0.042590       | 0.039304       | 0.029677       | 0.029004       | 0.136886       | 0.692179      
22     | 0.030526       | 0.041994       | 0.039146       | 0.027658       | 0.030279       | 0.137428       | 0.692969      
23     | 0.030367       | 0.044280       | 0.037250       | 0.028205       | 0.030479       | 0.138997       | 0.690421      
24     | 0.030196       | 0.040233       | 0.037296       | 0.028958       | 0.027617       | 0.137226       | 0.698475      
25     | 0.030319       | 0.040444       | 0.036654       | 0.029461       | 0.029241       | 0.139058       | 0.694823      
26     | 0.030022       | 0.039705       | 0.035742       | 0.026331       | 0.031321       | 0.141658       | 0.695221      
27     | 0.029667       | 0.040414       | 0.036518       | 0.026076       | 0.029530       | 0.142091       | 0.695703      
28     | 0.030305       | 0.040451       | 0.037169       | 0.027643       | 0.029910       | 0.140349       | 0.694172      
29     | 0.029845       | 0.040208       | 0.035305       | 0.026452       | 0.029865       | 0.143341       | 0.694984      
30     | 0.029248       | 0.039311       | 0.036789       | 0.029687       | 0.025982       | 0.137413       | 0.701570      
31     | 0.029420       | 0.040072       | 0.034414       | 0.026816       | 0.029253       | 0.141453       | 0.698573      
32     | 0.029439       | 0.039941       | 0.036298       | 0.027336       | 0.027795       | 0.139394       | 0.699797      
33     | 0.029323       | 0.038607       | 0.035387       | 0.027019       | 0.029049       | 0.143746       | 0.696869      
34     | 0.029729       | 0.040626       | 0.037459       | 0.028134       | 0.026719       | 0.134114       | 0.703220      
35     | 0.031246       | 0.040187       | 0.037011       | 0.025977       | 0.027734       | 0.137779       | 0.700067      
36     | 0.028364       | 0.038933       | 0.036955       | 0.026538       | 0.026115       | 0.141697       | 0.701398      
37     | 0.029821       | 0.039206       | 0.036180       | 0.027229       | 0.025460       | 0.137762       | 0.704341      
38     | 0.032428       | 0.043979       | 0.039460       | 0.026501       | 0.026028       | 0.132306       | 0.699299      
39     | 0.029313       | 0.040638       | 0.036435       | 0.026485       | 0.029631       | 0.141000       | 0.696499      
40     | 0.029045       | 0.038992       | 0.037986       | 0.026366       | 0.027181       | 0.140757       | 0.699673      
41     | 0.028033       | 0.038258       | 0.035006       | 0.028634       | 0.028238       | 0.141476       | 0.700355      
42     | 0.029641       | 0.039173       | 0.037483       | 0.024462       | 0.027781       | 0.143631       | 0.697830      
43     | 0.029574       | 0.039126       | 0.036204       | 0.026496       | 0.025107       | 0.139789       | 0.703704      
44     | 0.028381       | 0.037468       | 0.035917       | 0.024800       | 0.025795       | 0.141948       | 0.705692      
45     | 0.026104       | 0.039394       | 0.037139       | 0.023862       | 0.028519       | 0.145968       | 0.699013      
46     | 0.032024       | 0.040273       | 0.037794       | 0.026110       | 0.028074       | 0.140436       | 0.695289      
47     | 0.026836       | 0.036146       | 0.034576       | 0.026815       | 0.026938       | 0.146662       | 0.702026      
48     | 0.028913       | 0.038045       | 0.036163       | 0.030970       | 0.023157       | 0.132088       | 0.710664      
49     | 0.033020       | 0.042217       | 0.037869       | 0.023637       | 0.029555       | 0.145114       | 0.688589      
50     | 0.027189       | 0.038166       | 0.036020       | 0.027923       | 0.028518       | 0.142218       | 0.699967      
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
4e. SHADOW DISTANCE TO COORDINATE MEDIAN (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A)
--------------------------------------------------------------------------------
1      | 0.802971       | 0.626460       | 0.660390       | 0.883313       | 0.790884       | 0.062792       | 0.062792      
2      | 0.585321       | 0.474936       | 0.571752       | 0.642030       | 0.565322       | 0.048019       | 0.048019      
3      | 0.494028       | 0.375456       | 0.424716       | 0.521085       | 0.504037       | 0.044370       | 0.044370      
4      | 0.420827       | 0.315501       | 0.337370       | 0.467654       | 0.463342       | 0.041059       | 0.041059      
5      | 0.419009       | 0.296709       | 0.311045       | 0.451984       | 0.439985       | 0.040861       | 0.040861      
6      | 0.415118       | 0.287707       | 0.296404       | 0.418549       | 0.412418       | 0.038867       | 0.038867      
7      | 0.392347       | 0.274098       | 0.290408       | 0.428606       | 0.399617       | 0.038156       | 0.038156      
8      | 0.374415       | 0.271149       | 0.288053       | 0.422899       | 0.422601       | 0.039100       | 0.039100      
9      | 0.390644       | 0.273810       | 0.291487       | 0.426133       | 0.421369       | 0.039176       | 0.039176      
10     | 0.380093       | 0.267685       | 0.283515       | 0.421578       | 0.405509       | 0.038333       | 0.038333      
11     | 0.388086       | 0.273351       | 0.294991       | 0.414951       | 0.389539       | 0.037355       | 0.037355      
12     | 0.360741       | 0.260545       | 0.281461       | 0.410859       | 0.387249       | 0.036248       | 0.036248      
13     | 0.365782       | 0.259277       | 0.279415       | 0.395752       | 0.386857       | 0.035987       | 0.035987      
14     | 0.373680       | 0.259825       | 0.276074       | 0.386006       | 0.377365       | 0.035316       | 0.035316      
15     | 0.367621       | 0.258361       | 0.272398       | 0.393288       | 0.355400       | 0.034896       | 0.034896      
16     | 0.359100       | 0.262937       | 0.271842       | 0.389242       | 0.377835       | 0.034928       | 0.034928      
17     | 0.353957       | 0.257736       | 0.266488       | 0.376255       | 0.361238       | 0.033875       | 0.033875      
18     | 0.363057       | 0.260903       | 0.273319       | 0.376890       | 0.366816       | 0.034172       | 0.034172      
19     | 0.345091       | 0.255483       | 0.271433       | 0.366812       | 0.366166       | 0.033577       | 0.033577      
20     | 0.353022       | 0.249196       | 0.262106       | 0.356059       | 0.363185       | 0.033035       | 0.033035      
21     | 0.348095       | 0.248451       | 0.260580       | 0.349725       | 0.354615       | 0.032516       | 0.032516      
22     | 0.334395       | 0.247958       | 0.256438       | 0.355974       | 0.346970       | 0.032015       | 0.032015      
23     | 0.337170       | 0.243539       | 0.261148       | 0.346330       | 0.336844       | 0.031330       | 0.031330      
24     | 0.322643       | 0.245403       | 0.250804       | 0.330210       | 0.342428       | 0.029866       | 0.029866      
25     | 0.320679       | 0.246214       | 0.257044       | 0.327470       | 0.329867       | 0.029728       | 0.029728      
26     | 0.320274       | 0.245696       | 0.257334       | 0.342842       | 0.319859       | 0.029063       | 0.029063      
27     | 0.318295       | 0.238021       | 0.250004       | 0.329869       | 0.320559       | 0.028540       | 0.028540      
28     | 0.318172       | 0.242524       | 0.249554       | 0.334904       | 0.327320       | 0.029522       | 0.029522      
29     | 0.305684       | 0.238416       | 0.253373       | 0.332875       | 0.313382       | 0.028193       | 0.028193      
30     | 0.314698       | 0.238558       | 0.245816       | 0.302894       | 0.337474       | 0.028146       | 0.028146      
31     | 0.312676       | 0.242177       | 0.258290       | 0.333502       | 0.320016       | 0.028412       | 0.028412      
32     | 0.304317       | 0.236628       | 0.246382       | 0.315107       | 0.321891       | 0.027740       | 0.027740      
33     | 0.315322       | 0.243378       | 0.254068       | 0.330860       | 0.321263       | 0.028331       | 0.028331      
34     | 0.315450       | 0.238087       | 0.247886       | 0.323666       | 0.339122       | 0.028511       | 0.028511      
35     | 0.303235       | 0.241224       | 0.251014       | 0.339190       | 0.340408       | 0.029042       | 0.029042      
36     | 0.324652       | 0.241289       | 0.252235       | 0.319251       | 0.346144       | 0.028976       | 0.028976      
37     | 0.298525       | 0.238784       | 0.252474       | 0.326941       | 0.346163       | 0.028261       | 0.028261      
38     | 0.311804       | 0.239556       | 0.252778       | 0.352837       | 0.366455       | 0.030935       | 0.030935      
39     | 0.307302       | 0.235504       | 0.251202       | 0.331060       | 0.316071       | 0.027976       | 0.027976      
40     | 0.316249       | 0.242598       | 0.246159       | 0.340179       | 0.329330       | 0.028485       | 0.028485      
41     | 0.305275       | 0.238483       | 0.246726       | 0.307993       | 0.322089       | 0.027293       | 0.027293      
42     | 0.309452       | 0.241411       | 0.245040       | 0.335697       | 0.334843       | 0.028120       | 0.028120      
43     | 0.311832       | 0.238034       | 0.244093       | 0.320804       | 0.341544       | 0.028141       | 0.028141      
44     | 0.311755       | 0.239844       | 0.244779       | 0.317624       | 0.328270       | 0.027150       | 0.027150      
45     | 0.327599       | 0.241528       | 0.252072       | 0.342747       | 0.333239       | 0.028308       | 0.028308      
46     | 0.309904       | 0.245002       | 0.249831       | 0.352804       | 0.338345       | 0.030063       | 0.030063      
47     | 0.327975       | 0.246685       | 0.251416       | 0.303137       | 0.326136       | 0.027124       | 0.027124      
48     | 0.324599       | 0.250927       | 0.260567       | 0.317493       | 0.382691       | 0.030057       | 0.030057      
49     | 0.308042       | 0.244641       | 0.252356       | 0.393948       | 0.334315       | 0.032094       | 0.032094      
50     | 0.326952       | 0.239673       | 0.249487       | 0.318788       | 0.322732       | 0.027849       | 0.027849      
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
4f. UPDATE NORM (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A)
--------------------------------------------------------------------------------
1      | 1.361764       | 0.606631       | 0.560976       | 1.518111       | 1.264700       | 0.883457       | 0.883457      
2      | 1.091374       | 0.456474       | 0.444832       | 1.121806       | 1.015485       | 0.700432       | 0.700432      
3      | 0.797187       | 0.343377       | 0.389968       | 0.788796       | 0.790543       | 0.487816       | 0.487816      
4      | 0.603022       | 0.313136       | 0.337406       | 0.618022       | 0.645800       | 0.359636       | 0.359636      
5      | 0.551211       | 0.282117       | 0.308799       | 0.552944       | 0.567312       | 0.295336       | 0.295336      
6      | 0.514162       | 0.263286       | 0.296725       | 0.496099       | 0.513919       | 0.254237       | 0.254237      
7      | 0.463592       | 0.265800       | 0.278044       | 0.499538       | 0.480436       | 0.229000       | 0.229000      
8      | 0.428943       | 0.260282       | 0.269350       | 0.490549       | 0.498908       | 0.216824       | 0.216824      
9      | 0.451479       | 0.267130       | 0.277108       | 0.490293       | 0.500580       | 0.222939       | 0.222939      
10     | 0.433835       | 0.261136       | 0.262002       | 0.487770       | 0.475989       | 0.211839       | 0.211839      
11     | 0.445382       | 0.269372       | 0.269707       | 0.471219       | 0.455817       | 0.205244       | 0.205244      
12     | 0.402023       | 0.255221       | 0.261483       | 0.465900       | 0.452643       | 0.194720       | 0.194720      
13     | 0.415517       | 0.252444       | 0.261641       | 0.445034       | 0.450793       | 0.193899       | 0.193899      
14     | 0.421650       | 0.258474       | 0.263441       | 0.430674       | 0.433328       | 0.189118       | 0.189118      
15     | 0.414647       | 0.255707       | 0.255188       | 0.444097       | 0.406159       | 0.185328       | 0.185328      
16     | 0.406120       | 0.258584       | 0.257160       | 0.435622       | 0.431928       | 0.186187       | 0.186187      
17     | 0.398392       | 0.260254       | 0.256499       | 0.415696       | 0.412376       | 0.180095       | 0.180095      
18     | 0.415528       | 0.262547       | 0.253551       | 0.417644       | 0.413286       | 0.181034       | 0.181034      
19     | 0.386919       | 0.255716       | 0.262829       | 0.400868       | 0.411824       | 0.172541       | 0.172541      
20     | 0.400221       | 0.248239       | 0.253634       | 0.380045       | 0.406028       | 0.167779       | 0.167779      
21     | 0.387237       | 0.251315       | 0.254182       | 0.381355       | 0.397396       | 0.167267       | 0.167267      
22     | 0.371051       | 0.245628       | 0.252349       | 0.385050       | 0.392274       | 0.163624       | 0.163624      
23     | 0.374431       | 0.242663       | 0.258014       | 0.373368       | 0.376839       | 0.159521       | 0.159521      
24     | 0.351754       | 0.252748       | 0.251172       | 0.351709       | 0.382886       | 0.154976       | 0.154976      
25     | 0.360498       | 0.255429       | 0.254976       | 0.351271       | 0.364720       | 0.156593       | 0.156593      
26     | 0.352675       | 0.254643       | 0.254859       | 0.371203       | 0.358582       | 0.157214       | 0.157214      
27     | 0.356829       | 0.239063       | 0.252763       | 0.353702       | 0.355882       | 0.153649       | 0.153649      
28     | 0.354515       | 0.249544       | 0.253737       | 0.357009       | 0.365174       | 0.156557       | 0.156557      
29     | 0.335702       | 0.243218       | 0.255319       | 0.359721       | 0.349098       | 0.150889       | 0.150889      
30     | 0.341978       | 0.246791       | 0.249078       | 0.321612       | 0.378112       | 0.150528       | 0.150528      
31     | 0.341704       | 0.249864       | 0.259815       | 0.361935       | 0.352023       | 0.151938       | 0.151938      
32     | 0.342180       | 0.240175       | 0.248929       | 0.341691       | 0.356110       | 0.152282       | 0.152282      
33     | 0.347377       | 0.245355       | 0.251176       | 0.361998       | 0.357950       | 0.153250       | 0.153250      
34     | 0.347892       | 0.243753       | 0.252275       | 0.349767       | 0.375037       | 0.155169       | 0.155169      
35     | 0.328335       | 0.247130       | 0.253913       | 0.365549       | 0.384197       | 0.156219       | 0.156219      
36     | 0.353882       | 0.246705       | 0.254377       | 0.340330       | 0.389510       | 0.155819       | 0.155819      
37     | 0.320529       | 0.243812       | 0.258532       | 0.356701       | 0.387901       | 0.155361       | 0.155361      
38     | 0.341189       | 0.239408       | 0.247136       | 0.380658       | 0.412000       | 0.159495       | 0.159495      
39     | 0.341253       | 0.241519       | 0.254275       | 0.364136       | 0.349882       | 0.155528       | 0.155528      
40     | 0.347237       | 0.243317       | 0.247119       | 0.374046       | 0.373645       | 0.160093       | 0.160093      
41     | 0.336531       | 0.245874       | 0.251968       | 0.326615       | 0.365157       | 0.151746       | 0.151746      
42     | 0.339203       | 0.244873       | 0.245954       | 0.361422       | 0.379286       | 0.156111       | 0.156111      
43     | 0.346987       | 0.242400       | 0.246985       | 0.348449       | 0.382880       | 0.158210       | 0.158210      
44     | 0.345032       | 0.245268       | 0.249430       | 0.339767       | 0.367727       | 0.153459       | 0.153459      
45     | 0.364013       | 0.247056       | 0.252741       | 0.375481       | 0.373629       | 0.163324       | 0.163324      
46     | 0.344072       | 0.248819       | 0.246710       | 0.387972       | 0.376291       | 0.160579       | 0.160579      
47     | 0.367236       | 0.250520       | 0.250683       | 0.322225       | 0.366163       | 0.153776       | 0.153776      
48     | 0.356317       | 0.251913       | 0.259547       | 0.344009       | 0.433281       | 0.165066       | 0.165066      
49     | 0.333481       | 0.246783       | 0.257313       | 0.438017       | 0.375121       | 0.168220       | 0.168220      
50     | 0.371051       | 0.247981       | 0.251748       | 0.346542       | 0.359060       | 0.160829       | 0.160829      
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
4g. PAIRWISE SQUARED DISTANCE (Per Round, Upper Triangle)
--------------------------------------------------------------------------------
Round | d(0,1) | d(0,2) | d(0,3) | d(0,4) | d(0,5) | d(0,6) | d(1,2) | d(1,3) | d(1,4) | d(1,5) | d(1,6) | d(2,3) | d(2,4) | d(2,5) | d(2,6) | d(3,4) | d(3,5) | d(3,6) | d(4,5) | d(4,6) | d(5,6)
--------------------------------------------------------------------------------
1      | 1.554941       | 1.543046       | 0.901672       | 1.749678       | 0.641418       | 0.641418       | 0.127025       | 1.842158       | 1.025643       | 0.402350       | 0.402350       | 1.956156       | 1.144003       | 0.446026       | 0.446026       | 1.731028       | 0.777326       | 0.777326       | 0.622216       | 0.622216       | 0.000000      
2      | 0.840703       | 0.994576       | 0.603934       | 0.709290       | 0.342345       | 0.342345       | 0.142419       | 0.902372       | 0.708841       | 0.231747       | 0.231747       | 1.159920       | 0.806280       | 0.333511       | 0.333511       | 0.803400       | 0.406693       | 0.406693       | 0.318533       | 0.318533       | 0.000000      
3      | 0.526831       | 0.569189       | 0.529324       | 0.559179       | 0.243937       | 0.243937       | 0.133507       | 0.522059       | 0.512019       | 0.146148       | 0.146148       | 0.645688       | 0.545673       | 0.186088       | 0.186088       | 0.607391       | 0.268070       | 0.268070       | 0.252051       | 0.252051       | 0.000000      
4      | 0.347969       | 0.357855       | 0.439784       | 0.473545       | 0.177932       | 0.177932       | 0.128455       | 0.377465       | 0.393998       | 0.103918       | 0.103918       | 0.449853       | 0.384539       | 0.118479       | 0.118479       | 0.539584       | 0.215709       | 0.215709       | 0.212546       | 0.212546       | 0.000000      
5      | 0.324449       | 0.329472       | 0.442653       | 0.453516       | 0.175812       | 0.175812       | 0.126215       | 0.340198       | 0.341361       | 0.092314       | 0.092314       | 0.389912       | 0.331540       | 0.101369       | 0.101369       | 0.505099       | 0.201281       | 0.201281       | 0.192119       | 0.192119       | 0.000000      
6      | 0.320472       | 0.312834       | 0.408069       | 0.423790       | 0.171299       | 0.171299       | 0.123042       | 0.294128       | 0.304385       | 0.086644       | 0.086644       | 0.339535       | 0.293154       | 0.091987       | 0.091987       | 0.433612       | 0.173188       | 0.173188       | 0.169245       | 0.169245       | 0.000000      
7      | 0.273777       | 0.282026       | 0.393023       | 0.400847       | 0.153742       | 0.153742       | 0.117174       | 0.305953       | 0.278324       | 0.078807       | 0.078807       | 0.354587       | 0.268581       | 0.088311       | 0.088311       | 0.430399       | 0.180495       | 0.180495       | 0.159438       | 0.159438       | 0.000000      
8      | 0.243888       | 0.252989       | 0.376244       | 0.411867       | 0.141236       | 0.141236       | 0.119395       | 0.297396       | 0.304718       | 0.077345       | 0.077345       | 0.342245       | 0.299782       | 0.087174       | 0.087174       | 0.443932       | 0.176138       | 0.176138       | 0.176294       | 0.176294       | 0.000000      
9      | 0.266432       | 0.270340       | 0.398931       | 0.423123       | 0.152963       | 0.152963       | 0.123665       | 0.292854       | 0.305931       | 0.078855       | 0.078855       | 0.349135       | 0.296818       | 0.089176       | 0.089176       | 0.448296       | 0.178897       | 0.178897       | 0.175978       | 0.175978       | 0.000000      
10     | 0.252208       | 0.251937       | 0.389350       | 0.395714       | 0.144930       | 0.144930       | 0.121150       | 0.286808       | 0.281695       | 0.075347       | 0.075347       | 0.337304       | 0.276498       | 0.084403       | 0.084403       | 0.426834       | 0.174983       | 0.174983       | 0.162997       | 0.162997       | 0.000000      
11     | 0.269155       | 0.267631       | 0.391159       | 0.386123       | 0.150357       | 0.150357       | 0.138524       | 0.278859       | 0.266487       | 0.078066       | 0.078066       | 0.342386       | 0.267007       | 0.090611       | 0.090611       | 0.400268       | 0.169842       | 0.169842       | 0.151252       | 0.151252       | 0.000000      
12     | 0.228372       | 0.232982       | 0.359421       | 0.359380       | 0.130733       | 0.130733       | 0.126833       | 0.268887       | 0.259186       | 0.071126       | 0.071126       | 0.328278       | 0.252925       | 0.082734       | 0.082734       | 0.401485       | 0.166063       | 0.166063       | 0.149064       | 0.149064       | 0.000000      
13     | 0.231708       | 0.241899       | 0.351974       | 0.362286       | 0.134086       | 0.134086       | 0.120863       | 0.254692       | 0.263046       | 0.070427       | 0.070427       | 0.305289       | 0.257259       | 0.081486       | 0.081486       | 0.378344       | 0.154408       | 0.154408       | 0.148588       | 0.148588       | 0.000000      
14     | 0.241724       | 0.250617       | 0.352668       | 0.358767       | 0.139112       | 0.139112       | 0.123792       | 0.244200       | 0.252027       | 0.070644       | 0.070644       | 0.287279       | 0.243618       | 0.079455       | 0.079455       | 0.362306       | 0.147452       | 0.147452       | 0.141615       | 0.141615       | 0.000000      
15     | 0.238200       | 0.246034       | 0.349002       | 0.331858       | 0.134643       | 0.134643       | 0.119190       | 0.258075       | 0.226153       | 0.069741       | 0.069741       | 0.297313       | 0.217236       | 0.077424       | 0.077424       | 0.350142       | 0.152131       | 0.152131       | 0.126505       | 0.126505       | 0.000000      
16     | 0.231707       | 0.236989       | 0.335461       | 0.342174       | 0.129153       | 0.129153       | 0.120845       | 0.252050       | 0.256891       | 0.072146       | 0.072146       | 0.289749       | 0.238647       | 0.077129       | 0.077129       | 0.372101       | 0.149507       | 0.149507       | 0.141748       | 0.141748       | 0.000000      
17     | 0.224697       | 0.225864       | 0.326042       | 0.322007       | 0.125142       | 0.125142       | 0.121360       | 0.235318       | 0.237585       | 0.069214       | 0.069214       | 0.271494       | 0.224275       | 0.074027       | 0.074027       | 0.338864       | 0.139596       | 0.139596       | 0.129967       | 0.129967       | 0.000000      
18     | 0.234081       | 0.248610       | 0.325128       | 0.336242       | 0.131296       | 0.131296       | 0.121629       | 0.244346       | 0.242180       | 0.071022       | 0.071022       | 0.274353       | 0.231307       | 0.077740       | 0.077740       | 0.347261       | 0.140511       | 0.140511       | 0.133902       | 0.133902       | 0.000000      
19     | 0.211402       | 0.225485       | 0.304443       | 0.320635       | 0.119212       | 0.119212       | 0.123925       | 0.229053       | 0.241507       | 0.067982       | 0.067982       | 0.264189       | 0.234081       | 0.076519       | 0.076519       | 0.334340       | 0.133053       | 0.133053       | 0.132999       | 0.132999       | 0.000000      
20     | 0.223170       | 0.226604       | 0.299053       | 0.326813       | 0.124127       | 0.124127       | 0.113352       | 0.212390       | 0.229664       | 0.064787       | 0.064787       | 0.246933       | 0.225625       | 0.071592       | 0.071592       | 0.326526       | 0.125912       | 0.125912       | 0.130803       | 0.130803       | 0.000000      
21     | 0.217620       | 0.224394       | 0.288780       | 0.312626       | 0.120473       | 0.120473       | 0.108440       | 0.210110       | 0.226876       | 0.064398       | 0.064398       | 0.242762       | 0.218856       | 0.070674       | 0.070674       | 0.307333       | 0.121520       | 0.121520       | 0.124761       | 0.124761       | 0.000000      
22     | 0.198873       | 0.205425       | 0.291066       | 0.293817       | 0.111906       | 0.111906       | 0.111530       | 0.219289       | 0.220195       | 0.063964       | 0.063964       | 0.243141       | 0.211478       | 0.068374       | 0.068374       | 0.302891       | 0.125237       | 0.125237       | 0.119556       | 0.119556       | 0.000000      
23     | 0.208595       | 0.214815       | 0.280894       | 0.281189       | 0.113178       | 0.113178       | 0.110956       | 0.203139       | 0.205432       | 0.061656       | 0.061656       | 0.239878       | 0.207616       | 0.070749       | 0.070749       | 0.290520       | 0.118821       | 0.118821       | 0.112997       | 0.112997       | 0.000000      
24     | 0.196221       | 0.192389       | 0.254846       | 0.278042       | 0.104023       | 0.104023       | 0.108518       | 0.194931       | 0.212895       | 0.062383       | 0.062383       | 0.214227       | 0.211539       | 0.065188       | 0.065188       | 0.279255       | 0.108423       | 0.108423       | 0.116064       | 0.116064       | 0.000000      
25     | 0.193719       | 0.200618       | 0.247357       | 0.266221       | 0.102755       | 0.102755       | 0.120754       | 0.187348       | 0.204986       | 0.062613       | 0.062613       | 0.220894       | 0.192003       | 0.068117       | 0.068117       | 0.271487       | 0.106471       | 0.106471       | 0.108148       | 0.108148       | 0.000000      
26     | 0.190060       | 0.190788       | 0.268528       | 0.259670       | 0.102452       | 0.102452       | 0.116765       | 0.207944       | 0.193713       | 0.062329       | 0.062329       | 0.239383       | 0.191106       | 0.068251       | 0.068251       | 0.263401       | 0.116296       | 0.116296       | 0.102176       | 0.102176       | 0.000000      
27     | 0.185751       | 0.191969       | 0.251976       | 0.257655       | 0.100973       | 0.100973       | 0.108013       | 0.190340       | 0.190401       | 0.058540       | 0.058540       | 0.219118       | 0.185038       | 0.064520       | 0.064520       | 0.260764       | 0.108100       | 0.108100       | 0.102273       | 0.102273       | 0.000000      
28     | 0.193454       | 0.185394       | 0.261585       | 0.256494       | 0.101221       | 0.101221       | 0.112075       | 0.192661       | 0.196987       | 0.060880       | 0.060880       | 0.218823       | 0.195844       | 0.064368       | 0.064368       | 0.273288       | 0.111161       | 0.111161       | 0.106477       | 0.106477       | 0.000000      
29     | 0.174350       | 0.183733       | 0.245963       | 0.238892       | 0.093672       | 0.093672       | 0.117637       | 0.191613       | 0.183555       | 0.058627       | 0.058627       | 0.223139       | 0.180020       | 0.066024       | 0.066024       | 0.261756       | 0.109533       | 0.109533       | 0.097957       | 0.097957       | 0.000000      
30     | 0.187609       | 0.182817       | 0.224003       | 0.272518       | 0.098752       | 0.098752       | 0.109290       | 0.162884       | 0.206912       | 0.058758       | 0.058758       | 0.191953       | 0.200844       | 0.062357       | 0.062357       | 0.254786       | 0.092051       | 0.092051       | 0.112397       | 0.112397       | 0.000000      
31     | 0.182531       | 0.186702       | 0.254368       | 0.251749       | 0.097903       | 0.097903       | 0.117345       | 0.195932       | 0.192169       | 0.060416       | 0.060416       | 0.229733       | 0.195340       | 0.068592       | 0.068592       | 0.257287       | 0.110179       | 0.110179       | 0.102026       | 0.102026       | 0.000000      
32     | 0.177502       | 0.177816       | 0.227298       | 0.245702       | 0.092806       | 0.092806       | 0.109102       | 0.177713       | 0.188567       | 0.057710       | 0.057710       | 0.200328       | 0.189069       | 0.062436       | 0.062436       | 0.254150       | 0.098866       | 0.098866       | 0.102628       | 0.102628       | 0.000000      
33     | 0.193028       | 0.191663       | 0.245158       | 0.251770       | 0.099229       | 0.099229       | 0.109536       | 0.196763       | 0.191998       | 0.061091       | 0.061091       | 0.224071       | 0.193006       | 0.066581       | 0.066581       | 0.261976       | 0.108596       | 0.108596       | 0.102728       | 0.102728       | 0.000000      
34     | 0.184263       | 0.182435       | 0.242069       | 0.276008       | 0.099661       | 0.099661       | 0.109976       | 0.181922       | 0.203326       | 0.058601       | 0.058601       | 0.210851       | 0.200604       | 0.063417       | 0.063417       | 0.275115       | 0.104432       | 0.104432       | 0.113730       | 0.113730       | 0.000000      
35     | 0.173693       | 0.174052       | 0.250109       | 0.258164       | 0.092706       | 0.092706       | 0.111566       | 0.195025       | 0.213157       | 0.060209       | 0.060209       | 0.226937       | 0.204659       | 0.064998       | 0.064998       | 0.290543       | 0.113864       | 0.113864       | 0.114735       | 0.114735       | 0.000000      
36     | 0.192715       | 0.196808       | 0.250034       | 0.282139       | 0.105075       | 0.105075       | 0.108882       | 0.185006       | 0.210932       | 0.060162       | 0.060162       | 0.198651       | 0.220800       | 0.065610       | 0.065610       | 0.274642       | 0.102295       | 0.102295       | 0.118202       | 0.118202       | 0.000000      
37     | 0.170005       | 0.175516       | 0.229209       | 0.260404       | 0.089873       | 0.089873       | 0.109019       | 0.187315       | 0.214128       | 0.058885       | 0.058885       | 0.214506       | 0.215368       | 0.065669       | 0.065669       | 0.286945       | 0.106309       | 0.106309       | 0.118223       | 0.118223       | 0.000000      
38     | 0.176451       | 0.175467       | 0.269842       | 0.292026       | 0.098358       | 0.098358       | 0.108342       | 0.206413       | 0.229441       | 0.059708       | 0.059708       | 0.234202       | 0.235317       | 0.066265       | 0.066265       | 0.328219       | 0.123361       | 0.123361       | 0.132409       | 0.132409       | 0.000000      
39     | 0.175170       | 0.185231       | 0.243075       | 0.243629       | 0.094622       | 0.094622       | 0.108437       | 0.193504       | 0.183192       | 0.057294       | 0.057294       | 0.220069       | 0.184160       | 0.064894       | 0.064894       | 0.259536       | 0.108519       | 0.108519       | 0.099494       | 0.099494       | 0.000000      
40     | 0.186660       | 0.183337       | 0.260331       | 0.261946       | 0.100044       | 0.100044       | 0.109225       | 0.200086       | 0.200235       | 0.060765       | 0.060765       | 0.223091       | 0.189346       | 0.062574       | 0.062574       | 0.281528       | 0.114613       | 0.114613       | 0.108064       | 0.108064       | 0.000000      
41     | 0.180508       | 0.179188       | 0.220685       | 0.248400       | 0.093394       | 0.093394       | 0.108512       | 0.173161       | 0.192441       | 0.058526       | 0.058526       | 0.197262       | 0.190118       | 0.062633       | 0.062633       | 0.244199       | 0.094601       | 0.094601       | 0.102574       | 0.102574       | 0.000000      
42     | 0.183717       | 0.175463       | 0.251972       | 0.257659       | 0.096095       | 0.096095       | 0.104468       | 0.197245       | 0.202965       | 0.060106       | 0.060106       | 0.216820       | 0.201006       | 0.061941       | 0.061941       | 0.281948       | 0.112008       | 0.112008       | 0.111116       | 0.111116       | 0.000000      
43     | 0.185659       | 0.179898       | 0.235607       | 0.268738       | 0.097457       | 0.097457       | 0.102909       | 0.180958       | 0.205603       | 0.058486       | 0.058486       | 0.201467       | 0.206159       | 0.061551       | 0.061551       | 0.278410       | 0.102647       | 0.102647       | 0.115198       | 0.115198       | 0.000000      
44     | 0.181462       | 0.183137       | 0.238735       | 0.256297       | 0.097083       | 0.097083       | 0.105871       | 0.181362       | 0.201113       | 0.059159       | 0.059159       | 0.199256       | 0.193591       | 0.061644       | 0.061644       | 0.258033       | 0.100557       | 0.100557       | 0.106988       | 0.106988       | 0.000000      
45     | 0.197284       | 0.198942       | 0.275127       | 0.270196       | 0.107358       | 0.107358       | 0.106541       | 0.202624       | 0.199251       | 0.060253       | 0.060253       | 0.224023       | 0.201734       | 0.065372       | 0.065372       | 0.286133       | 0.116656       | 0.116656       | 0.110485       | 0.110485       | 0.000000      
46     | 0.181527       | 0.180018       | 0.264956       | 0.261815       | 0.096702       | 0.096702       | 0.107388       | 0.220930       | 0.205536       | 0.062249       | 0.062249       | 0.233437       | 0.206616       | 0.064626       | 0.064626       | 0.299027       | 0.122655       | 0.122655       | 0.113761       | 0.113761       | 0.000000      
47     | 0.206001       | 0.204073       | 0.232968       | 0.270370       | 0.106621       | 0.106621       | 0.113637       | 0.174434       | 0.198390       | 0.062490       | 0.062490       | 0.191180       | 0.195097       | 0.064838       | 0.064838       | 0.243800       | 0.092522       | 0.092522       | 0.105577       | 0.105577       | 0.000000      
48     | 0.194729       | 0.197900       | 0.244853       | 0.319879       | 0.105968       | 0.105968       | 0.117178       | 0.181496       | 0.260396       | 0.065219       | 0.065219       | 0.203282       | 0.259109       | 0.070021       | 0.070021       | 0.304852       | 0.101426       | 0.101426       | 0.143416       | 0.143416       | 0.000000      
49     | 0.176658       | 0.176834       | 0.302414       | 0.254187       | 0.096147       | 0.096147       | 0.104871       | 0.260919       | 0.198317       | 0.062289       | 0.062289       | 0.281667       | 0.198165       | 0.066435       | 0.066435       | 0.339459       | 0.151174       | 0.151174       | 0.112095       | 0.112095       | 0.000000      
50     | 0.195143       | 0.196139       | 0.252087       | 0.270097       | 0.106326       | 0.106326       | 0.111285       | 0.182709       | 0.189325       | 0.059290       | 0.059290       | 0.204063       | 0.190319       | 0.064015       | 0.064015       | 0.251155       | 0.101430       | 0.101430       | 0.103621       | 0.103621       | 0.000000      
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
4h. PAIRWISE COSINE (Per Round, Upper Triangle)
--------------------------------------------------------------------------------
Round | c(0,1) | c(0,2) | c(0,3) | c(0,4) | c(0,5) | c(0,6) | c(1,2) | c(1,3) | c(1,4) | c(1,5) | c(1,6) | c(2,3) | c(2,4) | c(2,5) | c(2,6) | c(3,4) | c(3,5) | c(3,6) | c(4,5) | c(4,6) | c(5,6)
--------------------------------------------------------------------------------
1      | 0.403994       | 0.409766       | 0.787847       | 0.494773       | 0.828518       | 0.828518       | 0.816432       | 0.450911       | 0.613809       | 0.696131       | 0.696131       | 0.389379       | 0.542777       | 0.654940       | 0.654940       | 0.565934       | 0.860387       | 0.860387       | 0.786614       | 0.786614       | 1.000003      
2      | 0.560809       | 0.406198       | 0.753750       | 0.682612       | 0.876064       | 0.876064       | 0.649651       | 0.551143       | 0.572490       | 0.730676       | 0.730676       | 0.296994       | 0.468001       | 0.569649       | 0.569649       | 0.652350       | 0.854210       | 0.854210       | 0.845877       | 0.845877       | 1.000004      
3      | 0.413881       | 0.351261       | 0.579185       | 0.556405       | 0.809440       | 0.809440       | 0.509600       | 0.402528       | 0.425213       | 0.626040       | 0.626040       | 0.209013       | 0.375242       | 0.536069       | 0.536069       | 0.512993       | 0.769394       | 0.769394       | 0.792043       | 0.792043       | 0.999998      
4      | 0.301129       | 0.293974       | 0.410285       | 0.394364       | 0.726364       | 0.726364       | 0.394890       | 0.264932       | 0.299464       | 0.548226       | 0.548226       | 0.110159       | 0.335858       | 0.513850       | 0.513850       | 0.325005       | 0.664951       | 0.664951       | 0.718736       | 0.718736       | 1.000000      
5      | 0.189624       | 0.204801       | 0.273847       | 0.275281       | 0.661118       | 0.661118       | 0.279697       | 0.144683       | 0.187673       | 0.447084       | 0.447084       | 0.032773       | 0.244489       | 0.445250       | 0.445250       | 0.195245       | 0.586925       | 0.586925       | 0.647439       | 0.647439       | 1.000005      
6      | 0.048795       | 0.129699       | 0.200744       | 0.198093       | 0.603216       | 0.603216       | 0.219674       | 0.081560       | 0.107338       | 0.353413       | 0.353413       | -0.018259      | 0.193470       | 0.402293       | 0.402293       | 0.150255       | 0.545348       | 0.545348       | 0.610409       | 0.610409       | 1.000000      
7      | 0.047842       | 0.039566       | 0.154232       | 0.100775       | 0.535122       | 0.535122       | 0.208275       | 0.053604       | 0.090623       | 0.363776       | 0.363776       | -0.099865      | 0.148024       | 0.325413       | 0.325413       | 0.104084       | 0.531005       | 0.531005       | 0.562740       | 0.562740       | 1.000005      
8      | 0.035162       | 0.015375       | 0.114982       | 0.049147       | 0.482613       | 0.482613       | 0.149066       | 0.043036       | 0.045969       | 0.331486       | 0.331486       | -0.109960      | 0.080654       | 0.277289       | 0.277289       | 0.093196       | 0.524223       | 0.524223       | 0.552949       | 0.552949       | 1.000005      
9      | 0.036317       | 0.041094       | 0.102302       | 0.069228       | 0.499617       | 0.499617       | 0.165373       | 0.072124       | 0.059855       | 0.354357       | 0.354357       | -0.117616      | 0.110122       | 0.302014       | 0.302014       | 0.086933       | 0.508642       | 0.508642       | 0.556937       | 0.556937       | 1.000002      
10     | 0.018524       | 0.021644       | 0.086913       | 0.046161       | 0.479645       | 0.479645       | 0.114645       | 0.075777       | 0.052548       | 0.340950       | 0.340950       | -0.120270      | 0.075026       | 0.262317       | 0.262317       | 0.081086       | 0.521709       | 0.521709       | 0.537755       | 0.537755       | 1.000007      
11     | 0.007385       | 0.014468       | 0.069695       | 0.049289       | 0.493022       | 0.493022       | 0.046656       | 0.062044       | 0.056377       | 0.331190       | 0.331190       | -0.187260      | 0.054926       | 0.219097       | 0.219097       | 0.068788       | 0.487685       | 0.487685       | 0.527216       | 0.527216       | 1.000001      
12     | -0.007856      | -0.014207      | 0.051426       | 0.019587       | 0.439483       | 0.439483       | 0.050032       | 0.055987       | 0.046906       | 0.321232       | 0.321232       | -0.175840      | 0.085901       | 0.231314       | 0.231314       | 0.048519       | 0.490068       | 0.490068       | 0.531774       | 0.531774       | 1.000000      
13     | 0.022280       | -0.003627      | 0.050659       | 0.036257       | 0.472685       | 0.472685       | 0.085700       | 0.031564       | 0.017121       | 0.315621       | 0.315621       | -0.166520      | 0.061096       | 0.242131       | 0.242131       | 0.057141       | 0.470766       | 0.470766       | 0.527554       | 0.527554       | 1.000004      
14     | 0.013184       | -0.015427      | 0.029188       | 0.018595       | 0.466783       | 0.466783       | 0.091186       | 0.036332       | 0.011405       | 0.326617       | 0.326617       | -0.142776      | 0.059378       | 0.258042       | 0.258042       | 0.029330       | 0.453023       | 0.453023       | 0.499853       | 0.499853       | 0.999998      
15     | -0.004159      | -0.042435      | 0.054720       | 0.014961       | 0.466115       | 0.466115       | 0.086719       | 0.019960       | 0.020209       | 0.316442       | 0.316442       | -0.154290      | 0.061988       | 0.233059       | 0.233059       | 0.033389       | 0.482603       | 0.482603       | 0.483633       | 0.483633       | 1.000001      
16     | 0.000440       | -0.028365      | 0.054375       | 0.026569       | 0.465834       | 0.465834       | 0.091374       | 0.020339       | -0.015503      | 0.305181       | 0.305181       | -0.151095      | 0.063228       | 0.247164       | 0.247164       | 0.011234       | 0.461901       | 0.461901       | 0.494173       | 0.494173       | 1.000003      
17     | 0.008446       | -0.006634      | 0.016537       | 0.020584       | 0.460014       | 0.460014       | 0.091110       | 0.024114       | 0.000937       | 0.330196       | 0.330196       | -0.154276      | 0.054693       | 0.261927       | 0.261927       | 0.011647       | 0.438412       | 0.438412       | 0.488259       | 0.488259       | 1.000009      
18     | 0.034434       | -0.055330      | 0.063277       | 0.021041       | 0.492811       | 0.492811       | 0.087054       | -0.004511      | -0.011264      | 0.322773       | 0.322773       | -0.168279      | 0.018064       | 0.210473       | 0.210473       | -0.005877      | 0.441030       | 0.441030       | 0.465649       | 0.465649       | 0.999996      
19     | 0.018676       | -0.032938      | 0.019209       | -0.004173      | 0.451377       | 0.451377       | 0.078446       | -0.014472      | -0.030947      | 0.308004       | 0.308004       | -0.163327      | 0.021234       | 0.246214       | 0.246214       | -0.012254      | 0.415046       | 0.415046       | 0.467040       | 0.467040       | 1.000002      
20     | -0.006896      | -0.010326      | 0.018271       | -0.005467      | 0.478051       | 0.478051       | 0.100069       | -0.033568      | -0.015787      | 0.299952       | 0.299952       | -0.197988      | 0.017306       | 0.245432       | 0.245432       | -0.055841      | 0.365991       | 0.365991       | 0.456581       | 0.456581       | 1.000003      
21     | -0.023162      | -0.049949      | 0.022360       | -0.015433      | 0.443547       | 0.443547       | 0.151284       | -0.007925      | -0.029002      | 0.318059       | 0.318059       | -0.168789      | 0.018201       | 0.257702       | 0.257702       | -0.013121      | 0.406744       | 0.406744       | 0.459922       | 0.459922       | 0.999999      
22     | -0.004726      | -0.021716      | -0.017932      | -0.007762      | 0.432752       | 0.432752       | 0.100696       | -0.056527      | -0.031050      | 0.287912       | 0.287912       | -0.160540      | 0.030716       | 0.267361       | 0.267361       | -0.002479      | 0.395220       | 0.395220       | 0.475945       | 0.475945       | 1.000001      
23     | -0.052336      | -0.041642      | -0.004618      | 0.003604       | 0.439220       | 0.439220       | 0.115802       | -0.026761      | -0.024820      | 0.292908       | 0.292908       | -0.175966      | 0.004952       | 0.258386       | 0.258386       | -0.032370      | 0.386428       | 0.386428       | 0.452967       | 0.452967       | 1.000003      
24     | -0.048416      | -0.031531      | -0.029976      | -0.028625      | 0.401062       | 0.401062       | 0.145326       | -0.041348      | -0.012463      | 0.325716       | 0.325716       | -0.155318      | -0.009621      | 0.281533       | 0.281533       | -0.033250      | 0.360454       | 0.360454       | 0.459711       | 0.459711       | 1.000005      
25     | 0.008059       | -0.030713      | 0.023662       | -0.012327      | 0.458149       | 0.458149       | 0.072954       | 0.007174       | -0.036074      | 0.339428       | 0.339428       | -0.181382      | 0.032423       | 0.268203       | 0.268203       | -0.058834      | 0.376702       | 0.376702       | 0.432440       | 0.432440       | 1.000003      
26     | -0.004658      | -0.008097      | -0.024277      | -0.026524      | 0.420640       | 0.420640       | 0.100395       | -0.028087      | -0.001583      | 0.340105       | 0.340105       | -0.193641      | 0.013284       | 0.267284       | 0.267284       | 0.011163       | 0.395946       | 0.395946       | 0.453425       | 0.453425       | 1.000007      
27     | -0.007466      | -0.004177      | 0.001805       | -0.014476      | 0.455645       | 0.455645       | 0.107796       | -0.047807      | -0.038780      | 0.302458       | 0.302458       | -0.168479      | 0.030586       | 0.295823       | 0.295823       | -0.035776      | 0.373655       | 0.373655       | 0.438807       | 0.438807       | 1.000006      
28     | -0.031088      | 0.025953       | -0.033378      | 0.009805       | 0.441166       | 0.441166       | 0.115129       | -0.016464      | -0.007481      | 0.331513       | 0.331513       | -0.148949      | 0.010196       | 0.308683       | 0.308683       | -0.047869      | 0.365040       | 0.365040       | 0.449413       | 0.449413       | 1.000001      
29     | -0.015305      | -0.034122      | -0.016017      | -0.018459      | 0.412530       | 0.412530       | 0.053992       | -0.017483      | -0.014903      | 0.317392       | 0.317392       | -0.155442      | 0.039478       | 0.284641       | 0.284641       | -0.041759      | 0.392738       | 0.392738       | 0.443101       | 0.443101       | 1.000002      
30     | -0.057787      | -0.022472      | -0.016457      | -0.048724      | 0.396841       | 0.396841       | 0.111076       | 0.009172       | -0.016273      | 0.333891       | 0.333891       | -0.165278      | 0.022109       | 0.297942       | 0.297942       | -0.034468      | 0.351601       | 0.351601       | 0.467629       | 0.467629       | 1.000010      
31     | -0.019546      | -0.013720      | -0.026724      | -0.046002      | 0.403956       | 0.403956       | 0.096974       | -0.013841      | -0.033066      | 0.330599       | 0.330599       | -0.166067      | -0.021406      | 0.278623       | 0.278623       | -0.009302      | 0.399189       | 0.399189       | 0.420485       | 0.420485       | 0.999999      
32     | -0.016611      | 0.007259       | 0.027977       | -0.007390      | 0.455522       | 0.455522       | 0.088206       | -0.019964      | -0.023787      | 0.316674       | 0.316674       | -0.127035      | -0.001635      | 0.299675       | 0.299675       | -0.043489      | 0.394720       | 0.394720       | 0.436822       | 0.436822       | 1.000005      
33     | -0.071325      | -0.045288      | 0.026065       | -0.011949      | 0.421983       | 0.421983       | 0.111581       | -0.031085      | -0.020900      | 0.300452       | 0.300452       | -0.164637      | -0.009948      | 0.259716       | 0.259716       | -0.010824      | 0.413986       | 0.413986       | 0.445591       | 0.445591       | 1.000002      
34     | -0.022520      | 0.012744       | 0.005331       | -0.054903      | 0.420941       | 0.420941       | 0.106375       | -0.000994      | -0.017819      | 0.329062       | 0.329062       | -0.140936      | 0.019512       | 0.310427       | 0.310427       | -0.046217      | 0.386776       | 0.386776       | 0.438201       | 0.438201       | 1.000000      
35     | -0.029673      | -0.010651      | -0.036155      | -0.010912      | 0.385080       | 0.385080       | 0.111390       | -0.001802      | -0.023576      | 0.327270       | 0.327270       | -0.155354      | 0.038028       | 0.300996       | 0.300996       | -0.033145      | 0.386722       | 0.386722       | 0.477165       | 0.477165       | 1.000007      
36     | -0.037910      | -0.038149      | -0.037268      | -0.018821      | 0.402944       | 0.402944       | 0.132966       | -0.049538      | 0.008583       | 0.324923       | 0.324923       | -0.104650      | -0.022075      | 0.294901       | 0.294901       | -0.026780      | 0.356500       | 0.356500       | 0.476146       | 0.476146       | 1.000005      
37     | -0.050044      | -0.035829      | 0.003346       | -0.028945      | 0.371544       | 0.371544       | 0.136943       | -0.003653      | -0.022288      | 0.326005       | 0.326005       | -0.110781      | 0.009664       | 0.315037       | 0.315037       | -0.033398      | 0.406594       | 0.406594       | 0.467797       | 0.467797       | 1.000008      
38     | -0.016676      | 0.011974       | -0.032847      | -0.020888      | 0.399608       | 0.399608       | 0.084937       | -0.023024      | -0.012072      | 0.301794       | 0.301794       | -0.150021      | -0.022087      | 0.256867       | 0.256867       | -0.043280      | 0.386897       | 0.386897       | 0.477655       | 0.477655       | 1.000002      
39     | -0.002337      | -0.023753      | 0.024037       | -0.019927      | 0.433559       | 0.433559       | 0.118468       | -0.014656      | -0.014457      | 0.335793       | 0.335793       | -0.123225      | 0.016373       | 0.302819       | 0.302819       | -0.017752      | 0.426129       | 0.426129       | 0.432892       | 0.432892       | 1.000000      
40     | -0.040730      | -0.009877      | 0.000590       | -0.006788      | 0.415187       | 0.415187       | 0.091857       | -0.005339      | -0.007815      | 0.308939       | 0.308939       | -0.119615      | 0.061370       | 0.304890       | 0.304890       | -0.007181      | 0.425245       | 0.425245       | 0.477931       | 0.477931       | 1.000003      
41     | -0.041097      | -0.014432      | -0.003432      | -0.007356      | 0.419913       | 0.419913       | 0.124532       | -0.037545      | 0.007533       | 0.334429       | 0.334429       | -0.164630      | 0.036460       | 0.312313       | 0.312313       | -0.017535      | 0.354137       | 0.354137       | 0.485405       | 0.485405       | 1.000006      
42     | -0.052348      | 0.000530       | -0.025642      | 0.004888       | 0.409179       | 0.409179       | 0.132733       | -0.037605      | 0.004609       | 0.316896       | 0.316896       | -0.144562      | 0.017933       | 0.298511       | 0.298511       | -0.027225      | 0.380961       | 0.380961       | 0.482292       | 0.482292       | 1.000004      
43     | -0.038649      | 0.008776       | 0.025679       | -0.006553      | 0.436950       | 0.436950       | 0.140731       | -0.004636      | -0.001334      | 0.329895       | 0.329895       | -0.110668      | 0.007612       | 0.313267       | 0.313267       | -0.038962      | 0.397271       | 0.397271       | 0.465788       | 0.465788       | 1.000003      
44     | -0.013344      | -0.010893      | -0.018111      | -0.007986      | 0.429802       | 0.429802       | 0.134863       | -0.034581      | -0.031785      | 0.326101       | 0.326101       | -0.127435      | 0.020976       | 0.315093       | 0.315093       | -0.029489      | 0.368576       | 0.368576       | 0.458845       | 0.458845       | 1.000003      
45     | -0.020803      | -0.013907      | -0.005981      | 0.007017       | 0.435846       | 0.435846       | 0.147133       | -0.003238      | 0.007502       | 0.340265       | 0.340265       | -0.100947      | 0.009225       | 0.305019       | 0.305019       | -0.019775      | 0.415868       | 0.415868       | 0.457127       | 0.457127       | 1.000005      
46     | -0.007189      | -0.004516      | 0.014801       | -0.007086      | 0.429589       | 0.429589       | 0.125343       | -0.044009      | -0.010845      | 0.318454       | 0.318454       | -0.115180      | -0.022381      | 0.277987       | 0.277987       | -0.023667      | 0.430610       | 0.430610       | 0.443695       | 0.443695       | 1.000002      
47     | -0.045537      | -0.034591      | 0.024187       | -0.005324      | 0.459426       | 0.459426       | 0.095266       | -0.048588      | -0.008472      | 0.310427       | 0.310427       | -0.151712      | 0.009918       | 0.280827       | 0.280827       | -0.024986      | 0.352722       | 0.352722       | 0.463058       | 0.463058       | 1.000004      
48     | -0.023994      | -0.019320      | 0.001839       | -0.016793      | 0.410108       | 0.410108       | 0.104364       | 0.001768       | -0.042164      | 0.306483       | 0.306483       | -0.098419      | -0.017841      | 0.286991       | 0.286991       | 0.004100       | 0.388873       | 0.388873       | 0.500311       | 0.500311       | 0.999998      
49     | -0.027627      | 0.003411       | 0.002239       | -0.009041      | 0.386481       | 0.386481       | 0.175127       | -0.037738      | 0.017827       | 0.324123       | 0.324123       | -0.104689      | 0.045382       | 0.324290       | 0.324290       | -0.020951      | 0.468118       | 0.468118       | 0.451009       | 0.451009       | 1.000002      
50     | 0.021899       | 0.026319       | 0.022100       | -0.013113      | 0.479428       | 0.479428       | 0.108820       | -0.006534      | 0.006143       | 0.351919       | 0.351919       | -0.118036      | 0.010965       | 0.311559       | 0.311559       | -0.008599      | 0.399467       | 0.399467       | 0.443059       | 0.443059       | 1.000003      
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
🛡️  SHADOW DEFENSE SUMMARY (computed only, NOT applied)
  Parameters: n=7, f=2, k=3, m=5, beta=2, rounds=50
  Krum        : attacker selection rate = 1.0000   (chance = A/n = 0.2857)   [rounds where the selected update is malicious]
  Multi-Krum  : DR = 0.0000  FPR = 0.4000  ER = 1.0000   (chance DR = FPR = (n-m)/n = 0.2857)
  Trimmed Mean: DR = 0.0825  FPR = 0.7670  ER = 0.9175   (chance = 2*beta/n = 0.5714)   [DR/FPR = mean trim fraction over attacker/benign submissions]
  Median      : attacker provider rate = 0.4175  attacker total influence = 0.8350  benign provider rate = 0.0330   (chance per client = 1/n = 0.1429)   [no rejection step: DR/FPR n/a]
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
💾 SAVING DATA TO CSV FILES FOR EASY COLLECTION
--------------------------------------------------------------------------------
✅ Global Accuracy saved to: results/qwen_ag_news_alie_alpha0p3_seed42069_shadow_global_accuracy.csv
✅ Cosine Similarity saved to: results/qwen_ag_news_alie_alpha0p3_seed42069_shadow_cosine_similarity.csv
✅ Local Accuracy saved to: results/qwen_ag_news_alie_alpha0p3_seed42069_shadow_local_accuracy.csv

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
         1    0.000     0.00      0.00      0      0.00    0.00      0.04        -     120.82      0.17       6.92       8.59     136.58
         2    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.31      0.11       6.94       8.01     134.47
         3    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.55      0.11       6.94       7.62     134.36
         4    0.000     0.00      0.00      0      0.00    0.00      0.05        -     119.55      0.11       6.94       7.59     134.29
         5    0.000     0.00      0.00      0      0.00    0.00      0.05        -     119.55      0.11       6.93       7.62     134.33
         6    0.000     0.00      0.00      0      0.00    0.00      0.05        -     119.46      0.11       6.93       7.58     134.22
         7    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.56      0.11       6.93       7.57     134.27
         8    0.000     0.00      0.00      0      0.00    0.00      0.05        -     119.51      0.11       6.93       7.56     134.22
         9    0.000     0.00      0.00      0      0.00    0.00      0.03        -     119.50      0.11       6.93       7.58     134.21
        10    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.51      0.11       6.93       7.57     134.24
        11    0.000     0.00      0.00      0      0.00    0.00      0.05        -     119.53      0.11       6.93       7.59     134.29
        12    0.000     0.00      0.00      0      0.00    0.00      0.05        -     119.52      0.10       6.93       7.55     134.24
        13    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.41      0.11       6.93       7.54     134.09
        14    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.30      0.11       6.93       7.60     134.03
        15    0.000     0.00      0.00      0      0.00    0.00      0.03        -     119.36      0.11       6.93       7.54     134.04
        16    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.38      0.11       6.93       7.59     134.12
        17    0.000     0.00      0.00      0      0.00    0.00      0.03        -     119.24      0.11       6.94       7.60     133.98
        18    0.000     0.00      0.00      0      0.00    0.00      0.05        -     119.20      0.11       6.93       7.62     133.98
        19    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.24      0.11       6.94       7.59     133.99
        20    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.26      0.11       6.93       7.57     133.97
        21    0.000     0.00      0.00      0      0.00    0.00      0.05        -     119.20      0.10       6.94       7.61     133.98
        22    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.21      0.11       6.93       7.55     133.90
        23    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.31      0.15       6.93       7.63     134.12
        24    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.22      0.11       6.93       7.56     133.93
        25    0.000     0.00      0.00      0      0.00    0.00      0.05        -     119.21      0.12       6.93       7.59     134.00
        26    0.000     0.00      0.00      0      0.00    0.00      0.05        -     119.21      0.14       6.93       7.57     133.99
        27    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.20      0.11       6.93       7.58     133.93
        28    0.000     0.00      0.00      0      0.00    0.00      0.05        -     119.25      0.11       6.93       7.60     134.00
        29    0.000     0.00      0.00      0      0.00    0.00      0.03        -     119.53      0.11       6.94       7.59     134.26
        30    0.000     0.00      0.00      0      0.00    0.00      0.05        -     119.52      0.12       6.93       7.56     134.25
        31    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.29      0.11       6.94       7.64     134.08
        32    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.23      0.11       6.93       7.59     133.98
        33    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.23      0.11       6.94       7.62     134.00
        34    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.23      0.11       6.94       7.61     134.01
        35    0.000     0.00      0.00      0      0.00    0.00      0.05        -     119.43      0.10       6.94       7.59     134.19
        36    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.28      0.11       6.94       7.59     134.04
        37    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.33      0.11       6.94       7.61     134.09
        38    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.28      0.11       6.94       7.58     134.01
        39    0.000     0.00      0.00      0      0.00    0.00      0.05        -     119.31      0.11       6.94       7.60     134.07
        40    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.30      0.11       6.94       7.62     134.07
        41    0.000     0.00      0.00      0      0.00    0.00      0.05        -     119.37      0.11       6.94       7.65     134.20
        42    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.31      0.12       6.94       7.62     134.10
        43    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.32      0.11       6.94       7.62     134.09
        44    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.30      0.11       6.94       7.60     134.05
        45    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.33      0.11       6.94       7.60     134.08
        46    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.34      0.11       6.94       7.56     134.06
        47    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.34      0.11       6.94       7.60     134.09
        48    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.28      0.11       6.94       7.58     134.01
        49    0.000     0.00      0.00      0      0.00    0.00      0.03        -     119.33      0.11       6.94       7.62     134.09
        50    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.45      0.13       6.94       7.58     134.19
----------------------------------------------------------------------------------------------------------------------------------------
 mean r>=2    0.000     0.00      0.00    0.0      0.00    0.00      0.04        -     119.35      0.11       6.93       7.60     134.11
  std r>=2    0.000     0.00      0.00    0.0      0.00    0.00      0.01        -       0.12      0.01       0.00       0.06       0.13
  mean all    0.000     0.00      0.00    0.0      0.00    0.00      0.04        -     119.38      0.11       6.93       7.62     134.16
   sum all    0.000     0.00      0.00    0.0      0.00    0.00      2.08        -    5968.91      5.64     346.71     380.98    6707.78
----------------------------------------------------------------------------------------------------------------------------------------

Wall-clock totals (s): setup_and_initial_eval_sec 17.5, rounds_sec 6726.5, experiment_sec 6744.0, rounds_completed 50.0
Overhead per round saved to: results/qwen_ag_news_alie_alpha0p3_seed42069_shadow_overhead_rounds.csv
Overhead per attacker-round saved to: results/qwen_ag_news_alie_alpha0p3_seed42069_shadow_overhead_attackers.csv
Summary saved to: results/qwen_ag_news_alie_alpha0p3_seed42069_shadow_summary.txt (226 KB)


🚀 Starting AugMP experiment...
============================================================
Using configuration from main.py
Full log file: results/qwen_ag_news_alie_alpha0p3_seed42069_shadow_log.txt
============================================================
Running ALIE Attack (Model Poisoning Baseline)...

==================================================
Setting up Experiment: qwen_ag_news_alie_alpha0p3_seed42069_shadow
==================================================
tokenizer_config.json: 
 7.23k/? [00:00<00:00, 2.05MB/s]
vocab.json: 
 2.78M/? [00:00<00:00, 92.8MB/s]
merges.txt: 
 1.67M/? [00:00<00:00, 198MB/s]
tokenizer.json: 
 7.03M/? [00:00<00:00, 328MB/s]
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
 681/681 [00:00<00:00, 220kB/s]
model.safetensors: 100%
 988M/988M [00:03<00:00, 568MB/s]
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
  Client 5: ATTACKER (ALIE Attack)
    Claimed data size D'_j(t): 5473 (matches assigned data)
    Lagrangian Dual enabled: λ_dist(1)=0.1
  Client 6: ATTACKER (ALIE Attack)
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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.8633, std_norm=0.7369, attack_norm=0.8835, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.8633, std_norm=0.7369, attack_norm=0.8835, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.980240
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.673, Std Dev: 0.086
    Client 0 (Benign): 0.626
    Client 1 (Benign): 0.613
    Client 2 (Benign): 0.578
    Client 3 (Benign): 0.652
    Client 4 (Benign): 0.632
    Client 5 (Attacker): 0.804
    Client 6 (Attacker): 0.804
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.590680, Std Dev: 0.257942
    Client 0 (Benign): 0.720415
    Client 1 (Benign): 0.744663
    Client 2 (Benign): 0.782136
    Client 3 (Benign): 0.765626
    Client 4 (Benign): 0.754365
    Client 5 (Attacker): 0.183776
    Client 6 (Attacker): 0.183776
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=1.361764 krum=2.184508 mkrum=KEEP tm_trim=0.8067 (lo 0.4136 / hi 0.3930) med_prov=0.0247 d_med=0.802971
    [shadow] C1 (B): norm=0.606631 krum=0.931724 mkrum=KEEP tm_trim=0.7250 (lo 0.3788 / hi 0.3462) med_prov=0.0363 d_med=0.626460
    [shadow] C2 (B): norm=0.560976 krum=1.019077 mkrum=KEEP tm_trim=0.7328 (lo 0.3829 / hi 0.3499) med_prov=0.0362 d_med=0.660390
    [shadow] C3 (B): norm=1.518111 krum=2.456323 mkrum=REJECT tm_trim=0.8650 (lo 0.4426 / hi 0.4223) med_prov=0.0251 d_med=0.883313
    [shadow] C4 (B): norm=1.264700 krum=2.270075 mkrum=REJECT tm_trim=0.7272 (lo 0.3741 / hi 0.3531) med_prov=0.0210 d_med=0.790884
    [shadow] C5 (A): norm=0.883457 krum=0.848375 mkrum=KEEP tm_trim=0.0453 (lo 0.0000 / hi 0.0453) med_prov=0.1983 d_med=0.062792
    [shadow] C6 (A): norm=0.883457 krum=0.848375 mkrum=KEEP tm_trim=0.0981 (lo 0.0079 / hi 0.0902) med_prov=0.6584 d_med=0.062792

⏱️  Overhead round 1 (wall-clock s): round 136.58 | broadcast 0.03 | prepare 0.00 | benign train 120.82 [0:30.8 1:11.2 2:9.9 3:34.0 4:34.9] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.17 | observe 0.00 | eval_global 6.92 | eval_local 8.59 (bookkeeping) | unaccounted 0.01
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 1 Results:
  Clean Accuracy: 0.4567
  ΔClean vs prev: +0.2457
  ΔClean vs best: +0.0000
  Global Loss: 1.9912

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.6860, std_norm=0.5540, attack_norm=0.7004, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.6860, std_norm=0.5540, attack_norm=0.7004, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.783093
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.683, Std Dev: 0.102
    Client 0 (Benign): 0.693
    Client 1 (Benign): 0.633
    Client 2 (Benign): 0.493
    Client 3 (Benign): 0.660
    Client 4 (Benign): 0.678
    Client 5 (Attacker): 0.813
    Client 6 (Attacker): 0.813
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.444878, Std Dev: 0.196304
    Client 0 (Benign): 0.517642
    Client 1 (Benign): 0.569055
    Client 2 (Benign): 0.671576
    Client 3 (Benign): 0.556356
    Client 4 (Benign): 0.511131
    Client 5 (Attacker): 0.144193
    Client 6 (Attacker): 0.144193
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=1.091374 krum=1.288623 mkrum=KEEP tm_trim=0.7998 (lo 0.4114 / hi 0.3884) med_prov=0.0253 d_med=0.585321
    [shadow] C1 (B): norm=0.456474 krum=0.605912 mkrum=KEEP tm_trim=0.7279 (lo 0.3801 / hi 0.3478) med_prov=0.0357 d_med=0.474936
    [shadow] C2 (B): norm=0.444832 krum=0.809440 mkrum=KEEP tm_trim=0.7860 (lo 0.4069 / hi 0.3791) med_prov=0.0308 d_med=0.571752
    [shadow] C3 (B): norm=1.121806 krum=1.417320 mkrum=REJECT tm_trim=0.8141 (lo 0.4171 / hi 0.3970) med_prov=0.0224 d_med=0.642030
    [shadow] C4 (B): norm=1.015485 krum=1.345907 mkrum=REJECT tm_trim=0.7334 (lo 0.3780 / hi 0.3555) med_prov=0.0245 d_med=0.565322
    [shadow] C5 (A): norm=0.700432 krum=0.550280 mkrum=KEEP tm_trim=0.0365 (lo 0.0000 / hi 0.0365) med_prov=0.1800 d_med=0.048019
    [shadow] C6 (A): norm=0.700432 krum=0.550280 mkrum=KEEP tm_trim=0.1022 (lo 0.0066 / hi 0.0956) med_prov=0.6812 d_med=0.048019

⏱️  Overhead round 2 (wall-clock s): round 134.47 | broadcast 0.02 | prepare 0.00 | benign train 119.31 [0:30.3 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 8.01 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 2 Results:
  Clean Accuracy: 0.6940
  ΔClean vs prev: +0.2373
  ΔClean vs best: +0.0000
  Global Loss: 0.9662

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.4738, std_norm=0.4539, attack_norm=0.4878, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.4738, std_norm=0.4539, attack_norm=0.4878, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.539807
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.591, Std Dev: 0.116
    Client 0 (Benign): 0.587
    Client 1 (Benign): 0.501
    Client 2 (Benign): 0.420
    Client 3 (Benign): 0.540
    Client 4 (Benign): 0.576
    Client 5 (Attacker): 0.755
    Client 6 (Attacker): 0.755
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.362341, Std Dev: 0.160184
    Client 0 (Benign): 0.455659
    Client 1 (Benign): 0.440125
    Client 2 (Benign): 0.494431
    Client 3 (Benign): 0.468007
    Client 4 (Benign): 0.457744
    Client 5 (Attacker): 0.110210
    Client 6 (Attacker): 0.110210
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.797187 krum=1.014705 mkrum=KEEP tm_trim=0.7992 (lo 0.4120 / hi 0.3872) med_prov=0.0281 d_med=0.494028
    [shadow] C1 (B): norm=0.343377 krum=0.425802 mkrum=KEEP tm_trim=0.7095 (lo 0.3739 / hi 0.3356) med_prov=0.0412 d_med=0.375456
    [shadow] C2 (B): norm=0.389968 krum=0.505683 mkrum=KEEP tm_trim=0.7489 (lo 0.3907 / hi 0.3583) med_prov=0.0355 d_med=0.424716
    [shadow] C3 (B): norm=0.788796 krum=1.058199 mkrum=REJECT tm_trim=0.7977 (lo 0.4108 / hi 0.3869) med_prov=0.0263 d_med=0.521085
    [shadow] C4 (B): norm=0.790543 krum=1.016121 mkrum=REJECT tm_trim=0.7869 (lo 0.4054 / hi 0.3815) med_prov=0.0266 d_med=0.504037
    [shadow] C5 (A): norm=0.487816 krum=0.332236 mkrum=KEEP tm_trim=0.0447 (lo 0.0000 / hi 0.0447) med_prov=0.1482 d_med=0.044370
    [shadow] C6 (A): norm=0.487816 krum=0.332236 mkrum=KEEP tm_trim=0.1130 (lo 0.0071 / hi 0.1059) med_prov=0.6940 d_med=0.044370

⏱️  Overhead round 3 (wall-clock s): round 134.36 | broadcast 0.02 | prepare 0.00 | benign train 119.55 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.62 (bookkeeping) | unaccounted 0.06
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 3 Results:
  Clean Accuracy: 0.7750
  ΔClean vs prev: +0.0810
  ΔClean vs best: +0.0000
  Global Loss: 0.6605

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.3452, std_norm=0.3946, attack_norm=0.3596, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.3452, std_norm=0.3946, attack_norm=0.3596, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.390323
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.499, Std Dev: 0.130
    Client 0 (Benign): 0.475
    Client 1 (Benign): 0.393
    Client 2 (Benign): 0.360
    Client 3 (Benign): 0.407
    Client 4 (Benign): 0.465
    Client 5 (Attacker): 0.695
    Client 6 (Attacker): 0.695
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.311801, Std Dev: 0.142243
    Client 0 (Benign): 0.399283
    Client 1 (Benign): 0.361289
    Client 2 (Benign): 0.386764
    Client 3 (Benign): 0.428457
    Client 4 (Benign): 0.427823
    Client 5 (Attacker): 0.089495
    Client 6 (Attacker): 0.089495
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.603022 krum=0.703833 mkrum=KEEP tm_trim=0.7920 (lo 0.4101 / hi 0.3819) med_prov=0.0312 d_med=0.420827
    [shadow] C1 (B): norm=0.313136 krum=0.336292 mkrum=KEEP tm_trim=0.6961 (lo 0.3681 / hi 0.3281) med_prov=0.0434 d_med=0.315501
    [shadow] C2 (B): norm=0.337406 krum=0.365413 mkrum=KEEP tm_trim=0.7260 (lo 0.3816 / hi 0.3444) med_prov=0.0399 d_med=0.337370
    [shadow] C3 (B): norm=0.618022 krum=0.808883 mkrum=REJECT tm_trim=0.8100 (lo 0.4171 / hi 0.3929) med_prov=0.0270 d_med=0.467654
    [shadow] C4 (B): norm=0.645800 krum=0.809631 mkrum=REJECT tm_trim=0.8072 (lo 0.4158 / hi 0.3914) med_prov=0.0271 d_med=0.463342
    [shadow] C5 (A): norm=0.359636 krum=0.222397 mkrum=KEEP tm_trim=0.0495 (lo 0.0000 / hi 0.0495) med_prov=0.1361 d_med=0.041059
    [shadow] C6 (A): norm=0.359636 krum=0.222397 mkrum=KEEP tm_trim=0.1192 (lo 0.0073 / hi 0.1119) med_prov=0.6952 d_med=0.041059

⏱️  Overhead round 4 (wall-clock s): round 134.29 | broadcast 0.02 | prepare 0.00 | benign train 119.55 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.05 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.59 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 4 Results:
  Clean Accuracy: 0.8080
  ΔClean vs prev: +0.0330
  ΔClean vs best: +0.0000
  Global Loss: 0.5475

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.2791, std_norm=0.3787, attack_norm=0.2953, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.2791, std_norm=0.3787, attack_norm=0.2953, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.318115
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.410, Std Dev: 0.145
    Client 0 (Benign): 0.378
    Client 1 (Benign): 0.283
    Client 2 (Benign): 0.275
    Client 3 (Benign): 0.303
    Client 4 (Benign): 0.366
    Client 5 (Attacker): 0.631
    Client 6 (Attacker): 0.631
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.297555, Std Dev: 0.138340
    Client 0 (Benign): 0.399735
    Client 1 (Benign): 0.336334
    Client 2 (Benign): 0.353872
    Client 3 (Benign): 0.417490
    Client 4 (Benign): 0.409264
    Client 5 (Attacker): 0.083096
    Client 6 (Attacker): 0.083096
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.551211 krum=0.676074 mkrum=KEEP tm_trim=0.8051 (lo 0.4167 / hi 0.3884) med_prov=0.0314 d_med=0.419009
    [shadow] C1 (B): norm=0.282117 krum=0.310843 mkrum=KEEP tm_trim=0.6863 (lo 0.3639 / hi 0.3224) med_prov=0.0458 d_med=0.296709
    [shadow] C2 (B): norm=0.308799 krum=0.328953 mkrum=KEEP tm_trim=0.7175 (lo 0.3786 / hi 0.3389) med_prov=0.0415 d_med=0.311045
    [shadow] C3 (B): norm=0.552944 krum=0.742761 mkrum=REJECT tm_trim=0.8136 (lo 0.4189 / hi 0.3947) med_prov=0.0282 d_med=0.451984
    [shadow] C4 (B): norm=0.567312 krum=0.715778 mkrum=REJECT tm_trim=0.8014 (lo 0.4143 / hi 0.3871) med_prov=0.0292 d_med=0.439985
    [shadow] C5 (A): norm=0.295336 krum=0.193683 mkrum=KEEP tm_trim=0.0479 (lo 0.0000 / hi 0.0479) med_prov=0.1357 d_med=0.040861
    [shadow] C6 (A): norm=0.295336 krum=0.193683 mkrum=KEEP tm_trim=0.1282 (lo 0.0076 / hi 0.1206) med_prov=0.6882 d_med=0.040861

⏱️  Overhead round 5 (wall-clock s): round 134.33 | broadcast 0.02 | prepare 0.00 | benign train 119.55 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.05 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.62 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 5 Results:
  Clean Accuracy: 0.8237
  ΔClean vs prev: +0.0157
  ΔClean vs best: +0.0000
  Global Loss: 0.5256

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.2372, std_norm=0.3607, attack_norm=0.2542, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.2372, std_norm=0.3607, attack_norm=0.2542, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.272651
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.350, Std Dev: 0.154
    Client 0 (Benign): 0.297
    Client 1 (Benign): 0.194
    Client 2 (Benign): 0.222
    Client 3 (Benign): 0.251
    Client 4 (Benign): 0.312
    Client 5 (Attacker): 0.586
    Client 6 (Attacker): 0.586
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.283368, Std Dev: 0.131721
    Client 0 (Benign): 0.394263
    Client 1 (Benign): 0.324395
    Client 2 (Benign): 0.335986
    Client 3 (Benign): 0.387440
    Client 4 (Benign): 0.384010
    Client 5 (Attacker): 0.078742
    Client 6 (Attacker): 0.078742
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C0 (B), C3 (B)
    [shadow] C0 (B): norm=0.514162 krum=0.655433 mkrum=REJECT tm_trim=0.8094 (lo 0.4179 / hi 0.3915) med_prov=0.0293 d_med=0.415118
    [shadow] C1 (B): norm=0.263286 krum=0.296330 mkrum=KEEP tm_trim=0.6971 (lo 0.3686 / hi 0.3284) med_prov=0.0440 d_med=0.287707
    [shadow] C2 (B): norm=0.296725 krum=0.307016 mkrum=KEEP tm_trim=0.7182 (lo 0.3784 / hi 0.3398) med_prov=0.0410 d_med=0.296404
    [shadow] C3 (B): norm=0.496099 krum=0.640505 mkrum=REJECT tm_trim=0.8064 (lo 0.4160 / hi 0.3904) med_prov=0.0294 d_med=0.418549
    [shadow] C4 (B): norm=0.513919 krum=0.631644 mkrum=KEEP tm_trim=0.7955 (lo 0.4116 / hi 0.3839) med_prov=0.0299 d_med=0.412418
    [shadow] C5 (A): norm=0.254237 krum=0.178631 mkrum=KEEP tm_trim=0.0444 (lo 0.0000 / hi 0.0444) med_prov=0.1376 d_med=0.038867
    [shadow] C6 (A): norm=0.254237 krum=0.178631 mkrum=KEEP tm_trim=0.1291 (lo 0.0075 / hi 0.1216) med_prov=0.6888 d_med=0.038867

⏱️  Overhead round 6 (wall-clock s): round 134.22 | broadcast 0.02 | prepare 0.00 | benign train 119.46 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.05 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.58 (bookkeeping) | unaccounted 0.07
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 6 Results:
  Clean Accuracy: 0.8343
  ΔClean vs prev: +0.0107
  ΔClean vs best: +0.0000
  Global Loss: 0.4896

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.2109, std_norm=0.3524, attack_norm=0.2290, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.2109, std_norm=0.3524, attack_norm=0.2290, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.244039
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.309, Std Dev: 0.157
    Client 0 (Benign): 0.235
    Client 1 (Benign): 0.188
    Client 2 (Benign): 0.158
    Client 3 (Benign): 0.212
    Client 4 (Benign): 0.261
    Client 5 (Attacker): 0.553
    Client 6 (Attacker): 0.553
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.276475, Std Dev: 0.129259
    Client 0 (Benign): 0.376062
    Client 1 (Benign): 0.309030
    Client 2 (Benign): 0.328706
    Client 3 (Benign): 0.393514
    Client 4 (Benign): 0.374779
    Client 5 (Attacker): 0.076616
    Client 6 (Attacker): 0.076616
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.463592 krum=0.581261 mkrum=KEEP tm_trim=0.8004 (lo 0.4141 / hi 0.3863) med_prov=0.0312 d_med=0.392347
    [shadow] C1 (B): norm=0.265800 krum=0.274788 mkrum=KEEP tm_trim=0.6814 (lo 0.3616 / hi 0.3199) med_prov=0.0458 d_med=0.274098
    [shadow] C2 (B): norm=0.278044 krum=0.293797 mkrum=KEEP tm_trim=0.7198 (lo 0.3790 / hi 0.3407) med_prov=0.0414 d_med=0.290408
    [shadow] C3 (B): norm=0.499538 krum=0.666942 mkrum=REJECT tm_trim=0.8248 (lo 0.4249 / hi 0.3999) med_prov=0.0273 d_med=0.428606
    [shadow] C4 (B): norm=0.480436 krum=0.587458 mkrum=REJECT tm_trim=0.7975 (lo 0.4129 / hi 0.3847) med_prov=0.0304 d_med=0.399617
    [shadow] C5 (A): norm=0.229000 krum=0.167118 mkrum=KEEP tm_trim=0.0437 (lo 0.0000 / hi 0.0437) med_prov=0.1381 d_med=0.038156
    [shadow] C6 (A): norm=0.229000 krum=0.167118 mkrum=KEEP tm_trim=0.1324 (lo 0.0076 / hi 0.1247) med_prov=0.6858 d_med=0.038156

⏱️  Overhead round 7 (wall-clock s): round 134.27 | broadcast 0.03 | prepare 0.00 | benign train 119.56 [0:30.3 1:11.0 2:9.7 3:33.9 4:34.7] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.57 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 7 Results:
  Clean Accuracy: 0.8480
  ΔClean vs prev: +0.0137
  ΔClean vs best: +0.0000
  Global Loss: 0.4616

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1977, std_norm=0.3517, attack_norm=0.2168, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1977, std_norm=0.3517, attack_norm=0.2168, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.231735
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.279, Std Dev: 0.161
    Client 0 (Benign): 0.197
    Client 1 (Benign): 0.156
    Client 2 (Benign): 0.115
    Client 3 (Benign): 0.198
    Client 4 (Benign): 0.229
    Client 5 (Attacker): 0.528
    Client 6 (Attacker): 0.528
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.275706, Std Dev: 0.129410
    Client 0 (Benign): 0.363905
    Client 1 (Benign): 0.305584
    Client 2 (Benign): 0.326198
    Client 3 (Benign): 0.389500
    Client 4 (Benign): 0.392110
    Client 5 (Attacker): 0.076321
    Client 6 (Attacker): 0.076321
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.428943 krum=0.526360 mkrum=KEEP tm_trim=0.7841 (lo 0.4069 / hi 0.3772) med_prov=0.0341 d_med=0.374415
    [shadow] C1 (B): norm=0.260282 krum=0.274086 mkrum=KEEP tm_trim=0.6790 (lo 0.3609 / hi 0.3181) med_prov=0.0468 d_med=0.271149
    [shadow] C2 (B): norm=0.269350 krum=0.293744 mkrum=KEEP tm_trim=0.7241 (lo 0.3812 / hi 0.3429) med_prov=0.0414 d_med=0.288053
    [shadow] C3 (B): norm=0.490549 krum=0.649673 mkrum=REJECT tm_trim=0.8242 (lo 0.4249 / hi 0.3993) med_prov=0.0278 d_med=0.422899
    [shadow] C4 (B): norm=0.498908 krum=0.652371 mkrum=REJECT tm_trim=0.8102 (lo 0.4183 / hi 0.3919) med_prov=0.0284 d_med=0.422601
    [shadow] C5 (A): norm=0.216824 krum=0.164520 mkrum=KEEP tm_trim=0.0519 (lo 0.0000 / hi 0.0519) med_prov=0.1320 d_med=0.039100
    [shadow] C6 (A): norm=0.216824 krum=0.164520 mkrum=KEEP tm_trim=0.1266 (lo 0.0079 / hi 0.1187) med_prov=0.6895 d_med=0.039100

⏱️  Overhead round 8 (wall-clock s): round 134.22 | broadcast 0.02 | prepare 0.00 | benign train 119.51 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.05 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.56 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.04s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 8 Results:
  Clean Accuracy: 0.8580
  ΔClean vs prev: +0.0100
  ΔClean vs best: +0.0000
  Global Loss: 0.4530

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.2039, std_norm=0.3564, attack_norm=0.2229, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.2039, std_norm=0.3564, attack_norm=0.2229, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.236953
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.289, Std Dev: 0.160
    Client 0 (Benign): 0.208
    Client 1 (Benign): 0.174
    Client 2 (Benign): 0.134
    Client 3 (Benign): 0.194
    Client 4 (Benign): 0.240
    Client 5 (Attacker): 0.537
    Client 6 (Attacker): 0.537
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.279179, Std Dev: 0.131300
    Client 0 (Benign): 0.377685
    Client 1 (Benign): 0.307842
    Client 2 (Benign): 0.329316
    Client 3 (Benign): 0.393501
    Client 4 (Benign): 0.392082
    Client 5 (Attacker): 0.076913
    Client 6 (Attacker): 0.076913
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.451479 krum=0.572358 mkrum=KEEP tm_trim=0.7933 (lo 0.4113 / hi 0.3821) med_prov=0.0325 d_med=0.390644
    [shadow] C1 (B): norm=0.267130 krum=0.281374 mkrum=KEEP tm_trim=0.6797 (lo 0.3609 / hi 0.3188) med_prov=0.0465 d_med=0.273810
    [shadow] C2 (B): norm=0.277108 krum=0.302016 mkrum=KEEP tm_trim=0.7198 (lo 0.3792 / hi 0.3406) med_prov=0.0418 d_med=0.291487
    [shadow] C3 (B): norm=0.490293 krum=0.650648 mkrum=REJECT tm_trim=0.8194 (lo 0.4225 / hi 0.3970) med_prov=0.0286 d_med=0.426133
    [shadow] C4 (B): norm=0.500580 krum=0.648775 mkrum=REJECT tm_trim=0.8097 (lo 0.4183 / hi 0.3914) med_prov=0.0286 d_med=0.421369
    [shadow] C5 (A): norm=0.222939 krum=0.168031 mkrum=KEEP tm_trim=0.0495 (lo 0.0000 / hi 0.0495) med_prov=0.1331 d_med=0.039176
    [shadow] C6 (A): norm=0.222939 krum=0.168031 mkrum=KEEP tm_trim=0.1285 (lo 0.0078 / hi 0.1207) med_prov=0.6889 d_med=0.039176

⏱️  Overhead round 9 (wall-clock s): round 134.21 | broadcast 0.03 | prepare 0.00 | benign train 119.50 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.03 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.58 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 9 Results:
  Clean Accuracy: 0.8770
  ΔClean vs prev: +0.0190
  ΔClean vs best: +0.0000
  Global Loss: 0.4059

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1927, std_norm=0.3475, attack_norm=0.2118, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1927, std_norm=0.3475, attack_norm=0.2118, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.225568
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.273, Std Dev: 0.162
    Client 0 (Benign): 0.189
    Client 1 (Benign): 0.157
    Client 2 (Benign): 0.103
    Client 3 (Benign): 0.194
    Client 4 (Benign): 0.222
    Client 5 (Attacker): 0.524
    Client 6 (Attacker): 0.524
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.272031, Std Dev: 0.128269
    Client 0 (Benign): 0.368306
    Client 1 (Benign): 0.299995
    Client 2 (Benign): 0.319701
    Client 3 (Benign): 0.389153
    Client 4 (Benign): 0.377816
    Client 5 (Attacker): 0.074624
    Client 6 (Attacker): 0.074624
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.433835 krum=0.541796 mkrum=KEEP tm_trim=0.7951 (lo 0.4126 / hi 0.3825) med_prov=0.0319 d_med=0.380093
    [shadow] C1 (B): norm=0.261136 krum=0.271844 mkrum=KEEP tm_trim=0.6832 (lo 0.3631 / hi 0.3200) med_prov=0.0464 d_med=0.267685
    [shadow] C2 (B): norm=0.262002 krum=0.289956 mkrum=KEEP tm_trim=0.7192 (lo 0.3789 / hi 0.3403) med_prov=0.0419 d_med=0.283515
    [shadow] C3 (B): norm=0.487770 krum=0.636775 mkrum=REJECT tm_trim=0.8218 (lo 0.4229 / hi 0.3989) med_prov=0.0276 d_med=0.421578
    [shadow] C4 (B): norm=0.475989 krum=0.602493 mkrum=REJECT tm_trim=0.8031 (lo 0.4148 / hi 0.3882) med_prov=0.0299 d_med=0.405509
    [shadow] C5 (A): norm=0.211839 krum=0.159750 mkrum=KEEP tm_trim=0.0473 (lo 0.0000 / hi 0.0473) med_prov=0.1343 d_med=0.038333
    [shadow] C6 (A): norm=0.211839 krum=0.159750 mkrum=KEEP tm_trim=0.1304 (lo 0.0076 / hi 0.1228) med_prov=0.6880 d_med=0.038333

⏱️  Overhead round 10 (wall-clock s): round 134.24 | broadcast 0.03 | prepare 0.00 | benign train 119.51 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.57 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 10 Results:
  Clean Accuracy: 0.8770
  ΔClean vs prev: +0.0000
  ΔClean vs best: +0.0000
  Global Loss: 0.4041

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1855, std_norm=0.3468, attack_norm=0.2052, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1855, std_norm=0.3468, attack_norm=0.2052, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.217608
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.255, Std Dev: 0.167
    Client 0 (Benign): 0.188
    Client 1 (Benign): 0.139
    Client 2 (Benign): 0.061
    Client 3 (Benign): 0.165
    Client 4 (Benign): 0.214
    Client 5 (Attacker): 0.510
    Client 6 (Attacker): 0.510
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.271781, Std Dev: 0.127357
    Client 0 (Benign): 0.373735
    Client 1 (Benign): 0.303441
    Client 2 (Benign): 0.329962
    Client 3 (Benign): 0.382691
    Client 4 (Benign): 0.363946
    Client 5 (Attacker): 0.074346
    Client 6 (Attacker): 0.074346
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.445382 krum=0.568345 mkrum=KEEP tm_trim=0.7945 (lo 0.4116 / hi 0.3829) med_prov=0.0309 d_med=0.388086
    [shadow] C1 (B): norm=0.269372 krum=0.294657 mkrum=KEEP tm_trim=0.6930 (lo 0.3671 / hi 0.3259) med_prov=0.0454 d_med=0.273351
    [shadow] C2 (B): norm=0.269707 krum=0.319746 mkrum=KEEP tm_trim=0.7278 (lo 0.3825 / hi 0.3453) med_prov=0.0395 d_med=0.294991
    [shadow] C3 (B): norm=0.471219 krum=0.618543 mkrum=REJECT tm_trim=0.8193 (lo 0.4214 / hi 0.3979) med_prov=0.0274 d_med=0.414951
    [shadow] C4 (B): norm=0.455817 krum=0.568990 mkrum=REJECT tm_trim=0.7911 (lo 0.4098 / hi 0.3813) med_prov=0.0310 d_med=0.389539
    [shadow] C5 (A): norm=0.205244 krum=0.168677 mkrum=KEEP tm_trim=0.0420 (lo 0.0000 / hi 0.0420) med_prov=0.1390 d_med=0.037355
    [shadow] C6 (A): norm=0.205244 krum=0.168677 mkrum=KEEP tm_trim=0.1322 (lo 0.0076 / hi 0.1246) med_prov=0.6867 d_med=0.037355

⏱️  Overhead round 11 (wall-clock s): round 134.29 | broadcast 0.02 | prepare 0.00 | benign train 119.53 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.05 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.59 (bookkeeping) | unaccounted 0.05
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 11 Results:
  Clean Accuracy: 0.8883
  ΔClean vs prev: +0.0113
  ΔClean vs best: +0.0000
  Global Loss: 0.3811

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1752, std_norm=0.3357, attack_norm=0.1947, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1752, std_norm=0.3357, attack_norm=0.1947, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.206104
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.247, Std Dev: 0.166
    Client 0 (Benign): 0.155
    Client 1 (Benign): 0.131
    Client 2 (Benign): 0.068
    Client 3 (Benign): 0.160
    Client 4 (Benign): 0.211
    Client 5 (Attacker): 0.502
    Client 6 (Attacker): 0.502
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.262715, Std Dev: 0.123837
    Client 0 (Benign): 0.349837
    Client 1 (Benign): 0.289650
    Client 2 (Benign): 0.315070
    Client 3 (Benign): 0.378873
    Client 4 (Benign): 0.362059
    Client 5 (Attacker): 0.071757
    Client 6 (Attacker): 0.071757
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.402023 krum=0.489839 mkrum=KEEP tm_trim=0.7864 (lo 0.4088 / hi 0.3776) med_prov=0.0330 d_med=0.360741
    [shadow] C1 (B): norm=0.255221 krum=0.269086 mkrum=KEEP tm_trim=0.6795 (lo 0.3606 / hi 0.3189) med_prov=0.0463 d_med=0.260545
    [shadow] C2 (B): norm=0.261483 krum=0.292302 mkrum=KEEP tm_trim=0.7295 (lo 0.3832 / hi 0.3464) med_prov=0.0406 d_med=0.281461
    [shadow] C3 (B): norm=0.465900 krum=0.601013 mkrum=REJECT tm_trim=0.8273 (lo 0.4255 / hi 0.4018) med_prov=0.0268 d_med=0.410859
    [shadow] C4 (B): norm=0.452643 krum=0.551053 mkrum=REJECT tm_trim=0.7997 (lo 0.4145 / hi 0.3852) med_prov=0.0308 d_med=0.387249
    [shadow] C5 (A): norm=0.194720 krum=0.153861 mkrum=KEEP tm_trim=0.0443 (lo 0.0000 / hi 0.0443) med_prov=0.1357 d_med=0.036248
    [shadow] C6 (A): norm=0.194720 krum=0.153861 mkrum=KEEP tm_trim=0.1333 (lo 0.0075 / hi 0.1258) med_prov=0.6867 d_med=0.036248

⏱️  Overhead round 12 (wall-clock s): round 134.24 | broadcast 0.03 | prepare 0.00 | benign train 119.52 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.05 [5:0.0 6:0.0] | aggregate 0.10 | observe 0.00 | eval_global 6.93 | eval_local 7.55 (bookkeeping) | unaccounted 0.05
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 12 Results:
  Clean Accuracy: 0.8853
  ΔClean vs prev: -0.0030
  ΔClean vs best: -0.0030
  Global Loss: 0.4106

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1747, std_norm=0.3327, attack_norm=0.1939, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1747, std_norm=0.3327, attack_norm=0.1939, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.205086
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.250, Std Dev: 0.165
    Client 0 (Benign): 0.175
    Client 1 (Benign): 0.131
    Client 2 (Benign): 0.077
    Client 3 (Benign): 0.152
    Client 4 (Benign): 0.204
    Client 5 (Attacker): 0.505
    Client 6 (Attacker): 0.505
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.260730, Std Dev: 0.122220
    Client 0 (Benign): 0.353814
    Client 1 (Benign): 0.289407
    Client 2 (Benign): 0.313516
    Client 3 (Benign): 0.365434
    Client 4 (Benign): 0.359713
    Client 5 (Attacker): 0.071613
    Client 6 (Attacker): 0.071613
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.415517 krum=0.499881 mkrum=KEEP tm_trim=0.7901 (lo 0.4094 / hi 0.3806) med_prov=0.0314 d_med=0.365782
    [shadow] C1 (B): norm=0.252444 krum=0.261718 mkrum=KEEP tm_trim=0.6840 (lo 0.3630 / hi 0.3210) med_prov=0.0473 d_med=0.259277
    [shadow] C2 (B): norm=0.261641 krum=0.283835 mkrum=KEEP tm_trim=0.7291 (lo 0.3835 / hi 0.3456) med_prov=0.0401 d_med=0.279415
    [shadow] C3 (B): norm=0.445034 krum=0.563508 mkrum=REJECT tm_trim=0.8164 (lo 0.4205 / hi 0.3959) med_prov=0.0281 d_med=0.395752
    [shadow] C4 (B): norm=0.450793 krum=0.554436 mkrum=REJECT tm_trim=0.8037 (lo 0.4160 / hi 0.3877) med_prov=0.0299 d_med=0.386857
    [shadow] C5 (A): norm=0.193899 krum=0.151913 mkrum=KEEP tm_trim=0.0460 (lo 0.0000 / hi 0.0460) med_prov=0.1342 d_med=0.035987
    [shadow] C6 (A): norm=0.193899 krum=0.151913 mkrum=KEEP tm_trim=0.1307 (lo 0.0076 / hi 0.1231) med_prov=0.6891 d_med=0.035987

⏱️  Overhead round 13 (wall-clock s): round 134.09 | broadcast 0.03 | prepare 0.00 | benign train 119.41 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.54 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 13 Results:
  Clean Accuracy: 0.8890
  ΔClean vs prev: +0.0037
  ΔClean vs best: +0.0000
  Global Loss: 0.3994

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1696, std_norm=0.3297, attack_norm=0.1891, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1696, std_norm=0.3297, attack_norm=0.1891, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.197401
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.245, Std Dev: 0.164
    Client 0 (Benign): 0.163
    Client 1 (Benign): 0.134
    Client 2 (Benign): 0.085
    Client 3 (Benign): 0.143
    Client 4 (Benign): 0.186
    Client 5 (Attacker): 0.501
    Client 6 (Attacker): 0.501
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.258088, Std Dev: 0.121309
    Client 0 (Benign): 0.359381
    Client 1 (Benign): 0.288636
    Client 2 (Benign): 0.308222
    Client 3 (Benign): 0.358118
    Client 4 (Benign): 0.351685
    Client 5 (Attacker): 0.070288
    Client 6 (Attacker): 0.070288
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.421650 krum=0.519948 mkrum=KEEP tm_trim=0.8002 (lo 0.4137 / hi 0.3865) med_prov=0.0297 d_med=0.373680
    [shadow] C1 (B): norm=0.258474 krum=0.265080 mkrum=KEEP tm_trim=0.6955 (lo 0.3682 / hi 0.3273) med_prov=0.0446 d_med=0.259825
    [shadow] C2 (B): norm=0.263441 krum=0.282703 mkrum=KEEP tm_trim=0.7243 (lo 0.3809 / hi 0.3434) med_prov=0.0407 d_med=0.276074
    [shadow] C3 (B): norm=0.430674 krum=0.539103 mkrum=REJECT tm_trim=0.8121 (lo 0.4184 / hi 0.3937) med_prov=0.0287 d_med=0.386006
    [shadow] C4 (B): norm=0.433328 krum=0.526848 mkrum=REJECT tm_trim=0.7932 (lo 0.4113 / hi 0.3820) med_prov=0.0311 d_med=0.377365
    [shadow] C5 (A): norm=0.189118 krum=0.150099 mkrum=KEEP tm_trim=0.0433 (lo 0.0000 / hi 0.0433) med_prov=0.1363 d_med=0.035316
    [shadow] C6 (A): norm=0.189118 krum=0.150099 mkrum=KEEP tm_trim=0.1313 (lo 0.0075 / hi 0.1238) med_prov=0.6890 d_med=0.035316

⏱️  Overhead round 14 (wall-clock s): round 134.03 | broadcast 0.02 | prepare 0.00 | benign train 119.30 [0:30.2 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.60 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 14 Results:
  Clean Accuracy: 0.8857
  ΔClean vs prev: -0.0033
  ΔClean vs best: -0.0033
  Global Loss: 0.4310

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1661, std_norm=0.3245, attack_norm=0.1853, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1661, std_norm=0.3245, attack_norm=0.1853, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.194476
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.241, Std Dev: 0.165
    Client 0 (Benign): 0.159
    Client 1 (Benign): 0.126
    Client 2 (Benign): 0.070
    Client 3 (Benign): 0.153
    Client 4 (Benign): 0.183
    Client 5 (Attacker): 0.497
    Client 6 (Attacker): 0.497
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.254249, Std Dev: 0.119234
    Client 0 (Benign): 0.352384
    Client 1 (Benign): 0.287426
    Client 2 (Benign): 0.304802
    Client 3 (Benign): 0.362158
    Client 4 (Benign): 0.333905
    Client 5 (Attacker): 0.069533
    Client 6 (Attacker): 0.069533
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C0 (B), C3 (B)
    [shadow] C0 (B): norm=0.414647 krum=0.507486 mkrum=REJECT tm_trim=0.7993 (lo 0.4138 / hi 0.3854) med_prov=0.0302 d_med=0.367621
    [shadow] C1 (B): norm=0.255707 krum=0.258672 mkrum=KEEP tm_trim=0.6945 (lo 0.3676 / hi 0.3269) med_prov=0.0447 d_med=0.258361
    [shadow] C2 (B): norm=0.255188 krum=0.274037 mkrum=KEEP tm_trim=0.7258 (lo 0.3816 / hi 0.3442) med_prov=0.0402 d_med=0.272398
    [shadow] C3 (B): norm=0.444097 krum=0.562336 mkrum=REJECT tm_trim=0.8202 (lo 0.4220 / hi 0.3982) med_prov=0.0271 d_med=0.393288
    [shadow] C4 (B): norm=0.406159 krum=0.470246 mkrum=KEEP tm_trim=0.7857 (lo 0.4074 / hi 0.3783) med_prov=0.0324 d_med=0.355400
    [shadow] C5 (A): norm=0.185328 krum=0.147165 mkrum=KEEP tm_trim=0.0392 (lo 0.0000 / hi 0.0392) med_prov=0.1417 d_med=0.034896
    [shadow] C6 (A): norm=0.185328 krum=0.147165 mkrum=KEEP tm_trim=0.1354 (lo 0.0076 / hi 0.1279) med_prov=0.6837 d_med=0.034896

⏱️  Overhead round 15 (wall-clock s): round 134.04 | broadcast 0.03 | prepare 0.00 | benign train 119.36 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.03 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.54 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.01s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 15 Results:
  Clean Accuracy: 0.8863
  ΔClean vs prev: +0.0007
  ΔClean vs best: -0.0027
  Global Loss: 0.4472

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1667, std_norm=0.3272, attack_norm=0.1862, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1667, std_norm=0.3272, attack_norm=0.1862, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.195198
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.239, Std Dev: 0.165
    Client 0 (Benign): 0.164
    Client 1 (Benign): 0.118
    Client 2 (Benign): 0.078
    Client 3 (Benign): 0.143
    Client 4 (Benign): 0.179
    Client 5 (Attacker): 0.496
    Client 6 (Attacker): 0.496
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.256451, Std Dev: 0.120038
    Client 0 (Benign): 0.345407
    Client 1 (Benign): 0.292622
    Client 2 (Benign): 0.304199
    Client 3 (Benign): 0.360335
    Client 4 (Benign): 0.352238
    Client 5 (Attacker): 0.070177
    Client 6 (Attacker): 0.070177
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.406120 krum=0.490013 mkrum=KEEP tm_trim=0.7930 (lo 0.4107 / hi 0.3822) med_prov=0.0312 d_med=0.359100
    [shadow] C1 (B): norm=0.258584 krum=0.265137 mkrum=KEEP tm_trim=0.6979 (lo 0.3696 / hi 0.3284) med_prov=0.0438 d_med=0.262937
    [shadow] C2 (B): norm=0.257160 krum=0.275102 mkrum=KEEP tm_trim=0.7240 (lo 0.3809 / hi 0.3431) med_prov=0.0402 d_med=0.271842
    [shadow] C3 (B): norm=0.435622 krum=0.551064 mkrum=REJECT tm_trim=0.8151 (lo 0.4192 / hi 0.3958) med_prov=0.0277 d_med=0.389242
    [shadow] C4 (B): norm=0.431928 krum=0.522142 mkrum=REJECT tm_trim=0.7970 (lo 0.4122 / hi 0.3848) med_prov=0.0301 d_med=0.377835
    [shadow] C5 (A): norm=0.186187 krum=0.149275 mkrum=KEEP tm_trim=0.0447 (lo 0.0000 / hi 0.0447) med_prov=0.1357 d_med=0.034928
    [shadow] C6 (A): norm=0.186187 krum=0.149275 mkrum=KEEP tm_trim=0.1283 (lo 0.0074 / hi 0.1210) med_prov=0.6913 d_med=0.034928

⏱️  Overhead round 16 (wall-clock s): round 134.12 | broadcast 0.03 | prepare 0.00 | benign train 119.38 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.59 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 16 Results:
  Clean Accuracy: 0.8880
  ΔClean vs prev: +0.0017
  ΔClean vs best: -0.0010
  Global Loss: 0.4498

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1610, std_norm=0.3180, attack_norm=0.1801, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1610, std_norm=0.3180, attack_norm=0.1801, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.186655
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.239, Std Dev: 0.165
    Client 0 (Benign): 0.160
    Client 1 (Benign): 0.131
    Client 2 (Benign): 0.085
    Client 3 (Benign): 0.129
    Client 4 (Benign): 0.177
    Client 5 (Attacker): 0.496
    Client 6 (Attacker): 0.496
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.249157, Std Dev: 0.116586
    Client 0 (Benign): 0.340681
    Client 1 (Benign): 0.285484
    Client 2 (Benign): 0.297195
    Client 3 (Benign): 0.348256
    Client 4 (Benign): 0.336597
    Client 5 (Attacker): 0.067944
    Client 6 (Attacker): 0.067944
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.398392 krum=0.474981 mkrum=KEEP tm_trim=0.7925 (lo 0.4100 / hi 0.3825) med_prov=0.0312 d_med=0.353957
    [shadow] C1 (B): norm=0.260254 krum=0.259788 mkrum=KEEP tm_trim=0.7007 (lo 0.3704 / hi 0.3303) med_prov=0.0436 d_med=0.257736
    [shadow] C2 (B): norm=0.256499 krum=0.269414 mkrum=KEEP tm_trim=0.7245 (lo 0.3804 / hi 0.3441) med_prov=0.0391 d_med=0.266488
    [shadow] C3 (B): norm=0.415696 krum=0.514510 mkrum=REJECT tm_trim=0.8130 (lo 0.4189 / hi 0.3942) med_prov=0.0281 d_med=0.376255
    [shadow] C4 (B): norm=0.412376 krum=0.484210 mkrum=REJECT tm_trim=0.7971 (lo 0.4128 / hi 0.3843) med_prov=0.0302 d_med=0.361238
    [shadow] C5 (A): norm=0.180095 krum=0.143241 mkrum=KEEP tm_trim=0.0427 (lo 0.0000 / hi 0.0427) med_prov=0.1370 d_med=0.033875
    [shadow] C6 (A): norm=0.180095 krum=0.143241 mkrum=KEEP tm_trim=0.1294 (lo 0.0075 / hi 0.1219) med_prov=0.6908 d_med=0.033875

⏱️  Overhead round 17 (wall-clock s): round 133.98 | broadcast 0.03 | prepare 0.00 | benign train 119.24 [0:30.2 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.03 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.60 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 17 Results:
  Clean Accuracy: 0.8893
  ΔClean vs prev: +0.0013
  ΔClean vs best: +0.0000
  Global Loss: 0.4599

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1613, std_norm=0.3228, attack_norm=0.1810, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1613, std_norm=0.3228, attack_norm=0.1810, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.188816
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.231, Std Dev: 0.167
    Client 0 (Benign): 0.175
    Client 1 (Benign): 0.125
    Client 2 (Benign): 0.050
    Client 3 (Benign): 0.128
    Client 4 (Benign): 0.159
    Client 5 (Attacker): 0.489
    Client 6 (Attacker): 0.489
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.253199, Std Dev: 0.118083
    Client 0 (Benign): 0.347136
    Client 1 (Benign): 0.290131
    Client 2 (Benign): 0.305268
    Client 3 (Benign): 0.348864
    Client 4 (Benign): 0.342321
    Client 5 (Attacker): 0.069337
    Client 6 (Attacker): 0.069337
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.415528 krum=0.496672 mkrum=KEEP tm_trim=0.7940 (lo 0.4108 / hi 0.3832) med_prov=0.0308 d_med=0.363057
    [shadow] C1 (B): norm=0.262547 krum=0.263673 mkrum=KEEP tm_trim=0.7045 (lo 0.3723 / hi 0.3322) med_prov=0.0424 d_med=0.260903
    [shadow] C2 (B): norm=0.253551 krum=0.277108 mkrum=KEEP tm_trim=0.7269 (lo 0.3822 / hi 0.3448) med_prov=0.0391 d_med=0.273319
    [shadow] C3 (B): norm=0.417644 krum=0.525367 mkrum=REJECT tm_trim=0.8095 (lo 0.4167 / hi 0.3928) med_prov=0.0287 d_med=0.376890
    [shadow] C4 (B): norm=0.413286 krum=0.499111 mkrum=REJECT tm_trim=0.7936 (lo 0.4108 / hi 0.3828) med_prov=0.0305 d_med=0.366816
    [shadow] C5 (A): norm=0.181034 krum=0.148762 mkrum=KEEP tm_trim=0.0424 (lo 0.0000 / hi 0.0424) med_prov=0.1377 d_med=0.034172
    [shadow] C6 (A): norm=0.181034 krum=0.148762 mkrum=KEEP tm_trim=0.1291 (lo 0.0073 / hi 0.1218) med_prov=0.6908 d_med=0.034172

⏱️  Overhead round 18 (wall-clock s): round 133.98 | broadcast 0.03 | prepare 0.00 | benign train 119.20 [0:30.2 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.05 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.62 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 18 Results:
  Clean Accuracy: 0.8863
  ΔClean vs prev: -0.0030
  ΔClean vs best: -0.0030
  Global Loss: 0.5115

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1527, std_norm=0.3155, attack_norm=0.1725, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1527, std_norm=0.3155, attack_norm=0.1725, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.177976
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.222, Std Dev: 0.166
    Client 0 (Benign): 0.151
    Client 1 (Benign): 0.111
    Client 2 (Benign): 0.066
    Client 3 (Benign): 0.110
    Client 4 (Benign): 0.151
    Client 5 (Attacker): 0.481
    Client 6 (Attacker): 0.481
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.247522, Std Dev: 0.115334
    Client 0 (Benign): 0.332348
    Client 1 (Benign): 0.283064
    Client 2 (Benign): 0.302168
    Client 3 (Benign): 0.339599
    Client 4 (Benign): 0.339986
    Client 5 (Attacker): 0.067744
    Client 6 (Attacker): 0.067744
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.386919 krum=0.449825 mkrum=KEEP tm_trim=0.7861 (lo 0.4071 / hi 0.3790) med_prov=0.0323 d_med=0.345091
    [shadow] C1 (B): norm=0.255716 krum=0.259890 mkrum=KEEP tm_trim=0.6999 (lo 0.3698 / hi 0.3301) med_prov=0.0431 d_med=0.255483
    [shadow] C2 (B): norm=0.262829 krum=0.276963 mkrum=KEEP tm_trim=0.7338 (lo 0.3855 / hi 0.3483) med_prov=0.0386 d_med=0.271433
    [shadow] C3 (B): norm=0.400868 krum=0.495158 mkrum=REJECT tm_trim=0.8094 (lo 0.4173 / hi 0.3921) med_prov=0.0285 d_med=0.366812
    [shadow] C4 (B): norm=0.411824 krum=0.500078 mkrum=REJECT tm_trim=0.7986 (lo 0.4129 / hi 0.3856) med_prov=0.0299 d_med=0.366166
    [shadow] C5 (A): norm=0.172541 krum=0.144501 mkrum=KEEP tm_trim=0.0445 (lo 0.0000 / hi 0.0445) med_prov=0.1352 d_med=0.033577
    [shadow] C6 (A): norm=0.172541 krum=0.144501 mkrum=KEEP tm_trim=0.1278 (lo 0.0074 / hi 0.1204) med_prov=0.6926 d_med=0.033577

⏱️  Overhead round 19 (wall-clock s): round 133.99 | broadcast 0.03 | prepare 0.00 | benign train 119.24 [0:30.2 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.59 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 19 Results:
  Clean Accuracy: 0.8880
  ΔClean vs prev: +0.0017
  ΔClean vs best: -0.0013
  Global Loss: 0.5183

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1479, std_norm=0.3118, attack_norm=0.1678, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1479, std_norm=0.3118, attack_norm=0.1678, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.172279
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.214, Std Dev: 0.167
    Client 0 (Benign): 0.159
    Client 1 (Benign): 0.107
    Client 2 (Benign): 0.067
    Client 3 (Benign): 0.077
    Client 4 (Benign): 0.142
    Client 5 (Attacker): 0.474
    Client 6 (Attacker): 0.474
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.244215, Std Dev: 0.114480
    Client 0 (Benign): 0.338133
    Client 1 (Benign): 0.276230
    Client 2 (Benign): 0.292541
    Client 3 (Benign): 0.331252
    Client 4 (Benign): 0.338269
    Client 5 (Attacker): 0.066539
    Client 6 (Attacker): 0.066539
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C0 (B), C4 (B)
    [shadow] C0 (B): norm=0.400221 krum=0.471425 mkrum=REJECT tm_trim=0.7994 (lo 0.4128 / hi 0.3866) med_prov=0.0305 d_med=0.353022
    [shadow] C1 (B): norm=0.248239 krum=0.242927 mkrum=KEEP tm_trim=0.6954 (lo 0.3682 / hi 0.3271) med_prov=0.0435 d_med=0.249196
    [shadow] C2 (B): norm=0.253634 krum=0.256536 mkrum=KEEP tm_trim=0.7255 (lo 0.3814 / hi 0.3442) med_prov=0.0401 d_med=0.262106
    [shadow] C3 (B): norm=0.380045 krum=0.464214 mkrum=KEEP tm_trim=0.8069 (lo 0.4169 / hi 0.3900) med_prov=0.0295 d_med=0.356059
    [shadow] C4 (B): norm=0.406028 krum=0.487230 mkrum=REJECT tm_trim=0.7999 (lo 0.4135 / hi 0.3865) med_prov=0.0292 d_med=0.363185
    [shadow] C5 (A): norm=0.167779 krum=0.136379 mkrum=KEEP tm_trim=0.0458 (lo 0.0000 / hi 0.0458) med_prov=0.1357 d_med=0.033035
    [shadow] C6 (A): norm=0.167779 krum=0.136379 mkrum=KEEP tm_trim=0.1270 (lo 0.0072 / hi 0.1198) med_prov=0.6915 d_med=0.033035

⏱️  Overhead round 20 (wall-clock s): round 133.97 | broadcast 0.03 | prepare 0.00 | benign train 119.26 [0:30.3 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.57 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 20 Results:
  Clean Accuracy: 0.8900
  ΔClean vs prev: +0.0020
  ΔClean vs best: +0.0000
  Global Loss: 0.5338

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1480, std_norm=0.3071, attack_norm=0.1673, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1480, std_norm=0.3071, attack_norm=0.1673, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.171774
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.222, Std Dev: 0.165
    Client 0 (Benign): 0.137
    Client 1 (Benign): 0.121
    Client 2 (Benign): 0.078
    Client 3 (Benign): 0.108
    Client 4 (Benign): 0.147
    Client 5 (Attacker): 0.481
    Client 6 (Attacker): 0.481
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.241067, Std Dev: 0.112130
    Client 0 (Benign): 0.332612
    Client 1 (Benign): 0.276806
    Client 2 (Benign): 0.291781
    Client 3 (Benign): 0.324215
    Client 4 (Benign): 0.329396
    Client 5 (Attacker): 0.066330
    Client 6 (Attacker): 0.066330
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C0 (B), C4 (B)
    [shadow] C0 (B): norm=0.387237 krum=0.458566 mkrum=REJECT tm_trim=0.7958 (lo 0.4124 / hi 0.3834) med_prov=0.0304 d_med=0.348095
    [shadow] C1 (B): norm=0.251315 krum=0.237236 mkrum=KEEP tm_trim=0.7020 (lo 0.3709 / hi 0.3311) med_prov=0.0426 d_med=0.248451
    [shadow] C2 (B): norm=0.254182 krum=0.249789 mkrum=KEEP tm_trim=0.7303 (lo 0.3832 / hi 0.3472) med_prov=0.0393 d_med=0.260580
    [shadow] C3 (B): norm=0.381355 krum=0.453151 mkrum=KEEP tm_trim=0.8025 (lo 0.4146 / hi 0.3880) med_prov=0.0297 d_med=0.349725
    [shadow] C4 (B): norm=0.397396 krum=0.468377 mkrum=REJECT tm_trim=0.7984 (lo 0.4118 / hi 0.3865) med_prov=0.0290 d_med=0.354615
    [shadow] C5 (A): norm=0.167267 krum=0.135072 mkrum=KEEP tm_trim=0.0450 (lo 0.0000 / hi 0.0450) med_prov=0.1369 d_med=0.032516
    [shadow] C6 (A): norm=0.167267 krum=0.135072 mkrum=KEEP tm_trim=0.1260 (lo 0.0072 / hi 0.1187) med_prov=0.6922 d_med=0.032516

⏱️  Overhead round 21 (wall-clock s): round 133.98 | broadcast 0.03 | prepare 0.00 | benign train 119.20 [0:30.2 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.05 [5:0.0 6:0.0] | aggregate 0.10 | observe 0.00 | eval_global 6.94 | eval_local 7.61 (bookkeeping) | unaccounted 0.05
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 21 Results:
  Clean Accuracy: 0.8830
  ΔClean vs prev: -0.0070
  ΔClean vs best: -0.0070
  Global Loss: 0.5871

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1444, std_norm=0.3032, attack_norm=0.1636, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1444, std_norm=0.3032, attack_norm=0.1636, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.168247
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.217, Std Dev: 0.166
    Client 0 (Benign): 0.136
    Client 1 (Benign): 0.097
    Client 2 (Benign): 0.081
    Client 3 (Benign): 0.092
    Client 4 (Benign): 0.157
    Client 5 (Attacker): 0.477
    Client 6 (Attacker): 0.477
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.237874, Std Dev: 0.110755
    Client 0 (Benign): 0.322564
    Client 1 (Benign): 0.275114
    Client 2 (Benign): 0.286000
    Client 3 (Benign): 0.329002
    Client 4 (Benign): 0.321982
    Client 5 (Attacker): 0.065227
    Client 6 (Attacker): 0.065227
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.371051 krum=0.422685 mkrum=KEEP tm_trim=0.7889 (lo 0.4089 / hi 0.3799) med_prov=0.0305 d_med=0.334395
    [shadow] C1 (B): norm=0.245628 krum=0.239458 mkrum=KEEP tm_trim=0.7059 (lo 0.3723 / hi 0.3335) med_prov=0.0420 d_med=0.247958
    [shadow] C2 (B): norm=0.252349 krum=0.248279 mkrum=KEEP tm_trim=0.7294 (lo 0.3823 / hi 0.3471) med_prov=0.0391 d_med=0.256438
    [shadow] C3 (B): norm=0.385050 krum=0.469763 mkrum=REJECT tm_trim=0.8129 (lo 0.4191 / hi 0.3938) med_prov=0.0277 d_med=0.355974
    [shadow] C4 (B): norm=0.392274 krum=0.450589 mkrum=REJECT tm_trim=0.7933 (lo 0.4101 / hi 0.3832) med_prov=0.0303 d_med=0.346970
    [shadow] C5 (A): norm=0.163624 krum=0.132338 mkrum=KEEP tm_trim=0.0424 (lo 0.0000 / hi 0.0424) med_prov=0.1374 d_med=0.032015
    [shadow] C6 (A): norm=0.163624 krum=0.132338 mkrum=KEEP tm_trim=0.1272 (lo 0.0071 / hi 0.1201) med_prov=0.6930 d_med=0.032015

⏱️  Overhead round 22 (wall-clock s): round 133.90 | broadcast 0.02 | prepare 0.00 | benign train 119.21 [0:30.2 1:10.9 2:9.7 3:33.7 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.55 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 22 Results:
  Clean Accuracy: 0.8847
  ΔClean vs prev: +0.0017
  ΔClean vs best: -0.0053
  Global Loss: 0.6040

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1403, std_norm=0.2995, attack_norm=0.1595, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1403, std_norm=0.2995, attack_norm=0.1595, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.163124
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.211, Std Dev: 0.167
    Client 0 (Benign): 0.131
    Client 1 (Benign): 0.100
    Client 2 (Benign): 0.070
    Client 3 (Benign): 0.089
    Client 4 (Benign): 0.143
    Client 5 (Attacker): 0.472
    Client 6 (Attacker): 0.472
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.235214, Std Dev: 0.109164
    Client 0 (Benign): 0.321716
    Client 1 (Benign): 0.269914
    Client 2 (Benign): 0.291446
    Client 3 (Benign): 0.320890
    Client 4 (Benign): 0.313146
    Client 5 (Attacker): 0.064692
    Client 6 (Attacker): 0.064692
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C0 (B), C3 (B)
    [shadow] C0 (B): norm=0.374431 krum=0.434951 mkrum=REJECT tm_trim=0.7929 (lo 0.4110 / hi 0.3819) med_prov=0.0304 d_med=0.337170
    [shadow] C1 (B): norm=0.242663 krum=0.234268 mkrum=KEEP tm_trim=0.6979 (lo 0.3692 / hi 0.3287) med_prov=0.0443 d_med=0.243539
    [shadow] C2 (B): norm=0.258014 krum=0.252453 mkrum=KEEP tm_trim=0.7400 (lo 0.3876 / hi 0.3525) med_prov=0.0373 d_med=0.261148
    [shadow] C3 (B): norm=0.373368 krum=0.440780 mkrum=REJECT tm_trim=0.8082 (lo 0.4166 / hi 0.3916) med_prov=0.0282 d_med=0.346330
    [shadow] C4 (B): norm=0.376839 krum=0.431426 mkrum=KEEP tm_trim=0.7903 (lo 0.4085 / hi 0.3818) med_prov=0.0305 d_med=0.336844
    [shadow] C5 (A): norm=0.159521 krum=0.132405 mkrum=KEEP tm_trim=0.0418 (lo 0.0000 / hi 0.0418) med_prov=0.1390 d_med=0.031330
    [shadow] C6 (A): norm=0.159521 krum=0.132405 mkrum=KEEP tm_trim=0.1287 (lo 0.0071 / hi 0.1217) med_prov=0.6904 d_med=0.031330

⏱️  Overhead round 23 (wall-clock s): round 134.12 | broadcast 0.02 | prepare 0.00 | benign train 119.31 [0:30.3 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.15 | observe 0.00 | eval_global 6.93 | eval_local 7.63 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 23 Results:
  Clean Accuracy: 0.8913
  ΔClean vs prev: +0.0067
  ΔClean vs best: +0.0000
  Global Loss: 0.6065

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1360, std_norm=0.2928, attack_norm=0.1550, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1360, std_norm=0.2928, attack_norm=0.1550, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.156230
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.210, Std Dev: 0.166
    Client 0 (Benign): 0.111
    Client 1 (Benign): 0.116
    Client 2 (Benign): 0.085
    Client 3 (Benign): 0.077
    Client 4 (Benign): 0.139
    Client 5 (Attacker): 0.471
    Client 6 (Attacker): 0.471
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.230019, Std Dev: 0.106515
    Client 0 (Benign): 0.309609
    Client 1 (Benign): 0.271550
    Client 2 (Benign): 0.279473
    Client 3 (Benign): 0.306505
    Client 4 (Benign): 0.316419
    Client 5 (Attacker): 0.063288
    Client 6 (Attacker): 0.063288
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.351754 krum=0.400435 mkrum=KEEP tm_trim=0.7882 (lo 0.4076 / hi 0.3806) med_prov=0.0302 d_med=0.322643
    [shadow] C1 (B): norm=0.252748 krum=0.233284 mkrum=KEEP tm_trim=0.7131 (lo 0.3755 / hi 0.3376) med_prov=0.0402 d_med=0.245403
    [shadow] C2 (B): norm=0.251172 krum=0.238893 mkrum=KEEP tm_trim=0.7313 (lo 0.3831 / hi 0.3482) med_prov=0.0373 d_med=0.250804
    [shadow] C3 (B): norm=0.351709 krum=0.411778 mkrum=REJECT tm_trim=0.8017 (lo 0.4144 / hi 0.3873) med_prov=0.0290 d_med=0.330210
    [shadow] C4 (B): norm=0.382886 krum=0.443667 mkrum=REJECT tm_trim=0.8013 (lo 0.4127 / hi 0.3886) med_prov=0.0276 d_med=0.342428
    [shadow] C5 (A): norm=0.154976 krum=0.127571 mkrum=KEEP tm_trim=0.0451 (lo 0.0000 / hi 0.0451) med_prov=0.1372 d_med=0.029866
    [shadow] C6 (A): norm=0.154976 krum=0.127571 mkrum=KEEP tm_trim=0.1192 (lo 0.0067 / hi 0.1125) med_prov=0.6985 d_med=0.029866

⏱️  Overhead round 24 (wall-clock s): round 133.93 | broadcast 0.03 | prepare 0.00 | benign train 119.22 [0:30.2 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.56 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 24 Results:
  Clean Accuracy: 0.8837
  ΔClean vs prev: -0.0077
  ΔClean vs best: -0.0077
  Global Loss: 0.6488

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1382, std_norm=0.2902, attack_norm=0.1566, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1382, std_norm=0.2902, attack_norm=0.1566, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.157863
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.218, Std Dev: 0.167
    Client 0 (Benign): 0.151
    Client 1 (Benign): 0.122
    Client 2 (Benign): 0.072
    Client 3 (Benign): 0.091
    Client 4 (Benign): 0.132
    Client 5 (Attacker): 0.479
    Client 6 (Attacker): 0.479
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.227859, Std Dev: 0.105538
    Client 0 (Benign): 0.306356
    Client 1 (Benign): 0.270064
    Client 2 (Benign): 0.283755
    Client 3 (Benign): 0.303646
    Client 4 (Benign): 0.306876
    Client 5 (Attacker): 0.062158
    Client 6 (Attacker): 0.062158
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.360498 krum=0.399229 mkrum=KEEP tm_trim=0.7872 (lo 0.4072 / hi 0.3800) med_prov=0.0303 d_med=0.320679
    [shadow] C1 (B): norm=0.255429 krum=0.245981 mkrum=KEEP tm_trim=0.7132 (lo 0.3754 / hi 0.3378) med_prov=0.0404 d_med=0.246214
    [shadow] C2 (B): norm=0.254976 krum=0.256989 mkrum=KEEP tm_trim=0.7423 (lo 0.3889 / hi 0.3534) med_prov=0.0367 d_med=0.257044
    [shadow] C3 (B): norm=0.351271 krum=0.400290 mkrum=REJECT tm_trim=0.7969 (lo 0.4115 / hi 0.3854) med_prov=0.0295 d_med=0.327470
    [shadow] C4 (B): norm=0.364720 krum=0.408299 mkrum=REJECT tm_trim=0.7942 (lo 0.4102 / hi 0.3840) med_prov=0.0292 d_med=0.329867
    [shadow] C5 (A): norm=0.156593 krum=0.130730 mkrum=KEEP tm_trim=0.0418 (lo 0.0000 / hi 0.0418) med_prov=0.1391 d_med=0.029728
    [shadow] C6 (A): norm=0.156593 krum=0.130730 mkrum=KEEP tm_trim=0.1243 (lo 0.0067 / hi 0.1176) med_prov=0.6948 d_med=0.029728

⏱️  Overhead round 25 (wall-clock s): round 134.00 | broadcast 0.03 | prepare 0.00 | benign train 119.21 [0:30.2 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.05 [5:0.0 6:0.0] | aggregate 0.12 | observe 0.00 | eval_global 6.93 | eval_local 7.59 (bookkeeping) | unaccounted 0.06
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 25 Results:
  Clean Accuracy: 0.9003
  ΔClean vs prev: +0.0167
  ΔClean vs best: +0.0000
  Global Loss: 0.5840

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1388, std_norm=0.2913, attack_norm=0.1572, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1388, std_norm=0.2913, attack_norm=0.1572, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.159176
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.219, Std Dev: 0.167
    Client 0 (Benign): 0.130
    Client 1 (Benign): 0.124
    Client 2 (Benign): 0.074
    Client 3 (Benign): 0.093
    Client 4 (Benign): 0.151
    Client 5 (Attacker): 0.480
    Client 6 (Attacker): 0.480
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.228935, Std Dev: 0.105820
    Client 0 (Benign): 0.308421
    Client 1 (Benign): 0.270482
    Client 2 (Benign): 0.285321
    Client 3 (Benign): 0.315206
    Client 4 (Benign): 0.297118
    Client 5 (Attacker): 0.062998
    Client 6 (Attacker): 0.062998
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.352675 krum=0.394964 mkrum=KEEP tm_trim=0.7838 (lo 0.4058 / hi 0.3780) med_prov=0.0300 d_med=0.320274
    [shadow] C1 (B): norm=0.254643 krum=0.241423 mkrum=KEEP tm_trim=0.7145 (lo 0.3761 / hi 0.3384) med_prov=0.0397 d_med=0.245696
    [shadow] C2 (B): norm=0.254859 krum=0.253267 mkrum=KEEP tm_trim=0.7432 (lo 0.3886 / hi 0.3547) med_prov=0.0357 d_med=0.257334
    [shadow] C3 (B): norm=0.371203 krum=0.440536 mkrum=REJECT tm_trim=0.8164 (lo 0.4196 / hi 0.3967) med_prov=0.0263 d_med=0.342842
    [shadow] C4 (B): norm=0.358582 krum=0.395459 mkrum=REJECT tm_trim=0.7790 (lo 0.4034 / hi 0.3756) med_prov=0.0313 d_med=0.319859
    [shadow] C5 (A): norm=0.157214 krum=0.130580 mkrum=KEEP tm_trim=0.0362 (lo 0.0000 / hi 0.0362) med_prov=0.1417 d_med=0.029063
    [shadow] C6 (A): norm=0.157214 krum=0.130580 mkrum=KEEP tm_trim=0.1269 (lo 0.0064 / hi 0.1205) med_prov=0.6952 d_med=0.029063

⏱️  Overhead round 26 (wall-clock s): round 133.99 | broadcast 0.03 | prepare 0.00 | benign train 119.21 [0:30.2 1:10.9 2:9.7 3:33.7 4:34.6] | attack 0.05 [5:0.0 6:0.0] | aggregate 0.14 | observe 0.00 | eval_global 6.93 | eval_local 7.57 (bookkeeping) | unaccounted 0.06
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 26 Results:
  Clean Accuracy: 0.8953
  ΔClean vs prev: -0.0050
  ΔClean vs best: -0.0050
  Global Loss: 0.6602

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1356, std_norm=0.2857, attack_norm=0.1536, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1356, std_norm=0.2857, attack_norm=0.1536, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.155508
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.217, Std Dev: 0.166
    Client 0 (Benign): 0.148
    Client 1 (Benign): 0.103
    Client 2 (Benign): 0.093
    Client 3 (Benign): 0.083
    Client 4 (Benign): 0.137
    Client 5 (Attacker): 0.478
    Client 6 (Attacker): 0.478
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.224382, Std Dev: 0.104016
    Client 0 (Benign): 0.304893
    Client 1 (Benign): 0.262246
    Client 2 (Benign): 0.277272
    Client 3 (Benign): 0.305062
    Client 4 (Benign): 0.298204
    Client 5 (Attacker): 0.061497
    Client 6 (Attacker): 0.061497
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.356829 krum=0.387698 mkrum=KEEP tm_trim=0.7906 (lo 0.4083 / hi 0.3823) med_prov=0.0297 d_med=0.318295
    [shadow] C1 (B): norm=0.239063 krum=0.225092 mkrum=KEEP tm_trim=0.7035 (lo 0.3705 / hi 0.3330) med_prov=0.0404 d_med=0.238021
    [shadow] C2 (B): norm=0.252763 krum=0.237052 mkrum=KEEP tm_trim=0.7382 (lo 0.3866 / hi 0.3516) med_prov=0.0365 d_med=0.250004
    [shadow] C3 (B): norm=0.353702 krum=0.406541 mkrum=REJECT tm_trim=0.8181 (lo 0.4213 / hi 0.3968) med_prov=0.0261 d_med=0.329869
    [shadow] C4 (B): norm=0.355882 krum=0.389583 mkrum=REJECT tm_trim=0.7874 (lo 0.4067 / hi 0.3808) med_prov=0.0295 d_med=0.320559
    [shadow] C5 (A): norm=0.153649 krum=0.123060 mkrum=KEEP tm_trim=0.0391 (lo 0.0000 / hi 0.0391) med_prov=0.1421 d_med=0.028540
    [shadow] C6 (A): norm=0.153649 krum=0.123060 mkrum=KEEP tm_trim=0.1231 (lo 0.0066 / hi 0.1165) med_prov=0.6957 d_med=0.028540

⏱️  Overhead round 27 (wall-clock s): round 133.93 | broadcast 0.03 | prepare 0.00 | benign train 119.20 [0:30.2 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.58 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 27 Results:
  Clean Accuracy: 0.8947
  ΔClean vs prev: -0.0007
  ΔClean vs best: -0.0057
  Global Loss: 0.6541

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1384, std_norm=0.2889, attack_norm=0.1566, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1384, std_norm=0.2889, attack_norm=0.1566, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.157480
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.222, Std Dev: 0.166
    Client 0 (Benign): 0.142
    Client 1 (Benign): 0.121
    Client 2 (Benign): 0.103
    Client 3 (Benign): 0.081
    Client 4 (Benign): 0.144
    Client 5 (Attacker): 0.483
    Client 6 (Attacker): 0.483
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.226765, Std Dev: 0.105245
    Client 0 (Benign): 0.305362
    Client 1 (Benign): 0.266981
    Client 2 (Benign): 0.276609
    Client 3 (Benign): 0.311010
    Client 4 (Benign): 0.303377
    Client 5 (Attacker): 0.062008
    Client 6 (Attacker): 0.062008
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.354515 krum=0.387837 mkrum=KEEP tm_trim=0.7917 (lo 0.4092 / hi 0.3825) med_prov=0.0303 d_med=0.318172
    [shadow] C1 (B): norm=0.249544 krum=0.233835 mkrum=KEEP tm_trim=0.7132 (lo 0.3750 / hi 0.3382) med_prov=0.0405 d_med=0.242524
    [shadow] C2 (B): norm=0.253737 krum=0.240812 mkrum=KEEP tm_trim=0.7347 (lo 0.3852 / hi 0.3494) med_prov=0.0372 d_med=0.249554
    [shadow] C3 (B): norm=0.357009 krum=0.414983 mkrum=REJECT tm_trim=0.8086 (lo 0.4164 / hi 0.3921) med_prov=0.0276 d_med=0.334904
    [shadow] C4 (B): norm=0.365174 krum=0.408798 mkrum=REJECT tm_trim=0.7864 (lo 0.4073 / hi 0.3791) med_prov=0.0299 d_med=0.327320
    [shadow] C5 (A): norm=0.156557 krum=0.125248 mkrum=KEEP tm_trim=0.0403 (lo 0.0000 / hi 0.0403) med_prov=0.1403 d_med=0.029522
    [shadow] C6 (A): norm=0.156557 krum=0.125248 mkrum=KEEP tm_trim=0.1251 (lo 0.0068 / hi 0.1183) med_prov=0.6942 d_med=0.029522

⏱️  Overhead round 28 (wall-clock s): round 134.00 | broadcast 0.03 | prepare 0.00 | benign train 119.25 [0:30.2 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.05 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.60 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 28 Results:
  Clean Accuracy: 0.8997
  ΔClean vs prev: +0.0050
  ΔClean vs best: -0.0007
  Global Loss: 0.6439

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1328, std_norm=0.2829, attack_norm=0.1509, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1328, std_norm=0.2829, attack_norm=0.1509, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.151999
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.213, Std Dev: 0.167
    Client 0 (Benign): 0.124
    Client 1 (Benign): 0.107
    Client 2 (Benign): 0.079
    Client 3 (Benign): 0.092
    Client 4 (Benign): 0.142
    Client 5 (Attacker): 0.475
    Client 6 (Attacker): 0.475
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.222029, Std Dev: 0.103016
    Client 0 (Benign): 0.293559
    Client 1 (Benign): 0.260654
    Client 2 (Benign): 0.279231
    Client 3 (Benign): 0.307555
    Client 4 (Benign): 0.292166
    Client 5 (Attacker): 0.060519
    Client 6 (Attacker): 0.060519
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.335702 krum=0.361694 mkrum=KEEP tm_trim=0.7854 (lo 0.4058 / hi 0.3796) med_prov=0.0298 d_med=0.305684
    [shadow] C1 (B): norm=0.243218 krum=0.234892 mkrum=KEEP tm_trim=0.7115 (lo 0.3749 / hi 0.3367) med_prov=0.0402 d_med=0.238416
    [shadow] C2 (B): norm=0.255319 krum=0.249686 mkrum=KEEP tm_trim=0.7481 (lo 0.3906 / hi 0.3575) med_prov=0.0353 d_med=0.253373
    [shadow] C3 (B): norm=0.359721 krum=0.410680 mkrum=REJECT tm_trim=0.8108 (lo 0.4170 / hi 0.3938) med_prov=0.0265 d_med=0.332875
    [shadow] C4 (B): norm=0.349098 krum=0.375935 mkrum=REJECT tm_trim=0.7825 (lo 0.4054 / hi 0.3771) med_prov=0.0299 d_med=0.313382
    [shadow] C5 (A): norm=0.150889 krum=0.124651 mkrum=KEEP tm_trim=0.0371 (lo 0.0000 / hi 0.0371) med_prov=0.1433 d_med=0.028193
    [shadow] C6 (A): norm=0.150889 krum=0.124651 mkrum=KEEP tm_trim=0.1245 (lo 0.0064 / hi 0.1181) med_prov=0.6950 d_med=0.028193

⏱️  Overhead round 29 (wall-clock s): round 134.26 | broadcast 0.02 | prepare 0.00 | benign train 119.53 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.03 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.59 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 29 Results:
  Clean Accuracy: 0.9020
  ΔClean vs prev: +0.0023
  ΔClean vs best: +0.0000
  Global Loss: 0.6322

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1323, std_norm=0.2824, attack_norm=0.1505, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1323, std_norm=0.2824, attack_norm=0.1505, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.150899
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.213, Std Dev: 0.166
    Client 0 (Benign): 0.108
    Client 1 (Benign): 0.119
    Client 2 (Benign): 0.090
    Client 3 (Benign): 0.083
    Client 4 (Benign): 0.143
    Client 5 (Attacker): 0.475
    Client 6 (Attacker): 0.475
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.221632, Std Dev: 0.102971
    Client 0 (Benign): 0.301442
    Client 1 (Benign): 0.262096
    Client 2 (Benign): 0.272194
    Client 3 (Benign): 0.282792
    Client 4 (Benign): 0.311587
    Client 5 (Attacker): 0.060657
    Client 6 (Attacker): 0.060657
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C0 (B), C4 (B)
    [shadow] C0 (B): norm=0.341978 krum=0.380321 mkrum=REJECT tm_trim=0.7895 (lo 0.4077 / hi 0.3818) med_prov=0.0292 d_med=0.314698
    [shadow] C1 (B): norm=0.246791 krum=0.226806 mkrum=KEEP tm_trim=0.7116 (lo 0.3747 / hi 0.3369) med_prov=0.0393 d_med=0.238558
    [shadow] C2 (B): norm=0.249078 krum=0.234005 mkrum=KEEP tm_trim=0.7393 (lo 0.3869 / hi 0.3523) med_prov=0.0368 d_med=0.245816
    [shadow] C3 (B): norm=0.321612 krum=0.346986 mkrum=KEEP tm_trim=0.7955 (lo 0.4107 / hi 0.3848) med_prov=0.0297 d_med=0.302894
    [shadow] C4 (B): norm=0.378112 krum=0.425639 mkrum=REJECT tm_trim=0.8031 (lo 0.4135 / hi 0.3896) med_prov=0.0260 d_med=0.337474
    [shadow] C5 (A): norm=0.150528 krum=0.121115 mkrum=KEEP tm_trim=0.0463 (lo 0.0000 / hi 0.0463) med_prov=0.1374 d_med=0.028146
    [shadow] C6 (A): norm=0.150528 krum=0.121115 mkrum=KEEP tm_trim=0.1147 (lo 0.0066 / hi 0.1082) med_prov=0.7016 d_med=0.028146

⏱️  Overhead round 30 (wall-clock s): round 134.25 | broadcast 0.03 | prepare 0.00 | benign train 119.52 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.05 [5:0.0 6:0.0] | aggregate 0.12 | observe 0.00 | eval_global 6.93 | eval_local 7.56 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 30 Results:
  Clean Accuracy: 0.8943
  ΔClean vs prev: -0.0077
  ΔClean vs best: -0.0077
  Global Loss: 0.6951

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1334, std_norm=0.2873, attack_norm=0.1519, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1334, std_norm=0.2873, attack_norm=0.1519, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.152572
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.210, Std Dev: 0.166
    Client 0 (Benign): 0.117
    Client 1 (Benign): 0.115
    Client 2 (Benign): 0.076
    Client 3 (Benign): 0.097
    Client 4 (Benign): 0.122
    Client 5 (Attacker): 0.472
    Client 6 (Attacker): 0.472
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.225859, Std Dev: 0.104213
    Client 0 (Benign): 0.301101
    Client 1 (Benign): 0.265874
    Client 2 (Benign): 0.286020
    Client 3 (Benign): 0.307204
    Client 4 (Benign): 0.296363
    Client 5 (Attacker): 0.062224
    Client 6 (Attacker): 0.062224
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.341704 krum=0.378337 mkrum=KEEP tm_trim=0.7865 (lo 0.4063 / hi 0.3802) med_prov=0.0294 d_med=0.312676
    [shadow] C1 (B): norm=0.249864 krum=0.238177 mkrum=KEEP tm_trim=0.7055 (lo 0.3712 / hi 0.3343) med_prov=0.0401 d_med=0.242177
    [shadow] C2 (B): norm=0.259815 krum=0.254529 mkrum=KEEP tm_trim=0.7493 (lo 0.3909 / hi 0.3584) med_prov=0.0344 d_med=0.258290
    [shadow] C3 (B): norm=0.361935 krum=0.416289 mkrum=REJECT tm_trim=0.8126 (lo 0.4184 / hi 0.3942) med_prov=0.0268 d_med=0.333502
    [shadow] C4 (B): norm=0.352023 krum=0.396221 mkrum=REJECT tm_trim=0.7861 (lo 0.4068 / hi 0.3793) med_prov=0.0293 d_med=0.320016
    [shadow] C5 (A): norm=0.151938 krum=0.129008 mkrum=KEEP tm_trim=0.0376 (lo 0.0000 / hi 0.0376) med_prov=0.1415 d_med=0.028412
    [shadow] C6 (A): norm=0.151938 krum=0.129008 mkrum=KEEP tm_trim=0.1224 (lo 0.0064 / hi 0.1160) med_prov=0.6986 d_med=0.028412

⏱️  Overhead round 31 (wall-clock s): round 134.08 | broadcast 0.02 | prepare 0.00 | benign train 119.29 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.64 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 31 Results:
  Clean Accuracy: 0.8937
  ΔClean vs prev: -0.0007
  ΔClean vs best: -0.0083
  Global Loss: 0.7419

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1348, std_norm=0.2791, attack_norm=0.1523, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1348, std_norm=0.2791, attack_norm=0.1523, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.154035
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.223, Std Dev: 0.166
    Client 0 (Benign): 0.154
    Client 1 (Benign): 0.110
    Client 2 (Benign): 0.094
    Client 3 (Benign): 0.104
    Client 4 (Benign): 0.133
    Client 5 (Attacker): 0.484
    Client 6 (Attacker): 0.484
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.219236, Std Dev: 0.101424
    Client 0 (Benign): 0.291572
    Client 1 (Benign): 0.259757
    Client 2 (Benign): 0.272309
    Client 3 (Benign): 0.292711
    Client 4 (Benign): 0.298208
    Client 5 (Attacker): 0.060048
    Client 6 (Attacker): 0.060048
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.342180 krum=0.363114 mkrum=KEEP tm_trim=0.7885 (lo 0.4078 / hi 0.3807) med_prov=0.0294 d_med=0.304317
    [shadow] C1 (B): norm=0.240175 krum=0.224523 mkrum=KEEP tm_trim=0.7138 (lo 0.3753 / hi 0.3385) med_prov=0.0399 d_med=0.236628
    [shadow] C2 (B): norm=0.248929 krum=0.233974 mkrum=KEEP tm_trim=0.7380 (lo 0.3863 / hi 0.3517) med_prov=0.0363 d_med=0.246382
    [shadow] C3 (B): norm=0.341691 krum=0.375446 mkrum=REJECT tm_trim=0.8072 (lo 0.4153 / hi 0.3919) med_prov=0.0273 d_med=0.315107
    [shadow] C4 (B): norm=0.356110 krum=0.393824 mkrum=REJECT tm_trim=0.7916 (lo 0.4086 / hi 0.3830) med_prov=0.0278 d_med=0.321891
    [shadow] C5 (A): norm=0.152282 krum=0.120146 mkrum=KEEP tm_trim=0.0430 (lo 0.0000 / hi 0.0430) med_prov=0.1394 d_med=0.027740
    [shadow] C6 (A): norm=0.152282 krum=0.120146 mkrum=KEEP tm_trim=0.1178 (lo 0.0066 / hi 0.1112) med_prov=0.6998 d_med=0.027740

⏱️  Overhead round 32 (wall-clock s): round 133.98 | broadcast 0.03 | prepare 0.00 | benign train 119.23 [0:30.2 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.93 | eval_local 7.59 (bookkeeping) | unaccounted 0.05
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 32 Results:
  Clean Accuracy: 0.8980
  ΔClean vs prev: +0.0043
  ΔClean vs best: -0.0040
  Global Loss: 0.7013

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1352, std_norm=0.2870, attack_norm=0.1532, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1352, std_norm=0.2870, attack_norm=0.1532, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.156667
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.212, Std Dev: 0.167
    Client 0 (Benign): 0.124
    Client 1 (Benign): 0.098
    Client 2 (Benign): 0.069
    Client 3 (Benign): 0.108
    Client 4 (Benign): 0.140
    Client 5 (Attacker): 0.474
    Client 6 (Attacker): 0.474
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.225877, Std Dev: 0.103818
    Client 0 (Benign): 0.300703
    Client 1 (Benign): 0.269082
    Client 2 (Benign): 0.282901
    Client 3 (Benign): 0.304959
    Client 4 (Benign): 0.298109
    Client 5 (Attacker): 0.062692
    Client 6 (Attacker): 0.062692
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.347377 krum=0.390120 mkrum=KEEP tm_trim=0.7892 (lo 0.4083 / hi 0.3809) med_prov=0.0293 d_med=0.315322
    [shadow] C1 (B): norm=0.245355 krum=0.231717 mkrum=KEEP tm_trim=0.7158 (lo 0.3753 / hi 0.3406) med_prov=0.0386 d_med=0.243378
    [shadow] C2 (B): norm=0.251176 krum=0.242698 mkrum=KEEP tm_trim=0.7451 (lo 0.3887 / hi 0.3564) med_prov=0.0354 d_med=0.254068
    [shadow] C3 (B): norm=0.361998 krum=0.413956 mkrum=REJECT tm_trim=0.8083 (lo 0.4168 / hi 0.3916) med_prov=0.0270 d_med=0.330860
    [shadow] C4 (B): norm=0.357950 krum=0.397454 mkrum=REJECT tm_trim=0.7821 (lo 0.4044 / hi 0.3777) med_prov=0.0290 d_med=0.321263
    [shadow] C5 (A): norm=0.153250 krum=0.127672 mkrum=KEEP tm_trim=0.0379 (lo 0.0000 / hi 0.0379) med_prov=0.1437 d_med=0.028331
    [shadow] C6 (A): norm=0.153250 krum=0.127672 mkrum=KEEP tm_trim=0.1215 (lo 0.0065 / hi 0.1150) med_prov=0.6969 d_med=0.028331

⏱️  Overhead round 33 (wall-clock s): round 134.00 | broadcast 0.03 | prepare 0.00 | benign train 119.23 [0:30.2 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.62 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 33 Results:
  Clean Accuracy: 0.8957
  ΔClean vs prev: -0.0023
  ΔClean vs best: -0.0063
  Global Loss: 0.7655

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1369, std_norm=0.2875, attack_norm=0.1552, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1369, std_norm=0.2875, attack_norm=0.1552, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.156015
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.221, Std Dev: 0.165
    Client 0 (Benign): 0.130
    Client 1 (Benign): 0.121
    Client 2 (Benign): 0.103
    Client 3 (Benign): 0.098
    Client 4 (Benign): 0.129
    Client 5 (Attacker): 0.481
    Client 6 (Attacker): 0.481
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.225425, Std Dev: 0.105109
    Client 0 (Benign): 0.303817
    Client 1 (Benign): 0.261388
    Client 2 (Benign): 0.274292
    Client 3 (Benign): 0.301088
    Client 4 (Benign): 0.314639
    Client 5 (Attacker): 0.061375
    Client 6 (Attacker): 0.061375
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.347892 krum=0.381757 mkrum=KEEP tm_trim=0.7909 (lo 0.4091 / hi 0.3818) med_prov=0.0297 d_med=0.315450
    [shadow] C1 (B): norm=0.243753 krum=0.227178 mkrum=KEEP tm_trim=0.7032 (lo 0.3709 / hi 0.3323) med_prov=0.0406 d_med=0.238087
    [shadow] C2 (B): norm=0.252275 krum=0.236810 mkrum=KEEP tm_trim=0.7354 (lo 0.3851 / hi 0.3503) med_prov=0.0375 d_med=0.247886
    [shadow] C3 (B): norm=0.349767 krum=0.390787 mkrum=REJECT tm_trim=0.8057 (lo 0.4147 / hi 0.3910) med_prov=0.0281 d_med=0.323666
    [shadow] C4 (B): norm=0.375037 krum=0.428064 mkrum=REJECT tm_trim=0.8021 (lo 0.4137 / hi 0.3884) med_prov=0.0267 d_med=0.339122
    [shadow] C5 (A): norm=0.155169 krum=0.122018 mkrum=KEEP tm_trim=0.0456 (lo 0.0000 / hi 0.0456) med_prov=0.1341 d_med=0.028511
    [shadow] C6 (A): norm=0.155169 krum=0.122018 mkrum=KEEP tm_trim=0.1170 (lo 0.0065 / hi 0.1106) med_prov=0.7032 d_med=0.028511

⏱️  Overhead round 34 (wall-clock s): round 134.01 | broadcast 0.03 | prepare 0.00 | benign train 119.23 [0:30.2 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.61 (bookkeeping) | unaccounted 0.06
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 34 Results:
  Clean Accuracy: 0.8980
  ΔClean vs prev: +0.0023
  ΔClean vs best: -0.0040
  Global Loss: 0.7301

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1378, std_norm=0.2897, attack_norm=0.1562, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1378, std_norm=0.2897, attack_norm=0.1562, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.157987
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.219, Std Dev: 0.166
    Client 0 (Benign): 0.114
    Client 1 (Benign): 0.118
    Client 2 (Benign): 0.098
    Client 3 (Benign): 0.091
    Client 4 (Benign): 0.154
    Client 5 (Attacker): 0.480
    Client 6 (Attacker): 0.480
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.227359, Std Dev: 0.105701
    Client 0 (Benign): 0.293349
    Client 1 (Benign): 0.265775
    Client 2 (Benign): 0.278164
    Client 3 (Benign): 0.314651
    Client 4 (Benign): 0.314998
    Client 5 (Attacker): 0.062288
    Client 6 (Attacker): 0.062288
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.328335 krum=0.359105 mkrum=KEEP tm_trim=0.7796 (lo 0.4047 / hi 0.3748) med_prov=0.0312 d_med=0.303235
    [shadow] C1 (B): norm=0.247130 krum=0.231983 mkrum=KEEP tm_trim=0.7091 (lo 0.3730 / hi 0.3361) med_prov=0.0402 d_med=0.241224
    [shadow] C2 (B): norm=0.253913 krum=0.241562 mkrum=KEEP tm_trim=0.7364 (lo 0.3861 / hi 0.3503) med_prov=0.0370 d_med=0.251014
    [shadow] C3 (B): norm=0.365549 krum=0.422752 mkrum=REJECT tm_trim=0.8130 (lo 0.4179 / hi 0.3951) med_prov=0.0260 d_med=0.339190
    [shadow] C4 (B): norm=0.384197 krum=0.434129 mkrum=REJECT tm_trim=0.7998 (lo 0.4115 / hi 0.3883) med_prov=0.0277 d_med=0.340408
    [shadow] C5 (A): norm=0.156219 krum=0.125207 mkrum=KEEP tm_trim=0.0438 (lo 0.0000 / hi 0.0438) med_prov=0.1378 d_med=0.029042
    [shadow] C6 (A): norm=0.156219 krum=0.125207 mkrum=KEEP tm_trim=0.1183 (lo 0.0068 / hi 0.1116) med_prov=0.7001 d_med=0.029042

⏱️  Overhead round 35 (wall-clock s): round 134.19 | broadcast 0.03 | prepare 0.00 | benign train 119.43 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.05 [5:0.0 6:0.0] | aggregate 0.10 | observe 0.00 | eval_global 6.94 | eval_local 7.59 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.04s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 35 Results:
  Clean Accuracy: 0.9020
  ΔClean vs prev: +0.0040
  ΔClean vs best: +0.0000
  Global Loss: 0.7340

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1373, std_norm=0.2912, attack_norm=0.1558, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1373, std_norm=0.2912, attack_norm=0.1558, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.157360
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.215, Std Dev: 0.166
    Client 0 (Benign): 0.112
    Client 1 (Benign): 0.117
    Client 2 (Benign): 0.093
    Client 3 (Benign): 0.082
    Client 4 (Benign): 0.149
    Client 5 (Attacker): 0.476
    Client 6 (Attacker): 0.476
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.228650, Std Dev: 0.106181
    Client 0 (Benign): 0.311028
    Client 1 (Benign): 0.266117
    Client 2 (Benign): 0.280142
    Client 3 (Benign): 0.298809
    Client 4 (Benign): 0.318866
    Client 5 (Attacker): 0.062792
    Client 6 (Attacker): 0.062792
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C0 (B), C4 (B)
    [shadow] C0 (B): norm=0.353882 krum=0.402865 mkrum=REJECT tm_trim=0.7957 (lo 0.4112 / hi 0.3845) med_prov=0.0284 d_med=0.324652
    [shadow] C1 (B): norm=0.246705 krum=0.229207 mkrum=KEEP tm_trim=0.7052 (lo 0.3708 / hi 0.3344) med_prov=0.0389 d_med=0.241289
    [shadow] C2 (B): norm=0.254377 krum=0.240102 mkrum=KEEP tm_trim=0.7306 (lo 0.3819 / hi 0.3487) med_prov=0.0370 d_med=0.252235
    [shadow] C3 (B): norm=0.340330 krum=0.389596 mkrum=KEEP tm_trim=0.8145 (lo 0.4191 / hi 0.3954) med_prov=0.0265 d_med=0.319251
    [shadow] C4 (B): norm=0.389510 krum=0.447335 mkrum=REJECT tm_trim=0.7971 (lo 0.4104 / hi 0.3867) med_prov=0.0261 d_med=0.346144
    [shadow] C5 (A): norm=0.155819 krum=0.125772 mkrum=KEEP tm_trim=0.0437 (lo 0.0000 / hi 0.0437) med_prov=0.1417 d_med=0.028976
    [shadow] C6 (A): norm=0.155819 krum=0.125772 mkrum=KEEP tm_trim=0.1132 (lo 0.0065 / hi 0.1067) med_prov=0.7014 d_med=0.028976

⏱️  Overhead round 36 (wall-clock s): round 134.04 | broadcast 0.03 | prepare 0.00 | benign train 119.28 [0:30.3 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.59 (bookkeeping) | unaccounted 0.05
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 36 Results:
  Clean Accuracy: 0.9017
  ΔClean vs prev: -0.0003
  ΔClean vs best: -0.0003
  Global Loss: 0.7376

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1373, std_norm=0.2872, attack_norm=0.1554, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1373, std_norm=0.2872, attack_norm=0.1554, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.157053
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.221, Std Dev: 0.165
    Client 0 (Benign): 0.105
    Client 1 (Benign): 0.119
    Client 2 (Benign): 0.105
    Client 3 (Benign): 0.111
    Client 4 (Benign): 0.143
    Client 5 (Attacker): 0.481
    Client 6 (Attacker): 0.481
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.225649, Std Dev: 0.104583
    Client 0 (Benign): 0.287661
    Client 1 (Benign): 0.263505
    Client 2 (Benign): 0.280463
    Client 3 (Benign): 0.303882
    Client 4 (Benign): 0.319426
    Client 5 (Attacker): 0.062301
    Client 6 (Attacker): 0.062301
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.320529 krum=0.349751 mkrum=KEEP tm_trim=0.7872 (lo 0.4072 / hi 0.3800) med_prov=0.0298 d_med=0.298525
    [shadow] C1 (B): norm=0.243812 krum=0.226789 mkrum=KEEP tm_trim=0.7098 (lo 0.3734 / hi 0.3363) med_prov=0.0392 d_med=0.238784
    [shadow] C2 (B): norm=0.258532 krum=0.240357 mkrum=KEEP tm_trim=0.7399 (lo 0.3867 / hi 0.3532) med_prov=0.0362 d_med=0.252474
    [shadow] C3 (B): norm=0.356701 krum=0.399933 mkrum=REJECT tm_trim=0.8010 (lo 0.4126 / hi 0.3884) med_prov=0.0272 d_med=0.326941
    [shadow] C4 (B): norm=0.387901 krum=0.450574 mkrum=REJECT tm_trim=0.8042 (lo 0.4139 / hi 0.3903) med_prov=0.0255 d_med=0.346163
    [shadow] C5 (A): norm=0.155361 krum=0.124553 mkrum=KEEP tm_trim=0.0459 (lo 0.0000 / hi 0.0459) med_prov=0.1378 d_med=0.028261
    [shadow] C6 (A): norm=0.155361 krum=0.124553 mkrum=KEEP tm_trim=0.1120 (lo 0.0062 / hi 0.1058) med_prov=0.7043 d_med=0.028261

⏱️  Overhead round 37 (wall-clock s): round 134.09 | broadcast 0.02 | prepare 0.00 | benign train 119.33 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.61 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 37 Results:
  Clean Accuracy: 0.9027
  ΔClean vs prev: +0.0010
  ΔClean vs best: +0.0000
  Global Loss: 0.7702

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1402, std_norm=0.3004, attack_norm=0.1595, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1402, std_norm=0.3004, attack_norm=0.1595, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.163636
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.211, Std Dev: 0.166
    Client 0 (Benign): 0.123
    Client 1 (Benign): 0.106
    Client 2 (Benign): 0.073
    Client 3 (Benign): 0.087
    Client 4 (Benign): 0.143
    Client 5 (Attacker): 0.470
    Client 6 (Attacker): 0.470
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.235153, Std Dev: 0.110636
    Client 0 (Benign): 0.304105
    Client 1 (Benign): 0.264802
    Client 2 (Benign): 0.281379
    Client 3 (Benign): 0.328591
    Client 4 (Benign): 0.338773
    Client 5 (Attacker): 0.064209
    Client 6 (Attacker): 0.064209
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.341189 krum=0.372183 mkrum=KEEP tm_trim=0.7785 (lo 0.4041 / hi 0.3745) med_prov=0.0324 d_med=0.311804
    [shadow] C1 (B): norm=0.239408 krum=0.227758 mkrum=KEEP tm_trim=0.6911 (lo 0.3656 / hi 0.3254) med_prov=0.0440 d_med=0.239556
    [shadow] C2 (B): norm=0.247136 krum=0.240872 mkrum=KEEP tm_trim=0.7286 (lo 0.3828 / hi 0.3458) med_prov=0.0395 d_med=0.252778
    [shadow] C3 (B): norm=0.380658 krum=0.453135 mkrum=REJECT tm_trim=0.8190 (lo 0.4216 / hi 0.3974) med_prov=0.0265 d_med=0.352837
    [shadow] C4 (B): norm=0.412000 krum=0.494258 mkrum=REJECT tm_trim=0.8144 (lo 0.4189 / hi 0.3954) med_prov=0.0260 d_med=0.366455
    [shadow] C5 (A): norm=0.159495 krum=0.125973 mkrum=KEEP tm_trim=0.0499 (lo 0.0000 / hi 0.0499) med_prov=0.1323 d_med=0.030935
    [shadow] C6 (A): norm=0.159495 krum=0.125973 mkrum=KEEP tm_trim=0.1185 (lo 0.0070 / hi 0.1116) med_prov=0.6993 d_med=0.030935

⏱️  Overhead round 38 (wall-clock s): round 134.01 | broadcast 0.03 | prepare 0.00 | benign train 119.28 [0:30.3 1:11.0 2:9.7 3:33.7 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.58 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 38 Results:
  Clean Accuracy: 0.8997
  ΔClean vs prev: -0.0030
  ΔClean vs best: -0.0030
  Global Loss: 0.7999

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1380, std_norm=0.2826, attack_norm=0.1555, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1380, std_norm=0.2826, attack_norm=0.1555, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.157425
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.229, Std Dev: 0.165
    Client 0 (Benign): 0.141
    Client 1 (Benign): 0.126
    Client 2 (Benign): 0.099
    Client 3 (Benign): 0.120
    Client 4 (Benign): 0.138
    Client 5 (Attacker): 0.489
    Client 6 (Attacker): 0.489
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.222033, Std Dev: 0.102668
    Client 0 (Benign): 0.294882
    Client 1 (Benign): 0.259497
    Client 2 (Benign): 0.278260
    Client 3 (Benign): 0.305371
    Client 4 (Benign): 0.293994
    Client 5 (Attacker): 0.061114
    Client 6 (Attacker): 0.061114
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.341253 krum=0.364413 mkrum=KEEP tm_trim=0.7941 (lo 0.4098 / hi 0.3843) med_prov=0.0293 d_med=0.307302
    [shadow] C1 (B): norm=0.241519 krum=0.223025 mkrum=KEEP tm_trim=0.7075 (lo 0.3719 / hi 0.3356) med_prov=0.0406 d_med=0.235504
    [shadow] C2 (B): norm=0.254275 krum=0.238224 mkrum=KEEP tm_trim=0.7417 (lo 0.3882 / hi 0.3535) med_prov=0.0364 d_med=0.251202
    [shadow] C3 (B): norm=0.364136 krum=0.410542 mkrum=REJECT tm_trim=0.8112 (lo 0.4173 / hi 0.3939) med_prov=0.0265 d_med=0.331060
    [shadow] C4 (B): norm=0.349882 krum=0.382180 mkrum=REJECT tm_trim=0.7829 (lo 0.4062 / hi 0.3767) med_prov=0.0296 d_med=0.316071
    [shadow] C5 (A): norm=0.155528 krum=0.122188 mkrum=KEEP tm_trim=0.0386 (lo 0.0000 / hi 0.0386) med_prov=0.1410 d_med=0.027976
    [shadow] C6 (A): norm=0.155528 krum=0.122188 mkrum=KEEP tm_trim=0.1239 (lo 0.0065 / hi 0.1174) med_prov=0.6965 d_med=0.027976

⏱️  Overhead round 39 (wall-clock s): round 134.07 | broadcast 0.03 | prepare 0.00 | benign train 119.31 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.05 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.60 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.01s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 39 Results:
  Clean Accuracy: 0.9063
  ΔClean vs prev: +0.0067
  ΔClean vs best: +0.0000
  Global Loss: 0.7620

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1423, std_norm=0.2895, attack_norm=0.1601, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1423, std_norm=0.2895, attack_norm=0.1601, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.163718
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.230, Std Dev: 0.165
    Client 0 (Benign): 0.129
    Client 1 (Benign): 0.109
    Client 2 (Benign): 0.106
    Client 3 (Benign): 0.120
    Client 4 (Benign): 0.166
    Client 5 (Attacker): 0.489
    Client 6 (Attacker): 0.489
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.227106, Std Dev: 0.105726
    Client 0 (Benign): 0.304086
    Client 1 (Benign): 0.267025
    Client 2 (Benign): 0.272583
    Client 3 (Benign): 0.315165
    Client 4 (Benign): 0.306926
    Client 5 (Attacker): 0.061981
    Client 6 (Attacker): 0.061981
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.347237 krum=0.383425 mkrum=KEEP tm_trim=0.7914 (lo 0.4091 / hi 0.3823) med_prov=0.0290 d_med=0.316249
    [shadow] C1 (B): norm=0.243317 krum=0.230756 mkrum=KEEP tm_trim=0.7088 (lo 0.3723 / hi 0.3365) med_prov=0.0390 d_med=0.242598
    [shadow] C2 (B): norm=0.247119 krum=0.234374 mkrum=KEEP tm_trim=0.7277 (lo 0.3817 / hi 0.3460) med_prov=0.0380 d_med=0.246159
    [shadow] C3 (B): norm=0.374046 krum=0.429311 mkrum=REJECT tm_trim=0.8130 (lo 0.4193 / hi 0.3938) med_prov=0.0264 d_med=0.340179
    [shadow] C4 (B): norm=0.373645 krum=0.405474 mkrum=REJECT tm_trim=0.7994 (lo 0.4114 / hi 0.3881) med_prov=0.0272 d_med=0.329330
    [shadow] C5 (A): norm=0.160093 krum=0.123340 mkrum=KEEP tm_trim=0.0402 (lo 0.0000 / hi 0.0402) med_prov=0.1408 d_med=0.028485
    [shadow] C6 (A): norm=0.160093 krum=0.123340 mkrum=KEEP tm_trim=0.1194 (lo 0.0062 / hi 0.1132) med_prov=0.6997 d_med=0.028485

⏱️  Overhead round 40 (wall-clock s): round 134.07 | broadcast 0.03 | prepare 0.00 | benign train 119.30 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.62 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 40 Results:
  Clean Accuracy: 0.9003
  ΔClean vs prev: -0.0060
  ΔClean vs best: -0.0060
  Global Loss: 0.7908

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1344, std_norm=0.2782, attack_norm=0.1517, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1344, std_norm=0.2782, attack_norm=0.1517, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.152760
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.224, Std Dev: 0.167
    Client 0 (Benign): 0.129
    Client 1 (Benign): 0.120
    Client 2 (Benign): 0.101
    Client 3 (Benign): 0.081
    Client 4 (Benign): 0.165
    Client 5 (Attacker): 0.484
    Client 6 (Attacker): 0.484
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.218768, Std Dev: 0.100801
    Client 0 (Benign): 0.292299
    Client 1 (Benign): 0.262253
    Client 2 (Benign): 0.273327
    Client 3 (Benign): 0.285407
    Client 4 (Benign): 0.297468
    Client 5 (Attacker): 0.060312
    Client 6 (Attacker): 0.060312
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C0 (B), C4 (B)
    [shadow] C0 (B): norm=0.336531 krum=0.365976 mkrum=REJECT tm_trim=0.8025 (lo 0.4141 / hi 0.3884) med_prov=0.0280 d_med=0.305275
    [shadow] C1 (B): norm=0.245874 krum=0.225565 mkrum=KEEP tm_trim=0.7129 (lo 0.3734 / hi 0.3395) med_prov=0.0383 d_med=0.238483
    [shadow] C2 (B): norm=0.251968 krum=0.233777 mkrum=KEEP tm_trim=0.7450 (lo 0.3895 / hi 0.3555) med_prov=0.0350 d_med=0.246726
    [shadow] C3 (B): norm=0.326615 krum=0.362363 mkrum=KEEP tm_trim=0.7975 (lo 0.4113 / hi 0.3862) med_prov=0.0286 d_med=0.307993
    [shadow] C4 (B): norm=0.365157 krum=0.395266 mkrum=REJECT tm_trim=0.7839 (lo 0.4053 / hi 0.3786) med_prov=0.0282 d_med=0.322089
    [shadow] C5 (A): norm=0.151746 krum=0.121159 mkrum=KEEP tm_trim=0.0409 (lo 0.0000 / hi 0.0409) med_prov=0.1415 d_med=0.027293
    [shadow] C6 (A): norm=0.151746 krum=0.121159 mkrum=KEEP tm_trim=0.1172 (lo 0.0064 / hi 0.1109) med_prov=0.7004 d_med=0.027293

⏱️  Overhead round 41 (wall-clock s): round 134.20 | broadcast 0.03 | prepare 0.00 | benign train 119.37 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.05 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.65 (bookkeeping) | unaccounted 0.05
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.03s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 41 Results:
  Clean Accuracy: 0.9053
  ΔClean vs prev: +0.0050
  ΔClean vs best: -0.0010
  Global Loss: 0.7582

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1381, std_norm=0.2880, attack_norm=0.1561, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1381, std_norm=0.2880, attack_norm=0.1561, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.158798
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.221, Std Dev: 0.166
    Client 0 (Benign): 0.124
    Client 1 (Benign): 0.114
    Client 2 (Benign): 0.101
    Client 3 (Benign): 0.088
    Client 4 (Benign): 0.161
    Client 5 (Attacker): 0.481
    Client 6 (Attacker): 0.481
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.226130, Std Dev: 0.104932
    Client 0 (Benign): 0.297975
    Client 1 (Benign): 0.266401
    Client 2 (Benign): 0.272361
    Client 3 (Benign): 0.311858
    Client 4 (Benign): 0.309992
    Client 5 (Attacker): 0.062160
    Client 6 (Attacker): 0.062160
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.339203 krum=0.367654 mkrum=KEEP tm_trim=0.7897 (lo 0.4074 / hi 0.3823) med_prov=0.0296 d_med=0.309452
    [shadow] C1 (B): norm=0.244873 krum=0.224679 mkrum=KEEP tm_trim=0.7134 (lo 0.3752 / hi 0.3381) med_prov=0.0392 d_med=0.241411
    [shadow] C2 (B): norm=0.245954 krum=0.228350 mkrum=KEEP tm_trim=0.7282 (lo 0.3817 / hi 0.3465) med_prov=0.0375 d_med=0.245040
    [shadow] C3 (B): norm=0.361422 krum=0.421262 mkrum=REJECT tm_trim=0.8211 (lo 0.4221 / hi 0.3991) med_prov=0.0245 d_med=0.335697
    [shadow] C4 (B): norm=0.379286 krum=0.423238 mkrum=REJECT tm_trim=0.7890 (lo 0.4073 / hi 0.3817) med_prov=0.0278 d_med=0.334843
    [shadow] C5 (A): norm=0.156111 krum=0.122047 mkrum=KEEP tm_trim=0.0406 (lo 0.0000 / hi 0.0406) med_prov=0.1436 d_med=0.028120
    [shadow] C6 (A): norm=0.156111 krum=0.122047 mkrum=KEEP tm_trim=0.1179 (lo 0.0063 / hi 0.1117) med_prov=0.6978 d_med=0.028120

⏱️  Overhead round 42 (wall-clock s): round 134.10 | broadcast 0.03 | prepare 0.00 | benign train 119.31 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.12 | observe 0.00 | eval_global 6.94 | eval_local 7.62 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 42 Results:
  Clean Accuracy: 0.9013
  ΔClean vs prev: -0.0040
  ΔClean vs best: -0.0050
  Global Loss: 0.7950

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1408, std_norm=0.2860, attack_norm=0.1582, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1408, std_norm=0.2860, attack_norm=0.1582, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.160845
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.232, Std Dev: 0.164
    Client 0 (Benign): 0.144
    Client 1 (Benign): 0.126
    Client 2 (Benign): 0.112
    Client 3 (Benign): 0.111
    Client 4 (Benign): 0.149
    Client 5 (Attacker): 0.491
    Client 6 (Attacker): 0.491
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.224480, Std Dev: 0.104396
    Client 0 (Benign): 0.299126
    Client 1 (Benign): 0.262520
    Client 2 (Benign): 0.271292
    Client 3 (Benign): 0.299265
    Client 4 (Benign): 0.316072
    Client 5 (Attacker): 0.061543
    Client 6 (Attacker): 0.061543
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.346987 krum=0.374812 mkrum=KEEP tm_trim=0.7890 (lo 0.4083 / hi 0.3807) med_prov=0.0296 d_med=0.311832
    [shadow] C1 (B): norm=0.242400 krum=0.219880 mkrum=KEEP tm_trim=0.7085 (lo 0.3720 / hi 0.3365) med_prov=0.0391 d_med=0.238034
    [shadow] C2 (B): norm=0.246985 krum=0.226010 mkrum=KEEP tm_trim=0.7305 (lo 0.3826 / hi 0.3479) med_prov=0.0362 d_med=0.244093
    [shadow] C3 (B): norm=0.348449 krum=0.386251 mkrum=REJECT tm_trim=0.8095 (lo 0.4162 / hi 0.3932) med_prov=0.0265 d_med=0.320804
    [shadow] C4 (B): norm=0.382880 krum=0.436000 mkrum=REJECT tm_trim=0.8060 (lo 0.4146 / hi 0.3915) med_prov=0.0251 d_med=0.341544
    [shadow] C5 (A): norm=0.158210 krum=0.120036 mkrum=KEEP tm_trim=0.0451 (lo 0.0000 / hi 0.0451) med_prov=0.1398 d_med=0.028141
    [shadow] C6 (A): norm=0.158210 krum=0.120036 mkrum=KEEP tm_trim=0.1114 (lo 0.0063 / hi 0.1051) med_prov=0.7037 d_med=0.028141

⏱️  Overhead round 43 (wall-clock s): round 134.09 | broadcast 0.03 | prepare 0.00 | benign train 119.32 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.62 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 43 Results:
  Clean Accuracy: 0.9083
  ΔClean vs prev: +0.0070
  ΔClean vs best: +0.0000
  Global Loss: 0.7726

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1359, std_norm=0.2828, attack_norm=0.1535, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1359, std_norm=0.2828, attack_norm=0.1535, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.154665
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.223, Std Dev: 0.165
    Client 0 (Benign): 0.135
    Client 1 (Benign): 0.118
    Client 2 (Benign): 0.108
    Client 3 (Benign): 0.088
    Client 4 (Benign): 0.145
    Client 5 (Attacker): 0.483
    Client 6 (Attacker): 0.483
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.222148, Std Dev: 0.102807
    Client 0 (Benign): 0.298943
    Client 1 (Benign): 0.264046
    Client 2 (Benign): 0.271016
    Client 3 (Benign): 0.295448
    Client 4 (Benign): 0.303586
    Client 5 (Attacker): 0.060998
    Client 6 (Attacker): 0.060998
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.345032 krum=0.375629 mkrum=KEEP tm_trim=0.7852 (lo 0.4050 / hi 0.3802) med_prov=0.0284 d_med=0.311755
    [shadow] C1 (B): norm=0.245268 krum=0.224189 mkrum=KEEP tm_trim=0.7124 (lo 0.3737 / hi 0.3388) med_prov=0.0375 d_med=0.239844
    [shadow] C2 (B): norm=0.249430 krum=0.229158 mkrum=KEEP tm_trim=0.7318 (lo 0.3833 / hi 0.3485) med_prov=0.0359 d_med=0.244779
    [shadow] C3 (B): norm=0.339767 krum=0.382475 mkrum=REJECT tm_trim=0.8154 (lo 0.4184 / hi 0.3970) med_prov=0.0248 d_med=0.317624
    [shadow] C4 (B): norm=0.367727 krum=0.407567 mkrum=REJECT tm_trim=0.8029 (lo 0.4134 / hi 0.3895) med_prov=0.0258 d_med=0.328270
    [shadow] C5 (A): norm=0.153459 krum=0.120802 mkrum=KEEP tm_trim=0.0403 (lo 0.0000 / hi 0.0403) med_prov=0.1419 d_med=0.027150
    [shadow] C6 (A): norm=0.153459 krum=0.120802 mkrum=KEEP tm_trim=0.1121 (lo 0.0062 / hi 0.1059) med_prov=0.7057 d_med=0.027150

⏱️  Overhead round 44 (wall-clock s): round 134.05 | broadcast 0.03 | prepare 0.00 | benign train 119.30 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.60 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 44 Results:
  Clean Accuracy: 0.9040
  ΔClean vs prev: -0.0043
  ΔClean vs best: -0.0043
  Global Loss: 0.7910

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1454, std_norm=0.2941, attack_norm=0.1633, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1454, std_norm=0.2941, attack_norm=0.1633, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.166110
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.234, Std Dev: 0.164
    Client 0 (Benign): 0.140
    Client 1 (Benign): 0.135
    Client 2 (Benign): 0.109
    Client 3 (Benign): 0.117
    Client 4 (Benign): 0.153
    Client 5 (Attacker): 0.492
    Client 6 (Attacker): 0.492
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.230707, Std Dev: 0.107420
    Client 0 (Benign): 0.314299
    Client 1 (Benign): 0.266472
    Client 2 (Benign): 0.279598
    Client 3 (Benign): 0.318661
    Client 4 (Benign): 0.309623
    Client 5 (Attacker): 0.063147
    Client 6 (Attacker): 0.063147
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.364013 krum=0.411999 mkrum=KEEP tm_trim=0.8102 (lo 0.4163 / hi 0.3939) med_prov=0.0261 d_med=0.327599
    [shadow] C1 (B): norm=0.247056 krum=0.227046 mkrum=KEEP tm_trim=0.7025 (lo 0.3700 / hi 0.3326) med_prov=0.0394 d_med=0.241528
    [shadow] C2 (B): norm=0.252741 krum=0.237284 mkrum=KEEP tm_trim=0.7268 (lo 0.3810 / hi 0.3457) med_prov=0.0371 d_med=0.252072
    [shadow] C3 (B): norm=0.375481 krum=0.435935 mkrum=REJECT tm_trim=0.8240 (lo 0.4231 / hi 0.4009) med_prov=0.0239 d_med=0.342747
    [shadow] C4 (B): norm=0.373629 krum=0.420220 mkrum=REJECT tm_trim=0.7815 (lo 0.4034 / hi 0.3781) med_prov=0.0285 d_med=0.333239
    [shadow] C5 (A): norm=0.163324 krum=0.125624 mkrum=KEEP tm_trim=0.0369 (lo 0.0000 / hi 0.0369) med_prov=0.1460 d_med=0.028308
    [shadow] C6 (A): norm=0.163324 krum=0.125624 mkrum=KEEP tm_trim=0.1181 (lo 0.0062 / hi 0.1119) med_prov=0.6990 d_med=0.028308

⏱️  Overhead round 45 (wall-clock s): round 134.08 | broadcast 0.03 | prepare 0.00 | benign train 119.33 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.60 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 45 Results:
  Clean Accuracy: 0.9050
  ΔClean vs prev: +0.0010
  ΔClean vs best: -0.0033
  Global Loss: 0.8047

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1421, std_norm=0.2940, attack_norm=0.1606, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1421, std_norm=0.2940, attack_norm=0.1606, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.164262
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.224, Std Dev: 0.165
    Client 0 (Benign): 0.143
    Client 1 (Benign): 0.117
    Client 2 (Benign): 0.090
    Client 3 (Benign): 0.116
    Client 4 (Benign): 0.137
    Client 5 (Attacker): 0.483
    Client 6 (Attacker): 0.483
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.230878, Std Dev: 0.107230
    Client 0 (Benign): 0.299396
    Client 1 (Benign): 0.271483
    Client 2 (Benign): 0.278399
    Client 3 (Benign): 0.325625
    Client 4 (Benign): 0.314102
    Client 5 (Attacker): 0.063572
    Client 6 (Attacker): 0.063572
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.344072 krum=0.373422 mkrum=KEEP tm_trim=0.7813 (lo 0.4047 / hi 0.3766) med_prov=0.0320 d_med=0.309904
    [shadow] C1 (B): norm=0.248819 krum=0.231887 mkrum=KEEP tm_trim=0.7106 (lo 0.3742 / hi 0.3363) med_prov=0.0403 d_med=0.245002
    [shadow] C2 (B): norm=0.246710 krum=0.236641 mkrum=KEEP tm_trim=0.7286 (lo 0.3822 / hi 0.3464) med_prov=0.0378 d_med=0.249831
    [shadow] C3 (B): norm=0.387972 krum=0.466240 mkrum=REJECT tm_trim=0.8164 (lo 0.4191 / hi 0.3973) med_prov=0.0261 d_med=0.352804
    [shadow] C4 (B): norm=0.376291 krum=0.433059 mkrum=REJECT tm_trim=0.7989 (lo 0.4129 / hi 0.3859) med_prov=0.0281 d_med=0.338345
    [shadow] C5 (A): norm=0.160579 krum=0.126875 mkrum=KEEP tm_trim=0.0425 (lo 0.0000 / hi 0.0425) med_prov=0.1404 d_med=0.030063
    [shadow] C6 (A): norm=0.160579 krum=0.126875 mkrum=KEEP tm_trim=0.1218 (lo 0.0069 / hi 0.1149) med_prov=0.6953 d_med=0.030063

⏱️  Overhead round 46 (wall-clock s): round 134.06 | broadcast 0.03 | prepare 0.00 | benign train 119.34 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.56 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 46 Results:
  Clean Accuracy: 0.9063
  ΔClean vs prev: +0.0013
  ΔClean vs best: -0.0020
  Global Loss: 0.7900

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1359, std_norm=0.2850, attack_norm=0.1538, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1359, std_norm=0.2850, attack_norm=0.1538, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.155807
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.216, Std Dev: 0.167
    Client 0 (Benign): 0.143
    Client 1 (Benign): 0.102
    Client 2 (Benign): 0.080
    Client 3 (Benign): 0.084
    Client 4 (Benign): 0.150
    Client 5 (Attacker): 0.478
    Client 6 (Attacker): 0.478
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.223949, Std Dev: 0.103466
    Client 0 (Benign): 0.311126
    Client 1 (Benign): 0.270975
    Client 2 (Benign): 0.277763
    Client 3 (Benign): 0.282620
    Client 4 (Benign): 0.301931
    Client 5 (Attacker): 0.061614
    Client 6 (Attacker): 0.061614
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C0 (B), C4 (B)
    [shadow] C0 (B): norm=0.367236 krum=0.417316 mkrum=REJECT tm_trim=0.7956 (lo 0.4095 / hi 0.3861) med_prov=0.0268 d_med=0.327975
    [shadow] C1 (B): norm=0.250520 krum=0.238617 mkrum=KEEP tm_trim=0.7220 (lo 0.3772 / hi 0.3448) med_prov=0.0361 d_med=0.246685
    [shadow] C2 (B): norm=0.250683 krum=0.243314 mkrum=KEEP tm_trim=0.7388 (lo 0.3859 / hi 0.3529) med_prov=0.0346 d_med=0.251416
    [shadow] C3 (B): norm=0.322225 krum=0.359477 mkrum=KEEP tm_trim=0.8073 (lo 0.4163 / hi 0.3910) med_prov=0.0268 d_med=0.303137
    [shadow] C4 (B): norm=0.366163 krum=0.406250 mkrum=REJECT tm_trim=0.7850 (lo 0.4050 / hi 0.3800) med_prov=0.0269 d_med=0.326136
    [shadow] C5 (A): norm=0.153776 krum=0.127328 mkrum=KEEP tm_trim=0.0376 (lo 0.0000 / hi 0.0376) med_prov=0.1467 d_med=0.027124
    [shadow] C6 (A): norm=0.153776 krum=0.127328 mkrum=KEEP tm_trim=0.1137 (lo 0.0061 / hi 0.1077) med_prov=0.7020 d_med=0.027124

⏱️  Overhead round 47 (wall-clock s): round 134.09 | broadcast 0.03 | prepare 0.00 | benign train 119.34 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.60 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 47 Results:
  Clean Accuracy: 0.9020
  ΔClean vs prev: -0.0043
  ΔClean vs best: -0.0063
  Global Loss: 0.8606

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1464, std_norm=0.3022, attack_norm=0.1651, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1464, std_norm=0.3022, attack_norm=0.1651, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.169406
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.223, Std Dev: 0.165
    Client 0 (Benign): 0.127
    Client 1 (Benign): 0.109
    Client 2 (Benign): 0.090
    Client 3 (Benign): 0.115
    Client 4 (Benign): 0.155
    Client 5 (Attacker): 0.482
    Client 6 (Attacker): 0.482
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.237154, Std Dev: 0.110613
    Client 0 (Benign): 0.313780
    Client 1 (Benign): 0.277664
    Client 2 (Benign): 0.289550
    Client 3 (Benign): 0.298216
    Client 4 (Benign): 0.349912
    Client 5 (Attacker): 0.065476
    Client 6 (Attacker): 0.065476
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C0 (B), C4 (B)
    [shadow] C0 (B): norm=0.356317 krum=0.406665 mkrum=REJECT tm_trim=0.7900 (lo 0.4087 / hi 0.3813) med_prov=0.0289 d_med=0.324599
    [shadow] C1 (B): norm=0.251913 krum=0.247615 mkrum=KEEP tm_trim=0.7147 (lo 0.3741 / hi 0.3406) med_prov=0.0380 d_med=0.250927
    [shadow] C2 (B): norm=0.259547 krum=0.257220 mkrum=KEEP tm_trim=0.7352 (lo 0.3846 / hi 0.3506) med_prov=0.0362 d_med=0.260567
    [shadow] C3 (B): norm=0.344009 krum=0.384349 mkrum=KEEP tm_trim=0.7848 (lo 0.4060 / hi 0.3787) med_prov=0.0310 d_med=0.317493
    [shadow] C4 (B): norm=0.433281 krum=0.545942 mkrum=REJECT tm_trim=0.8181 (lo 0.4201 / hi 0.3980) med_prov=0.0232 d_med=0.382691
    [shadow] C5 (A): norm=0.165066 krum=0.135240 mkrum=KEEP tm_trim=0.0527 (lo 0.0000 / hi 0.0527) med_prov=0.1321 d_med=0.030057
    [shadow] C6 (A): norm=0.165066 krum=0.135240 mkrum=KEEP tm_trim=0.1045 (lo 0.0065 / hi 0.0980) med_prov=0.7107 d_med=0.030057

⏱️  Overhead round 48 (wall-clock s): round 134.01 | broadcast 0.03 | prepare 0.00 | benign train 119.28 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.58 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 48 Results:
  Clean Accuracy: 0.9080
  ΔClean vs prev: +0.0060
  ΔClean vs best: -0.0003
  Global Loss: 0.8501

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1498, std_norm=0.3029, attack_norm=0.1682, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1498, std_norm=0.3029, attack_norm=0.1682, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.172176
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.236, Std Dev: 0.163
    Client 0 (Benign): 0.124
    Client 1 (Benign): 0.129
    Client 2 (Benign): 0.128
    Client 3 (Benign): 0.129
    Client 4 (Benign): 0.156
    Client 5 (Attacker): 0.492
    Client 6 (Attacker): 0.492
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.237181, Std Dev: 0.111751
    Client 0 (Benign): 0.299553
    Client 1 (Benign): 0.272171
    Client 2 (Benign): 0.282906
    Client 3 (Benign): 0.360767
    Client 4 (Benign): 0.314089
    Client 5 (Attacker): 0.065389
    Client 6 (Attacker): 0.065389
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C3 (B), C4 (B)
    [shadow] C0 (B): norm=0.333481 krum=0.368952 mkrum=KEEP tm_trim=0.7863 (lo 0.4085 / hi 0.3778) med_prov=0.0330 d_med=0.308042
    [shadow] C1 (B): norm=0.246783 krum=0.229449 mkrum=KEEP tm_trim=0.6966 (lo 0.3672 / hi 0.3293) med_prov=0.0422 d_med=0.244641
    [shadow] C2 (B): norm=0.257313 krum=0.237741 mkrum=KEEP tm_trim=0.7271 (lo 0.3814 / hi 0.3457) med_prov=0.0379 d_med=0.252356
    [shadow] C3 (B): norm=0.438017 krum=0.563266 mkrum=REJECT tm_trim=0.8298 (lo 0.4260 / hi 0.4038) med_prov=0.0236 d_med=0.393948
    [shadow] C4 (B): norm=0.375121 krum=0.422356 mkrum=REJECT tm_trim=0.7939 (lo 0.4097 / hi 0.3842) med_prov=0.0296 d_med=0.334315
    [shadow] C5 (A): norm=0.168220 krum=0.128724 mkrum=KEEP tm_trim=0.0386 (lo 0.0000 / hi 0.0386) med_prov=0.1451 d_med=0.032094
    [shadow] C6 (A): norm=0.168220 krum=0.128724 mkrum=KEEP tm_trim=0.1277 (lo 0.0072 / hi 0.1204) med_prov=0.6886 d_med=0.032094

⏱️  Overhead round 49 (wall-clock s): round 134.09 | broadcast 0.03 | prepare 0.00 | benign train 119.33 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.6] | attack 0.03 [5:0.0 6:0.0] | aggregate 0.11 | observe 0.00 | eval_global 6.94 | eval_local 7.62 (bookkeeping) | unaccounted 0.04
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 49 Results:
  Clean Accuracy: 0.9100
  ΔClean vs prev: +0.0020
  ΔClean vs best: +0.0000
  Global Loss: 0.7844

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
    [ALIE Attacker 5] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1436, std_norm=0.2858, attack_norm=0.1608, num_benign=5, param_dim=1084928
  ⚠️ Triggering camouflage logic for Client 6
    [ALIE Attacker 6] Generated attack (LoRA mode): z_max=0.2533, mean_norm=0.1436, std_norm=0.2858, attack_norm=0.1608, num_benign=5, param_dim=1084928

📊 Phase 4: Model Aggregation
  📊 Standard FedAvg: Aggregated 7/7 updates
  🔧 Server Learning Rate: 1.0
  📐 Aggregated update norm: 0.162599
  📊 Computing cosine similarities (pairwise: local vs local, no self)
  📈 Cosine Similarity (pairwise mean) - Mean: 0.239, Std Dev: 0.165
    Client 0 (Benign): 0.169
    Client 1 (Benign): 0.139
    Client 2 (Benign): 0.109
    Client 3 (Benign): 0.115
    Client 4 (Benign): 0.147
    Client 5 (Attacker): 0.498
    Client 6 (Attacker): 0.498
  📊 Computing Euclidean distances (weighted aggregation, matches camouflage optimization)
  📈 Euclidean Distance - Mean: 0.224230, Std Dev: 0.104291
    Client 0 (Benign): 0.313066
    Client 1 (Benign): 0.263016
    Client 2 (Benign): 0.275397
    Client 3 (Benign): 0.296098
    Client 4 (Benign): 0.299870
    Client 5 (Attacker): 0.061080
    Client 6 (Attacker): 0.061080
  🛡️ Shadow defenses (computed only, NOT applied; n=7, f=2, k=3, m=5, beta=2)
    [shadow] Krum selected: C5 (A)
    [shadow] Multi-Krum rejected: C0 (B), C4 (B)
    [shadow] C0 (B): norm=0.371051 krum=0.407795 mkrum=REJECT tm_trim=0.8010 (lo 0.4135 / hi 0.3875) med_prov=0.0272 d_med=0.326952
    [shadow] C1 (B): norm=0.247981 krum=0.229866 mkrum=KEEP tm_trim=0.7193 (lo 0.3770 / hi 0.3422) med_prov=0.0382 d_med=0.239673
    [shadow] C2 (B): norm=0.251748 krum=0.239314 mkrum=KEEP tm_trim=0.7386 (lo 0.3870 / hi 0.3515) med_prov=0.0360 d_med=0.249487
    [shadow] C3 (B): norm=0.346542 krum=0.385570 mkrum=KEEP tm_trim=0.8007 (lo 0.4118 / hi 0.3889) med_prov=0.0279 d_med=0.318788
    [shadow] C4 (B): norm=0.359060 krum=0.396566 mkrum=REJECT tm_trim=0.7826 (lo 0.4043 / hi 0.3783) med_prov=0.0285 d_med=0.322732
    [shadow] C5 (A): norm=0.160829 krum=0.123305 mkrum=KEEP tm_trim=0.0381 (lo 0.0000 / hi 0.0381) med_prov=0.1422 d_med=0.027849
    [shadow] C6 (A): norm=0.160829 krum=0.123305 mkrum=KEEP tm_trim=0.1197 (lo 0.0063 / hi 0.1134) med_prov=0.7000 d_med=0.027849

⏱️  Overhead round 50 (wall-clock s): round 134.19 | broadcast 0.02 | prepare 0.00 | benign train 119.45 [0:30.3 1:11.0 2:9.7 3:33.8 4:34.7] | attack 0.04 [5:0.0 6:0.0] | aggregate 0.13 | observe 0.00 | eval_global 6.94 | eval_local 7.58 (bookkeeping) | unaccounted 0.03
    [Attacker 5] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Attacker 6] no stage report (not an AugMP attacker or no benign updates); wall 0.02s
    [Benign fine-tuning peak GPU] 0:40.65 1:40.65 2:40.65 3:40.65 4:40.65 GB (mean 40.65 GB, max 40.65 GB)

📊 Round 50 Results:
  Clean Accuracy: 0.9130
  ΔClean vs prev: +0.0030
  ΔClean vs best: +0.0000
  Global Loss: 0.7658

Results saved to: results/qwen_ag_news_alie_alpha0p3_seed42069_shadow_results.json

================================================================================
📊 DETAILED EXPERIMENT STATISTICS FOR DATA COLLECTION
================================================================================

--------------------------------------------------------------------------------
1️⃣  GLOBAL ACCURACY (Per Round)
--------------------------------------------------------------------------------
Round    | Clean Accuracy  | Accuracy Change  
--------------------------------------------------------------------------------
1        | 0.456667        |         +0.000000
2        | 0.694000        |         +0.237333
3        | 0.775000        |         +0.081000
4        | 0.808000        |         +0.033000
5        | 0.823667        |         +0.015667
6        | 0.834333        |         +0.010667
7        | 0.848000        |         +0.013667
8        | 0.858000        |         +0.010000
9        | 0.877000        |         +0.019000
10       | 0.877000        |         +0.000000
11       | 0.888333        |         +0.011333
12       | 0.885333        |         -0.003000
13       | 0.889000        |         +0.003667
14       | 0.885667        |         -0.003333
15       | 0.886333        |         +0.000667
16       | 0.888000        |         +0.001667
17       | 0.889333        |         +0.001333
18       | 0.886333        |         -0.003000
19       | 0.888000        |         +0.001667
20       | 0.890000        |         +0.002000
21       | 0.883000        |         -0.007000
22       | 0.884667        |         +0.001667
23       | 0.891333        |         +0.006667
24       | 0.883667        |         -0.007667
25       | 0.900333        |         +0.016667
26       | 0.895333        |         -0.005000
27       | 0.894667        |         -0.000667
28       | 0.899667        |         +0.005000
29       | 0.902000        |         +0.002333
30       | 0.894333        |         -0.007667
31       | 0.893667        |         -0.000667
32       | 0.898000        |         +0.004333
33       | 0.895667        |         -0.002333
34       | 0.898000        |         +0.002333
35       | 0.902000        |         +0.004000
36       | 0.901667        |         -0.000333
37       | 0.902667        |         +0.001000
38       | 0.899667        |         -0.003000
39       | 0.906333        |         +0.006667
40       | 0.900333        |         -0.006000
41       | 0.905333        |         +0.005000
42       | 0.901333        |         -0.004000
43       | 0.908333        |         +0.007000
44       | 0.904000        |         -0.004333
45       | 0.905000        |         +0.001000
46       | 0.906333        |         +0.001333
47       | 0.902000        |         -0.004333
48       | 0.908000        |         +0.006000
49       | 0.910000        |         +0.002000
50       | 0.913000        |         +0.003000
--------------------------------------------------------------------------------
Summary: Initial=0.456667, Final=0.913000, Best=0.913000, Change=+0.456333

--------------------------------------------------------------------------------
2️⃣  COSINE SIMILARITY (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A) | Mean | Std
--------------------------------------------------------------------------------
1      | 0.625569       | 0.612901       | 0.578039       | 0.652474       | 0.631754       | 0.804432       | 0.804432       | 0.672800 | 0.085815
2      | 0.692583       | 0.632574       | 0.493357       | 0.660443       | 0.677867       | 0.812746       | 0.812746       | 0.683188 | 0.101982
3      | 0.586602       | 0.500550       | 0.419542       | 0.540418       | 0.575656       | 0.755497       | 0.755497       | 0.590538 | 0.116195
4      | 0.475413       | 0.392811       | 0.360430       | 0.406714       | 0.465359       | 0.695353       | 0.695353       | 0.498776 | 0.129720
5      | 0.377631       | 0.282641       | 0.275377       | 0.303400       | 0.366260       | 0.631304       | 0.631304       | 0.409702 | 0.144725
6      | 0.297294       | 0.194032       | 0.221528       | 0.250833       | 0.311662       | 0.585779       | 0.585779       | 0.349558 | 0.154039
7      | 0.235443       | 0.187983       | 0.157804       | 0.212344       | 0.261498       | 0.553011       | 0.553011       | 0.308728 | 0.157479
8      | 0.196649       | 0.156034       | 0.114952       | 0.198283       | 0.229144       | 0.528095       | 0.528095       | 0.278750 | 0.161206
9      | 0.208029       | 0.173731       | 0.133834       | 0.193505       | 0.240002       | 0.536928       | 0.536928       | 0.288994 | 0.159632
10     | 0.188755       | 0.157232       | 0.102613       | 0.194487       | 0.221722       | 0.523731       | 0.523731       | 0.273182 | 0.162154
11     | 0.187813       | 0.139140       | 0.061164       | 0.164773       | 0.213969       | 0.509702       | 0.509702       | 0.255181 | 0.166939
12     | 0.154652       | 0.131256       | 0.068086       | 0.160038       | 0.210743       | 0.502312       | 0.502312       | 0.247057 | 0.166124
13     | 0.175157       | 0.131318       | 0.076819       | 0.152396       | 0.204454       | 0.504793       | 0.504793       | 0.249961 | 0.165235
14     | 0.163184       | 0.134224       | 0.084741       | 0.143020       | 0.186402       | 0.500720       | 0.500720       | 0.244716 | 0.164433
15     | 0.159219       | 0.125936       | 0.069683       | 0.153164       | 0.182969       | 0.496976       | 0.496976       | 0.240703 | 0.165360
16     | 0.164115       | 0.117835       | 0.078245       | 0.143109       | 0.178979       | 0.495710       | 0.495710       | 0.239100 | 0.165066
17     | 0.159827       | 0.130833       | 0.084791       | 0.129141       | 0.177396       | 0.496468       | 0.496468       | 0.239275 | 0.164834
18     | 0.174841       | 0.125210       | 0.050409       | 0.127778       | 0.158877       | 0.488789       | 0.488789       | 0.230670 | 0.167214
19     | 0.150588       | 0.111285       | 0.065974       | 0.109875       | 0.151323       | 0.481280       | 0.481280       | 0.221658 | 0.166356
20     | 0.158614       | 0.107287       | 0.066654       | 0.077143       | 0.142229       | 0.474335       | 0.474335       | 0.214371 | 0.167159
21     | 0.136819       | 0.121219       | 0.077692       | 0.107669       | 0.146748       | 0.480996       | 0.480996       | 0.221734 | 0.165240
22     | 0.135561       | 0.097370       | 0.080646       | 0.092160       | 0.156886       | 0.476531       | 0.476531       | 0.216526 | 0.166238
23     | 0.130574       | 0.099617       | 0.069986       | 0.088857       | 0.142883       | 0.471651       | 0.471651       | 0.210746 | 0.166560
24     | 0.110596       | 0.115755       | 0.085320       | 0.076836       | 0.139244       | 0.471413       | 0.471413       | 0.210083 | 0.166356
25     | 0.150830       | 0.121828       | 0.071615       | 0.090671       | 0.131678       | 0.479154       | 0.479154       | 0.217847 | 0.167014
26     | 0.129621       | 0.124380       | 0.074418       | 0.092842       | 0.150531       | 0.479567       | 0.479567       | 0.218704 | 0.166579
27     | 0.147829       | 0.103110       | 0.092895       | 0.082842       | 0.136528       | 0.477732       | 0.477732       | 0.216953 | 0.166302
28     | 0.142270       | 0.120520       | 0.103282       | 0.080570       | 0.143913       | 0.482636       | 0.482636       | 0.222261 | 0.165922
29     | 0.123526       | 0.106848       | 0.078865       | 0.092463       | 0.141760       | 0.475068       | 0.475068       | 0.213371 | 0.166574
30     | 0.108040       | 0.118995       | 0.090220       | 0.082695       | 0.142984       | 0.474652       | 0.474652       | 0.213177 | 0.166362
31     | 0.116987       | 0.115286       | 0.075505       | 0.097074       | 0.121866       | 0.472142       | 0.472142       | 0.210143 | 0.166334
32     | 0.153713       | 0.110199       | 0.094358       | 0.104488       | 0.132890       | 0.483902       | 0.483902       | 0.223350 | 0.165778
33     | 0.123578       | 0.098196       | 0.068524       | 0.107915       | 0.139594       | 0.473622       | 0.473622       | 0.212150 | 0.166615
34     | 0.130422       | 0.120527       | 0.103092       | 0.098456       | 0.129496       | 0.480901       | 0.480901       | 0.220542 | 0.165049
35     | 0.113795       | 0.118480       | 0.097568       | 0.091165       | 0.154121       | 0.479540       | 0.479540       | 0.219172 | 0.165715
36     | 0.112290       | 0.117324       | 0.092982       | 0.082461       | 0.148867       | 0.475903       | 0.475903       | 0.215104 | 0.166072
37     | 0.105270       | 0.118828       | 0.105012       | 0.111451       | 0.143438       | 0.481164       | 0.481164       | 0.220904 | 0.165043
38     | 0.123463       | 0.106126       | 0.073090       | 0.087437       | 0.142831       | 0.470470       | 0.470470       | 0.210555 | 0.165721
39     | 0.140856       | 0.126434       | 0.098917       | 0.120110       | 0.138337       | 0.488532       | 0.488532       | 0.228817 | 0.164751
40     | 0.128928       | 0.109309       | 0.105586       | 0.119824       | 0.165908       | 0.488699       | 0.488699       | 0.229565 | 0.164905
41     | 0.128918       | 0.120380       | 0.101093       | 0.080855       | 0.164985       | 0.484366       | 0.484366       | 0.223566 | 0.166663
42     | 0.124298       | 0.113530       | 0.100609       | 0.087815       | 0.160798       | 0.481307       | 0.481307       | 0.221380 | 0.165735
43     | 0.143859       | 0.125984       | 0.112164       | 0.110992       | 0.148723       | 0.490529       | 0.490529       | 0.231826 | 0.164152
44     | 0.134878       | 0.117893       | 0.107949       | 0.087923       | 0.144901       | 0.483070       | 0.483070       | 0.222812 | 0.165472
45     | 0.139670       | 0.135188       | 0.108590       | 0.116966       | 0.153037       | 0.492354       | 0.492354       | 0.234023 | 0.163941
46     | 0.142531       | 0.116701       | 0.089873       | 0.115527       | 0.137235       | 0.483390       | 0.483390       | 0.224093 | 0.164751
47     | 0.142931       | 0.102254       | 0.080089       | 0.084058       | 0.149542       | 0.477744       | 0.477744       | 0.216337 | 0.167158
48     | 0.126991       | 0.108823       | 0.090461       | 0.114506       | 0.154654       | 0.482127       | 0.482127       | 0.222813 | 0.164992
49     | 0.123657       | 0.129306       | 0.127969       | 0.129183       | 0.155872       | 0.492337       | 0.492337       | 0.235809 | 0.162535
50     | 0.169343       | 0.139028       | 0.108531       | 0.114644       | 0.146919       | 0.497573       | 0.497573       | 0.239087 | 0.164548
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
2b. EUCLIDEAN DISTANCE (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A) | Mean | Std
--------------------------------------------------------------------------------
1      | 0.720415       | 0.744663       | 0.782136       | 0.765626       | 0.754365       | 0.183776       | 0.183776       | 0.590680 | 0.257942
2      | 0.517642       | 0.569055       | 0.671576       | 0.556356       | 0.511131       | 0.144193       | 0.144193       | 0.444878 | 0.196304
3      | 0.455659       | 0.440125       | 0.494431       | 0.468007       | 0.457744       | 0.110210       | 0.110210       | 0.362341 | 0.160184
4      | 0.399283       | 0.361289       | 0.386764       | 0.428457       | 0.427823       | 0.089495       | 0.089495       | 0.311801 | 0.142243
5      | 0.399735       | 0.336334       | 0.353872       | 0.417490       | 0.409264       | 0.083096       | 0.083096       | 0.297555 | 0.138340
6      | 0.394263       | 0.324395       | 0.335986       | 0.387440       | 0.384010       | 0.078742       | 0.078742       | 0.283368 | 0.131721
7      | 0.376062       | 0.309030       | 0.328706       | 0.393514       | 0.374779       | 0.076616       | 0.076616       | 0.276475 | 0.129259
8      | 0.363905       | 0.305584       | 0.326198       | 0.389500       | 0.392110       | 0.076321       | 0.076321       | 0.275706 | 0.129410
9      | 0.377685       | 0.307842       | 0.329316       | 0.393501       | 0.392082       | 0.076913       | 0.076913       | 0.279179 | 0.131300
10     | 0.368306       | 0.299995       | 0.319701       | 0.389153       | 0.377816       | 0.074624       | 0.074624       | 0.272031 | 0.128269
11     | 0.373735       | 0.303441       | 0.329962       | 0.382691       | 0.363946       | 0.074346       | 0.074346       | 0.271781 | 0.127357
12     | 0.349837       | 0.289650       | 0.315070       | 0.378873       | 0.362059       | 0.071757       | 0.071757       | 0.262715 | 0.123837
13     | 0.353814       | 0.289407       | 0.313516       | 0.365434       | 0.359713       | 0.071613       | 0.071613       | 0.260730 | 0.122220
14     | 0.359381       | 0.288636       | 0.308222       | 0.358118       | 0.351685       | 0.070288       | 0.070288       | 0.258088 | 0.121309
15     | 0.352384       | 0.287426       | 0.304802       | 0.362158       | 0.333905       | 0.069533       | 0.069533       | 0.254249 | 0.119234
16     | 0.345407       | 0.292622       | 0.304199       | 0.360335       | 0.352238       | 0.070177       | 0.070177       | 0.256451 | 0.120038
17     | 0.340681       | 0.285484       | 0.297195       | 0.348256       | 0.336597       | 0.067944       | 0.067944       | 0.249157 | 0.116586
18     | 0.347136       | 0.290131       | 0.305268       | 0.348864       | 0.342321       | 0.069337       | 0.069337       | 0.253199 | 0.118083
19     | 0.332348       | 0.283064       | 0.302168       | 0.339599       | 0.339986       | 0.067744       | 0.067744       | 0.247522 | 0.115334
20     | 0.338133       | 0.276230       | 0.292541       | 0.331252       | 0.338269       | 0.066539       | 0.066539       | 0.244215 | 0.114480
21     | 0.332612       | 0.276806       | 0.291781       | 0.324215       | 0.329396       | 0.066330       | 0.066330       | 0.241067 | 0.112130
22     | 0.322564       | 0.275114       | 0.286000       | 0.329002       | 0.321982       | 0.065227       | 0.065227       | 0.237874 | 0.110755
23     | 0.321716       | 0.269914       | 0.291446       | 0.320890       | 0.313146       | 0.064692       | 0.064692       | 0.235214 | 0.109164
24     | 0.309609       | 0.271550       | 0.279473       | 0.306505       | 0.316419       | 0.063288       | 0.063288       | 0.230019 | 0.106515
25     | 0.306356       | 0.270064       | 0.283755       | 0.303646       | 0.306876       | 0.062158       | 0.062158       | 0.227859 | 0.105538
26     | 0.308421       | 0.270482       | 0.285321       | 0.315206       | 0.297118       | 0.062998       | 0.062998       | 0.228935 | 0.105820
27     | 0.304893       | 0.262246       | 0.277272       | 0.305062       | 0.298204       | 0.061497       | 0.061497       | 0.224382 | 0.104016
28     | 0.305362       | 0.266981       | 0.276609       | 0.311010       | 0.303377       | 0.062008       | 0.062008       | 0.226765 | 0.105245
29     | 0.293559       | 0.260654       | 0.279231       | 0.307555       | 0.292166       | 0.060519       | 0.060519       | 0.222029 | 0.103016
30     | 0.301442       | 0.262096       | 0.272194       | 0.282792       | 0.311587       | 0.060657       | 0.060657       | 0.221632 | 0.102971
31     | 0.301101       | 0.265874       | 0.286020       | 0.307204       | 0.296363       | 0.062224       | 0.062224       | 0.225859 | 0.104213
32     | 0.291572       | 0.259757       | 0.272309       | 0.292711       | 0.298208       | 0.060048       | 0.060048       | 0.219236 | 0.101424
33     | 0.300703       | 0.269082       | 0.282901       | 0.304959       | 0.298109       | 0.062692       | 0.062692       | 0.225877 | 0.103818
34     | 0.303817       | 0.261388       | 0.274292       | 0.301088       | 0.314639       | 0.061375       | 0.061375       | 0.225425 | 0.105109
35     | 0.293349       | 0.265775       | 0.278164       | 0.314651       | 0.314998       | 0.062288       | 0.062288       | 0.227359 | 0.105701
36     | 0.311028       | 0.266117       | 0.280142       | 0.298809       | 0.318866       | 0.062792       | 0.062792       | 0.228650 | 0.106181
37     | 0.287661       | 0.263505       | 0.280463       | 0.303882       | 0.319426       | 0.062301       | 0.062301       | 0.225649 | 0.104583
38     | 0.304105       | 0.264802       | 0.281379       | 0.328591       | 0.338773       | 0.064209       | 0.064209       | 0.235153 | 0.110636
39     | 0.294882       | 0.259497       | 0.278260       | 0.305371       | 0.293994       | 0.061114       | 0.061114       | 0.222033 | 0.102668
40     | 0.304086       | 0.267025       | 0.272583       | 0.315165       | 0.306926       | 0.061981       | 0.061981       | 0.227106 | 0.105726
41     | 0.292299       | 0.262253       | 0.273327       | 0.285407       | 0.297468       | 0.060312       | 0.060312       | 0.218768 | 0.100801
42     | 0.297975       | 0.266401       | 0.272361       | 0.311858       | 0.309992       | 0.062160       | 0.062160       | 0.226130 | 0.104932
43     | 0.299126       | 0.262520       | 0.271292       | 0.299265       | 0.316072       | 0.061543       | 0.061543       | 0.224480 | 0.104396
44     | 0.298943       | 0.264046       | 0.271016       | 0.295448       | 0.303586       | 0.060998       | 0.060998       | 0.222148 | 0.102807
45     | 0.314299       | 0.266472       | 0.279598       | 0.318661       | 0.309623       | 0.063147       | 0.063147       | 0.230707 | 0.107420
46     | 0.299396       | 0.271483       | 0.278399       | 0.325625       | 0.314102       | 0.063572       | 0.063572       | 0.230878 | 0.107230
47     | 0.311126       | 0.270975       | 0.277763       | 0.282620       | 0.301931       | 0.061614       | 0.061614       | 0.223949 | 0.103466
48     | 0.313780       | 0.277664       | 0.289550       | 0.298216       | 0.349912       | 0.065476       | 0.065476       | 0.237154 | 0.110613
49     | 0.299553       | 0.272171       | 0.282906       | 0.360767       | 0.314089       | 0.065389       | 0.065389       | 0.237181 | 0.111751
50     | 0.313066       | 0.263016       | 0.275397       | 0.296098       | 0.299870       | 0.061080       | 0.061080       | 0.224230 | 0.104291
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
2c. GLOBAL LOSS (Per Round)
--------------------------------------------------------------------------------
Round    | Global Loss    
--------------------------------------------------------------------------------
1        | 1.991154       
2        | 0.966186       
3        | 0.660474       
4        | 0.547519       
5        | 0.525599       
6        | 0.489649       
7        | 0.461563       
8        | 0.453002       
9        | 0.405915       
10       | 0.404065       
11       | 0.381145       
12       | 0.410645       
13       | 0.399374       
14       | 0.431015       
15       | 0.447248       
16       | 0.449755       
17       | 0.459933       
18       | 0.511479       
19       | 0.518287       
20       | 0.533837       
21       | 0.587086       
22       | 0.603987       
23       | 0.606484       
24       | 0.648768       
25       | 0.584001       
26       | 0.660172       
27       | 0.654098       
28       | 0.643877       
29       | 0.632248       
30       | 0.695093       
31       | 0.741947       
32       | 0.701255       
33       | 0.765545       
34       | 0.730146       
35       | 0.734020       
36       | 0.737638       
37       | 0.770239       
38       | 0.799902       
39       | 0.761986       
40       | 0.790760       
41       | 0.758204       
42       | 0.795020       
43       | 0.772579       
44       | 0.791023       
45       | 0.804658       
46       | 0.790038       
47       | 0.860566       
48       | 0.850122       
49       | 0.784418       
50       | 0.765824       
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
3️⃣  LOCAL ACCURACY (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A) | Mean | Std
--------------------------------------------------------------------------------
1      | 0.592391       | 0.222826       | 0.326087       | 0.592391       | 0.445652       | 0.222826       | 0.222826       | 0.375000 | 0.156467
2      | 0.766304       | 0.559783       | 0.440217       | 0.663043       | 0.527174       | 0.418478       | 0.418478       | 0.541925 | 0.123274
3      | 0.836957       | 0.701087       | 0.581522       | 0.668478       | 0.581522       | 0.663043       | 0.663043       | 0.670807 | 0.079814
4      | 0.864130       | 0.782609       | 0.619565       | 0.668478       | 0.619565       | 0.755435       | 0.755435       | 0.723602 | 0.084467
5      | 0.869565       | 0.804348       | 0.630435       | 0.668478       | 0.630435       | 0.771739       | 0.771739       | 0.735248 | 0.086114
6      | 0.869565       | 0.788043       | 0.663043       | 0.673913       | 0.657609       | 0.777174       | 0.777174       | 0.743789 | 0.074486
7      | 0.869565       | 0.777174       | 0.646739       | 0.673913       | 0.673913       | 0.798913       | 0.798913       | 0.748447 | 0.077500
8      | 0.853261       | 0.853261       | 0.722826       | 0.668478       | 0.684783       | 0.815217       | 0.815217       | 0.773292 | 0.073360
9      | 0.864130       | 0.826087       | 0.695652       | 0.684783       | 0.695652       | 0.836957       | 0.836957       | 0.777174 | 0.074575
10     | 0.875000       | 0.842391       | 0.706522       | 0.679348       | 0.717391       | 0.858696       | 0.858696       | 0.791149 | 0.079177
11     | 0.885870       | 0.815217       | 0.701087       | 0.679348       | 0.739130       | 0.847826       | 0.847826       | 0.788043 | 0.074857
12     | 0.858696       | 0.875000       | 0.766304       | 0.679348       | 0.744565       | 0.869565       | 0.869565       | 0.809006 | 0.072650
13     | 0.880435       | 0.880435       | 0.771739       | 0.684783       | 0.750000       | 0.880435       | 0.880435       | 0.818323 | 0.075690
14     | 0.869565       | 0.842391       | 0.793478       | 0.684783       | 0.717391       | 0.896739       | 0.896739       | 0.814441 | 0.079314
15     | 0.869565       | 0.858696       | 0.788043       | 0.684783       | 0.750000       | 0.885870       | 0.885870       | 0.817547 | 0.072501
16     | 0.880435       | 0.885870       | 0.760870       | 0.684783       | 0.711957       | 0.880435       | 0.880435       | 0.812112 | 0.083078
17     | 0.885870       | 0.875000       | 0.804348       | 0.690217       | 0.750000       | 0.885870       | 0.885870       | 0.825311 | 0.073516
18     | 0.885870       | 0.869565       | 0.804348       | 0.684783       | 0.744565       | 0.885870       | 0.885870       | 0.822981 | 0.075242
19     | 0.891304       | 0.869565       | 0.782609       | 0.673913       | 0.744565       | 0.880435       | 0.880435       | 0.817547 | 0.078589
20     | 0.891304       | 0.891304       | 0.804348       | 0.679348       | 0.793478       | 0.869565       | 0.869565       | 0.828416 | 0.071031
21     | 0.869565       | 0.858696       | 0.793478       | 0.690217       | 0.755435       | 0.880435       | 0.880435       | 0.818323 | 0.068614
22     | 0.880435       | 0.896739       | 0.809783       | 0.711957       | 0.739130       | 0.864130       | 0.864130       | 0.823758 | 0.067247
23     | 0.891304       | 0.847826       | 0.777174       | 0.695652       | 0.798913       | 0.864130       | 0.864130       | 0.819876 | 0.062672
24     | 0.875000       | 0.847826       | 0.798913       | 0.684783       | 0.760870       | 0.891304       | 0.891304       | 0.821429 | 0.071891
25     | 0.880435       | 0.864130       | 0.788043       | 0.739130       | 0.782609       | 0.869565       | 0.869565       | 0.827640 | 0.052186
26     | 0.880435       | 0.858696       | 0.798913       | 0.684783       | 0.777174       | 0.880435       | 0.880435       | 0.822981 | 0.068614
27     | 0.875000       | 0.875000       | 0.804348       | 0.717391       | 0.766304       | 0.880435       | 0.880435       | 0.828416 | 0.061546
28     | 0.902174       | 0.815217       | 0.804348       | 0.744565       | 0.820652       | 0.885870       | 0.885870       | 0.836957 | 0.052612
29     | 0.880435       | 0.858696       | 0.798913       | 0.739130       | 0.798913       | 0.880435       | 0.880435       | 0.833851 | 0.051465
30     | 0.885870       | 0.831522       | 0.826087       | 0.733696       | 0.750000       | 0.880435       | 0.880435       | 0.826863 | 0.058349
31     | 0.896739       | 0.847826       | 0.782609       | 0.722826       | 0.739130       | 0.864130       | 0.864130       | 0.816770 | 0.063094
32     | 0.902174       | 0.853261       | 0.842391       | 0.744565       | 0.771739       | 0.880435       | 0.880435       | 0.839286 | 0.054878
33     | 0.896739       | 0.847826       | 0.809783       | 0.722826       | 0.793478       | 0.864130       | 0.864130       | 0.828416 | 0.053869
34     | 0.891304       | 0.847826       | 0.820652       | 0.733696       | 0.798913       | 0.875000       | 0.875000       | 0.834627 | 0.051136
35     | 0.885870       | 0.842391       | 0.809783       | 0.739130       | 0.820652       | 0.864130       | 0.864130       | 0.832298 | 0.045231
36     | 0.885870       | 0.836957       | 0.788043       | 0.744565       | 0.793478       | 0.885870       | 0.885870       | 0.831522 | 0.053170
37     | 0.891304       | 0.836957       | 0.798913       | 0.766304       | 0.804348       | 0.880435       | 0.880435       | 0.836957 | 0.045098
38     | 0.891304       | 0.875000       | 0.804348       | 0.766304       | 0.782609       | 0.885870       | 0.885870       | 0.841615 | 0.050770
39     | 0.896739       | 0.885870       | 0.815217       | 0.760870       | 0.831522       | 0.875000       | 0.875000       | 0.848602 | 0.045044
40     | 0.891304       | 0.864130       | 0.826087       | 0.760870       | 0.760870       | 0.885870       | 0.885870       | 0.839286 | 0.053633
41     | 0.885870       | 0.875000       | 0.782609       | 0.766304       | 0.853261       | 0.891304       | 0.891304       | 0.849379 | 0.049104
42     | 0.891304       | 0.836957       | 0.804348       | 0.744565       | 0.788043       | 0.885870       | 0.885870       | 0.833851 | 0.053000
43     | 0.885870       | 0.842391       | 0.836957       | 0.760870       | 0.820652       | 0.880435       | 0.880435       | 0.843944 | 0.041259
44     | 0.896739       | 0.885870       | 0.815217       | 0.755435       | 0.798913       | 0.902174       | 0.902174       | 0.850932 | 0.055641
45     | 0.896739       | 0.875000       | 0.820652       | 0.777174       | 0.831522       | 0.891304       | 0.891304       | 0.854814 | 0.042369
46     | 0.885870       | 0.896739       | 0.804348       | 0.766304       | 0.804348       | 0.885870       | 0.885870       | 0.847050 | 0.049507
47     | 0.875000       | 0.858696       | 0.798913       | 0.755435       | 0.831522       | 0.885870       | 0.885870       | 0.841615 | 0.045788
48     | 0.891304       | 0.853261       | 0.815217       | 0.798913       | 0.782609       | 0.880435       | 0.880435       | 0.843168 | 0.040715
49     | 0.885870       | 0.885870       | 0.798913       | 0.798913       | 0.804348       | 0.891304       | 0.891304       | 0.850932 | 0.043561
50     | 0.885870       | 0.864130       | 0.809783       | 0.820652       | 0.847826       | 0.885870       | 0.885870       | 0.857143 | 0.029727
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
4️⃣  SHADOW KRUM SCORE (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A) | Selected | SelIsAtk
--------------------------------------------------------------------------------
1      | 2.184508       | 0.931724       | 1.019077       | 2.456323       | 2.270075       | 0.848375       | 0.848375       | 5        | 1       
2      | 1.288623       | 0.605912       | 0.809440       | 1.417320       | 1.345907       | 0.550280       | 0.550280       | 5        | 1       
3      | 1.014705       | 0.425802       | 0.505683       | 1.058199       | 1.016121       | 0.332236       | 0.332236       | 5        | 1       
4      | 0.703833       | 0.336292       | 0.365413       | 0.808883       | 0.809631       | 0.222397       | 0.222397       | 5        | 1       
5      | 0.676074       | 0.310843       | 0.328953       | 0.742761       | 0.715778       | 0.193683       | 0.193683       | 5        | 1       
6      | 0.655433       | 0.296330       | 0.307016       | 0.640505       | 0.631644       | 0.178631       | 0.178631       | 5        | 1       
7      | 0.581261       | 0.274788       | 0.293797       | 0.666942       | 0.587458       | 0.167118       | 0.167118       | 5        | 1       
8      | 0.526360       | 0.274086       | 0.293744       | 0.649673       | 0.652371       | 0.164520       | 0.164520       | 5        | 1       
9      | 0.572358       | 0.281374       | 0.302016       | 0.650648       | 0.648775       | 0.168031       | 0.168031       | 5        | 1       
10     | 0.541796       | 0.271844       | 0.289956       | 0.636775       | 0.602493       | 0.159750       | 0.159750       | 5        | 1       
11     | 0.568345       | 0.294657       | 0.319746       | 0.618543       | 0.568990       | 0.168677       | 0.168677       | 5        | 1       
12     | 0.489839       | 0.269086       | 0.292302       | 0.601013       | 0.551053       | 0.153861       | 0.153861       | 5        | 1       
13     | 0.499881       | 0.261718       | 0.283835       | 0.563508       | 0.554436       | 0.151913       | 0.151913       | 5        | 1       
14     | 0.519948       | 0.265080       | 0.282703       | 0.539103       | 0.526848       | 0.150099       | 0.150099       | 5        | 1       
15     | 0.507486       | 0.258672       | 0.274037       | 0.562336       | 0.470246       | 0.147165       | 0.147165       | 5        | 1       
16     | 0.490013       | 0.265137       | 0.275102       | 0.551064       | 0.522142       | 0.149275       | 0.149275       | 5        | 1       
17     | 0.474981       | 0.259788       | 0.269414       | 0.514510       | 0.484210       | 0.143241       | 0.143241       | 5        | 1       
18     | 0.496672       | 0.263673       | 0.277108       | 0.525367       | 0.499111       | 0.148762       | 0.148762       | 5        | 1       
19     | 0.449825       | 0.259890       | 0.276963       | 0.495158       | 0.500078       | 0.144501       | 0.144501       | 5        | 1       
20     | 0.471425       | 0.242927       | 0.256536       | 0.464214       | 0.487230       | 0.136379       | 0.136379       | 5        | 1       
21     | 0.458566       | 0.237236       | 0.249789       | 0.453151       | 0.468377       | 0.135072       | 0.135072       | 5        | 1       
22     | 0.422685       | 0.239458       | 0.248279       | 0.469763       | 0.450589       | 0.132338       | 0.132338       | 5        | 1       
23     | 0.434951       | 0.234268       | 0.252453       | 0.440780       | 0.431426       | 0.132405       | 0.132405       | 5        | 1       
24     | 0.400435       | 0.233284       | 0.238893       | 0.411778       | 0.443667       | 0.127571       | 0.127571       | 5        | 1       
25     | 0.399229       | 0.245981       | 0.256989       | 0.400290       | 0.408299       | 0.130730       | 0.130730       | 5        | 1       
26     | 0.394964       | 0.241423       | 0.253267       | 0.440536       | 0.395459       | 0.130580       | 0.130580       | 5        | 1       
27     | 0.387698       | 0.225092       | 0.237052       | 0.406541       | 0.389583       | 0.123060       | 0.123060       | 5        | 1       
28     | 0.387837       | 0.233835       | 0.240812       | 0.414983       | 0.408798       | 0.125248       | 0.125248       | 5        | 1       
29     | 0.361694       | 0.234892       | 0.249686       | 0.410680       | 0.375935       | 0.124651       | 0.124651       | 5        | 1       
30     | 0.380321       | 0.226806       | 0.234005       | 0.346986       | 0.425639       | 0.121115       | 0.121115       | 5        | 1       
31     | 0.378337       | 0.238177       | 0.254529       | 0.416289       | 0.396221       | 0.129008       | 0.129008       | 5        | 1       
32     | 0.363114       | 0.224523       | 0.233974       | 0.375446       | 0.393824       | 0.120146       | 0.120146       | 5        | 1       
33     | 0.390120       | 0.231717       | 0.242698       | 0.413956       | 0.397454       | 0.127672       | 0.127672       | 5        | 1       
34     | 0.381757       | 0.227178       | 0.236810       | 0.390787       | 0.428064       | 0.122018       | 0.122018       | 5        | 1       
35     | 0.359105       | 0.231983       | 0.241562       | 0.422752       | 0.434129       | 0.125207       | 0.125207       | 5        | 1       
36     | 0.402865       | 0.229207       | 0.240102       | 0.389596       | 0.447335       | 0.125772       | 0.125772       | 5        | 1       
37     | 0.349751       | 0.226789       | 0.240357       | 0.399933       | 0.450574       | 0.124553       | 0.124553       | 5        | 1       
38     | 0.372183       | 0.227758       | 0.240872       | 0.453135       | 0.494258       | 0.125973       | 0.125973       | 5        | 1       
39     | 0.364413       | 0.223025       | 0.238224       | 0.410542       | 0.382180       | 0.122188       | 0.122188       | 5        | 1       
40     | 0.383425       | 0.230756       | 0.234374       | 0.429311       | 0.405474       | 0.123340       | 0.123340       | 5        | 1       
41     | 0.365976       | 0.225565       | 0.233777       | 0.362363       | 0.395266       | 0.121159       | 0.121159       | 5        | 1       
42     | 0.367654       | 0.224679       | 0.228350       | 0.421262       | 0.423238       | 0.122047       | 0.122047       | 5        | 1       
43     | 0.374812       | 0.219880       | 0.226010       | 0.386251       | 0.436000       | 0.120036       | 0.120036       | 5        | 1       
44     | 0.375629       | 0.224189       | 0.229158       | 0.382475       | 0.407567       | 0.120802       | 0.120802       | 5        | 1       
45     | 0.411999       | 0.227046       | 0.237284       | 0.435935       | 0.420220       | 0.125624       | 0.125624       | 5        | 1       
46     | 0.373422       | 0.231887       | 0.236641       | 0.466240       | 0.433059       | 0.126875       | 0.126875       | 5        | 1       
47     | 0.417316       | 0.238617       | 0.243314       | 0.359477       | 0.406250       | 0.127328       | 0.127328       | 5        | 1       
48     | 0.406665       | 0.247615       | 0.257220       | 0.384349       | 0.545942       | 0.135240       | 0.135240       | 5        | 1       
49     | 0.368952       | 0.229449       | 0.237741       | 0.563266       | 0.422356       | 0.128724       | 0.128724       | 5        | 1       
50     | 0.407795       | 0.229866       | 0.239314       | 0.385570       | 0.396566       | 0.123305       | 0.123305       | 5        | 1       
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
20     | 1              | 0              | 0              | 0              | 1              | 0              | 0             
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
33     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
34     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
35     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
36     | 1              | 0              | 0              | 0              | 1              | 0              | 0             
37     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
38     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
39     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
40     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
41     | 1              | 0              | 0              | 0              | 1              | 0              | 0             
42     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
43     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
44     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
45     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
46     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
47     | 1              | 0              | 0              | 0              | 1              | 0              | 0             
48     | 1              | 0              | 0              | 0              | 1              | 0              | 0             
49     | 0              | 0              | 0              | 1              | 1              | 0              | 0             
50     | 1              | 0              | 0              | 0              | 1              | 0              | 0             
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
4c. SHADOW TRIMMED-MEAN TRIM FRACTION (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A)
--------------------------------------------------------------------------------
1      | 0.806651       | 0.724999       | 0.732848       | 0.864952       | 0.727239       | 0.045257       | 0.098054      
2      | 0.799816       | 0.727909       | 0.786033       | 0.814082       | 0.733449       | 0.036509       | 0.102202      
3      | 0.799211       | 0.709514       | 0.748941       | 0.797702       | 0.786916       | 0.044698       | 0.113019      
4      | 0.791988       | 0.696141       | 0.725959       | 0.810024       | 0.807241       | 0.049460       | 0.119187      
5      | 0.805135       | 0.686328       | 0.717455       | 0.813563       | 0.801389       | 0.047935       | 0.128196      
6      | 0.809357       | 0.697090       | 0.718158       | 0.806412       | 0.795454       | 0.044429       | 0.129100      
7      | 0.800402       | 0.681440       | 0.719760       | 0.824799       | 0.797537       | 0.043696       | 0.132366      
8      | 0.784063       | 0.679005       | 0.724077       | 0.824152       | 0.810178       | 0.051893       | 0.126632      
9      | 0.793321       | 0.679687       | 0.719784       | 0.819438       | 0.809735       | 0.049492       | 0.128544      
10     | 0.795139       | 0.683181       | 0.719163       | 0.821769       | 0.803055       | 0.047290       | 0.130403      
11     | 0.794535       | 0.693020       | 0.727830       | 0.819328       | 0.791054       | 0.042037       | 0.132196      
12     | 0.786411       | 0.679527       | 0.729528       | 0.827262       | 0.799699       | 0.044294       | 0.133279      
13     | 0.790083       | 0.684026       | 0.729072       | 0.816411       | 0.803724       | 0.046010       | 0.130674      
14     | 0.800223       | 0.695490       | 0.724287       | 0.812127       | 0.793204       | 0.043340       | 0.131329      
15     | 0.799294       | 0.694468       | 0.725754       | 0.820153       | 0.785732       | 0.039162       | 0.135437      
16     | 0.792969       | 0.697938       | 0.724006       | 0.815067       | 0.796998       | 0.044683       | 0.128339      
17     | 0.792537       | 0.700727       | 0.724483       | 0.813009       | 0.797092       | 0.042732       | 0.129421      
18     | 0.793995       | 0.704527       | 0.726941       | 0.809479       | 0.793598       | 0.042376       | 0.129084      
19     | 0.786132       | 0.699876       | 0.733769       | 0.809365       | 0.798570       | 0.044482       | 0.127806      
20     | 0.799439       | 0.695356       | 0.725534       | 0.806901       | 0.799942       | 0.045785       | 0.127043      
21     | 0.795797       | 0.702037       | 0.730338       | 0.802542       | 0.798351       | 0.044982       | 0.125954      
22     | 0.788885       | 0.705863       | 0.729440       | 0.812913       | 0.793296       | 0.042391       | 0.127213      
23     | 0.792936       | 0.697916       | 0.740036       | 0.808219       | 0.790311       | 0.041834       | 0.128748      
24     | 0.788219       | 0.713114       | 0.731308       | 0.801731       | 0.801329       | 0.045096       | 0.119203      
25     | 0.787174       | 0.713236       | 0.742314       | 0.796941       | 0.794216       | 0.041835       | 0.124284      
26     | 0.783807       | 0.714484       | 0.743224       | 0.816360       | 0.779005       | 0.036199       | 0.126922      
27     | 0.790600       | 0.703493       | 0.738192       | 0.818084       | 0.787426       | 0.039056       | 0.123149      
28     | 0.791684       | 0.713210       | 0.734668       | 0.808576       | 0.786384       | 0.040334       | 0.125144      
29     | 0.785424       | 0.711535       | 0.748091       | 0.810783       | 0.782492       | 0.037127       | 0.124547      
30     | 0.789462       | 0.711609       | 0.739255       | 0.795526       | 0.803133       | 0.046278       | 0.114739      
31     | 0.786494       | 0.705498       | 0.749273       | 0.812622       | 0.786139       | 0.037602       | 0.122372      
32     | 0.788544       | 0.713833       | 0.737978       | 0.807232       | 0.791604       | 0.042965       | 0.117845      
33     | 0.789180       | 0.715839       | 0.745130       | 0.808339       | 0.782127       | 0.037857       | 0.121528      
34     | 0.790938       | 0.703206       | 0.735400       | 0.805673       | 0.802117       | 0.045620       | 0.117046      
35     | 0.779565       | 0.709064       | 0.736416       | 0.812970       | 0.799831       | 0.043839       | 0.118316      
36     | 0.795683       | 0.705211       | 0.730594       | 0.814514       | 0.797093       | 0.043714       | 0.113191      
37     | 0.787224       | 0.709756       | 0.739882       | 0.801007       | 0.804234       | 0.045882       | 0.112015      
38     | 0.778547       | 0.691061       | 0.728643       | 0.818998       | 0.814356       | 0.049879       | 0.118517      
39     | 0.794147       | 0.707535       | 0.741738       | 0.811226       | 0.782853       | 0.038562       | 0.123939      
40     | 0.791440       | 0.708802       | 0.727705       | 0.813035       | 0.799448       | 0.040192       | 0.119378      
41     | 0.802498       | 0.712905       | 0.745045       | 0.797452       | 0.783930       | 0.040935       | 0.117235      
42     | 0.789719       | 0.713381       | 0.728233       | 0.821140       | 0.788988       | 0.040590       | 0.117950      
43     | 0.789015       | 0.708522       | 0.730461       | 0.809463       | 0.806031       | 0.045121       | 0.111386      
44     | 0.785187       | 0.712439       | 0.731786       | 0.815372       | 0.802856       | 0.040253       | 0.112107      
45     | 0.810191       | 0.702546       | 0.726777       | 0.824010       | 0.781456       | 0.036875       | 0.118143      
46     | 0.781322       | 0.710561       | 0.728579       | 0.816408       | 0.798854       | 0.042503       | 0.121772      
47     | 0.795598       | 0.721979       | 0.738771       | 0.807314       | 0.785026       | 0.037567       | 0.113745      
48     | 0.789961       | 0.714701       | 0.735160       | 0.784783       | 0.818146       | 0.052714       | 0.104534      
49     | 0.786321       | 0.696564       | 0.727101       | 0.829791       | 0.793926       | 0.038637       | 0.127660      
50     | 0.801046       | 0.719266       | 0.738576       | 0.800708       | 0.782588       | 0.038129       | 0.119686      
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
4d. SHADOW MEDIAN PROVIDER FRACTION (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A)
--------------------------------------------------------------------------------
1      | 0.024745       | 0.036342       | 0.036166       | 0.025066       | 0.020992       | 0.198299       | 0.658390      
2      | 0.025337       | 0.035718       | 0.030787       | 0.022378       | 0.024491       | 0.180043       | 0.681245      
3      | 0.028111       | 0.041208       | 0.035521       | 0.026257       | 0.026619       | 0.148236       | 0.694048      
4      | 0.031218       | 0.043416       | 0.039922       | 0.027027       | 0.027065       | 0.136131       | 0.695222      
5      | 0.031408       | 0.045759       | 0.041486       | 0.028239       | 0.029240       | 0.135675       | 0.688194      
6      | 0.029299       | 0.043965       | 0.040972       | 0.029383       | 0.029910       | 0.137649       | 0.688823      
7      | 0.031240       | 0.045780       | 0.041390       | 0.027264       | 0.030389       | 0.138111       | 0.685827      
8      | 0.034125       | 0.046805       | 0.041415       | 0.027794       | 0.028387       | 0.131958       | 0.689517      
9      | 0.032545       | 0.046492       | 0.041826       | 0.028593       | 0.028580       | 0.133059       | 0.688906      
10     | 0.031941       | 0.046399       | 0.041917       | 0.027559       | 0.029877       | 0.134273       | 0.688034      
11     | 0.030903       | 0.045365       | 0.039500       | 0.027425       | 0.031040       | 0.139039       | 0.686729      
12     | 0.032987       | 0.046319       | 0.040639       | 0.026809       | 0.030820       | 0.135702       | 0.686725      
13     | 0.031367       | 0.047262       | 0.040077       | 0.028120       | 0.029857       | 0.134190       | 0.689127      
14     | 0.029657       | 0.044551       | 0.040651       | 0.028699       | 0.031112       | 0.136307       | 0.689024      
15     | 0.030241       | 0.044665       | 0.040248       | 0.027069       | 0.032376       | 0.141684       | 0.683717      
16     | 0.031184       | 0.043805       | 0.040241       | 0.027701       | 0.030091       | 0.135717       | 0.691261      
17     | 0.031188       | 0.043562       | 0.039110       | 0.028095       | 0.030196       | 0.137034       | 0.690814      
18     | 0.030825       | 0.042353       | 0.039079       | 0.028661       | 0.030542       | 0.137712       | 0.690827      
19     | 0.032287       | 0.043074       | 0.038551       | 0.028497       | 0.029879       | 0.135156       | 0.692557      
20     | 0.030478       | 0.043460       | 0.040113       | 0.029538       | 0.029239       | 0.135715       | 0.691457      
21     | 0.030361       | 0.042590       | 0.039304       | 0.029677       | 0.029004       | 0.136886       | 0.692179      
22     | 0.030526       | 0.041994       | 0.039146       | 0.027658       | 0.030279       | 0.137428       | 0.692969      
23     | 0.030367       | 0.044280       | 0.037250       | 0.028205       | 0.030479       | 0.138997       | 0.690421      
24     | 0.030196       | 0.040233       | 0.037296       | 0.028958       | 0.027617       | 0.137226       | 0.698475      
25     | 0.030319       | 0.040444       | 0.036654       | 0.029461       | 0.029241       | 0.139058       | 0.694823      
26     | 0.030022       | 0.039705       | 0.035742       | 0.026331       | 0.031321       | 0.141658       | 0.695221      
27     | 0.029667       | 0.040414       | 0.036518       | 0.026076       | 0.029530       | 0.142091       | 0.695703      
28     | 0.030305       | 0.040451       | 0.037169       | 0.027643       | 0.029910       | 0.140349       | 0.694172      
29     | 0.029845       | 0.040208       | 0.035305       | 0.026452       | 0.029865       | 0.143341       | 0.694984      
30     | 0.029248       | 0.039311       | 0.036789       | 0.029687       | 0.025982       | 0.137413       | 0.701570      
31     | 0.029420       | 0.040072       | 0.034414       | 0.026816       | 0.029253       | 0.141453       | 0.698573      
32     | 0.029439       | 0.039941       | 0.036298       | 0.027336       | 0.027795       | 0.139394       | 0.699797      
33     | 0.029323       | 0.038607       | 0.035387       | 0.027019       | 0.029049       | 0.143746       | 0.696869      
34     | 0.029729       | 0.040626       | 0.037459       | 0.028134       | 0.026719       | 0.134114       | 0.703220      
35     | 0.031246       | 0.040187       | 0.037011       | 0.025977       | 0.027734       | 0.137779       | 0.700067      
36     | 0.028364       | 0.038933       | 0.036955       | 0.026538       | 0.026115       | 0.141697       | 0.701398      
37     | 0.029821       | 0.039206       | 0.036180       | 0.027229       | 0.025460       | 0.137762       | 0.704341      
38     | 0.032428       | 0.043979       | 0.039460       | 0.026501       | 0.026028       | 0.132306       | 0.699299      
39     | 0.029313       | 0.040638       | 0.036435       | 0.026485       | 0.029631       | 0.141000       | 0.696499      
40     | 0.029045       | 0.038992       | 0.037986       | 0.026366       | 0.027181       | 0.140757       | 0.699673      
41     | 0.028033       | 0.038258       | 0.035006       | 0.028634       | 0.028238       | 0.141476       | 0.700355      
42     | 0.029641       | 0.039173       | 0.037483       | 0.024462       | 0.027781       | 0.143631       | 0.697830      
43     | 0.029574       | 0.039126       | 0.036204       | 0.026496       | 0.025107       | 0.139789       | 0.703704      
44     | 0.028381       | 0.037468       | 0.035917       | 0.024800       | 0.025795       | 0.141948       | 0.705692      
45     | 0.026104       | 0.039394       | 0.037139       | 0.023862       | 0.028519       | 0.145968       | 0.699013      
46     | 0.032024       | 0.040273       | 0.037794       | 0.026110       | 0.028074       | 0.140436       | 0.695289      
47     | 0.026836       | 0.036146       | 0.034576       | 0.026815       | 0.026938       | 0.146662       | 0.702026      
48     | 0.028913       | 0.038045       | 0.036163       | 0.030970       | 0.023157       | 0.132088       | 0.710664      
49     | 0.033020       | 0.042217       | 0.037869       | 0.023637       | 0.029555       | 0.145114       | 0.688589      
50     | 0.027189       | 0.038166       | 0.036020       | 0.027923       | 0.028518       | 0.142218       | 0.699967      
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
4e. SHADOW DISTANCE TO COORDINATE MEDIAN (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A)
--------------------------------------------------------------------------------
1      | 0.802971       | 0.626460       | 0.660390       | 0.883313       | 0.790884       | 0.062792       | 0.062792      
2      | 0.585321       | 0.474936       | 0.571752       | 0.642030       | 0.565322       | 0.048019       | 0.048019      
3      | 0.494028       | 0.375456       | 0.424716       | 0.521085       | 0.504037       | 0.044370       | 0.044370      
4      | 0.420827       | 0.315501       | 0.337370       | 0.467654       | 0.463342       | 0.041059       | 0.041059      
5      | 0.419009       | 0.296709       | 0.311045       | 0.451984       | 0.439985       | 0.040861       | 0.040861      
6      | 0.415118       | 0.287707       | 0.296404       | 0.418549       | 0.412418       | 0.038867       | 0.038867      
7      | 0.392347       | 0.274098       | 0.290408       | 0.428606       | 0.399617       | 0.038156       | 0.038156      
8      | 0.374415       | 0.271149       | 0.288053       | 0.422899       | 0.422601       | 0.039100       | 0.039100      
9      | 0.390644       | 0.273810       | 0.291487       | 0.426133       | 0.421369       | 0.039176       | 0.039176      
10     | 0.380093       | 0.267685       | 0.283515       | 0.421578       | 0.405509       | 0.038333       | 0.038333      
11     | 0.388086       | 0.273351       | 0.294991       | 0.414951       | 0.389539       | 0.037355       | 0.037355      
12     | 0.360741       | 0.260545       | 0.281461       | 0.410859       | 0.387249       | 0.036248       | 0.036248      
13     | 0.365782       | 0.259277       | 0.279415       | 0.395752       | 0.386857       | 0.035987       | 0.035987      
14     | 0.373680       | 0.259825       | 0.276074       | 0.386006       | 0.377365       | 0.035316       | 0.035316      
15     | 0.367621       | 0.258361       | 0.272398       | 0.393288       | 0.355400       | 0.034896       | 0.034896      
16     | 0.359100       | 0.262937       | 0.271842       | 0.389242       | 0.377835       | 0.034928       | 0.034928      
17     | 0.353957       | 0.257736       | 0.266488       | 0.376255       | 0.361238       | 0.033875       | 0.033875      
18     | 0.363057       | 0.260903       | 0.273319       | 0.376890       | 0.366816       | 0.034172       | 0.034172      
19     | 0.345091       | 0.255483       | 0.271433       | 0.366812       | 0.366166       | 0.033577       | 0.033577      
20     | 0.353022       | 0.249196       | 0.262106       | 0.356059       | 0.363185       | 0.033035       | 0.033035      
21     | 0.348095       | 0.248451       | 0.260580       | 0.349725       | 0.354615       | 0.032516       | 0.032516      
22     | 0.334395       | 0.247958       | 0.256438       | 0.355974       | 0.346970       | 0.032015       | 0.032015      
23     | 0.337170       | 0.243539       | 0.261148       | 0.346330       | 0.336844       | 0.031330       | 0.031330      
24     | 0.322643       | 0.245403       | 0.250804       | 0.330210       | 0.342428       | 0.029866       | 0.029866      
25     | 0.320679       | 0.246214       | 0.257044       | 0.327470       | 0.329867       | 0.029728       | 0.029728      
26     | 0.320274       | 0.245696       | 0.257334       | 0.342842       | 0.319859       | 0.029063       | 0.029063      
27     | 0.318295       | 0.238021       | 0.250004       | 0.329869       | 0.320559       | 0.028540       | 0.028540      
28     | 0.318172       | 0.242524       | 0.249554       | 0.334904       | 0.327320       | 0.029522       | 0.029522      
29     | 0.305684       | 0.238416       | 0.253373       | 0.332875       | 0.313382       | 0.028193       | 0.028193      
30     | 0.314698       | 0.238558       | 0.245816       | 0.302894       | 0.337474       | 0.028146       | 0.028146      
31     | 0.312676       | 0.242177       | 0.258290       | 0.333502       | 0.320016       | 0.028412       | 0.028412      
32     | 0.304317       | 0.236628       | 0.246382       | 0.315107       | 0.321891       | 0.027740       | 0.027740      
33     | 0.315322       | 0.243378       | 0.254068       | 0.330860       | 0.321263       | 0.028331       | 0.028331      
34     | 0.315450       | 0.238087       | 0.247886       | 0.323666       | 0.339122       | 0.028511       | 0.028511      
35     | 0.303235       | 0.241224       | 0.251014       | 0.339190       | 0.340408       | 0.029042       | 0.029042      
36     | 0.324652       | 0.241289       | 0.252235       | 0.319251       | 0.346144       | 0.028976       | 0.028976      
37     | 0.298525       | 0.238784       | 0.252474       | 0.326941       | 0.346163       | 0.028261       | 0.028261      
38     | 0.311804       | 0.239556       | 0.252778       | 0.352837       | 0.366455       | 0.030935       | 0.030935      
39     | 0.307302       | 0.235504       | 0.251202       | 0.331060       | 0.316071       | 0.027976       | 0.027976      
40     | 0.316249       | 0.242598       | 0.246159       | 0.340179       | 0.329330       | 0.028485       | 0.028485      
41     | 0.305275       | 0.238483       | 0.246726       | 0.307993       | 0.322089       | 0.027293       | 0.027293      
42     | 0.309452       | 0.241411       | 0.245040       | 0.335697       | 0.334843       | 0.028120       | 0.028120      
43     | 0.311832       | 0.238034       | 0.244093       | 0.320804       | 0.341544       | 0.028141       | 0.028141      
44     | 0.311755       | 0.239844       | 0.244779       | 0.317624       | 0.328270       | 0.027150       | 0.027150      
45     | 0.327599       | 0.241528       | 0.252072       | 0.342747       | 0.333239       | 0.028308       | 0.028308      
46     | 0.309904       | 0.245002       | 0.249831       | 0.352804       | 0.338345       | 0.030063       | 0.030063      
47     | 0.327975       | 0.246685       | 0.251416       | 0.303137       | 0.326136       | 0.027124       | 0.027124      
48     | 0.324599       | 0.250927       | 0.260567       | 0.317493       | 0.382691       | 0.030057       | 0.030057      
49     | 0.308042       | 0.244641       | 0.252356       | 0.393948       | 0.334315       | 0.032094       | 0.032094      
50     | 0.326952       | 0.239673       | 0.249487       | 0.318788       | 0.322732       | 0.027849       | 0.027849      
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
4f. UPDATE NORM (Per Round, Per Client)
--------------------------------------------------------------------------------
Round | Client0(B) | Client1(B) | Client2(B) | Client3(B) | Client4(B) | Client5(A) | Client6(A)
--------------------------------------------------------------------------------
1      | 1.361764       | 0.606631       | 0.560976       | 1.518111       | 1.264700       | 0.883457       | 0.883457      
2      | 1.091374       | 0.456474       | 0.444832       | 1.121806       | 1.015485       | 0.700432       | 0.700432      
3      | 0.797187       | 0.343377       | 0.389968       | 0.788796       | 0.790543       | 0.487816       | 0.487816      
4      | 0.603022       | 0.313136       | 0.337406       | 0.618022       | 0.645800       | 0.359636       | 0.359636      
5      | 0.551211       | 0.282117       | 0.308799       | 0.552944       | 0.567312       | 0.295336       | 0.295336      
6      | 0.514162       | 0.263286       | 0.296725       | 0.496099       | 0.513919       | 0.254237       | 0.254237      
7      | 0.463592       | 0.265800       | 0.278044       | 0.499538       | 0.480436       | 0.229000       | 0.229000      
8      | 0.428943       | 0.260282       | 0.269350       | 0.490549       | 0.498908       | 0.216824       | 0.216824      
9      | 0.451479       | 0.267130       | 0.277108       | 0.490293       | 0.500580       | 0.222939       | 0.222939      
10     | 0.433835       | 0.261136       | 0.262002       | 0.487770       | 0.475989       | 0.211839       | 0.211839      
11     | 0.445382       | 0.269372       | 0.269707       | 0.471219       | 0.455817       | 0.205244       | 0.205244      
12     | 0.402023       | 0.255221       | 0.261483       | 0.465900       | 0.452643       | 0.194720       | 0.194720      
13     | 0.415517       | 0.252444       | 0.261641       | 0.445034       | 0.450793       | 0.193899       | 0.193899      
14     | 0.421650       | 0.258474       | 0.263441       | 0.430674       | 0.433328       | 0.189118       | 0.189118      
15     | 0.414647       | 0.255707       | 0.255188       | 0.444097       | 0.406159       | 0.185328       | 0.185328      
16     | 0.406120       | 0.258584       | 0.257160       | 0.435622       | 0.431928       | 0.186187       | 0.186187      
17     | 0.398392       | 0.260254       | 0.256499       | 0.415696       | 0.412376       | 0.180095       | 0.180095      
18     | 0.415528       | 0.262547       | 0.253551       | 0.417644       | 0.413286       | 0.181034       | 0.181034      
19     | 0.386919       | 0.255716       | 0.262829       | 0.400868       | 0.411824       | 0.172541       | 0.172541      
20     | 0.400221       | 0.248239       | 0.253634       | 0.380045       | 0.406028       | 0.167779       | 0.167779      
21     | 0.387237       | 0.251315       | 0.254182       | 0.381355       | 0.397396       | 0.167267       | 0.167267      
22     | 0.371051       | 0.245628       | 0.252349       | 0.385050       | 0.392274       | 0.163624       | 0.163624      
23     | 0.374431       | 0.242663       | 0.258014       | 0.373368       | 0.376839       | 0.159521       | 0.159521      
24     | 0.351754       | 0.252748       | 0.251172       | 0.351709       | 0.382886       | 0.154976       | 0.154976      
25     | 0.360498       | 0.255429       | 0.254976       | 0.351271       | 0.364720       | 0.156593       | 0.156593      
26     | 0.352675       | 0.254643       | 0.254859       | 0.371203       | 0.358582       | 0.157214       | 0.157214      
27     | 0.356829       | 0.239063       | 0.252763       | 0.353702       | 0.355882       | 0.153649       | 0.153649      
28     | 0.354515       | 0.249544       | 0.253737       | 0.357009       | 0.365174       | 0.156557       | 0.156557      
29     | 0.335702       | 0.243218       | 0.255319       | 0.359721       | 0.349098       | 0.150889       | 0.150889      
30     | 0.341978       | 0.246791       | 0.249078       | 0.321612       | 0.378112       | 0.150528       | 0.150528      
31     | 0.341704       | 0.249864       | 0.259815       | 0.361935       | 0.352023       | 0.151938       | 0.151938      
32     | 0.342180       | 0.240175       | 0.248929       | 0.341691       | 0.356110       | 0.152282       | 0.152282      
33     | 0.347377       | 0.245355       | 0.251176       | 0.361998       | 0.357950       | 0.153250       | 0.153250      
34     | 0.347892       | 0.243753       | 0.252275       | 0.349767       | 0.375037       | 0.155169       | 0.155169      
35     | 0.328335       | 0.247130       | 0.253913       | 0.365549       | 0.384197       | 0.156219       | 0.156219      
36     | 0.353882       | 0.246705       | 0.254377       | 0.340330       | 0.389510       | 0.155819       | 0.155819      
37     | 0.320529       | 0.243812       | 0.258532       | 0.356701       | 0.387901       | 0.155361       | 0.155361      
38     | 0.341189       | 0.239408       | 0.247136       | 0.380658       | 0.412000       | 0.159495       | 0.159495      
39     | 0.341253       | 0.241519       | 0.254275       | 0.364136       | 0.349882       | 0.155528       | 0.155528      
40     | 0.347237       | 0.243317       | 0.247119       | 0.374046       | 0.373645       | 0.160093       | 0.160093      
41     | 0.336531       | 0.245874       | 0.251968       | 0.326615       | 0.365157       | 0.151746       | 0.151746      
42     | 0.339203       | 0.244873       | 0.245954       | 0.361422       | 0.379286       | 0.156111       | 0.156111      
43     | 0.346987       | 0.242400       | 0.246985       | 0.348449       | 0.382880       | 0.158210       | 0.158210      
44     | 0.345032       | 0.245268       | 0.249430       | 0.339767       | 0.367727       | 0.153459       | 0.153459      
45     | 0.364013       | 0.247056       | 0.252741       | 0.375481       | 0.373629       | 0.163324       | 0.163324      
46     | 0.344072       | 0.248819       | 0.246710       | 0.387972       | 0.376291       | 0.160579       | 0.160579      
47     | 0.367236       | 0.250520       | 0.250683       | 0.322225       | 0.366163       | 0.153776       | 0.153776      
48     | 0.356317       | 0.251913       | 0.259547       | 0.344009       | 0.433281       | 0.165066       | 0.165066      
49     | 0.333481       | 0.246783       | 0.257313       | 0.438017       | 0.375121       | 0.168220       | 0.168220      
50     | 0.371051       | 0.247981       | 0.251748       | 0.346542       | 0.359060       | 0.160829       | 0.160829      
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
4g. PAIRWISE SQUARED DISTANCE (Per Round, Upper Triangle)
--------------------------------------------------------------------------------
Round | d(0,1) | d(0,2) | d(0,3) | d(0,4) | d(0,5) | d(0,6) | d(1,2) | d(1,3) | d(1,4) | d(1,5) | d(1,6) | d(2,3) | d(2,4) | d(2,5) | d(2,6) | d(3,4) | d(3,5) | d(3,6) | d(4,5) | d(4,6) | d(5,6)
--------------------------------------------------------------------------------
1      | 1.554941       | 1.543046       | 0.901672       | 1.749678       | 0.641418       | 0.641418       | 0.127025       | 1.842158       | 1.025643       | 0.402350       | 0.402350       | 1.956156       | 1.144003       | 0.446026       | 0.446026       | 1.731028       | 0.777326       | 0.777326       | 0.622216       | 0.622216       | 0.000000      
2      | 0.840703       | 0.994576       | 0.603934       | 0.709290       | 0.342345       | 0.342345       | 0.142419       | 0.902372       | 0.708841       | 0.231747       | 0.231747       | 1.159920       | 0.806280       | 0.333511       | 0.333511       | 0.803400       | 0.406693       | 0.406693       | 0.318533       | 0.318533       | 0.000000      
3      | 0.526831       | 0.569189       | 0.529324       | 0.559179       | 0.243937       | 0.243937       | 0.133507       | 0.522059       | 0.512019       | 0.146148       | 0.146148       | 0.645688       | 0.545673       | 0.186088       | 0.186088       | 0.607391       | 0.268070       | 0.268070       | 0.252051       | 0.252051       | 0.000000      
4      | 0.347969       | 0.357855       | 0.439784       | 0.473545       | 0.177932       | 0.177932       | 0.128455       | 0.377465       | 0.393998       | 0.103918       | 0.103918       | 0.449853       | 0.384539       | 0.118479       | 0.118479       | 0.539584       | 0.215709       | 0.215709       | 0.212546       | 0.212546       | 0.000000      
5      | 0.324449       | 0.329472       | 0.442653       | 0.453516       | 0.175812       | 0.175812       | 0.126215       | 0.340198       | 0.341361       | 0.092314       | 0.092314       | 0.389912       | 0.331540       | 0.101369       | 0.101369       | 0.505099       | 0.201281       | 0.201281       | 0.192119       | 0.192119       | 0.000000      
6      | 0.320472       | 0.312834       | 0.408069       | 0.423790       | 0.171299       | 0.171299       | 0.123042       | 0.294128       | 0.304385       | 0.086644       | 0.086644       | 0.339535       | 0.293154       | 0.091987       | 0.091987       | 0.433612       | 0.173188       | 0.173188       | 0.169245       | 0.169245       | 0.000000      
7      | 0.273777       | 0.282026       | 0.393023       | 0.400847       | 0.153742       | 0.153742       | 0.117174       | 0.305953       | 0.278324       | 0.078807       | 0.078807       | 0.354587       | 0.268581       | 0.088311       | 0.088311       | 0.430399       | 0.180495       | 0.180495       | 0.159438       | 0.159438       | 0.000000      
8      | 0.243888       | 0.252989       | 0.376244       | 0.411867       | 0.141236       | 0.141236       | 0.119395       | 0.297396       | 0.304718       | 0.077345       | 0.077345       | 0.342245       | 0.299782       | 0.087174       | 0.087174       | 0.443932       | 0.176138       | 0.176138       | 0.176294       | 0.176294       | 0.000000      
9      | 0.266432       | 0.270340       | 0.398931       | 0.423123       | 0.152963       | 0.152963       | 0.123665       | 0.292854       | 0.305931       | 0.078855       | 0.078855       | 0.349135       | 0.296818       | 0.089176       | 0.089176       | 0.448296       | 0.178897       | 0.178897       | 0.175978       | 0.175978       | 0.000000      
10     | 0.252208       | 0.251937       | 0.389350       | 0.395714       | 0.144930       | 0.144930       | 0.121150       | 0.286808       | 0.281695       | 0.075347       | 0.075347       | 0.337304       | 0.276498       | 0.084403       | 0.084403       | 0.426834       | 0.174983       | 0.174983       | 0.162997       | 0.162997       | 0.000000      
11     | 0.269155       | 0.267631       | 0.391159       | 0.386123       | 0.150357       | 0.150357       | 0.138524       | 0.278859       | 0.266487       | 0.078066       | 0.078066       | 0.342386       | 0.267007       | 0.090611       | 0.090611       | 0.400268       | 0.169842       | 0.169842       | 0.151252       | 0.151252       | 0.000000      
12     | 0.228372       | 0.232982       | 0.359421       | 0.359380       | 0.130733       | 0.130733       | 0.126833       | 0.268887       | 0.259186       | 0.071126       | 0.071126       | 0.328278       | 0.252925       | 0.082734       | 0.082734       | 0.401485       | 0.166063       | 0.166063       | 0.149064       | 0.149064       | 0.000000      
13     | 0.231708       | 0.241899       | 0.351974       | 0.362286       | 0.134086       | 0.134086       | 0.120863       | 0.254692       | 0.263046       | 0.070427       | 0.070427       | 0.305289       | 0.257259       | 0.081486       | 0.081486       | 0.378344       | 0.154408       | 0.154408       | 0.148588       | 0.148588       | 0.000000      
14     | 0.241724       | 0.250617       | 0.352668       | 0.358767       | 0.139112       | 0.139112       | 0.123792       | 0.244200       | 0.252027       | 0.070644       | 0.070644       | 0.287279       | 0.243618       | 0.079455       | 0.079455       | 0.362306       | 0.147452       | 0.147452       | 0.141615       | 0.141615       | 0.000000      
15     | 0.238200       | 0.246034       | 0.349002       | 0.331858       | 0.134643       | 0.134643       | 0.119190       | 0.258075       | 0.226153       | 0.069741       | 0.069741       | 0.297313       | 0.217236       | 0.077424       | 0.077424       | 0.350142       | 0.152131       | 0.152131       | 0.126505       | 0.126505       | 0.000000      
16     | 0.231707       | 0.236989       | 0.335461       | 0.342174       | 0.129153       | 0.129153       | 0.120845       | 0.252050       | 0.256891       | 0.072146       | 0.072146       | 0.289749       | 0.238647       | 0.077129       | 0.077129       | 0.372101       | 0.149507       | 0.149507       | 0.141748       | 0.141748       | 0.000000      
17     | 0.224697       | 0.225864       | 0.326042       | 0.322007       | 0.125142       | 0.125142       | 0.121360       | 0.235318       | 0.237585       | 0.069214       | 0.069214       | 0.271494       | 0.224275       | 0.074027       | 0.074027       | 0.338864       | 0.139596       | 0.139596       | 0.129967       | 0.129967       | 0.000000      
18     | 0.234081       | 0.248610       | 0.325128       | 0.336242       | 0.131296       | 0.131296       | 0.121629       | 0.244346       | 0.242180       | 0.071022       | 0.071022       | 0.274353       | 0.231307       | 0.077740       | 0.077740       | 0.347261       | 0.140511       | 0.140511       | 0.133902       | 0.133902       | 0.000000      
19     | 0.211402       | 0.225485       | 0.304443       | 0.320635       | 0.119212       | 0.119212       | 0.123925       | 0.229053       | 0.241507       | 0.067982       | 0.067982       | 0.264189       | 0.234081       | 0.076519       | 0.076519       | 0.334340       | 0.133053       | 0.133053       | 0.132999       | 0.132999       | 0.000000      
20     | 0.223170       | 0.226604       | 0.299053       | 0.326813       | 0.124127       | 0.124127       | 0.113352       | 0.212390       | 0.229664       | 0.064787       | 0.064787       | 0.246933       | 0.225625       | 0.071592       | 0.071592       | 0.326526       | 0.125912       | 0.125912       | 0.130803       | 0.130803       | 0.000000      
21     | 0.217620       | 0.224394       | 0.288780       | 0.312626       | 0.120473       | 0.120473       | 0.108440       | 0.210110       | 0.226876       | 0.064398       | 0.064398       | 0.242762       | 0.218856       | 0.070674       | 0.070674       | 0.307333       | 0.121520       | 0.121520       | 0.124761       | 0.124761       | 0.000000      
22     | 0.198873       | 0.205425       | 0.291066       | 0.293817       | 0.111906       | 0.111906       | 0.111530       | 0.219289       | 0.220195       | 0.063964       | 0.063964       | 0.243141       | 0.211478       | 0.068374       | 0.068374       | 0.302891       | 0.125237       | 0.125237       | 0.119556       | 0.119556       | 0.000000      
23     | 0.208595       | 0.214815       | 0.280894       | 0.281189       | 0.113178       | 0.113178       | 0.110956       | 0.203139       | 0.205432       | 0.061656       | 0.061656       | 0.239878       | 0.207616       | 0.070749       | 0.070749       | 0.290520       | 0.118821       | 0.118821       | 0.112997       | 0.112997       | 0.000000      
24     | 0.196221       | 0.192389       | 0.254846       | 0.278042       | 0.104023       | 0.104023       | 0.108518       | 0.194931       | 0.212895       | 0.062383       | 0.062383       | 0.214227       | 0.211539       | 0.065188       | 0.065188       | 0.279255       | 0.108423       | 0.108423       | 0.116064       | 0.116064       | 0.000000      
25     | 0.193719       | 0.200618       | 0.247357       | 0.266221       | 0.102755       | 0.102755       | 0.120754       | 0.187348       | 0.204986       | 0.062613       | 0.062613       | 0.220894       | 0.192003       | 0.068117       | 0.068117       | 0.271487       | 0.106471       | 0.106471       | 0.108148       | 0.108148       | 0.000000      
26     | 0.190060       | 0.190788       | 0.268528       | 0.259670       | 0.102452       | 0.102452       | 0.116765       | 0.207944       | 0.193713       | 0.062329       | 0.062329       | 0.239383       | 0.191106       | 0.068251       | 0.068251       | 0.263401       | 0.116296       | 0.116296       | 0.102176       | 0.102176       | 0.000000      
27     | 0.185751       | 0.191969       | 0.251976       | 0.257655       | 0.100973       | 0.100973       | 0.108013       | 0.190340       | 0.190401       | 0.058540       | 0.058540       | 0.219118       | 0.185038       | 0.064520       | 0.064520       | 0.260764       | 0.108100       | 0.108100       | 0.102273       | 0.102273       | 0.000000      
28     | 0.193454       | 0.185394       | 0.261585       | 0.256494       | 0.101221       | 0.101221       | 0.112075       | 0.192661       | 0.196987       | 0.060880       | 0.060880       | 0.218823       | 0.195844       | 0.064368       | 0.064368       | 0.273288       | 0.111161       | 0.111161       | 0.106477       | 0.106477       | 0.000000      
29     | 0.174350       | 0.183733       | 0.245963       | 0.238892       | 0.093672       | 0.093672       | 0.117637       | 0.191613       | 0.183555       | 0.058627       | 0.058627       | 0.223139       | 0.180020       | 0.066024       | 0.066024       | 0.261756       | 0.109533       | 0.109533       | 0.097957       | 0.097957       | 0.000000      
30     | 0.187609       | 0.182817       | 0.224003       | 0.272518       | 0.098752       | 0.098752       | 0.109290       | 0.162884       | 0.206912       | 0.058758       | 0.058758       | 0.191953       | 0.200844       | 0.062357       | 0.062357       | 0.254786       | 0.092051       | 0.092051       | 0.112397       | 0.112397       | 0.000000      
31     | 0.182531       | 0.186702       | 0.254368       | 0.251749       | 0.097903       | 0.097903       | 0.117345       | 0.195932       | 0.192169       | 0.060416       | 0.060416       | 0.229733       | 0.195340       | 0.068592       | 0.068592       | 0.257287       | 0.110179       | 0.110179       | 0.102026       | 0.102026       | 0.000000      
32     | 0.177502       | 0.177816       | 0.227298       | 0.245702       | 0.092806       | 0.092806       | 0.109102       | 0.177713       | 0.188567       | 0.057710       | 0.057710       | 0.200328       | 0.189069       | 0.062436       | 0.062436       | 0.254150       | 0.098866       | 0.098866       | 0.102628       | 0.102628       | 0.000000      
33     | 0.193028       | 0.191663       | 0.245158       | 0.251770       | 0.099229       | 0.099229       | 0.109536       | 0.196763       | 0.191998       | 0.061091       | 0.061091       | 0.224071       | 0.193006       | 0.066581       | 0.066581       | 0.261976       | 0.108596       | 0.108596       | 0.102728       | 0.102728       | 0.000000      
34     | 0.184263       | 0.182435       | 0.242069       | 0.276008       | 0.099661       | 0.099661       | 0.109976       | 0.181922       | 0.203326       | 0.058601       | 0.058601       | 0.210851       | 0.200604       | 0.063417       | 0.063417       | 0.275115       | 0.104432       | 0.104432       | 0.113730       | 0.113730       | 0.000000      
35     | 0.173693       | 0.174052       | 0.250109       | 0.258164       | 0.092706       | 0.092706       | 0.111566       | 0.195025       | 0.213157       | 0.060209       | 0.060209       | 0.226937       | 0.204659       | 0.064998       | 0.064998       | 0.290543       | 0.113864       | 0.113864       | 0.114735       | 0.114735       | 0.000000      
36     | 0.192715       | 0.196808       | 0.250034       | 0.282139       | 0.105075       | 0.105075       | 0.108882       | 0.185006       | 0.210932       | 0.060162       | 0.060162       | 0.198651       | 0.220800       | 0.065610       | 0.065610       | 0.274642       | 0.102295       | 0.102295       | 0.118202       | 0.118202       | 0.000000      
37     | 0.170005       | 0.175516       | 0.229209       | 0.260404       | 0.089873       | 0.089873       | 0.109019       | 0.187315       | 0.214128       | 0.058885       | 0.058885       | 0.214506       | 0.215368       | 0.065669       | 0.065669       | 0.286945       | 0.106309       | 0.106309       | 0.118223       | 0.118223       | 0.000000      
38     | 0.176451       | 0.175467       | 0.269842       | 0.292026       | 0.098358       | 0.098358       | 0.108342       | 0.206413       | 0.229441       | 0.059708       | 0.059708       | 0.234202       | 0.235317       | 0.066265       | 0.066265       | 0.328219       | 0.123361       | 0.123361       | 0.132409       | 0.132409       | 0.000000      
39     | 0.175170       | 0.185231       | 0.243075       | 0.243629       | 0.094622       | 0.094622       | 0.108437       | 0.193504       | 0.183192       | 0.057294       | 0.057294       | 0.220069       | 0.184160       | 0.064894       | 0.064894       | 0.259536       | 0.108519       | 0.108519       | 0.099494       | 0.099494       | 0.000000      
40     | 0.186660       | 0.183337       | 0.260331       | 0.261946       | 0.100044       | 0.100044       | 0.109225       | 0.200086       | 0.200235       | 0.060765       | 0.060765       | 0.223091       | 0.189346       | 0.062574       | 0.062574       | 0.281528       | 0.114613       | 0.114613       | 0.108064       | 0.108064       | 0.000000      
41     | 0.180508       | 0.179188       | 0.220685       | 0.248400       | 0.093394       | 0.093394       | 0.108512       | 0.173161       | 0.192441       | 0.058526       | 0.058526       | 0.197262       | 0.190118       | 0.062633       | 0.062633       | 0.244199       | 0.094601       | 0.094601       | 0.102574       | 0.102574       | 0.000000      
42     | 0.183717       | 0.175463       | 0.251972       | 0.257659       | 0.096095       | 0.096095       | 0.104468       | 0.197245       | 0.202965       | 0.060106       | 0.060106       | 0.216820       | 0.201006       | 0.061941       | 0.061941       | 0.281948       | 0.112008       | 0.112008       | 0.111116       | 0.111116       | 0.000000      
43     | 0.185659       | 0.179898       | 0.235607       | 0.268738       | 0.097457       | 0.097457       | 0.102909       | 0.180958       | 0.205603       | 0.058486       | 0.058486       | 0.201467       | 0.206159       | 0.061551       | 0.061551       | 0.278410       | 0.102647       | 0.102647       | 0.115198       | 0.115198       | 0.000000      
44     | 0.181462       | 0.183137       | 0.238735       | 0.256297       | 0.097083       | 0.097083       | 0.105871       | 0.181362       | 0.201113       | 0.059159       | 0.059159       | 0.199256       | 0.193591       | 0.061644       | 0.061644       | 0.258033       | 0.100557       | 0.100557       | 0.106988       | 0.106988       | 0.000000      
45     | 0.197284       | 0.198942       | 0.275127       | 0.270196       | 0.107358       | 0.107358       | 0.106541       | 0.202624       | 0.199251       | 0.060253       | 0.060253       | 0.224023       | 0.201734       | 0.065372       | 0.065372       | 0.286133       | 0.116656       | 0.116656       | 0.110485       | 0.110485       | 0.000000      
46     | 0.181527       | 0.180018       | 0.264956       | 0.261815       | 0.096702       | 0.096702       | 0.107388       | 0.220930       | 0.205536       | 0.062249       | 0.062249       | 0.233437       | 0.206616       | 0.064626       | 0.064626       | 0.299027       | 0.122655       | 0.122655       | 0.113761       | 0.113761       | 0.000000      
47     | 0.206001       | 0.204073       | 0.232968       | 0.270370       | 0.106621       | 0.106621       | 0.113637       | 0.174434       | 0.198390       | 0.062490       | 0.062490       | 0.191180       | 0.195097       | 0.064838       | 0.064838       | 0.243800       | 0.092522       | 0.092522       | 0.105577       | 0.105577       | 0.000000      
48     | 0.194729       | 0.197900       | 0.244853       | 0.319879       | 0.105968       | 0.105968       | 0.117178       | 0.181496       | 0.260396       | 0.065219       | 0.065219       | 0.203282       | 0.259109       | 0.070021       | 0.070021       | 0.304852       | 0.101426       | 0.101426       | 0.143416       | 0.143416       | 0.000000      
49     | 0.176658       | 0.176834       | 0.302414       | 0.254187       | 0.096147       | 0.096147       | 0.104871       | 0.260919       | 0.198317       | 0.062289       | 0.062289       | 0.281667       | 0.198165       | 0.066435       | 0.066435       | 0.339459       | 0.151174       | 0.151174       | 0.112095       | 0.112095       | 0.000000      
50     | 0.195143       | 0.196139       | 0.252087       | 0.270097       | 0.106326       | 0.106326       | 0.111285       | 0.182709       | 0.189325       | 0.059290       | 0.059290       | 0.204063       | 0.190319       | 0.064015       | 0.064015       | 0.251155       | 0.101430       | 0.101430       | 0.103621       | 0.103621       | 0.000000      
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
4h. PAIRWISE COSINE (Per Round, Upper Triangle)
--------------------------------------------------------------------------------
Round | c(0,1) | c(0,2) | c(0,3) | c(0,4) | c(0,5) | c(0,6) | c(1,2) | c(1,3) | c(1,4) | c(1,5) | c(1,6) | c(2,3) | c(2,4) | c(2,5) | c(2,6) | c(3,4) | c(3,5) | c(3,6) | c(4,5) | c(4,6) | c(5,6)
--------------------------------------------------------------------------------
1      | 0.403994       | 0.409766       | 0.787847       | 0.494773       | 0.828518       | 0.828518       | 0.816432       | 0.450911       | 0.613809       | 0.696131       | 0.696131       | 0.389379       | 0.542777       | 0.654940       | 0.654940       | 0.565934       | 0.860387       | 0.860387       | 0.786614       | 0.786614       | 1.000003      
2      | 0.560809       | 0.406198       | 0.753750       | 0.682612       | 0.876064       | 0.876064       | 0.649651       | 0.551143       | 0.572490       | 0.730676       | 0.730676       | 0.296994       | 0.468001       | 0.569649       | 0.569649       | 0.652350       | 0.854210       | 0.854210       | 0.845877       | 0.845877       | 1.000004      
3      | 0.413881       | 0.351261       | 0.579185       | 0.556405       | 0.809440       | 0.809440       | 0.509600       | 0.402528       | 0.425213       | 0.626040       | 0.626040       | 0.209013       | 0.375242       | 0.536069       | 0.536069       | 0.512993       | 0.769394       | 0.769394       | 0.792043       | 0.792043       | 0.999998      
4      | 0.301129       | 0.293974       | 0.410285       | 0.394364       | 0.726364       | 0.726364       | 0.394890       | 0.264932       | 0.299464       | 0.548226       | 0.548226       | 0.110159       | 0.335858       | 0.513850       | 0.513850       | 0.325005       | 0.664951       | 0.664951       | 0.718736       | 0.718736       | 1.000000      
5      | 0.189624       | 0.204801       | 0.273847       | 0.275281       | 0.661118       | 0.661118       | 0.279697       | 0.144683       | 0.187673       | 0.447084       | 0.447084       | 0.032773       | 0.244489       | 0.445250       | 0.445250       | 0.195245       | 0.586925       | 0.586925       | 0.647439       | 0.647439       | 1.000005      
6      | 0.048795       | 0.129699       | 0.200744       | 0.198093       | 0.603216       | 0.603216       | 0.219674       | 0.081560       | 0.107338       | 0.353413       | 0.353413       | -0.018259      | 0.193470       | 0.402293       | 0.402293       | 0.150255       | 0.545348       | 0.545348       | 0.610409       | 0.610409       | 1.000000      
7      | 0.047842       | 0.039566       | 0.154232       | 0.100775       | 0.535122       | 0.535122       | 0.208275       | 0.053604       | 0.090623       | 0.363776       | 0.363776       | -0.099865      | 0.148024       | 0.325413       | 0.325413       | 0.104084       | 0.531005       | 0.531005       | 0.562740       | 0.562740       | 1.000005      
8      | 0.035162       | 0.015375       | 0.114982       | 0.049147       | 0.482613       | 0.482613       | 0.149066       | 0.043036       | 0.045969       | 0.331486       | 0.331486       | -0.109960      | 0.080654       | 0.277289       | 0.277289       | 0.093196       | 0.524223       | 0.524223       | 0.552949       | 0.552949       | 1.000005      
9      | 0.036317       | 0.041094       | 0.102302       | 0.069228       | 0.499617       | 0.499617       | 0.165373       | 0.072124       | 0.059855       | 0.354357       | 0.354357       | -0.117616      | 0.110122       | 0.302014       | 0.302014       | 0.086933       | 0.508642       | 0.508642       | 0.556937       | 0.556937       | 1.000002      
10     | 0.018524       | 0.021644       | 0.086913       | 0.046161       | 0.479645       | 0.479645       | 0.114645       | 0.075777       | 0.052548       | 0.340950       | 0.340950       | -0.120270      | 0.075026       | 0.262317       | 0.262317       | 0.081086       | 0.521709       | 0.521709       | 0.537755       | 0.537755       | 1.000007      
11     | 0.007385       | 0.014468       | 0.069695       | 0.049289       | 0.493022       | 0.493022       | 0.046656       | 0.062044       | 0.056377       | 0.331190       | 0.331190       | -0.187260      | 0.054926       | 0.219097       | 0.219097       | 0.068788       | 0.487685       | 0.487685       | 0.527216       | 0.527216       | 1.000001      
12     | -0.007856      | -0.014207      | 0.051426       | 0.019587       | 0.439483       | 0.439483       | 0.050032       | 0.055987       | 0.046906       | 0.321232       | 0.321232       | -0.175840      | 0.085901       | 0.231314       | 0.231314       | 0.048519       | 0.490068       | 0.490068       | 0.531774       | 0.531774       | 1.000000      
13     | 0.022280       | -0.003627      | 0.050659       | 0.036257       | 0.472685       | 0.472685       | 0.085700       | 0.031564       | 0.017121       | 0.315621       | 0.315621       | -0.166520      | 0.061096       | 0.242131       | 0.242131       | 0.057141       | 0.470766       | 0.470766       | 0.527554       | 0.527554       | 1.000004      
14     | 0.013184       | -0.015427      | 0.029188       | 0.018595       | 0.466783       | 0.466783       | 0.091186       | 0.036332       | 0.011405       | 0.326617       | 0.326617       | -0.142776      | 0.059378       | 0.258042       | 0.258042       | 0.029330       | 0.453023       | 0.453023       | 0.499853       | 0.499853       | 0.999998      
15     | -0.004159      | -0.042435      | 0.054720       | 0.014961       | 0.466115       | 0.466115       | 0.086719       | 0.019960       | 0.020209       | 0.316442       | 0.316442       | -0.154290      | 0.061988       | 0.233059       | 0.233059       | 0.033389       | 0.482603       | 0.482603       | 0.483633       | 0.483633       | 1.000001      
16     | 0.000440       | -0.028365      | 0.054375       | 0.026569       | 0.465834       | 0.465834       | 0.091374       | 0.020339       | -0.015503      | 0.305181       | 0.305181       | -0.151095      | 0.063228       | 0.247164       | 0.247164       | 0.011234       | 0.461901       | 0.461901       | 0.494173       | 0.494173       | 1.000003      
17     | 0.008446       | -0.006634      | 0.016537       | 0.020584       | 0.460014       | 0.460014       | 0.091110       | 0.024114       | 0.000937       | 0.330196       | 0.330196       | -0.154276      | 0.054693       | 0.261927       | 0.261927       | 0.011647       | 0.438412       | 0.438412       | 0.488259       | 0.488259       | 1.000009      
18     | 0.034434       | -0.055330      | 0.063277       | 0.021041       | 0.492811       | 0.492811       | 0.087054       | -0.004511      | -0.011264      | 0.322773       | 0.322773       | -0.168279      | 0.018064       | 0.210473       | 0.210473       | -0.005877      | 0.441030       | 0.441030       | 0.465649       | 0.465649       | 0.999996      
19     | 0.018676       | -0.032938      | 0.019209       | -0.004173      | 0.451377       | 0.451377       | 0.078446       | -0.014472      | -0.030947      | 0.308004       | 0.308004       | -0.163327      | 0.021234       | 0.246214       | 0.246214       | -0.012254      | 0.415046       | 0.415046       | 0.467040       | 0.467040       | 1.000002      
20     | -0.006896      | -0.010326      | 0.018271       | -0.005467      | 0.478051       | 0.478051       | 0.100069       | -0.033568      | -0.015787      | 0.299952       | 0.299952       | -0.197988      | 0.017306       | 0.245432       | 0.245432       | -0.055841      | 0.365991       | 0.365991       | 0.456581       | 0.456581       | 1.000003      
21     | -0.023162      | -0.049949      | 0.022360       | -0.015433      | 0.443547       | 0.443547       | 0.151284       | -0.007925      | -0.029002      | 0.318059       | 0.318059       | -0.168789      | 0.018201       | 0.257702       | 0.257702       | -0.013121      | 0.406744       | 0.406744       | 0.459922       | 0.459922       | 0.999999      
22     | -0.004726      | -0.021716      | -0.017932      | -0.007762      | 0.432752       | 0.432752       | 0.100696       | -0.056527      | -0.031050      | 0.287912       | 0.287912       | -0.160540      | 0.030716       | 0.267361       | 0.267361       | -0.002479      | 0.395220       | 0.395220       | 0.475945       | 0.475945       | 1.000001      
23     | -0.052336      | -0.041642      | -0.004618      | 0.003604       | 0.439220       | 0.439220       | 0.115802       | -0.026761      | -0.024820      | 0.292908       | 0.292908       | -0.175966      | 0.004952       | 0.258386       | 0.258386       | -0.032370      | 0.386428       | 0.386428       | 0.452967       | 0.452967       | 1.000003      
24     | -0.048416      | -0.031531      | -0.029976      | -0.028625      | 0.401062       | 0.401062       | 0.145326       | -0.041348      | -0.012463      | 0.325716       | 0.325716       | -0.155318      | -0.009621      | 0.281533       | 0.281533       | -0.033250      | 0.360454       | 0.360454       | 0.459711       | 0.459711       | 1.000005      
25     | 0.008059       | -0.030713      | 0.023662       | -0.012327      | 0.458149       | 0.458149       | 0.072954       | 0.007174       | -0.036074      | 0.339428       | 0.339428       | -0.181382      | 0.032423       | 0.268203       | 0.268203       | -0.058834      | 0.376702       | 0.376702       | 0.432440       | 0.432440       | 1.000003      
26     | -0.004658      | -0.008097      | -0.024277      | -0.026524      | 0.420640       | 0.420640       | 0.100395       | -0.028087      | -0.001583      | 0.340105       | 0.340105       | -0.193641      | 0.013284       | 0.267284       | 0.267284       | 0.011163       | 0.395946       | 0.395946       | 0.453425       | 0.453425       | 1.000007      
27     | -0.007466      | -0.004177      | 0.001805       | -0.014476      | 0.455645       | 0.455645       | 0.107796       | -0.047807      | -0.038780      | 0.302458       | 0.302458       | -0.168479      | 0.030586       | 0.295823       | 0.295823       | -0.035776      | 0.373655       | 0.373655       | 0.438807       | 0.438807       | 1.000006      
28     | -0.031088      | 0.025953       | -0.033378      | 0.009805       | 0.441166       | 0.441166       | 0.115129       | -0.016464      | -0.007481      | 0.331513       | 0.331513       | -0.148949      | 0.010196       | 0.308683       | 0.308683       | -0.047869      | 0.365040       | 0.365040       | 0.449413       | 0.449413       | 1.000001      
29     | -0.015305      | -0.034122      | -0.016017      | -0.018459      | 0.412530       | 0.412530       | 0.053992       | -0.017483      | -0.014903      | 0.317392       | 0.317392       | -0.155442      | 0.039478       | 0.284641       | 0.284641       | -0.041759      | 0.392738       | 0.392738       | 0.443101       | 0.443101       | 1.000002      
30     | -0.057787      | -0.022472      | -0.016457      | -0.048724      | 0.396841       | 0.396841       | 0.111076       | 0.009172       | -0.016273      | 0.333891       | 0.333891       | -0.165278      | 0.022109       | 0.297942       | 0.297942       | -0.034468      | 0.351601       | 0.351601       | 0.467629       | 0.467629       | 1.000010      
31     | -0.019546      | -0.013720      | -0.026724      | -0.046002      | 0.403956       | 0.403956       | 0.096974       | -0.013841      | -0.033066      | 0.330599       | 0.330599       | -0.166067      | -0.021406      | 0.278623       | 0.278623       | -0.009302      | 0.399189       | 0.399189       | 0.420485       | 0.420485       | 0.999999      
32     | -0.016611      | 0.007259       | 0.027977       | -0.007390      | 0.455522       | 0.455522       | 0.088206       | -0.019964      | -0.023787      | 0.316674       | 0.316674       | -0.127035      | -0.001635      | 0.299675       | 0.299675       | -0.043489      | 0.394720       | 0.394720       | 0.436822       | 0.436822       | 1.000005      
33     | -0.071325      | -0.045288      | 0.026065       | -0.011949      | 0.421983       | 0.421983       | 0.111581       | -0.031085      | -0.020900      | 0.300452       | 0.300452       | -0.164637      | -0.009948      | 0.259716       | 0.259716       | -0.010824      | 0.413986       | 0.413986       | 0.445591       | 0.445591       | 1.000002      
34     | -0.022520      | 0.012744       | 0.005331       | -0.054903      | 0.420941       | 0.420941       | 0.106375       | -0.000994      | -0.017819      | 0.329062       | 0.329062       | -0.140936      | 0.019512       | 0.310427       | 0.310427       | -0.046217      | 0.386776       | 0.386776       | 0.438201       | 0.438201       | 1.000000      
35     | -0.029673      | -0.010651      | -0.036155      | -0.010912      | 0.385080       | 0.385080       | 0.111390       | -0.001802      | -0.023576      | 0.327270       | 0.327270       | -0.155354      | 0.038028       | 0.300996       | 0.300996       | -0.033145      | 0.386722       | 0.386722       | 0.477165       | 0.477165       | 1.000007      
36     | -0.037910      | -0.038149      | -0.037268      | -0.018821      | 0.402944       | 0.402944       | 0.132966       | -0.049538      | 0.008583       | 0.324923       | 0.324923       | -0.104650      | -0.022075      | 0.294901       | 0.294901       | -0.026780      | 0.356500       | 0.356500       | 0.476146       | 0.476146       | 1.000005      
37     | -0.050044      | -0.035829      | 0.003346       | -0.028945      | 0.371544       | 0.371544       | 0.136943       | -0.003653      | -0.022288      | 0.326005       | 0.326005       | -0.110781      | 0.009664       | 0.315037       | 0.315037       | -0.033398      | 0.406594       | 0.406594       | 0.467797       | 0.467797       | 1.000008      
38     | -0.016676      | 0.011974       | -0.032847      | -0.020888      | 0.399608       | 0.399608       | 0.084937       | -0.023024      | -0.012072      | 0.301794       | 0.301794       | -0.150021      | -0.022087      | 0.256867       | 0.256867       | -0.043280      | 0.386897       | 0.386897       | 0.477655       | 0.477655       | 1.000002      
39     | -0.002337      | -0.023753      | 0.024037       | -0.019927      | 0.433559       | 0.433559       | 0.118468       | -0.014656      | -0.014457      | 0.335793       | 0.335793       | -0.123225      | 0.016373       | 0.302819       | 0.302819       | -0.017752      | 0.426129       | 0.426129       | 0.432892       | 0.432892       | 1.000000      
40     | -0.040730      | -0.009877      | 0.000590       | -0.006788      | 0.415187       | 0.415187       | 0.091857       | -0.005339      | -0.007815      | 0.308939       | 0.308939       | -0.119615      | 0.061370       | 0.304890       | 0.304890       | -0.007181      | 0.425245       | 0.425245       | 0.477931       | 0.477931       | 1.000003      
41     | -0.041097      | -0.014432      | -0.003432      | -0.007356      | 0.419913       | 0.419913       | 0.124532       | -0.037545      | 0.007533       | 0.334429       | 0.334429       | -0.164630      | 0.036460       | 0.312313       | 0.312313       | -0.017535      | 0.354137       | 0.354137       | 0.485405       | 0.485405       | 1.000006      
42     | -0.052348      | 0.000530       | -0.025642      | 0.004888       | 0.409179       | 0.409179       | 0.132733       | -0.037605      | 0.004609       | 0.316896       | 0.316896       | -0.144562      | 0.017933       | 0.298511       | 0.298511       | -0.027225      | 0.380961       | 0.380961       | 0.482292       | 0.482292       | 1.000004      
43     | -0.038649      | 0.008776       | 0.025679       | -0.006553      | 0.436950       | 0.436950       | 0.140731       | -0.004636      | -0.001334      | 0.329895       | 0.329895       | -0.110668      | 0.007612       | 0.313267       | 0.313267       | -0.038962      | 0.397271       | 0.397271       | 0.465788       | 0.465788       | 1.000003      
44     | -0.013344      | -0.010893      | -0.018111      | -0.007986      | 0.429802       | 0.429802       | 0.134863       | -0.034581      | -0.031785      | 0.326101       | 0.326101       | -0.127435      | 0.020976       | 0.315093       | 0.315093       | -0.029489      | 0.368576       | 0.368576       | 0.458845       | 0.458845       | 1.000003      
45     | -0.020803      | -0.013907      | -0.005981      | 0.007017       | 0.435846       | 0.435846       | 0.147133       | -0.003238      | 0.007502       | 0.340265       | 0.340265       | -0.100947      | 0.009225       | 0.305019       | 0.305019       | -0.019775      | 0.415868       | 0.415868       | 0.457127       | 0.457127       | 1.000005      
46     | -0.007189      | -0.004516      | 0.014801       | -0.007086      | 0.429589       | 0.429589       | 0.125343       | -0.044009      | -0.010845      | 0.318454       | 0.318454       | -0.115180      | -0.022381      | 0.277987       | 0.277987       | -0.023667      | 0.430610       | 0.430610       | 0.443695       | 0.443695       | 1.000002      
47     | -0.045537      | -0.034591      | 0.024187       | -0.005324      | 0.459426       | 0.459426       | 0.095266       | -0.048588      | -0.008472      | 0.310427       | 0.310427       | -0.151712      | 0.009918       | 0.280827       | 0.280827       | -0.024986      | 0.352722       | 0.352722       | 0.463058       | 0.463058       | 1.000004      
48     | -0.023994      | -0.019320      | 0.001839       | -0.016793      | 0.410108       | 0.410108       | 0.104364       | 0.001768       | -0.042164      | 0.306483       | 0.306483       | -0.098419      | -0.017841      | 0.286991       | 0.286991       | 0.004100       | 0.388873       | 0.388873       | 0.500311       | 0.500311       | 0.999998      
49     | -0.027627      | 0.003411       | 0.002239       | -0.009041      | 0.386481       | 0.386481       | 0.175127       | -0.037738      | 0.017827       | 0.324123       | 0.324123       | -0.104689      | 0.045382       | 0.324290       | 0.324290       | -0.020951      | 0.468118       | 0.468118       | 0.451009       | 0.451009       | 1.000002      
50     | 0.021899       | 0.026319       | 0.022100       | -0.013113      | 0.479428       | 0.479428       | 0.108820       | -0.006534      | 0.006143       | 0.351919       | 0.351919       | -0.118036      | 0.010965       | 0.311559       | 0.311559       | -0.008599      | 0.399467       | 0.399467       | 0.443059       | 0.443059       | 1.000003      
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
🛡️  SHADOW DEFENSE SUMMARY (computed only, NOT applied)
  Parameters: n=7, f=2, k=3, m=5, beta=2, rounds=50
  Krum        : attacker selection rate = 1.0000   (chance = A/n = 0.2857)   [rounds where the selected update is malicious]
  Multi-Krum  : DR = 0.0000  FPR = 0.4000  ER = 1.0000   (chance DR = FPR = (n-m)/n = 0.2857)
  Trimmed Mean: DR = 0.0825  FPR = 0.7670  ER = 0.9175   (chance = 2*beta/n = 0.5714)   [DR/FPR = mean trim fraction over attacker/benign submissions]
  Median      : attacker provider rate = 0.4175  attacker total influence = 0.8350  benign provider rate = 0.0330   (chance per client = 1/n = 0.1429)   [no rejection step: DR/FPR n/a]
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
💾 SAVING DATA TO CSV FILES FOR EASY COLLECTION
--------------------------------------------------------------------------------
✅ Global Accuracy saved to: results/qwen_ag_news_alie_alpha0p3_seed42069_shadow_global_accuracy.csv
✅ Cosine Similarity saved to: results/qwen_ag_news_alie_alpha0p3_seed42069_shadow_cosine_similarity.csv
✅ Local Accuracy saved to: results/qwen_ag_news_alie_alpha0p3_seed42069_shadow_local_accuracy.csv

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
         1    0.000     0.00      0.00      0      0.00    0.00      0.04        -     120.82      0.17       6.92       8.59     136.58
         2    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.31      0.11       6.94       8.01     134.47
         3    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.55      0.11       6.94       7.62     134.36
         4    0.000     0.00      0.00      0      0.00    0.00      0.05        -     119.55      0.11       6.94       7.59     134.29
         5    0.000     0.00      0.00      0      0.00    0.00      0.05        -     119.55      0.11       6.93       7.62     134.33
         6    0.000     0.00      0.00      0      0.00    0.00      0.05        -     119.46      0.11       6.93       7.58     134.22
         7    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.56      0.11       6.93       7.57     134.27
         8    0.000     0.00      0.00      0      0.00    0.00      0.05        -     119.51      0.11       6.93       7.56     134.22
         9    0.000     0.00      0.00      0      0.00    0.00      0.03        -     119.50      0.11       6.93       7.58     134.21
        10    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.51      0.11       6.93       7.57     134.24
        11    0.000     0.00      0.00      0      0.00    0.00      0.05        -     119.53      0.11       6.93       7.59     134.29
        12    0.000     0.00      0.00      0      0.00    0.00      0.05        -     119.52      0.10       6.93       7.55     134.24
        13    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.41      0.11       6.93       7.54     134.09
        14    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.30      0.11       6.93       7.60     134.03
        15    0.000     0.00      0.00      0      0.00    0.00      0.03        -     119.36      0.11       6.93       7.54     134.04
        16    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.38      0.11       6.93       7.59     134.12
        17    0.000     0.00      0.00      0      0.00    0.00      0.03        -     119.24      0.11       6.94       7.60     133.98
        18    0.000     0.00      0.00      0      0.00    0.00      0.05        -     119.20      0.11       6.93       7.62     133.98
        19    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.24      0.11       6.94       7.59     133.99
        20    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.26      0.11       6.93       7.57     133.97
        21    0.000     0.00      0.00      0      0.00    0.00      0.05        -     119.20      0.10       6.94       7.61     133.98
        22    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.21      0.11       6.93       7.55     133.90
        23    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.31      0.15       6.93       7.63     134.12
        24    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.22      0.11       6.93       7.56     133.93
        25    0.000     0.00      0.00      0      0.00    0.00      0.05        -     119.21      0.12       6.93       7.59     134.00
        26    0.000     0.00      0.00      0      0.00    0.00      0.05        -     119.21      0.14       6.93       7.57     133.99
        27    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.20      0.11       6.93       7.58     133.93
        28    0.000     0.00      0.00      0      0.00    0.00      0.05        -     119.25      0.11       6.93       7.60     134.00
        29    0.000     0.00      0.00      0      0.00    0.00      0.03        -     119.53      0.11       6.94       7.59     134.26
        30    0.000     0.00      0.00      0      0.00    0.00      0.05        -     119.52      0.12       6.93       7.56     134.25
        31    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.29      0.11       6.94       7.64     134.08
        32    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.23      0.11       6.93       7.59     133.98
        33    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.23      0.11       6.94       7.62     134.00
        34    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.23      0.11       6.94       7.61     134.01
        35    0.000     0.00      0.00      0      0.00    0.00      0.05        -     119.43      0.10       6.94       7.59     134.19
        36    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.28      0.11       6.94       7.59     134.04
        37    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.33      0.11       6.94       7.61     134.09
        38    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.28      0.11       6.94       7.58     134.01
        39    0.000     0.00      0.00      0      0.00    0.00      0.05        -     119.31      0.11       6.94       7.60     134.07
        40    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.30      0.11       6.94       7.62     134.07
        41    0.000     0.00      0.00      0      0.00    0.00      0.05        -     119.37      0.11       6.94       7.65     134.20
        42    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.31      0.12       6.94       7.62     134.10
        43    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.32      0.11       6.94       7.62     134.09
        44    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.30      0.11       6.94       7.60     134.05
        45    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.33      0.11       6.94       7.60     134.08
        46    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.34      0.11       6.94       7.56     134.06
        47    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.34      0.11       6.94       7.60     134.09
        48    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.28      0.11       6.94       7.58     134.01
        49    0.000     0.00      0.00      0      0.00    0.00      0.03        -     119.33      0.11       6.94       7.62     134.09
        50    0.000     0.00      0.00      0      0.00    0.00      0.04        -     119.45      0.13       6.94       7.58     134.19
----------------------------------------------------------------------------------------------------------------------------------------
 mean r>=2    0.000     0.00      0.00    0.0      0.00    0.00      0.04        -     119.35      0.11       6.93       7.60     134.11
  std r>=2    0.000     0.00      0.00    0.0      0.00    0.00      0.01        -       0.12      0.01       0.00       0.06       0.13
  mean all    0.000     0.00      0.00    0.0      0.00    0.00      0.04        -     119.38      0.11       6.93       7.62     134.16
   sum all    0.000     0.00      0.00    0.0      0.00    0.00      2.08        -    5968.91      5.64     346.71     380.98    6707.78
----------------------------------------------------------------------------------------------------------------------------------------

Wall-clock totals (s): setup_and_initial_eval_sec 17.5, rounds_sec 6726.5, experiment_sec 6744.0, rounds_completed 50.0
Overhead per round saved to: results/qwen_ag_news_alie_alpha0p3_seed42069_shadow_overhead_rounds.csv
Overhead per attacker-round saved to: results/qwen_ag_news_alie_alpha0p3_seed42069_shadow_overhead_attackers.csv

============================================================
Generating Visualization Plots
============================================================

============================================================
Generating Visualization Figures
============================================================

📊 Generating Figure 1: Global Accuracy Stability...
  ✅ Saved Figure 3 to: results/qwen_ag_news_alie_alpha0p3_seed42069_shadow_figure1.png
📊 Generating Figure 2: Cosine Similarity...
  ✅ Saved Figure 4 to: results/qwen_ag_news_alie_alpha0p3_seed42069_shadow_figure2.png
📊 Generating Figure 3: Local accuracy by client...
  ✅ Saved Figure 6 to: results/qwen_ag_news_alie_alpha0p3_seed42069_shadow_figure3.png
📊 Generating Figure 4: Euclidean Distance...
  ✅ Saved Figure 4 to: results/qwen_ag_news_alie_alpha0p3_seed42069_shadow_figure4.png
📊 Generating Figure 5: Global Loss...
  ✅ Saved Global Loss figure to: results/qwen_ag_news_alie_alpha0p3_seed42069_shadow_figure5.png

✅ All available figures generated successfully!
   Output directory: results

⏱️  Total wall-clock incl. figures/checkpoint/downstream: 6745.8s (FL rounds 6726.5s, setup+initial eval 17.5s)

==================================================
Experiment Summary
==================================================
Total Rounds: 50
Final Clean Accuracy: 0.9130
Best Clean Accuracy: 0.9130
Accuracy Change: +0.4563

✅ Experiment completed successfully!
Full log saved to: results/qwen_ag_news_alie_alpha0p3_seed42069_shadow_log.txt (1968 KB)