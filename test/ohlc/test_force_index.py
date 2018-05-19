import numpy as np
import pandas as pd
from test.util import array_equal
from feature_util.ohlc import ForceIndexFeatureProducer


def test_fi_feature():
    ohlc_df = pd.DataFrame([
        {'open': 1, 'high': 9, 'low': 1, 'close': 1, 'volume': 100},
        {'open': 1, 'high': 8, 'low': 1, 'close': 2, 'volume': 100},
        {'open': 1, 'high': 7, 'low': 1, 'close': 4, 'volume': 100},
        {'open': 1, 'high': 6, 'low': 1, 'close': 8, 'volume': 100},
        {'open': 1, 'high': 5, 'low': 1, 'close': 16, 'volume': 100},
        {'open': 1, 'high': 4, 'low': 1, 'close': 32, 'volume': 100},
        {'open': 1, 'high': 3, 'low': 1, 'close': 64, 'volume': 100}
    ])

    fi_producer = ForceIndexFeatureProducer(period=3)
    fi_result = fi_producer.produce(ohlc_df)

    assert 'fi_1' in fi_result
    assert 'fi_3' in fi_result

    expect_fi_1 = [np.nan, 200, 400, 800, 1600, 3200]
    array_equal(fi_result['fi_1'].values, expect_fi_1)
