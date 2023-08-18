import requests
import scipy

def preprocess(x, y, xout):

    x = x[~np.isnan(x)] 
    method = "cubic"
    # interpolate missing values with cubic spline
    return scipy.interpolate.interp1d(x, y)(xout)
