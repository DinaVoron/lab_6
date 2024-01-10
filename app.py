import datetime

from flask import Flask, session
app = Flask(__name__)


# установим секретный ключ для подписи.
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

import controllers.index
import controllers.book
import controllers.statistics
import controllers.new_reader
import controllers.search
