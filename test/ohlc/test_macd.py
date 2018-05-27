import pandas as pd
from test.util import array_equal, generate_ohlc_df
from feature_util.ohlc import MACDFeatureProducer


def test_macd():
    ohlc_df = pd.DataFrame([
        {'open': 1, 'high': 9, 'low': 1, 'close': 1, 'volume': 100},
        {'open': 1, 'high': 8, 'low': 1, 'close': 2, 'volume': 100},
        {'open': 1, 'high': 7, 'low': 1, 'close': 4, 'volume': 100},
        {'open': 1, 'high': 6, 'low': 1, 'close': 8, 'volume': 100},
        {'open': 1, 'high': 5, 'low': 1, 'close': 16, 'volume': 100},
        {'open': 1, 'high': 4, 'low': 1, 'close': 32, 'volume': 100},
        {'open': 1, 'high': 3, 'low': 1, 'close': 64, 'volume': 100}
    ])

    macd_producer = MACDFeatureProducer(fast_period=1, slow_period=3, signal_period=2)
    result = macd_producer.produce(ohlc_df)

    assert 'macd' in result
    assert 'macd_signal' in result
    assert 'macd_hist' in result
