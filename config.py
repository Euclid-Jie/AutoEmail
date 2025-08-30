import os


def load_environment():
    # 自动检测环境（优先使用 GitHub Actions 的环境变量）
    if not os.getenv("GITHUB_ACTIONS"):  # 非 CI 环境
        env_file = ".env"
        if os.path.exists(env_file):
            with open(env_file, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    if "=" in line:
                        key, value = line.split("=", 1)
                        key = key.strip()
                        value = value.strip().strip('"').strip("'")
                        os.environ.setdefault(key, value)
        else:
            print(
                f"⚠️ Warning: {env_file} not found. Using system environment variables"
            )


# 初始化环境
load_environment()

# 获取环境变量（统一访问点）
SEND = os.getenv("SEND")
PASS = os.getenv("PASS")
RECV = os.getenv("RECV")

# 支持多个收件人（逗号分隔）
if RECV:
    RECV = [email.strip() for email in RECV.split(",") if email.strip()]
else:
    RECV = []
