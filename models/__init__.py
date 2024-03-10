#!/usr/bin/python3
"""this creates unique instance for your application"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
