# -*- coding: utf-8 -*-
"""
    Setup dos logs da aplicação
"""
import logzero
from logzero import *

log_file = "logs/app.log"
MAX_LOG_SIZE = 2048
FORMAT = '[%(asctime)s|%(levelname)s|%(module)s:linha %(lineno)d] %(message)s'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

# Definição do formatter
formatter = logzero.LogFormatter(fmt=FORMAT, datefmt=DATE_FORMAT);
logzero.formatter(formatter=formatter)

# Setup log rotate com 5 rotações
logzero.logfile(log_file, maxBytes=MAX_LOG_SIZE, backupCount=5)

# Definição do path e nome do arquivo, bem como, nível do log
logzero.logfile(log_file, loglevel=logging.INFO)