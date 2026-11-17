"""返回本地已确认记录与引用缺口。"""
import json
from .publication import assess
def overview(c,collection):
 rows=c.execute('SELECT kind,record_id,version,source_digest,refs,payload FROM records WHERE collection=? ORDER BY kind,record_id,version',(collection,)).fetchall()
 ids={r[1] for r in rows};missing=sorted({ref for r in rows for ref in json.loads(r[4]) if ref not in ids})
 business_rows=[{'kind':r[0],'id':r[1],'version':r[2],'refs':json.loads(r[4]),'payload':json.loads(r[5])} for r in rows]
 business=assess(business_rows) if any('position' not in r['payload'] for r in business_rows) else {'publishable':False,'reasons':['通用来源尚无协议核验']}
 return {'business':business,'collection':collection,'records':[{'kind':r[0],'id':r[1],'version':r[2],'source_digest':r[3]} for r in rows],'missing_refs':missing,'locally_closed':not missing}
