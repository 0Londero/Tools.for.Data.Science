import matplotlib.pyplot as plt
import numpy as np
x = range(0, 20)
y = [value ** 2 for value in x]

plt.plot(x, y)
plt.xlabel ('x')
plt.ylabel ('y')
plt.annotate('Min Value', xy=(min(x),min(y)), xycoords='data')
plt.annotate('Max Value', xy=(max(x),max(y)), xycoords='data')
plt.show()

"""
def annotate(
    text: str,
    xy: tuple[float, float],
    xytext: tuple[float, float] | None = None,
    xycoords: CoordsType = "data",
    textcoords: CoordsType | None = None,
    arrowprops: dict[str, Any] | None = None,
    annotation_clip: bool | None = None,
    **kwargs,
"""