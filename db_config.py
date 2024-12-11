import datetime
import logging
import os
# import sys
from dotenv import load_dotenv
from peewee import Model, IntegerField, CharField, TextField, TimestampField
from playhouse.db_url import connect

# .envの読み込み
load_dotenv(override=True)

# # 実行したSQLをログで出力する設定
# logger = logging.getLogger("peewee")
# logger.addHandler(logging.StreamHandler())
# logger.setLevel(logging.DEBUG)

# データベースへの接続設定
# db = SqliteDatabase("peewee_db.db")
# SQLite固定の場合(この場合はインポートが必要 from peewee import SqliteDatabase)
db = connect(os.environ.get("DATABASE"))  # 環境変数に合わせて変更する場合
# db = connect(os.environ.get("DATABASE") or "sqlite:///peewee_db.sqlite")
# 環境変数が無い場合にデフォルト値として値を設定することも可能


# メッセージのモデル
class Message(Model):
    """Message Model"""

    id = IntegerField(primary_key=True)  # idは自動で追加されるが明示
    user = CharField()
    age = IntegerField()
    content = TextField()
    pub_date = TimestampField(default=datetime.datetime.now())  # 何も指定しない場合は現在時刻が入る

    class Meta:
        database = db
        table_name = "messages"


db.create_tables([Message])
