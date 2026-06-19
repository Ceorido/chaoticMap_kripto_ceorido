import streamlit as st
import pandas as pd

from chaotic_sbox import generate_chaotic_sbox
from lap import calculate_lap
from dap import calculate_dap
from nonlinearity import calculate_nonlinearity
from sac import calculate_sac
from bic_NL import calculate_bic_nl
from bic_SAC import calculate_bic_sac
from plot_graph import (
    plot_summary,
    plot_nonlinearity,
    plot_bic_nl,
    plot_bic_sac,
    plot_chaotic_sequence
)



# =====================================
# LOAD SBOX
# =====================================
def load_sbox(uploaded_file):

    content = uploaded_file.read().decode("utf-8")

    values = []

    for item in content.replace(",", " ").split():

        try:
            values.append(int(item))
        except:
            pass

    return values


# =====================================
# STREAMLIT CONFIG
# =====================================
st.set_page_config(
    page_title="S-Box Evaluation Dashboard",
    page_icon="🔐",
    layout="wide"
)

st.title("🔐 S-Box Evaluation Dashboard")

st.write(
    "Evaluasi keamanan S-Box menggunakan "
    "NL, SAC, BIC-NL, BIC-SAC, LAP, dan DAP."
)

st.divider()

# =====================================
# SBOX SOURCE
# =====================================

source_option = st.radio(
    "Sumber S-Box",
    [
        "Upload S-Box",
        "Generate Chaotic S-Box"
    ]
)

sbox = None

# =====================================
# UPLOAD MODE
# =====================================

if source_option == "Upload S-Box":

    uploaded_file = st.file_uploader(
        "Upload S-Box (.txt)",
        type=["txt"]
    )

    if uploaded_file is not None:

        sbox = load_sbox(uploaded_file)

        st.success(
            f"S-Box loaded successfully "
            f"({len(sbox)} elements)"
        )

# =====================================
# CHAOTIC MODE
# =====================================

