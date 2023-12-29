# 📧 Find Work Emails / 查找客户的工作邮箱

<p align="center">
  <a href="./README.md">English</a> |
  <a href="./README_Chinese.md">简体中文</a>
</p>

## 🔥 概览
知道客户的姓名和公司网站？找到他的邮箱使用暴力穷举法哈哈。Find-Work-Emails 是一个简单的 Python 脚本，旨在使用 SMTP 协议和 DNS 查找来验证电子邮件地址。它从包含姓名和域的 CSV 文件中读取数据，基于常见模式生成可能的电子邮件格式猜测，并通过执行 SMTP 检查来验证每一个的有效性。

## ⚙️ 特性
- **MX 记录缓存**：通过缓存 MX 记录减少冗余的 DNS 查找。
- **多线程**：利用 Python 的 concurrent.futures 进行更快的处理。
- **命令行界面**：使用参数轻松设置文件路径，姓名列和域名列。
- **进度跟踪**：包含实时反馈的进度条。

## 😄 先决条件
在运行此脚本之前，请确保您已安装以下先决条件：
- Python 3.6 或更高版本
- pandas
- dnspython

## 💻 安装
1. 克隆仓库：
    ```bash
    git clone https://github.com/yourusername/email-verifier.git
    ```
2. 导航到克隆的目录：
    ```bash
    cd email-verifier
    ```
3. 安装所需的包：
    ```bash
    pip install pandas dnspython tqdm
    ```

## 🎆 使用方法
要使用 Email Verifier，您将需要一个包含全名和公司域列的 CSV 文件。然后，使用以下命令运行脚本：

```bash
python email_verifier.py --file "path/to/your/csvfile.csv" --namecol "全名的列名称例如Name或Full Names" --domaincol "公司域的列名称例如Domain或者domain，domain格式一般会是xxx.com"
```
示例
```bash
python csv2email.py --file "/Users/mac/Downloads/test.csv" --namecol "Name" --domaincol "domain"
```

## 🧑‍💻 贡献者
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="100px">
        <img src="https://images.weserv.nl/?url=https://github.com/lem6ns.png&mask=circle"/><br />
        <sub><a href="https://github.com/lem6ns">@lem6ns</a></sub>
      </td>
    </tr>
  </tbody>
</table>
