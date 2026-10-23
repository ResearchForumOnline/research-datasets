"""Synthetic transport/integrity tests; no real network or datasets."""
import hashlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import download

class DownloadTests(unittest.TestCase):
    def run_case(self, body=b'synthetic bytes', expected=b'synthetic bytes', existing=False, url=None, name='sample.zip'):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);out=root/'out';out.mkdir()
            data={'packs':[{'id':'synthetic','license':'CC-BY-4.0','asset':{'url':url or 'https://github.com/ResearchForumOnline/research-datasets/releases/download/test/sample.zip','name':name,'bytes':len(expected),'sha256':hashlib.sha256(expected).hexdigest()}}]}
            (root/'catalog.json').write_text(json.dumps(data))
            target=out/'sample.zip'
            if existing:target.write_bytes(b'preserve existing')
            with patch.object(download,'ROOT',root),patch('sys.argv',['download.py','--pack','synthetic','--destination',str(out)]),patch.object(download.urllib.request,'urlopen',return_value=io.BytesIO(body)) as network:
                try:download.main()
                except BaseException as exc:return type(exc),target.read_bytes() if target.exists() else None,network.call_count
                return None,target.read_bytes(),network.call_count

    def test_verified_bytes(self):
        error,data,calls=self.run_case();self.assertIsNone(error);self.assertEqual(data,b'synthetic bytes');self.assertEqual(calls,1)
    def test_same_length_changed_bytes_removed(self):
        error,data,_=self.run_case(body=b'Synthetic bytes');self.assertEqual(error,ValueError);self.assertIsNone(data)
    def test_truncated_and_oversized_removed(self):
        for data in [b'short',b'synthetic bytes with excess']:
            error,result,_=self.run_case(body=data);self.assertEqual(error,ValueError);self.assertIsNone(result)
    def test_existing_file_preserved_without_network(self):
        error,data,calls=self.run_case(existing=True);self.assertEqual(error,FileExistsError);self.assertEqual(data,b'preserve existing');self.assertEqual(calls,0)
    def test_unexpected_host_and_path_rejected(self):
        for options in [{'url':'https://example.invalid/data.zip'},{'name':'../escape.zip'}]:
            error,data,calls=self.run_case(**options);self.assertEqual(error,ValueError);self.assertIsNone(data);self.assertEqual(calls,0)

if __name__=='__main__':unittest.main()
