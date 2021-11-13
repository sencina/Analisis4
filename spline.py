from numpy import array
from scipy.interpolate import UnivariateSpline, interp1d
from scipy.interpolate.interpolate import _do_extrapolate

x=[1,2,3]
y=[1,0.5,1/3]

linear = interp1d(x, y, kind='linear')
quad = interp1d(x, y, kind='quadratic')
cubic = interp1d(x, y, kind='cubic')

