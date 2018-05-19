import pandas as pd
from feature_util.ohlc import BollingerBandsFeatureProducer
from feature_util.ohlc import SimpleMovingAverageFeatureProducer
from test.util import array_equal


def test_bb_feature():
    ohlc_df = pd.DataFrame([
        {'open': 1, 'high': 9, 'low': 1, 'close': 1, 'volume': 100},
        {'open': 1, 'high': 8, 'low': 1, 'close': 2, 'volume': 100},
        {'open': 1, 'high': 7, 'low': 1, 'close': 4, 'volume': 100},
        {'open': 1, 'high': 6, 'low': 1, 'close': 8, 'volume': 100},
        {'open': 1, 'high': 5, 'low': 1, 'close': 16, 'volume': 100},
        {'open': 1, 'high': 4, 'low': 1, 'close': 32, 'volume': 100},
        {'open': 1, 'high': 3, 'low': 1, 'close': 64, 'volume': 100}
    ])

    bb_producer = BollingerBandsFeatureProducer(period=3)
    bb_result = bb_producer.produce(ohlc_df)

    sma_producer = SimpleMovingAverageFeatureProducer(period=3)
    sma_result = sma_producer.produce(ohlc_df)

    assert 'bb_3_middle' in bb_result
    assert 'bb_3_upper' in bb_result
    assert 'bb_3_lower' in bb_result

    array_equal(bb_result['bb_3_middle'].values, sma_result['close_sma_3'].values)
