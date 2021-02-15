from typing import Union

import numpy as np
from jesse.helpers import get_config
import talib

from jesse.helpers import get_candle_source


def ht_trendmode(candles: np.ndarray, source_type: str = "close", sequential: bool = False) -> Union[float, np.ndarray]:
    """
    HT_TRENDMODE - Hilbert Transform - Trend vs Cycle Mode

    :param candles: np.ndarray
    :param source_type: str - default: "close"
    :param sequential: bool - default=False

    :return: int | np.ndarray
    """
    warmup_candles_num = get_config('env.data.warmup_candles_num', 210)
    if not sequential and len(candles) > warmup_candles_num:
        candles = candles[-warmup_candles_num:]

    source = get_candle_source(candles, source_type=source_type)
    res = talib.HT_TRENDMODE(source)

    return res if sequential else res[-1]
