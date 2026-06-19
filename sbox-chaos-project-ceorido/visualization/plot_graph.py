import matplotlib.pyplot as plt
import pandas as pd


# =====================================
# CHAOTIC SEQUENCE
# =====================================
def plot_chaotic_sequence(sequence):

    plt.figure(figsize=(10, 5))

    plt.plot(sequence)

    plt.title(
        "Hybrid Logistic-Sine Chaotic Sequence"
    )

    plt.xlabel("Iteration")

    plt.ylabel("Chaos Value")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        "chaotic_sequence.png",
        dpi=300
    )

    plt.show()


# =====================================
# NONLINEARITY
# =====================================
def plot_nonlinearity(nl_values):

    bits = [
        f"Bit {i}"
        for i in range(len(nl_values))
    ]

    plt.figure(figsize=(8, 5))

    plt.bar(bits, nl_values)

    plt.title(
        "Nonlinearity per Output Bit"
    )

    plt.ylabel("NL Value")

    plt.grid(
        axis="y",
        linestyle="--",
        alpha=0.5
    )

    plt.tight_layout()

    plt.savefig(
        "nonlinearity.png",
        dpi=300
    )

    plt.show()


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

    plt.figure(figsize=(12, 5))

    plt.bar(pairs, values)

    plt.title(
        "BIC Nonlinearity"
    )

    plt.xlabel("Bit Pair")

    plt.ylabel("NL")

    plt.xticks(rotation=90)

    plt.tight_layout()

    plt.savefig(
        "bic_nl.png",
        dpi=300
    )

    plt.show()


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

    plt.figure(figsize=(12, 5))

    plt.bar(pairs, values)

    plt.axhline(
        y=0.5,
        linestyle="--"
    )

    plt.title(
        "BIC-SAC"
    )

    plt.xlabel("Bit Pair")

    plt.ylabel("BIC-SAC")

    plt.xticks(rotation=90)

    plt.tight_layout()

    plt.savefig(
        "bic_sac.png",
        dpi=300
    )

    plt.show()


# =====================================
# SUMMARY GRAPH
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

    plt.figure(figsize=(10, 5))

    plt.bar(
        parameters,
        values
    )

    plt.title(
        "Overall S-Box Evaluation"
    )

    plt.ylabel("Value")

    plt.grid(
        axis="y",
        linestyle="--",
        alpha=0.5
    )

    plt.tight_layout()

    plt.savefig(
        "summary_metrics.png",
        dpi=300
    )

    plt.show()