from dataclasses import dataclass
from typing import Optional


@dataclass
class DataMetaRule:
    alg: int
    org: dict[str, str]
    ref: Optional[dict[str, str]] = None
    org_x: Optional[dict[str, str]] = None
    ref_x: Optional[dict[str, str]] = None


# 稍微註解
ALG_R1 = 0

# 稍微註解
META_DEMO1 = DataMetaRule(
    alg=ALG_R1,
    org={'d': 'origin_demo.txt'},
    ref={'s': 'ref_sample.txt'},
)
