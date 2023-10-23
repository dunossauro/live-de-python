import matplotlib.pyplot as plt
from librosa import load
from librosa.display import waveshow
from typer import Option, Typer

plot = Typer(no_args_is_help=True)


@plot.command()
def plot_wave(file: str, fig_name: str) -> None:
    """Plot a figure with audio wave."""
    y, sr = load(file, mono=False)
    waveshow(y, sr=sr)

    plt.savefig(fig_name)


@plot.command()
def compare_waves(
    files: list[str],
    fig_name: str,
    fig_size: tuple[float, float] = (10, 12),
    force_db: bool = Option(True, help='Force to use 1 to -1 dbs in plot'),
) -> None:
    """Plot a figure with N audio waves for comparison."""
    _, ax = plt.subplots(
        nrows=len(files), sharex=True, figsize=fig_size, tight_layout=True
    )

    for n, file in enumerate(files):
        if force_db:
            ax[n].set(ylim=[-1.1, 1.1], title=file)
        else:
            ax[n].set(title=file)
        y_b, sr_b = load(file, mono=False)
        waveshow(y_b, sr=sr_b, ax=ax[n])

    plt.savefig(fig_name)


plot()
