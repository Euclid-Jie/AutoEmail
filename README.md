# AutoEmail

## 项目简介
AutoEmail 是一个基于 Python 标准库实现的邮件自动发送工具，支持多收件人、邮件正文、附件等功能。无需额外依赖第三方库，轻量且易于集成。

---

## 作为 Git 子模块的使用方法

1. **添加子模块**
   在目标项目中，运行以下命令将 AutoEmail 添加为子模块，注意使用https
   
   ```bash
   git submodule add https://github.com/Euclid-Jie/AutoEmail.git AutoEmail
   ```
   
2. **初始化子模块**
   如果是第一次克隆包含子模块的仓库，需初始化子模块：
   ```bash
   git submodule update --init --recursive
   ```

3. **更新子模块**
   当 AutoEmail 仓库有更新时，在目标项目中运行以下命令同步更新：
   ```bash
   git submodule update --remote
   ```

4. **移除子模块**
   如果需要移除 AutoEmail 子模块，运行以下命令：
   ```bash
   git submodule deinit -f AutoEmail
   git rm -f AutoEmail
   rm -rf .git/modules/AutoEmail
   ```

---

## 关于 `.env` 文件的注意事项

1. **文件位置**
   `.env` 文件应放置在 AutoEmail 项目的根目录下。

2. **文件内容**
   `.env` 文件用于存储敏感信息，例如发件人邮箱、授权码、收件人邮箱等。示例如下：
   
   ```properties
   SEND = **84@qq.com
   PASS = **ebja
   RECV = **123@outlook.com,another@example.com
   ```
   
   - `SEND`：发件人邮箱地址。
   - `PASS`：发件人邮箱的授权码（非邮箱密码）。
   - `RECV`：收件人邮箱地址，支持多个收件人，使用逗号分隔。

---

## 使用示例

1. **配置 `.env` 文件**
   根据上述说明创建并配置 `.env` 文件。

2. **运行示例代码**
   在 AutoEmail 项目目录下运行以下命令：
   ```bash
   python AutoEmail.py
   ```

3. **自定义邮件内容**
   修改 `AutoEmail.py` 中的 `EmailParams` 参数，设置邮件标题、正文和附件路径。

4. 在其他项目中作为submodule使用

   ```python
   from AutoEmail import AutoEmail, EmailParams
   AutoEmail(
       EmailParams(
           title="", content=""
       )
   )
   ```

   