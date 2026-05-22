"""First scientific Python script."""
import numpy as np
import matplotlib.pyplot as plt


def main() -> None:
    """Plot a sine wave."""
    x = np.linspace(0, 2 * np.pi, 200)
    y = 2*np.sin(x)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x, y, label="sin(x)")
    ax.set_xlabel("x [rad]")
    ax.set_ylabel("sin(x)")
    ax.set_title("First plot")
    ax.grid(True)
    ax.legend()
    fig.savefig("sine.png", dpi=150, bbox_inches="tight")
    plt.show()

if __name__ == "__main__":
    main()