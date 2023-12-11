"""Fit the Mawell spectrum."""

from typing import List, Tuple

import numpy as np
import numpy.typing as npt
from scipy.optimize import minimize

from .maxwell import loss_modulus, storage_modulus, diff_loss_modulus, diff_storage_modulus


def loss_maxwell(omega: npt.NDArray, y: Tuple[npt.NDArray, npt.NDArray], p: Tuple[float, npt.NDArray, npt.NDArray]) -> float:
    """Loss for maxwell"""
    g_e, lambda_i, g_i = p

    # g_e = np.abs(g_e)
    # lambda_i = np.abs(lambda_i)
    # g_i = np.abs(g_i)

    g_prime_meas, g_dbl_prime_meas = y

    g_prime = storage_modulus(omega=omega, g_e=g_e, lambda_i=lambda_i, g_i=g_i)
    g_dbl_prime = loss_modulus(omega=omega, lambda_i=lambda_i, g_i=g_i)

    #  mse = (np.log(g_prime)/np.log(g_prime_meas) - 1)**2 + (np.log(g_dbl_prime)/np.log(g_dbl_prime_meas) - 1)**2
    mse = ((g_prime)/(g_prime_meas) - 1)**2 + ((g_dbl_prime)/(g_dbl_prime_meas) - 1)**2

    return np.sum(mse)


def diff_loss_maxwell(omega: npt.NDArray, y: Tuple[npt.NDArray, npt.NDArray], p: Tuple[float, npt.NDArray, npt.NDArray]):
    g_e, lambda_i, g_i = p

    g_prime_meas, g_dbl_prime_meas = y

    g_prime = storage_modulus(omega=omega, g_e=g_e, lambda_i=lambda_i, g_i=g_i)
    g_dbl_prime = loss_modulus(omega=omega, lambda_i=lambda_i, g_i=g_i)

    mse = ((g_prime)/(g_prime_meas) - 1)**2 + ((g_dbl_prime)/(g_dbl_prime_meas) - 1)**2


def reg(p: Tuple[float, npt.NDArray, npt.NDArray]):
    """Regularization"""
    g_e, lambda_i, g_i = p

    res = g_e**2 + lambda_i**2 + g_i**2

    return np.sum((res))


def split_p(p):
    g_e = p[0]
    p = p[1:]
    lambda_i = np.asarray(p[:len(p)//2])
    g_i = np.asarray(p[len(p)//2:])

    return g_e, lambda_i, g_i


class MaxwellCost:
    def __init__(self, omega, g_prime_meas: npt.NDArray, g_dbl_prime_meas: npt.NDArray) -> None:
        self.omega = omega
        self.g_prime_meas = g_prime_meas
        self.g_dbl_prime_meas = g_dbl_prime_meas
        self.alpha = 0.1

    def __call__(self, p: List[float]) -> float:
        g_e, lambda_i, g_i = split_p(p)

        loss_maxw = loss_maxwell(omega=self.omega, y=(self.g_prime_meas, self.g_dbl_prime_meas), p=(g_e, lambda_i, g_i))
        r = reg((g_e, lambda_i, g_i))

        return loss_maxw + self.alpha*r

    def diff(self, p: List[float]):




if __name__ == '__main__':
    lmda = [2.4e-3, 3.4e-2, 5.2e-1, 7.5e0, 8.1e1]
    g = [4e-3, 2e-2, 6e-1, 2e0, 3e1]

    omg = np.logspace(-4, 2, 30)

    g_prime_meas = storage_modulus(omg, 0, lmda, g)
    g_dbl_prime_meas = loss_modulus(omg, lmda, g)


    mw = MaxwellCost(omg, g_prime_meas, g_dbl_prime_meas)
    mw.alpha = 1e-4

    x0 = [1, 5e-3, 5e-2, 5e-1, 5e0, 5e1, 1e-2, 2e-2, 3e-1, 4, 10]
    mini = minimize(mw, x0=x0, method='Nelder-Mead')
    g_e_f, lambda_i_f, g_i_f = split_p(mini.x)
    g_prime = storage_modulus(omg, g_e_f, lambda_i_f, g_i_f)
    g_dbl_prime = loss_modulus(omg, lambda_i_f, g_i_f)


    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()

    ax.plot(omg, g_prime_meas, 'o')
    ax.plot(omg, g_dbl_prime_meas, 'd')

    ax.plot(omg, g_prime)
    ax.plot(omg, g_dbl_prime)

    print(g_e_f)
    print(lmda, lambda_i_f)
    print(g, g_i_f)

    ax.loglog()
    plt.show()
