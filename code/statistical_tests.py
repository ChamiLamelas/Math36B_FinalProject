import scipy.stats
import numpy as np


def f_test(sample_x, sample_y, larger_varx_alt):
    """
    Computes the F-value and corresponding p-value for a pair of samples and alternative hypothesis.

    Parameters
    ----------
    sample_x : list
        A random sample x1,...,xnx. Let its (underlying) variance be ox^2 and its sample variance Sx^2. 
    sample_y : list
        A random sample y1,...,yny. Let its (underlying) variance be oy^2 and its sample variance Sy^2.
    larger_varx_alt : bool
        True if alternative hypothesis is ox^2 > oy^2. False if ox^2 < oy^2. 

    Returns
    -------
    f_value : float
        Sx^2 / Sy^2 as defined in 'A Quick, Compact, Two-Sample Dispersion Test: Count Five'.
    p_value : 
        Let F be the F-distribution with nx, ny df. 1 - P(F < f_value) if larger_varx_alt = True, P(F < f_value) otherwise. More extreme F = Sx^2 / Sy^2 values for alternative ox^2 > oy^2 are to the right. More extreme F values for ox^2 < oy^2 are to the left. 
    """

    # calculate unbiased sample variances (n-1 in the denominator)
    sample_var_x = np.var(sample_x, ddof=1)
    sample_var_y = np.var(sample_y, ddof=1)
    f_value = sample_var_x/sample_var_y
    nx = len(sample_x)
    ny = len(sample_y)

    # compute P(F < f_value) with nx-1, ny-1 df
    cdf = scipy.stats.f.cdf(f_value, nx-1, ny-1)

    # More extreme f_value = Sx^2 / Sy^2 values for alternative ox^2 > oy^2. ox^2 being even bigger would be represented by larger quotient Sx^2 / Sy^2.
    # More extreme f_value for ox^2 < oy^2 are to the left. ox^2 being even smaller would be represented by smaller quotient.
    p_value = 1 - cdf if larger_varx_alt else cdf
    return f_value, p_value


def f1_test(sample_x, sample_y, larger_varx_alt):
    """
    Computes the F1-value as defined in 'Fixing the F Test for Equal Variances' and corresponding p-value for a pair of samples and alternative hypothesis. 

    Parameters
    ----------
    sample_x : list
        A random sample x1,...,xnx. Let its (underlying) variance be ox^2 and its sample variance Sx^2. 
    sample_y : list
        A random sample y1,...,yny. Let its (underlying) variance be oy^2 and its sample variance Sy^2.
    larger_varx_alt : bool
        True if alternative hypothesis is ox^2 > oy^2. False if ox^2 < oy^2. 

    Returns
    -------
    p_value : 
        Let F be the F-distribution with rx, ry df as specified in equation (1) of 'Fixing the F Test for Equal Variances'. 1 - P(F < f_value) if larger_varx_alt = True, P(F < f_value) otherwise. 
    """

    # calculate unbiased sample variances (n-1 in the denominator)
    sample_var_x = np.var(sample_x, ddof=1)
    sample_var_y = np.var(sample_y, ddof=1)
    f_value = sample_var_x/sample_var_y
    nx = len(sample_x)
    ny = len(sample_y)
    xmean = np.mean(sample_x)
    ymean = np.mean(sample_y)

    # compute moment, variance below equatio (1) of Shoemaker paper
    fourth_moment = (np.sum((sample_x - xmean)**4) +
                     np.sum((sample_y - ymean)**4))/(nx + ny)
    pooled_var = ((nx-1)*sample_var_x + (ny-1)*sample_var_y)/(nx + ny)

    # see equation (1) of Shoemaker paper
    rx = 2*nx / ((fourth_moment/pooled_var**2) - ((nx - 3)/(nx - 1)))
    ry = 2*ny / ((fourth_moment/pooled_var**2) - ((ny - 3)/(ny - 1)))

    # compute P(F < f_value) with rx-1, ry-1 df
    cdf = scipy.stats.f.cdf(f_value, rx-1, ry-1)

    # More extreme f_value = Sx^2 / Sy^2 values for alternative ox^2 > oy^2. ox^2 being even bigger would be represented by larger quotient Sx^2 / Sy^2.
    # More extreme f_value for ox^2 < oy^2 are to the left. ox^2 being even smaller would be represented by smaller quotient.
    p_value = 1 - cdf if larger_varx_alt else cdf
    return p_value


def count_five(sample_x, sample_y, center):
    """
    Computes the extreme counts for samples x and y as defined in 'A Quick, Compact, Two-Sample Dispersion Test: Count Five'.

    Parameters
    ----------
        sample_x : list
            A random sample x1,...,xn. 
        sample_y : list
            A random sample y1,...,ym.
        center : str
            Whether to use 'mean' or 'median' for centering. 
    Returns
    -------
        extreme_count_x : int
            C_x computed with centering mu being sample mean if center = 'mean' and sample median if center = 'median' as defined in equation (1) of 'A Quick, Compact, Two-Sample Dispersion Test: Count Five'.
        extreme_count_y : int
            C_y defined analogously to C_x above.
    Raises
    ------
    ValueError
        If center is neither 'mean' or 'median'.
    """

    if center not in {'mean', 'median'}:
        raise ValueError('Invalid center %s' % (center))
    if center == 'mean':
        centering_x = np.mean(sample_x)
        centering_y = np.mean(sample_y)
    else:
        centering_x = np.median(sample_x)
        centering_y = np.median(sample_y)

    # compute absolute deviations from centering for x, y samples
    abs_dev_x = np.abs(np.array(sample_x) - centering_x)
    abs_dev_y = np.abs(np.array(sample_y) - centering_y)

    # count number of X deviations greater than max Y deviation and vice versa
    # see equation (1) of Count Five paper
    extreme_count_x = np.sum(np.where(abs_dev_x > np.max(abs_dev_y), 1, 0))
    extreme_count_y = np.sum(np.where(abs_dev_y > np.max(abs_dev_x), 1, 0))
    return extreme_count_x, extreme_count_y
