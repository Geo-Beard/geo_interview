import matplotlib.pyplot as plt
import welly


project = welly.read_las('data/WA1.las')

well = project[0]

tracks = ['M__DEPTH',
          'SP',
          'GR',
          'CALI',
          'BitSize',
          'LL8',
          'ILM',
          'ILD',
          'RHOB',
          'NPHI',
          'DT',
          'MudWgt']

# Build alt_tracks after trying to find issues with multiplot
alt_tracks = ['M__DEPTH',
              'SP',
              'GR',
              'CALI',
              'LL8',
              'ILM',
              'ILD',
              'RHOB',
              'NPHI',
              'DT']

# Still not plotting with alt_tracks
well.plot(tracks=alt_tracks)

# gr = well.data['GR']
# gr.plot()

# Check all logs plot individually (issues with BitSize and MudWgt)
# for log in tracks:
#     if log == 'BitSize':
#         continue
#     if log == 'MudWgt':
#         continue
#     if log != 'M__DEPTH':
#         log_to_plot = well.data[log]
#         log_to_plot.plot()

plt.savefig('output/welly_fig.png')
plt.show()
