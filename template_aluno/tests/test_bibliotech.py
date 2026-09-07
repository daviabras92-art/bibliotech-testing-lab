import pytest

from scr.bibliotech import (
    pode_emprestar,
    calcular_multa,
    classificar_atraso,
)


# ============================================================
# RF01 - Permissão para empréstimo
# ============================================================

def test_rf01_usuario_ativo_sem_pendencia_zero_emprestimos():
    resultado = pode_emprestar(
        usuario_ativo=True,
        possui_pendencia=False,
        emprestimos_ativos=0,
    )
    assert resultado is True


def test_rf01_usuario_ativo_sem_pendencia_dois_emprestimos():
    resultado = pode_emprestar(
        usuario_ativo=True,
        possui_pendencia=False,
        emprestimos_ativos=2,
    )
    assert resultado is True


def test_rf01_usuario_inativo():
    resultado = pode_emprestar(
        usuario_ativo=False,
        possui_pendencia=False,
        emprestimos_ativos=0,
    )
    assert resultado is False


def test_rf01_usuario_com_pendencia():
    resultado = pode_emprestar(
        usuario_ativo=True,
        possui_pendencia=True,
        emprestimos_ativos=0,
    )
    assert resultado is False


def test_rf01_limite_tres_emprestimos():
    resultado = pode_emprestar(
        usuario_ativo=True,
        possui_pendencia=False,
        emprestimos_ativos=3,
    )
    assert resultado is False


# ============================================================
# RF02 - Cálculo de multa
# ============================================================

def test_rf02_sem_atraso():
    assert calcular_multa(0) == 0.0
    assert calcular_multa(-1) == 0.0


def test_rf02_um_dia_de_atraso():
    assert calcular_multa(1) == pytest.approx(2.0)


def test_rf02_sete_dias_de_atraso():
    assert calcular_multa(7) == pytest.approx(14.0)


def test_rf02_oito_dias_de_atraso():
    assert calcular_multa(8) == pytest.approx(17.0)


def test_rf02_dez_dias_de_atraso():
    assert calcular_multa(10) == pytest.approx(23.0)


# ============================================================
# RF03 - Classificação de atraso
# ============================================================

def test_rf03_sem_atraso():
    assert classificar_atraso(0) == "sem atraso"


def test_rf03_atraso_leve():
    assert classificar_atraso(1) == "atraso leve"
    assert classificar_atraso(7) == "atraso leve"


def test_rf03_atraso_moderado():
    assert classificar_atraso(8) == "atraso moderado"
    assert classificar_atraso(30) == "atraso moderado"


def test_rf03_atraso_grave():
    assert classificar_atraso(31) == "atraso grave"


def test_rf03_atraso_negativo():
    assert classificar_atraso(-1) == "sem atraso"
