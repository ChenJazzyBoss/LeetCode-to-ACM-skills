"""日期辅助工具 —— 输出当天的 YYYY-MM-DD 和 workspace 路径。

用法:
    python commands/date/date_helper.py              # 仅打印日期
    python commands/date/date_helper.py --workspace  # 打印 workspace/<日期> 路径
"""

import sys
from datetime import date, timezone, timedelta

# 北京时间 (UTC+8)
TZ = timezone(timedelta(hours=8))


def today_str() -> str:
    """返回当天日期字符串 (北京时间) 如 '2026-07-14'"""
    return date.today(TZ).isoformat()


def workspace_dir() -> str:
    """返回当天的 workspace 子目录路径，如 'workspace/2026-07-14'"""
    import os
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    return os.path.join(root, "workspace", today_str())


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--workspace":
        print(workspace_dir())
    else:
        print(today_str())
