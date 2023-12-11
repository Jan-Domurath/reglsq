#####################
Viscoelastic Spectrum
#####################

.. math::
    :label: storage

    G'(\omega) = G_\text{e} + \sum_{i=1}^N g_i \frac{(\omega\lambda_i)^2}{1+(\omega\lambda_i)^2}


.. math::
    :label: loss

    G''(\omega) = \sum_{i=1}^N g_i \frac{\omega\lambda_i}{1+(\omega\lambda_i)^2}


.. math::
    :label: minimizer

    \mathcal{G} = \sum_{j=1}^M \left( \left[ \frac{G'(\omega_j)}{\mathring{G}'_j} - 1 \right]^2 + \left[ \frac{G''(\omega_j)}{\mathring{G}''_j} - 1 \right]^2\right)

:math:`\mathring{G}'_j` and :math:`\mathring{G}''_j` are the storage and loss moduli measured at frequency :math:`\omega_j`.

The derivative of :eq:`minimizer` is

.. math::

    \frac{\partial\mathcal{G}}{\partial\omega_j} = \sum_{j=1}^M \left( \left[ \frac{2(G'(\omega_j) - \mathring{G}'_j) \frac{\partial G'(\omega)}{\partial\omega}}{(\mathring{G}'_j)^2} \right] + \left[ \frac{2(G''(\omega_j) - \mathring{G}''_j) \frac{\partial G''(\omega)}{\partial\omega}}{(\mathring{G}''_j)^2} \right] \right)

with

.. math::

    \frac{\partial G'(\omega)}{\partial\omega} = 2 g_i \frac{\lambda_i^2 \omega}{\left(1+(\omega\lambda_i)^2\right)^2}

and

.. math::

    \frac{\partial G''(\omega)}{\partial\omega} = g_i \frac{\lambda_i - \lambda_i^3 \omega^2}{\left(1+(\omega\lambda_i)^2\right)^2}
