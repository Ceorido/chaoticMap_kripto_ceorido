import matplotlib.pyplot as plt


# =====================================
# CHAOTIC SEQUENCE
# =====================================
def plot_chaotic_sequence(sequence):

    fig, ax = plt.subplots(
        figsize=(10, 5)
    )

    ax.plot(
        sequence,
        linewidth=1
    )

    ax.set_title(
        "Hybrid Logistic-Sine Chaotic Sequence"
    )

    ax.set_xlabel(
        "Iteration"
    )

    ax.set_ylabel(
        "Chaos Value"
    )

    ax.grid(True)

    plt.tight_layout()

    return fig


# =====================================
# NONLINEARITY
# =====================================
def plot_nonlinearity(nl_values):

    bits = [
        f"Bit {i}"
        for i in range(len(nl_values))
    ]

    fig, ax = plt.subplots(
        figsize=(8, 5)
    )

    ax.bar(
        bits,
        nl_values
    )

    ax.set_title(
        "Nonlinearity per Output Bit"
    )

    ax.set_xlabel(
        "Output Bit"
    )

    ax.set_ylabel(
        "NL Value"
    )

    ax.grid(
        axis="y",
        linestyle="--",
        alpha=0.5
    )

    plt.tight_layout()

    return fig


# =====================================
# BIC-NL
# =====================================
def plot_bic_nl(bic_nl_results):

    pairs = [
        str(item["pair"])
        for item in bic_nl_results
    ]

    values = [
        item["nl"]
        for item in bic_nl_results
    ]

    fig, ax = plt.subplots(
        figsize=(12, 5)
    )

    ax.bar(
        pairs,
        values
    )

    ax.set_title(
        "Bit Independence Criterion - Nonlinearity"
    )

    ax.set_xlabel(
        "Bit Pair"
    )

    ax.set_ylabel(
        "NL Value"
    )

    ax.grid(
        axis="y",
        linestyle="--",
        alpha=0.5
    )

    plt.xticks(
        rotation=90
    )

    plt.tight_layout()

    return fig


# =====================================
# BIC-SAC
# =====================================
def plot_bic_sac(bic_sac_results):

    pairs = [
        str(item["pair"])
        for item in bic_sac_results
    ]

    values = [
        item["bic_sac"]
        for item in bic_sac_results
    ]

    fig, ax = plt.subplots(
        figsize=(12, 5)
    )

    ax.bar(
        pairs,
        values
    )

    ax.axhline(
        y=0.5,
        linestyle="--",
        linewidth=2,
        label="Ideal SAC"
    )

    ax.set_title(
        "Bit Independence Criterion - SAC"
    )

    ax.set_xlabel(
        "Bit Pair"
    )

    ax.set_ylabel(
        "BIC-SAC"
    )

    ax.legend()

    ax.grid(
        axis="y",
        linestyle="--",
        alpha=0.5
    )

    plt.xticks(
        rotation=90
    )

    plt.tight_layout()

    return fig


# =====================================
# SUMMARY
# =====================================
def plot_summary(
        avg_nl,
        sac,
        avg_bic_nl,
        avg_bic_sac,
        lap,
        dap):

    parameters = [

        "NL",
        "SAC",
        "BIC-NL",
        "BIC-SAC",
        "LAP",
        "DAP"

    ]

    values = [

        avg_nl,
        sac,
        avg_bic_nl,
        avg_bic_sac,
        lap,
        dap

    ]

    fig, ax = plt.subplots(
        figsize=(10, 5)
    )

    ax.bar(
        parameters,
        values
    )

    ax.set_title(
        "Overall S-Box Evaluation Metrics"
    )

    ax.set_ylabel(
        "Metric Value"
    )

    ax.grid(
        axis="y",
        linestyle="--",
        alpha=0.5
    )

    plt.tight_layout()

    return fig