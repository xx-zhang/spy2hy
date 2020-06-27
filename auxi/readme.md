# auxiliary-APP (辅助脚本)

## 2020-6-26
- [local_main.py](./local_main.py)
  - 本文件记录的是本地测试的核心函数。
  - 可以随意修改和测试进行运行。
- `data` 目录对应的是数据集,例如 `header`
- `deploments` 对应的是部署相关的教程


## 2020-6-27
- 使用火狐浏览器保存了 `headers` 和 `cookies`后用requests编辑重发测试。

## 重点说明
- 1. 脚本如果不连接数据库直接备份到对应的文件夹即可，后面用文件读取再集中处理到csv/txt
- 2. 多线程的使用说明在 `spy_util/muti_thread_spy.py` 中
- 3. 免费代理池的使用说明在 `spy_util/proxy_pool.py` 中
- NOTE: spyder.py 当前已经修改为单一测试脚本的接口。
     - 当前出现了问题，无法对这个编辑重发成功。
     -
