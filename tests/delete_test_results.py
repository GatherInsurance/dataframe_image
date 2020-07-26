from pathlib import Path
import shutil

def delete(fp):
    p = Path(fp)
    for file in p.iterdir():
        if file.suffix in ('.pdf', '.md') or file.name.endswith('_dataframe_image.ipynb'):
            if file.name != 'README.md':
                file.unlink()

        if file.name.endswith('_files'):
            shutil.rmtree(file)

home = Path(__file__).parent
delete(home / 'notebooks')
delete(home / 'test_output')