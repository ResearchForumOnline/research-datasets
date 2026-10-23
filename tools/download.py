"""Download a published data asset and verify it; never extract or execute it."""
from pathlib import Path
import argparse
import hashlib
import json
import urllib.request

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--list',action='store_true')
    parser.add_argument('--pack')
    parser.add_argument('--destination',type=Path)
    args=parser.parse_args()
    catalog=json.loads((ROOT/'catalog.json').read_text(encoding='utf-8'))
    if args.list:
        for pack in catalog['packs']:
            print(pack['id'],pack['asset']['bytes'],pack['license'])
        return
    if not args.pack or args.destination is None:
        parser.error('Choose --list, or both --pack and --destination')
    matches=[p for p in catalog['packs'] if p['id']==args.pack]
    if len(matches)!=1:
        parser.error('Unknown or ambiguous pack ID')
    asset=matches[0]['asset']
    if not asset['url'].startswith('https://github.com/ResearchForumOnline/research-datasets/releases/download/'):
        raise ValueError('Unexpected asset destination in catalog')
    filename=Path(asset['name'])
    if filename.name!=asset['name'] or filename.is_absolute():
        raise ValueError('Unsafe catalog filename')
    args.destination.mkdir(parents=True,exist_ok=True)
    target=args.destination/filename
    digest=hashlib.sha256();size=0
    # Exclusive creation prevents replacing a previous download, including links.
    with target.open('xb') as output:
        try:
            with urllib.request.urlopen(asset['url'],timeout=60) as response:
                while block:=response.read(1024*1024):
                    size+=len(block)
                    if size>asset['bytes']:
                        raise ValueError('Download exceeds recorded size')
                    digest.update(block);output.write(block)
            if size!=asset['bytes'] or digest.hexdigest()!=asset['sha256']:
                raise ValueError('Download checksum or length does not match')
        except BaseException:
            output.close()
            # Only the file exclusively created by this invocation is removed.
            target.unlink(missing_ok=True)
            raise
    print('Verified:',target)
    print('SHA256:',digest.hexdigest())

if __name__=='__main__':
    main()
