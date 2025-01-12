#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
metadata_collector.py

Collects additional metadata for GPT interactions, such as user ID, 
session info, or other relevant experiment data. 
"""

import uuid
import socket
import datetime

class MetadataCollector:
    def __init__(self):
        self.session_id = str(uuid.uuid4())
        self.hostname = socket.gethostname()
        self.start_time = datetime.datetime.now()

    def get_metadata(self):
        """
        Returns a dictionary of metadata for the current session or interaction.
        """
        return {
            "session_id": self.session_id,
            "hostname": self.hostname,
            "start_time": self.start_time.isoformat()
        }
