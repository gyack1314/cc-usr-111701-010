"""封存已确认的来源和记录版本，不替外部协议判断完整性。"""
import hashlib,json,sqlite3
from .io import asset
SCHEMA="CREATE TABLE IF NOT EXISTS sources(collection TEXT,digest TEXT,raw BLOB,PRIMARY KEY(collection,digest));CREATE TABLE IF NOT EXISTS records(collection TEXT,kind TEXT,record_id TEXT,version TEXT,source_digest TEXT,refs TEXT,payload TEXT,PRIMARY KEY(collection,kind,record_id,version),FOREIGN KEY(collection,source_digest) REFERENCES sources(collection,digest));"
def connect(path):
 c=sqlite3.connect(path);c.execute('PRAGMA foreign_keys=ON');c.executescript(SCHEMA);return c
def receive(c,manifest,root):
 raw=asset(root,manifest['assets'][0]);digest=hashlib.sha256(raw).hexdigest();doc=json.loads(raw.decode('utf-8'))
 if doc.get('collection')!=manifest['collection'] or doc.get('protocol')!=manifest['protocol']:raise ValueError('来源身份不匹配')
 with c:
  c.execute('INSERT OR IGNORE INTO sources VALUES(?,?,?)',(doc['collection'],digest,raw))
  for row in doc['records']:
   refs=json.dumps(row.get('refs',[]),ensure_ascii=False);payload=json.dumps(row.get('payload',{}),ensure_ascii=False,sort_keys=True)
   old=c.execute('SELECT source_digest,payload FROM records WHERE collection=? AND kind=? AND record_id=? AND version=?',(doc['collection'],row['kind'],row['id'],row['version'])).fetchone()
   if old and old!=(digest,payload):raise ValueError('版本冲突')
   c.execute('INSERT OR IGNORE INTO records VALUES(?,?,?,?,?,?,?)',(doc['collection'],row['kind'],row['id'],row['version'],digest,refs,payload))
 return digest
