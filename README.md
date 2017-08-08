# taobao_scrapy
This is a crawler that crawls out taobao merchandise data!

## 使用说明
```
[yuchaoshui@localhost taobao_scrapy $] ./taobao_scrapy.py -k 超短裙 -k 貂皮大衣 -p 5
getting page...0
getting page...1
getting page...2
getting page...3
getting page...4
getting page...0
getting page...1
getting page...2
getting page...3
getting page...4
[yuchaoshui@localhost taobao_scrapy $]
```

`-k`: 表示搜索关键词， 多个关键词多次指定 <br>
`-p`: 搜索结果页数


```
[yuchaoshui@localhost taobao_scrapy $] ls -l ./data
-rw-rw-r-- 1 yuchaoshui yuchaoshui   8094 Aug  8 11:41 貂皮大衣.txt
-rw-rw-r-- 1 yuchaoshui yuchaoshui   8155 Aug  8 11:41 超短裙.txt

[yuchaoshui@localhost taobao_scrapy $] head ./data/超短裙.txt

hzp926388:      2017夏季新款齐比 齐B小短裙 超短裙 开档裙裤 开裆短裤 包臀露臀
horasora:       HORASORA 0703超模同款！漆皮性感侧镂空超短裙 LKB-64
雅莹旗舰店:      雅莹春季专柜百搭舒适蕾丝半裙
vicky_lam193:   下身裙子女2017新款夏a字chic风半身裙短裙 不规则A型信封裙裤裙
vilin0013:      【VKBANG】正品Ann teano 明星同款 黑色百搭时髦显瘦百褶裙裤裙
铁蝴蝶33:        夏季百搭复古性感拼色百褶超短半身裙
千衣百酷旗舰店:   韩版学生高腰破洞包臀牛仔a字裙
charmmy4:       CHARMMYCHARMAY 2017s/s 限量粉色百褶裙
中国戴先森:      夏季淑女高腰不规则超短裙
happysunny1019: 花朵刺绣A字显瘦半身裙女包臀  黑色复古民族风绣花小A型迷你短裙

```
## 备注

各位 `Pythoner` 可根据实际情况修改 `taobao_scrapy.py` 代码，取自己所需字段。


