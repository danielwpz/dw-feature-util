import pandas as pd
from test.util import array_equal
from feature_util.ohlc import CCIFeatureProducer


def test_cci_feature():
    ohlc_df = pd.DataFrame([
        {'open': 1, 'high': 9, 'low': 1, 'close': 1, 'volume': 100},
        {'open': 1, 'high': 8, 'low': 1, 'close': 2, 'volume': 100},
        {'open': 1, 'high': 7, 'low': 1, 'close': 4, 'volume': 100},
        {'open': 1, 'high': 6, 'low': 1, 'close': 8, 'volume': 100},
        {'open': 1, 'high': 5, 'low': 1, 'close': 16, 'volume': 100},
        {'open': 1, 'high': 4, 'low': 1, 'close': 32, 'volume': 100},
        {'open': 1, 'high': 3, 'low': 1, 'close': 64, 'volume': 100}
    ])

    cci_producer = CCIFeatureProducer(period=3)
    cci_result = cci_producer.produce(ohlc_df)

    assert 'cci' in cci_result  # TODO need to find a good way to test this :(

