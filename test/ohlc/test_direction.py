import pandas as pd
import numpy as np
from test.util import array_equal
from feature_util.ohlc import DirectionFeatureProducer


def test_direction_feature():
    df = pd.DataFrame([
        {'open': 1, 'high': 9, 'low': 1, 'close': 1, 'volume': 100},
        {'open': 1, 'high': 8, 'low': 2, 'close': 2, 'volume': 100},
        {'open': 1, 'high': 7, 'low': 3, 'close': 3, 'volume': 100},
        {'open': 1, 'high': 6, 'low': 2, 'close': 4, 'volume': 100},
        {'open': 1, 'high': 5, 'low': 1, 'close': 5, 'volume': 100},
        {'open': 1, 'high': 4, 'low': 0, 'close': 6, 'volume': 100},
        {'open': 1, 'high': 3, 'low': 0, 'close': 7, 'volume': 100}
    ])
    direction_close_producer = DirectionFeatureProducer()
    close_direction_result = direction_close_producer.produce(df)['Y_close_direction_1']
    expected_close_direction = [1] * len(df)
    expected_close_direction[-1] = np.nan
    array_equal(close_direction_result, expected_close_direction)

    direction_low_producer = DirectionFeatureProducer(feature='low', lags=2)
    low_2_direction_result = direction_low_producer.produce(df)['Y_low_direction_2']
    expected_low_direction = [1, 1, 0, 0, 0, np.nan, np.nan]
    array_equal(low_2_direction_result, expected_low_direction)

