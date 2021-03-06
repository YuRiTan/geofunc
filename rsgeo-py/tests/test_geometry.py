import numpy as np
import pytest

from rsgeo.geometry import Polygon  # noqa


class TestPolygon:
    def setup_method(self):
        self.p = Polygon([(0, 0), (1, 1), (1, 0), (0, 0)])

    def test_repr(self):
        str_repr = str(self.p)
        exp = "Polygon([(0, 0), (1, 1), (1, 0), (0, 0)])"
        assert str_repr == exp

    def test_seq_to_2darray(self):
        seq = [(1, 2), (3, 4)]
        res = self.p._seq_to_2darray(seq)
        np.testing.assert_array_equal(res, np.array([[1, 2], [3, 4]]))

    def test_seq_to_2darray_sad_case(self):
        seq = [(1, 2, 3), (4, 5, 6)]
        with pytest.raises(ValueError):
            _ = self.p._seq_to_2darray(seq)

    @pytest.mark.parametrize("x, expected", [
        (np.array([1, 2, 3]), np.array([1, 2, 3])),
        (np.array([[1], [2], [3]]), np.array([1, 2, 3])),
    ])
    def test_to_1d(self, x, expected):
        result = self.p._to_1d(x)
        np.testing.assert_array_equal(result, expected)

    def test_to_1d_sad_case(self):
        x = np.array([(1, 2, 3), (4, 5, 6)])
        with pytest.raises(ValueError):
            _ = self.p._to_1d(x)

    def test_contains(self, xs, ys):
        res = self.p.contains(xs, ys)
        np.testing.assert_array_equal(res, np.array([False, False, False, True]))

    def test_distance(self, xs, ys):
        result = self.p.distance(xs, ys)
        np.testing.assert_array_equal(result, np.array([0, 0, 1.4142135623730951, 0]))
