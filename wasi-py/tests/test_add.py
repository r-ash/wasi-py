import pytest

from src.wasi_py.example import run_wasm

def test_can_run_wasi_main():
    run_wasm()
