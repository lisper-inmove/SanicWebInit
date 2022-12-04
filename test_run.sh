#!/bin/bash

export APPNAME=demo1
export LOGGER_ENABLE_CONSOLE=true
export LOGGER_ENABLE_SYSLOG=true
export LOGGER_SYSLOG_HOST=logger.server
export LOGGER_SYSLOG_PORT=514
export LOGGER_SYSLOG_FACILITY=local7
sanic app:app --host=0.0.0.0 --port=18888 --fast --debug
