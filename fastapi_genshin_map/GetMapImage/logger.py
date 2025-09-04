import logging
import sys
import io

import fastapi
import rollbar
from rollbar.contrib.fastapi import LoggerMiddleware
from rollbar.logger import RollbarHandler

# 强制标准输出使用UTF-8编码（解决中文乱码）
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Initialize Rollbar SDK with your server-side access token
rollbar.init(
    'ACCESS_TOKEN',
    environment='staging',
    handler='async',
)

# Set root logger to log DEBUG and above
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Report ERROR and above to Rollbar
rollbar_handler = RollbarHandler()
rollbar_handler.setLevel(logging.ERROR)

# Attach Rollbar handler to the root logger
logger.addHandler(rollbar_handler)
