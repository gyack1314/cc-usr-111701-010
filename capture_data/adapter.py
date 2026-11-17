import json
def decode(raw, manifest):
    doc=json.loads(raw.decode('utf-8'));principal=doc['principal'];draft=doc['draft']
    records=[{'kind':'principal','id':principal,'version':'received','refs':[],
              'payload':{'source_url':manifest['source_url']}},
             {'kind':'draft','id':draft,'version':doc['revision'],'refs':[principal],
              'payload':{'principal':principal}}]
    for attachment in doc['attachments']:
        records.append({'kind':'attachment','id':attachment['id'],'version':doc['revision'],
                        'refs':[draft],'payload':attachment})
    for receipt in doc['receipts']:
        if receipt['draft_revision']!=doc['revision']:raise ValueError('回执草稿版本不符')
        records.append({'kind':'receipt','id':receipt['id'],'version':doc['revision'],
                        'refs':[draft],'payload':receipt})
    return {'protocol':manifest['protocol'],'collection':manifest['collection'],'records':records}
