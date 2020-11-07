# Since I don't know beautiful soup very well, this was much easier for me to do quickly :)

s = '''<li class="column1"><a href="/returns/ballot-measures/county/alameda">Alameda</a></li>
        <li class="column1"><a href="/returns/ballot-measures/county/alpine">Alpine</a></li>
        <li class="column1"><a href="/returns/ballot-measures/county/amador">Amador</a></li>
        <li class="column1"><a href="/returns/ballot-measures/county/butte">Butte</a></li>
        <li class="column1"><a href="/returns/ballot-measures/county/calaveras">Calaveras</a></li>
        <li class="column1"><a href="/returns/ballot-measures/county/colusa">Colusa</a></li>
        <li class="column1"><a href="/returns/ballot-measures/county/contra-costa">Contra Costa</a></li>
        <li class="column1"><a href="/returns/ballot-measures/county/del-norte">Del Norte</a></li>
        <li class="column1"><a href="/returns/ballot-measures/county/el-dorado">El Dorado</a></li>
        <li class="column1"><a href="/returns/ballot-measures/county/fresno">Fresno</a></li>
        <li class="column1"><a href="/returns/ballot-measures/county/glenn">Glenn</a></li>
        <li class="column2 reset12"><a href="/returns/ballot-measures/county/humboldt">Humboldt</a></li>
        <li class="column2"><a href="/returns/ballot-measures/county/imperial">Imperial</a></li>
        <li class="column2"><a href="/returns/ballot-measures/county/inyo">Inyo</a></li>
        <li class="column2"><a href="/returns/ballot-measures/county/kern">Kern</a></li>
        <li class="column2"><a href="/returns/ballot-measures/county/kings">Kings</a></li>
        <li class="column2"><a href="/returns/ballot-measures/county/lake">Lake</a></li>
        <li class="column2"><a href="/returns/ballot-measures/county/lassen">Lassen</a></li>
        <li class="column2"><a href="/returns/ballot-measures/county/los-angeles">Los Angeles</a></li>
        <li class="column2"><a href="/returns/ballot-measures/county/madera">Madera</a></li>
        <li class="column2"><a href="/returns/ballot-measures/county/marin">Marin</a></li>
        <li class="column2"><a href="/returns/ballot-measures/county/mariposa">Mariposa</a></li>
        <li class="column2"><a href="/returns/ballot-measures/county/mendocino">Mendocino</a></li>
        <li class="column3 reset12"><a href="/returns/ballot-measures/county/merced">Merced</a></li>
        <li class="column3"><a href="/returns/ballot-measures/county/modoc">Modoc</a></li>
        <li class="column3"><a href="/returns/ballot-measures/county/mono">Mono</a></li>
        <li class="column3"><a href="/returns/ballot-measures/county/monterey">Monterey</a></li>
        <li class="column3"><a href="/returns/ballot-measures/county/napa">Napa</a></li>
        <li class="column3"><a href="/returns/ballot-measures/county/nevada">Nevada</a></li>
        <li class="column3"><a href="/returns/ballot-measures/county/orange">Orange</a></li>
        <li class="column3"><a href="/returns/ballot-measures/county/placer">Placer</a></li>
        <li class="column3"><a href="/returns/ballot-measures/county/plumas">Plumas</a></li>
        <li class="column3"><a href="/returns/ballot-measures/county/riverside">Riverside</a></li>
        <li class="column3"><a href="/returns/ballot-measures/county/sacramento">Sacramento</a></li>
        <li class="column3"><a href="/returns/ballot-measures/county/san-benito">San Benito</a></li>
        <li class="column4 reset12"><a href="/returns/ballot-measures/county/san-bernardino">San Bernardino</a></li>
        <li class="column4"><a href="/returns/ballot-measures/county/san-diego">San Diego</a></li>
        <li class="column4"><a href="/returns/ballot-measures/county/san-francisco">San Francisco</a></li>
        <li class="column4"><a href="/returns/ballot-measures/county/san-joaquin">San Joaquin</a></li>
        <li class="column4"><a href="/returns/ballot-measures/county/san-luis-obispo">San Luis Obispo</a></li>
        <li class="column4"><a href="/returns/ballot-measures/county/san-mateo">San Mateo</a></li>
        <li class="column4"><a href="/returns/ballot-measures/county/santa-barbara">Santa Barbara</a></li>
        <li class="column4"><a href="/returns/ballot-measures/county/santa-clara">Santa Clara</a></li>
        <li class="column4"><a href="/returns/ballot-measures/county/santa-cruz">Santa Cruz</a></li>
        <li class="column4"><a href="/returns/ballot-measures/county/shasta">Shasta</a></li>
        <li class="column4"><a href="/returns/ballot-measures/county/sierra">Sierra</a></li>
        <li class="column4"><a href="/returns/ballot-measures/county/siskiyou">Siskiyou</a></li>
        <li class="column5 reset12"><a href="/returns/ballot-measures/county/solano">Solano</a></li>
        <li class="column5"><a href="/returns/ballot-measures/county/sonoma">Sonoma</a></li>
        <li class="column5"><a href="/returns/ballot-measures/county/stanislaus">Stanislaus</a></li>
        <li class="column5"><a href="/returns/ballot-measures/county/sutter">Sutter</a></li>
        <li class="column5"><a href="/returns/ballot-measures/county/tehama">Tehama</a></li>
        <li class="column5"><a href="/returns/ballot-measures/county/trinity">Trinity</a></li>
        <li class="column5"><a href="/returns/ballot-measures/county/tulare">Tulare</a></li>
        <li class="column5"><a href="/returns/ballot-measures/county/tuolumne">Tuolumne</a></li>
        <li class="column5"><a href="/returns/ballot-measures/county/ventura">Ventura</a></li>
        <li class="column5"><a href="/returns/ballot-measures/county/yolo">Yolo</a></li>
        <li class="column5"><a href="/returns/ballot-measures/county/yuba">Yuba</a></li>'''

url_start = 'https://electionresults.sos.ca.gov'
d = {}
for line in s.split('\n'):
    line = line.strip()
    url_end = line.split('"')[3]
    county_name = line.split('>')[-3].split('<')[0]
    d[county_name] = url_start+url_end
print(d)
