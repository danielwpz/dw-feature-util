import pandas as pd
import numpy as np
from test.util import array_equal
from feature_util.ohlc import SimpleMovingAverageFeatureProducer
from feature_util.ohlc import ExponentialMovingAverageFeatureProducer


def test_simple_moving_average():
    ohlc_df = pd.DataFrame([
        {'open': 1, 'high': 9, 'low': 1, 'close': 1, 'volume': 100},
        {'open': 1, 'high': 8, 'low': 1, 'close': 2, 'volume': 100},
        {'open': 1, 'high': 7, 'low': 1, 'close': 3, 'volume': 100},
        {'open': 1, 'high': 6, 'low': 1, 'close': 4, 'volume': 100},
        {'open': 1, 'high': 5, 'low': 1, 'close': 5, 'volume': 100},
        {'open': 1, 'high': 4, 'low': 1, 'close': 6, 'volume': 100},
        {'open': 1, 'high': 3, 'low': 1, 'close': 7, 'volume': 100}
    ])

    close_2_sma_provider = SimpleMovingAverageFeatureProducer(period=2)
    close_2_sma_result = close_2_sma_provider.produce(ohlc_df)['close_sma_2'].values
    expect_close_2_sma = [np.nan, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
    assert array_equal(close_2_sma_result, expect_close_2_sma)


def test_exponential_moving_average():
    ohlc_df = pd.DataFrame([
        {'open': 1, 'high': 9, 'low': 1, 'close': 1, 'volume': 100},
        {'open': 1, 'high': 8, 'low': 1, 'close': 2, 'volume': 100},
        {'open': 1, 'high': 7, 'low': 1, 'close': 3, 'volume': 100},
        {'open': 1, 'high': 6, 'low': 1, 'close': 4, 'volume': 100},
        {'open': 1, 'high': 5, 'low': 1, 'close': 5, 'volume': 100},
        {'open': 1, 'high': 4, 'low': 1, 'close': 6, 'volume': 100},
        {'open': 1, 'high': 3, 'low': 1, 'close': 7, 'volume': 100}
    ])
    volume_2_ema_provider = ExponentialMovingAverageFeatureProducer(period=2, feature='volume')
    volume_2_ema_result = volume_2_ema_provider.produce(ohlc_df)['volume_ema_2'].values
    expect_volume_2_ema = [100] * len(volume_2_ema_result)
    assert array_equal(volume_2_ema_result, expect_volume_2_ema)

