from bokeh.plotting import figure, output_file, show 
from motion_detection import df 
      
f= figure(x_axis_type='datetime',height=100,width=500,sizing_mode="scale_both",title='Motion_Graph') 
f.yaxis.minor_tick_line_color=None 
f.yaxis[0].ticker.desired_num_ticks=1 
c=f.quad(left=df['Start'], right=df['End'], bottom=0, top=1, color='red') 
      
output_file('Motion_detector_graph.html') 
show(f)