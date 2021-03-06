#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved

from .new_task import NewDocumentClassification, NewTask, _NewTask
from .serialize import load, save
from .task import Task_Deprecated, TaskBase, create_task


__all__ = [
    "_NewTask",
    "NewTask",
    "NewDocumentClassification",
    "Task_Deprecated",
    "TaskBase",
    "save",
    "load",
    "create_task",
]
