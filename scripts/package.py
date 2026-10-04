from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
root = Path(__file__).resolve().parent.parent
out = root / 'dist' / 'bahai-milano.zip'
out.parent.mkdir(exist_ok=True)
files = list(root.glob('*.hbs')) + [root / 'package.json']
for directory in ('assets', 'partials', 'locales'):
    files += [p for p in (root / directory).rglob('*') if p.is_file()]
with ZipFile(out, 'w', ZIP_DEFLATED) as archive:
    for file in files:
        archive.write(file, file.relative_to(root))
print(out)
