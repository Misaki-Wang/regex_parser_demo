#!/bin/zsh

# 检查是否提供了文件名参数
if [ -z "$1" ]; then
  echo "Usage: $0 <test_file>"
  exit 1
fi

TEST_FILE=$1

# 运行指定的测试文件
python -m unittest $TEST_FILE
