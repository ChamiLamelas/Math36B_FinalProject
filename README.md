
# Important Links

* [Count Five Paper on JSTOR](https://www.jstor.org/stable/27643615)
* [Google Colab Notebook with Simulations](https://colab.research.google.com/drive/1bUGJVALhi2YsFAqSIgkcEGQpx9e1zBSN?usp=sharing)

# Repository Description

The `code` directory has a single file `statistical_tests.py` that implements the following tests:
* F-test for equal variance as formulated in [A Quick, Compact, Two-Sample Dispersion Test: Count Five](https://www.jstor.org/stable/27643615). 
* F1-test for equal variance as formulated in [Fixing the F Test for Equal Variances](https://www.jstor.org/stable/30037243). This and the F-test are implemented using [SciPy's F-distribution](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.f.html).
* The Count Five test for equal variance as formulated in [A Quick, Compact, Two-Sample Dispersion Test: Count Five](https://www.jstor.org/stable/27643615).
* [SciPy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.levene.html) provides an implementation of [Levene's test](https://itl.nist.gov/div898/handbook/eda/section3/eda35a.htm). 

The `measurements` directory has two files:
* `P(type_I_error).csv` which holds the probability of type I error estimated in the experiments conducted [here](https://colab.research.google.com/drive/1bUGJVALhi2YsFAqSIgkcEGQpx9e1zBSN?usp=sharing).
* `power.csv` which holds the power estimated in the experiments conducted [here](https://colab.research.google.com/drive/1bUGJVALhi2YsFAqSIgkcEGQpx9e1zBSN?usp=sharing).

The `p_type_I_error_plots` directory has the P(type I error) plots made [here](https://colab.research.google.com/drive/1bUGJVALhi2YsFAqSIgkcEGQpx9e1zBSN?usp=sharing).

The `power_plots` directory has the power plots made [here](https://colab.research.google.com/drive/1bUGJVALhi2YsFAqSIgkcEGQpx9e1zBSN?usp=sharing).

The `sample_observation_plots` has the sample observation plots made [here](https://colab.research.google.com/drive/1bUGJVALhi2YsFAqSIgkcEGQpx9e1zBSN?usp=sharing).

