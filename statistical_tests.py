import scipy.stats
import numpy as np


def f_test(sample_x, sample_y, larger_varx_alt):
    sample_var_x = np.var(sample_x, ddof=1)
    sample_var_y = np.var(sample_y, ddof=1)
    f_value = sample_var_x/sample_var_y
    nx = len(sample_x)
    ny = len(sample_y)
    cdf = scipy.stats.f.cdf(f_value, nx-1, ny-1)
    p_value = 1 - cdf if larger_varx_alt else cdf
    return f_value, p_value


def f1_test(sample_x, sample_y, larger_varx_alt):
    sample_var_x = np.var(sample_x, ddof=1)
    sample_var_y = np.var(sample_y, ddof=1)
    f_value = sample_var_x/sample_var_y
    nx = len(sample_x)
    ny = len(sample_y)
    xmean = np.mean(sample_x)
    ymean = np.mean(sample_y)
    fourth_moment = (np.sum((sample_x - xmean)**4) +
                     np.sum((sample_y - ymean)**4))/(nx + ny)
    pooled_var = ((nx-1)*sample_var_x + (ny-1)*sample_var_y)/(nx + ny)
    rx = 2*nx / ((fourth_moment/pooled_var**2) - ((nx - 3)/(nx - 1)))
    ry = 2*ny / ((fourth_moment/pooled_var**2) - ((ny - 3)/(ny - 1)))
    cdf = scipy.stats.f.cdf(f_value, rx-1, ry-1)
    p_value = 1 - cdf if larger_varx_alt else cdf
    return p_value


def count_five(sample_x, sample_y, center):
    if center not in {'mean', 'median'}:
        raise ValueError('Invalid center %s' % (center))
    if center == 'mean':
        centering_x = np.mean(sample_x)
        centering_y = np.mean(sample_y)
    else:
        centering_x = np.median(sample_x)
        centering_y = np.median(sample_y)
    abs_dev_x = np.abs(np.array(sample_x) - centering_x)
    abs_dev_y = np.abs(np.array(sample_y) - centering_y)
    extreme_count_x = np.sum(np.where(abs_dev_x > np.max(abs_dev_y), 1, 0))
    extreme_count_y = np.sum(np.where(abs_dev_y > np.max(abs_dev_x), 1, 0))
    return extreme_count_x, extreme_count_y
