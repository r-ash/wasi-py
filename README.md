# wasm-py

This repo contains an example of 
* A Rust binary which compiles to WASI
* A python project which then calls the wasm module using wasmer

To run this
1. Clone the repo
1. Build the Rust project `(cd rust-wasi && cargo build --target wasm32-wasi --release)`
1. Copy the wasm into the Python project `cp rust-wasi/target/wasm32-wasi/release/rust-wasi.wasm wasi-py/src/wasi_py/resources/main.wasm`
1. Run the python project tests `(cd wasi-py && hatch run test -s)` 
