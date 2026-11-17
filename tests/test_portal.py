"""核对双标签页的代理主体和草稿范围。"""
import json,unittest
from pathlib import Path
from capture_data.rpa import PortalReplay
FILE=Path(__file__).resolve().parents[1]/'data/portal-actions.json'
class PortalActions(unittest.TestCase):
    def test_tab_context(self):
        replay=PortalReplay(json.loads(FILE.read_text(encoding='utf-8'))['steps'])
        replay.next('open','tab-A','agent-1','d-17')
        replay.next('open','tab-B','agent-2','d-42')
        with self.assertRaises(ValueError):replay.next('upload','tab-B','agent-1','d-17')
        replay.next('upload','tab-A','agent-1','d-17')
        self.assertEqual(replay.tabs['tab-A']['principal'],'agent-1')
        self.assertEqual(replay.tabs['tab-B']['draft'],'d-42')
