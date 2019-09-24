#!/usr/bin/env python
import os

#db_config = os.environ.get('DB')
db_config = 'sqlite:///url'
jwt_secret_key = os.environ.get('JWT_TOKEN')
testing = True
