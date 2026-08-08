import os
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
from matplotlib.path import Path as MplPath
import matplotlib.patches as patches


OUT = Path(__file__).resolve().parent / "figures"
OUT.mkdir(parents=True, exist_ok=True)

TEAL = "#159A9C"
AMBER = "#F2A23A"
PURPLE = "#7B61FF"
CHARCOAL = "#263238"
GRAY = "#EEF2F5"
DARK_GRAY = "#60717B"


def box(ax, xy, wh, text, fc="white", ec=CHARCOAL, lw=1.4, fs=9, weight="regular"):
    x, y = xy
    w, h = wh
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.018,rounding_size=0.04",
        linewidth=lw,
        edgecolor=ec,
        facecolor=fc,
        zorder=2,
    )
    ax.add_patch(patch)
    ax.text(
        x + w / 2,
        y + h / 2,
        text,
        ha="center",
        va="center",
        fontsize=fs,
        color=CHARCOAL,
        fontweight=weight,
        linespacing=1.12,
        zorder=3,
    )
    return patch


def arrow(ax, p1, p2, color=CHARCOAL, lw=1.6, rad=0.0, ms=13, style="-|>"):
    arr = FancyArrowPatch(
        p1,
        p2,
        arrowstyle=style,
        mutation_scale=ms,
        linewidth=lw,
        color=color,
        connectionstyle=f"arc3,rad={rad}",
        zorder=4,
    )
    ax.add_patch(arr)
    return arr


def manifold_curve(ax, color, yoff=0.0, label=None):
    verts = [
        (0.62, 0.22 + yoff),
        (0.70, 0.31 + yoff),
        (0.80, 0.15 + yoff),
        (0.90, 0.27 + yoff),
    ]
    codes = [MplPath.MOVETO, MplPath.CURVE4, MplPath.CURVE4, MplPath.CURVE4]
    path = MplPath(verts, codes)
    patch = patches.PathPatch(path, facecolor="none", edgecolor=color, lw=3.0, alpha=0.72, zorder=1)
    ax.add_patch(patch)
    for x, y in [(0.67, 0.27 + yoff), (0.78, 0.20 + yoff), (0.87, 0.25 + yoff)]:
        ax.scatter([x], [y], s=36, color=color, edgecolor="white", linewidth=0.9, zorder=5)
    if label:
        ax.text(0.76, 0.08 + yoff, label, ha="center", fontsize=8.5, color=color, fontweight="bold")


