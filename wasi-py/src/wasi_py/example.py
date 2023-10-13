from wasmer import engine, wasi, Store, Module, ImportObject, Instance
from wasmer_compiler_cranelift import Compiler
from importlib import resources as impresources
from . import resources


def run_wasm():

    wasm_file = (impresources.files(resources) / "main.wasm")

    # Create a store. Engines and compilers are explained in other
    # examples.
    store = Store(engine.Universal(Compiler))

    # Let's compile the Wasm module.
    module = Module(
        store,
        wasm_file.open('rb').read())

    # First, let's extract the WASI version from the module. Why? Because
    # WASI already exists in multiple versions, and it doesn't work the
    # same way. So, to ensure compatibility, we need to know the version.
    wasi_version = wasi.get_version(module, strict=True)

    # Second, create a `wasi.Environment`. It contains everything related
    # to WASI. To build such an environment, we must use the
    # `wasi.StateBuilder`.
    #
    # In this case, we specify the program name is `wasi_test_program`. We
    # also specify the program is invoked with the `--test` argument, in
    # addition to two environment variable: `COLOR` and
    # `APP_SHOULD_LOG`. Finally, we map the `the_host_current_dir` to the
    # current directory. There it is:
    wasi_env = \
        wasi.StateBuilder('wasi_test_program'). \
            argument('--test'). \
            environment('COLOR', 'true'). \
            environment('APP_SHOULD_LOG', 'false'). \
            map_directory('the_host_current_dir', '.'). \
            finalize()

    # From the WASI environment, we generate a custom import object. Why?
    # Because WASI is, from the user perspective, a bunch of
    # imports. Consequently `generate_import_object`… generates a
    # pre-configured import object.
    #
    # Do you remember when we said WASI has multiple versions? Well, we
    # need the WASI version here!
    import_object = wasi_env.generate_import_object(store, wasi_version)

    # Now we can instantiate the module.
    instance = Instance(module, import_object)

    # The entry point for a WASI WebAssembly module is a function named
    # `_start`. Let's call it and see what happens!
    instance.exports._start()

