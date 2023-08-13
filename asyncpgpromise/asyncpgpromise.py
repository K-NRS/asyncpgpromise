import asyncpg
import json
import re


class AsyncPGPromise:
  def __init__(self, connection: asyncpg.connection.Connection | None):
    if connection is not None:
      self.set_connection(connection)

  def set_connection(self, connection: asyncpg.connection.Connection):
    self.conn = connection

  @staticmethod
  def _parse_sql(sql: str):
    pattern = r'\$[\[|\(|\{\\][a-zA-Z0-9_]+[\]\)\}\\]'
    named_args = re.findall(pattern, sql, re.I)

    for i, arg in enumerate(named_args):
      sql = sql.replace(f'{arg}', f'${i+1}')

    return sql

  async def query(self, sql: str, **params):
    sql = self._parse_sql(sql)
    rows = await self.conn.fetch(sql, *params.values())
    return [dict(row) for row in rows]

  async def one(self, sql: str, **params):
    sql = self._parse_sql(sql)
    row = await self.conn.fetchrow(sql, *params.values())

    return row

  @staticmethod
  def _parse_json(row):
    result = {}
    for key, value in row.items():
      if isinstance(value, str):
        try:
          result[key] = json.loads(value)
        except json.JSONDecodeError:
          result[key] = value
      else:
        result[key] = value
    return result
