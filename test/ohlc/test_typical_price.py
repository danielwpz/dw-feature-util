import pandas as pd
from test.util import array_equal
from feature_util.ohlc import TypicalPriceFeatureProducer


def test_typical_price():
    ohlc_df = pd.DataFrame([
        {'open': 1, 'high': 1, 'low': 1, 'close': 1, 'volume': 100},
        {'open': 1, 'high': 3, 'low': 1, 'close': 2, 'volume': 100},
        {'open': 1, 'high': 7, 'low': 1, 'close': 4, 'volume': 100}
    ])

    typical_price_producer = TypicalPriceFeatureProducer()
    typical_price_result = typical_price_producer.produce(ohlc_df)['tp'].values
    expected_typical_price = [1, 2, 4]

    assert array_equal(typical_price_result, expected_typical_price)
