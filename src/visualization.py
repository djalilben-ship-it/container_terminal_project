import matplotlib.pyplot as plt

def plot_equipment(current, required, label):
    plt.bar(["Current", "Required"], [current, required])
    plt.title(f"{label} Comparison")
    plt.show()
