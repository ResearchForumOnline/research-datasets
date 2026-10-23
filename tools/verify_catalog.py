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
    print('Validated', len(identifiers), 'pack metadata records; no network, extraction or execution')

if __name__ == '__main__':
    main()
