import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.utils import formataddr
from datetime import datetime
from typing import NamedTuple, List, Optional
from config import SEND, PASS, RECV
from pathlib import Path


class EmailParams(NamedTuple):
    title: Optional[str] = None
    content: Optional[str] = None
    attachments: Optional[List[Path]] = None  # 附件文件路径列表


def AutoEmail(params: EmailParams) -> bool:
    my_sender = SEND
    sender_passKey = PASS
    receivers = RECV  # 列表

    msg = MIMEMultipart()
    # 主题和正文
    content = params.content or "this is auto content"
    title = params.title or "Auto Title for Test"
    msg.attach(MIMEText(content, "plain", "utf-8"))
    msg["Subject"] = f"{title}-{datetime.today().strftime('%Y-%m-%d %H:%M:%S')}"
    msg["From"] = formataddr(("AutoEmail", my_sender))
    msg["To"] = ", ".join(receivers)

    # 添加附件
    if params.attachments:
        for file_path in params.attachments:
            if file_path.is_file():
                with open(file_path, "rb") as f:
                    att = MIMEApplication(f.read(), Name=file_path.name)
                att["Content-Disposition"] = f'attachment; filename="{file_path.name}"'
                msg.attach(att)

    try:
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        server.login(my_sender, sender_passKey)
        server.sendmail(
            my_sender,
            receivers,
            msg.as_string(),
        )
        server.quit()
        return True
    except Exception as e:
        print(f"邮件发送失败: {e}")
        return False


if __name__ == "__main__":
    params = EmailParams(
        title="测试邮件",
        content="你好，这是正文内容",
        attachments=[Path("test.txt")],
    )
    if AutoEmail(params):
        print("邮件发送成功")
    else:
        print("邮件发送失败")