def make_architecture():
    fig, ax = plt.subplots(figsize=(13.4, 7.1))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # Background grid.
    for x in [i / 20 for i in range(1, 20)]:
        ax.plot([x, x], [0.04, 0.96], color=GRAY, lw=0.5, zorder=0)
    for y in [i / 20 for i in range(1, 20)]:
        ax.plot([0.02, 0.98], [y, y], color=GRAY, lw=0.5, zorder=0)

    ax.text(
        0.035,
        0.94,
        "DUET: Dual Manifold Alignment",
        fontsize=18,
        color=CHARCOAL,
        fontweight="bold",
        ha="left",
        va="center",
    )
    ax.text(
        0.035,
        0.895,
        "Relative actions form a local tangent field; absolute waypoints define global state-manifold anchors.",
        fontsize=10.5,
        color=DARK_GRAY,
        ha="left",
    )

    box(ax, (0.05, 0.74), (0.19, 0.08), "Images $o_t$\nInstruction $l$", fc="#F8FAFB")
    box(ax, (0.28, 0.74), (0.20, 0.08), "Optional state text\n$<state>\\ s_t\\ </state>$", fc="#F8FAFB")
    box(ax, (0.16, 0.58), (0.28, 0.10), "Shared causal VLM\nQwen-VL hidden states $H$", fc="#F5F7FF", ec=PURPLE, lw=1.8, weight="bold")

    arrow(ax, (0.145, 0.74), (0.24, 0.68), color=DARK_GRAY)
    arrow(ax, (0.38, 0.74), (0.34, 0.68), color=DARK_GRAY)

    # Relative branch.
    box(ax, (0.045, 0.40), (0.20, 0.09), "REL branch\nfull sequence + state encoder", fc="#EAF8F8", ec=TEAL, lw=1.8)
    box(ax, (0.045, 0.27), (0.20, 0.08), "Flow Matching DiT-B\n16 layers", fc="#F2FBFB", ec=TEAL, lw=1.5)
    box(ax, (0.045, 0.15), (0.20, 0.07), "$\\Delta a_t$\nlocal tangent command", fc="#EAF8F8", ec=TEAL, lw=1.8, weight="bold")
    arrow(ax, (0.22, 0.58), (0.145, 0.49), color=TEAL)
    arrow(ax, (0.145, 0.40), (0.145, 0.35), color=TEAL)
    arrow(ax, (0.145, 0.27), (0.145, 0.22), color=TEAL)

    # Absolute branch.
    box(ax, (0.35, 0.40), (0.20, 0.09), "ABS branch\nstate-masked tokens", fc="#FFF6E7", ec=AMBER, lw=1.8)
    box(ax, (0.35, 0.28), (0.20, 0.075), "Query pooling\n$16$ condition tokens", fc="#FFF9EF", ec=AMBER, lw=1.5)
    box(ax, (0.35, 0.18), (0.20, 0.065), "RVQ discrete atlas\n$3 \\times 512$ codebooks", fc="#FFF6E7", ec=AMBER, lw=1.8, weight="bold")
    box(ax, (0.35, 0.075), (0.20, 0.065), "CFG DiT-B, stateless\n$W_t$ manifold waypoint", fc="#FFF6E7", ec=AMBER, lw=1.8)
    arrow(ax, (0.36, 0.58), (0.45, 0.49), color=AMBER)
    arrow(ax, (0.45, 0.40), (0.45, 0.355), color=AMBER)
    arrow(ax, (0.45, 0.28), (0.45, 0.245), color=AMBER)
    arrow(ax, (0.45, 0.18), (0.45, 0.14), color=AMBER)

    # Manifold visual.
    ax.text(0.74, 0.78, "Closed-loop manifold alignment", fontsize=12.5, color=CHARCOAL, fontweight="bold", ha="center")
    manifold_curve(ax, TEAL, yoff=0.38, label="tangent field")
    manifold_curve(ax, AMBER, yoff=0.24)
    arrow(ax, (0.82, 0.46), (0.76, 0.61), color=AMBER, lw=2.0, rad=-0.12, ms=16)
    ax.scatter([0.84], [0.44], s=85, color="#FFFFFF", edgecolor=PURPLE, linewidth=2.2, zorder=5)
    ax.text(0.84, 0.405, "live pose\n$p_t$", ha="center", va="top", fontsize=8.5, color=PURPLE)

    # Alignment boxes.
    box(ax, (0.62, 0.30), (0.25, 0.095), "$c_t = (W_t - p_t) / \\sigma_a$\nmanifold projection", fc="#FFF6E7", ec=AMBER, lw=1.5, fs=8.4)
    box(ax, (0.63, 0.18), (0.23, 0.08), "$D_t = \\|c_t - \\Delta a_t\\|$\ntangent-projection disagreement", fc="#F8F7FF", ec=PURPLE, lw=1.7, weight="bold")
    box(ax, (0.63, 0.065), (0.23, 0.075), "$\\alpha_t = \\sigma(k(D_t + \\lambda S_t - \\tau))$\nsoft fusion gate", fc="#F8F7FF", ec=PURPLE, lw=1.7)

    box(ax, (0.78, 0.83), (0.17, 0.065), "$w_t \\downarrow$ when OOD grows\nconservative CFG", fc="#FFF9EF", ec=AMBER, lw=1.4, fs=8.7)

    # Connections to alignment.
    arrow(ax, (0.245, 0.185), (0.63, 0.22), color=TEAL, rad=0.08, lw=1.8)
    arrow(ax, (0.55, 0.105), (0.63, 0.34), color=AMBER, rad=0.18, lw=1.8)
    arrow(ax, (0.745, 0.30), (0.745, 0.26), color=PURPLE, lw=1.5)
    arrow(ax, (0.745, 0.18), (0.745, 0.14), color=PURPLE, lw=1.5)
    arrow(ax, (0.86, 0.102), (0.94, 0.102), color=PURPLE, lw=1.8)
    box(ax, (0.90, 0.065), (0.08, 0.075), "$a_t$\nexecuted", fc="white", ec=CHARCOAL, lw=1.5, weight="bold")

    # State isolation note.
    ax.plot([0.565, 0.565], [0.07, 0.51], color="#CFD8DC", lw=1.2, ls="--")
    ax.text(0.565, 0.53, "state isolation boundary", ha="center", fontsize=8.5, color=DARK_GRAY)
    ax.text(0.45, 0.028, "ABS branch never conditions on current state $s_t$; it remains a global waypoint anchor.", ha="center", fontsize=8.8, color=DARK_GRAY)

    fig.savefig(OUT / "duet_architecture.pdf", bbox_inches="tight")
    fig.savefig(OUT / "duet_architecture.png", dpi=300, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    make_architecture()
