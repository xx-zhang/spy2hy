# 工具箱

## 解读接口和爬取思路。

```
API 解读过程
1. 首先发现全国的URL列表存在位置在
    - https://static.122.gov.cn/V1.18.4/static/js/funcDistrict.js
2. 针对单个zf机构的列表查询，我们可以发现。这里有一个列表和时间的查询。
    - https://{city_short}.122.gov.cn/m/viopub/getVioPubList
    - NOTE: city_short 对应的就是之前的bj、tj等（省市的缩写）
3. 获取详情
    - NOTE: 针对每一个列表查看详情后, 可以得到一个详情介绍的Json（页面上渲染出的内容）
    - https://{city_short}.122.gov.cn/m/viopub/getVioPubDetail  POST
```
