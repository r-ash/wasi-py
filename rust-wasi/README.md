# adder

This is a Rust binary that contains a main function which we can compile to WASI which we then call from Python to prototype functionality

### Setup

We want to use wasm as a portable way of running Rust code from a python package. For that we want the WASI, the web assembly system interface. To compile code for wasm32-wasi you need to install this in your Rust toolchain

```
rustup target add wasm32-wasi
```

Build targeting wasi using cargo wasi

```
cargo build --target wasm32-wasi --release
```

This will output a build into target/debug directory

Run using wasmer

```
wasmer run target/wasm32-wasi/release/rust-wasi.wasm --env MYVAR=MYVALUE --dir . -- --arg1=test
```

