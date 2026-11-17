"""草稿、已收附件和正式申报回执分别陈列。"""
def assess(rows):
    receipts=[r for r in rows if r['kind']=='receipt']
    status=[r['payload']['status'] for r in receipts]
    pending=[r['id'] for r in receipts if r['payload']['status']!='accepted']
    return {'publishable':bool(receipts) and not pending,
            'reasons':['回执尚未确认正式提交:'+x for x in pending],
            'receipt_statuses':status}
