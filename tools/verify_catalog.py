"""Validate public catalog metadata without downloading or executing data."""
from pathlib import Path, PurePosixPath
import json, re

ROOT = Path(__file__).resolve().parents[1]

def main():
    catalog = json.loads((ROOT/'catalog.json').read_text(encoding='utf-8'))
    assert catalog['schema_version'] == 1
    assert re.fullmatch(r'datasets-\d{4}\.\d{2}\.\d{2}', catalog['release'])
    prefix = 'https://github.com/ResearchForumOnline/research-datasets/releases/download/' + catalog['release'] + '/'
    identifiers = set()
    for pack in catalog['packs']:
        assert re.fullmatch(r'[a-z0-9][a-z0-9.-]+', pack['id'])
        assert pack['id'] not in identifiers
        identifiers.add(pack['id'])
        card = PurePosixPath(pack['card'])
        assert not card.is_absolute() and '..' not in card.parts
        assert card.parts[0] == 'cards' and ROOT.joinpath(*card.parts).is_file()
        assert pack['license'] and pack['contents'] and pack['title']
        assert isinstance(pack['file_count'], int) and pack['file_count'] > 0
        assert pack['uncompressed_bytes'] > 0
        asset = pack['asset']
        assert asset['name'] == pack['id'] + '.zip'
        assert asset['url'] == prefix + asset['name']
        assert 0 < asset['bytes'] < 2*1024**3
        assert re.fullmatch(r'[a-f0-9]{64}', asset['sha256'])
    assert identifiers
    for mirror in catalog.get('reference_mirrors', []):
        rel=PurePosixPath(mirror['manifest'])
        assert not rel.is_absolute() and '..' not in rel.parts
        source=json.loads(ROOT.joinpath(*rel.parts).read_text(encoding='utf-8'))
        assert source['schema_version']==1 and source['id']==mirror['id']
        assert len(source['files'])==mirror['original_files']
        assert sum(x['bytes'] for x in source['files'])==mirror['original_bytes']==source['total_original_bytes']
        prefix='https://github.com/ResearchForumOnline/research-datasets/releases/download/'+source['release']+'/'
        names=set();parts=set()
        for file in source['files']:
            assert file['name'] not in names and PurePosixPath(file['name']).name==file['name']
            assert '/' not in file['name'] and '\\' not in file['name'] and ':' not in file['name']
            names.add(file['name'])
            assert re.fullmatch(r'[a-f0-9]{64}',file['sha256'])
            assert re.fullmatch(r'[a-f0-9]{32}',file['upstream_md5'])
            assert sum(p['bytes'] for p in file['parts'])==file['bytes']
            for part in file['parts']:
                assert part['name'] not in parts and PurePosixPath(part['name']).name==part['name']
                assert '\\' not in part['name'] and ':' not in part['name']
                parts.add(part['name'])
                assert part['url']==prefix+part['name']
                assert 0<part['bytes']<2*1024**3
                assert re.fullmatch(r'[a-f0-9]{64}',part['sha256'])
    print('Validated', len(identifiers), 'packs and',len(catalog.get('reference_mirrors',[])),'reference mirrors; no network, extraction or execution')

if __name__ == '__main__':
    main()
