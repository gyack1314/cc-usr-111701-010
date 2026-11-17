# customs-portal 来源契约

来源清单中的资产长度与 SHA-256 用于核对本地原文字节。文档的 collection 与 protocol 必须匹配清单，现有记录类型包括 principal, draft, attachment, receipt。每条记录以 kind、id、version 定位，refs 指向同集合的其他记录，payload 原样留存。来源版本冲突会中断接收；本地引用闭合只表示当前收到的引用能定位，不表示远端序列或授权资料已经完整。

## 已接收的协议资料
现有入口保留代理主体、草稿版本、附件摘要和服务回执归属；needs_correction 不等于正式提交成功。样例为服务响应，不操作真实海关门户。
