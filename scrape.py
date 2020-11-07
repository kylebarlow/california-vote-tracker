import os
import datetime
import time
import random
import pandas as pd
from tqdm import tqdm
import glob

statewide_ballot_url = 'https://electionresults.sos.ca.gov/returns/ballot-measures'

county_urls = {'Alameda': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/alameda', 'Alpine': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/alpine', 'Amador': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/amador', 'Butte': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/butte', 'Calaveras': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/calaveras', 'Colusa': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/colusa', 'Contra Costa': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/contra-costa', 'Del Norte': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/del-norte', 'El Dorado': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/el-dorado', 'Fresno': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/fresno', 'Glenn': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/glenn', 'Humboldt': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/humboldt', 'Imperial': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/imperial', 'Inyo': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/inyo', 'Kern': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/kern', 'Kings': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/kings', 'Lake': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/lake', 'Lassen': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/lassen', 'Los Angeles': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/los-angeles', 'Madera': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/madera', 'Marin': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/marin', 'Mariposa': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/mariposa', 'Mendocino': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/mendocino', 'Merced': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/merced', 'Modoc': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/modoc', 'Mono': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/mono', 'Monterey': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/monterey', 'Napa': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/napa', 'Nevada': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/nevada', 'Orange': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/orange', 'Placer': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/placer', 'Plumas': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/plumas', 'Riverside': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/riverside', 'Sacramento': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/sacramento', 'San Benito': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/san-benito', 'San Bernardino': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/san-bernardino', 'San Diego': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/san-diego', 'San Francisco': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/san-francisco', 'San Joaquin': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/san-joaquin', 'San Luis Obispo': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/san-luis-obispo', 'San Mateo': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/san-mateo', 'Santa Barbara': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/santa-barbara', 'Santa Clara': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/santa-clara', 'Santa Cruz': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/santa-cruz', 'Shasta': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/shasta', 'Sierra': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/sierra', 'Siskiyou': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/siskiyou', 'Solano': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/solano', 'Sonoma': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/sonoma', 'Stanislaus': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/stanislaus', 'Sutter': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/sutter', 'Tehama': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/tehama', 'Trinity': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/trinity', 'Tulare': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/tulare', 'Tuolumne': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/tuolumne', 'Ventura': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/ventura', 'Yolo': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/yolo', 'Yuba': 'https://electionresults.sos.ca.gov/returns/ballot-measures/county/yuba'}

date_format = '%Y-%m-%d-%H-%M-%S'

output_path = 'csv_data'
if not os.path.isdir(output_path):
    os.makedirs(output_path)

start_time = datetime.datetime.now()

prop_results = []
pres_results = []

try:
    for county_name, county_prop_results_url in tqdm(county_urls.items()):
        county_prop_results = pd.read_html(county_prop_results_url)
        assert( len(county_prop_results) == 1 )
        county_prop_results = county_prop_results[0]
        county_prop_results.columns = county_prop_results.columns.droplevel()
        county_prop_results.columns = [
            'Currently Passing?',
            'Proposition Number',
            'Proposition Title',
            'Yes Votes',
            'Yes %',
            'No Votes',
            'No %',
            'State - Yes Votes',
            'State - Yes %',
            'State - No Votes',
            'State - No %',
        ]
        county_prop_results.loc[ county_prop_results['Currently Passing?'].str.strip().str.lower() == 'yes', 'Currently Passing?' ] = True
        county_prop_results.loc[ county_prop_results['Currently Passing?'].str.strip().str.lower() == 'no', 'Currently Passing?' ] = False
        for col in ['Yes %', 'No %', 'State - Yes %', 'State - No %']:
            county_prop_results[col] = county_prop_results[col].str[:-1].astype(float) / 100.0
        county_prop_results['County'] = county_name
        county_prop_results['Fetch Time'] = datetime.datetime.now().strftime(date_format)
        prop_results.append( county_prop_results )

        time.sleep( 1 )

        county_pres_results_url = 'https://electionresults.sos.ca.gov/returns/president/county/' + os.path.basename(county_prop_results_url)
        county_pres_results = pd.read_html(county_pres_results_url)
        assert( len(county_pres_results) == 1 )
        county_pres_results = county_pres_results[0]
        county_pres_results.columns = [
            'Incumbent?',
            'Candidate',
            'Votes',
            '%',
            'State - Votes',
            'State - %',
        ]
        county_pres_results.loc[ ~county_pres_results['Incumbent?'].isna(), 'Incumbent?' ] = True
        county_pres_results.loc[ county_pres_results['Incumbent?'].isna(), 'Incumbent?' ] = False
        for col in ['%', 'State - %']:
            county_pres_results[col] = county_pres_results[col].str[:-1].astype(float) / 100.0
        county_pres_results['County'] = county_name
        county_pres_results['Fetch Time'] = datetime.datetime.now().strftime(date_format)
        pres_results.append(county_pres_results)

        time.sleep( 1 )
        
    prop_results = pd.concat( prop_results, ignore_index = True, sort = False )
    pres_results = pd.concat( pres_results, ignore_index = True, sort = False )

    end_time = datetime.datetime.now()

    date_str = '%s_%s' % ( start_time.strftime(date_format), end_time.strftime(date_format) )

    prop_results.to_csv( os.path.join(output_path, 'prop_%s.csv' % date_str), index=False )
    pres_results.to_csv( os.path.join(output_path, 'pres_%s.csv' % date_str), index=False )

    pres_csv_paths = glob.glob( os.path.join(output_path, 'pres_*.csv') )
    prop_csv_paths = glob.glob( os.path.join(output_path, 'prop_*.csv') )

    print( 'Found %d total presidential result CSVs and %d total proposition result CSVs' % (len(pres_csv_paths), len(prop_csv_paths)) )

    pres = [ pd.read_csv(p) for p in pres_csv_paths ]
    prop = [ pd.read_csv(p) for p in prop_csv_paths ]

    for df_type, df in [('president', pres), ('proposition', prop)]:
        df = pd.concat(df, ignore_index=True, sort=False)
        df['Fetch Time'] = pd.to_datetime( df['Fetch Time'], format=date_format )
        # Sort by every column (interesting ones first) to prevent unnecessary git diffs
        df = df.sort_values(
            ['Fetch Time', 'County'] + [x for x in df.columns if x not in ['Fetch Time', 'County']]
        )
        df = df.drop_duplicates([x for x in df.columns if x != 'Fetch Time'])
        df.to_csv( os.path.join(output_path, '%s_summary.csv' % df_type), index=False )

except Exception as e:
    with open(os.path.join(output_path, '%s-error.txt' % datetime.datetime.now().strftime(date_format)), 'w' ) as f:
        f.write(str(e))