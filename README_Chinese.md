# 📧 查找工作邮箱

## 🔥 概览
Find-Work-Emails 是一个简单的 Python 脚本，旨在使用 SMTP 协议和 DNS 查找来验证电子邮件地址。它从包含姓名和域的 CSV 文件中读取数据，基于常见模式生成可能的电子邮件格式猜测，并通过执行 SMTP 检查来验证每一个的有效性。

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
python email_verifier.py --file "path/to/your/csvfile.csv" --namecol "全名的列名称" --domaincol "公司域的列名称"
