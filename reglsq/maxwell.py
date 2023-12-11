"""Maxwell model of visco elasticity."""


import numpy as np
import numpy.typing as npt


def storage_modulus(omega: npt.NDArray, g_e: float, lambda_i: npt.NDArray, g_i: npt.NDArray) -> npt.NDArray:
    """Storage modulus for the Maxwell model"""
    g_prime = np.zeros_like(omega, dtype=np.float64)

    for lamda, g in zip(lambda_i, g_i, strict=True):
        g_prime += g * (omega*lamda)**2 / (1 + (omega*lamda)**2)

    return g_e + g_prime


def loss_modulus(omega: npt.NDArray, lambda_i: npt.NDArray, g_i: npt.NDArray) -> npt.NDArray:
    """Loss modulus for the Maxwell model"""
    g_dbl_prime = np.zeros_like(omega, dtype=np.float64)

    for lamda, g in zip(lambda_i, g_i, strict=True):
        g_dbl_prime += g * (omega*lamda) / (1 + (omega*lamda)**2)

    return g_dbl_prime


def diff_storage_modulus(omega: npt.NDArray, g_e: float, lambda_i: npt.NDArray, g_i: npt.NDArray) -> npt.NDArray:
    """Derivative of storage modulus for the Maxwell model"""
    g_prime = np.zeros_like(omega, dtype=np.float64)

    for lamda, g in zip(lambda_i, g_i, strict=True):
        g_prime += g * omega*lamda**2 / (1 + (omega*lamda)**2)**2

    return g_prime


def diff_loss_modulus(omega: npt.NDArray, lambda_i: npt.NDArray, g_i: npt.NDArray) -> npt.NDArray:
    """Derivative of loss modulus for the Maxwell model"""
    g_dbl_prime = np.zeros_like(omega, dtype=np.float64)

    for lamda, g in zip(lambda_i, g_i, strict=True):
        g_dbl_prime += g * (lamda - omega**2*lamda**3) / (1 + (omega*lamda)**2)**2

    return g_dbl_prime
