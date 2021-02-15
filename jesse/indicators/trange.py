from typing import Union

import numpy as np
from jesse.helpers import get_config
import talib


def trange(candles: np.ndarray, sequential: bool = False) -> Union[float, np.ndarray]:
    """
    TRANGE - True Range

    :param candles: np.ndarray
    :param sequential: bool - default=False

    :return: float | np.ndarray
    """
    warmup_candles_num = get_config('env.data.warmup_candles_num', 210)
    if not sequential and len(candles) > warmup_candles_num:
        candles = candles[-warmup_candles_num:]

    res = talib.TRANGE(candles[:, 3], candles[:, 4], candles[:, 2])

    if sequential:
        return res
    else:
        return None if np.isnan(res[-1]) else res[-1]
