#######################
Tikhonov regularization
#######################

In the linear case the Tikhonov [#Tychonov]_ regularization is defined as :cite:`strang2007computational,wiki:Ridge_regression`

.. math::
    :label: Tikhonov

    \min_{\boldsymbol{\beta}}\|A\boldsymbol{\beta} - \boldsymbol{y}\|_2^2 + \|\Gamma \boldsymbol{\beta}\|_2^2

with :math:`\Gamma` usually chosen as :math:`\alpha I`. Where :math:`I` is the identity matrix and :math:`\alpha` is a scalar constant. With :math:`\Gamma=\alpha I`   :eq:`Tikhonov` becomes

.. math::
    :label: Tikhonov-x

    \min_{\boldsymbol{\beta}}\|A\boldsymbol{\beta} - \boldsymbol{y}\|_2^2 + \alpha \|\boldsymbol{\beta}\|_2^2

For :math:`\alpha = 0` :eq:`Tikhonov-x` reduces to the usual least squares definition :cite:`strang2007computational`.

In the nonlinear case we may write

.. math::
    :label: Tikhonov-nonlin

    \min_{\boldsymbol{\beta}} \sum_i \left[f(x_i, \boldsymbol{\beta}) - y_i \right]^2 + \alpha \|\boldsymbol{\beta}\|_2^2

.. caution::

    While :eq:`Tikhonov-nonlin` is clearly the same as :eq:`Tikhonov-x` if :math:`f(x_i, \boldsymbol{\beta})` is a polynomial. I'm not entirely sure that it is fully mathematically correct, meaning I lake a proof of :eq:`Tikhonov-nonlin`.

.. rubric:: Footnotes

.. [#Tychonov] Sometimes also spelled "Tychonov", for example in :cite:`strang2007computational`.
