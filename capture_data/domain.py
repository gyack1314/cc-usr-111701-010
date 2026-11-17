"""核对本领域冻结来源的基本结构与记录身份。"""
import json
from .io import asset
from .adapter import decode
PROTOCOL='customs-portal'
KINDS=set(['principal', 'draft', 'attachment', 'receipt'])
def summarize(v,root):
 if v.get('kind')!='source-records' or v.get('protocol')!=PROTOCOL:raise ValueError('来源协议不匹配')
 raw=asset(root,v['assets'][0]);doc=decode(raw,v) if v['assets'][0]['path'] in ('protocol-source.bin','conflict-source.bin') else json.loads(raw.decode('utf-8'))
 if doc.get('protocol')!=PROTOCOL or doc.get('collection')!=v.get('collection'):raise ValueError('来源文档不匹配')
 rows=doc.get('records')
 if not isinstance(rows,list) or not rows:raise ValueError('记录为空')
 if any(row.get('kind') not in KINDS or not row.get('id') or not row.get('version') for row in rows):raise ValueError('记录身份非法')
 return {'protocol':PROTOCOL,'collection':doc['collection'],'record_count':len(rows),'kinds':sorted({row['kind'] for row in rows}),'raw_bytes':len(raw)}
