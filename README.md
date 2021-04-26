The `code` directory has a single file `statistical_tests.py` that implements the following tests:
* F-test for equal variance as formulated in [A Quick, Compact, Two-Sample Dispersion Test: Count Five](https://www.jstor.org/stable/27643615). 
* F1-test for equal variance as formulated in [Fixing the F Test for Equal Variances](https://www.jstor.org/stable/30037243). This and the F-test are implemented using [SciPy's F-distribution](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.f.html).
* The Count Five test for equal variance as formulated in [A Quick, Compact, Two-Sample Dispersion Test: Count Five](https://www.jstor.org/stable/27643615).
* [SciPy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.levene.html) provides an implementation of [Levene's test](https://itl.nist.gov/div898/handbook/eda/section3/eda35a.htm). 

The `data` directory holds:
* `example1.csv` which holds the data table found in Table 1 of [A Quick, Compact, Two-Sample Dispersion Test: Count Five](https://www.jstor.org/stable/27643615).
* `student-mat.csv` as taken from the [UCI Machine Learning Database](http://archive.ics.uci.edu/ml/datasets/Student+Performance). 
* `student-por.csv` as taken from the [UCI Machine Learning Database](http://archive.ics.uci.edu/ml/datasets/Student+Performance).
* `student.txt` as taken from the [UCI Machine Learning Database](http://archive.ics.uci.edu/ml/datasets/Student+Performance).  
