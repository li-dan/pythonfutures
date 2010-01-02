# Copyright 2009 Brian Quinlan. All Rights Reserved. See LICENSE file.

"""Execute computations asynchronously using threads or processes."""

__author__ = 'Brian Quinlan (brian@sweetapp.com)'

from futures._base import (FIRST_COMPLETED, FIRST_EXCEPTION,
                           ALL_COMPLETED, RETURN_IMMEDIATELY,
                           CancelledError, TimeoutError,
                           Future, wait, iter_as_completed) 
from futures.thread import ThreadPoolExecutor
from futures.process import ProcessPoolExecutor

