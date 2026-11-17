"""验证来源文档、持久账本与引用投影的贯通。"""
import unittest,tempfile
from pathlib import Path
from capture_data.io import load,asset,Source
from capture_data.domain import summarize
from capture_data.journal import connect,receive
from capture_data.projection import overview
FILE=Path(__file__).resolve().parents[1]/'data/normal.json'
class MaterialTests(unittest.TestCase):
 def test_receipt_and_projection(self):
  v,_=load(FILE);summary=summarize(v,FILE.parent);self.assertGreater(summary['record_count'],2)
  with tempfile.TemporaryDirectory() as t:
   db=connect(Path(t)/'journal.sqlite3');first=receive(db,v,FILE.parent);second=receive(db,v,FILE.parent)
   self.assertEqual(first,second);view=overview(db,v['collection'])
   self.assertTrue(view['locally_closed']);self.assertEqual(len(view['records']),summary['record_count']);db.close()
 def test_asset_identity_and_ranges(self):
  v,_=load(FILE);source=Source(FILE.parent,v['assets'][0]);self.assertEqual(source.read_at(0,1),asset(FILE.parent,v['assets'][0])[:1])
  with self.assertRaises(ValueError):source.read_at(-1,3)
