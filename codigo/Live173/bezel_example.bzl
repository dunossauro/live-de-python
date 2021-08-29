def make_dist():
    return default_python_distribution(flavor='standalone_dynamic')


def make_exe(dist):
    policy = dist.make_python_packaging_policy()
    policy.allow_files = True
    policy.set_resource_handling_mode("files")
    # policy.resources_location = "filesystem-relative:lib"
    policy.resources_location_fallback = "filesystem-relative:lib"

    python_config = dist.make_python_interpreter_config()
    python_config.module_search_paths = ["$ORIGIN/lib"]

    python_config.run_module = "live_bin"
    exe = dist.to_python_executable(
        name="live_bin",
        packaging_policy=policy,
        config=python_config,
    )
    exe.add_python_resources(exe.pip_install(["."]))
    # exe.add_python_resources(exe.pip_install(["-r", "requirements.txt"]))
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


register_target("dist", make_dist)
register_target("exe", make_exe, depends=["dist"])
register_target("resources", make_embedded_resources, depends=["exe"], default_build_script=True)
register_target("install", make_install, depends=["exe"], default=True)

resolve_targets()

# -----------------------------

PYOXIDIZER_VERSION = "0.16.2"
PYOXIDIZER_COMMIT = "e91995636f8deed0a7d8e1917f96a7dc17309b63"
