from typing import Any, Optional, Tuple

import pandas as pd

from DataMetaRule import DataMetaRule


class DataModelRule:
    def __init__(self, meta: DataMetaRule):
        self.__meta = meta
        self.__model = None

    def __checkSource(self, cate: int, origins: dict, refs: Optional[dict]) -> tuple[set, set]:
        checkOri = self.__meta.org if cate == 0 or self.__meta.org_x is None else self.__meta.org_x
        checkRef = self.__meta.ref if cate == 0 or self.__meta.ref_x is None else self.__meta.ref_x
        return set(checkOri) - set(origins), set(checkRef) - set(refs or [])

    def prepare(self, cate: int, origins: dict, refs: Optional[dict] = None, save: str = 'file/input') -> Tuple[pd.DataFrame, Optional[pd.DataFrame]]:
        print('ml: prepare')
        # check if miss
        ori_miss, ref_miss = self.__checkSource(cate, origins, refs)
        print('miss origin:', ori_miss)
        print('miss ref:', ref_miss)
        # return X, Y

    def train(self, X: pd.DataFrame, Y: pd.DataFrame, save: str = 'file/train') -> Tuple[Any, Optional[Any]]:
        print('ml: train')
        # assign self.__model
        # return modelData, pipeData

    def load(self, modelData: Any, pipeData: Optional[Any]):
        print('ml: load')
        # assign self.__model

    def loadPath(self, modelPath: str, pipePath: str):
        print('ml: load by path')
        # assign self.__model

    def predict(self, X: pd.DataFrame) -> pd.DataFrame:
        print('ml: predict')

    def validate(self, X: pd.DataFrame, Y: pd.DataFrame) -> Any:
        print('ml: validate')