else:

    st.subheader(
        "Hybrid Logistic-Sine Map"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        x0 = st.number_input(
            "Initial Value (x0)",
            value=0.54321,
            min_value=0.000001,
            max_value=0.999999,
            format="%.6f"
        )

    with col2:

        r = st.number_input(
            "Control Parameter (r)",
            value=3.99,
            min_value=3.57,
            max_value=4.0,
            format="%.4f"
        )

    with col3:

        discard = st.number_input(
            "Transient Removal",
            value=1000,
            min_value=100,
            step=100
        )

    if st.button(
        "Generate Chaotic S-Box",
        use_container_width=True
    ):

        sbox, chaotic_sequence = (
            generate_chaotic_sbox(
                x0=x0,
                r=r,
                discard=discard
            )
        )

        st.session_state["sbox"] = sbox
        st.session_state["chaos"] = (
            chaotic_sequence
        )

if "sbox" in st.session_state:

    sbox = st.session_state["sbox"]

# =====================================
# VALIDATION
# =====================================

if sbox is not None:

    if len(sbox) != 256:

        st.error(
            "S-Box harus berisi "
            "tepat 256 elemen."
        )

        st.stop()

    if len(set(sbox)) != 256:

        st.error(
            "S-Box bukan permutasi valid."
        )

        st.stop()

    st.success(
        "S-Box valid dan siap dianalisis."
    )

    # ==========================
    # CHAOTIC PREVIEW
    # ==========================

    if (
        source_option ==
        "Generate Chaotic S-Box"
        and "chaos"
        in st.session_state
    ):

        st.subheader(
            "Chaotic Sequence Preview"
        )

        chaos_df = pd.DataFrame({

            "Iteration":
            list(range(256)),

            "Chaos Value":
            st.session_state["chaos"]

        })

        st.dataframe(
            chaos_df,
            height=250,
            use_container_width=True
        )

    st.divider()

    # =====================================
    # RUN ANALYSIS
    # =====================================
    if st.button(
        "🚀 Jalankan Semua Analisis",
        use_container_width=True
    ):

        with st.spinner("Sedang menghitung..."):

            # ==========================
            # LAP
            # ==========================
            lap_value, input_mask, output_mask = \
                calculate_lap(sbox)

            # ==========================
            # DAP
            # ==========================
            dap_value, max_count, dx, dy = \
                calculate_dap(sbox)

            # ==========================
            # NONLINEARITY
            # ==========================
            nl_values = \
                calculate_nonlinearity(sbox)

            avg_nl = (
                sum(nl_values)
                / len(nl_values)
            )

            # ==========================
            # SAC
            # ==========================
            sac_value = \
                calculate_sac(sbox)

            # ==========================
            # BIC-NL
            # ==========================
            bic_nl_results = \
                calculate_bic_nl(sbox)

            avg_bic_nl = (
                sum(
                    item["nl"]
                    for item in bic_nl_results
                )
                / len(bic_nl_results)
            )

            # ==========================
            # BIC-SAC
            # ==========================
            bic_sac_results = \
                calculate_bic_sac(sbox)

            avg_bic_sac = (
                sum(
                    item["bic_sac"]
                    for item in bic_sac_results
                )
                / len(bic_sac_results)
            )

        st.success("Analisis selesai.")

        # =====================================
        # REKAPITULASI
        # =====================================
        st.header(
            "📋 Rekapitulasi Hasil Akhir Project"
        )

        summary_df = pd.DataFrame({

            "Parameter": [

                "NL",
                "SAC",
                "BIC-NL",
                "BIC-SAC",
                "LAP",
                "DAP"

            ],

            "Nilai": [

                round(avg_nl, 2),
                round(sac_value, 4),
                round(avg_bic_nl, 2),
                round(avg_bic_sac, 4),
                round(lap_value, 4),
                round(dap_value, 4)

            ]

        })

        st.table(summary_df)

        st.divider()

        # =====================================
        # DETAIL ANALISIS
        # =====================================
        tab1, tab2, tab3, tab4, tab5 = st.tabs(
            [
                "LAP",
                "DAP",
                "NL",
                "BIC-NL",
                "BIC-SAC"
            ]
        )

        # =====================================
        # LAP
        # =====================================
        with tab1:

            st.subheader(
                "Linear Approximation Probability"
            )

            st.write(
                f"Input Mask : {input_mask}"
            )

            st.write(
                f"Output Mask : {output_mask}"
            )

            st.write(
                f"LAP : {lap_value:.6f}"
            )

        # =====================================
        # DAP
        # =====================================
        with tab2:

            st.subheader(
                "Differential Approximation Probability"
            )

            st.write(
                f"Input Difference : {dx}"
            )

            st.write(
                f"Output Difference : {dy}"
            )

            st.write(
                f"Maximum Count : {max_count}"
            )

            st.write(
                f"DAP : {dap_value:.6f}"
            )

        # =====================================
        # NONLINEARITY
        # =====================================
        with tab3:

            nl_df = pd.DataFrame({

                "Bit":
                [f"Bit {i}" for i in range(8)],

                "Nonlinearity":
                nl_values

            })

            st.dataframe(
                nl_df,
                use_container_width=True
            )

            st.write(
                f"Average NL = {avg_nl:.2f}"
            )

        # =====================================
        # BIC-NL
        # =====================================
        with tab4:

            bic_nl_df = pd.DataFrame(
                [
                    {
                        "Pair":
                        str(item["pair"]),

                        "NL":
                        item["nl"]
                    }
                    for item in bic_nl_results
                ]
            )

            st.dataframe(
                bic_nl_df,
                use_container_width=True
            )

            st.write(
                f"Average BIC-NL = "
                f"{avg_bic_nl:.2f}"
            )

        # =====================================
        # BIC-SAC
        # =====================================
        with tab5:

            bic_sac_df = pd.DataFrame(
                [
                    {
                        "Pair":
                        str(item["pair"]),

                        "BIC-SAC":
                        item["bic_sac"]
                    }
                    for item in bic_sac_results
                ]
            )

            st.dataframe(
                bic_sac_df,
                use_container_width=True
            )

            st.write(
                f"Average BIC-SAC = "
                f"{avg_bic_sac:.4f}"
            )

        st.divider()

        # =====================================
        # SBOX PREVIEW
        # =====================================
        st.subheader("S-Box Preview")

        preview_df = pd.DataFrame({

            "Index":
            list(range(256)),

            "Value":
            sbox

        })

        st.dataframe(
            preview_df,
            height=350,
            use_container_width=True
        )

        st.header("📈 Visualization")

        summary_fig = plot_summary(
            avg_nl,
            sac_value,
            avg_bic_nl,
            avg_bic_sac,
            lap_value,
            dap_value
        )

        st.pyplot(summary_fig)

        nl_fig = plot_nonlinearity(
            nl_values
        )

        st.pyplot(nl_fig)

        bic_nl_fig = plot_bic_nl(
            bic_nl_results
        )

        st.pyplot(bic_nl_fig)

        bic_sac_fig = plot_bic_sac(
            bic_sac_results
        )

        st.pyplot(bic_sac_fig)

        if "chaos" in st.session_state:

            chaos_fig = plot_chaotic_sequence(
                st.session_state["chaos"]
            )

            st.pyplot(chaos_fig)