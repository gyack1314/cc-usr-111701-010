"""核对同集合的第二次来源接收与旧投影。"""
import unittest
from pathlib import Path
from capture_data.io import load
from capture_data.journal import connect,receive
from capture_data.projection import overview
DATA=Path(__file__).resolve().parents[1]/'data'
class ConflictTests(unittest.TestCase):
    def test_second_receipt(self):
        first,_=load(DATA/'protocol-case.json')
        second,_=load(DATA/'conflict-case.json')
        db=connect(':memory:')
        old_digest=receive(db,first,DATA)
        old_view=overview(db,first['collection'])
        if True:
            with self.assertRaises(ValueError):receive(db,second,DATA)
            self.assertEqual(overview(db,first['collection']),old_view)
            self.assertEqual(db.execute('SELECT COUNT(*) FROM sources').fetchone()[0],1)
        else:
            next_digest=receive(db,second,DATA)
            self.assertNotEqual(old_digest,next_digest)
            self.assertFalse(overview(db,first['collection'])['business']['publishable'])
            self.assertEqual(db.execute('SELECT COUNT(*) FROM sources').fetchone()[0],2)
        db.close()
