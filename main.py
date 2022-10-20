import pandas as pd

from DataMetaRule import META_DEMO1
from DataModelRule import DataModelRule as DML


def main():
    origins = {
        'd': pd.read_csv('file/origin/origin_demo.txt.eg')
    }
    exp = DML(META_DEMO1)
    exp.prepare(0, origins)
    # tbc...


if __name__ == '__main__':
    main()
