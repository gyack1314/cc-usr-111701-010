"""核对协议来源从原文到版本账本及业务投影。"""
import unittest
from pathlib import Path
from capture_data.io import load
from capture_data.domain import summarize
from capture_data.journal import connect, receive
from capture_data.projection import overview

FILE = Path(__file__).resolve().parents[1] / 'data' / 'protocol-case.json'

class ProtocolTest(unittest.TestCase):
    def test_protocol_receipt_chain(self):
        manifest, _ = load(FILE)
        summary = summarize(manifest, FILE.parent)
        db = connect(':memory:')
        digest = receive(db, manifest, FILE.parent)
        view = overview(db, manifest['collection'])
        self.assertEqual(summary['record_count'], len(view['records']))
        self.assertEqual(len(view['records']), 4)
        self.assertTrue(view['locally_closed'])
        self.assertFalse(view['business']['publishable'])
        self.assertTrue(view['business']['reasons'])
        self.assertEqual({r['source_digest'] for r in view['records']}, {digest})
        self.assertIn('receipt', {r['kind'] for r in view['records']})
        self.assertEqual(receive(db, manifest, FILE.parent), digest)
        self.assertEqual(len(overview(db, manifest['collection'])['records']), 4)
        db.close()
