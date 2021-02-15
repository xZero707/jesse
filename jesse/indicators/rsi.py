from typing import Union

import numpy as np
from jesse.helpers import get_config
import talib

from jesse.helpers import get_candle_source


def rsi(candles: np.ndarray, period:int=14, source_type: str ="close", sequential: bool = False) -> Union[float, np.ndarray]:
    """
    RSI - Relative Strength Index

    :param candles: np.ndarray
    :param period: int - default: 14
    :param source_type: str - default: "close"
    :param sequential: bool - default=False

    :return: float | np.ndarray
    """
    warmup_candles_num = get_config('env.data.warmup_candles_num', 210)
    if not sequential and len(candles) > warmup_candles_num:
        candles = candles[-warmup_candles_num:]

    source = get_candle_source(candles, source_type=source_type)
    r = talib.RSI(source, timeperiod=period)

    return r if sequential else r[-1]
