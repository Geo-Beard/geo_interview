from welly import Well
from welly import Curve
import matplotlib.pyplot as plt

well = Well.from_las('data/WA1.las')

tracks = ['M__DEPTH',
          'SP',
          'GR',
          'CALI',
          ['LL8', 'ILM', 'ILD'],
          ['RHOB', 'NPHI'],
          'DT']

well.plot(tracks=tracks)
plt.ylim(0, 3666)
plt.show()
