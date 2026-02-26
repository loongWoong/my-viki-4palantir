#!/bin/bash

# 使用虚拟环境的启动脚本

APP_NAME="app.py"
LOG_FILE="app.log"
PID_FILE="app.pid"
VENV_DIR="venv"  # 虚拟环境目录

# 切换到脚本目录
cd "$(dirname "$0")" || exit 1

# 激活虚拟环境
if [ -d "$VENV_DIR" ]; then
    source "$VENV_DIR/bin/activate"
    echo "已激活虚拟环境: $VENV_DIR"
else
    echo "错误: 未找到虚拟环境 $VENV_DIR"
    exit 1
fi

# 检查 Python
PYTHON_CMD=$(which python3)
echo "使用 Python: $PYTHON_CMD"

start() {
    if [ -f "$PID_FILE" ] && kill -0 "$(cat "$PID_FILE")" 2>/dev/null; then
        echo "应用已在运行 (PID: $(cat "$PID_FILE"))"
        return 1
    fi
    
    echo "启动 $APP_NAME ..."
    
    # 记录启动时间到日志
    echo "=== $(date '+%Y-%m-%d %H:%M:%S') 启动应用 ===" >> "$LOG_FILE"
    
    nohup "$PYTHON_CMD" "$APP_NAME" >> "$LOG_FILE" 2>&1 &
    echo $! > "$PID_FILE"
    
    echo "启动成功，PID: $(cat "$PID_FILE")"
    echo "查看日志: tail -f $LOG_FILE"
}

stop() {
    if [ ! -f "$PID_FILE" ]; then
        echo "应用未运行"
        return 1
    fi
    
    PID=$(cat "$PID_FILE")
    echo "停止应用 (PID: $PID)..."
    kill "$PID" 2>/dev/null
    
    # 等待进程结束
    for i in {1..10}; do
        if ! kill -0 "$PID" 2>/dev/null; then
            echo "应用已停止"
            rm -f "$PID_FILE"
            echo "=== $(date '+%Y-%m-%d %H:%M:%S') 应用停止 ===" >> "$LOG_FILE"
            return 0
        fi
        sleep 1
    done
    
    kill -9 "$PID" 2>/dev/null
    rm -f "$PID_FILE"
    echo "应用已强制停止"
}

# 主逻辑（同上）
case "${1:-start}" in
    start) start ;;
    stop) stop ;;
    restart) stop; sleep 2; start ;;
    status) 
        if [ -f "$PID_FILE" ] && kill -0 "$(cat "$PID_FILE")" 2>/dev/null; then
            echo "运行中 (PID: $(cat "$PID_FILE"))"
        else
            echo "未运行"
        fi
        ;;
    *) echo "用法: $0 {start|stop|restart|status}" ;;
esac