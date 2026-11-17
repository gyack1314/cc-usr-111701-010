"""返回本地已确认记录与引用缺口。"""
import json
def overview(c,collection):
 rows=c.execute('SELECT kind,record_id,version,source_digest,refs FROM records WHERE collection=? ORDER BY kind,record_id,version',(collection,)).fetchall()
 ids={r[1] for r in rows};missing=sorted({ref for r in rows for ref in json.loads(r[4]) if ref not in ids})
 return {'collection':collection,'records':[{'kind':r[0],'id':r[1],'version':r[2],'source_digest':r[3]} for r in rows],'missing_refs':missing,'locally_closed':not missing}
