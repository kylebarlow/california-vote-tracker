import os
import glob
import pandas as pd
import plotly.express as px


csv_output_path = 'csv_data'
html_output_path = 'output_html'

if not os.path.isdir(html_output_path):
    os.makedirs(html_output_path)

prop_summary = pd.read_csv( os.path.join(csv_output_path, 'proposition_summary.csv') )
prop_summary = prop_summary.sort_values(['Fetch Time', 'Proposition Number', 'County'])
state_prop_cols = ['Proposition Number', 'Proposition Title', 'State - Yes Votes', 'State - No Votes']
state_prop_summary = prop_summary[ state_prop_cols + ['Fetch Time'] ].drop_duplicates(state_prop_cols)

state_prop_summary['Total'] = state_prop_summary['State - Yes Votes'] + state_prop_summary['State - No Votes']
state_prop_summary['Yes %'] = state_prop_summary['State - Yes Votes'] / state_prop_summary['Total']

# Merge in which counties reported new data
new_counties = prop_summary.drop_duplicates(['Proposition Number', 'Proposition Title', 'Yes Votes', 'No Votes', 'County'])
new_counties = new_counties[ state_prop_cols + ['County'] ].groupby( state_prop_cols ).agg({
    'County' : lambda x: '<br>'.join(x),
}).reset_index()
print(new_counties.tail(n=10))
state_prop_summary = state_prop_summary.merge(new_counties, how = 'left', on = state_prop_cols)

# Rename columns for display
state_prop_summary = state_prop_summary.rename( columns = {
    'State - Yes Votes' : 'Yes', 'State - No Votes':'No',
    'Fetch Time' : 'Fetch Time (PST)',
    'County' : 'Counties reporting new data',
} )
print(state_prop_summary.head())

fig = px.line(
    state_prop_summary, x="Fetch Time (PST)", y="Yes %", color="Proposition Number",
    line_group="Proposition Number", hover_name="Proposition Number",
    template='plotly_white',
    hover_data=['Yes', 'No', 'Total', 'Counties reporting new data'],
)
fig.write_html( os.path.join(html_output_path, 'props.html') )