def make_dist():
    return default_python_distribution()


def make_exe(dist):
    policy = dist.make_python_packaging_policy()
    policy.allow_files = True
    policy.set_resource_handling_mode("files")

    python_config = dist.make_python_interpreter_config()
    python_config.run_module = "live_bin"

    exe = dist.to_python_executable(
        name="live_bin",
        packaging_policy=policy,
        config=python_config,
    )
    exe.add_python_resources(exe.pip_install(["."]))
    exe.add_python_resources(exe.read_package_root(
        path=".",
        packages=["live_bin"],
    ))

    exe.tcl_files_path = "lib"

    return exe


def make_embedded_resources(exe):
    return exe.to_embedded_resources()


def make_install(exe):
    files = FileManifest()

    files.add_python_resource(".", exe)

    return files

def make_msi(exe):
    return exe.to_wix_msi_builder(
        # Simple identifier of your app.
        "myapp",
        # The name of your application.
        "My Application",
        # The version of your application.
        "1.0",
        # The author/manufacturer of your application.
        "Alice Jones"
    )


def register_code_signers():
    if not VARS.get("ENABLE_CODE_SIGNING"):
        return

register_code_signers()

# Tell PyOxidizer about the build targets defined above.
register_target("dist", make_dist)
register_target("exe", make_exe, depends=["dist"])
register_target("resources", make_embedded_resources, depends=["exe"], default_build_script=True)
register_target("install", make_install, depends=["exe"], default=True)
register_target("msi_installer", make_msi, depends=["exe"])

resolve_targets()


PYOXIDIZER_VERSION = "0.16.2"
PYOXIDIZER_COMMIT = "e91995636f8deed0a7d8e1917f96a7dc17309b63"
