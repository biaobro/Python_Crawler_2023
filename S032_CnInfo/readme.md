## 说明

- 这个网站有个接口叫 spidercheck，会定期向 https://webapi.cninfo.com.cn/api/spidercheck 发送 空的POST请求
- 这个网站实现【数据下载】也比较有趣，不是后端生成文件，而是前端生成，调用了1个 URL.createObjectURL(csvData)，参见 json2csv_full.js，因为只下载当天的数据，性能看起来也OK。看起来在数据量不大的场合，也可以使用
- 没有分页加载，1个接口就返回当天的全部数据 —— ke'neng