# 海关门户代理申报的多步骤 RPA 恢复与回执归属资料账本

项目保存冻结来源记录及其原始资产。`capture_data.io` 核对文件身份，提供固定字节范围读取和顺序响应重放；`capture_data.domain` 清点来源，`capture_data.cli` 输出概况。当前只处理通用来源清单，尚未解释外部协议及其完整性。

Python 3.11 以上，无第三方依赖。样例为本地合成资料，不访问真实服务。

```sh
python -m unittest discover -s tests -v
python -m compileall -q capture_data tests
python -m capture_data.cli inspect data/normal.json
```

Dockerfile 提供 Linux 运行环境，构建命令为 `docker build -t source-capture .`，测试命令为 `docker run --rm source-capture python -m unittest discover -s tests -v`。
