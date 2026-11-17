# 海关门户代理申报的多步骤 RPA 恢复与回执归属资料服务

项目接收 customs-portal 来源资料，现有目录只核对 principal, draft, attachment, receipt 的基本身份和引用。`capture_data.io` 冻结字节和请求来源，`capture_data.domain` 核对本领域记录结构，`capture_data.journal` 封存来源原文和版本，`capture_data.projection` 显示本地引用缺口。现有判断只覆盖本地资料，尚未推断外部服务的连续性或全量完整性。

Python 3.11 以上，无第三方依赖。样例均为合成，不访问真实站点。

```sh
python -m unittest discover -s tests -v
python -m compileall -q capture_data tests
python -m capture_data.cli inspect data/normal.json
```

Dockerfile 提供 Linux 运行环境；`docker build -t source-capture .` 构建，`docker run --rm source-capture python -m unittest discover -s tests -v` 运行测试。
